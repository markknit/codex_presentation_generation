#!/usr/bin/env python3
"""Package the three Cell Structure drafts with review PDFs, print sheets, notes and evidence."""
import argparse,hashlib,json,shutil,subprocess,zipfile
from pathlib import Path
from pptx import Presentation
from docx import Document
from docx.shared import Inches,Pt
ROOT=Path(__file__).resolve().parents[1]
NAMES={1:'Bio_G10_CellStructure_L1_The_Healing_Cut',2:'Bio_G10_CellStructure_L2_What_Is_a_Cell',3:'Bio_G10_CellStructure_L3_Prokaryotic_vs_Eukaryotic_Cells'}
p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
files=[]
for n,name in NAMES.items():
    src=ROOT/'outputs/drafts'/f'{name}.pptx';target=a.out/src.name;shutil.copy2(src,target);files.append(target)
    pdf=ROOT/f'qa/renders/cellstructure_l{n}'/f'{name}.pdf';target=a.out/f'{name}_ReviewSlides.pdf';shutil.copy2(pdf,target);files.append(target)
    if n>1:
        log=ROOT/'build_logs'/f'{name}.md';target=a.out/log.name;shutil.copy2(log,target);files.append(target)
# Print sheets use the authored slide pages directly, preserving diagram labels and table editability in PPTX.
work=ROOT/'.cache/print_sheets';work.mkdir(parents=True,exist_ok=True)
for n,start,end in [(2,9,14),(3,8,9)]:
    name=NAMES[n];pdf=a.out/f'{name}_ReviewSlides.pdf'
    subprocess.run(['pdfseparate','-f',str(start),'-l',str(end),str(pdf),str(work/f'l{n}-%02d.pdf')],check=True)
    dest=a.out/f'CellStructure_L{n}_PrintSheets.pdf'
    subprocess.run(['pdfunite',*[str(work/f'l{n}-{i:02d}.pdf') for i in range(start,end+1)],str(dest)],check=True);files.append(dest)
d=Document();d.styles['Normal'].font.name='Calibri';d.styles['Normal'].font.size=Pt(10)
d.add_heading('Cell Structure · Lessons 1–3',0);d.add_paragraph('Grade 10 Biology · review drafts · 23 October 2026')
d.add_paragraph('Three separate lesson decks: L1 40 minutes, L2 80 minutes, L3 40 minutes. The user explicitly authorised Lessons 2–3 before completion of the pilot’s external review. All decks remain drafts; no teacher or native PowerPoint approval is implied.')
d.add_heading('Review checklist',1)
for t in ['Open each PPTX in native PowerPoint. Verify Slide Show and Presenter View, including complete speaker notes.','Confirm slides 2–3 stay hidden in each Slide Show. PDFs deliberately include those teacher-only pages.','Check Calibri on the review host; Linux PDF previews use Carlito as a substitute.','Review source fidelity, scientific accuracy, local context, realistic timings and every build-log correction.','Resolve source numbering (1.1 versus 1.3) and the manual/source task differences in the logs.','Preview ARES resources and verify links/offline availability before use; use supplied print sheets as the offline route.','Record teacher decision and date before release.']:
    d.add_paragraph('☐ '+t)
d.add_paragraph('Teacher checker: ____________________   Date: ____________________')
d.add_paragraph('Decision: ☐ Return with corrections   ☐ Approve only after all required checks')
d.add_heading('Using the print sheets',1)
d.add_paragraph('L2: print diagrams, scientist reading, blank evidence table and 12-card page; pre-cut one card set per group. L3: print the side-by-side diagrams and blank comparison table. Reference labels are schematic, not micrographs or measurements.')
d.add_heading('GPU record',1)
d.add_paragraph('CUDA on the GB10 resized previews and computed raster signals on all 62 slides. Native PPTX assembly, document layout, conversion and file operations use CPU code paths. Pixel metrics do not establish scientific or semantic correctness.')
for n,name in NAMES.items():
    ppt=Presentation(ROOT/'outputs/drafts'/f'{name}.pptx')
    for i,s in enumerate(ppt.slides,1):
        d.add_page_break();d.add_heading(f'Lesson {n} · Slide {i}'+(' · TEACHER ONLY (hidden)' if s._element.get('show')=='0' else ''),1)
        image=ROOT/f'qa/renders/cellstructure_l{n}/gpu'/f'slide-{i:02d}_preview.png'
        d.add_picture(str(image),width=Inches(6.3))
        for para in s.notes_slide.notes_text_frame.text.split('\n\n'):
            if para.strip():d.add_paragraph(para.strip())
notes=a.out/'CellStructure_Lessons1-3_TeacherReview.docx';d.save(notes);files.append(notes)
index=a.out/'CellStructure_Lessons1-3_ReviewNotes.md'
index.write_text('''# Cell Structure Lessons 1–3 — review package

All three drafts are supplied as separate PPTX files with teacher notes. L1: 21 slides / 40 minutes; L2: 21 slides / 80 minutes; L3: 20 slides / 40 minutes. Slides 2 and 3 are hidden in each deck. PDF review copies include all slides.

The user explicitly instructed “Proceed with lessons 2-3” after receiving L1. This is a limited draft-generation exception to the pre-batch pilot checkpoint. Teacher, native PowerPoint, font and ARES gates remain open; these files are not released or approved.

The combined TeacherReview document contains a checklist, thumbnails and all speaker notes. L2 and L3 print sheets supply offline diagrams, reading/tables and the card-sort page. Per-deck build logs record source corrections and unresolved manual/source differences. The original L1 build log belongs to the earlier pilot checkpoint and is not a current statement that L2–3 are unbuilt.

CUDA GB10 processing ran on all 62 slide previews. PPTX assembly, LibreOffice conversion, Poppler rasterisation, document layout and file encoding use CPU code paths. Structural validation and visual inspection passed; they are not teacher or native PowerPoint approval.

Outstanding review: scientific and source fidelity; realistic pacing; Calibri fidelity (Carlito substituted locally); 1.1 versus 1.3 numbering; source/manual task exceptions; ARES links/content/offline availability; native Slide Show/Presenter View; teacher sign-off.
''');files.append(index)
bundle=a.out/'CellStructure_Lessons1-3_Drafts.zip'
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
