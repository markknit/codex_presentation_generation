#!/usr/bin/env python3
"""Build one explicitly authored lesson in the organised curriculum set.

Specs are source-specific editorial work, not automatic source-text dumps.
CPU-only PPTX/vector/DOCX assembly; the separate renderer verifies CUDA.
"""
import argparse
import hashlib
import json
import re
import shutil
import textwrap
from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt
from docx.oxml import OxmlElement
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches as PI, Pt as PP

from curriculum_set_inventory import ROOT, CONTROL, unit_paths, digest, slug
from session_usage import latest_usage
from lesson_visuals import VisualDeck, tx, box, oval, badge, timer, question, steps, arrow, line, table, COL, INK, MUTED, CREAM, A, note

PHASES=list(COL)


def card(path,code,suffix):
    doc=Document(next(path.glob('*_'+suffix+'.docx')))
    ps=[p.text for p in doc.paragraphs]
    start=next((i for i,t in enumerate(ps) if t.startswith(code+' —')),None)
    if start is None:return []
    end=next((i for i in range(start+1,len(ps)) if re.match(r'^[A-Z]+\d+\s+—',ps[i])),len(ps))
    return [t for t in ps[start:end] if t.strip()]


def visual(slide,spec,phase):
    kind=spec.get('kind','bullets')
    if kind=='bullets':
        steps(slide,spec['items'],y=2.32,dy=1.02,w=11.7,size=25,c=COL.get(phase,'47C6E4'))
    elif kind=='question':question(slide,spec['text'],phase,size=31)
    elif kind=='cards':
        values=spec['values']
        cols=5 if len(values)>8 else (2 if max(map(len,values))>16 else min(4,len(values)))
        w=(11.9-.18*(cols-1))/cols
        for i,value in enumerate(values):
            x=.72+(i%cols)*(w+.18);y=2.45+(i//cols)*1.3
            box(slide,x,y,w,1.12,CREAM)
            tx(slide,value,x+.15,y+.2,w-.3,.78,28,INK,True,A.CENTER)
    elif kind=='equation':
        box(slide,.75,2.45,11.8,1.7,CREAM)
        tx(slide,spec['text'],1.0,2.85,11.3,1.0,36,INK,True,A.CENTER)
    elif kind=='table':
        table(slide,spec['headers'],spec['rows'],.75,2.28,11.8,spec.get('height',3.5),spec.get('widths'),spec.get('size',21))
    elif kind=='columns':
        for i,col in enumerate(spec['columns']):
            x=.75+i*6.05;box(slide,x,2.4,5.75,3.5,CREAM)
            tx(slide,col[0],x+.22,2.65,5.3,.5,20,INK,True)
            tx(slide,col[1],x+.22,3.4,5.3,2.0,26)
    elif kind=='flow':
        nodes=spec['nodes'];w=(11.8-.35*(len(nodes)-1))/len(nodes)
        for i,value in enumerate(nodes):
            x=.75+i*(w+.35);box(slide,x,2.75,w,1.65,CREAM)
            tx(slide,value,x+.13,3.08,w-.26,1.12,23,INK,True,A.CENTER)
            if i<len(nodes)-1:arrow(slide,x+w+.06,3.4,.23,COL.get(phase,'CF128C'))
    elif kind=='numberline':
        lo,hi=spec['bounds'];left=.95;width=11.25;y=3.7
        line(slide,left,y,left+width,y,INK,2)
        for value,label in spec['points']:
            x=left+(value-lo)/(hi-lo)*width
            line(slide,x,y-.12,x,y+.12,INK,2);oval(slide,x-.045,y-.045,.09,.09,'CF128C')
            tx(slide,label,x-.55,y+.35,1.1,.6,22,INK,True,A.CENTER)
    elif kind=='bars':
        data=CategoryChartData();data.categories=spec['categories']
        for name,values in spec['series']:data.add_series(name,values)
        chart=slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED,PI(.9),PI(2.2),PI(11.5),PI(3.75),data).chart
        chart.has_legend=len(spec['series'])>1
        chart.value_axis.has_title=True;chart.value_axis.axis_title.text_frame.text=spec['axis']
        chart.category_axis.has_title=True;chart.category_axis.axis_title.text_frame.text=spec.get('category_axis','')
        chart.chart_style=10
        for axis in [chart.value_axis,chart.category_axis]:
            axis.tick_labels.font.name='Calibri';axis.tick_labels.font.size=PP(16)
            for p in axis.axis_title.text_frame.paragraphs:
                p.font.name='Calibri';p.font.size=PP(16)
                for r in p.runs:r.font.name='Calibri';r.font.size=PP(16)
    else:raise ValueError(kind)
    if spec.get('caption'):
        tx(slide,spec['caption'],.8,6.0,9.5,.7,19,MUTED)
    if spec.get('timer'):
        timer(slide,spec['timer'],spec.get('mode','work time'))


