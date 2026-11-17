#!/usr/bin/env python3
"""Explicit source-backed checks for the remaining two Real Numbers units."""
import argparse
import json

from author_quiz_review_pilots import quiz
from curriculum_set_inventory import CONTROL
from lesson_quizzes import REVISION,validate_quizzes


def items(module):
    # Each row: stem, ordered A–D options, key, reinforcement, three wrong-choice
    # reasons in label order, verbatim reviewed-key evidence, objective.
    if module=='essmath_1_1':return {
      6:[
       ('The tank starts with 3/4 L, uses 1/6 L and adds 1/3 L. What is the final amount?',
        ['7/12 L','11/12 L','5/4 L','−1/12 L'],'B',
        'Represent the actions as 3/4 − 1/6 + 1/3 = (9 − 2 + 4)/12 = 11/12 L. The signs describe what is used and added.',
        ['This omits the added 1/3 L.','This treats the used volume as an addition.','This does not match the stated changes.'],
        '3/4−1/6+1/3=11/12 L; assume exact amounts/no loss beyond stated use.','Match signed volume changes to exact operations.'),
       ('How should the fictional 120/80 mmHg record be copied in RN6?',
        ['Divide 120 by 80 and record 1.5.','Record a single volume in litres.',
         'Put 120 and 80 in separate labelled columns, each with mmHg.','Use the arithmetic alone to judge health status.'],'C',
        'Here the slash separates two readings. Copy systolic 120 mmHg and diastolic 80 mmHg separately; the task does not ask for division or a health judgement.',
        ['The slash separates two readings, not a requested quotient.','The source gives mmHg, not litres.','The task provides no clinical interpretation.'],
        'Blood-pressure recording columns: systolic 120 mmHg,diastolic 80 mmHg; the slash separates readings, not a fraction calculation.',
        'Preserve the meaning and units of a two-reading record.'),
       ('For bottles holding 3/4 L each, what does the reciprocal 4/3 represent?',
        ['Litres per bottle','The tank’s final liquid volume','A temperature change','Bottles per litre'],'D',
        'The original capacity is 3/4 litres per bottle. Its reciprocal is 4/3 bottles per litre, so 3 litres × 4/3 bottles per litre gives 4 bottles.',
        ['That is the original capacity’s unit, not its reciprocal.','The reciprocal is a conversion rate, not the final tank volume.','The bottle model concerns volume and counts.'],
        'The reciprocal 4/3 has bottles per litre in this model, while 3/4 is litres per bottle.',
        'Interpret a reciprocal’s unit in a stated model.')],
      7:[
       ('The plan has 2.5 L and reserves 1/4 L. What volume remains usable?',
        ['9/4 L','11/4 L','5/8 L','1/4 L'],'A',
        'Subtract the reserve once: 2.5 − 0.25 = 2.25 L = 9/4 L. The reserve is kept out of the serving calculation.',
        ['This adds the reserve instead of subtracting it.','This multiplies by the reserve instead of subtracting it.','This is the reserve alone, not the usable volume.'],
        '2.5−0.25=2.25 L=9/4 L; (9/4)÷(3/8)=6 servings exactly.',
        'Subtract a reserve before planning full servings.'),
       ('Why does the reported 0.844 resemble an operation error in 2.25 ÷ 0.375?',
        ['It is the exact quotient.','It is the volume of seven full servings.',
         'It is the rounded product 2.25 × 0.375.','It proves that the reserve is zero.'],'C',
        '2.25 × 0.375 = 0.84375, which rounds to 0.844. The intended quotient is 6; compare the requested operation with the actual entry.',
        ['The quotient is 6, not 0.844.','Seven servings require 2.625 L.','The source explicitly reserves 1/4 L.'],
        '0.844 is the rounded product 2.25×0.375=0.84375, not the quotient; multiplication by reciprocal 8/3 gives 6.',
        'Diagnose an operation mismatch rather than trust a plausible display.'),
       ('Which reverse check verifies six full 3/8 L servings use the available serving volume?',
        ['6 + 3/8 = 51/8','6 − 3/8 = 45/8','6 ÷ 3/8 = 16','6 × 3/8 = 9/4 L'],'D',
        'Multiply the count by the volume per serving: 6 × 3/8 L = 9/4 L. That equals the usable volume, with the reserve already subtracted.',
        ['Adding count and volume does not check the total serving volume.','Subtraction does not reverse the original division.','Dividing again does not check volume used.'],
        'Check 6×3/8=9/4 L.','Verify a full-serving decision with a product and units.')]
    }
    return {
      6:[
       ('Which exact value equals 1 ÷ (2 ÷ 3)?',
        ['2/3','1/6','3/2','−3/2'],'C',
        'The entire denominator is 2/3. Dividing 1 by that fraction gives 3/2, verified by (2/3) × (3/2) = 1.',
        ['This retains the denominator rather than its reciprocal.','This fails to divide by the whole fractional denominator.','Both 1 and the denominator are positive.'],
        'Exact results5/18,−2/5,3/2,1/√2;',
        'Protect a compound denominator with parentheses.'),
       ('No calculator was supplied. Which record is accurate?',
        ['NOT OBSERVED for device use; retain exact paper work.','Invent a plausible copied display.',
         'A correct paper answer proves device use.','A partner’s entry proves my device use.'],'A',
        'Paper mathematics can be checked on its own. Actual calculator performance remains unobserved until an individual device action is provided and recorded.',
        ['A fabricated display is not an observed record.','Written correctness does not establish an action.','A partner’s action is not the learner’s own evidence.'],
        'Never invent a pupil key sequence, display or observed-use record.',
        'Keep actual device evidence distinct from written mathematical correctness.'),
       ('Which approximation gives 1/√2 to four significant figures?',
        ['0.707','0.7071','0.7072','0.7000'],'B',
        'The value begins 0.707106… . Its first four significant figures are 7, 0, 7, 1; the next digit is 0, giving 0.7071. This is approximate.',
        ['0.707 has three significant figures.','The next digit does not round the last retained digit up.','This discards significant digits incorrectly.'],
        '4sig approximate0.2778 and0.7071.',
        'Round an already-investigated reciprocal to the source precision.')],
      7:[
       ('How many exact 3/4 L portions fit in 4½ L with no spills?',
        ['3','4','6','8'],'C',
        '(9/2) ÷ (3/4) = (9/2) × (4/3) = 6 portions. The count assumes the stated exact quantities and no spills.',
        ['Three portions use only 9/4 L.','Four portions use only 3 L.','Eight portions would require 6 L.'],
        '(a)(9/2)×(4/3)=6full portions;6×3/4L=9/2L.',
        'Use a reciprocal to count exact full portions.'),
       ('Which exact value equals (−3/5) ÷ (2/7)?',
        ['−6/35','21/10','−10/21','−21/10'],'D',
        'Multiply by the nonzero divisor’s reciprocal: (−3/5) × (7/2) = −21/10. Multiplying this result by 2/7 returns −3/5.',
        ['This multiplies by 2/7 rather than its reciprocal.','The quotient must be negative.','This reverses the required quotient.'],
        '(c)(−3/5)×(7/2)=−21/10; times2/7 gives−3/5.',
        'Apply signed division and verify by multiplication.'),
       ('Which check verifies eight 0.3 m pieces account for a 2.4 m strip?',
        ['8 × 0.3 m = 2.4 m','8 + 0.3 m = 8.3 m','8 ÷ 0.3 m = 2.4 m','8 − 0.3 m = 2.4 m'],'A',
        'Multiply count by length per piece: 8 × 0.3 m = 2.4 m. This paper model assumes exact lengths and no cutting loss.',
        ['Adding count to length does not verify the used length.','The stated division does not equal 2.4 or check the length.','Subtraction does not verify the total used length.'],
        '(b)(12/5)×(10/3)=8pieces;8×0.3m=2.4m.',
        'Check a piece count with length and the no-loss assumption.')],
      8:[
       ('Which statement would make a numerical advice card verifiable?',
        ['Everyone should agree because I am confident.','Use a checked calculation tied to a specific decision.',
         'Remove units so the message is shorter.','Copy a slogan without any evidence.'],'B',
        'Useful advice links a correct classification or computation to a concrete decision. Include the numerical evidence, units, assumptions and relevant limits.',
        ['Confidence is not the mathematical evidence.','Units explain what the result means.','A slogan does not establish a checked result.'],
        'Accept varied advice only when the classification and worked computation are correct and linked to a concrete decision.',
        'Connect correct numerical evidence to a useful decision.'),
       ('Which advice correctly combines a classification with the reciprocal domain limit?',
        ['Zero is prime, so divide by it.','Zero is odd, so its reciprocal is −1.',
         'Zero is even, but it has no real reciprocal.','Every even number has reciprocal zero.'],'C',
        'Zero is even because 0 = 2 × 0. It cannot be a divisor in real-number division: 0 × r cannot equal 1 for any real r.',
        ['Zero is neither prime nor composite and cannot be a divisor.','Zero is even and has no real reciprocal.','A nonzero original times zero is not 1.'],
        'Example:0 is even but cannot be a divisor;',
        'Keep parity and reciprocal existence as different decisions.'),
       ('What does the CRN7 check 6 × 3/4 L = 4½ L support in an advice card?',
        ['Any fraction of a portion can be rounded up.','Losses never matter in a real situation.',
         'The same count works for every portion size.','Six exact full portions fit under the no-spill assumption.'],'D',
        'The product checks this stated supply and portion size. It supports six full portions under the stated exact-quantity and no-spill assumptions, with those limits visible.',
        ['These exact whole counts do not justify rounding any fractional count up.','The no-spill assumption is a condition, not a universal fact.','Changing portion size changes the count.'],
        '4½L÷3/4L=6full portions with no spills.',
        'State the scope of an evidence-based planning recommendation.')],
      9:[
       ('Which counterexample disproves “Every odd whole number is prime”?',
        ['9 has the positive divisors 1, 3 and 9.','2 has exactly two positive divisors.',
         '0 equals 2 × 0.','Every integer n can be written as n/1.'],'A',
        '9 is odd and has more than two positive divisors, so it is composite. One odd composite example disproves the universal prime claim.',
        ['2 is even and does not test the odd-number claim.','Zero’s parity does not test this universal odd claim.','Rational membership does not decide prime status.'],
        'A counterexample9 has divisors1,3,9;',
        'Choose a counterexample relevant to a particular universal claim.'),
       ('Which correction repairs the claim that an error display makes zero’s reciprocal 0?',
        ['An error display changes the real-number definition.','0 × r is always 0, so no real reciprocal exists.',
         '0 × 0 = 1.','Zero’s reciprocal is the number of display digits.'],'B',
        'A reciprocal must give a product of 1. Since zero times any real r is zero, an error display cannot supply or redefine a real reciprocal.',
        ['Device messages do not redefine the product-of-one rule.','0 × 0 equals 0.','Display length does not define a reciprocal.'],
        'E0×r=0 can never equal1.',
        'Use the defining rule to reject a misleading device shortcut.'),
       ('Which exact comparison checks the direction of reciprocal scaling?',
        ['1/3.2 = 0.3125; 1/32 = 3.125','1/3.2 = 0.3125; 1/32 = 0.3125',
         '1/3.2 = 0.3125; 1/32 = 0.03125','1/3.2 = 0.3125; 1/32 = 32'],'C',
        '32 is ten times 3.2, so its reciprocal is one tenth as large: 0.3125 ÷ 10 = 0.03125. This checks the claim with exact values.',
        ['This increases the reciprocal tenfold instead of dividing it by ten.','A changed nonzero input does not keep this reciprocal unchanged.','32 is the input, not its reciprocal.'],
        'D 1/3.2=0.3125 but1/32=0.03125, divided by10;',
        'Repair a scaling shortcut with exact numerical evidence.')]
    }


