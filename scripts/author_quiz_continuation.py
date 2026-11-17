#!/usr/bin/env python3
"""Source-specific quiz authoring after the six-deck review checkpoint.

Does not build decks. Preserve the six reviewed pilot specifications and sources.
"""
import argparse
import json
from pathlib import Path

from author_quiz_review_pilots import quiz
from curriculum_set_inventory import CONTROL
from lesson_quizzes import REVISION, validate_quizzes


def general_science():
    m='gensci_1_1'
    return {
      3:[
        quiz(m,3,1,6,'What is the mean of the printed paper A rises: 18, 20 and 22 mm?',
             ['60 mm','22 mm','20 mm','18 mm'],'C',
             'Add the three rises to get 60 mm, then divide by three readings: 20 mm. Keep the measurement unit.',
             ['60 mm is the sum, not the mean.','22 mm is the largest reading.','18 mm is the smallest reading.'],
             'Printed means A20 mm and B10 mm.','Calculate a mean with its unit.','After the individual calculations, comparison and worked mean; no later data used.'),
        quiz(m,3,2,8,'Which conclusion stays within the printed GS13 test?',
             ['Paper A is best for every job.','Paper A had greater mean rise in these conditions.',
              'Paper B had the greater mean rise.','The test establishes every paper property.'],'B',
             'The means are A 20 mm and B 10 mm in this small trial. The test compares water rise under stated conditions, not every property or use.',
             ['One water-rise test does not compare every possible job.','10 mm is smaller than 20 mm.','Other properties require other measurements.'],
             'Paper A shows greater mean rise in this small trial; the result does not establish every property of the paper or prove a microscopic explanation.',
             'Limit a conclusion to the measured property and conditions.','After the conditional conclusion and test-limit explanation.'),
        quiz(m,3,3,11,'You analysed GS13’s printed data without a practical. Which label is honest?',
             ['Our own experimental measurements','Proof of our hands-on measuring skill',
              'A measurement of every paper property','Analysis of printed illustrative readings'],'D',
             'Printed readings support data analysis and inference. They are not your own measurements and do not show that you carried out the measuring procedure.',
             ['The readings came from the supplied sheet.','Hands-on measuring was not observed.','Only water rise is represented.'],
             'Printed analysis provides inference/data skills, not evidence of hands-on measuring.',
             'Distinguish supplied data analysis from observed practical competence.','After the saved individual numerical conclusion and limit; reinforce honest data provenance.')],
      4:[
        quiz(m,4,1,6,'Tray P went from 10 seedlings to 6. How many seedlings were lost?',
             ['4','6','10','16'],'A',
             'The loss is the starting count minus the final count: 10 − 6 = 4 seedlings. The count change alone does not establish its cause.',
             ['6 is the final count, not the loss.','10 is the initial count.','Adding the counts does not give the loss.'],
             'Losses P4 and Q1; observed counts differ.','Use starting and final counts to describe a change.','After the individual count extraction and worked differences.'),
        quiz(m,4,2,8,'Why do GS14’s records fail to isolate water as the cause?',
             ['The initial counts were different.','No seedling counts were recorded.',
              'The water amounts were equal.','Light, temperature and location also differed.'],'D',
             'The water amounts and environments differed together. Light, temperature or location could also contribute, so the records do not isolate water.',
             ['Both trays started with 10 seedlings.','Monday and Friday counts are supplied.','P received 20 mL daily and Q 40 mL.'],
             'Less water may contribute, but light/temperature/location also differ, and counts alone do not identify mechanism.',
             'Identify a changed factor that confounds a causal claim.','After comparing the changed conditions and defending a bounded conclusion.'),
        quiz(m,4,3,11,'Which plan would better test the effect of water amount?',
             ['Change water, light and soil together.','Use one tray and assume its cause.',
              'Vary water; keep other conditions comparable and repeat.','Choose a cause before checking counts.'],'C',
             'Vary water while keeping relevant conditions comparable. Define the outcome and observation period, and use several trays per condition; uncertainty still remains.',
             ['Changing several factors together prevents isolating water.','One tray does not compare the two conditions.','A cause must be evaluated using evidence.'],
             'A fairer comparison varies water amount with comparable seed type, initial condition, soil, container, light and temperature, measures a defined outcome over a fixed interval and uses several trays per condition.',
             'Choose a fairer comparison with repeats.','After saving the individual confound and concrete design-change exit.')],
      5:[
        quiz(m,5,1,6,'Which career direction is supported by source A’s weather observations and forecasts?',
             ['Human-health research','Weather/climate science','A guaranteed job placement','A specified salary grade'],'B',
             'Source A describes weather/climate observations, analysis, forecasts and early warnings. This supports a weather/climate science direction, without promising a job or salary.',
             ['The human-health research role is described by source B.','The summary does not guarantee employment.','The summary does not establish a salary.'],
             'Weather/climate scientist is a reasonable inference from A; suggested evidence includes instrument measurements and weather records.',
             'Connect a career direction to its stated institutional evidence.','After individual chart construction, source checking and the supported-direction explanation.'),
        quiz(m,5,2,8,'What remains unverified by the two GS15 source summaries?',
             ['Entry qualifications for a particular course.','A weather/climate observation role.',
              'A human-health research role.','That the summaries describe institutional work.'],'A',
             'The summaries describe institutional roles. They do not specify entry qualifications; a training question needs a separate reliable source check.',
             ['Source A supports that role.','Source B supports that role.','The summaries explicitly concern institutional roles.'],
             'The sources support institutional roles, not every proposed job title, duty, qualification or salary.',
             'Distinguish source-supported roles from training claims.','After explaining benefits and source limits; career choices remain private.'),
        quiz(m,5,3,11,'Your chart proposes a question about rainfall patterns. How should you label it?',
             ['An exact quotation from source A','A guaranteed duty of every weather scientist',
              'An established entry qualification','My proposed example of a science question'],'D',
             'The source supports a weather/climate role. Your suggested rainfall question is a proposed example, rather than a quotation, guaranteed duty or qualification.',
             ['The proposed question is not an exact source quotation.','The summary does not specify every person’s duties.','A question about rainfall does not establish a qualification.'],
             'Require learners to label proposed questions/evidence as examples and training as unverified.',
             'Distinguish a proposed example from a source statement.','After the saved chart/reflection; tests source labelling rather than the learner’s career preference.')],
      6:[
        quiz(m,6,1,7,'Which claim respects the earlier GS13 paper test?',
             ['A is always best for every material use.','The trial proves how paper works microscopically.',
              'A had greater mean rise in the stated trial.','Every property of A was tested.'],'C',
             'The water-rise comparison supports a limited statement about this trial. A proposed material choice still needs testing of the property required for that job.',
             ['A single measured property does not settle every use.','The trial does not establish a microscopic mechanism.','Only water rise under stated conditions was compared.'],
             'One absorption test cannot certify a product for every use.',
             'Replace an all-purpose claim with a test-bounded conclusion.','After the evidence/use chain and limited-claim comparison, using previously taught data only.'),
        quiz(m,6,2,8,'Which peer comment would best help make a science-use message defensible?',
             ['Remove every uncertainty to sound confident.','Name the evidence and limit the claimed use.',
              'Choose the most popular wording regardless of evidence.','Treat a proposed benefit as a measured result.'],'B',
             'A defensible message connects evidence to a possible decision and states its limits. Respectful critique concerns the claim and reasoning, rather than the person.',
             ['Removing a real uncertainty makes the claim less defensible.','Popularity does not replace evidence.','A suggested application has not necessarily been tested.'],
             'Distinguish established trial evidence from suggested application.',
             'Use evidence and limits in respectful revision.','After learners explain why their evidence-based revision improves the message.'),
        quiz(m,6,3,11,'What should happen to a question whose required evidence is still missing?',
             ['Keep it open and name the evidence still needed.','Erase it because the unit is ending.',
              'Mark it answered after a confident vote.','Replace its evidence with a career preference.'],'A',
             'Keep an unanswered question visible and identify evidence that could help. Completion of a message or unit does not establish an answer.',
             ['An ending does not supply missing evidence.','A vote cannot replace the relevant evidence.','A personal preference does not answer the evidence question.'],
             'Keep career information within GS15 source limits.',
             'Preserve a still-open evidence question after communication.','After the question-board audit, revised message and saved independent exit.')]
    }


