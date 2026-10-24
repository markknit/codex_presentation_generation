"""Editable science illustrations for the remainder of the Cell Structure unit."""
import math
from lesson_visuals import *

def polygon(s,pts,fill,border=INK,width=1):
 pts=[(int(Inches(x)),int(Inches(y))) for x,y in pts]
 b=s.shapes.build_freeform(*pts[0]);b.add_line_segments(pts[1:],close=True);sh=b.convert_to_shape();sh.fill.solid();sh.fill.fore_color.rgb=rgb(fill);sh.line.color.rgb=rgb(border);sh.line.width=Pt(width);return sh

def path(s,pts,color=INK,width=2):
 for a,b in zip(pts,pts[1:]):line(s,*a,*b,color,width)

def specialised(s,kind,x=.9,y=2.65,w=5.2,h=3.35,labels=False):
 def P(a,b):return x+w*a,y+h*b
 if kind=='red blood cell':
  oval(s,*P(.12,.16),w*.66,h*.65,'CD6272','A83E54');oval(s,*P(.28,.33),w*.34,h*.3,'EBA9B2')
 elif kind=='neutrophil':
  oval(s,*P(.08,.06),w*.75,h*.85,'ECE3F2','936BAE')
  for a,b in [(.3,.3),(.43,.4),(.35,.55)]:oval(s,*P(a,b),w*.19,h*.19,'8B5CA8')
  path(s,[P(.37,.4),P(.5,.47),P(.41,.61)],'8B5CA8',max(2,w))
  for a,b in [(.22,.26),(.59,.28),(.65,.65),(.24,.7),(.63,.49)]:oval(s,*P(a,b),w*.055,h*.07,'D898B2')
 elif kind=='neuron':
  polygon(s,[P(a,b) for a,b in [(.08,.42),(.18,.24),(.32,.28),(.43,.45),(.32,.67),(.17,.69)]],'D8C7EB','936BAE');oval(s,*P(.2,.41),w*.1,h*.14,'9468B2')
  for end in [(.02,.08),(.01,.75),(.27,.04),(.43,.1)]:
   path(s,[P(.23,.46),P(end[0],end[1])],'936BAE',2)
   path(s,[P(end[0],end[1]),P(end[0]+.04,end[1]-.04)],'936BAE',1)
  line(s,*P(.4,.47),*P(.92,.47),'9F6C59',3)
  for i in range(5):box(s,*P(.44+i*.085,.38),w*.065,h*.18,'E6C87B','BDA160')
  for yy in [.2,.47,.78]:path(s,[P(.91,.47),P(.99,yy)],'9F6C59',2);oval(s,*P(.98,yy),w*.03,h*.04,'9F6C59')
 elif kind=='sperm cell':
  oval(s,*P(.06,.3),w*.2,h*.35,'DAC6EB','936BAE');oval(s,*P(.1,.35),w*.12,h*.25,'9468B2')
  box(s,*P(.25,.43),w*.18,h*.12,'F0B574')
  for i in range(5):oval(s,*P(.26+i*.03,.43),w*.025,h*.12,'CD9761')
  path(s,[P(.43+i*.012,.49+.12*math.sin(i*.3)) for i in range(46)],'9468B2',2)
 elif kind=='skeletal muscle fibre':
  box(s,*P(.03,.2),w*.94,h*.57,'F2C4CA','BC6D7B')
  for i in range(15):line(s,*P(.08+i*.06,.24),*P(.08+i*.06,.73),'D18A98',1.5)
  for a in [.12,.4,.7]:oval(s,*P(a,.24),w*.09,h*.10,'9468B2');organelle(s,'mitochondrion',*P(a,.60),w*.11,h*.11)
 elif kind=='platelet':
  pts=[]
  for i in range(24):
   a=i*math.pi/12;r=.38 if i%2==0 else .25;pts.append(P(.45+r*math.cos(a),.48+r*math.sin(a)))
  polygon(s,pts,'E6BD62','A77943')
  for a,b in [(.35,.4),(.5,.4),(.45,.6)]:oval(s,*P(a,b),w*.05,h*.07,'BE8A40')
 elif kind=='macrophage':
  polygon(s,[P(a,b) for a,b in [(.1,.3),(.22,.2),(.2,.03),(.44,.18),(.7,.08),(.82,.3),(.72,.5),(.9,.8),(.58,.77),(.4,.95),(.2,.73),(.04,.6)]],'D9E8EF','6689A0')
  oval(s,*P(.27,.35),w*.30,h*.32,'A38AC4');oval(s,*P(.43,.32),w*.19,h*.22,'D9E8EF')
  for a,b in [(.2,.3),(.65,.3),(.58,.65),(.24,.71)]:oval(s,*P(a,b),w*.06,h*.08,'D898B2')
 elif kind=='fibroblast':
  polygon(s,[P(a,b) for a,b in [(0,.25),(.35,.32),(.68,.15),(1,.05),(.78,.48),(1,.82),(.62,.72),(.24,.89),(0,.98),(.2,.6)]],'D1E4DD','5D8F80')
  organelle(s,'nucleus',*P(.32,.35),w*.24,h*.3);organelle(s,'rough ER',*P(.59,.4),w*.21,h*.19);organelle(s,'Golgi apparatus',*P(.24,.72),w*.2,h*.13)
 elif kind=='epidermal cells':
  for row in range(3):
   for col in range(4):
    xx=x+col*w*.23+(row%2)*w*.02;yy=y+row*h*.25
    box(s,xx,yy,w*.225,h*.24,'F2C7BA','C58979');oval(s,xx+w*.08,yy+h*.075,w*.07,h*.08,'A38AC4')
 elif kind=='root hair cell':
  pts=[(.08,.05),(.48,.05),(.48,.43),(.95,.43),(1,.49),(.95,.56),(.48,.56),(.48,.95),(.08,.95)]
  polygon(s,[P(a,b) for a,b in pts],'E2EFCB','659055',2);box(s,*P(.14,.15),w*.27,h*.66,'C0E8E9','71B3BC');oval(s,*P(.415,.65),w*.05,h*.12,'A38AC4')
 elif kind=='guard cells':
  for flip in [False,True]:
   pts=[(.42,.07),(.18,.14),(.08,.4),(.13,.72),(.35,.92),(.43,.83),(.29,.61),(.26,.4),(.34,.22)]
   if flip:pts=[(1-a,b) for a,b in pts]
   polygon(s,[P(a,b) for a,b in pts],'C4DEA0','50814F',1.4)
   for a,b in [(.22,.28),(.19,.49),(.28,.72)]:
    if flip:a=1-a-.05
    oval(s,*P(a,b),w*.05,h*.065,'57925C')
  path(s,[P(.42,.07),P(.34,.22),P(.26,.4),P(.29,.61),P(.43,.83)],'397045',3)
  path(s,[P(.58,.07),P(.66,.22),P(.74,.4),P(.71,.61),P(.57,.83)],'397045',3)
 elif kind=='xylem vessel':
  box(s,*P(.18,.03),w*.11,h*.94,'B68D62');box(s,*P(.72,.03),w*.11,h*.94,'B68D62')
  for i in range(6):
   line(s,*P(.18,.12+i*.14),*P(.29,.18+i*.14),'82613D',3);line(s,*P(.72,.12+i*.14),*P(.83,.18+i*.14),'82613D',3)
  for yy in [.22,.55]:sh=shape(s,*P(.45,yy),w*.12,h*.18,'68ABBC',kind=M.CHEVRON);sh.rotation=270
 elif kind=='phloem sieve tube':
  for yy in [.05,.49]:box(s,*P(.2,yy),w*.42,h*.44,'E4EFCC','79A169')
  for yy in [.05,.49,.91]:
   line(s,*P(.2,yy),*P(.62,yy),'79A169',3)
   for i in range(4):oval(s,*P(.25+i*.08,yy-.015),w*.035,h*.03,'FFFFFF')
  box(s,*P(.67,.15),w*.16,h*.7,'C5DAA7','79A169');oval(s,*P(.71,.47),w*.08,h*.12,'A38AC4')
 elif kind=='palisade cell':
  box(s,*P(.15,.03),w*.7,h*.94,'DCECCA','659055');box(s,*P(.3,.15),w*.4,h*.7,'BDEAF1','64AFC0')
  for i in range(5):
   for xx in [.2,.73]:oval(s,*P(xx,.13+i*.145),w*.07,h*.09,'57925C')
  oval(s,*P(.45,.86),w*.09,h*.08,'A38AC4')
 if labels:tx(s,kind,x,y+h+.14,w,.48,20,INK,True,A.CENTER)

