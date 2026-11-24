import os, sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\professional-profile-optimisation-system\03_Editable_Templates'
NAVY = RGBColor(0x1F,0x38,0x64); GREY=RGBColor(0x59,0x59,0x59)
names = ['Technology_IT','Business_Analysis','Product_Management','Project_Management','Finance_Accounting','Sales_Business_Development','Marketing_Growth','Management_Operations','Early_Career_Professional','Experienced_Professional','Career_Switcher','General_Professional']
for n in names:
    doc = Document()
    st = doc.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(10.5)
    for s in doc.sections:
        s.top_margin=Inches(0.7); s.bottom_margin=Inches(0.7); s.left_margin=Inches(0.8); s.right_margin=Inches(0.8)
    p=doc.add_paragraph(); r=p.add_run(f'Professional Profile Template — {n.replace("_"," ")}'); r.bold=True; r.font.size=Pt(16); r.font.color.rgb=NAVY
    for field in ['Professional Headline','About Section','Current Experience','Previous Experience','Achievements','Skills','Certifications','Education','Projects','Featured Content','Portfolio Links','Target Roles','Professional Positioning Statement']:
        p=doc.add_paragraph(); r=p.add_run(field); r.bold=True; r.font.size=Pt(11); r.font.color.rgb=NAVY
        p=doc.add_paragraph(); r=p.add_run(f'[Replace with your {field.lower()}]'); r.italic=True; r.font.color.rgb=GREY; r.font.size=Pt(9.5)
        doc.add_paragraph()
    p=doc.add_paragraph(); r=p.add_run('Instructions: Replace all bracketed placeholders with truthful information. Remove sections that do not apply. Do not fabricate achievements or credentials.'); r.italic=True; r.font.size=Pt(9)
    doc.save(os.path.join(OUT, f'{n}_Profile_Template.docx'))
    print('saved', n)
print('ALL TEMPLATES DONE')
