#!/usr/bin/env python3
"""Source-specific, single-lesson review pilots from the November curriculum.

CPU-only PPTX/DOCX assembly. Raster review uses the separate verified CUDA tool.
Mathematics invocation requires the recorded pilot-specific user authorisation.
"""
import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

from docx import Document
from docx.shared import Inches as DI, Pt as DP
from lesson_visuals import (VisualDeck, tx, box, oval, badge, timer, question,
                            steps, arrow, line, table, COL, INK, MUTED, CREAM, A, note)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'outputs/drafts/curriculum_pilots_2026-11'
CONFIG = {
 'science': ('General_Science', 'SS1.1_Introduction_to_General_Science', 'GenSci_G10_Introduction_L1_Scientific_Questions', 'GS11'),
 'essential': ('Essential_Mathematics', 'SS1.1_Real_Numbers', 'EssMath_G10_RealNumbers_L1_Exact_Number_Classes', 'RN1'),
 'core': ('Core_Mathematics', 'SS1.1_Real_Numbers', 'CoreMath_G10_RealNumbers_L1_Zero_Parity_and_Primes', 'CRN1'),
}
PHASES = list(COL)


def source(key):
    c,u,_,_=CONFIG[key]
    p=ROOT/'final_curriculum_outputs/outputs/v2'/c/u
    return p,json.loads(next(p.glob('*_data.json')).read_text())


def material_block(path, suffix, code):
    """Read the exact first teaching card; never include later assessment data."""
    d=Document(next(path.glob('*_'+suffix+'.docx')))
    ps=[p.text for p in d.paragraphs]
    start=next(i for i,t in enumerate(ps) if t.startswith(code+' —'))
    end=next((i for i in range(start+1,len(ps)) if ' — ' in ps[i] and ps[i].split(' — ')[0].startswith(code.rstrip('1'))),len(ps))
    return ps[start:end]


def chips(s,values,y=2.5,size=34):
    n=len(values);gap=.22;w=(11.9-gap*(n-1))/n
    for i,v in enumerate(values):
        x=.72+i*(w+gap);box(s,x,y,w,1.12,CREAM)
        tx(s,v,x+.08,y+.27,w-.16,.65,size,INK,True,A.CENTER)


def case_icon(s,kind,x,y,w=3.2):
    """Qualitative context icons, never measurements or observed photographs."""
    if kind=='A':
        oval(s,x+w*.72,y,.48,.48,'F7C759')
        box(s,x+.28,y+.66,w*.65,.67,'9BCAD5',INK)
        box(s,x+.24,y+.57,w*.68,.16,'5F9EAE')
        line(s,x+.8,y+.55,x+.8,y+.38,INK,2)
        line(s,x+.8,y+.38,x+1.35,y+.38,INK,2)
        line(s,x+1.35,y+.38,x+1.35,y+.55,INK,2)
    elif kind=='B':
        box(s,x+.2,y+.18,w*.77,1.12,'C5D5DB',INK)
        for i in range(5):line(s,x+.38+i*.43,y+.25,x+.38+i*.43,y+1.22,INK,2)
        for xx,yy in [(.7,.5),(1.5,.7),(2.1,.38)]:oval(s,x+xx,y+yy,.32,.21,'A9633F')
    else:
        box(s,x+.18,y+1.05,w*.8,.23,'AC8966')
        line(s,x+w*.47,y+.4,x+w*.47,y+1.05,'3D815E',3)
        oval(s,x+w*.47,y+.52,.58,.25,'87BA74')
        oval(s,x+w*.47-.54,y+.35,.58,.25,'87BA74')


CASES=[('A','Lunchbox','A lunchbox left in sunlight feels warmer than a similar box indoors.'),
       ('B','Metal gate','A metal gate shows reddish-brown patches after a wet season.'),
       ('C','School garden','A garden team records fewer seedlings after a dry week.')]