FEATURES={
'red blood cell':['Biconcave disc','No nucleus in the mature cell','Haemoglobin inside'],
'neutrophil':['Multi-lobed nucleus','Lysosomes with digestive enzymes','Flexible cell boundary'],
'neuron':['Branching dendrites','Long axon, often myelinated','Terminal branches'],
'sperm cell':['Head with nucleus','Mitochondria-rich midpiece','Long flagellum'],
'skeletal muscle fibre':['Long contractile fibre','Parallel contractile filaments','Many nuclei and mitochondria'],
'root hair cell':['Long hair-like extension','Thin wall; large vacuole','Usually no chloroplasts'],
'guard cells':['Paired cells around a pore','Thicker inner walls','Chloroplasts in these cells'],
'xylem vessel':['Hollow lumen','Thick lignified walls','Mature vessel elements are dead'],
'phloem sieve tube':['Perforated sieve plates','Living sieve-tube elements','Companion cell alongside'],
'palisade cell':['Tall elongated cell','Many chloroplasts','Large central vacuole']}
FUNCTIONS={
'red blood cell':'Flexible discs deliver oxygen to respiring tissues.',
'neutrophil':'Engulfs bacteria; lysosomes help digest the engulfed material.',
'neuron':'Carries signals between parts of the body.',
'sperm cell':'Delivers genetic material during fertilisation. It does not heal a finger cut.',
'skeletal muscle fibre':'Contractile filaments shorten the fibre; respiration supports contraction.',
'root hair cell':'The extension increases surface area for water and mineral uptake.',
'guard cells':'Changes in turgor alter the pore opening, regulating gas exchange and water loss.',
'xylem vessel':'Hollow, supported tubes conduct water and minerals and help support the plant.',
'phloem sieve tube':'Transports dissolved sugars from sources to sinks through sieve plates.',
'palisade cell':'Many chloroplasts absorb light for photosynthesis.'}

