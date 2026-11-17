#!/usr/bin/env python3
"""CPU file layout only: recompose existing CUDA-sized previews, no resampling."""
import argparse,json
from pathlib import Path
from PIL import Image,ImageDraw


def main(root):
    count=0
    for report in root.rglob('gpu_report.json'):
        data=json.loads(report.read_text());assert data['backend']=='CUDA sm_121'
        previews=[]
        for row in data['slides']:
            p=Path(row['preview'])
            previews.append((Path(row['image']).stem,Image.open(p).convert('RGB')))
        for start in range(0,len(previews),8):
            page=previews[start:start+8];height=page[0][1].height+36
            sheet=Image.new('RGB',(1600,height*((len(page)+1)//2)),'#e5e7eb');draw=ImageDraw.Draw(sheet)
            for i,(label,im) in enumerate(page):
                x=(i%2)*800;y=(i//2)*height
                draw.text((x+12,y+10),label,fill='black');sheet.paste(im,(x,y+36))
            sheet.save(report.parent/f'contact_{start//8+1:02}.jpg',quality=92);count+=1
    print('Reflowed',count,'contact sheets; existing CUDA previews unchanged.')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('root',type=Path);a=p.parse_args();main(a.root)
