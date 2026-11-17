#!/usr/bin/env python3
"""Source-specific authoring for the six explicitly authorised quiz review decks."""
import json
from pathlib import Path

from curriculum_set_inventory import CONTROL
from lesson_quizzes import REVISION, validate_quizzes


def s(phase, minutes, title, kind='bullets', **kw):
    return {'phase': phase, 'minutes': minutes, 'title': title, 'kind': kind, **kw}


def task(phase, minutes, title, items, mode='write alone', **kw):
    seconds=round(minutes*60)
    return s(phase,minutes,title,items=items,timer=f'{seconds//60}:{seconds%60:02}',mode=mode,**kw)


def quiz(module, n, ordinal, after, stem, options, correct, explanation, wrong,
         evidence, objective, placement):
    subject, topic = {'gensci_1_1':('General_Science','Introduction_to_General_Science'),
                     'essmath_1_1':('Essential_Mathematics','Real_Numbers'),
                     'coremath_1_1':('Core_Mathematics','Real_Numbers')}[module]
    code={'gensci_1_1':f'GS1{n}','essmath_1_1':f'RN{n}','coremath_1_1':f'CRN{n}'}[module]
    phase='Model Building' if ordinal==3 else 'Explain'
    return {'id':f'{module}.L{n:02}.Q{ordinal:02}.v1','after_slide':after,'phase':phase,
            'stem':stem,'options':dict(zip('ABCD',options)),'correct':correct,
            'explanation':explanation,'distractor_feedback':dict(zip([k for k in 'ABCD' if k!=correct],wrong)),
            'objective':objective,'placement_reason':placement,
            'no_future_content_reason':f'Uses only {code} content already investigated and explained; no later lesson or final assessment inputs.',
            'timing_source':('One minute of the source ten-minute Explain allocation. Authored explanation screens total eight minutes; two quizzes total two.'
                             if ordinal<3 else 'One minute of the source Model Building allocation after the written exit is saved; summary remains last. Required model and exit tasks are retained.'),
            'response_minutes':.5,'feedback_minutes':.5,
            'source_refs':[{'file':f'Codex_{subject}_{topic}_MaterialsTeacherKey.docx',
                            'locator':f'{code} — Teacher key and preparation','evidence':evidence}],
            'accuracy_check':'Checked against the named source key, every alternative and the independent item checks in qa/Quiz_Review_Pilots_content_checks.json.'}