def cell_detail(s,kind,features=True):
 specialised(s,kind,.85,2.7,5.1,3.3)
 if features:steps(s,FEATURES.get(kind,[]),x=6.5,y=2.72,w=6.0,dy=1.0,size=23,c='D7DF23')
 tx(s,'Editable schematic · not a micrograph · cell types are not shown at one scale',.8,6.53,11.5,.3,12,MUTED)

def sheet_cells(s,kinds,labels=True):
 for i,k in enumerate(kinds):
  xx=.8+i*2.48;specialised(s,k,xx,2.75,2.15,2.5)
  tx(s,k if labels else chr(65+i),xx,5.55,2.15,.85,18,INK,True,A.CENTER)
 tx(s,'Drawn models · not micrographs · not a common scale',.8,6.57,11.5,.3,12,MUTED)

def cheek(s):
 pts=[(.12,.25),(.4,.05),(.8,.1),(.96,.4),(.83,.78),(.48,.95),(.16,.8),(.03,.5)]
 polygon(s,[(4.0+a*4.9,2.6+b*3.6) for a,b in pts],'F5E8EE','AC6483',2)
 organelle(s,'nucleus',5.45,3.7,1.0,.85)
 for title,px,py,xx,yy in [('Cell boundary',4.4,3.5,.8,3),('Nucleus',5.95,4.1,9.5,3.5),('Cytoplasm',7.3,4.8,9.5,5)]:
  tx(s,title,xx,yy,3,.5,22,INK,True);line(s,px,py,3.8 if xx<4 else 9.3,yy+.22,'7D8D94');oval(s,px-.035,py-.035,.07,.07,INK)
 tx(s,'Comparison drawing only · never a substitute for your own recorded observation',.8,6.55,11.6,.3,12,MUTED)