def essential_mathematics():
    m='essmath_1_1'
    return {
      3:[
        quiz(m,3,1,5,'What is (3/5) ÷ (−9/10) as an exact fraction?',
             ['−2/3','2/3','−3/2','−27/50'],'A',
             'Divide by multiplying by the nonzero divisor’s reciprocal: (3/5) × (−10/9) = −2/3. A positive value divided by a negative value is negative.',
             ['The divisor is negative, so the quotient is negative.','This reverses the required quotient.','This multiplies by the divisor instead of its reciprocal.'],
             '(d)(3/5)×(−10/9)=−2/3.','Use the divisor’s reciprocal and retain the sign.','After all exact calculations, checks and worked results.'),
        quiz(m,3,2,7,'Why is 0 ÷ 0 undefined in real-number division?',
             ['No real x can satisfy 0 × x = 0.','It has the unique answer 0.',
              '0 × x = 0 has no unique solution.','It has the unique answer 1.'],'C',
             'Every real x satisfies 0 × x = 0, so there is no unique quotient. For a nonzero numerator, 0 × x = a has no solution instead.',
             ['Every real x satisfies that equation.','Zero is one of many solutions, not a unique quotient.','One is one of many solutions, not a unique quotient.'],
             'Division a÷0 would require a unique x with 0 x=a: no solution if a≠0 and no unique solution if a=0.',
             'Distinguish no solution from no unique division result.','After both cases of division by zero are explained; no operation-order examples from Lesson 4.'),
        quiz(m,3,3,10,'Which product corrects the signed-multiplication error in RN3?',
             ['(−2) × (−5) = −10','(−2) × (−5) = −7','(−2) × (−5) = 7','(−2) × (−5) = 10'],'D',
             'The product of the two negative values is positive: (−2) × (−5) = 10. Check both the sign and the magnitude.',
             ['Two negative factors give a positive product.','This adds the values instead of multiplying.','The magnitudes multiply to 10, not 7.'],
             '(−2)×(−5)=10; common denominators are needed for addition, giving 5/4.',
             'Correct the sign of a product of negative numbers.','After the saved common-denominator exit; reinforces a different operation from the source task.')],
      4:[
        quiz(m,4,1,6,'Why do (−3)² and −3² have different values?',
             ['Every power ignores a negative sign.','Both expressions have the base −3.',
              'Parentheses include the sign in the first base only.','A calculator may choose either exact value.'],'C',
             '(−3)² squares the whole negative value and equals 9. Without those parentheses, −3² means −(3²), which equals −9.',
             ['The sign’s grouping matters.','Without parentheses the squared base is 3.','The written expressions determine their mathematical values.'],
             'D=−(3²)=−9; parentheses determine whether the negative sign is part of the base.',
             'Identify the base of a power using grouping.','After individual work and the A–D worked comparison.'),
        quiz(m,4,2,8,'How should 6 ÷ 3 × 2 be evaluated?',
             ['(6 ÷ 3) × 2 = 4','6 ÷ (3 × 2) = 1','6 ÷ (3 + 2) = 6/5','(6 × 3) ÷ 2 = 9'],'A',
             'Multiplication and division have equal priority, so process them from left to right: 6 ÷ 3 = 2, then 2 × 2 = 4.',
             ['This adds parentheses not present in the expression.','The expression requests multiplication, not addition.','This changes the stated operations.'],
             'C=(6÷3)×2=4 because multiplication/division have equal priority and are processed left to right.',
             'Apply equal-priority processing rather than an incorrect mnemonic.','After left-to-right processing and unambiguous entry have been explained.'),
        quiz(m,4,3,11,'Which is an unambiguous calculator entry for A = 3/4 − [1/2 ÷ (−2)]?',
             ['((3 ÷ 4) − (1 ÷ 2)) ÷ (−2)','(3 ÷ 4) − ((1 ÷ 2) ÷ (−2))',
              '(3 ÷ 4) − ((1 ÷ 2) × (−2))','(3 ÷ 4) + ((1 ÷ 2) ÷ (−2))'],'B',
             'The bracketed division applies to 1/2 and −2 only. Then subtract that result from 3/4; the exact result is 1.',
             ['This divides the entire difference by −2.','This changes division into multiplication.','This changes subtraction into addition.'],
             'Correct entry can be(3÷4)−((1÷2)÷(−2)); input method varies by calculator.',
             'Preserve the intended grouping in an entry.','After the saved first-operation exit; use the already-taught complete expression.')],
      5:[
        quiz(m,5,1,5,'What is the exact reciprocal of −0.2?',
             ['0.2','5','−1/5','−5'],'D',
             '−0.2 = −1/5, so its reciprocal is −5. Their exact product is (−1/5) × (−5) = 1.',
             ['Changing the sign alone does not give a product of 1.','The reciprocal of a negative number remains negative.','−1/5 is the original value, not its reciprocal.'],
             'The reciprocal of a negative number is negative.',
             'Use the product-of-one condition for a negative reciprocal.','After actual calculator records, product checks and the complete reciprocal table.'),
        quiz(m,5,2,7,'Why does zero have no real reciprocal?',
             ['Zero’s reciprocal is zero.','0 × r always equals 0, never 1.',
              'Zero’s reciprocal is one.','A calculator error is a new real number.'],'B',
             'A reciprocal must multiply by the original value to give 1. Zero times any real r is 0, so it cannot pass that test.',
             ['0 × 0 is 0, not 1.','0 × 1 is 0, not 1.','An error message is not a real reciprocal.'],
             '0 r cannot equal 1, so zero has no reciprocal.',
             'Explain the zero exception using the defining product.','After the exact/rounded product comparison and zero explanation.'),
        quiz(m,5,3,10,'Which statement about the displayed 0.707106781 for 1/√2 is correct?',
             ['It is an approximation to the exact reciprocal.','It is exactly equal to 1/√2.',
              'The display makes √2 rational.','It shows that no reciprocal exists.'],'A',
             'The exact reciprocal is 1/√2 = √2/2. Its finite decimal display is approximate; a rounded product can differ slightly from 1.',
             ['The finite decimal omits part of the exact value.','A finite display does not change the exact number class.','√2 is nonzero, so it has a reciprocal.'],
             'A calculator display is approximate for the irrational reciprocal.',
             'Keep an exact reciprocal distinct from a rounded display.','After the saved reciprocal-of-3/4 exit; reinforces exactness with the already-investigated √2 example.')]
    }