def author(module):
    path=CONTROL/'specs'/(module+'.json');unit=json.loads(path.read_text());specs=unit['lessons']
    inventory=json.loads((CONTROL/'inventory.json').read_text());u=next(u for u in inventory['units'] if u['module']==module)
    definition=items(module);final=8 if module=='essmath_1_1' else 10
    for n in sorted([*definition,final]):
        spec=specs[str(n)]
        if module=='essmath_1_1' and n==6:
            spec['slides'][4]['widths']=[3.1,4.5,4.2]
            spec['record']['rows']=[r for r in spec['record']['rows'] if 'Blood-pressure' not in r[0]]
            spec['additional_records']=[{'headers':['Systolic (mmHg)','Diastolic (mmHg)'],'rows':[['','']],'row_height':.5}]
            decision=' Added a separate blank two-column record for the source blood-pressure readings; no clinical interpretation or personal measurement. Widened the context column so Temperature remains one word after PDF/visual inspection.'
            if decision not in spec.get('decisions',''):spec['decisions']=spec.get('decisions','')+decision
        if spec.get('design_revision')==REVISION:
            validate_quizzes(spec,module,n,u['source_hashes']);continue
        if n==final:
            spec.update(design_revision=REVISION,quizzes=[],quiz_exception='Independent source assessment: all original phase/section work and checking/collection time retained. No coached A–D poll or feedback before collection; use actual collected work to plan later reinforcement.',decisions='Independent assessment quiz exception. Phase labels schedule original sections, not coached teaching. Preserve source rubric and tasks. Print rubric begins on a separate page with non-splitting rows and repeated headers; wording and scoring unchanged. No device observation is inferred from written answers.')
        else:
            exp=[i+1 for i,r in enumerate(spec['slides']) if r['phase']=='Explain']
            positions=[exp[0],exp[-1],len(spec['slides'])]
            for pos in [exp[0],exp[-1]]:spec['slides'][pos-1]['minutes']-=1
            next(s for s in spec['slides'] if s['phase']=='Model Building')['minutes']-=1
            spec['slides'][-1]['do']='Save the complete individual exit before the final reinforcement quiz. Keep first-attempt exit and quiz records separate.'
            qs=[]
            for i,(stem,options,key,feedback,wrong,evidence,objective) in enumerate(definition[n],1):
                placement=f'After source {spec["code"]} '+('individual task/checks and first worked explanation.' if i==1 else 'complete explanation, before question-board work.' if i==2 else 'saved individual exit; reinforcement only, not independent-transfer evidence.')
                q=quiz(module,n,i,positions[i-1],stem,options,key,feedback,wrong,evidence,objective,placement)
                q['accuracy_check']='Reviewed each choice and feedback against the complete source unit and exact cited key; exact arithmetic and source checks recorded in qa/Quiz_Continuation_content_checks.json.';qs.append(q)
            spec.update(design_revision=REVISION,quizzes=qs)
            spec['decisions']=spec.get('decisions','')+' Three source-backed quiz pairs at taught concept transitions and after the saved exit. Two one-minute pairs use Explain/check time; one uses Model Building reinforcement. Preserve all Observe subdivisions, every original task and exact source phase totals. Teacher must confirm 30+30-second response/feedback pacing. No future assessment data, live class results or fabricated tool evidence.'
            if spec.get('record'):spec['record']['row_height']=.65
        for row in spec['slides']:
            if row.get('timer'):
                seconds=round(row['minutes']*60);row['timer']=f'{seconds//60}:{seconds%60:02}'
        validate_quizzes(spec,module,n,u['source_hashes'])
    unit['status']='Complete source-specific unit authored for quiz-v1. Final independent assessment has a documented quiz exception. Native PowerPoint/teacher/release gates open.'
    path.write_text(json.dumps(unit,indent=2,ensure_ascii=False)+'\n');print(module,'remaining source-specific quizzes authored; existing pilots/earlier lessons preserved')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('module',choices=['essmath_1_1','coremath_1_1']);a=p.parse_args();author(a.module)
