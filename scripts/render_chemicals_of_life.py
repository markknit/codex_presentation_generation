#!/usr/bin/env python3
"""CPU PDF conversion/rasterisation, CUDA resize and pixel checks; no semantic sign-off."""
import hashlib, json, subprocess
from pathlib import Path
from build_chemicals_of_life import ROOT, NAMES, OUT

for n,name in NAMES.items():
    dest=ROOT/'qa/renders/chemicals_of_life'/f'l{n}'
    dest.mkdir(parents=True,exist_ok=True)
    ppt=OUT/(name+'.pptx')
    subprocess.run(['soffice','-env:UserInstallation=file://'+str(ROOT/'.cache/lo-chemicals'), '--headless','--convert-to','pdf:impress_pdf_Export:{"ExportHiddenSlides":{"type":"boolean","value":"true"}}','--outdir',str(dest),str(ppt)],check=True)
    subprocess.run(['pdftoppm','-png','-r','110',str(dest/(name+'.pdf')),str(dest/'slide')],check=True)
    pngs=sorted(dest.glob('slide-*.png'))
    subprocess.run([str(ROOT/'.venv/bin/python'),str(ROOT/'scripts/gpu_visual_qa.py'),*map(str,pngs),'--out',str(dest/'gpu')],check=True)
    report=json.loads((dest/'gpu/gpu_report.json').read_text())
    report['deck_sha256']=hashlib.sha256(ppt.read_bytes()).hexdigest()
    (ROOT/'qa'/f'{name}_gpu.json').write_text(json.dumps(report,indent=2))
