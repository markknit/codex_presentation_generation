#!/usr/bin/env python3
"""Package the three Cell Structure drafts with review PDFs, print sheets, notes and evidence."""
import argparse,hashlib,json,shutil,subprocess,zipfile
from pathlib import Path
from pptx import Presentation
from docx import Document
from docx.shared import Inches,Pt
ROOT=Path(__file__).resolve().parents[1]
NAMES={1:'Bio_G10_CellStructure_L1_The_Healing_Cut',2:'Bio_G10_CellStructure_L2_What_Is_a_Cell',3:'Bio_G10_CellStructure_L3_Prokaryotic_vs_Eukaryotic_Cells',6:'Bio_G10_CellStructure_L6_Onion_Cells_Practical'}
p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);p.add_argument('--lessons',type=int,nargs='+',default=[1,2,3],choices=[1,2,3,6]);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
NAMES={n:NAMES[n] for n in sorted(set(a.lessons))}
stem='CellStructure_Lessons1-3' if list(NAMES)==[1,2,3] else 'CellStructure_Pilot_Lessons'+'-'.join(map(str,NAMES))
label=', '.join(map(str,NAMES))
slide_total=sum(len(Presentation(ROOT/'outputs/drafts'/f'{name}.pptx').slides) for name in NAMES.values())
files=[]
for n,name in NAMES.items():
    src=ROOT/'outputs/drafts'/f'{name}.pptx';target=a.out/src.name;shutil.copy2(src,target);files.append(target)
    pdf=ROOT/f'qa/renders/cellstructure_l{n}'/f'{name}.pdf';target=a.out/f'{name}_ReviewSlides.pdf';shutil.copy2(pdf,target);files.append(target)
    if n>1:
        log=ROOT/'build_logs'/f'{name}.md';target=a.out/log.name;shutil.copy2(log,target);files.append(target)
# Print sheets use the authored slide pages directly, preserving diagram labels and table editability in PPTX.
work=ROOT/'.cache/print_sheets';work.mkdir(parents=True,exist_ok=True)
for n,start,end in [(n,start,end) for n,start,end in [(2,9,14),(3,8,9),(6,9,11)] if n in NAMES]:
    name=NAMES[n];pdf=a.out/f'{name}_ReviewSlides.pdf'
    subprocess.run(['pdfseparate','-f',str(start),'-l',str(end),str(pdf),str(work/f'l{n}-%02d.pdf')],check=True)
    dest=a.out/f'CellStructure_L{n}_PrintSheets.pdf'
    subprocess.run(['pdfunite',*[str(work/f'l{n}-{i:02d}.pdf') for i in range(start,end+1)],str(dest)],check=True);files.append(dest)
d=Document();d.styles['Normal'].font.name='Calibri';d.styles['Normal'].font.size=Pt(10)
d.add_heading('Cell Structure · Pilot lessons '+label,0);d.add_paragraph('Grade 10 Biology · review drafts · 23 October 2026')
d.add_paragraph('Separate lesson decks: '+', '.join('L'+str(n)+' '+('40' if n in [1,3] else '80')+' minutes' for n in NAMES)+'. The user explicitly authorised these pilot drafts. All remain drafts; no teacher, safety or native PowerPoint approval is implied.')
d.add_heading('Review checklist',1)
for t in ['Open each PPTX in native PowerPoint. Verify Slide Show and Presenter View, including complete speaker notes.','Confirm slides 2–3 stay hidden in each Slide Show. PDFs deliberately include those teacher-only pages.','Check Calibri on the review host; Linux PDF previews use Carlito as a substitute.','Review source fidelity, scientific accuracy, local context, realistic timings and every build-log correction.','Resolve source numbering (1.1 versus 1.3) and the manual/source task differences in the logs.','Preview ARES resources and verify links/offline availability before use; use supplied print sheets as the offline route.','Record teacher decision and date before release.']:
    d.add_paragraph('☐ '+t)
d.add_paragraph('Teacher checker: ____________________   Date: ____________________')
d.add_paragraph('Decision: ☐ Return with corrections   ☐ Approve only after all required checks')
d.add_heading('Using the print sheets',1)
d.add_paragraph('L2: print diagrams, scientist reading, blank evidence table and 12-card page; pre-cut one card set per group. L3: print the side-by-side diagrams and blank comparison table. Reference labels are schematic, not micrographs or measurements.')
if 6 in NAMES:
    d.add_heading('Lesson 6 practical readiness',1)
    d.add_paragraph('Before classroom use, the school must confirm the stain product/concentration/SDS, PPE, disposal, individual restrictions, real microscope performance and field calibration. The source no-goggles and improvised pharmacy-stain fallbacks are flagged, not approved. L6 assumes the earlier L4–5 teaching/model; adding it to this pilot does not generate those lessons. The comparison schematic is not a real observation. See the L6 build log and observation sheet.')
