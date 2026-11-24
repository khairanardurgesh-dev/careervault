import os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from docx import Document
from docx.shared import Pt, Inches, RGBColor

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\90-day-job-switch-programme'
NAVY='1F3864'; GREY='F2F2F2'
thin=Side(style='thin',color='BFBFBF'); border=Border(left=thin,right=thin,top=thin,bottom=thin)

# 90-Day Daily Action Calendar
wb=Workbook(); ws=wb.active; ws.title='Daily Calendar'
ws['A1']='90-Day Daily Action Calendar'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Day','Date','Phase','Weekly Objective','Daily Action','Estimated Time','Priority','Completion Status','Notes','Relevant Module']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border; c.alignment=Alignment(horizontal='center',wrap_text=True)
ws.row_dimensions[row].height=30
row+=1; start=row
for d in range(1,91):
    phase = 'Foundation' if d<=30 else ('Activation' if d<=60 else 'Execution')
    ws.cell(row=row,column=1,value=d).border=border
    ws.cell(row=row,column=2,value=None).border=border
    ws.cell(row=row,column=3,value=phase).border=border
    ws.cell(row=row,column=4,value=f'Week {(d-1)//7+1} objective').border=border
    ws.cell(row=row,column=5,value=f'Day {d} action').border=border
    ws.cell(row=row,column=6,value='30 min').border=border
    ws.cell(row=row,column=7,value='Medium').border=border
    ws.cell(row=row,column=8,value='Not Started').border=border
    ws.cell(row=row,column=9).border=border
    ws.cell(row=row,column=10,value='CareerVault').border=border
    row+=1
end=row-1
dv=DataValidation(type='list',formula1='"Not Started,In Progress,Completed,Skipped"',allow_blank=True); ws.add_data_validation(dv); dv.add(f'H{start}:H{end}')
# dashboard
ws2=wb.create_sheet('Dashboard')
ws2['A1']='Calendar Dashboard'; ws2['A1'].font=Font(bold=True,size=14,color=NAVY)
ws2.cell(row=3,column=1,value='Total Days').font=Font(bold=True)
ws2.cell(row=3,column=2,value=f'=COUNTA(\'Daily Calendar\'!A{start}:A{end})')
ws2.cell(row=4,column=1,value='Completed').font=Font(bold=True)
ws2.cell(row=4,column=2,value=f'=COUNTIF(\'Daily Calendar\'!H{start}:H{end},"Completed")')
ws2.cell(row=5,column=1,value='Completion %').font=Font(bold=True)
ws2.cell(row=5,column=2,value=f'=IFERROR(B4/B3,0)').number_format='0%'
for i,w in enumerate([6,12,14,24,40,12,10,14,20,18],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'programme-calendar','90_Day_Daily_Action_Calendar.xlsx'))
print('saved calendar')

# Weekly Planner
wb=Workbook(); ws=wb.active; ws.title='Weekly Plan'
ws['A1']='Weekly Job Switch Planner'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Week','Weekly Objective','Planned Activities','Available Time','Priority Tasks','Applications Planned','Networking Activities','Interview Prep','Skills Development','Completed Tasks','Weekly Reflection','Next-Week Adjustments']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border; c.alignment=Alignment(horizontal='center',wrap_text=True)
ws.row_dimensions[row].height=30
row+=1
for i in range(13):
    for j in range(12): ws.cell(row=row,column=j+1).border=border
    row+=1
for i,w in enumerate([8,24,30,12,30,16,20,16,16,16,30,30],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'programme-calendar','Weekly_Job_Switch_Planner.xlsx'))
print('saved weekly planner')

# Dashboard
wb=Workbook(); ws=wb.active; ws.title='Dashboard'
ws['A1']='90-Day Job Switch Dashboard'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
items=['Current Phase','Daily Completion %','Weekly Completion %','Day 30 Checkpoint','Day 60 Checkpoint','Day 90 Checkpoint','Current Target Role','Applications Submitted','Recruiter Responses','Interviews Completed','Offers Received','Skills Progress','Next Priority Action']
row=3
for i,l in enumerate(items,1):
    ws.cell(row=row,column=1,value=l).font=Font(bold=True)
    ws.cell(row=row,column=2,value='').border=border
    row+=1
ws.column_dimensions['A'].width=28; ws.column_dimensions['B'].width=24
wb.save(os.path.join(OUT,'programme-calendar','90_Day_Job_Switch_Dashboard.xlsx'))
print('saved dashboard')

