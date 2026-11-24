import os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from docx import Document
from docx.shared import Pt, Inches, RGBColor

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\job-search-operating-system'
NAVY='1F3864'; GREY='F2F2F2'
thin=Side(style='thin',color='BFBFBF'); border=Border(left=thin,right=thin,top=thin,bottom=thin)

# Company Research Workbook
wb=Workbook(); ws=wb.active; ws.title='Company Research'
ws['A1']='Target Company Research Workbook'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Company Name','Industry','Company Website','Career Page URL','Location','Preferred Work Arrangement','Target Role','Career Track','Company Size/Category','Why Relevant','Relevant Skills','Known Hiring Opportunities','Recruiter/Contact (user-entered)','Research Date','Research Status','Priority','Next Action','Notes']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border; c.alignment=Alignment(horizontal='center',wrap_text=True)
ws.row_dimensions[row].height=30
row+=1; start=row
for i in range(15):
    for j in range(18): ws.cell(row=row,column=j+1).border=border
    row+=1
end=row-1
dv=DataValidation(type='list',formula1='"High,Medium,Low"',allow_blank=True); ws.add_data_validation(dv); dv.add(f'P{start}:P{end}')
for i,w in enumerate([20,16,22,22,14,14,18,18,14,30,20,20,20,12,14,10,20,20],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'03_Company_Research','Target_Company_Research_Workbook.xlsx'))
print('saved company research')

# Application Tracker
wb=Workbook(); ws=wb.active; ws.title='Applications'
ws['A1']='Job Application Tracker'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Application ID','Company','Job Title','Career Track','Job URL','Location','Work Arrangement','Date Discovered','Application Deadline','Date Applied','Application Source','Resume Version','Recruiter/Contact','Application Status','Follow-up Date','Interview Date','Salary Range (if known)','Priority','Next Action','Last Updated','Notes']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border; c.alignment=Alignment(horizontal='center',wrap_text=True)
ws.row_dimensions[row].height=30
row+=1; start=row
for i in range(20):
    for j in range(21): ws.cell(row=row,column=j+1).border=border
    row+=1
end=row-1
statuses='"Researching,Shortlisted,Preparing application,Applied,Recruiter contacted,Screening,Interview,Assessment,Offer,Rejected,Withdrawn,No response,Closed"'
dv=DataValidation(type='list',formula1=statuses,allow_blank=True); ws.add_data_validation(dv); dv.add(f'N{start}:N{end}')
dv2=DataValidation(type='list',formula1='"High,Medium,Low"',allow_blank=True); ws.add_data_validation(dv2); dv2.add(f'R{start}:R{end}')
# dashboard sheet
ws2=wb.create_sheet('Dashboard')
ws2['A1']='Application Dashboard'; ws2['A1'].font=Font(bold=True,size=14,color=NAVY)
labels=['Total Applications','Active Applications','Interviews','Offers','Rejections']
for i,l in enumerate(labels,3):
    ws2.cell(row=i,column=1,value=l).font=Font(bold=True)
for i,w in enumerate([18,14,14,14,14,14,14,14,14,14,14,16,18,20,14,14,18,10,20,14,24],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'05_Application_Tracking','Job_Application_Tracker.xlsx'))
print('saved application tracker')

# Weekly Planner
wb=Workbook(); ws=wb.active; ws.title='Weekly Plan'
ws['A1']='Weekly Job Search Planner'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Week','Target Applications','Actual Applications','Company Research','Networking Activity','Recruiter Conversations','Interview Prep (hrs)','Follow-ups','Skills Development (hrs)','Weekly Reflection','Next Week Priorities']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border; c.alignment=Alignment(horizontal='center',wrap_text=True)
ws.row_dimensions[row].height=30
row+=1
for i in range(12):
    for j in range(11): ws.cell(row=row,column=j+1).border=border
    row+=1
for i,w in enumerate([8,14,14,14,16,18,14,12,16,30,30],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'08_Weekly_Planning','Weekly_Job_Search_Planner.xlsx'))
print('saved weekly planner')

# Performance Review
wb=Workbook(); ws=wb.active; ws.title='Performance'
ws['A1']='Job Search Performance Review'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
metrics=['Applications Submitted','Recruiter Responses','Screening Calls','Interviews','Assessments','Offers','Rejections','Follow-ups Completed']
row=3
for i,h in enumerate(['Metric','Value','Notes'],1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border
row+=1
for m in metrics:
    ws.cell(row=row,column=1,value=m).border=border
    ws.cell(row=row,column=2,value=0).border=border
    ws.cell(row=row,column=3).border=border
    row+=1
# conversion rates
for label,formula in [('Application-to-Response Rate','=IFERROR(B4/B3,0)'),('Response-to-Interview Rate','=IFERROR(B7/B4,0)'),('Interview-to-Offer Rate','=IFERROR(B9/B7,0)')]:
    ws.cell(row=row,column=1,value=label).font=Font(bold=True)
    ws.cell(row=row,column=2,value=formula).number_format='0%'
    row+=1
ws.column_dimensions['A'].width=32; ws.column_dimensions['B'].width=12; ws.column_dimensions['C'].width=30
wb.save(os.path.join(OUT,'11_Performance_Review','Job_Search_Performance_Review.xlsx'))
print('saved performance review')

# Strategy Planner DOCX
doc=Document()
st=doc.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(10.5)
for s in doc.sections: s.top_margin=Inches(0.7); s.bottom_margin=Inches(0.7); s.left_margin=Inches(0.8); s.right_margin=Inches(0.8)
def h1(t): p=doc.add_paragraph(); r=p.add_run(t); r.bold=True; r.font.size=Pt(18); r.font.color.rgb=RGBColor(0x1F,0x38,0x64)
h1('Job Search Strategy Planner')
for f in ['Target career track','Current experience','Target job titles','Target industries','Preferred locations','Remote/hybrid/onsite preference','Expected compensation range','Minimum acceptable compensation','Current skills','Skills gaps','Target companies','Weekly application capacity','Networking capacity','Interview preparation time','Personal constraints','Success indicators']:
    p=doc.add_paragraph(); r=p.add_run(f'{f}: ________________________________________________________________'); r.font.size=Pt(10.5)
doc.save(os.path.join(OUT,'06_Strategy_Planning','Job_Search_Strategy_Planner.docx'))
print('saved strategy planner')
print('ALL DONE')
