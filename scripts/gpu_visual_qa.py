#!/usr/bin/env python3
"""Resize slide renders on CUDA and report simple raster signals; not a science/semantic review."""
import argparse
import ctypes
import hashlib
import json
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('images',nargs='+',type=Path)
    parser.add_argument('--out',required=True,type=Path)
    args=parser.parse_args()
    repo=Path(__file__).resolve().parents[1]
    cache=repo/'.cache';cache.mkdir(exist_ok=True)
    src=repo/'scripts/gpu_image_ops.cu';lib=cache/'gpu_image_ops.so'
    if not lib.exists() or src.stat().st_mtime>lib.stat().st_mtime:
        subprocess.run(['/usr/local/cuda/bin/nvcc','-arch=sm_121','--shared','-Xcompiler','-fPIC',str(src),'-o',str(lib)],check=True)
    gpu=ctypes.CDLL(str(lib)).gpu_resize
    gpu.argtypes=[ctypes.c_void_p,ctypes.c_int,ctypes.c_int,ctypes.c_void_p,ctypes.c_int,ctypes.c_int,ctypes.c_void_p]
    gpu.restype=ctypes.c_int
    args.out.mkdir(parents=True,exist_ok=True)
    reports=[];thumbs=[]
    for file in args.images:
        with Image.open(file) as im: im=im.convert('RGB')
        w,h=im.size;ow,oh=800,round(800*h/w)
        host=ctypes.create_string_buffer(im.tobytes());out=ctypes.create_string_buffer(ow*oh*3);counts=(ctypes.c_uint*2)()
        rc=gpu(host,w,h,out,ow,oh,counts)
        if rc: raise RuntimeError(f'CUDA operation failed ({rc}); CPU fallback is prohibited')
        thumb=Image.frombytes('RGB',(ow,oh),out.raw);target=args.out/(file.stem+'_preview.png');thumb.save(target)
        reports.append({'image':str(file),'preview':str(target),'width':w,'height':h,'nonwhite_fraction':counts[0]/(w*h),'dark_fraction':counts[1]/(w*h),'sha256':hashlib.sha256(im.tobytes()).hexdigest()})
        thumbs.append((file.stem,thumb))
    # Compositing labels/tiles is CPU file-layout work; all resampling and pixel metrics above execute on CUDA.
    for start in range(0,len(thumbs),8):
        page=thumbs[start:start+8];tileh=page[0][1].height+36
        sheet=Image.new('RGB',(1600,tileh*4),'#e5e7eb');draw=ImageDraw.Draw(sheet)
        for i,(label,im) in enumerate(page):
            x=(i%2)*800;y=(i//2)*tileh;draw.text((x+12,y+10),label,fill='black');sheet.paste(im,(x,y+36))
        sheet.save(args.out/f'contact_{start//8+1:02}.jpg',quality=92)
    record={'backend':'CUDA sm_121','operations':['nearest-neighbour preview resizing','pixel ink/darkness counts'],'limits':'No semantic, scientific, font, or PowerPoint compatibility claim. PNG I/O and contact-sheet compositing use CPU.','device':subprocess.check_output(['nvidia-smi','--query-gpu=name,driver_version,compute_cap','--format=csv,noheader'],text=True).strip(),'slides':reports}
    (args.out/'gpu_report.json').write_text(json.dumps(record,indent=2))
    print(f'CUDA processed {len(reports)} slides; output: {args.out}')
if __name__=='__main__':main()