def first_lessons():
    pred=lambda text:[s('Predict',2,'Your first idea and reason','question',text=text,timer='2:00',mode='write alone'),
                      task('Predict',1,'BEFORE · keep our reasons',['Share your prediction and its reason.','Keep a different first idea visible.'],mode='share; do not correct')]
    gs={'code':'GS11','short':'Scientific_Questions','goals':['Ask questions evidence could answer.','Separate a report from a proposed cause.','Connect an investigation to a possible use.'],
        'words':'report: what is stated\n\nevidence: information used to check a claim',
        'slides':pred('Which of the three GS11 school cases needs science? Give a reason before discussing.')+[
        s('Observe',9,'GS11 · three reports to investigate','notice_cases',timer='9:00',mode='case table in pairs',
          do='Provide the complete GS11 table. Pairs spend nine minutes on all three cases. Each learner records the reported observation, question, needed evidence and possible benefit. These are fictional reports, not demonstrations or actual measurements.'),
        task('Observe',4,'Compare the evidence we would need',['Compare the three completed case rows.','Separate what is reported from what you propose.','Keep causes as questions until evidence is collected.'],mode='compare in pairs'),
        task('Observe',3,'Report a question and possible benefit',['Report one evidence-seeking question.','Name what evidence would help and a possible use.'],mode='share case evidence'),
        s('Explain',2,'What does General Science connect?','columns',columns=[['INQUIRY','Ask questions.\nGather and check evidence.\nRevise explanations.'],['CONNECTED KNOWLEDGE','Living things\nMatter and chemical change\nPhysical processes']],caption='One case can connect more than one science area.'),
        s('Explain',3,'Which questions can measurements answer?','columns',columns=[['EVIDENCE-SEEKING','How do the two lunchbox temperatures compare?'],['PREFERENCE','Which gate colour is prettiest?']],caption='Measurements can inform a choice; they do not decide a preference.'),
        task('Explain',3,'Explain a useful investigation',['Define General Science in your own words.','Use one GS11 report, proposed evidence and possible benefit.','State what the report has not yet established.']),
        task('Driving Question Board',4,'Our Driving Question Board',['Post evidence we have and questions still open.','Sort observation, cause and usefulness questions.','Keep untested cause questions on the board.'],mode='sort; evidence vote'),
        task('Model Building',2,'Version 0 · draw your evidence model',['Observation → question → evidence → explanation → possible use','Add one GS11 case; mark missing evidence with a question mark.']),
        task('Model Building',2,'Individual exit · save your first response',['Explain General Science and one possible benefit.','Use a GS11 case and name evidence still needed.'],do='Collect or securely save each individual exit before the final quiz feedback. The later quiz is reinforcement, not independent exit evidence.')],
        'record':{'headers':['Case','Reported observation','Question','Evidence needed','Possible benefit'],'rows':[['A','','','',''],['B','','','',''],['C','','','','']],'row_height':.85}}
    ess={'code':'RN1','short':'Exact_Number_Classes','goals':['Classify exact values with reasons.','Write a fraction for each rational example.','Compare number classes using your records.'],
         'words':'exact value: the value as written\n\nrepresentation: a way to write a value',
         'slides':pred('Where would you place 0, √9 and √2? Keep a first classification and reason.')+[
         task('Observe',3,'RN1 · prerequisite diagnostic',['Calculate −4 + 7.','Calculate 3/4 + 1/2; show your working.'],do='Give three minutes individually. Privately note fraction-addition support needs; do not replace the nine-minute classification task.'),
         s('Observe',9,'RN1 · classify every exact value','cards',values=['−3','0','2/5','0.125','0.333…','√9','√2','π'],caption='3 repeats forever in 0.333… · Give fraction forms and identify integers.',timer='9:00',mode='classify alone'),
         task('Observe',4,'Compare reasons and fraction forms',['Compare all eight classifications.','Check fraction representations and integer membership.','Keep a question where your reasons differ.'],mode='compare in pairs'),
         s('Explain',2,'The exact rational-number rule','equation',text='a/b, where a and b are integers and b ≠ 0',caption='A rational number has at least one such exact representation.'),
         s('Explain',3,'Check the fraction evidence','table',headers=['Exact value','Equal fraction','Integer?'],rows=[['−3','−3/1','Yes'],['0','0/1','Yes'],['2/5','2/5','No'],['0.125','1/8','No'],['0.333…','1/3','No'],['√9 = 3','3/1','Yes']],height=3.7,size=22,caption='√2 and π are established irrational examples; a short display is not a proof.'),
         s('Explain',3,'How the number classes fit together','sets',integers=['−3','0','√9 = 3'],other_rational=['2/5','0.125 = 1/8','0.333… = 1/3'],irrational=['√2','π'],caption='Use exact values; do not classify every radical as irrational.'),
         task('Driving Question Board',4,'Our Driving Question Board',['Post a classification supported by a fraction.','Keep questions about exact values and displays.','Save the display investigation for Lesson 2.'],mode='sort questions'),
         task('Model Building',2,'Build your own number-class model',['Draw real, rational and integer regions.','Place all RN1 values using your fraction evidence.']),
         task('Model Building',2,'Individual exit · classify with reasons',['Classify −3, √9 and π.','Give fraction evidence or the established irrational classification.'],do='Save the individual exit before the final quiz. Do not replace its reasons with the class distribution.')],
         'record':{'headers':['Exact value','Rational / irrational','Fraction / reason','Integer?'],'rows':[[v,'','',''] for v in ['−3','0','2/5','0.125','0.333… (3 repeats)','√9','√2','π']]}}
    core={'code':'CRN1','short':'Zero_Parity_and_Primes','goals':['Classify whole numbers with reasons.','Use positive factor pairs to check a claim.','Revise a number label using evidence.'],
          'words':'whole numbers: 0, 1, 2, …\n\nfactor pair: two positive integers whose product is the number',
          'slides':pred('Could 0, 1 and 9 be prime? Record one reason before comparing.')+[
          s('Observe',8,'CRN1 · classify all nine whole numbers','cards',values=['0','1','2','3','4','9','11','15','21'],caption='Odd/even AND prime/composite/neither · Positive factor pairs for 9 and 15.',timer='8:00',mode='work individually'),
          task('Observe',6,'Compare the two kinds of classification',['Compare all nine numbers and your reasons.','Check the positive factor pairs for 9 and 15.','Decide whether every odd whole number is prime.'],mode='compare in pairs'),
          s('Explain',2,'Is zero even?','equation',text='0 = 2 × 0',caption='Even means two times an integer; parity does not decide prime status.'),
          s('Explain',3,'Positive divisors decide prime status','table',headers=['Case','Positive-divisor evidence','Class'],rows=[['1','Only the divisor 1','Neither'],['2','Exactly 1 and 2','Prime'],['9','1, 3 and 9','Composite'],['0','Not an integer greater than 1','Neither']],size=22,caption='Prime and composite numbers here must be greater than 1.'),
          s('Explain',3,'One counterexample checks the label','table',headers=['Number','Positive factor pairs','What follows?'],rows=[['9','(1, 9), (3, 3)','Odd and composite'],['15','(1, 15), (3, 5)','Odd and composite']],size=24,height=2.5,caption='Every whole number n is rational as n/1; none is irrational.'),
          task('Driving Question Board',4,'Our Driving Question Board',['Post the claim your factor evidence corrected.','Ask how whole numbers fit among real numbers.','Keep new exact-number questions for Lesson 2.'],mode='sort questions'),
          task('Model Building',4,'Revise the supply label',['Keep the original “Every odd count is prime” claim.','Add a counterexample with positive-divisor evidence.','Keep parity and prime status as separate decisions.']),
          task('Model Building',2,'Individual exit · 21 and 0',['Classify both by parity and prime/composite/neither.','Give divisor or multiplication evidence.'],do='Save each individual exit before the last quiz. Use 21 factor pairs (1,21),(3,7) and 0=2×0 in the private key.')],
          'record':{'headers':['Number','Odd / even','Prime / composite / neither','Reason'],'rows':[[str(v),'','',''] for v in [0,1,2,3,4,9,11,15,21]]}}
    return {'gensci_1_1':gs,'essmath_1_1':ess,'coremath_1_1':core}