def core_mathematics():
    m='coremath_1_1'
    return {
      3:[
        quiz(m,3,1,5,'Which exact value is the reciprocal of 2/3?',
             ['−2/3','2/3','−3/2','3/2'],'D',
             '1 ÷ (2/3) = 3/2, and (2/3) × (3/2) = 1. A reciprocal undoes multiplication by the original nonzero value.',
             ['This is the additive opposite, not the reciprocal.','Multiplying 2/3 by itself does not give 1.','A positive original has a positive reciprocal.'],
             'Results1/4,−1/5,3/2,1/√2. Each nonzero original times its reciprocal equals1.',
             'Find a reciprocal by division and verify the product.','After all CRN3 divisions, checks and the worked reciprocal table.'),
        quiz(m,3,2,7,'Which pair correctly distinguishes the reciprocal and additive opposite of 4?',
             ['Reciprocal 1/4; opposite −4','Reciprocal −4; opposite 1/4',
              'Reciprocal 4; opposite −4','Reciprocal 1/4; opposite 4'],'A',
             '4 × 1/4 = 1 tests the reciprocal. 4 + (−4) = 0 tests the additive opposite. The two undoing operations are different.',
             ['This swaps the two different inverse operations.','4 × 4 is 16, not 1.','4 + 4 is 8, not 0.'],
             'Reciprocal4 is1/4, while its additive opposite is−4.',
             'Match each inverse to its defining operation.','After the zero-domain explanation and reciprocal/opposite comparison.'),
        quiz(m,3,3,10,'Could zero have a real reciprocal r?',
             ['Yes: r = 0','No: 0 × r is always 0, never 1','Yes: r = 1','Yes: r = −1'],'B',
             'Every real r gives 0 × r = 0. A reciprocal would require a product of 1, so zero has no real reciprocal.',
             ['0 × 0 = 0, not 1.','0 × 1 = 0, not 1.','0 × (−1) = 0, not 1.'],
             'For0,0r=0 for every real r, never1; so not defined.',
             'Use a product argument for the zero exception.','After the saved individual −5 reciprocal/opposite exit; no later mixed-number or table inputs.')],
      4:[
        quiz(m,4,1,5,'What is the reciprocal of the entire signed value −2½?',
             ['−2/3','2/5','−2/5','−5/2'],'C',
             '−2½ = −5/2, so its reciprocal is −2/5. The sign belongs to the whole mixed number; (−5/2) × (−2/5) = 1.',
             ['Swapping mixed-number digits misrepresents the value.','The reciprocal of a negative original must be negative.','−5/2 is the original value, not its reciprocal.'],
             '1½=3/2 gives2/3;−2½=−5/2 gives−2/5;0.25=1/4 gives4;−0.4=−2/5 gives−5/2;1/9 gives9.',
             'Convert the whole signed mixed number before inversion.','After all five conversions, individual product checks and the worked table.'),
        quiz(m,4,2,7,'Which product exposes the proposed −2/3 reciprocal of −2½ as incorrect?',
             ['(−5/2) × (−2/3) = 1','(−5/2) × (−2/3) = −1',
              '(−5/2) × (−2/3) = 0','(−5/2) × (−2/3) = 5/3'],'D',
             'The product is 10/6 = 5/3, which is not 1. The proposed value therefore fails the defining reciprocal test.',
             ['The numerator and denominator give 10/6, not 1.','The product of two negative values is positive.','Neither factor is zero.'],
             'Convert the entire signed mixed number first; the proposed−2/3 does not multiply−5/2 to1.',
             'Use a product check to reject a plausible digit-swapping claim.','After the proposed/actual product comparison and full signed-value explanation.'),
        quiz(m,4,3,10,'Which is the exact reciprocal of −0.4?',
             ['−5/2','−2/5','5/2','−4'],'A',
             '−0.4 = −2/5, so its reciprocal is −5/2. Multiplying those fractions gives 1; the negative sign is retained.',
             ['−2/5 is the original value.','The negative original needs a negative reciprocal.','(−0.4) × (−4) = 1.6, not 1.'],
             '1½=3/2 gives2/3;−2½=−5/2 gives−2/5;0.25=1/4 gives4;−0.4=−2/5 gives−5/2;1/9 gives9.',
             'Convert a terminating decimal before finding its reciprocal.','After the saved 0.25 exit; reinforces the representation rule with another taught signed value.')],
      5:[
        quiz(m,5,1,5,'Which statement correctly reads the table’s precision?',
             ['Both 0.3125 and 0.2778 are exact reciprocals.','1/3.2 = 0.3125; 1/3.6 ≈ 0.2778.',
              '1/3.2 ≈ 0.3125; 1/3.6 = 0.2778 exactly.','No decimal table entry can ever be exact.'],'B',
             '1/3.2 equals 5/16 = 0.3125 exactly. 1/3.6 equals 5/18, whose recurring decimal is rounded to 0.2778 in the table.',
             ['5/18 is not exactly the terminating decimal 0.2778.','This gives exact equality to the rounded 5/18 entry.','A terminating exact reciprocal can be shown in full.'],
             '1/3.2=0.3125 exact;1/3.6≈0.2778, since exact5/18 repeats.',
             'Distinguish a full terminating value from a rounded table entry.','After all table tasks and the exact/rounded comparison; no calculator-use evidence claimed.'),
        quiz(m,5,2,7,'Since 32 = 10 × 3.2, how does 1/32 relate to 1/3.2?',
             ['It is ten times as large.','It is unchanged.','It is one tenth as large.','It is ten more.'],'C',
             'Multiplying the nonzero input by 10 divides its reciprocal by 10. Thus 1/32 = 0.3125 ÷ 10 = 0.03125.',
             ['This scales the reciprocal in the same direction as the input.','Changing the nonzero input changes its reciprocal.','The relationship is multiplicative, not additive.'],
             '32=10×3.2 so1/32=0.03125;',
             'Track inverse scaling instead of guessing decimal positions.','After the complete scaling table and the explanation of its inverse factor.'),
        quiz(m,5,3,10,'Which statement respects the precision of the supplied table?',
             ['1/0.036 = 27.78 exactly','1/0.036 = 0.2778 exactly',
              'The table proves actual calculator use','1/0.036 ≈ 27.78'],'D',
             '0.036 is 0.01 × 3.6, so its reciprocal is 100 × (1/3.6). Scaling the rounded entry gives an approximation, 27.78.',
             ['The scaled rounded entry remains approximate.','This omits the inverse factor of 100.','Reading a table is not an observed calculator action.'],
             '0.036=0.01×3.6 so1/0.036≈27.78.',
             'Preserve approximation when scaling a rounded entry.','After the saved exact/approximate exit; reinforce why the scaled table entry needs ≈.')]
    }


