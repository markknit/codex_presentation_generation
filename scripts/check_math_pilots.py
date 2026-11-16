#!/usr/bin/env python3
"""Source coverage, independent arithmetic checks and print text preservation."""
import hashlib
import json
import subprocess
from collections import Counter
from fractions import Fraction

from docx import Document
from pptx import Presentation
from build_curriculum_pilots import CONFIG, ROOT, OUT
from check_curriculum_pilots import words


def visible(slide):
    result=[]
    for shape in slide.shapes:
        if shape.has_text_frame:result.append(shape.text)
        if shape.has_table:
            result.extend(c.text for r in shape.table.rows for c in r.cells)
    return '\n'.join(result)


def main():
    reports=[]
    for key in ['essential','core']:
        name=CONFIG[key][2];deck=OUT/(name+'.pptx')
        subprocess.run([str(ROOT/'.venv/bin/python'),str(ROOT/'scripts/check_curriculum_pilots.py'),
                        '--curriculum',key],check=True,stdout=subprocess.DEVNULL)
        p=Presentation(deck);texts=[visible(s) for s in p.slides]
        notes=[s.notes_slide.notes_text_frame.text for s in p.slides]
        m=json.loads((ROOT/'qa'/f'{name}_manifest.json').read_text())
        explain=next(i for i,r in enumerate(m['slides']) if r['phase']=='Explain')
        for token in (['0 = 0/1','√9 = 3 = 3/1','REAL NUMBERS'] if key=='essential'
                      else ['0 = 2 × 0','1 → {1}','9 is odd and composite']):
            first=next(i for i,t in enumerate(texts) if token in t)
            assert first>=explain,(name,'early result',token)
        for i,n in enumerate(notes):
            assert 'SCIENCE NOTE FOR YOU' not in n,(name,i+1)
            if i not in [0,1,2]:
                assert '\nANSWER KEY\n' in n,(name,i+1,'missing key')
        if key=='essential':
            t=next(sh.table for s in p.slides for sh in s.shapes
                   if sh.has_table and sh.table.cell(0,0).text=='Exact value')
            rational={'−3':Fraction(-3),'0':Fraction(0),'2/5':Fraction(2,5),
                      '0.125':Fraction('0.125'),'0.333…':Fraction(1,3),'√9':Fraction(3)}
            for r in list(t.rows)[1:]:
                value,kind,integer,reason=[c.text for c in r.cells]
                if value in rational:
                    n=rational[value]
                    assert kind=='Rational' and integer==('Yes' if n.denominator==1 else 'No')
                    assert Fraction(reason.split(' (')[0].replace('−','-'))==n,(value,reason)
                else:assert value in ['√2','π'] and kind=='Irrational' and integer=='No'
            assert len(t.rows)==9
            assert '3/4+2/4=5/4' in '\n'.join(notes)
            assert Fraction(3,4)+Fraction(1,2)==Fraction(5,4)
            task=Document(OUT/(name+'_Student_Task.docx'))
            assert [r.cells[0].text for r in list(task.tables[0].rows)[1:]]==[
                '−3','0','2/5','0.125','0.333…\n(3 repeats forever)','√9','√2','π']
        else:
            t=next(sh.table for s in p.slides for sh in s.shapes
                   if sh.has_table and sh.table.cell(0,0).text=='Parity')
            seen=[]
            for row in list(t.rows)[1:]:
                parity=row.cells[0].text
                for kind,cell in zip(['Prime','Composite','Neither'],list(row.cells)[1:]):
                    for token in cell.text.split(', '):
                        n=int(token);seen.append(n)
                        divisors=[d for d in range(1,n+1) if n%d==0]
                        derived='Neither' if n<2 else ('Prime' if len(divisors)==2 else 'Composite')
                        assert parity==('Even' if n%2==0 else 'Odd') and kind==derived,(n,kind)
            assert sorted(seen)==[0,1,2,3,4,9,11,15,21]
            for n in [9,15]:
                pairs=[(a,n//a) for a in range(1,n+1) if n%a==0 and a<=n//a]
                for a,b in pairs:assert f'{a} × {b}' in '\n'.join(texts)
            task=Document(OUT/(name+'_Student_Task.docx'))
            assert [int(r.cells[0].text) for r in list(task.tables[0].rows)[1:]]==[0,1,2,3,4,9,11,15,21]
        docs=[]
        for suffix in ['Student_Task','Teacher_Notes']:
            file=OUT/(name+'_'+suffix+'.docx');d=Document(file)
            strings=[p.text for p in d.paragraphs]
            strings.extend(c.text for t in d.tables for r in t.rows for c in r.cells)
            pdf=file.with_suffix('.pdf')
            rendered=subprocess.check_output(['pdftotext','-layout',str(pdf),'-'],text=True)
            # Ignore line-drawing underscores and discretionary word hyphenation.
            clean=lambda t: words(t.replace('_',' ').replace('\u00ad',''))
            missing=Counter(clean('\n'.join(strings)))-Counter(clean(rendered))
            assert not missing,(file,dict(missing))
            gpu_path=ROOT/'qa/renders/curriculum_pilots_2026-11'/name/(name+'_'+suffix)/'gpu/gpu_report.json'
            gpu=json.loads(gpu_path.read_text())
            assert gpu['backend']=='CUDA sm_121'
            docs.append({'file':str(file.relative_to(ROOT)),'sha256':hashlib.sha256(file.read_bytes()).hexdigest(),
                         'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
                         'pages':len(gpu['slides']),'text_retention':'PASS','raster_backend':gpu['backend']})
        report={'name':name,'deck_sha256':hashlib.sha256(deck.read_bytes()).hexdigest(),
                'source_task_coverage':'PASS','arithmetic_and_classification_checks':'PASS',
                'results_after_individual_work':'PASS','math_note_labels_and_task_keys':'PASS',
                'print_documents':docs,'limits':'Automated checks supplement source and visual review; no teacher or native PowerPoint approval.'}
        reports.append(report)
    (ROOT/'qa/Mathematics_pilots_checks.json').write_text(json.dumps(reports,indent=2))
    print(json.dumps(reports,indent=2))


if __name__=='__main__':main()