def questions():
    q={}
    m='gensci_1_1'
    q[m,1]=[
      quiz(m,1,1,6,'Which question could a temperature measurement help answer?',
           ['Which gate colour is prettiest?','Which lunchbox do you like most?','How do the lunchbox temperatures compare?','Which science topic is your favourite?'],'C',
           'Comparing temperatures asks about a measurable property. A measurement alone does not decide a personal preference.',
           ['Colour preference is a value judgement.','Liking a lunchbox is a preference.','A favourite topic is a preference.'],
           'A value judgement such as which gate colour is prettiest is not settled by measurement alone.','Recognise an evidence-seeking question.','After the inquiry definition; before the preference comparison.'),
      quiz(m,1,2,8,'The garden report gives fewer seedlings after a dry week. What is established?',
           ['Dry weather was the only cause.','A lower seedling count was reported.','Pests caused the seedling loss.','Watering will certainly solve the problem.'],'B',
           'The reported lower count is evidence to investigate. The report alone does not establish a cause or guarantee a solution.',
           ['An exclusive cause has not been tested.','Pests have not been measured or established.','The report does not test a solution.'],
           'Reported observations are warmth, reddish-brown patches and lower seedling count, not established causes.','Separate a reported observation from a cause claim.','After learners write a bounded GS11 explanation.'),
      quiz(m,1,3,11,'What should support a proposed scientific explanation?',
           ['The most confident speaker','A guess repeated by many people','The benefit we hope for','Relevant observable or measurable evidence'],'D',
           'An explanation needs relevant evidence and remains open to revision. Confidence, repetition and hoped-for benefits do not replace checking.',
           ['Confidence is not evidence of the cause.','Agreement does not replace investigation.','A possible benefit is not proof of an explanation.'],
           'Investigations need observable/measurable evidence and explanations open to revision.','Reinforce evidence before a useful explanation.','After the individual exit is saved; before the summary.')]
    q[m,2]=[
      quiz(m,2,1,6,'Which GS12 statement is a reported observation?',
           ['The paper beside the closed window is wet.','Rain must have entered through a gap.','Someone may have spilled water.','Where did the water come from?'],'A',
           'Wet paper is reported. Rain entering and a spill interpret possible causes; asking where the water came from is a question.',
           ['Rain entering is an inference about a cause.','A possible spill is an inference.','This asks for information rather than reporting it.'],
           '1,3,6 observations; 2,4 inferences; 5 question.','Distinguish observation, inference and question.','After solo classification, comparison and the explanation table.'),
      quiz(m,2,2,7,'An empty cup is beside wet paper. Which conclusion is justified?',
           ['It proves somebody spilled the water.','It rules out rain entering.','A spill is possible, but not proved.','It proves condensation was the cause.'],'C',
           'An empty cup is consistent with a spill, but it does not show where the water came from. Other explanations remain possible.',
           ['The cup does not identify the cause.','The cup does not rule out rain.','Condensation would also need supporting evidence.'],
           'An empty cup is not proof of a spill.','Limit a conclusion to what the evidence supports.','After comparing consistent-with and proof claims.'),
      quiz(m,2,3,11,'Which follow-up could help test the rain explanation without accusing anyone?',
           ['Name the person nearest the window.','Inspect weather records and state their limits.','Repeat the spill claim more confidently.','Treat the empty cup as conclusive proof.'],'B',
           'Weather records could add relevant evidence about rain. They have limits and would not alone prove how the paper became wet.',
           ['Proximity is not evidence of responsibility.','Repetition supplies no new evidence.','The cup does not establish a spill.'],
           'Inspecting weather records or asking whether water was placed there can help; each has limitations.','Choose relevant additional evidence without overclaiming.','After the written observation/two-inferences/follow-up exit is saved.')]
    m='essmath_1_1'
    q[m,1]=[
      quiz(m,1,1,6,'Which is a valid integer-fraction representation of zero?',
           ['0/0','0/1','1/0','Zero has no fraction representation.'],'B',
           '0/1 equals zero and has a nonzero denominator. Therefore zero is rational.',
           ['A zero denominator is not permitted.','A zero denominator is not permitted.','0/1 is a valid representation.'],
           'Rational:−3=−3/1,0=0/1,2/5,0.125=1/8,0.333…=1/3,√9=3=3/1.','Use the nonzero-denominator rule.','After the rational-number definition and individual fraction evidence.'),
      quiz(m,1,2,8,'How should the exact number √9 be classified?',
           ['Irrational because it has a root sign','Rational but not an integer','Neither rational nor irrational','Integer and rational because √9 = 3'],'D',
           '√9 equals 3 exactly, and 3 = 3/1. It is both an integer and a rational number.',
           ['A root sign does not always give an irrational value.','3 is an integer as well as rational.','√9 is a real number with exact value 3.'],
           'Integer members:−3,0,√9. Irrational:√2 andπ.','Distinguish a symbol from its exact value.','After the complete classification explanation and set diagram.'),
      quiz(m,1,3,11,'Which statement follows from the integer-fraction rule?',
           ['Every integer is rational.','Every rational number is an integer.','No irrational number is real.','Every real number is rational.'],'A',
           'Any integer n can be written as n/1. Rational numbers also include non-integers, and real numbers include irrationals.',
           ['2/5 is rational and not an integer.','√2 and π are irrational real numbers.','√2 and π are counterexamples.'],
           'A rational number is expressible as a/b for integers a,b with b≠0.','Connect integer and rational membership.','After the individual diagram and written exit have been saved.')]
    q[m,2]=[
      quiz(m,2,1,6,'Which statement uses exactness and approximation correctly?',
           ['π = 3.14 exactly','√2 becomes rational on a calculator','√16 is irrational','π ≈ 3.14'],'D',
           '3.14 is a rounded approximation to π. The approximation sign preserves that distinction.',
           ['Exact π is not equal to 3.14.','A finite display does not change the exact number.','√16 equals the rational number 4.'],
           'π≈3.14, not exact equality.','Choose notation that matches a rounded value.','After correcting the three RN2 exact-value claims.'),
      quiz(m,2,2,7,'Since 1.4² = 1.96 and 1.5² = 2.25, which bound is correct?',
           ['√2 < 1.4','1.4 < √2 < 1.5','√2 = 1.5','√2 > 1.5'],'B',
           '2 lies between 1.96 and 2.25. Its positive square root therefore lies between 1.4 and 1.5.',
           ['1.4² is smaller than 2.','1.5² is 2.25, not 2.','1.5² is already greater than 2.'],
           '1.4²=1.96<2<2.25=1.5², so 1.4<√2<1.5.','Use squared bounds to locate a positive root.','After learners have bracketed √2 and compared the squares.'),
      quiz(m,2,3,11,'Both 1.411 and 1.414 round to 1.41 at two decimal places. What follows?',
           ['The exact numbers are different despite the same rounded display.','The exact numbers are equal.','Both exact numbers are 1.41.','Rounding preserves every digit of the exact numbers.'],'A',
           'Rounding loses information: 1.411 and 1.414 remain different exact values even though both are communicated as 1.41.',
           ['Their third decimal digits differ.','1.41 is the common rounded value, not either exact value.','Digits beyond the stated precision are lost.'],
           'Examples 1.411 and 1.414 both round to 1.41.','Explain information lost in rounding.','After the individual 1/3 versus finite-decimal exit is saved.')]
    m='coremath_1_1'
    q[m,1]=[
      quiz(m,1,1,5,'Which reason establishes that zero is even?',
           ['Zero has no digits.','0 = 2 × 0','Zero is prime.','Every whole number is even.'],'B',
           'An even integer is twice an integer. Zero equals 2 × 0, so zero is even; this says nothing by itself about being prime.',
           ['Digit count is not the parity rule.','Zero is not prime.','The source list includes odd whole numbers.'],
           'Odd9 is composite;0=2×0 is even.','Justify zero parity using the defining multiplication.','After individual classification and the zero-parity explanation.'),
      quiz(m,1,2,7,'Why does 9 disprove “Every odd whole number is prime”?',
           ['9 is even.','9 has no positive divisors.','9 is odd and has divisors 1, 3 and 9.','9 is not a whole number.'],'C',
           '9 is an odd whole number with more than two positive divisors. One such counterexample disproves the universal claim.',
           ['9 is odd.','1, 3 and 9 are positive divisors.','9 is a whole number.'],
           'Factorpairs9:(1,9),(3,3);15:(1,15),(3,5).','Use a factor-based counterexample.','After the factor-pair comparison and counterexample explanation.'),
      quiz(m,1,3,10,'How is 1 classified by prime/composite status here?',
           ['Prime because it is odd','Composite because it is a whole number','Both prime and composite','Neither: it has only one positive divisor'],'D',
           '1 has only the positive divisor 1. Prime and composite classifications here require an integer greater than 1.',
           ['Oddness does not imply primality.','Being whole does not imply being composite.','The categories are not both applicable to 1.'],
           'Prime:2,3,11; composite:4,9,15,21; neither:0,1.','Apply the greater-than-one/divisor conditions.','After the saved written exit on 21 and 0, as reinforcement on a different listed case.')]
    q[m,2]=[
      quiz(m,2,1,5,'Which integer-fraction form equals the exact number 0.125?',
           ['1/8','1/125','125/10','No fraction can equal it.'],'A',
           '0.125 = 125/1000 = 1/8. A terminating decimal is an exact rational number when treated as written.',
           ['1/125 equals 0.008, not 0.125.','125/10 equals 12.5.','The fraction 1/8 equals it exactly.'],
           '0.125=1/8,0.777…=7/9,√16=4/1,22/7.','Represent a terminating decimal exactly.','After the rational fraction evidence table.'),
      quiz(m,2,2,6,'Which statement correctly compares exact π and 22/7?',
           ['Both are irrational.','They are exactly equal.','π is irrational; 22/7 is a rational approximation.','π is rational because 22/7 is a fraction.'],'C',
           '22/7 is an integer ratio, so it is rational. Exact π is irrational and is not equal to 22/7.',
           ['22/7 is rational.','The source explicitly distinguishes the values.','An approximation does not redefine the exact constant.'],
           'π is not22/7. Every whole number is rational; real numbers also include irrational values.','Distinguish an irrational constant from its rational approximation.','After the exact-constant/display comparison.'),
      quiz(m,2,3,10,'For 0.777… with 7 repeating forever, which statement is correct?',
           ['It is irrational because it never ends.','It is rational and equals 7/9.','It is a finite approximation to 7/9.','It is a whole number.'],'B',
           'The repeating decimal 0.777… equals 7/9 exactly. A decimal can be infinite and rational when it repeats.',
           ['Repeating non-terminating decimals can be rational.','The dots specify endless repetition, not a finite truncation.','7/9 is not a whole number.'],
           '0.125=1/8,0.777…=7/9,√16=4/1,22/7.','Distinguish exact recurring notation from a finite screen.','After the saved individual exit; repeats the representation principle with a different listed value.')]
    return q


