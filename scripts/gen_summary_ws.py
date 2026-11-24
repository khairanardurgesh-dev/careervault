import os, sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\resume-mastery-system\03_Workbooks'
doc = Document()
st = doc.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(10.5)
for s in doc.sections:
    s.top_margin=Inches(0.7); s.bottom_margin=Inches(0.7); s.left_margin=Inches(0.8); s.right_margin=Inches(0.8)
def h1(t):
    p=doc.add_paragraph(); r=p.add_run(t); r.bold=True; r.font.size=Pt(18); r.font.color.rgb=RGBColor(0x1F,0x38,0x64)
def para(t):
    p=doc.add_paragraph(); r=p.add_run(t); r.font.size=Pt(10.5)
h1('Professional Summary Worksheet')
para('Framework: Domain + Years + Key Skills + Target Role + Value.')
para('Draft your summary below, then refine.')
for i in range(5):
    para(f'Draft {i+1}: ________________________________________________________________')
para('Checklist: specific, no generic claims, tailored to JD, 2-4 sentences.')
doc.save(os.path.join(OUT,'Professional_Summary_Worksheet.docx'))
print('saved')
