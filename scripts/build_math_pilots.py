#!/usr/bin/env python3
"""Two user-approved Mathematics Lesson 1 pilots; CPU-only editable assembly.

The November Mathematics sources and approved pilot guidance control pedagogy.
Only the presentation frame and document utilities are shared with science.
"""
import argparse
import hashlib
import json
from docx import Document
from docx.shared import Inches, Pt

from build_curriculum_pilots import Pilot, ROOT, OUT, CONFIG, chips
from lesson_visuals import tx, box, oval, timer, question, steps, table, INK, MUTED, CREAM, A

GUIDANCE = ROOT/'content/curriculum_pilots_2026-11/MATHEMATICS_PILOT_GUIDANCE.md'
ESS_KEY = ('Rational: −3=−3/1; 0=0/1; 2/5; 0.125=1/8; '
           '0.333… (3 repeats forever)=1/3; √9=3=3/1. '
           'Integers: −3, 0 and √9. Irrational: √2 and π. '
           'The irrationality of √2 and π is established mathematical knowledge; '
           'it is not proved by a finite calculator display.')
CORE_KEY = ('Even: 0, 2, 4. Odd: 1, 3, 9, 11, 15, 21. '
            'Prime: 2, 3, 11. Composite: 4, 9, 15, 21. Neither: 0, 1. '
            'Positive factor pairs: 9 → (1,9), (3,3); 15 → (1,15), (3,5). '
            '9 is an odd composite counterexample. 0=2×0 is even. '
            'Every whole number n=n/1 is rational; there are no irrational whole numbers.')


class MathPilot(Pilot):
    def __init__(self, key):
        assert key in ('essential', 'core')
        assert 'Status: approved by the user' in GUIDANCE.read_text(), 'Mathematics approval required'
        super().__init__(key)

    def opening(self, *args):
        super().opening(*args)
        for s in self.b.deck.slides:
            tf=s.notes_slide.notes_text_frame
            tf.text=tf.text.replace('SCIENCE NOTE FOR YOU','MATHEMATICS NOTE FOR YOU').replace(
                'The background label is inherited; Mathematics notes contain mathematical guidance.',
                'MATHEMATICS NOTE FOR YOU contains source-specific mathematical guidance.')

    def save(self):
        for s in self.b.deck.slides:
            tf=s.notes_slide.notes_text_frame
            tf.text=tf.text.replace('SCIENCE NOTE FOR YOU','MATHEMATICS NOTE FOR YOU')
        super().save()
        src=ROOT/'qa'/f'{self.name}_sources.json'
        manifest=json.loads(src.read_text())
        manifest['approved_guidance']={
            'path':str(GUIDANCE.relative_to(ROOT)),
            'sha256':hashlib.sha256(GUIDANCE.read_bytes()).hexdigest(),
            'approval':'User approved the proposal and instructed proceeding, 2026-11-16',
            'scope':'Lesson 1 only; no wider Mathematics generation or release'}
        src.write_text(json.dumps(manifest,indent=2,ensure_ascii=False))

    def support(self):
        super().support()
        # Retain the exact source task; provide enough physical room for reasons.
        d=Document();sec=d.sections[0]
        sec.top_margin=sec.bottom_margin=Inches(.6)
        sec.left_margin=sec.right_margin=Inches(.65)
        d.styles['Normal'].font.name='Calibri';d.styles['Normal'].font.size=Pt(11)
        d.add_heading(self.subject+' · Grade 10 · Lesson 1',0)
        d.add_paragraph('Name: ____________________    Class: __________    Date: __________')
        d.add_heading(self.card[0],1)
        for p in self.card[1:]:
            if p.strip():d.add_paragraph(p)
        if self.key=='essential':
            d.add_paragraph('Diagnostic working: −4+7 = __________    3/4+1/2 = __________')
            heads=['Exact number','Rational / irrational','Integer?','Fraction / reason']
            vals=['−3','0','2/5','0.125','0.333…\n(3 repeats forever)','√9','√2','π']
        else:
            heads=['Whole number','Odd / even','Prime / composite / neither','Reason']
            vals=['0','1','2','3','4','9','11','15','21']
        t=d.add_table(rows=1,cols=4);t.style='Table Grid'
        for c,h in zip(t.rows[0].cells,heads):c.text=h
        for val in vals:
            row=t.add_row();row.height=Inches(.43);row.cells[0].text=val
        if self.key=='core':
            d.add_paragraph('Positive factor pairs for 9: __________________________________________')
            d.add_paragraph('Positive factor pairs for 15: _________________________________________')
            d.add_paragraph('Every odd whole number is prime: verdict and reason ___________________')
            d.add_paragraph('Zero is even: verdict and reason _____________________________________')
        d.add_paragraph('Keep your own first answers. Compare only when directed.')
        d.add_page_break()
        d.add_heading('Model Building · keep this section for later',0)
        d.add_paragraph('Use your notebook if you need more room. Keep your first idea and revise in a new colour.')
        if self.key=='essential':
            d.add_heading('The club’s number reference sheet',1)
            d.add_paragraph('Draw nested real / rational / integer sets. Place all eight RN1 numbers and add fraction evidence or a reason.')
        else:
            d.add_heading('The corrected classroom supply label',1)
            d.add_paragraph('Revise “Every odd count is prime.” Use a counterexample and factor evidence. Explain where 0 and 1 belong.')
        for _ in range(6):d.add_paragraph('________________________________________________________________________________')
        d.add_heading('Individual exit',1)
        d.add_paragraph('Classify −3, √9 and π with reasons; identify the integers and give fractions where possible.'
                        if self.key=='essential' else 'Classify 21 and 0 by parity and divisors. Give evidence for each decision.')
        for _ in range(2):d.add_paragraph('________________________________________________________________________________')
        d.add_heading('Summary Table',1)
        t=d.add_table(rows=2,cols=3);t.style='Table Grid'
        for c,h in zip(t.rows[0].cells,['What did I observe?','What did I learn?','How does this explain the unit phenomenon?']):c.text=h
        t.rows[1].height=Inches(.7)
        d.add_paragraph('© 2026 SeaVuria & ARES Education · CC BY-NC 4.0 · Review draft')
        d.save(OUT/(self.name+'_Student_Task.docx'))