# Target Role Workbook
wb=Workbook(); ws=wb.active; ws.title='Target Role'
ws['A1']='Target Role and Career Direction Workbook'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Current Role','Desired Role','Alternative Roles','Preferred Industries','Transferable Skills','Experience Evidence','Skill Gaps','Salary Expectations','Work Preferences','Decision Matrix Score']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border
row+=1
for i in range(10):
    for j in range(10): ws.cell(row=row,column=j+1).border=border
    row+=1
for i,w in enumerate([18,18,20,18,20,24,20,16,18,14],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'assessments','Target_Role_and_Career_Direction_Workbook.xlsx'))
print('saved target role')

# Skills Gap Planner
wb=Workbook(); ws=wb.active; ws.title='Skills Gap'
ws['A1']='Skills Gap and Learning Planner'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Target Role','Required Skill','Current Proficiency','Evidence','Gap','Priority','Learning Resource','Practice Activity','Completion Date','Demonstrable Output']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border
row+=1
for i in range(15):
    for j in range(10): ws.cell(row=row,column=j+1).border=border
    row+=1
for i,w in enumerate([18,18,14,24,18,10,20,24,14,20],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'assessments','Skills_Gap_and_Learning_Planner.xlsx'))
print('saved skills gap')

# Performance Review
wb=Workbook(); ws=wb.active; ws.title='Performance'
ws['A1']='Job Search Performance Review'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
metrics=['Applications','Recruiter Responses','Screening Calls','Interview Invitations','Interview Stages','Rejections','Follow-ups','Referrals','Networking Conversations','Skills Development']
row=3
for i,h in enumerate(['Metric','Value','Notes'],1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border
row+=1
for m in metrics:
    ws.cell(row=row,column=1,value=m).border=border
    ws.cell(row=row,column=2,value=0).border=border
    ws.cell(row=row,column=3).border=border
    row+=1
ws.column_dimensions['A'].width=28; ws.column_dimensions['B'].width=10; ws.column_dimensions['C'].width=30
wb.save(os.path.join(OUT,'tracking','Job_Search_Performance_Review.xlsx'))
print('saved performance')

# Interview Improvement
wb=Workbook(); ws=wb.active; ws.title='Interview Improvement'
ws['A1']='Interview Performance Improvement Workbook'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Interview Date','Company & Role','Interview Stage','Questions Asked','Self-Assessment','Strong Responses','Weak Responses','Knowledge Gaps','Feedback Received','Follow-up Actions','Prep Plan']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border
row+=1
for i in range(10):
    for j in range(11): ws.cell(row=row,column=j+1).border=border
    row+=1
for i,w in enumerate([14,20,14,30,14,24,24,20,24,24,24],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'tracking','Interview_Performance_Improvement_Workbook.xlsx'))
print('saved interview improvement')

# DOCX files
for fname,title,fields in [
 ('Job_Switch_Readiness_Assessment.docx','Job Switch Readiness Assessment',['Career clarity','Role suitability','Skills readiness','Resume readiness','Profile readiness','Job-market understanding','Interview readiness','Compensation expectations','Personal time availability','Transition considerations']),
 ('Job_Switch_Decision_Journal.docx','Job Switch Decision Journal',['Why I want to switch','What I want from my next role','What I will not compromise on','My career priorities','My progress so far','Difficult decisions','Lessons from rejection','Offer evaluation','Final decision','My next 90-day career objectives']),
 ('Day_30_Review_Template.docx','Day 30 Review Template',['Completed actions','Remaining tasks','Skills and profile improvements','Job-search progress','Interview progress','Obstacles','What is working','What is not working','Changes required','Next-stage priorities']),
 ('Day_60_Review_Template.docx','Day 60 Review Template',['Completed actions','Remaining tasks','Skills and profile improvements','Job-search progress','Interview progress','Obstacles','What is working','What is not working','Changes required','Next-stage priorities']),
 ('Day_90_Review_Template.docx','Day 90 Review Template',['Completed actions','Remaining tasks','Skills and profile improvements','Job-search progress','Interview progress','Obstacles','What is working','What is not working','Changes required','Next-stage priorities','Offer received scenario','No offer scenario']),
]:
    doc=Document()
    st=doc.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(10.5)
    for s in doc.sections: s.top_margin=Inches(0.7); s.bottom_margin=Inches(0.7); s.left_margin=Inches(0.8); s.right_margin=Inches(0.8)
    p=doc.add_paragraph(); r=p.add_run(title); r.bold=True; r.font.size=Pt(18); r.font.color.rgb=RGBColor(0x1F,0x38,0x64)
    for f in fields:
        p=doc.add_paragraph(); r=p.add_run(f'{f}: ________________________________________________________________'); r.font.size=Pt(10.5)
    doc.save(os.path.join(OUT,'assessments' if 'Readiness' in fname else 'reflection',fname))
    print('saved',fname)
print('ALL DONE')
