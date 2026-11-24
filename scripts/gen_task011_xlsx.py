import os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from docx import Document
from docx.shared import Pt, Inches, RGBColor

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\career-advancement-toolkit'
NAVY='1F3864'; GREY='F2F2F2'
thin=Side(style='thin',color='BFBFBF'); border=Border(left=thin,right=thin,top=thin,bottom=thin)

# Career Growth Strategy Workbook
wb=Workbook(); ws=wb.active; ws.title='Strategy'
ws['A1']='Career Growth Strategy Workbook'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Current Position','Desired Position','Career Vision','Short-term Objectives','Medium-term Objectives','Long-term Objectives','Preferred Pathway','Strengths','Development Gaps','Opportunities','Obstacles','Action Plan','Review Date']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border
row+=1
for i in range(10):
    for j in range(13): ws.cell(row=row,column=j+1).border=border
    row+=1
for i,w in enumerate([18,18,24,24,24,24,16,20,20,20,20,30,14],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'career-planning','Career_Growth_Strategy_Workbook.xlsx'))
print('saved strategy')

# Professional Impact Tracker
wb=Workbook(); ws=wb.active; ws.title='Impact'
ws['A1']='Professional Impact and Achievement Tracker'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Project/Responsibility','Business Problem','Your Contribution','Action Taken','Result','Evidence','Stakeholders','Skills Demonstrated','Impact Type','Date','Achievement Category','Promotion Relevance']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border
row+=1
for i in range(15):
    for j in range(12): ws.cell(row=row,column=j+1).border=border
    row+=1
for i,w in enumerate([22,24,24,24,20,20,18,20,16,12,18,20],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'performance-and-promotion','Professional_Impact_Achievement_Tracker.xlsx'))
print('saved impact')

# Promotion Prep Workbook
wb=Workbook(); ws=wb.active; ws.title='Promotion Prep'
ws['A1']='Promotion Preparation Workbook'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Current Position','Target Position','Role Expectations','Current Responsibilities','Next-Level Responsibilities','Evidence of Impact','Missing Capabilities','Development Plan','Manager Discussion Prep','Conversation Notes','Follow-up Actions']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border
row+=1
for i in range(10):
    for j in range(11): ws.cell(row=row,column=j+1).border=border
    row+=1
for i,w in enumerate([18,18,24,24,24,24,20,24,24,24,24],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'performance-and-promotion','Promotion_Preparation_Workbook.xlsx'))
print('saved promotion prep')

# Leadership Development Workbook
wb=Workbook(); ws=wb.active; ws.title='Leadership'
ws['A1']='Leadership Development Workbook'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Leadership Area','Self-Assessment','Strengths','Development Areas','Scenario','Decision-Making','Delegation','Feedback','Conflict Resolution','Stakeholder Mgmt','Coaching','Action Plan','Reflection']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border
row+=1
for i in range(10):
    for j in range(13): ws.cell(row=row,column=j+1).border=border
    row+=1
for i,w in enumerate([18,14,20,20,24,18,18,18,18,18,18,24,24],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'leadership','Leadership_Development_Workbook.xlsx'))
print('saved leadership')

# Skills Development Planner
wb=Workbook(); ws=wb.active; ws.title='Skills'
ws['A1']='Professional Skills Development Planner'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Target Role/Direction','Required Skill','Current Capability','Desired Capability','Priority','Evidence of Proficiency','Learning Resource','Practical Exercise','Real-World Application','Demonstrable Output','Review Date','Completion Status']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border
row+=1
for i in range(15):
    for j in range(12): ws.cell(row=row,column=j+1).border=border
    row+=1
for i,w in enumerate([20,18,14,14,10,24,20,24,24,20,14,14],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'skills-and-mobility','Professional_Skills_Development_Planner.xlsx'))
print('saved skills')

# 12-Month Roadmap
wb=Workbook(); ws=wb.active; ws.title='Roadmap'
ws['A1']='12-Month Career Advancement Roadmap'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Month','Monthly Objective','Quarterly Checkpoint','Performance Goals','Skills Goals','Leadership Goals','Portfolio Milestones','Networking Activities','Promotion Prep','Internal Mobility','Reflection','Next-Month Priorities']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border
row+=1
for i in range(12):
    ws.cell(row=row,column=1,value=f'Month {i+1}').border=border
    for j in range(2,13): ws.cell(row=row,column=j).border=border
    row+=1
for i,w in enumerate([10,24,18,24,20,20,20,20,20,20,24,24],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'career-planning','12_Month_Career_Advancement_Roadmap.xlsx'))
print('saved roadmap')

# DOCX files
for fname,title,fields in [
 ('Promotion_Readiness_Assessment.docx','Promotion Readiness Assessment',['Current role performance','Next-level responsibilities','Ownership','Problem-solving','Initiative','Communication','Stakeholder management','Leadership behaviours','Consistency','Business understanding','Evidence of impact','Skill gaps']),
 ('Promotion_and_Workplace_Communication_Library.docx','Promotion and Workplace Communication Library',['Discussing career goals with manager','Requesting development feedback','Asking about promotion criteria','Discussing increased responsibility','Presenting achievements','Requesting performance review discussion','Responding to promotion delays','Responding to promotion rejection','Requesting internal mobility guidance','Communicating with senior stakeholders','Requesting mentorship','Giving professional feedback','Managing disagreement','Discussing workload and priorities']),
 ('Professional_Portfolio_Builder.docx','Professional Portfolio Builder',['Documenting work outcomes','Selecting suitable projects','Writing project summaries','Demonstrating problem-solving','Presenting expertise','Protecting confidential info','Building credible presence','Organising achievements']),
 ('Career_Achievement_Portfolio_Template.docx','Career Achievement Portfolio Template',['Project title','Context','Your role','Actions','Results','Evidence','Skills demonstrated','Relevance']),
 ('Quarterly_Career_Review.docx','Quarterly Career Review',['Career progress','Professional achievements','Skills acquired','Responsibilities gained','Feedback received','Current satisfaction','Career opportunities','Development gaps','Next objectives','Changes in direction']),
 ('Annual_Career_Review.docx','Annual Career Review',['Career progress','Professional achievements','Skills acquired','Responsibilities gained','Feedback received','Current satisfaction','Career opportunities','Development gaps','Next objectives','Changes in direction']),
 ('Career_Direction_Reassessment.docx','Career Direction Reassessment',['Career progress','Professional achievements','Skills acquired','Responsibilities gained','Feedback received','Current satisfaction','Career opportunities','Development gaps','Next objectives','Changes in direction']),
]:
    doc=Document()
    st=doc.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(10.5)
    for s in doc.sections: s.top_margin=Inches(0.7); s.bottom_margin=Inches(0.7); s.left_margin=Inches(0.8); s.right_margin=Inches(0.8)
    p=doc.add_paragraph(); r=p.add_run(title); r.bold=True; r.font.size=Pt(18); r.font.color.rgb=RGBColor(0x1F,0x38,0x64)
    for f in fields:
        p=doc.add_paragraph(); r=p.add_run(f'{f}: ________________________________________________________________'); r.font.size=Pt(10.5)
    folder = 'performance-and-promotion' if 'Promotion' in fname else ('professional-brand' if 'Portfolio' in fname else 'career-planning')
    doc.save(os.path.join(OUT,folder,fname))
    print('saved',fname)
print('ALL DONE')
