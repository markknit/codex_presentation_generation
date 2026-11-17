#!/usr/bin/env python3
"""Author the remaining Essential/Core Real Numbers lessons from RN/CRN keys."""
import json
from curriculum_set_inventory import CONTROL
from author_initial_unit_specs import lesson,assessment,slide,task,cards,eq,tbl


def essential():
    return {
    '2':lesson('RN2','Exact_Values_and_Rounded_Displays',
        ['Distinguish exact values from approximations.','Locate a value using squared bounds.','Correct a display-based overclaim.'],
        'Card A says “π = 3.14 exactly”. Do you agree? Give a reason.',[
            slide('Observe',8,'RN2 · audit three exact-value claims','columns',columns=[
                ['CLAIMS A AND B','A: “π = 3.14 exactly.”\nB: “√2 is rational because my calculator displays 1.414213562.”'],
                ['CLAIM C','“√16 is irrational because it has a root sign.”']],
                caption='Correct every claim on your own RN2 record.',timer='8:00',mode='claim audit'),
            task('Observe',4,'Locate the numbers',['Place −3, −1/2, 0, √2 and 2 on a number line.','Use 1.4² and 1.5² to bracket √2.']),
            task('Observe',4,'Exact values that display alike',['Compare 1/3 with 0.333333333 as written.','Find two exact numbers that round to 1.41 at 2 decimal places.'])],[
            slide('Explain',3,'What changes when equality becomes approximation?','columns',columns=[
                ['EXACT EXPRESSIONS','π\n√2\n√16 = 4'],['APPROXIMATIONS','π ≈ 3.14\nA finite √2 display is approximate.']],
                caption='A short display does not determine an underlying exact number’s class.'),
            eq(3,'Use squares to bracket the value','1.96 < 2 < 2.25','1.4² = 1.96 and 1.5² = 2.25, so 1.4 < √2 < 1.5.'),
            slide('Explain',4,'Same rounded display, different exact values','numberline',bounds=[-3,2],
                points=[[-3,'−3'],[-.5,'−1/2'],[0,'0'],[1.414,'√2'],[2,'2']],
                caption='1.411 and 1.414 both round to 1.41. The number line locates √2; it does not prove irrationality.')],
        ['Add exact and approximate columns to the reference sheet.','Keep one corrected claim and one exact/approximate pair.'],
        ['Explain the difference between 1/3 and 0.333333333 as written.','Give a reason that uses exact meaning.'],
        record={'headers':['Claim','Correction','Reason'],'rows':[['A','',''],['B','',''],['C','','']]}),
    '3':lesson('RN3','Signed_Rational_Operations',
        ['Calculate signed rational operations exactly.','Correct a sign or denominator error.','Verify a result independently.'],
        'Estimate the sign and rough size of RN3(a) and RN3(c) before calculating.',[
            cards('Observe',10,'RN3 · four exact calculations',[
                '(a) −3/4 + 5/6','(b) 2/3 − 5/4','(c) (−2/3) × (9/4)','(d) (3/5) ÷ (−9/10)'],
                caption='Show intermediate working and a check for every result.',timer='10:00',mode='exact working'),
            task('Observe',6,'Audit errors and compare checks',['Correct (−2) × (−5) = −10 and 3/4 + 1/2 = 4/6.','Explain what division by zero would require.','Compare a reverse, equivalent-fraction or magnitude check.'])],[
            tbl('Explain',4,'Exact results with visible working',['Item','Working','Result'],[
                ['a','(−9 + 10)/12','1/12'],['b','(8 − 15)/12','−7/12'],
                ['c','−18/12','−3/2'],['d','(3/5) × (−10/9)','−2/3']],widths=[.9,7.5,3.4],size=25),
            eq(3,'A common denominator preserves the values','3/4 + 1/2 = 3/4 + 2/4 = 5/4','Also: (−2) × (−5) = 10. Correct the reason, not only the answer.'),
            slide('Explain',3,'Why is division by zero excluded?','columns',columns=[
                ['a ≠ 0','0 × x = a has no solution.'],['a = 0','0 × x = 0 has no unique solution.']],
                caption='Division would need a unique result; an error display is not a numerical answer.')],
        ['Keep a corrected example and an annotated counterexample.','Add an independent check to the same reference sheet.'],
        ['Correct 3/4 + 1/2.','Explain why a common denominator is needed.'],
        record={'headers':['Item','Intermediate working','Exact answer','Independent check'],'rows':[[x,'','',''] for x in ['a','b','c','d']]}),
    '4':lesson('RN4','Grouping_and_Operation_Order',
        ['Evaluate a grouped rational expression.','Explain equal-priority operation order.','Write an unambiguous calculator entry.'],
        'Do B = (−3)² − 2(5 − 8) and D = −3² start with the same square value?',[
            cards('Observe',8,'RN4 · work all four expressions',[
                'A: 3/4 − [1/2 ÷ (−2)]','B: (−3)² − 2(5 − 8)','C: 6 ÷ 3 × 2','D: −3²'],
                caption='Show the intermediate operations; mark the base of each power.',timer='8:00',mode='calculate alone'),
            task('Observe',4,'Protect the intended calculator grouping',['Write an unambiguous bracketed entry for A.','Compare the entry with exact arithmetic.']),
            task('Observe',4,'Create, exchange and check',['Create one rational expression with parentheses worth 1/2.','Exchange it and check the result.'])],[
            tbl('Explain',4,'Check A–D with the requested grouping',['Expression','Working','Value'],[
                ['A','3/4 − (−1/4)','1'],['B','9 − 2(−3)','15'],['C','(6 ÷ 3) × 2','4'],['D','−(3²)','−9']],
                widths=[1.6,7.0,3.2],size=25),
            eq(3,'Multiplication and division have equal priority','6 ÷ 3 × 2 = (6 ÷ 3) × 2 = 4','Process equal-priority operations left to right.'),
            eq(3,'Make the calculator entry unambiguous','(3 ÷ 4) − ((1 ÷ 2) ÷ (−2))','Parentheses identify what the negative denominator and division apply to.')],
        ['Add the C and B/D counterexamples to your reference sheet.','Keep a bracketed entry and a reverse or estimation check.'],
        ['Explain the first operation in A.','Show which part the brackets protect.'],
        record={'headers':['Expression','Intermediate working','Value','Check'],'rows':[[x,'','',''] for x in ['A','B','C','D']]}),
    '5':lesson('RN5','Reciprocals_and_Calculator_Evidence',
        ['Find exact reciprocals of nonzero numbers.','Verify each reciprocal by multiplication.','Record actual calculator use and precision.'],
        'What is the reciprocal of −0.2? Could zero have one? Propose a product check.',[
            cards('Observe',10,'RN5 · exact forms and actual entries',['4','−5','3/4','−0.2','√2'],
                caption='Record the actual model/key sequence, exact form and result to 3 decimal places.',timer='10:00',mode='record entries'),
            task('Observe',6,'Check each product and the display limit',['Multiply each original value by its exact reciprocal.','Compare exact and rounded products.','Explain why zero and the finite 1/√2 display need care.'])],[
            tbl('Explain',4,'Exact reciprocals and decimal forms',['Original','Exact reciprocal','Decimal form (3 d.p.)'],[
                ['4','1/4','0.250'],['−5','−1/5','−0.200'],['3/4','4/3','≈ 1.333'],['−0.2','−5','−5.000'],['√2','1/√2','≈ 0.707']],
                widths=[2.2,4.2,5.4],size=23,height=3.55),
            eq(3,'What does the product test require?','x × (1/x) = 1, for x ≠ 0','Rounded products may differ slightly from the exact product.'),
            eq(3,'Zero cannot pass the product-of-one test','0 × r = 0, never 1','A finite calculator display of 1/√2 is approximate, not the exact reciprocal.')],
        ['Add a definition, the zero exception and one actual calculator record.','Keep exact and approximate results distinct.'],
        ['Find the reciprocal of 3/4.','Justify it by a product.'],
        preparation='RN5 record per learner; teacher-approved scientific calculators for roots, shared fairly if needed. Each learner records an actual entry. If unavailable, retain paper work and schedule an accessible device station.',
        route='Use the source’s actual-device route where supplied. Printed calculations do not certify device use. Mark missing/unobserved device work honestly.',
        record={'headers':['Original','Exact reciprocal','3 d.p.','Actual entry / display','Product check'],'rows':[[x,'','','',''] for x in ['4','−5','3/4','−0.2','√2']]}),
    '6':lesson('RN6','Rational_Models_and_Units',
        ['Choose operations that match a stated change.','Calculate with signed values and units.','Interpret a result with an assumption.'],
        'The tank has 3/4 L; 1/6 L is used and 1/3 L added. More or less than it began with?',[
            task('Observe',10,'RN6 · model every fictional context',['Write expressions for volume, credit and temperature change.','Copy the two blood-pressure readings into separate columns.','Model the bottle count; state each assumption.']),
            task('Observe',6,'Explain and check one chosen model',['Explain what each sign or reciprocal represents.','Keep the unit in your result.','Compare one reverse or contextual check.'])],[
            tbl('Explain',4,'Operations must represent the situation',['Context','Expression','Interpretation'],[
                ['Tank','3/4 − 1/6 + 1/3','11/12 L'],['Credit','50 − 80 + 45','15 KES'],['Temperature','37.4 − 36.8','0.6 °C increase']],
                widths=[2.0,5.0,4.8],size=25,height=3.1,
                caption='Fictional records only. The arithmetic does not establish health status.'),
            eq(3,'What does the reciprocal count here?','3 L ÷ (3/4 L per bottle) = 4 bottles','4/3 bottles per litre × 3 litres = 4 bottles.'),
            tbl('Explain',3,'The slash separates two readings',['Systolic (mmHg)','Diastolic (mmHg)'],[['120','80']],
                size=28,height=2.3,caption='120/80 mmHg is not an instruction to divide. No personal measurements or clinical interpretation.')],
        ['Add expression → result with unit → conclusion → check.','Retain one assumption for each fictional context.'],
        ['Identify one model assumption.','Give one reverse check.'],
        route='Fictional paper records only, preserving the source’s two-reading convention and limits. No liquid handling, real financial action, health measurement or medical advice.',
        record={'headers':['Context','Expression','Result and unit','Assumption / check'],'rows':[[x,'','',''] for x in ['Tank','Credit','Temperature change','Bottle count']]}),
    '7':lesson('RN7','Full_Servings_and_Reverse_Checks',
        ['Model usable volume and full servings.','Diagnose a plausible operation error.','Defend a decision with units and a check.'],
        'Available 2.5 L; reserve 1/4 L; serving 3/8 L. Could the poster promise 7 full servings?',[
            cards('Observe',8,'RN7 · model the club’s paper plan',['Available: 2.5 L','Reserve: 1/4 L','Serving: 3/8 L'],
                caption='Calculate usable volume and the number of full servings. Assume no spills.',timer='8:00',mode='model alone'),
            task('Observe',4,'Diagnose the peer’s result',['The peer writes 2.25 ÷ 0.375 = 0.844.','Identify a likely operation error and a check.']),
            task('Observe',4,'Explain the action the evidence supports',['Defend the full-serving count.','Explain one benefit of exact reasoning.','Name one calculator-care or turn-taking action.'])],[
            eq(3,'First preserve the reserve','2.5 − 0.25 = 2.25 L = 9/4 L','Usable volume is distinct from the original total.'),
            eq(4,'Use the reciprocal to count full servings','(9/4) ÷ (3/8) = (9/4) × (8/3) = 6','Check: 6 × 3/8 L = 9/4 L. Seven require 21/8 L = 2.625 L.'),
            eq(3,'The displayed error resembles a product','2.25 × 0.375 = 0.84375 ≈ 0.844','A likely operation error, not evidence of which buttons a learner actually pressed.')],
        ['Correct the poster and explain why the decision is useful.','Cite exact amounts, units, the reserve and a reverse check.'],
        ['Explain a benefit of real-number reasoning.','Name one specific check of the serving promise.'],
        route='Paper club plan only; no real food or liquid distribution. Device-care observations remain distinct from the numerical rubric.',
        record={'headers':['Quantity / claim','Working','Result / decision','Check or assumption'],'rows':[[x,'','',''] for x in ['Usable volume','Full servings','Seven-serving promise','Peer operation error']]}),
    '8':assessment('RN8','Independent_Numerical_Decision',
        ['Classify new exact values independently.','Show operations and reciprocal reasoning.','Defend a numerical decision in context.'],[
            task('Observe',16,'Assessment · classification and operations',['Complete sections 1–2 using RN8.','Show exact working and the requested checks.','No comparison or hints before collection.']),
            task('Explain',12,'Assessment · reciprocals and contexts',['Complete sections 3–4 independently.','Record the actual calculator entry when used.','Keep exact forms, approximations and units distinct.']),
            task('Driving Question Board',4,'Assessment · usefulness and assumption',['Write the reasoned usefulness statement.','Identify one assumption without discussing answers.']),
            task('Model Building',4,'Check and submit all work',['Check results, units, names and completion.','Submit before any key is displayed.'])],
        preparation='RN8 data plus original final prompts; an accessible calculator per learner or supervised provision as source requires. Keep teaching cards and teacher key private.',
        route='Independent source assessment; no peer comparison, hints or worked exemplars before collection.')}


