#!/usr/bin/env python3
"""Source-specific authoring for the three pilot sub-strands' remaining lessons."""
import json
from pathlib import Path
from curriculum_set_inventory import CONTROL


def slide(phase,minutes,title,kind='bullets',**kwargs):
    return {'phase':phase,'minutes':minutes,'title':title,'kind':kind,**kwargs}


def task(p,m,title,items,**kw):return slide(p,m,title,items=items,timer=f'{m}:00',**kw)
def cards(p,m,title,values,**kw):return slide(p,m,title,'cards',values=values,**kw)
def eq(m,title,text,caption='',**kw):return slide('Explain',m,title,'equation',text=text,caption=caption,**kw)
def tbl(p,m,title,headers,rows,**kw):return slide(p,m,title,'table',headers=headers,rows=rows,**kw)


def lesson(code,short,goals,prediction,observe,explain,model,exit,core=False,**kw):
    result={'code':code,'short':short,'goals':goals,'slides':[
        slide('Predict',2,'Your first idea and reason','question',text=prediction,timer='2:00',mode='write alone'),
        task('Predict',1,'BEFORE · keep our reasons',['Share a prediction and its reason.','Keep a different idea visible.'],
             do='Invite two contrasting predictions from learners who have written individually. Record exact reasons without correction.'),
        *observe,*explain,
        task('Driving Question Board',4,'Our Driving Question Board',
             kw.pop('board',['Post today’s evidence.','Keep a question that needs more evidence.','Sort: answered, partly answered, still open.'])),
        task('Model Building',5 if core else 3,'Revise your own model',model),
        task('Model Building',2,'Individual exit',exit)
    ],**kw}
    return result


def assessment(code,short,goals,rows,**kw):
    return {'code':code,'short':short,'goals':goals,'assessment':True,'slides':[
        task('Predict',3,'Independent work · procedure',[
            'Use only today’s data and assessment prompts.','Keep your working and reasons visible.','Work alone; submit before any discussion.']),*rows],**kw}


