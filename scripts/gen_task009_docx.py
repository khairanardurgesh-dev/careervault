import os, sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\ai-career-assistant-toolkit'
NAVY = RGBColor(0x1F,0x38,0x64)
for name in ['AI_Career_Discovery_Playbook','AI_Resume_and_Profile_Playbook','AI_Job_Search_Playbook','AI_Interview_Practice_Playbook','AI_Salary_Negotiation_Playbook','AI_Career_Development_Playbook']:
    doc = Document()
    st = doc.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(10.5)
    for s in doc.sections: s.top_margin=Inches(0.7); s.bottom_margin=Inches(0.7); s.left_margin=Inches(0.8); s.right_margin=Inches(0.8)
    p=doc.add_paragraph(); r=p.add_run(name.replace('_',' ')); r.bold=True; r.font.size=Pt(18); r.font.color.rgb=NAVY
    for sec in ['Objective','When to use','Required inputs','Step-by-step process','Prompts in order','Expected output','Human review checklist','Common failure modes','Completion criteria']:
        p=doc.add_paragraph(); r=p.add_run(sec); r.bold=True; r.font.size=Pt(12); r.font.color.rgb=NAVY
        p=doc.add_paragraph(); r=p.add_run(f'[Content for {sec}]'); r.italic=True; r.font.size=Pt(9.5)
    doc.save(os.path.join(OUT,'06_Workflow_Playbooks',f'{name}.docx'))
    print('saved',name)

# Prompt Engineering Workbook
doc = Document()
st = doc.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(10.5)
for s in doc.sections: s.top_margin=Inches(0.7); s.bottom_margin=Inches(0.7); s.left_margin=Inches(0.8); s.right_margin=Inches(0.8)
p=doc.add_paragraph(); r=p.add_run('AI Prompt Engineering Workbook'); r.bold=True; r.font.size=Pt(18); r.font.color.rgb=NAVY
for sec in ['Defining the task','Providing context','Establishing AI role','Setting constraints','Providing source material','Specifying output format','Defining evaluation criteria','Adding examples','Iterating on responses','Verifying the result']:
    p=doc.add_paragraph(); r=p.add_run(sec); r.bold=True; r.font.size=Pt(12); r.font.color.rgb=NAVY
    p=doc.add_paragraph(); r=p.add_run(f'Framework step: {sec}.'); r.font.size=Pt(10.5)
for i in range(20):
    p=doc.add_paragraph(); r=p.add_run(f'Exercise {i+1}: Weak prompt → Improved prompt → Explanation → Practice space.'); r.font.size=Pt(10)
doc.save(os.path.join(OUT,'04_Prompt_Engineering','AI_Prompt_Engineering_Workbook.docx'))
print('saved workbook')
print('ALL DONE')