def main():
    inventory=json.loads((CONTROL/'inventory.json').read_text())
    units={u['module']:u for u in inventory['units']}
    first=first_lessons(); qs=questions()
    for module, lesson in first.items():
        p=CONTROL/'specs'/(module+'.json');data=json.loads(p.read_text())
        data['lessons']['1']=lesson
        for n in [1,2]:
            l=data['lessons'][str(n)]
            if module=='coremath_1_1':
                l['inquiry']='Does odd imply prime, and where do 0 and 1 belong?' if n==1 else 'How do exact π and the rational approximation 22/7 differ?'
            if module=='essmath_1_1' and n==2:
                l['inquiry']='Is π exactly 3.14?'
                previous=l['slides'][7]
                l['slides'][6].update({'kind':'numberline','bounds':previous.get('bounds',l['slides'][6].get('bounds',[-3,2])),
                    'points':previous.get('points',l['slides'][6].get('points',[[-3,'−3'],[-.5,'−1/2'],[0,'0'],[2**.5,'√2'],[2,'2']])),
                    'headline':'1.4² = 1.96 < 2 < 2.25 = 1.5²',
                    'caption':'1.4 < √2 < 1.5. Locating √2 does not prove that it is irrational.'})
                l['slides'][7].update({'kind':'columns','columns':[
                    ['DIFFERENT EXACT VALUES','1.411 ≠ 1.414'],['SAME ROUNDED VALUE','Both round to 1.41\nat two decimal places.']],
                    'caption':'Rounding loses information; a shared rounded display does not make exact values equal.'})
                for key in ['bounds','points']:l['slides'][7].pop(key,None)
            if n==2:
                if module=='gensci_1_1':
                    for i,t in [(6,2),(7,3),(8,3),(10,2)]:l['slides'][i-1]['minutes']=t
                elif module=='essmath_1_1':
                    for i,t in [(6,2),(7,3),(8,3),(10,2)]:l['slides'][i-1]['minutes']=t
                else:
                    for i,t in [(5,3),(6,2),(7,3),(9,4)]:l['slides'][i-1]['minutes']=t
                l['slides'][-1]['do']='Save the individual written exit before the final quiz and its feedback. Keep first-attempt exit and quiz records separate.'
            for row in l['slides']:
                if row.get('timer'):
                    seconds=round(row['minutes']*60);row['timer']=f'{seconds//60}:{seconds%60:02}'
            l.update({'design_revision':REVISION,'quizzes':qs[module,n],
                'decisions':'User-authorised periodic quizzes. Preserve every source task and all source Observe subdivisions. Two one-minute checks use the existing ten-minute Explain/check allocation; a one-minute reinforcement check follows the saved exit within Model Building. Source phase totals remain unchanged. Real-class pacing and individual response-server provision require teacher review.',
                'preparation':'Print the complete source task and blank record. Prepare notebooks, pencils, second colour, board and timer. Configure the matching versioned question IDs only if the future server is available; otherwise record individual paper responses privately. Project class aggregates only after closure. No practical or personal measurements.',
                'route':'Source printed tasks; no invented practical, live poll chart, pupil response, media or URL. Native editable diagrams and source values. The response/report server is not implemented in this repository.'})
            if module=='coremath_1_1' or (module=='essmath_1_1' and n==2):
                l['decisions']+=' Corrected missing spaces in the source-derived student inquiry without changing its meaning.'
            if module=='essmath_1_1' and n==2:
                l['decisions']+=' Matched the rounded-display heading to an explicit 1.411 versus 1.414 comparison; moved the complete source number line beside its squared bounds. No required task or phase time changed.'
            validate_quizzes(l,module,n,units[module]['source_hashes'])
        data['status']='Lessons 1–2 authored for quiz-v1 review; all remaining lessons stay pre-quiz baselines.'
        p.write_text(json.dumps(data,indent=2,ensure_ascii=False))
        print(module,'Lessons 1–2; six source-backed questions')


if __name__=='__main__': main()