def science():
    return {
    '2':lesson('GS12','Observation_and_Inference',
        ['Separate reports from interpretations.','Compare two possible explanations.','Choose a useful additional observation.'],
        'Wet paper, an empty cup and frame droplets. What might explain them?',[
            tbl('Observe',6,'GS12 · classify the six statements',['#','Statement','Your class'],[
                ['1','The paper beside the closed window is wet.',''],['2','Rain must have entered through a gap.',''],
                ['3','A cup on the sill is empty.',''],['4','Someone may have spilled water.',''],
                ['5','Where did the water come from?',''],['6','The window frame has droplets on it.','']],
                widths=[.5,9.2,2.1],size=20,height=3.4,caption='Reported observation, inference or question? Record alone.',timer='6:00',mode='classify alone'),
            task('Observe',6,'Compare possible explanations',['Compare your six classifications.','Construct two explanations fitting two observations.','Keep the evidence for each separate.']),
            task('Observe',4,'Which observation would help next?',['Share one safe additional observation.','Explain how it could distinguish your two ideas.'])],[
            tbl('Explain',3,'Which words report the evidence?',['Reports','Interpretations','Question'],[['1, 3, 6','2, 4','5']],size=28,height=2.2,
                caption='An inference interprets observations; it is not certain knowledge of an unseen cause.'),
            slide('Explain',3,'Does an empty cup prove a spill?','columns',columns=[['CONSISTENT WITH','Rain entering\nA spill\nAnother justified explanation'],['DOES NOT PROVE','An empty cup alone does not identify the cause.']],
                caption='Condensation is another candidate if justified; avoid accusations.'),
            task('Explain',4,'Write a limited explanation',['Name one observation and two interpretations.','State a limit and a safe follow-up check.'])],
        ['Keep observation and inference in separate boxes.','Retain your first explanation; annotate changed confidence.'],
        ['Give one observation and two inferences.','Add one useful, safe additional check.'],
        board=['What would distinguish rain from a spill?','Separate a measurement from a witness report.','Keep untested explanations open.'],
        record={'headers':['Statement','Observation / inference / question','Reason'],'rows':[[str(i),'',''] for i in range(1,7)]}),
    '3':lesson('GS13','Repeated_Water_Rise_Evidence',
        ['Organise repeated measurements with units.','Calculate and compare means.','State a conclusion within the test’s limits.'],
        'Which paper would show greater water rise in 60 seconds? What must we measure?',[
            tbl('Observe',8,'GS13 · printed illustrative readings',['Paper type','Trial 1 (mm)','Trial 2 (mm)','Trial 3 (mm)','Mean (mm)'],
                [['A','18','20','22',''],['B','9','10','11','']],widths=[2.2,2.4,2.4,2.4,2.4],height=2.8,size=23,
                caption='Printed illustrative fallback · equal 60 s tests · not your own measurements.',timer='8:00',mode='check data'),
            task('Observe',5,'Calculate each mean',['Add the three rises for each paper.','Divide each total by the number of trials.','Keep millimetres in your record.']),
            task('Observe',3,'Compare the pattern',['Which mean is greater?','What varied between repeat readings?','What can this test actually support?'])],[
            eq(3,'Mean rise in this printed trial','A: (18 + 20 + 22)/3 = 20 mm','B: (9 + 10 + 11)/3 = 10 mm'),
            slide('Explain',3,'Compare means without losing the conditions','bars',categories=['A','B'],series=[['Mean rise',[20,10]]],
                axis='Mean water rise (mm)',category_axis='Paper type',caption='Printed illustrative data · after equal 60 s tests.'),
            task('Explain',4,'What can we infer?',['Use “in these conditions” in your conclusion.','Name what was kept comparable.','State one untested property or limitation.'])],
        ['Add collection, organisation and analysis to your evidence model.','Cite the labelled printed data; retain untested properties.'],
        ['Give a numerical conclusion with units.','State one limit of that conclusion.'],
        route='Use the source-permitted printed illustrative fallback. This draft does not claim hands-on measurement. The optional real trial requires teacher preparation/access review; follow the unchanged source procedure and safety notes if selected.',
        preparation='One labelled GS13 data sheet per learner; notebook, pencil, ruler for the printed table and timer. The printed route requires no water or apparatus.',
        decisions='Printed fallback chosen explicitly. Never present means or printed values as class observations. Source clean-water/paper trial remains an optional teacher-reviewed route, not a fabricated practical.',
        record={'headers':['Paper','Trial 1 (mm)','Trial 2 (mm)','Trial 3 (mm)','Mean (mm)'],'rows':[['A','18','20','22',''],['B','9','10','11','']]}),
    '4':lesson('GS14','Seedling_Claims_and_Confounds',
        ['Use counts to describe a change.','Identify another changed factor.','Plan a fairer written comparison.'],
        'The trays received different water amounts. Does that alone establish the cause?',[
            tbl('Observe',5,'GS14 · illustrative garden records',['Tray','Monday','Friday','Water daily (mL)','Environment'],
                [['P','10','6','20','Sunny room'],['Q','10','9','40','Cooler shaded room']],
                widths=[.8,1.6,1.6,3.0,4.8],size=22,height=2.7,caption='Illustrative records · not a real class experiment.',timer='5:00',mode='extract evidence'),
            task('Observe',7,'Write a fairer comparison plan',['Use all six GS14 plan headings.','Name the changed factor and comparable conditions.','Specify an outcome, repeats and a limitation.']),
            task('Observe',4,'Ask a partner to test the plan',['What else could explain the difference?','Does your plan separate those possibilities?'])],[
            eq(3,'What changed in the counts?','P: 10 − 6 = 4 seedlings lost','Q: 10 − 9 = 1 seedling lost'),
            slide('Explain',3,'Two differences changed together','columns',columns=[['WATER','P: 20 mL daily\nQ: 40 mL daily'],['ENVIRONMENT','P: sunny room\nQ: cooler shaded room']],
                caption='Light, temperature and location can confound the water claim.'),
            task('Explain',4,'Defend a bounded conclusion',['Say what the counts show.','Explain why water alone is not isolated.','Describe one concrete design improvement.'])],
        ['Add competing explanations and fair comparison to your model.','Preserve the initial claim and revise with today’s record.'],
        ['Name one confound.','Give one concrete design change.'],
        route='Written planning from illustrative GS14 records only; no seed-growing practical is added.',
        record={'headers':['Plan heading','Your decision'],'rows':[[x,''] for x in ['Question','Changed factor','Factors kept comparable','Measured outcome','Repeats','Limitation']]}),
    '5':lesson('GS15','Careers_and_Source_Evidence',
        ['Identify two science-related career directions.','Link each direction to source evidence.','Explain an interest and a next learning action.'],
        'Which science-related career direction interests you? What would you like to know?',[
            slide('Observe',4,'GS15 · two printed source summaries','columns',columns=[
                ['SOURCE A · KENYA METEOROLOGICAL DEPARTMENT','Weather/climate observations, analysis, forecasting and early warnings.'],
                ['SOURCE B · KEMRI','A national research role concerning human health.']],
                caption='Source-supplied paraphrases checked 13 November 2026; not quotations or qualification advice.'),
            task('Observe',8,'Build your own career chart',['Cover both directions using all GS15 columns.','Label suggested questions and evidence as examples.','Keep stated roles separate from your inferences.']),
            task('Observe',4,'Check the source support',['Verify statements against the printed summaries.','Use the optional approved official-page route only if provided.','Record actual navigation as observed or not observed.'])],[
            slide('Explain',3,'What do the source roles support?','columns',columns=[
                ['SUPPORTED CAREER DIRECTION','Weather/climate science\nHuman-health research'],
                ['STILL NEEDS CHECKING','Training requirements\nSpecific job duties\nQualifications or employment']],caption='A reasonable career inference is not a job guarantee.'),
            task('Explain',3,'Connect evidence and possible benefit',['Use source A or B for each career link.','Explain a possible community benefit as an example.']),
            task('Explain',4,'Explain an interest without an overclaim',['Give a reason for your chosen direction.','Name a training question that remains unverified.','Keep the two source limits visible.'])],
        ['Add careers to your evidence model.','Write one attainable personal learning action and a reason.'],
        ['Submit your individual chart.','Explain why your next learning action matters.'],
        route='Printed summaries remain the offline route. Optional official-page navigation uses only teacher-approved pages/cached copies. Print work is not evidence of digital navigation; no personal data or unrelated links.',
        preparation='GS15 printed source summaries and blank chart per learner. Optional supervised device access only if locally provided and observed.',
        record={'headers':['Direction','Questions / evidence','Possible benefit','Source support','Still needed'],'rows':[['Weather/climate science','','','',''],['Human-health research','','','','']]}),
    '6':lesson('GS16','Defensible_Science_Use_Message',
        ['Connect scientific evidence with a possible use.','Critique an overclaim respectfully.','Revise a sourced message with limits.'],
        'Which claim from our earlier work most needs a qualification?',[
            task('Observe',10,'GS16 · draft the one-page message',['Include life, environment and technology examples.','Explain each evidence-to-decision link.','Add a small career chart and a next learning action.']),
            task('Observe',4,'Exchange one evidence-based critique',['Identify one supported claim.','Identify one overclaim and ask a question.']),
            task('Observe',2,'Choose a revision',['Select a change your evidence supports.','Keep the first wording visible.'])],[
            slide('Explain',3,'From evidence to a possible use','flow',nodes=['Observation','Inference','Possible use','Limit'],
                caption='Use a specific GS11–GS15 example; do not turn a proposed use into a tested outcome.'),
            slide('Explain',3,'Which claim respects the absorption test?','columns',columns=[
                ['SUPPORTED SCOPE','Paper A had greater mean rise in the stated printed trial.'],
                ['OVERCLAIM','“Paper A is always best for every job.”']],caption='Material selection needs a test of the property required for that job.'),
            task('Explain',4,'Explain why your revision is stronger',['Cite the evidence and its source.','State the limit or uncertainty.','Explain the possible usefulness without promising an outcome.'])],
        ['Revise the same message in a new colour.','Record a personal next action and retain a still-open question.'],
        ['Define General Science in your own words.','Give one useful link and one remaining uncertainty.'],
        preparation='GS16 and earlier GS11–GS15 cards, learners’ own records, two colours and paper. No new practical or treatment/weather advice.',
        record={'headers':['Application','Evidence / source','Possible decision','Limit'],'rows':[['Life','','',''],['Environment','','',''],['Technology','','','']]}),
    '7':assessment('GS17','Independent_Evidence_Transfer',
        ['Use unfamiliar evidence independently.','Evaluate a claim and its limits.','Explain a source-supported application.'],[
            task('Observe',16,'Assessment · sections 1–2',['Use only GS17 and the separate assessment prompts.','Show your own means, units and reasoning.','Keep observations and interpretations distinct.']),
            task('Explain',12,'Assessment · sections 3–4',['Complete the career/source and reflection prompts.','Check that evidence and limits are labelled.','Work independently; no exemplar is shown.']),
            task('Driving Question Board',4,'A separate still-open scientific question',['Write one still-open scientific question.','Explain what additional evidence could help.','Keep the question private until collection.']),
            task('Model Building',4,'Check and submit',['Check names, units and completion.','Submit all sheets before any discussion.'])],
        preparation='Print only GS17 and the original independent assessment prompts. Basic calculator optional. Keep all teaching cards and exemplars private.',
        route='Independent printed assessment. Phase names are scheduling labels; no peer discussion, hints or answer correction before collection.',
        record={'headers':['Material','Trial 1 (mm)','Trial 2 (mm)','Trial 3 (mm)','Mean (mm)'],'rows':[['X','12','14','16',''],['Y','6','8','10','']]})}


