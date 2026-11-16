#!/usr/bin/env python3
"""CPU document conversion; fail-closed CUDA raster previews and pixel metrics."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs/drafts/curriculum_pilots_2026-11'

def main():
    p=argparse.ArgumentParser();p.add_argument('prefix',nargs='?',default='')
    a=p.parse_args()
    for ppt in sorted(OUT.glob(a.prefix+'*.pptx')):
        dest=ROOT/'qa/renders/curriculum_pilots_2026-11'/ppt.stem;dest.mkdir(parents=True,exist_ok=True)
        subprocess.run(['soffice','-env:UserInstallation=file://'+str(ROOT/'.cache/lo-curriculum-pilots'),'--headless',
            '--convert-to','pdf:impress_pdf_Export:{"ExportHiddenSlides":{"type":"boolean","value":"true"}}',
            '--outdir',str(dest),str(ppt)],check=True)
        subprocess.run(['pdftoppm','-png','-r','110',str(dest/(ppt.stem+'.pdf')),str(dest/'slide')],check=True)
        pngs=sorted(dest.glob('slide-*.png'))
        subprocess.run([str(ROOT/'.venv/bin/python'),str(ROOT/'scripts/gpu_visual_qa.py'),*map(str,pngs),'--out',str(dest/'gpu')],check=True)
        report=json.loads((dest/'gpu/gpu_report.json').read_text())
        report['deck_sha256']=hashlib.sha256(ppt.read_bytes()).hexdigest()
        (ROOT/'qa'/f'{ppt.stem}_gpu.json').write_text(json.dumps(report,indent=2))
        for doc in sorted(OUT.glob(ppt.stem+'*.docx')):
            subprocess.run(['soffice','-env:UserInstallation=file://'+str(ROOT/'.cache/lo-curriculum-pilots'),'--headless',
                '--convert-to','pdf','--outdir',str(OUT),str(doc)],check=True)
            pages=dest/doc.stem
            pages.mkdir(parents=True,exist_ok=True)
            subprocess.run(['pdftoppm','-png','-r','85',str(OUT/(doc.stem+'.pdf')),str(pages/'page')],check=True)
            subprocess.run([str(ROOT/'.venv/bin/python'),str(ROOT/'scripts/gpu_visual_qa.py'),
                            *map(str,sorted(pages.glob('page-*.png'))),'--out',str(pages/'gpu')],check=True)

if __name__=='__main__':main()