def cases(s,y=2.25):
    for i,(code,title,body) in enumerate(CASES):
        x=.72+i*4.06;box(s,x,y,3.82,3.95,'F0F4F4')
        badge(s,code,x+.2,y+.18,'47C6E4');tx(s,title,x+.85,y+.22,2.65,.4,20,INK,True)
        case_icon(s,code,x+.33,y+.85,3.1)
        tx(s,body,x+.22,y+2.35,3.38,1.4,21)


class Pilot:
    def __init__(self,key):
        self.key=key;self.path,self.data=source(key);self.l=self.data['LESSONS'][0]
        self.name=CONFIG[key][2];self.code=CONFIG[key][3]
        self.subject=self.data['META']['subject'];self.unit=self.data['META']['substrand_name']
        self.b=VisualDeck(1,self.name,subject=self.subject,unit=self.unit)
        self.phase_totals=[4,14 if key=='core' else 16,10,4,8 if key=='core' else 6]
        self.seen=set();self.coverage=[]
        self.card=material_block(self.path,'StudentMaterials',self.code)
        self.key_block=material_block(self.path,'MaterialsTeacherKey',self.code)

    def slide(self,title,phase,t,do,*,say='',key='',look='',iff='',why='',wait='',sub='',check=False,**kw):
        if phase in PHASES and phase not in self.seen:
            self.seen.add(phase)
            kw['phase_note']=f'{phase.upper()} PHASE ({self.phase_totals[PHASES.index(phase)]} minutes total; opening is within Predict, summary within Model Building)'
        if check:
            assert look and iff,(title,'check needs actionable notes')
        n=note(t,do,say=say,wait=wait,look=look,iff=iff,why=why,key=key,
               science=f'Source: {self.path.relative_to(ROOT)}/, Lesson 1 and {self.code}. '+kw.pop('science',''),**kw)
        return self.b.slide(title,phase,n,sub,check=check)

    def task(self,title,phase,t,items,do,*,key,look,iff,clock=None,**kw):
        s=self.slide(title,phase,t,do,key=key,look=look,iff=iff,check=True,**kw)
        steps(s,items,w=10.9,dy=.94,size=25,c=COL[phase])
        if clock:timer(s,clock,'individual' if 'alone' in do.lower() else 'work time')
        return s

    def opening(self,goals,words,subtitle):
        prediction_end=7
        s=self.slide('', 'Predict', .25,'Introduce the title briefly. Opening, unit map and goals share one minute within the four-minute Predict phase.',
            purpose=self.l['slo']['purpose']+' '+self.l['slo']['purposeInStoryline'],
            before=f'Print one {self.code} task per learner and keep the teacher key private. Prepare notebooks, pencils, a second colour, paper slips, board and timer. Work is paper-based. No live experiment is required. Read all unit lessons first. Do not show Explain slides until learners finish and record the Observe task. Initial predictions finish on slide {prediction_end}. '+self.l['slo']['safetyNotes'],
            say=subtitle)
        s.background.fill.fore_color.rgb=__import__('pptx').dml.color.RGBColor.from_string(INK)
        # VisualDeck sets dark text by default: title uses its own editable shapes.
        tx(s,f'GRADE 10 · {self.subject.upper()} · LESSON 1 OF {len(self.data["LESSONS"])}',.73,1.0,11.8,.4,14,'D7DF23',True)
        title=self.l['title']
        if self.key=='science':title='What makes a question\nscientific?'
        tx(s,title,.73,1.9,7.8,1.9,40,'FFFFFF',True)
        tx(s,subtitle,.73,4.0,7.1,1.1,24,'D2E4E8')
        if self.key=='science':
            box(s,9.0,1.95,3.35,3.2,CREAM)
            for i,(c,t,_) in enumerate(CASES):badge(s,c,9.2,2.2+i*.83,'47C6E4');tx(s,t,9.85,2.28+i*.83,2.2,.4,18,INK,True)
        else:
            vals=['0','√9','√2'] if self.key=='essential' else ['0','1','9']
            for i,v in enumerate(vals):box(s,9.3,1.85+i*1.08,2.8,.85,CREAM);tx(s,v,9.4,2.0+i*1.08,2.6,.65,35,INK,True,A.CENTER)
        for i,(ph,c) in enumerate(COL.items()):
            x=.75+(i%3)*3.15;y=5.55+(i//3)*.49
            oval(s,x,y,.15,.15,c);tx(s,ph,x+.24,y-.015,2.8,.3,12,'FFFFFF',True)
        tx(s,'40 MINUTES · REVIEW PILOT · 16 NOVEMBER 2026',.75,6.62,8.5,.23,11,'FCBA63',True)
        # Restore a white logo background and light footer on the dark title.
        for sh in s.shapes:
            if sh.has_text_frame and sh.text.startswith('©'):
                for p in sh.text_frame.paragraphs:
                    for r in p.runs:r.font.color.rgb=__import__('pptx').dml.color.RGBColor.from_string('D2E4E8')
        box(s,10.02,6.82,2.65,.52,'FFFFFF')
        # White plaque was added last; move under the inherited logo pictures.
        plaque=s.shapes[-1]._element;s.shapes._spTree.remove(plaque);s.shapes._spTree.insert(2,plaque)
        s=self.b.slide('One routine. Five phases.','Routine',note(0,'Read before class. Slides 2–3 are hidden. Open Presenter View to read these notes while learners see slides. Notes follow TIME, DO, SAY, WAIT TIME, LOOK FOR, IF…, WHY THIS WORKS, ANSWER KEY, SCIENCE NOTE FOR YOU and TEACHER REFLECTION. The background label is inherited; Mathematics notes contain mathematical guidance.'),hidden=True)
        for i,(ph,c) in enumerate(COL.items()):
            box(s,.72,2.2+i*.7,3.0,.5,c);tx(s,ph,.85,2.31+i*.7,2.74,.3,14,INK,True,A.CENTER)
            tx(s,['Write a reason before hearing others.','Record evidence from the supplied task.','Use evidence and definitions to revise.','Keep evidence and open questions visible.','Keep and revise the same model.'][i],4.0,2.27+i*.7,8.4,.4,20)
        tx(s,'WAIT · DO NOT CORRECT PREDICTIONS · CALL ACROSS THE CLASS',.75,6.1,11.8,.4,17,INK,True)
        tx(s,'A check label points to LOOK FOR and IF… in the notes.',.75,6.58,11.8,.3,14,MUTED)
        s=self.b.slide('Lesson 1 at a glance','Glance',note(0,
            f'Prepare one {self.code} task and blank record per learner. Each pair shares only during the specified comparison stage. Provide a pencil and second colour per learner, board and timer; paper slips can replace sticky notes. No special apparatus or chemicals. No projector: use the included student sheet and copy key diagrams onto the board.',
            science='Timings include opening in Predict and final Summary Table in Model Building. Source phase names include “Phase” and “Creation”; the visible tags use their established short forms. ARES: Preview first (not an exact match). The source provides only a search URL, no matched video/reading. Search/offline access remains unverified. No ARES resource is needed to teach this pilot. Do not show keys or later lesson content.'),hidden=True)
        activities={'science':['Choose a case + reason','Three case rows; compare; report','Define inquiry; connect science areas','Sort evidence + open questions','Initial model, exit + summary'],
                    'essential':['Initial number sort + reason','Diagnostic; RN1; pair comparison','Fraction definition + classification','Questions about exact values','Nested model, exit + summary'],
                    'core':['Initial prime predictions','CRN1 alone; compare factor evidence','Separate parity from divisors','Questions about number classes','Correct label, exit + summary']}[self.key]
        table(s,['Phase','min','Learner work'],[[p,str(t),a] for p,t,a in zip(PHASES,self.phase_totals,activities)],.72,2.2,8.6,3.8,[2.7,.6,5.3],15)
        tx(s,'PREPARE',9.65,2.3,2.9,.35,14,INK,True)
        tx(s,f'{self.code} sheet per learner\nNotebook + two colours\nPaper slips + board\nTimer\nTeacher key kept private',9.65,2.85,2.9,2.6,18)
        link=self.l['resourceLinks']['predict']['fallback_search_url']
        sh=box(s,9.65,5.6,2.9,.55,INK);sh.click_action.hyperlink.address=link
        sh=tx(s,'ARES search · preview first',9.78,5.78,2.64,.27,12,'FFFFFF',True);sh.click_action.hyperlink.address=link
        tx(s,'No matched media supplied.\nPrinted route works offline.',9.65,6.25,2.9,.5,12,MUTED)
        s=self.slide('Our unit journey','Unit map',.25,'Point to Lesson 1 and read the unit driving question. Read lesson titles only; do not explain future answers.',key='Today begins the unit; no prior class evidence is assumed.')
        for i,l in enumerate(self.data['LESSONS']):
            col=i//5;row=i%5;x=.72+col*6.08;y=2.1+row*.65
            box(s,x,y,5.88,.56,'D7DF23' if i==0 else 'F0F4F4');badge(s,str(i+1),x+.1,y+.09,INK,.36)
            tx(s,l['title'],x+.58,y+.08,5.12,.45,14,INK,i==0)
        tx(s,'YOU ARE HERE: Lesson 1 · So far: we begin with an untested claim.',.75,5.52,11.8,.4,16,INK,True)
        box(s,.72,6.0,11.9,.72,INK)
        dq=self.data['UNIT']['drivingQuestion'].replace(' KICD:','\nKICD:')
        tx(s,dq,.91,6.1,11.5,.56,15,'FFFFFF',True)
        s=self.slide('By the end of this lesson you can…','Today',.5,'Read three goals without supplying task answers. Procedural key words support the task; teach classification definitions after pupils commit to an initial prediction.',key='Goals are intentions; use the later individual task evidence to check achievement.')
        steps(s,goals,w=8.1,dy=1.13,size=24)
        box(s,9.2,2.4,3.4,3.7,CREAM);tx(s,'KEY WORDS FOR WORKING',9.4,2.62,3,.4,13,INK,True)
        tx(s,words,9.4,3.18,2.98,2.7,18)

    def board(self,question_text):
        self.task('Our Driving Question Board','Driving Question Board',4,
            ['Post evidence from today’s task.','Post one question we still need to answer.','Sort: answered, partly answered, still open.'],
            'Learners write evidence and a question on two colours of paper. Hear one learner with a supported claim and one with an unresolved question. Use a quick vote: does the cited evidence support this claim? Preserve questions for later lessons. '+question_text,
            key={'science':'Evidence: the three fictional case reports are observations, not established causes. Open questions may ask what caused the patches or seedling change. Sort questions about observations, causes and usefulness. Do not answer later wet-window/absorption/seedling cases.',
                 'essential':'Evidence: 0=0/1 and √9=3/1 are rational integer examples. Open question: can a finite calculator display establish an exact number class? Preserve the detailed display argument for Lesson 2.',
                 'core':'Evidence: 9 is odd composite; 0=2×0 is even and neither prime nor composite. Open question: how do whole numbers fit within real numbers? All whole numbers are rational; do not teach the later reciprocal mechanism.'}[self.key],
            look='Read five evidence/question pairs. Check that an evidence note cites this lesson and a cause or exactness question remains open.',
            iff='If a claim has no support, say: “Which entry or representation from today supports that?” Keep untested questions in the open column.',clock='4:00',
            why='Public questions make the next investigation purposeful without treating a class vote as proof.')

    def summary(self):
        key='Observed: '+self.l['summaryTablePrompt']['observed']+'\nLearned: '+self.l['summaryTablePrompt']['learned']+'\nConnection: '+self.l['summaryTablePrompt']['explained']
        s=self.slide('Summary Table · Lesson 1','Model Building',1,
            'Learners complete the three columns on their own sheet. Keep written exits and models for review before Lesson 2. This minute is within Model Building, not extra homework.',
            say='What came from today’s task? What changed in your thinking?',key=key,
            look='Check each learner submits a model and exit response; scan for the specific misconception named in the lesson.',
            iff='If an entry is vague, say: “Name one number or one case from today, then explain what it supports.”',check=True,
            reflection='Which individual answers show the target misconception? Who needs support before Lesson 2? Did all learners record their own evidence? Was the 40-minute pacing realistic? Which question remains unanswered?')
        for i,(h,p) in enumerate([('OBSERVE','What did I observe?'),('LEARN','What did I learn?'),('CONNECT','How does this explain\nour unit phenomenon?')]):
            x=.73+i*4.06;badge(s,str(i+1),x,2.6,list(COL.values())[i],.55);tx(s,h,x,3.4,3.7,.4,16,INK,True);tx(s,p,x,4.15,3.7,1.5,26)
        tx(s,'Next lesson: '+self.data['LESSONS'][1]['title'],.75,6.32,11.8,.4,20,INK,True)

    def save(self):
        assert abs(sum(r['minutes'] for r in self.b.records)-40)<1e-6,self.b.records
        self.b.deck.core_properties.title=self.l['title']
        self.b.deck.core_properties.subject=self.subject+' · Grade 10 · review pilot'
        self.b.save(OUT)
        self.support()

    def support(self):
        OUT.mkdir(parents=True,exist_ok=True)
        d=Document();sec=d.sections[0];sec.top_margin=sec.bottom_margin=DI(.6)
        sec.left_margin=sec.right_margin=DI(.65)
        d.styles['Normal'].font.name='Calibri';d.styles['Normal'].font.size=DP(11)
        d.add_heading(self.subject+' · Grade 10 · Lesson 1',0)
        d.add_heading(self.card[0],1)
        for p in self.card[1:]:
            if p.strip():d.add_paragraph(p)
        heads={'science':['Case','Reported observation','Question','Evidence to collect','Possible benefit'],
               'essential':['Exact number','Rational / irrational','Integer?','Fraction / reason'],
               'core':['Whole number','Odd / even','Prime / composite / neither','Reason']}[self.key]
        vals={'science':['A','B','C'],'essential':['−3','0','2/5','0.125','0.333… (3 repeats forever)','√9','√2','π'],
              'core':['0','1','2','3','4','9','11','15','21']}[self.key]
        t=d.add_table(rows=1,cols=len(heads));t.style='Table Grid'
        for c,h in zip(t.rows[0].cells,heads):c.text=h
        for val in vals:
            cells=t.add_row().cells;cells[0].text=val
        d.add_paragraph({'science':'Initial model: observation → question → evidence → explanation → possible use. Draw your own model below. Exit: explain General Science and one benefit using a GS11 case.',
                         'essential':'Diagnostic working: −4+7 and 3/4+1/2. Draw your own nested real / rational / integer model. Exit: classify −3, √9 and π, giving reasons.',
                         'core':'Positive factor pairs for 9: __________ and for 15: __________. Correct the opening label. Exit: classify 21 and 0 using divisor and parity evidence.'}[self.key])
        for _ in range(3):d.add_paragraph('________________________________________________________________________________')
        d.add_paragraph('Summary Table: What did I observe? What did I learn? How does this explain the unit phenomenon?')
        d.add_paragraph('© 2026 SeaVuria & ARES Education · CC BY-NC 4.0 · Review draft')
        d.save(OUT/(self.name+'_Student_Task.docx'))
        t=Document();t.styles['Normal'].font.name='Calibri';t.styles['Normal'].font.size=DP(10)
        t.add_heading(self.subject+' · Lesson 1 · Teacher notes',0)
        t.add_paragraph('REVIEW DRAFT — Keep this document private. Native PowerPoint, teacher/source-owner approval, Calibri and ARES checks remain open.')
        t.add_heading('Source card and teacher key',1)
        for p in self.key_block:t.add_paragraph(p)
        for r,sl in zip(self.b.records,self.b.deck.slides):
            t.add_heading(f'Slide {r["slide"]}: {r["title"] or self.l["title"]}',1)
            t.add_paragraph(sl.notes_slide.notes_text_frame.text)
        t.save(OUT/(self.name+'_Teacher_Notes.docx'))
        files=sorted(self.path.glob('*'))
        source_manifest={str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files if f.is_file()}
        (ROOT/'qa'/f'{self.name}_sources.json').write_text(json.dumps({'sources':source_manifest,'source_status':'User-selected reviewed November curriculum; classroom acceptance pending',
             'lesson':1,'unit_lessons_read':len(self.data['LESSONS']),'student_card':self.card,'teacher_key':self.key_block,
             'source_authority':'New symlink collection explicitly selected by user on 2026-11-16; no changes to upstream artifacts.'},indent=2,ensure_ascii=False))


def science():
    l=Pilot('science');l.opening(['Separate a report from a proposed cause.','Ask questions that evidence can answer.','Explain General Science and a possible benefit.'],
        'observation: what is reported or recorded\n\nquestion: what we want to find out\n\nevidence: information used to test an idea',
        'Three everyday reports.\nWhich questions could evidence answer?')
    s=l.slide('Which case needs science?','Predict',2,
        'Read GS11’s three fictional cases aloud without identifying a cause. Learners choose a case and write a reason alone. Ask for an initial answer to “What makes a question scientific?” Do not rank the choices.',
        say='Choose a case. Write “I think this needs science because…” Then write a question evidence could help answer.',
        wait='Two minutes of silent reading and writing.',key='Accept any A/B/C choice with a reason and evidence-seeking question. All three can invite science; do not reveal this judgement before initial answers.',
        look='Scan five notebooks for a choice, reason and question about the natural or material world.',iff='If a learner gives only a choice, say: “What would you want to find out about it?”',check=True)
    cases(s);tx(s,'Fictional school cases · read GS11 · choose, give a reason, ask a question.',.75,6.4,9.5,.35,16,MUTED);timer(s,'2:00','read + write',x=10.65,y=6.0)
    l.task('BEFORE · our first ideas','Predict',1,['Share your choice and reason.','What evidence might change your choice?'],
        'Invite one learner for each case if available. Record their exact reasons on the board without correction. Retain initial ideas for Explain.',
        say='Listen for a different reason. We will return to these ideas.',key='Predictions and proposed evidence vary. Do not rank cases or confirm causes.',
        look='Hear choices from different parts of the class; each reason has a question or proposed evidence.',iff='If one voice dominates, say: “We have heard that view. Let us hear a different case.”')
    s=l.slide('GS11 · build the evidence table','Observe',9,
        'Pairs complete all three case rows on the printed GS11 record. Each learner keeps an individual record. Spend nine minutes across the cases. The words describe fictional reports, not a live investigation. Do not handle unknown substances.',
        say='What is actually reported? What would you need to find out?',wait='Nine minutes of pair work.',
        key='Reported: A warmer lunchbox than indoors; B reddish-brown gate patches after a wet season; C fewer seedlings after a dry week. Questions, evidence to collect and benefits are proposals. Possible A temperature readings under comparable conditions, B observations of material change, C repeated counts and growing-condition records. These are possible checks, not new lesson experiments or actual results.',
        look='Inspect at least five individual records. Observation cells must contain reported facts, not “sun caused”, “rust proved” or “drought killed”.',
        iff='If a cause is written as an observation, say: “Which exact words in the case report that? Put the cause in your question instead.”',check=True,
        why='A structured record separates what is known from what still requires evidence.')
    table(s,['Case','Observation','Question','Evidence','Possible benefit'],[['A','','','',''],['B','','','',''],['C','','','','']],.75,2.3,11.85,2.75,[.9,2.6,2.6,2.65,3.1],17)
    tx(s,'Copy only reported facts into “Observation”.\nUse the other columns for your proposed investigation.',.8,5.4,9.25,.95,24);timer(s,'9:00','pairs')
    l.task('Compare · did we add a cause?','Observe',4,['Compare all three observation cells.','Underline words copied from the report.','Does “fewer seedlings” tell us why?'],
        'Pairs inspect their own rows for unsupported causes. Ask the seedling question but preserve detailed alternative-cause and fair-test work for Lesson 4.',
        key='The report gives a lower seedling count, not an established cause. Learners may propose a cause as a question, not as an observed fact.',
        look='Check five learners distinguish the count report from a proposed reason.',iff='Say: “Could the count be correct even if your suggested reason were wrong?” Return to the case wording.',clock='4:00')
    l.task('Report · one row, one question','Observe',3,['Share one reported observation.','Read the question it led you to.','Name evidence you would collect.'],
        'Hear three pairs, one per case. Ask a learner outside each reporting pair to identify which words are report and which are proposal. Do not supply later case results.',
        key='A/B/C report wording as GS11. Accept relevant observable or measurable evidence proposals and conditional benefits; no cause is established.',
        look='Reports distinguish evidence already supplied from evidence proposed.',iff='If a learner invents readings, say: “Were those readings supplied, or are they what you would collect?”')
    l.task('Return to your first idea','Explain',2,['Read your original choice and reason.','In a new colour, keep or revise it.','Point to a case that supports your change.'],
        'Learners revisit predictions. Hear one changed and one retained idea; require evidence rather than agreement with the teacher.',
        key='All three cases can lead to questions investigated with evidence. Reasons should link a reported fact, question and possible check.',
        look='Read five revisions for a case-based reason.',iff='Ask: “Which case led you to that new view?”',clock='2:00')
    s=l.slide('What connects these three cases?','Explain',2,
        'Ask pairs to propose a definition of General Science using the cases. Elicit living things, materials and physical processes before revealing the next slide.',
        say='What kind of questions do all three cases invite?',wait='10–15 seconds, then hear two contrasting definitions.',
        key='A suitable proposed definition connects inquiry and knowledge about the natural/material world, with evidence and revisable explanations.',
        look='Hear definitions from two learners; look for inquiry and evidence, not just a list of subjects.',iff='Ask: “How would we decide whether an explanation fits the report?”',check=True)
    question(s,'What would a useful definition include?','Explain',size=32)
    for i,(c,t,_) in enumerate(CASES):badge(s,c,1.0+i*4.0,4.35,'CF128C');tx(s,t,1.65+i*4.0,4.42,2.9,.5,22,INK,True)
    s=l.slide('General Science · connected inquiry','Explain',2,
        'Build the definition from pupils’ suggestions. Relate the lunchbox to physical processes, the gate to materials/chemical change, and seedlings to living things; the areas overlap. Do not explain heating, corrosion mechanisms or plant-loss causes.',
        say='General Science connects knowledge and systematic inquiry about living things, materials and physical processes. We seek evidence and revise explanations.',
        key='The three source cases connect areas of science without rigid boundaries. A useful explanation needs evidence; the reported pattern alone does not prove a cause.')
    for i,t in enumerate(['Physical processes','Materials and change','Living things']):
        x=.75+i*4.05;box(s,x,2.35,3.8,1.05,'FBE9F5');tx(s,t,x+.18,2.64,3.44,.5,23,INK,True,A.CENTER)
        badge(s,CASES[i][0],x+1.62,3.75,'CF128C',.58)
    box(s,.78,4.75,11.8,1.2,INK);tx(s,'Questions → evidence → explanations we can revise',1.02,5.12,11.3,.6,27,'FFFFFF',True,A.CENTER)
    s=l.slide('Can measurement settle a preference?','Explain',2,
        'Use the source teacher-key contrast with a favourite gate colour. Each learner explains why measuring alone does not decide a preference. Avoid saying that all questions involving people are unscientific.',
        say='Could a measurement tell us which gate colour everyone ought to like most?',wait='30 seconds of individual thinking; hear two explanations.',
        key='Measurements can describe colour or count stated preferences, but measurement alone cannot decide which colour a person should prefer. A natural/material question needs an evidence-based investigation.',
        look='Hear individual reasons distinguish measuring a property or preference count from deciding what ought to be liked.',iff='Say: “We can count favourite colours. Does that force every person to like the most popular one?”',check=True)
    question(s,'Which gate colour is prettiest?','Explain',size=34)
    tx(s,'Explain why measurement alone cannot decide this.',.92,4.45,10.6,1,28,INK,True)
    l.task('Write · what makes it scientific?','Explain',2,['Use one GS11 case.','Link its question to evidence you could collect.','Explain one possible benefit.'],
        'Learners write individually. Require question, proposed evidence and conditional benefit, without claiming an investigation took place.',
        key='Example: We could ask how growing conditions relate to the lower seedling count. We would need counts and condition records before explaining the change. This could help the garden team decide what to investigate next. Accept other evidence-seeking case links; no experiment or cause has been proved.',
        look='Scan five explanations for a reported case and evidence-to-benefit link.',iff='Ask: “What would you collect before deciding that?”',clock='2:00')
    l.board('Sort observation, cause and usefulness questions. Retain unanswered causes.')
    s=l.slide('Version 0 · our evidence model','Model Building',3,
        'Every learner draws the initial five-part model, adds one GS11 case and dates it. Keep the model for revision in later lessons. Do not add later data-analysis or fair-comparison answers.',
        say='Show how a report could lead to an explanation and a possible use. Put a question mark where evidence is missing.',wait='Three minutes of individual drawing.',
        key='Five linked parts: observation → question → evidence → explanation → possible use. The chosen case should preserve report/proposal distinctions. Leave explanation tentative until suitable evidence is gathered.',
        look='Inspect five models for an evidence link before explanation.',iff='If the model jumps straight to a cause, say: “What evidence would go between your question and explanation?”',check=True)
    for i,t in enumerate(['Observation','Question','Evidence','Explanation','Possible use']):
        x=.75+i*2.42;box(s,x,2.7,2.14,1.0,CREAM);tx(s,t,x+.1,3.02,1.94,.45,20,INK,True,A.CENTER)
        if i<4:arrow(s,x+2.17,3.05,.21,'E44145')
    tx(s,'Choose one case. Add your own detail beneath each box.\nKeep uncollected evidence and explanations as questions.',.9,4.3,10.8,1.3,26);timer(s,'3:00','draw alone')
    l.task('Exit · explain science and a benefit','Model Building',2,['Explain General Science in your own words.','Use a GS11 case to show one possible benefit.'],
        'Collect one response and model per learner. Support access without supplying reasoning.',
        key='General Science connects evidence-seeking inquiry and knowledge about the natural/material world. Example: investigating gate-material changes can inform a possible care decision once sufficient evidence is collected. Accept accurate case-specific benefits; do not turn the fictional report into a proven mechanism.',
        look='Each individual names evidence and a case-specific possible use.',iff='If the answer is just “science helps us”, ask: “Which case, and what decision might its evidence help?”',clock='2:00')
    l.summary();l.save()


if __name__=='__main__':
    raise SystemExit('Superseded pre-quiz writer. Use quiz-v1 source-specific specifications and build_curriculum_set_lesson.py; see QUIZ_DESIGN.md.')
    p=argparse.ArgumentParser();p.add_argument('curriculum',choices=['science'])
    a=p.parse_args();science()