if __name__=='__main__':
    raise SystemExit('Superseded pre-quiz writer. Use quiz-v1 source-specific specifications and build_curriculum_set_lesson.py; see QUIZ_DESIGN.md.')
    folder=CONTROL/'specs';folder.mkdir(parents=True,exist_ok=True)
    data={'module':'gensci_1_1','whole_unit_read':True,
          'anchor_line':'Our school notice board: which claims go beyond the evidence?', 'lessons':science()}
    data['lessons']['2']['slides'][0]['caption']='Record your confidence as well as your reason.'
    data['lessons']['3']['preparation']+=' Show or describe the two paper samples before prediction, without hinting at the result. If descriptions are unavailable, retain that uncertainty rather than invent paper properties.'
    data['lessons']['4']['slides'][0].update({'kind':'columns','columns':[
        ['TRAY P','10 seedlings → 6\n20 mL water daily'],['TRAY Q','10 seedlings → 9\n40 mL water daily']],
        'caption':'Does water alone explain the difference? Give your first reason.'})
    data['lessons']['5']['slides'][1].update({'title':'BEFORE · a question about science work',
        'items':['Share a question about the work if you wish.','Keep a personal career choice private if you prefer.'],
        'do':'Invite voluntary questions about the work, not compulsory personal aspirations. Do not rank careers. Keep every learner’s private written reason.'})
    (folder/'gensci_1_1.json').write_text(json.dumps(data,indent=2,ensure_ascii=False))
    print('Authored General Science Introduction L2–7 specs.')
