import os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from docx import Document
from docx.shared import Pt, Inches, RGBColor

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\salary-and-offer-negotiation-system'
NAVY='1F3864'; GREY='F2F2F2'
thin=Side(style='thin',color='BFBFBF'); border=Border(left=thin,right=thin,top=thin,bottom=thin)

# Offer Comparison Calculator
wb=Workbook(); ws=wb.active; ws.title='Offer Comparison'
ws['A1']='Salary & Offer Comparison Calculator'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
ws['A2']='Manual inputs. Estimates only. Not tax advice.'; ws['A2'].font=Font(italic=True,size=9,color='595959')
# Inputs section
row=4
headers=['Component','Offer 1','Offer 2','Offer 3']
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border
row+=1
inputs=['Annual CTC','Annual Fixed Gross','Annual Target Variable','Joining Bonus (one-time)','Retention Bonus (one-time)','Employer PF','Gratuity','Equity Value (annual)','Other Benefits','One-time Payments']
start=row
for inp in inputs:
    ws.cell(row=row,column=1,value=inp).border=border
    for j in range(2,5): ws.cell(row=row,column=j).border=border
    row+=1
# Outputs
ws.cell(row=row,column=1,value='Fixed Annual Compensation').font=Font(bold=True)
for j in range(2,5):
    ws.cell(row=row,column=j,value=f'=B{start+1}').border=border
row+=1
ws.cell(row=row,column=1,value='Target Annual Cash').font=Font(bold=True)
for j in range(2,5):
    ws.cell(row=row,column=j,value=f'=B{start+1}+B{start+2}').border=border
row+=1
ws.cell(row=row,column=1,value='First-Year Compensation').font=Font(bold=True)
for j in range(2,5):
    ws.cell(row=row,column=j,value=f'=B{start+1}+B{start+2}+B{start+3}+B{start+4}').border=border
row+=1
ws.cell(row=row,column=1,value='Recurring Annual Compensation').font=Font(bold=True)
for j in range(2,5):
    ws.cell(row=row,column=j,value=f'=B{start+1}+B{start+2}').border=border
# Weighted preference
row+=2
ws.cell(row=row,column=1,value='Candidate-Defined Weighted Preference').font=Font(bold=True,color=NAVY)
row+=1
for i,h in enumerate(['Priority','Weight','Offer 1 Score','Offer 2 Score','Offer 3 Score'],1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border
row+=1
priorities=['Compensation','Role Quality','Career Growth','Work-Life Balance','Location','Learning','Stability','Benefits']
pstart=row
for p in priorities:
    ws.cell(row=row,column=1,value=p).border=border
    ws.cell(row=row,column=2,value=0.125).number_format='0%'
    for j in range(3,6): ws.cell(row=row,column=j,value=3).border=border
    row+=1
pend=row-1
ws.cell(row=row,column=1,value='Weighted Total').font=Font(bold=True)
for j in range(3,6):
    col=get_column_letter(j)
    ws.cell(row=row,column=j,value=f'=SUMPRODUCT($B{pstart}:$B{pend},{col}{pstart}:{col}{pend})').font=Font(bold=True)
    ws.cell(row=row,column=j).number_format='0.00'
for i,w in enumerate([30,14,14,14],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'03_Editable_Workbooks','Salary_and_Offer_Comparison_Calculator.xlsx'))
print('saved offer calculator')

# Benefits Comparison
wb=Workbook(); ws=wb.active; ws.title='Benefits'
ws['A1']='Compensation and Benefits Comparison'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Benefit','Employer 1','Employer 2','Employer 3','Candidate Priority','Employer Confirmation','Notes']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border
row+=1
benefits=['Health Insurance','Dependants Coverage','Leave Entitlement','Remote Work','Working Days','Flexible Hours','Learning Budget','Transport','Meal Benefits','Retirement Contributions','Equity','Bonus Conditions','Relocation Assistance','Other Benefits']
for b in benefits:
    ws.cell(row=row,column=1,value=b).border=border
    for j in range(2,8): ws.cell(row=row,column=j).border=border
    row+=1
for i,w in enumerate([24,16,16,16,16,20,24],1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'03_Editable_Workbooks','Compensation_and_Benefits_Comparison.xlsx'))
print('saved benefits')

# DOCX workbooks
for fname,title,fields in [
 ('Salary_Expectation_Preparation_Workbook.docx','Salary Expectation Preparation Workbook',['Current role','Current responsibilities','Current fixed compensation','Current variable compensation','Actual variable received','Current benefits','Target role','Target industry','Target location','Experience','Demonstrable skills','Professional achievements','Research sources','Target compensation range','Minimum acceptable offer','Preferred compensation structure','Non-monetary priorities','Negotiating points']),
 ('Salary_Negotiation_Strategy_Planner.docx','Salary Negotiation Strategy Planner',['Negotiation objective','Preferred outcome','Minimum acceptable outcome','Supporting evidence','Negotiable components','Non-negotiable conditions','Questions for recruiter','Risks and trade-offs','Final decision']),
 ('Salary_Negotiation_Practice_Workbook.docx','Salary Negotiation Practice Workbook',['Scenario 1: Initial salary expectations','Scenario 2: Low offer','Scenario 3: Competing offers','Scenario 4: Fixed vs variable','Scenario 5: Joining bonus','Scenario 6: Notice period','Scenario 7: Delayed joining','Scenario 8: Relocation','Scenario 9: Benefits clarification','Scenario 10: Offer deadline','Scenario 11: Verbal promises','Scenario 12: Counteroffer','Scenario 13: Negotiation failure','Scenario 14: Final acceptance','Scenario 15: Professional rejection']),
]:
    doc=Document()
    st=doc.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(10.5)
    for s in doc.sections: s.top_margin=Inches(0.7); s.bottom_margin=Inches(0.7); s.left_margin=Inches(0.8); s.right_margin=Inches(0.8)
    p=doc.add_paragraph(); r=p.add_run(title); r.bold=True; r.font.size=Pt(18); r.font.color.rgb=RGBColor(0x1F,0x38,0x64)
    for f in fields:
        p=doc.add_paragraph(); r=p.add_run(f'{f}: ________________________________________________________________'); r.font.size=Pt(10.5)
    doc.save(os.path.join(OUT,'03_Editable_Workbooks',fname))
    print('saved',fname)
print('ALL DONE')