def core():
    return {
    '2':lesson('CRN2','Exact_Number_Classes',
        ['Classify exact real values with reasons.','Identify whole numbers and integers.','Distinguish exact constants from displays.'],
        'Do √16 and √2 belong to the same exact number class? Give a reason.',[
            cards('Observe',8,'CRN2 · classify every exact value',['−5','0','2/3','0.125','0.777…','√16','√2','π','22/7'],
                caption='7 repeats forever. Give fractions; identify integers and whole numbers.',timer='8:00',mode='work alone'),
            task('Observe',6,'Compare fractions and display claims',['Compare every exact classification and fraction.','Distinguish π from the rational approximation 22/7.','Explain what a finite √2 display cannot establish.'])],[
            tbl('Explain',4,'Fraction representations support rational membership',['Value','Exact fraction','Integer / whole?'],[
                ['−5','−5/1','Integer'],['0','0/1','Integer and whole'],['2/3','2/3','Neither'],
                ['0.125','1/8','Neither'],['0.777…','7/9','Neither'],['√16','4/1','Integer and whole'],['22/7','22/7','Neither']],
                widths=[2.1,3.1,6.6],size=22,height=3.6),
            slide('Explain',3,'Exact constants are not short displays','columns',columns=[
                ['ESTABLISHED IRRATIONAL EXAMPLES','√2 and π\nNo exact integer-ratio representation.'],
                ['RATIONAL APPROXIMATION','22/7 is rational.\nIt is not equal to exact π.']],caption='A finite display approximates an irrational value; it is not a proof of rationality.'),
            eq(3,'Every whole number has a fraction form','n = n/1','There are no irrational whole numbers. Real numbers also include irrational values.')],
        ['Revise your exact-number classification model.','Keep the fraction evidence and the display limit visible.'],
        ['Explain why 0.125 is rational.','Explain why a finite √2 display does not settle its exact class.'],core=True,
        record={'headers':['Value','Rational / irrational','Fraction / reason','Integer? Whole?'],'rows':[[x,'','',''] for x in ['−5','0','2/3','0.125','0.777… (7 repeats)','√16','√2','π','22/7']]}),
    '3':lesson('CRN3','One_Divided_by_a_Number',
        ['Construct reciprocals through division.','Verify a multiplicative inverse.','Distinguish a reciprocal from an opposite.'],
        'What is the reciprocal of 4, and what should a product check show?',[
            cards('Observe',10,'CRN3 · divide one by each value',['4','−5','2/3','√2'],caption='Keep exact forms and multiply each result by its original value.',timer='10:00',mode='exact divisions'),
            task('Observe',4,'Test zero and the opposite-number claim',['Could 0 × r equal 1 for any real r?','Does reciprocal mean additive opposite?','Compare reasons using a specific counterexample.'])],[
            tbl('Explain',4,'Each exact reciprocal passes a product test',['Original','1 ÷ original','Product'],[
                ['4','1/4','4 × 1/4 = 1'],['−5','−1/5','(−5) × (−1/5) = 1'],
                ['2/3','3/2','(2/3) × (3/2) = 1'],['√2','1/√2','√2 × (1/√2) = 1']],widths=[2.0,3.3,6.5],size=24),
            eq(3,'Zero cannot have a real reciprocal','0 × r = 0, never 1','Reciprocal means multiplicative inverse, with a nonzero original.'),
            slide('Explain',3,'Two different kinds of undoing','columns',columns=[['RECIPROCAL OF 4','1/4\n4 × 1/4 = 1'],['ADDITIVE OPPOSITE OF 4','−4\n4 + (−4) = 0']],caption='The inverse operation must match the operation being undone.')],
        ['Retain the original claim and add product evidence.','Keep reciprocal and additive opposite separate.'],
        ['Give the reciprocal and additive opposite of −5.','Verify each by its different operation.'],core=True,
        record={'headers':['Original','1 ÷ original','Exact reciprocal','Product check'],'rows':[[x,'','',''] for x in ['4','−5','2/3','√2']]}),
    '4':lesson('CRN4','Convert_Before_Inverting',
        ['Represent the whole signed value as a fraction.','Find and verify exact reciprocals.','Audit a digit-swapping claim.'],
        'Will the reciprocal of −2½ have magnitude greater or less than 1?',[
            cards('Observe',10,'CRN4 · convert, invert, verify',['1½','−2½','0.25','−0.4','1/9'],caption='Show the fraction conversion and a product check for all five inputs.',timer='10:00',mode='exact working'),
            task('Observe',4,'Audit the proposed reciprocal',['The learner proposes −2/3 as the reciprocal of −2½.','Multiply to test it; explain what was misrepresented.'])],[
            tbl('Explain',4,'The sign belongs to the whole mixed number',['Input','Equivalent fraction','Reciprocal'],[
                ['1½','3/2','2/3'],['−2½','−5/2','−2/5'],['0.25','1/4','4'],['−0.4','−2/5','−5/2'],['1/9','1/9','9']],
                widths=[2.2,4.6,5.0],size=25,height=3.5),
            eq(3,'Check the proposed and actual products','(−5/2) × (−2/5) = 1','The proposed −2/3 does not multiply the original −5/2 to 1.'),
            task('Explain',3,'Which value is being inverted?',['Explain the full signed fraction first.','Use the product to check sign and magnitude.','Keep zero outside the reciprocal domain.'])],
        ['Revise the representation before its reciprocal.','Keep a complete conversion and multiplicative check.'],
        ['Find the reciprocal of 0.25.','Show its exact fraction conversion and product check.'],core=True,
        record={'headers':['Input','Fraction conversion','Reciprocal','Product check'],'rows':[[x,'','',''] for x in ['1½','−2½','0.25','−0.4','1/9']]}),
    '5':lesson('CRN5','Reciprocal_Table_and_Scaling',
        ['Read the supplied mathematical table.','Track the reciprocal of a scaled input.','Label exact and rounded values honestly.'],
        'Is 1/32 larger or smaller than 1/3.2? Give a reason before using the table.',[
            tbl('Observe',10,'CRN5 · use the complete supplied table',['x','1/x (4 s.f.)','x','1/x (4 s.f.)'],[
                ['3.0','0.3333','3.5','0.2857'],['3.1','0.3226','3.6','0.2778'],['3.2','0.3125','3.7','0.2703'],
                ['3.3','0.3030','3.8','0.2632'],['3.4','0.2941','3.9','0.2564']],size=25,height=3.55,
                caption='Source-supplied instructional table, not an official KICD table. Read and derive all five requested values.'),
            task('Observe',4,'Compare scale and precision reasons',['Compare 1/3.2 and 1/3.6.','Derive 1/32, 1/0.32 and 1/0.036.','Which entries are exact? Where is ≈ needed?'])],[
            slide('Explain',3,'Same table, different precision','columns',columns=[['EXACT','1/3.2 = 0.3125'],['ROUNDED','1/3.6 = 5/18 ≈ 0.2778']],caption='A rounded table does not make every entry approximate or every entry exact.'),
            tbl('Explain',4,'Scale the reciprocal in the opposite direction',['Input relationship','Reciprocal result'],[
                ['32 = 10 × 3.2','1/32 = 0.03125'],['0.32 = 0.1 × 3.2','1/0.32 = 3.125'],['0.036 = 0.01 × 3.6','1/0.036 ≈ 27.78']],size=25,height=3.1),
            task('Explain',3,'Explain the scale instead of guessing digits',['Write the relationship between the inputs.','Explain the inverse scale factor.','Use an exact or approximate sign to match the evidence.'])],
        ['Add a table-reading and scale check to your model.','Retain which rows are exact and which are rounded.'],
        ['Show why 1/0.32 = 3.125.','Explain why the 0.036 answer needs ≈.'],core=True,
        record={'headers':['Requested value','Table row / scaling','Result','Exact or approximate?'],'rows':[[x,'','',''] for x in ['1/3.2','1/3.6','1/32','1/0.32','1/0.036']]}),
    '6':lesson('CRN6','Actual_Calculator_Evidence',
        ['Enter reciprocals on an approved device.','Record the actual entry, display and precision.','Compare device evidence with a table.'],
        'Predict the sign of 1 ÷ (−2.5) and the approximate size of 1 ÷ √2.',[
            cards('Observe',14,'CRN6 · record actual device actions',['1 ÷ 3.6','1 ÷ (−2.5)','1 ÷ (2 ÷ 3)','1 ÷ √(2)'],
                caption='Complete all entries, the CRN5 comparison and the normal 1 ÷ 0 check. Record actual use or NOT OBSERVED.',timer='14:00',mode='individual device record')],[
            tbl('Explain',4,'Exact meaning and permitted precision',['Entry','Exact result','Rounded result (4 s.f. where needed)'],[
                ['1 ÷ 3.6','5/18','≈ 0.2778'],['1 ÷ (−2.5)','−2/5','−0.4 exactly'],['1 ÷ (2 ÷ 3)','3/2','1.5 exactly'],['1 ÷ √2','1/√2','≈ 0.7071']],
                widths=[3.2,2.4,6.2],size=23),
            eq(3,'An error message is not a real number','0 × r cannot equal 1','Normal approved devices may report division by zero differently. Record what actually happened.'),
            task('Explain',3,'Keep two kinds of evidence separate',['Compare the CRN5 table entry with your actual display.','Use parentheses for a compound denominator.','Do not invent device action from a paper answer.'])],
        ['Retain actual entry, display, precision and observation status.','Explain the comparison with the supplied table.'],
        ['Submit your individual actual-action record.','If no device was provided, retain NOT OBSERVED and the exact paper work.'],core=True,
        preparation='CRN6 records and teacher-approved calculators/supervised equivalents; CRN5 table. Each learner’s own action is observed separately where provided.',
        route='Actual-device evidence is required for the calculator component. If no device is provided, preserve paper mathematics and mark device use NOT OBSERVED; it remains unconfirmed.',
        record={'headers':['Entry','Actual key sequence','Full copied display','Precision / table comparison','Observed / not observed'],'rows':[[x,'','','',''] for x in ['1÷3.6','1÷(−2.5)','1÷(2÷3)','1÷√2','1÷0']]}),
    '7':lesson('CRN7','Reciprocal_Models_for_Portion_Counts',
        ['Translate a division context exactly.','Multiply by a reciprocal and verify.','Interpret counts with units and assumptions.'],
        'Can 4½ L make fewer or more than four exact 3/4 L portions?',[
            cards('Observe',10,'CRN7 · solve all three tasks',['4½ L in 3/4 L portions','2.4 m in 0.3 m pieces','(−3/5) ÷ (2/7)'],
                caption='Show division, reciprocal multiplication, units, the nonzero condition and a product check.',timer='10:00',mode='model alone'),
            task('Observe',4,'Compare what each quotient counts',['Compare exact models and reverse checks.','Explain the no-spill or no-cutting-loss assumption.'])],[
            eq(4,'Count exact full portions','(9/2) × (4/3) = 6 portions','Check: 6 × 3/4 L = 9/2 L, with no spills.'),
            eq(3,'Count pieces without cutting loss','(12/5) × (10/3) = 8 pieces','Check: 8 × 0.3 m = 2.4 m.'),
            eq(3,'The signed quotient still needs a nonzero divisor','(−3/5) × (7/2) = −21/10','Check: (−21/10) × (2/7) = −3/5.')],
        ['Choose one context for the model you keep.','State exact count, unit, product check and loss assumption.'],
        ['Explain what the quotient counts.','Name the assumption that limits the conclusion.'],core=True,
        route='Paper planning only: no actual liquid handling or cutting. Exact whole counts in these tasks do not justify rounding a fractional count upwards.',
        record={'headers':['Task','Division / reciprocal model','Result with unit','Reverse check / assumption'],'rows':[[x,'','',''] for x in ['Portions','Pieces','Signed quotient']]}),
    '8':lesson('CRN8','Evidence_Based_Number_Advice',
        ['Link classification to a specific decision.','Explain a checked reciprocal model.','Revise advice using a real peer question.'],
        'Which error should a useful numerical advice card prevent?',[
            task('Observe',8,'CRN8 · write your own advice card',['Explain how classification prevents a specific mistake.','Use a checked CRN7 calculation with units and assumptions.','Include why zero has no reciprocal.']),
            task('Observe',6,'Explain, exchange and record what happened',['Share only when directed.','Record the actual peer question and your revision.','If not shared, mark presentation NOT OBSERVED.'])],[
            slide('Explain',3,'An advice message needs a checkable link','flow',nodes=['Specific error','Correct evidence','Useful decision','Limit'],caption='Use your own correct classification and computation from CRN1–7.'),
            eq(3,'An example of numerical evidence, not a slogan','4½ L ÷ (3/4 L per portion) = 6 portions','State no spills and exact quantities; zero cannot be a divisor.'),
            task('Explain',4,'Audit your message against earlier work',['Check the definition and calculation.','Keep units, assumptions and the zero limit.','Explain how the evidence changes a decision.'])],
        ['Revise your own advice card from the actual question received.','Retain the original claim and actual sharing status.'],
        ['Submit the advice, computation, assumption and revision.','Do not claim a presentation that was not observed.'],core=True,
        route='Individual advice first, then the source-directed peer stage. Written work alone does not certify an unobserved oral presentation.',
        record={'headers':['Evidence / calculation','Decision / benefit','Assumption / zero limit','Actual peer question / revision'],'rows':[['','','','']]}),
    '9':lesson('CRN9','Counterexample_Audit',
        ['Repair five different numerical shortcuts.','Use a counterexample or calculation for each.','Identify a remaining evidence-based question.'],
        'Which CRN9 claim looks plausible at first? Record a verdict and a reason.',[
            task('Observe',10,'CRN9 · repair every claim',['Audit A–E on the full supplied card.','Give a distinct counterexample or calculation for each.','Ask one evidence-based question.']),
            task('Observe',4,'Compare distinct reasons',['Check all five repairs.','Explain why each correction fits its own definition or operation.'])],[
            tbl('Explain',4,'A counterexample or exact representation',['Claim','Evidence that repairs it'],[
                ['A: odd means prime','9 has positive divisors 1, 3, 9.'],['B: all reals are rational','√2 and π are established irrational examples.'],
                ['C: reciprocal of −2½ is −2/3','−2½ = −5/2, so its reciprocal is −2/5.']],widths=[5.0,6.8],size=23,height=3.2),
            eq(3,'A tenfold input divides its reciprocal by ten','1/3.2 = 0.3125; 1/32 = 0.03125','Repair D with the scale relationship, not a guessed decimal shift.'),
            eq(3,'An error does not make the reciprocal zero','0 × r = 0, never 1','Repair E with the product-of-one definition; keep CRN10 private.')],
        ['Repair your most significant earlier error independently.','Attach a check and keep any remaining confusion visible.'],
        ['Submit the corrected claim and its check.','Name the definition that rules out the shortcut.'],core=True,
        record={'headers':['Claim','Initial verdict','Repair and evidence'],'rows':[[x,'',''] for x in ['A','B','C','D','E']]}),
    '10':assessment('CRN10','Independent_Number_Audit',
        ['Classify unfamiliar values independently.','Verify reciprocals and precision.','Communicate a checked planning decision.'],[
            task('Observe',8,'Assessment · section 1',['Classify the listed whole and exact real values.','Give the required divisor, fraction and display reasoning.']),
            task('Explain',8,'Assessment · section 2',['Find exact reciprocals with conversions and product checks.','Explain the zero and additive-opposite distinctions.']),
            task('Driving Question Board',10,'Assessment · section 3',['Use the supplied table and explain its scaling.','Record actual calculator action when a device is supplied.','If none is supplied, mark NOT OBSERVED; keep the exact expression.']),
            task('Model Building',10,'Assessment · section 4 and checking',['Use 7 minutes for the planning model and independent advice.','Use 3 minutes to check your own work.','Submit before any peer discussion or key.'])],
        preparation='CRN10 only, original assessment prompts and approved calculators where actually provided. Retain independent records of device provision/use; keep all teaching cards and exemplars private.',
        route='Independent source assessment. Unprovided or unobserved calculator performance remains pending; a paper key sequence does not complete it.')}


if __name__=='__main__':
    raise SystemExit('Superseded pre-quiz writer. Use quiz-v1 source-specific specifications and build_curriculum_set_lesson.py; see QUIZ_DESIGN.md.')
    folder=CONTROL/'specs';folder.mkdir(parents=True,exist_ok=True)
    for module,fn in [('essmath_1_1',essential),('coremath_1_1',core)]:
        lessons=fn()
        if module=='essmath_1_1':
            lessons['3']['slides'][0].update({'kind':'cards','values':['(a) −3/4 + 5/6','(c) (−2/3) × (9/4)'],
                'caption':'Estimate each sign and rough size before calculation.'})
        else:
            lessons['9']['slides'][0]['do']='Distribute only the CRN9 claims card for the initial individual choice. Withhold all corrections and CRN10 final inputs.'
        anchor='Our club reference sheet: exact meaning behind calculator displays.' if module=='essmath_1_1' else 'Our supply labels: which number claims survive a check?'
        (folder/(module+'.json')).write_text(json.dumps({'module':module,'whole_unit_read':True,'anchor_line':anchor,'lessons':lessons},indent=2,ensure_ascii=False))
    print('Authored Essential L2–8 and Core L2–10 Real Numbers specs.')