def number_grid(s, values, y=2.5):
    """Editable number cards with no classification or result shown."""
    cols=4 if len(values)==8 else 5
    width=(11.9-(cols-1)*.18)/cols
    for i,v in enumerate(values):
        x=.72+(i%cols)*(width+.18); yy=y+(i//cols)*1.16
        box(s,x,yy,width,.96,CREAM)
        tx(s,v,x+.08,yy+.16,width-.16,.65,29,INK,True,A.CENTER)


def essential():
    l=MathPilot('essential')
    l.opening(['Classify exact numbers with reasons.',
               'Write fractions for rational values.',
               'Build a model of number classes.'],
              'classify: put into groups\n\nexact: the value as written\n\njustify: give a mathematical reason',
              'The club starts a number reference sheet.\nCan a symbol’s appearance decide its class?')
    # Title notes retain the actual unit anchor, without leaking L2 examples.
    l.b.deck.slides[0].notes_slide.notes_text_frame.text += (
        '\nThe unit anchor is two calculators showing similar decimals when exact '
        'numbers and intended operations differ. This lesson builds classification '
        'evidence; preserve detailed rounded-display claims and bounds for Lesson 2.\n')
    s=l.slide('Start with your own number sort','Predict',2,
        'Learners sort 0, √9 and √2 alone, before rules are taught. Ask for each '
        'initial class and one reason. Keep the first record unchanged for later revision.',
        say='Which belong together? Write your first classification and a reason.',
        wait='Two minutes of silent thinking and writing.',
        key='Accept initial ideas as predictions, including uncertainty. Later key: '
            '0 and √9 are rational integers; √2 is irrational. Do not confirm yet.',
        look='Scan five notebooks for all three values and reasons, not only group names.',
        iff='If a learner is unsure, say: “Write what you think now and what you would need to check.”',check=True)
    chips(s,['0','√9','√2'])
    tx(s,'Write your first idea. Keep it for comparison later.',.75,4.32,10.8,.8,26)
    timer(s,'2:00','write alone')
    l.task('BEFORE · our first classifications','Predict',1,
        ['Share one classification and its reason.','Keep a different idea visible too.'],
        'Hear one learner who groups the roots together and one who separates them, '
        'if those predictions occur. Record exact reasons without correction.',
        key='Predictions vary. Retain them; formal classifications follow the RN1 task.',
        look='Hear contrasting reasons and check individual predictions were written first.',
        iff='If learners seek approval, say: “Keep that reason. We will test it against the number task.”')
    s=l.slide('RN1 · a short diagnostic','Observe',3,
        'Learners complete both source diagnostic items alone. Scan five books; '
        'identify signed-addition and fraction-addition needs separately. Support '
        'the prerequisite privately or plan follow-up without cutting RN1 classification.',
        say='Show your working for each. This helps me see which support you need.',
        key='−4+7=3. 3/4+1/2=3/4+2/4=5/4. '
            'Do not add denominators. Integer and fraction support needs are distinct.',
        look='Read both lines of working in five books; record which operation needs support.',
        iff='If denominators are added, say privately: “Can you write both fractions in quarters?” '
            'If a sign is lost, ask where −4 starts on a number line.',check=True)
    chips(s,['−4 + 7','3/4 + 1/2'])
    tx(s,'Two calculations · show the steps · work alone',.75,4.45,10.8,.7,26)
    timer(s,'3:00','diagnostic')
    s=l.slide('RN1 · classify every exact value','Observe',9,
        'Distribute RN1 and its blank four-column record. Each learner classifies all '
        'eight numbers alone, identifies integers, and gives an integer fraction for '
        'each rational value. Read the recurring-3 convention. RN1 supplies the '
        'integer reminder. Do not display a completed classification or nested diagram.',
        say='Record your own answer for every value. Leave a question mark where you need evidence.',
        wait='Nine minutes of individual work; check quietly without announcing answers.',
        key=ESS_KEY,
        look='Inspect five records for all eight rows and exact fractions, with integer decisions kept separate.',
        iff='If a learner judges every root by its symbol, say: “What exact value does this expression name?” '
            'If the recurring decimal is read as finite, reread “3 repeats forever”.',check=True)
    number_grid(s,['−3','0','2/5','0.125','0.333…','√9','√2','π'])
    tx(s,'0.333… means 3 repeats forever.',.75,4.94,10.8,.4,18,MUTED)
    tx(s,'Class? Integer too? Fraction or reason?',.75,5.52,9.6,.6,25,INK,True)
    timer(s,'9:00','work alone')
    l.task('Compare the fraction evidence','Observe',4,
        ['Compare all eight rows with a partner.','Check each proposed fraction has integer terms.','Keep an individual record of any disagreement.'],
        'Pairs compare RN1, including whether each value is an integer and what '
        'their fractions show. Each learner records changes in a second colour '
        'while keeping the first classification. Do not show the teacher key.',
        key=ESS_KEY,
        look='Hear three pairs justify a fraction and name one question; check both partners keep their own rows.',
        iff='If one learner simply copies, say: “Explain why that fraction names the same exact value.”',clock='4:00')
    s=l.slide('What makes a number rational?','Explain',2,
        'Now state the exact fraction definition. Invite a learner to use an RN1 '
        'fraction as evidence. Contrast integer membership with the wider rational set.',
        say='The numerator and denominator must be integers. The denominator cannot be zero.',
        key='A rational number equals a/b for integers a,b with b≠0. Integers '
            'include negative whole numbers, zero and positive whole numbers. '
            'Every integer n=n/1. A rational number need not be an integer: 2/5.',
        look='Ask one learner for the condition on a,b and another for a rational non-integer.',
        iff='If “a fraction” is given without restrictions, ask: “What must the two terms be? Can the denominator be zero?”',check=True)
    box(s,.75,2.4,7.65,2.6,CREAM)
    tx(s,'a/b',1.05,2.65,6.9,.9,52,INK,True,A.CENTER)
    tx(s,'a and b are integers · b ≠ 0',1.05,3.95,6.9,.6,27,INK,True,A.CENTER)
    tx(s,'An integer is also rational.\nA rational number need not be an integer.',8.8,2.8,3.7,2.0,26)
    s=l.slide('Why does zero belong?','Explain',2,
        'Return to the initial 0 prediction. Elicit 0/1 before showing the displayed '
        'equivalence. Learners revise their own reason in a second colour.',
        key='0=0/1. Its denominator is nonzero and both terms are integers; '
            '0 is therefore rational and is also an integer.',
        look='Hear one initially uncertain learner explain why denominator 1 is allowed.',
        iff='If zero is excluded, say: “Which part of the rational definition does 0/1 fail?”',check=True)
    chips(s,['0 = 0/1','integer + rational'])
    tx(s,'Return to your first idea. Add the fraction evidence.',.75,4.6,11.4,.9,27)
    s=l.slide('Does every root have the same class?','Explain',2,
        'Elicit √9=3, then compare the source’s established irrational example √2. '
        'Do not claim that a short decimal display proves irrationality. '
        'Ask learners to revise the original root grouping.',
        key='√9=3=3/1 is a rational integer. √2 is irrational: it has no exact '
            'integer-ratio representation. Its irrationality is stated as established '
            'mathematical knowledge here, not proved in this lesson.',
        look='Hear a learner use √9 as a counterexample to “every root is irrational”.',
        iff='If all roots are grouped as irrational, ask: “What is the exact value of √9?”',check=True)
    for i,(a,b) in enumerate([('√9 = 3 = 3/1','RATIONAL · INTEGER'),('√2','IRRATIONAL')]):
        x=.75+i*6.05;box(s,x,2.45,5.8,2.7,CREAM)
        tx(s,a,x+.2,2.9,5.4,.9,35,INK,True,A.CENTER)
        tx(s,b,x+.2,4.25,5.4,.5,20,INK,True,A.CENTER)
    tx(s,'The exact value matters.',.75,5.6,11.7,.55,28,INK,True)
    s=l.slide('Check all eight RN1 classifications','Explain',3,
        'After individual work and comparison, review the full source key. Learners '
        'correct rows in a second colour and explain one change. Emphasise that '
        'the ellipsis means repeated 3 forever, not a finite decimal.',
        key=ESS_KEY,
        look='Check five revised records and ask why 0.125 and recurring 0.333… are rational.',
        iff='If a learner copies only labels, ask for the exact fraction that supports one row.',check=True)
    table(s,['Exact value','Class','Integer?','Exact fraction / reason'],[
        ['−3','Rational','Yes','−3/1'],['0','Rational','Yes','0/1'],
        ['2/5','Rational','No','2/5'],['0.125','Rational','No','1/8'],
        ['0.333…','Rational','No','1/3 (3 repeats forever)'],['√9','Rational','Yes','3/1'],
        ['√2','Irrational','No','No integer-ratio form'],['π','Irrational','No','No integer-ratio form']],
        .75,2.18,11.8,4.3,[2.0,2.0,1.4,6.4],18)
    s=l.slide('What can a short display tell us?','Explain',1,
        'Ask the RN1 finite-display question after the classification evidence. '
        'Keep this to the source’s caution; preserve RN2 numerical display claims '
        'and the √2 bounds investigation for Lesson 2.',
        key='A finite calculator display alone cannot settle the exact classification '
            'of an underlying number. Use the exact expression and mathematical '
            'definition; a rounded display is not the full exact expansion.',
        look='Hear one learner distinguish the exact expression from a rounded output.',
        iff='If a display is treated as proof, say: “Are you classifying the exact number or only the digits shown?”',check=True)
    question(s,'Does the display show the whole exact value?','Explain')
    tx(s,'Keep the exact expression.\nLeave detailed display claims on our question board.',.9,4.45,11.2,1.0,27)
    l.board('Retain exact-versus-display questions for Lesson 2.')
    s=l.slide('Build the club’s number reference sheet','Model Building',3,
        'Each learner draws one nested real/rational/integer diagram. The editable '
        'outline is a set model, not a number line or a size comparison. Learners '
        'place all RN1 values, writing √2 and π within real numbers but outside '
        'rational numbers. Cite fraction evidence and retain the initial sort.',
        key='Inside integers: −3,0,√9. Rational but outside integers: 2/5,0.125,0.333… '
            '(3 repeats forever). Real but outside rational: √2,π. Sets are nested; '
            'the drawn area does not represent how many values each set contains.',
        look='Inspect five diagrams for 0 inside both integers and rational, and √2/π outside rational.',
        iff='If integer and rational circles are disjoint, say: “Where would n/1 put an integer?”',check=True)
    box(s,.75,2.35,8.2,3.9,'E9F8FC',INK);tx(s,'REAL NUMBERS',1.0,2.55,7.7,.4,20,INK,True)
    box(s,1.1,3.12,5.25,2.8,'F7F9DA',INK);tx(s,'RATIONAL',1.35,3.35,4.75,.4,19,INK,True)
    box(s,1.5,4.1,3.25,1.45,CREAM,INK);tx(s,'INTEGERS',1.7,4.38,2.85,.5,21,INK,True)
    tx(s,'Place all eight values.\nAdd a fraction or reason.\nKeep your first sort.',9.4,2.8,3.2,2.5,24)
    timer(s,'3:00','draw alone')
    l.task('Exit · classify with a reason','Model Building',2,
        ['Classify −3, √9 and π.','Identify the integers. Give fractions where possible.'],
        'Collect an individual response with the reference-sheet diagram. Use '
        'these to plan Lesson 2 support, not a class vote as evidence of mastery.',
        key='−3=−3/1 and √9=3/1 are rational integers. π is irrational '
            'and not an integer; it has no exact integer-fraction form.',
        look='Check each response gives a fraction for −3 and √9 and an accurate reason for π.',
        iff='If the radical symbol alone decides the class, ask: “Which exact value does √9 represent?”',clock='2:00')
    l.summary();l.save()


def core():
    l=MathPilot('core')
    l.opening(['Classify whole numbers in two ways.',
               'Use positive factors to justify a class.',
               'Correct a claim with a counterexample.'],
              'claim: a statement to check\n\nfactor: divides a number exactly\n\ncounterexample: an example that disproves a claim',
              'A supply label says: “Every odd count is prime.”\nWhich evidence could test that claim?')
    l.b.deck.slides[0].notes_slide.notes_text_frame.text += (
        '\nThe source anchor also includes trying to undo division with an additive '
        'opposite. Retain that later reciprocal problem for Lesson 3. This lesson '
        'investigates the label’s whole-number classification claim.\n')
    s=l.slide('Could these counts be prime?','Predict',2,
        'Learners predict whether 0, 1 and 9 can be prime and give a reason alone. '
        'Do not announce the parity or prime rules before this initial record. '
        'Present the fictional supply-label claim exactly as a claim to test.',
        say='Write your first verdict for each count. Give a reason before hearing others.',
        wait='Two minutes of silent thinking and writing.',
        key='Initial predictions may vary. Later key: 0 and 1 are neither prime '
            'nor composite; 9 is composite. Retain all initial reasons without correction.',
        look='Scan five notebooks for three individual verdicts and at least one reason.',
        iff='If learners copy a neighbour, say: “Record your own reason now; comparison comes later.”',check=True)
    chips(s,['0','1','9'])
    tx(s,'Supply-label claim: “Every odd count is prime.”',.75,4.35,11.5,.8,27,INK,True)
    timer(s,'2:00','predict alone')
    l.task('BEFORE · keep our claims visible','Predict',1,
        ['Share a verdict and its reason.','Keep a different prediction on the board.'],
        'Select one learner who treats odd and prime as the same category and one '
        'who questions that, if those ideas occur. Preserve the initial claim without correction.',
        key='No initial claim is endorsed. Use the later CRN1 factor evidence to decide.',
        look='Hear reasons from different parts of the class, with each learner’s prediction already recorded.',
        iff='If learners seek a correct answer now, say: “Which factor evidence would decide?”')
    s=l.slide('CRN1 · test every whole-number claim','Observe',8,
        'Give each learner CRN1 and the blank record. Read its definitions: whole '
        'numbers here are 0,1,2,…; a prime is an integer greater than 1 with '
        'exactly two positive divisors. Learners complete all nine rows alone, '
        'including parity, prime/composite/neither and positive factor pairs for '
        '9 and 15. They decide both the odd-prime and zero-even claims.',
        say='Keep parity and prime classification in separate columns. Show the factor pairs for 9 and 15.',
        wait='Eight minutes of individual work before partner comparison.',
        key=CORE_KEY,
        look='Inspect five records for all nine values, both independent classifications, and both factor-pair lists.',
        iff='If a category is guessed from parity, say: “Which positive divisors support that choice?” '
            'If 1 is called prime, point back to the supplied “exactly two” condition.',check=True)
    number_grid(s,['0','1','2','3','4','9','11','15','21'])
    tx(s,'Odd/even · prime/composite/neither · reason',.75,5.02,11.4,.5,24,INK,True)
    tx(s,'Also list positive factor pairs for 9 and 15.',.75,5.63,9.4,.55,23)
    timer(s,'8:00','work alone')
    l.task('Compare the divisor evidence','Observe',6,
        ['Compare every row with a partner.','Check the positive factor pairs for 9 and 15.','Decide both claims using evidence.'],
        'Pairs compare all CRN1 rows for six minutes, including whether every odd '
        'whole number is prime and whether zero is even. Each learner retains '
        'their own working and records a disagreement or justified change. '
        'No displayed key is available yet.',
        key=CORE_KEY,
        look='Hear three pairs explain factor evidence rather than repeat a label; check individual records remain.',
        iff='If agreement replaces a reason, say: “Show the divisors or multiplication that decides.”',clock='6:00')
    s=l.slide('Zero: can the even rule include it?','Explain',3,
        'Return to the zero prediction. Establish that a whole number is even '
        'when it equals 2 times a whole number. Elicit and show 0=2×0. '
        'Keep parity separate from prime/composite membership.',
        key='0=2×0, so zero is even. 0 is neither prime nor composite: these '
            'categories apply to whole numbers greater than 1. Zero is not excluded from even numbers.',
        look='Ask an initially uncertain learner to explain zero’s parity with the displayed product.',
        iff='If “zero means nothing” is used to exclude it, ask: “Does 0=2×0 satisfy the even rule?”',check=True)
    chips(s,['0 = 2 × 0','EVEN'])
    tx(s,'Its parity does not make it prime or composite.',.75,4.6,11.5,.9,27)
    s=l.slide('One: how many positive divisors?','Explain',2,
        'Ask for 1’s positive divisors. Compare the single divisor with the '
        'prime definition. Define composite as a whole number greater than 1 '
        'with more than two positive divisors. Make the “neither” category explicit.',
        key='1 has only one positive divisor: 1. It is odd, but neither prime '
            'nor composite. A prime is greater than 1 with exactly two positive '
            'divisors; a composite is greater than 1 with more than two.',
        look='Hear a learner distinguish “one divisor” from “two positive divisors”.',
        iff='If “only 1 and itself” is used, say: “For the number 1, are those two different divisors?”',check=True)
    chips(s,['1 → {1}','ONE divisor'])
    tx(s,'ODD · NEITHER PRIME NOR COMPOSITE',.75,4.6,11.5,.8,28,INK,True)
    s=l.slide('Nine gives us a counterexample','Explain',3,
        'Invite learners to supply both positive factor pairs for 9 and 15. '
        'The editable arrays are number representations, not photographs of supplies. '
        'Use 9 as one counterexample to the universal odd-prime claim. '
        'Check CRN1: primes 2,3,11; composites 4,9,15,21; neither 0,1. '
        'Even 0,2,4; the remaining listed values are odd.',
        key=CORE_KEY,
        look='Hear one learner name the extra divisor 3 of 9 and explain why one counterexample is enough.',
        iff='If 9 is still called prime because it is odd, ask: “Does 3 divide 9 exactly?”',check=True)
    for x,n,rows,cols,pairs in [(.75,9,3,3,'1 × 9 · 3 × 3'),(6.8,15,3,5,'1 × 15 · 3 × 5')]:
        box(s,x,2.25,5.75,3.5,CREAM)
        tx(s,str(n),x+.2,2.45,1.0,.6,34,INK,True)
        for r in range(rows):
            for c in range(cols):oval(s,x+1.6+c*.55,2.57+r*.55,.33,.33,'CF128C')
        tx(s,pairs,x+.2,4.65,5.35,.5,25,INK,True,A.CENTER)
    tx(s,'9 is odd and composite. One counterexample disproves “every”.',.75,6.0,11.5,.65,24,INK,True)
    s=l.slide('Two classifications. Different questions.','Explain',2,
        'Review every CRN1 value using this two-way arrangement. Ask learners '
        'to revise individual records in a new colour. Add the source reminder '
        'that every whole number n=n/1 is rational; the source competency '
        'wording does not imply that irrational whole numbers exist. '
        'Preserve full real-number and finite-display investigation for Lesson 2.',
        key=CORE_KEY,
        look='Check five records for 2 as an even prime and 0 and 1 as neither prime nor composite.',
        iff='If parity is used as a prime rule, contrast 2 and 4, then 3 and 9. '
            'If an irrational whole number is proposed, ask for its n/1 representation.',check=True)
    table(s,['Parity','Prime','Composite','Neither'],[
        ['Even','2','4','0'],['Odd','3, 11','9, 15, 21','1']],
        .75,2.5,11.8,2.5,[2.0,2.5,4.0,3.3],27)
    tx(s,'Every whole number n = n/1 is rational.',.75,5.5,11.5,.7,29,INK,True)
    l.board('Ask how these whole numbers sit within the wider real-number system; keep the detailed classification for Lesson 2.')
    s=l.slide('Revise the classroom supply label','Model Building',4,
        'Each learner keeps their original prediction and writes a corrected '
        'supply-label model in a new colour. Require the distinction between '
        'parity and divisors, 0 and 1 as neither prime nor composite, and a '
        'specific counterexample. Use today’s CRN1 evidence; do not solve the '
        'anchor’s later reciprocal issue.',
        key='Example: “Odd does not mean prime: 9 is odd and has positive divisors '
            '1,3,9. Zero is even because 0=2×0. Zero and 1 are neither prime nor '
            'composite.” Accept equivalent mathematically justified label models.',
        look='Inspect five labels for a named counterexample, zero’s parity evidence and correct categories for 0 and 1.',
        iff='If the label merely changes “all” to “some”, say: “Which example and divisors make your correction convincing?”',check=True)
    box(s,.75,2.4,7.3,3.4,CREAM)
    tx(s,'ORIGINAL CLAIM',1.0,2.65,6.8,.4,16,MUTED,True)
    tx(s,'“Every odd count is prime.”',1.0,3.35,6.8,1.1,32,INK,True)
    tx(s,'Keep this first claim. Add a justified revision.',1.0,4.95,6.8,.6,23)
    tx(s,'New colour\nCounterexample\nFactor evidence',8.7,2.9,3.7,2.3,27,INK,True)
    timer(s,'4:00','revise alone')
    l.task('Exit · classify 21 and 0','Model Building',3,
        ['Classify both by parity and divisors.','Give evidence for each decision.'],
        'Collect an individual exit and corrected label from each learner. '
        'Accept equivalent factor evidence; do not infer individual mastery '
        'from the earlier pair discussion.',
        key='21 is odd and composite: positive factor pairs (1,21),(3,7), '
            'with divisors 1,3,7,21. 0=2×0 is even and neither prime nor '
            'composite. Both are rational as 21/1 and 0/1.',
        look='Check each exit for separate parity and divisor-based classifications, '
             'including a nontrivial factor pair for 21.',
        iff='If 21 is called prime because it is odd, ask: “What is 3×7?” '
            'If zero is called composite, point to the greater-than-1 condition.',clock='3:00')
    l.summary();l.save()


if __name__=='__main__':
    raise SystemExit('Superseded pre-quiz writer. Use quiz-v1 source-specific specifications and build_curriculum_set_lesson.py; see QUIZ_DESIGN.md.')
    parser=argparse.ArgumentParser()
    parser.add_argument('curriculum',choices=['essential','core'])
    args=parser.parse_args()
    {'essential':essential,'core':core}[args.curriculum]()