def skin(s,x,y,w,h):
 box(s,x,y,w,h*.22,'E8B394');box(s,x,y+h*.22,w,h*.5,'EBC8C5');box(s,x,y+h*.72,w,h*.25,'F2E1B3')
 for i in range(3):line(s,x+w*(.1+i*.3),y+h*.46,x+w*(.3+i*.3),y+h*.56,'BD7F99',2)

def hierarchy(s,show=True):
 labels=['Cell','Tissue','Organ','Organ system','Organism'];examples=['Epidermal cell','Epithelial tissue','Skin','Integumentary\nsystem','Amina']
 for i,lab in enumerate(labels):
  xx=.7+i*2.52;tx(s,lab,xx,2.45,2.18,.6,21,INK,True,A.CENTER)
  if i==0:box(s,xx+.55,3.35,1.0,.7,'E8B394','BD7F78');oval(s,xx+.93,3.57,.2,.2,'A38AC4')
  elif i==1:
   for a in range(3):
    for b in range(3):box(s,xx+.22+b*.57,3.1+a*.36,.55,.34,'E8B394','BD7F78')
  elif i==2:skin(s,xx+.23,3.1,1.8,1.4)
  elif i==3:
   oval(s,xx+.88,3.1,.43,.43,'E8B394');box(s,xx+.67,3.53,.83,.65,'E8B394');line(s,xx+.67,4.17,xx+.55,4.7,'BD7F78',8);line(s,xx+1.48,4.17,xx+1.6,4.7,'BD7F78',8)
  else:photo(s,'amina',xx+.25,3.1,1.75)
  if show:tx(s,examples[i],xx,5.12,2.18,.92,21,INK,True,A.CENTER)
  if i<4:arrow(s,xx+2.18,3.85,.25,'CF128C')
 tx(s,'Schematic hierarchy · one valid pathway, not every wound cell placed in one tissue',.8,6.4,11.5,.4,14,MUTED)

def poster(s):
 for i,(lab,desc) in enumerate([('A · PLANT CELL','8+ structures + function notes'),('B · ANIMAL CELL','6+ structures + comparison'),('C · HEALING CELLS','3 types: structure → job'),('D · ORGANISATION','Cell → tissue → organ → system → organism')]):
  xx=.8+i%2*6.05;yy=2.38+i//2*1.9;box(s,xx,yy,5.7,1.65,['F2F7DC','F8E8EC','FFF1D5','E5F3F5'][i]);tx(s,lab,xx+.22,yy+.2,5.25,.45,22,INK,True);tx(s,desc,xx+.22,yy+.88,5.25,.6,20)

def gene_switches(s):
 for col,name in enumerate(['Neutrophil','Fibroblast']):
  xx=.85+col*6.25;tx(s,name,xx,2.55,5.55,.5,25,INK,True)
  for i in range(5):box(s,xx+i*.95,3.4,.8,.3,'BE80BE' if (i%2==col) else 'D9E0E3')
  tx(s,'Same broad genetic instructions; different genes used',xx,4.1,5.3,1.05,24)
  tx(s,'Lysosome-rich defence cell' if col==0 else 'Protein-secreting repair cell',xx,5.45,5.4,.8,25,INK,True)
 tx(s,'A simplified model of gene expression, not DNA sequencing data',.85,6.5,11.6,.3,13,MUTED)