def author_mathematics(module):
    p=CONTROL/'specs'/(module+'.json');data=json.loads(p.read_text())
    inv=json.loads((CONTROL/'inventory.json').read_text());u=next(u for u in inv['units'] if u['module']==module)
    authored=essential_mathematics() if module=='essmath_1_1' else core_mathematics()
    for n,qs in authored.items():
        l=data['lessons'][str(n)]
        l['record']['row_height']=.65
        if module=='essmath_1_1' and n==3:
            l['slides'][4]['widths']=[1.4,7.0,3.4]
            repair=' Widened the Item column after rendered inspection found its header wrapping within the word; increased blank calculation-row writing space.'
            if repair not in l.get('decisions',''):l['decisions']=l.get('decisions','')+repair
        if module=='essmath_1_1' and n==4:
            l['slides'][5]['widths']=[2.4,6.2,3.2]
            repair=' Widened the Expression header after PDF text/visual checks found an intra-word wrap; all source expressions and values retained.'
            if repair not in l.get('decisions',''):l['decisions']=l.get('decisions','')+repair
        if module=='coremath_1_1':
            if n==3:l['inquiry']='Why is −4 not the reciprocal of 4?'
            if n==5:
                l['slides'][2].update(timer='10:00',mode='table tasks alone')
                l['space_after_commas']=True
                repair=' Added spaces after source-card commas so the complete reciprocal list wraps between numbers instead of splitting a decimal; source values/text tokens unchanged. Explicit table-task timer retained.'
                if repair not in l.get('decisions',''):l['decisions']=l.get('decisions','')+repair
        if l.get('design_revision')==REVISION:
            validate_quizzes(l,module,n,u['source_hashes']);continue
        explain=[i for i,r in enumerate(l['slides']) if r['phase']=='Explain']
        l['slides'][explain[0]]['minutes']-=1;l['slides'][explain[-1]]['minutes']-=1
        model=next(r for r in l['slides'] if r['phase']=='Model Building');model['minutes']-=1
        l['slides'][-1]['do']='Save the individual written exit before final reinforcement feedback. Keep first-attempt exit and quiz records separate.'
        l.update(design_revision=REVISION,quizzes=qs)
        l['decisions']=l.get('decisions','')+' Source mathematics guidance governs this lesson. Retain every original Observe subdivision and source task. Two one-minute response/feedback pairs use the existing ten-minute Explain/check allocation; one one-minute reinforcement follows the saved two-minute exit within Model Building. Phase totals unchanged; teacher must assess 30+30-second quiz pacing. Blank calculation rows allow 0.65 inches for writing. No later assessment inputs or fabricated device evidence.'
        for q in qs:q['accuracy_check']='Compared all choices with the full source unit and exact cited key; independently verified fraction/sign/grouping/domain/scaling arithmetic in qa/Quiz_Continuation_content_checks.json.'
        for r in l['slides']:
            if r.get('timer'):
                seconds=round(r['minutes']*60);r['timer']=f'{seconds//60}:{seconds%60:02}'
        validate_quizzes(l,module,n,u['source_hashes'])
    ready=sum(l.get('design_revision')==REVISION for l in data['lessons'].values())
    data['status']=f'{ready} of {len(data["lessons"])} lessons authored for quiz-v1; any others remain pre-quiz baselines. External review gates open.'
    p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n');print(module,'authored Lessons 3–5; pilots preserved')


