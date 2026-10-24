#!/usr/bin/env python3
"""Render the eight remaining drafts, process previews on CUDA and check the complete unit. Run from the repository root after both builders."""
import sys,subprocess,json,hashlib
from pathlib import Path
sys.path.insert(0,'scripts')
from build_cellstructure_remaining_v2 import ROOT,REMAINING_NAMES
out=ROOT/'qa/renders/cellstructure_complete_v2'
for n,name in REMAINING_NAMES.items():
 p=ROOT/'outputs/drafts/v2'/f'{name}.pptx'
 subprocess.run([str(ROOT/'.venv/bin/python'),'scripts/validate_lesson_deck.py',str(p),'--minutes',str(40 if n in [3,11] else 80)],check=True,stdout=subprocess.DEVNULL)
 subprocess.run(['soffice','-env:UserInstallation=file://'+str(ROOT/'.cache/lo-complete-v2'),'--headless','--convert-to','pdf:impress_pdf_Export:{"ExportHiddenSlides":{"type":"boolean","value":"true"}}','--outdir',str(out),str(p)],check=True)
 dest=out/f'l{n}';dest.mkdir(exist_ok=True)
 subprocess.run(['pdftoppm','-png','-r','110',str(out/f'{name}.pdf'),str(dest/'slide')],check=True)
 subprocess.run([str(ROOT/'.venv/bin/python'),'scripts/gpu_visual_qa.py',*map(str,sorted(dest.glob('slide-*.png'))),'--out',str(dest/'gpu')],check=True)
 report=json.loads((dest/'gpu/gpu_report.json').read_text());report['deck_sha256']=hashlib.sha256(p.read_bytes()).hexdigest();(ROOT/'qa'/f'{name}_gpu.json').write_text(json.dumps(report,indent=2))
subprocess.run([str(ROOT/'.venv/bin/python'),'scripts/check_cellstructure_complete_v2.py'],check=True)