class Lesson:
    def __init__(self,module,number):
        self.inventory=json.loads((CONTROL/'inventory.json').read_text())
        self.u=next(u for u in self.inventory['units'] if u['module']==module)
        self.path=Path(self.u['source_folder']);self.paths=unit_paths(self.u)
        for p in self.paths.values():p.mkdir(parents=True,exist_ok=True)
        for f,h in self.u['source_hashes'].items():assert digest(self.path/f)==h,(module,f)
        self.data=json.loads(next(self.path.glob('*_data.json')).read_text())
        self.l=self.data['LESSONS'][number-1];self.n=number
        specfile=CONTROL/'specs'/(module+'.json')
        self.unit_spec=json.loads(specfile.read_text())
        self.spec=self.unit_spec['lessons'][str(number)]
        self.anchor=self.unit_spec['anchor_line']
        self.code=self.spec['code'];self.assessment=self.spec.get('assessment',False)
        self.math='Mathematics' in self.u['subject']
        self.cards=card(self.path,self.code,'AssessmentMaterials' if self.assessment else 'StudentMaterials')
        assert self.cards,(module,number,self.code)
        raw=card(self.path,self.code,'MaterialsTeacherKey')
        start=raw.index('Teacher key and preparation') if 'Teacher key and preparation' in raw else -1
        self.key='\n'.join(raw[start+1:]) if start>=0 else '\n'.join(raw)
        if self.assessment:self.key+='\n'+'\n'.join(s['exemplar'] for s in self.data['FINAL_EXPLANATION']['sections'])
        short={'Core Mathematics':'CoreMath','Essential Mathematics':'EssMath','General Science':'GenSci'}[self.u['subject']]
        self.name=f'{short}_G10_SS{self.u["module"].split("_")[1]}_{self.u["module"].split("_")[2]}_L{number:02}_{slug(self.spec["short"])}'
        self.b=VisualDeck(number,self.name,subject=self.u['subject'],unit=self.u['topic'])
        self.totals={p:0.0 for p in PHASES};self.totals['Predict']=1
        for row in self.spec['slides']:self.totals[row['phase']]+=row['minutes']
        self.totals['Model Building']+=0 if self.assessment else 1
        assert abs(sum(self.totals.values())-40)<1e-6,self.totals
        self.seen=set()

    def slide(self,title,phase,minutes,do,*,key=None,say='',look='',iff='',hidden=False,check=False,**kw):
        first=''
        if phase in PHASES and phase not in self.seen:
            self.seen.add(phase);first=f'{phase.upper()} PHASE ({self.totals[phase]:g} minutes total)'
        notes=note(minutes,do,say=say,look=look,iff=iff,key=key or self.key,
                   science=f'Source: {self.u["module"]}, Lesson {self.n}, {self.code}. '+kw.pop('background',''),
                   phase_note=first,**kw)
        if self.math:notes=notes.replace('SCIENCE NOTE FOR YOU','MATHEMATICS NOTE FOR YOU')
        return self.b.slide(title,phase,notes,hidden=hidden,check=check)

    def opening(self):
        s=self.slide(self.l['title'],'Predict',.25,'Introduce today’s source question without supplying its answer.',
            purpose=self.l['slo']['purpose']+' '+self.l['slo']['purposeInStoryline'],
            before='Read the complete unit and task/key before class. Print the supplied student task and keep teacher keys private. '
                   +self.spec.get('preparation','Notebooks, pencils, second colour, board, timer and source task per learner. ')
                   +' '+self.l['slo']['safetyNotes']+' '
                   +('Independent assessment: no teaching examples or peer discussion before collection.' if self.assessment else 'Do not show Explain slides until individual evidence is recorded.'),
            background='Anchor: '+self.data['UNIT']['phenomenon'],key='Title introduces the investigation; no answer is endorsed.')
        tx(s,f'{self.u["subject"]} · Grade 10 · {self.u["topic"]}',.75,2.35,11.7,.55,24,INK,True)
        question(s,self.l['slo']['keyInquiry'],'Predict',y=3.2,size=30)
        tx(s,f'LESSON {self.n} OF {len(self.data["LESSONS"])} · 40 MINUTES · REVIEW DRAFT',.8,5.1,11.5,.4,18,MUTED,True)
        tx(s,self.anchor,.8,5.62,11.5,.4,18,INK,True)
        for i,(p,c) in enumerate(COL.items()):
            x=.8+(i%3)*4.0;y=6.15+(i//3)*.43;oval(s,x,y,.15,.15,c);tx(s,p,x+.25,y-.015,3.6,.28,12,INK,True)
        s=self.slide('How to use this lesson','Routine',0,
            'Teacher only. Use Presenter View. Notes follow TIME, DO, SAY, WAIT TIME, LOOK FOR, IF…, WHY THIS WORKS, ANSWER KEY, '
            +('MATHEMATICS' if self.math else 'SCIENCE')+' NOTE FOR YOU and TEACHER REFLECTION. '
            +('This assessment retains phase names only as scheduling tags; give no hints or peer comparison before collection.' if self.assessment else 'Keep predictions, individual evidence and explanations in that order. Do not correct initial ideas.'),hidden=True)
        steps(s,['Read the ordered notes in Presenter View.','Keep teacher keys private.',
                 'Independent work only until collection.' if self.assessment else 'Use the source’s individual and comparison stages.'],dy=1.1,size=25)
        s=self.slide('Lesson at a glance','Glance',0,
            self.spec.get('preparation','Source task per learner; notebooks, pencils, second colour, board and timer.')
            +' '+self.spec.get('route','Follow the supplied paper task. No practical or media is required.')
            +' Source-specific resource fallback is a search URL, not verified matched media. Preview first; retain offline print route.',hidden=True)
        table(s,['Phase','min','Source focus'],[[p,str(int(self.totals[p])),textwrap.shorten(self.data['LESSONS'][self.n-1]['framework'][i]['learnerExperience'],width=66,placeholder='…')] for i,p in enumerate(PHASES)],
              .75,2.25,11.8,3.45,[3.0,.7,8.1],16)
        tx(s,self.spec.get('glance','Print the task. Keep the key private. Prepare board, timer and a second colour.'),.8,5.95,8.8,.65,18)
        link=self.l['resourceLinks']['predict'].get('fallback_search_url')
        if link:
            sh=box(s,9.7,6.1,2.8,.55,INK);sh.click_action.hyperlink.address=link
            sh=tx(s,'ARES · preview first',9.82,6.27,2.55,.25,12,'FFFFFF',True);sh.click_action.hyperlink.address=link
        s=self.slide('Our unit journey','Unit map',.25,
            'Read lesson titles and the driving question only. Do not explain future tasks. Link yesterday’s source evidence to today’s question.',
            key='The unit map locates the lesson; it does not add a new assessed task.')
        lessons=self.data['LESSONS'];rows=(len(lessons)+1)//2
        dy=min(.61,3.8/rows)
        for i,l in enumerate(lessons):
            x=.75+(i//rows)*6.0;y=2.15+(i%rows)*dy
            box(s,x,y,5.8,dy-.05,'D7DF23' if l['number']==self.n else 'F0F4F4')
            tx(s,f'{l["number"]}. {l["title"]}',x+.12,y+.06,5.56,dy-.1,13,INK,l['number']==self.n)
        tx(s,f'YOU ARE HERE: Lesson {self.n} · So far: '+('we begin with an untested claim.' if self.n==1 else 'retain the evidence and questions from earlier lessons.'),.8,6.08,11.5,.3,14,MUTED,True)
        tx(s,self.data['UNIT']['drivingQuestion'],.8,6.48,11.6,.52,15,INK,True)
        s=self.slide('By the end of this lesson you can…','Today',.5,
            'Read goals as intended actions without revealing task outcomes. Working words support access; introduce scientific/mathematical result definitions only at the source-specified stage.',
            key='Use later individual work to check these intentions.')
        steps(s,self.spec['goals'],dy=1.08,w=8.0,size=25)
        box(s,9.3,2.35,3.15,3.55,CREAM)
        tx(s,'WORKING WORDS',9.5,2.58,2.75,.4,15,INK,True)
        tx(s,self.spec.get('words','evidence: information that supports a claim\n\nreason: how evidence supports the claim'),9.5,3.18,2.75,2.4,19)

    def build(self):
        self.opening()
        for row in self.spec['slides']:
            p=row['phase'];framework=self.l['framework'][PHASES.index(p)]
            do=row.get('do',framework['teacherMoves']+' '+framework['learnerExperience'])
            do+=' '+('Do not coach mathematical/scientific answers or permit comparison before collection.' if self.assessment else 'Keep an individual record; retain earlier ideas and use a new colour for justified revisions.')
            if self.assessment:
                look='Check access, independent working and completion; record actual device action separately if supplied. '+framework['formativeAssessment']
                iff='If a procedure is unclear, reread that instruction without interpreting the mathematics/science. Record absent equipment or unobserved device use honestly.'
            else:
                look=row.get('look','Scan five individual records and hear two contrasting reasons. '+framework['formativeAssessment'])
                iff=row.get('if','If a claim lacks support, ask: “Which entry, representation or observation supports that?” Return to the source task without announcing a result.')
            s=self.slide(row['title'],p,row['minutes'],do,say=row.get('say','Read the task, record your evidence and give a reason.'),
                         look=look,iff=iff,check=True,key=row.get('key',self.key),why=framework['sensemakingStrategy'],
                         wait=row.get('wait','Keep the stated individual writing time; allow 5–15 seconds after oral questions.'),
                         background=row.get('background',''))
            visual(s,row,p)
        duration=0 if self.assessment else 1
        summary=self.l['summaryTablePrompt'];key='\n'.join(f'{k}: {v}' for k,v in summary.items())
        s=self.slide('Summary Table','Model Building',duration,
            'Collect all independent assessment work before any answer discussion. Use the source key privately to plan later feedback.' if self.assessment else 'Learners complete their own three summary columns. Link the source evidence back to the unit anchor.',
            key=key,reflection='Which individual responses show the target misconception? Who needs support? Were source timings realistic? Which question or access issue remains open?',
            look='Confirm individual work is collected and retain questions for later feedback.' if self.assessment else 'Scan five records for specific evidence and an appropriately bounded connection.',
            iff='If work is incomplete, record the missing evidence; plan accessible follow-up without inventing a result.',check=True)
        if self.assessment:
            question(s,'Submit all work before we discuss any answers.','Model Building')
            tx(s,'Feedback follows the evidence in your own work.',.9,4.65,11.0,.8,27)
        else:
            for i,t in enumerate(['What did I observe?','What did I learn?','How does this explain\nour unit phenomenon?']):
                x=.75+i*4.0;badge(s,str(i+1),x,2.5,list(COL.values())[i],.55);tx(s,t,x,3.5,3.6,1.6,27)
            tx(s,self.anchor,.8,5.6,11.5,.5,18,MUTED)
        if self.n<len(self.data['LESSONS']):tx(s,'Next lesson: '+self.data['LESSONS'][self.n]['title'],.8,6.35,11.7,.5,19,INK,True)
        assert abs(sum(r['minutes'] for r in self.b.records)-40)<1e-6
        self.b.deck.core_properties.title=self.l['title']
        self.b.save(self.paths['output']/'presentations')
        manifest=ROOT/'qa'/(self.name+'_manifest.json')
        manifest.rename(self.paths['qa']/(self.name+'_manifest.json'))
        self.support()
        report={'module':self.u['module'],'lesson':self.n,'name':self.name,'source_code':self.code,
                'spec_sha256':hashlib.sha256(json.dumps({'lesson':self.spec,'anchor':self.anchor},sort_keys=True,ensure_ascii=False).encode()).hexdigest(),
                'spec_scope':'Canonical JSON for this lesson and its shared anchor line',
                'source_hashes':self.u['source_hashes'],'source_archive_sha256':self.u['source_archive_sha256'],
                'phase_minutes':self.totals,'assessment':self.assessment,'status':'built; rendering and visual review pending',
                'notes':'CPU assembly; no GPU processing claimed until separate render report.'}
        (self.paths['qa']/(self.name+'_sources.json')).write_text(json.dumps(report,indent=2,ensure_ascii=False))
        self.u['lessons'][self.n-1].update({'status':'built_pending_review','name':self.name,
            'deck':str((self.paths['output']/'presentations'/(self.name+'.pptx')).relative_to(ROOT)),
            'qa_folder':str(self.paths['qa'].relative_to(ROOT))})
        (CONTROL/'inventory.json').write_text(json.dumps(self.inventory,indent=2,ensure_ascii=False))
        return self.name

    def support(self):
        student=Document();sec=student.sections[0];sec.top_margin=sec.bottom_margin=Inches(.6)
        sec.left_margin=sec.right_margin=Inches(.65)
        student.styles['Normal'].font.name='Calibri';student.styles['Normal'].font.size=Pt(11)
        student.add_heading(f'{self.u["subject"]} · Grade 10 · Lesson {self.n}',0)
        student.add_paragraph('Name: ______________________  Class: __________  Date: __________')
        for i,t in enumerate(self.cards):
            if i==0:student.add_heading(t,1)
            else:student.add_paragraph(t)
        if self.spec.get('record'):
            r=self.spec['record'];t=student.add_table(rows=1,cols=len(r['headers']));t.style='Table Grid'
            for c,h in zip(t.rows[0].cells,r['headers']):c.text=h
            for row in r['rows']:
                rr=t.add_row();rr.height=Inches(.43)
                for c,value in zip(rr.cells,row):c.text=str(value)
            for row in t.rows:
                row._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
            t.rows[0]._tr.get_or_add_trPr().append(OxmlElement('w:tblHeader'))
        if not self.assessment:student.add_page_break()
        student.add_heading('Your individual working and reasons',1)
        for _ in range(6):student.add_paragraph('________________________________________________________________________________')
        if not self.assessment:
            student.add_paragraph('Keep your first idea and a justified revision in different colours. Use your notebook if you need more room.')
            student.add_heading('Summary Table',1)
            t=student.add_table(rows=2,cols=3);t.style='Table Grid'
            for c,h in zip(t.rows[0].cells,['What did I observe?','What did I learn?','Connection to the unit phenomenon']):c.text=h
            t.rows[1].height=Inches(.7)
        student.add_paragraph('© 2026 SeaVuria & ARES Education · CC BY-NC 4.0 · Review draft')
        student.save(self.paths['output']/'student_materials'/(self.name+'_Student_Task.docx'))
        if self.assessment:
            original=next(self.path.glob('*_FinalExplanation.docx'))
            shutil.copy2(original,self.paths['output']/'student_materials'/(self.name+'_Assessment_Prompts.docx'))
        teacher=Document();teacher.styles['Normal'].font.name='Calibri';teacher.styles['Normal'].font.size=Pt(10)
        teacher.add_heading(f'{self.u["subject"]} · {self.u["topic"]} · Lesson {self.n}',0)
        teacher.add_paragraph('PRIVATE TEACHER NOTES · REVIEW DRAFT · Native PowerPoint/teacher approval remains open.')
        teacher.add_heading('Complete source task key',1);teacher.add_paragraph(self.key)
        for record,slide in zip(self.b.records,self.b.deck.slides):
            teacher.add_heading(f'Slide {record["slide"]}: {record["title"]}',1)
            teacher.add_paragraph(slide.notes_slide.notes_text_frame.text)
        teacher.save(self.paths['output']/'teacher_notes'/(self.name+'_Teacher_Notes.docx'))
        log=f'''# {self.u['subject']} · {self.u['topic']} · Lesson {self.n}

Review draft. Source {self.u['module']}, {self.code}; exact source hashes and
archive verification in the matching sources report. Whole unit read before
authoring; source-specific editable slide specification is tracked in content.
One deck per lesson. Phase totals: {json.dumps(self.totals)}.

Preserve the full supplied task in the individual student sheet; concise slides
stage its work. Full teacher key stays in private notes. No future assessment
inputs are exposed in earlier lessons. {'Assessment uses independent work only and phase tags as scheduling labels; no teaching answers on student screens.' if self.assessment else 'Initial ideas remain uncorrected until evidence and comparison; model revisions retain the first record.'}

Route and authoring decisions: {self.spec.get('route','Source paper task; no practical substituted.')}
{self.spec.get('decisions','Source tasks, input values, sequence and timings are retained. Early goals name actions rather than disclose results.')}

CPU-only: PowerPoint/DOCX/vector assembly, LibreOffice conversion, PDF rasterisation,
file encoding/layout, text extraction and ZIP packaging. Supported raster resizing
and pixel metrics must execute on CUDA and fail rather than fall back to CPU.
Local Calibri rendering substitutes Carlito. No semantic GPU review is claimed.

Open: rendered/visual review until its report is written; native PowerPoint,
Presenter View, exact Calibri, teacher/source-owner science/mathematics, practical
equipment/access, real-class pacing and ARES offline/content acceptance.
No classroom release or push.
'''
        (self.paths['logs']/(self.name+'.md')).write_text(log)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('module');p.add_argument('lesson',type=int)
    p.add_argument('--support-only',action='store_true');a=p.parse_args()
    usage=latest_usage()
    if not a.support_only and (not usage['available'] or usage['remaining_percent']<=5):
        print(json.dumps(usage));raise SystemExit(75)
    lesson=Lesson(a.module,a.lesson)
    if a.support_only:
        from pptx import Presentation
        deck=lesson.paths['output']/'presentations'/(lesson.name+'.pptx');assert deck.exists()
        lesson.b.deck=Presentation(deck)
        lesson.b.records=json.loads((lesson.paths['qa']/(lesson.name+'_manifest.json')).read_text())['slides']
        lesson.support();print('Refreshed support documents without changing PPTX:',lesson.name)
    else:print(lesson.build())