def author(module):
    if module in ['essmath_1_1','coremath_1_1']:return author_mathematics(module)
    assert module=='gensci_1_1'
    p=CONTROL/'specs'/(module+'.json');data=json.loads(p.read_text())
    inv=json.loads((CONTROL/'inventory.json').read_text());u=next(u for u in inv['units'] if u['module']==module)
    questions=general_science()
    for n in range(3,8):
        l=data['lessons'][str(n)]
        if n==5:
            l['slides'][2].update(timer='4:00',mode='read both sources')
            l['record']={'headers':['Chart heading','Weather/climate science','Human-health research'],
                         'rows':[[v,'',''] for v in ['Science question (proposed example)','Evidence used (proposed example)','Possible community benefit','Source support','Further information needed']],
                         'row_height':.8,'page_break_before':True}
            repair=' Career worksheet uses a dedicated page with separate question/evidence rows and space for both directions; all six required source chart headings retained. Four-minute reading timer made explicit.'
            if repair not in l.get('decisions',''):l['decisions']=l.get('decisions','')+repair
        if n==7:
            repair=' Assessment print layout starts the original rubric on a fresh page, repeats its headers and prevents a criterion row splitting across pages; all source text and scoring bands unchanged.'
            if repair not in l.get('decisions',''):l['decisions']=l.get('decisions','')+repair
        if l.get('design_revision')==REVISION:
            validate_quizzes(l,module,n,u['source_hashes']);continue
        l['design_revision']=REVISION
        if n==7:
            l['quizzes']=[]
            l['quiz_exception']='Independent transfer assessment: preserve all 40 source minutes for independent section work, separate still-open-question reflection and collection. No coached A–D poll or answer reveal before collection; plan later reinforcement from actual individual responses.'
            l['decisions']='No quiz added to the independent assessment; no teaching cards, peers, hints or exemplars before all work is collected. Phase tags are scheduling labels. Existing final rubric and source data retained.'
        else:
            # Keep every original Observe subdivision and the two-minute exit.
            for position,minutes in [(6,2),(7,3),(8,3),(10,2)]:
                l['slides'][position-1]['minutes']=minutes
            l['slides'][10]['do']='Save the individual written exit before the final reinforcement quiz. Retain first-attempt exit and quiz records separately.'
            l['quizzes']=questions[n]
            if n==6:
                l['quizzes'][2]['source_refs'].append({'file':'Codex_General_Science_Introduction_to_General_Science_data.json','locator':'LESSONS[5].framework[3].teacherMoves','evidence':'Require evidence for closure; retain training and untested material-property questions.'})
            if n==6:l['quizzes'][0]['timing_source']='One minute of the source Explain allocation after the limited-claim comparison; the second check follows the written revision explanation. Eight minutes of explanation plus two minutes of quiz response/feedback retain ten minutes.'
            for q in l['quizzes']:
                q['accuracy_check']='Reviewed every alternative against the complete GS1 unit, the exact cited source-key text, required task and source arithmetic; source evidence and arithmetic checks in qa/Quiz_Continuation_content_checks.json.'
            l['decisions']=l.get('decisions','')+' Periodic quiz-v1 checks: two one-minute response/feedback pairs use the existing ten-minute Explain/check time; one one-minute reinforcement follows the saved exit in Model Building. All required source tasks, original Observe subdivisions and phase totals remain. Teacher must confirm 30-second response plus 30-second feedback pacing.'
        for row in l['slides']:
            if row.get('timer'):
                seconds=round(row['minutes']*60);row['timer']=f'{seconds//60}:{seconds%60:02}'
        validate_quizzes(l,module,n,u['source_hashes'])
    data['status']='All seven source-specific lessons authored for quiz-v1; independent Lesson 7 has a documented no-coaching quiz exception. Draft generation authorised 17 November; external release gates open.'
    p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    print(module,'authored Lessons 3–7, preserving reviewed Lessons 1–2')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('module',choices=['gensci_1_1','essmath_1_1','coremath_1_1']);a=p.parse_args();author(a.module)
