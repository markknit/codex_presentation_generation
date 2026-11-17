#!/usr/bin/env python3
"""Verify authored continuation against reviewed files and actual built decks."""
import argparse
from collections import Counter
from fractions import Fraction
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import zipfile

from docx import Document
from pptx import Presentation
from curriculum_set_inventory import ROOT, CONTROL, unit_paths, digest
from lesson_quizzes import validate_quizzes, check_exports


def check(module, numbers, built=False):
    inventory=json.loads((CONTROL/'inventory.json').read_text())
    u=next(u for u in inventory['units'] if u['module']==module)
    folder=Path(u['source_folder']);archive=Path(u['source_archive'])
    assert digest(archive)==u['source_archive_sha256']
    with zipfile.ZipFile(archive) as z:
        for filename,expected in u['source_hashes'].items():
            matches=[n for n in z.namelist() if Path(n).name==filename]
            assert len(matches)==1 and digest(folder/filename)==expected
            assert hashlib.sha256(z.read(matches[0])).hexdigest()==expected
    source=json.loads(next(folder.glob('*_data.json')).read_text())
    specs=json.loads((CONTROL/'specs'/(module+'.json')).read_text())['lessons']
    results=[];ids=[]
    for n in numbers:
        spec=specs[str(n)];qs=validate_quizzes(spec,module,n,u['source_hashes'])
        totals=Counter({'Predict':1,'Model Building':0 if spec.get('assessment') else 1})
        for s in spec['slides']:totals[s['phase']]+=s['minutes']
        for q in qs:
            ids.append(q['id']);totals[q['phase']]+=q['response_minutes']+q['feedback_minutes']
            for ref in q['source_refs']:
                file=folder/ref['file']
                if file.suffix=='.json':text=file.read_text()
                else:
                    d=Document(file);text='\n'.join(p.text for p in d.paragraphs)
                    text+='\n'+'\n'.join(c.text for t in d.tables for r in t.rows for c in r.cells)
                assert ref['evidence'] in text,(q['id'],'source evidence absent')
        phases=['Predict','Observe','Explain','Driving Question Board','Model Building']
        expected=[int(re.match(r'\s*(\d+)',f['teacherMoves']).group(1)) for f in source['LESSONS'][n-1]['framework']]
        assert [totals[p] for p in phases]==expected and sum(totals.values())==40
        result={'module':module,'lesson':n,'quizzes':len(qs),'source_evidence':'PASS','phase_minutes':dict(totals),'assessment_exception':spec.get('quiz_exception')}
        if built:
            row=u['lessons'][n-1];paths=unit_paths(u);deck=ROOT/row['deck'];name=deck.stem
            manifest=json.loads((paths['qa']/(name+'_manifest.json')).read_text())
            metadata=json.loads((paths['qa']/(name+'_sources.json')).read_text())
            unit_spec=json.loads((CONTROL/'specs'/(module+'.json')).read_text())
            spec_hash=hashlib.sha256(json.dumps({'lesson':spec,'anchor':unit_spec['anchor_line']},sort_keys=True,ensure_ascii=False).encode()).hexdigest()
            assert metadata['spec_sha256']==spec_hash,(module,n,'stale source-specific specification')
            p=Presentation(deck)
            result['exports']=check_exports(paths['output'],name,module,n,spec,u['source_hashes'],digest(deck),manifest['slides'],p.slides)
            checks=json.loads((paths['qa']/(name+'_checks.json')).read_text())
            assert checks['sha256']==digest(deck)
            if not spec.get('assessment'):
                visible='\n'.join(s.text for slide in p.slides if slide._element.get('show')!='0' for s in slide.shapes if s.has_text_frame)
                # Whole source codes: Essential RN8 is not Core's taught CRN8.
                assert not re.search(r'\b(?:GS17|RN8|CRN10)\b',visible)
            result.update(deck_sha256=digest(deck),slides=len(p.slides),automated_checks='PASS')
        results.append(result)
    assert len(ids)==len(set(ids))
    if module=='gensci_1_1':
        assert sum([18,20,22])/3==20 and sum([9,10,11])/3==10
        assert 10-6==4 and 10-9==1
    if module=='essmath_1_1':
        a,b,c,d=Fraction(-3,4)+Fraction(5,6),Fraction(2,3)-Fraction(5,4),Fraction(-2,3)*Fraction(9,4),Fraction(3,5)/Fraction(-9,10)
        assert (a,b,c,d)==(Fraction(1,12),Fraction(-7,12),Fraction(-3,2),Fraction(-2,3))
        assert a-Fraction(5,6)==Fraction(-3,4) and d*Fraction(-9,10)==Fraction(3,5)
        assert Fraction(3,4)+Fraction(1,2)==Fraction(5,4) and (-2)*(-5)==10
        assert Fraction(3,4)-Fraction(1,2)/(-2)==1
        assert (-3)**2-2*(5-8)==15 and -(3**2)==-9 and Fraction(6,3)*2==4
        for value,reciprocal in [(Fraction(4),Fraction(1,4)),(Fraction(-5),Fraction(-1,5)),(Fraction(3,4),Fraction(4,3)),(Fraction('-.2'),Fraction(-5))]:
            assert value*reciprocal==1
        assert Fraction('0.707106781')**2!=Fraction(1,2)
        assert Fraction(3,4)-Fraction(1,6)+Fraction(1,3)==Fraction(11,12)
        assert 50-80+45==15 and Decimal('37.4')-Decimal('36.8')==Decimal('.6')
        assert Fraction(3)/Fraction(3,4)==4
        usable=Fraction('2.5')-Fraction(1,4)
        assert usable==Fraction(9,4) and usable/Fraction(3,8)==6
        assert 6*Fraction(3,8)==usable<7*Fraction(3,8)
        assert Decimal('2.25')*Decimal('.375')==Decimal('.84375')
    if module=='coremath_1_1':
        for value,reciprocal in [(Fraction(4),Fraction(1,4)),(Fraction(-5),Fraction(-1,5)),(Fraction(2,3),Fraction(3,2)),(Fraction(3,2),Fraction(2,3)),(Fraction(-5,2),Fraction(-2,5)),(Fraction('.25'),Fraction(4)),(Fraction('-.4'),Fraction(-5,2)),(Fraction(1,9),Fraction(9))]:
            assert value*reciprocal==1
        assert Fraction(-5,2)*Fraction(-2,3)==Fraction(5,3)!=1
        assert 1/Fraction('3.2')==Fraction('.3125') and 1/Fraction('32')==Fraction('.03125')
        assert 1/Fraction('.32')==Fraction('3.125')
        assert 1/Fraction('3.6')==Fraction(5,18)!=Fraction('.2778')
        assert 1/Fraction('.036')==Fraction(250,9)!=Fraction('27.78')
        assert 1/Fraction(2,3)==Fraction(3,2)
        assert (1/Decimal(2).sqrt()).quantize(Decimal('.0001'))==Decimal('.7071')
        assert Fraction(9,2)/Fraction(3,4)==6 and 6*Fraction(3,4)==Fraction(9,2)
        assert Fraction('2.4')/Fraction('.3')==8 and 8*Fraction('.3')==Fraction('2.4')
        assert Fraction(-3,5)/Fraction(2,7)==Fraction(-21,10)
    path=ROOT/'qa/Quiz_Continuation_content_checks.json'
    prior=json.loads(path.read_text()) if path.exists() else {'lessons':[]}
    remaining=[r for r in prior['lessons'] if (r['module'],r['lesson']) not in {(module,n) for n in numbers}]
    report={'lessons':sorted(remaining+results,key=lambda r:(r['module'],r['lesson'])),
            'status':'Source quote, archive/member hashes, unique IDs, exact phase totals and independent-assessment boundaries checked; mathematical/scientific teacher approval remains open.',
            'cpu_only':'Document/archive/text inspection and exact arithmetic. Separate CUDA reports cover raster processing.'}
    path.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(module,numbers,'PASS', 'including built artifacts' if built else 'authored specifications')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('module');p.add_argument('lessons',type=int,nargs='+');p.add_argument('--built',action='store_true');a=p.parse_args();check(a.module,a.lessons,a.built)