d.add_heading('GPU record',1)
d.add_paragraph(f'CUDA on the GB10 resized previews and computed raster signals on all {slide_total} slides. Native PPTX assembly, document layout, conversion and file operations use CPU code paths. Pixel metrics do not establish scientific, semantic or practical-safety correctness.')
for n,name in NAMES.items():
    ppt=Presentation(ROOT/'outputs/drafts'/f'{name}.pptx')
    for i,s in enumerate(ppt.slides,1):
        d.add_page_break();d.add_heading(f'Lesson {n} · Slide {i}'+(' · TEACHER ONLY (hidden)' if s._element.get('show')=='0' else ''),1)
        image=ROOT/f'qa/renders/cellstructure_l{n}/gpu'/f'slide-{i:02d}_preview.png'
        d.add_picture(str(image),width=Inches(6.3))
        for para in s.notes_slide.notes_text_frame.text.split('\n\n'):
            if para.strip():d.add_paragraph(para.strip())
notes=a.out/(stem+'_TeacherReview.docx');d.save(notes);files.append(notes)
if 6 in NAMES:
    from docx.enum.table import WD_ROW_HEIGHT_RULE
    obs=Document();obs.styles['Normal'].font.name='Calibri';obs.styles['Normal'].font.size=Pt(10)
    obs.add_heading('Onion microscopy · individual observation record',0)
    obs.add_paragraph('Name: ____________________  Group: ______  Date: __________')
    obs.add_paragraph('Draw only what you observe. Label uncertain features as uncertain. This blank sheet does not supply an expected result.')
    for title in ['Low power: draw 3–4 cells','Higher power: draw one cell']:
        obs.add_heading(title,2);obs.add_paragraph('Eyepiece: ____ ×   Objective: ____ ×   Total optical magnification: ____ ×')
        t=obs.add_table(rows=1,cols=1);t.style='Table Grid';t.rows[0].height=Inches(1.65);t.rows[0].height_rule=WD_ROW_HEIGHT_RULE.EXACTLY
    obs.add_page_break();obs.add_heading('Cell-size estimate and evidence',1)
    fields=[('Measured field diameter at objective ____ ×','____ mm'),('Number of cell lengths across the field (long axis)','____'),('Estimated cell length = field diameter ÷ count','____ mm'),('Estimated length in μm = mm × 1000','____ μm')]
    t=obs.add_table(rows=1,cols=2);t.style='Table Grid';t.rows[0].cells[0].text='Quantity / method';t.rows[0].cells[1].text='My value'
    for title,value in fields:
        cells=t.add_row().cells;cells[0].text=title;cells[1].text=value
    for title in ['Chloroplast visibility: what did I actually observe? Was the view clear enough to judge?','Other features visible / unclear / not seen','How did my evidence change my prediction?','Claim — Evidence — Reasoning','A specific prediction for the next animal-cell practical']:
        obs.add_heading(title,2);obs.add_paragraph('_________________________________________________________________\n_________________________________________________________________')
    target=a.out/'CellStructure_L6_ObservationSheet.docx';obs.save(target);files.append(target)
index=a.out/(stem+'_ReviewNotes.md')
index.write_text('# Cell Structure pilot lessons '+label+' — review drafts\n\n'+str(slide_total)+' total slides. Each separate deck has hidden teacher slides 2–3; review PDFs include all pages. Full speaker notes and per-lesson build logs are included.\n\nThe user authorised adding these lessons to the pilot. They are not approved for classroom use or release. Native PowerPoint/Presenter View, Calibri, ARES and teacher/source-owner checks remain open.\n\nIf Lesson 6 is included, its iodine/PPE/fallback, actual microscope visibility, field calibration and local risk-assessment decisions require teacher sign-off. L4–5 remain prerequisites, not newly generated lessons. The L6 observation sheet is blank; reference drawings and example calculations must not replace pupil data.\n\nCUDA processes all raster previews and pixel signals. PPTX assembly, conversion and file/layout work use CPU operations. These checks are not scientific or safety approval.\n')
files.append(index)
bundle=a.out/(stem+'_Drafts.zip')
with zipfile.ZipFile(bundle,'w',zipfile.ZIP_DEFLATED) as z:
    for f in files:z.write(f,f.name)
    for n,name in NAMES.items():
        candidates=[ROOT/'qa'/f'{name}_validation.json',ROOT/'qa'/f'{name}_manifest.json',ROOT/'qa'/f'{name}_gpu.json'] if n>1 else [ROOT/'qa'/f'{name}_validation.json',ROOT/'qa/Bio_G10_CellStructure_manifest.json',ROOT/'qa/Bio_G10_CellStructure_L1_gpu.json']
        for f in candidates:
            if f.exists():z.write(f,'qa/'+f.name)
for f in files+[bundle]:
    if f.suffix in ['.zip','.pptx','.docx']:
        with zipfile.ZipFile(f) as z:assert z.testzip() is None
print('Packaged',len(files),'review files;',bundle)
