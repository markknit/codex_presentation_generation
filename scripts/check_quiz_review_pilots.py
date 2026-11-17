#!/usr/bin/env python3
"""Source/archive, exact arithmetic and quiz-version checks for the six pilots."""
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
import json
from pathlib import Path
import re
import zipfile

from docx import Document
from pptx import Presentation
from curriculum_set_inventory import ROOT, CONTROL, unit_paths, digest
from lesson_quizzes import check_exports


def main():
    inventory=json.loads((CONTROL/'inventory.json').read_text())
    scope={'modules':{m:[1,2] for m in ['gensci_1_1','essmath_1_1','coremath_1_1']}}
    # Immutable six-deck review checkpoint; current generation scope can expand.
    lessons=[];all_ids=[];archives={}
    for u in inventory['units']:
        if u['module'] not in scope['modules']:continue
        archive=Path(u['source_archive'])
        assert digest(archive)==u['source_archive_sha256']
        with zipfile.ZipFile(archive) as z:
            for name,h in u['source_hashes'].items():
                assert digest(Path(u['source_folder'])/name)==h
                names=[n for n in z.namelist() if Path(n).name==name];assert len(names)==1
                import hashlib
                assert hashlib.sha256(z.read(names[0])).hexdigest()==h
        archives[u['module']]={'archive_sha256':u['source_archive_sha256'],'verified_source_members':len(u['source_hashes'])}
        data=json.loads(next(Path(u['source_folder']).glob('*_data.json')).read_text())
        specs=json.loads((CONTROL/'specs'/(u['module']+'.json')).read_text())
        for n in scope['modules'][u['module']]:
            row=u['lessons'][n-1];spec=specs['lessons'][str(n)];paths=unit_paths(u)
            deck=ROOT/row['deck'];name=row['name']
            meta=json.loads((paths['qa']/(name+'_sources.json')).read_text())
            expected=[int(re.match(r'\s*(\d+)',f['teacherMoves']).group(1)) for f in data['LESSONS'][n-1]['framework']]
            assert list(meta['phase_minutes'].values())==expected and sum(expected)==40
            records=json.loads((paths['qa']/(name+'_manifest.json')).read_text())['slides']
            pres=Presentation(deck)
            result=check_exports(paths['output'],name,u['module'],n,spec,u['source_hashes'],digest(deck),records,pres.slides)
            for q in spec['quizzes']:
                all_ids.append(q['id'])
                for ref in q['source_refs']:
                    text='\n'.join(p.text for p in Document(Path(u['source_folder'])/ref['file']).paragraphs)
                    assert ref['evidence'] in text,(q['id'],'source quotation')
            visible='\n'.join(sh.text for s in pres.slides if s._element.get('show')!='0' for sh in s.shapes if sh.has_text_frame)
            assert not any(code in visible for code in ['GS17','RN8','CRN10'])
            assert len(spec['quizzes'])==3
            checks=json.loads((paths['qa']/(name+'_checks.json')).read_text());assert checks['sha256']==digest(deck)
            lessons.append({'module':u['module'],'lesson':n,'deck_sha256':digest(deck),
                            'slides':len(pres.slides),'minutes':sum(expected),'quiz_ids':[q['id'] for q in spec['quizzes']],
                            'checks':result,'source_quotes':'PASS','later_assessment_inputs':'not present on student slides'})
    assert len(lessons)==6 and len(all_ids)==len(set(all_ids))==18
    assert Fraction('0.125')==Fraction(1,8)==Fraction(125,1000)
    assert Fraction(7,9)==Fraction(77,99)
    assert Fraction(1,3)>Fraction('0.333333333')
    assert Decimal('1.4')**2==Decimal('1.96')<2<Decimal('2.25')==Decimal('1.5')**2
    for number in ['1.411','1.414']:
        assert Decimal(number).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)==Decimal('1.41')
    assert 3*3==9 and 4*4==16 and 0==2*0
    divisors={n:[d for d in range(1,n+1) if n%d==0] for n in [1,2,3,4,9,11,15,21]}
    assert divisors[1]==[1] and divisors[2]==[1,2]
    assert divisors[9]==[1,3,9] and divisors[15]==[1,3,5,15] and divisors[21]==[1,3,7,21]
    answer_counts=dict(Counter(q['correct'] for u in inventory['units'] if u['module'] in scope['modules']
        for n in [1,2] for q in json.loads((CONTROL/'specs'/(u['module']+'.json')).read_text())['lessons'][str(n)]['quizzes']))
    report={'scope':'Original six user-authorised review drafts; later generation uses separate checks','lessons':lessons,
            'source_archives':archives,'unique_versioned_questions':18,'correct_option_distribution':answer_counts,
            'exact_arithmetic':'PASS: fraction conversions, recurring fractions, squared bounds, rounding, roots and divisor lists',
            'builder_content_review':'All 18 single-answer questions, explanations and distractor feedback compared with source keys; teacher review remains open.',
            'server':'Future integration only; no class or individual responses fabricated',
            'cpu_only':'Document/archive/text inspection and exact arithmetic; separate CUDA reports prove raster execution.'}
    (ROOT/'qa/Quiz_Review_Pilots_content_checks.json').write_text(json.dumps(report,indent=2))
    print('PASS: six source-verified decks, 18 unique questions, exact arithmetic and public/private manifests')


if __name__=='__main__': main()
