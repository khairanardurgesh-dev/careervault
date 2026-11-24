import os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\professional-profile-optimisation-system\04_Workbooks'
NAVY='1F3864'; GREY='F2F2F2'
thin=Side(style='thin',color='BFBFBF'); border=Border(left=thin,right=thin,top=thin,bottom=thin)

# Profile Audit Workbook
wb = Workbook()
ws = wb.active; ws.title='Audit'
ws['A1']='Professional Profile Audit Workbook'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
ws['A2']='Manual assessment. Not an actual LinkedIn or recruiter scoring algorithm.'; ws['A2'].font=Font(italic=True,size=9,color='595959')
ws.merge_cells('A1:I1'); ws.merge_cells('A2:I2')
headers=['Profile Section','Audit Criterion','Current Status','Evidence/Observation','Improvement Required','Priority','Action Owner','Completion Status','Notes']
row=4
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border; c.alignment=Alignment(horizontal='center',wrap_text=True)
ws.row_dimensions[row].height=30
row+=1; start=row
sections=['Headline','Profile Photo & Banner','About Section','Experience','Skills','Education','Certifications','Projects','Featured Section','Contact Information','Resume Consistency','Overall Positioning']
for s in sections:
    for i in range(3):
        ws.cell(row=row,column=1,value=s).border=border
        for j in range(2,10):
            ws.cell(row=row,column=j).border=border
        row+=1
end=row-1
# dropdowns
dv1=DataValidation(type='list',formula1='"Complete,Partial,Missing"',allow_blank=True); ws.add_data_validation(dv1); dv1.add(f'C{start}:C{end}')
dv2=DataValidation(type='list',formula1='"High,Medium,Low"',allow_blank=True); ws.add_data_validation(dv2); dv2.add(f'F{start}:F{end}')
dv3=DataValidation(type='list',formula1='"Done,In Progress,Not Started"',allow_blank=True); ws.add_data_validation(dv3); dv3.add(f'H{start}:H{end}')
# completion %
row+=1
ws.cell(row=row,column=1,value='Completion %').font=Font(bold=True)
ws.cell(row=row,column=2,value=f'=IFERROR(COUNTIF(H{start}:H{end},"Done")/COUNTA(H{start}:H{end}),"")').number_format='0%'
ws.cell(row=row,column=2).font=Font(bold=True)
widths=[20,24,14,30,30,10,14,14,20]
for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
wb.save(os.path.join(OUT,'Professional_Profile_Audit_Workbook.xlsx'))
print('saved audit')

# Positioning Workbook DOCX
from docx import Document
from docx.shared import Pt, Inches, RGBColor
doc=Document()
st=doc.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(10.5)
for s in doc.sections: s.top_margin=Inches(0.7); s.bottom_margin=Inches(0.7); s.left_margin=Inches(0.8); s.right_margin=Inches(0.8)
def h1(t): p=doc.add_paragraph(); r=p.add_run(t); r.bold=True; r.font.size=Pt(18); r.font.color.rgb=RGBColor(0x1F,0x38,0x64)
def para(t): p=doc.add_paragraph(); r=p.add_run(t); r.font.size=Pt(10.5)
h1('Professional Positioning Workbook')
for f in ['Current professional identity','Target role','Target industry','Relevant strengths','Demonstrable skills','Measurable achievements','Preferred work','Relevant projects','Career direction','Differentiating experience','Evidence supporting claims']:
    para(f'{f}: ________________________________________________________________')
para('Concise positioning statement: ________________________________________________')
doc.save(os.path.join(OUT,'Professional_Positioning_Workbook.docx'))
print('saved positioning')

# Networking Tracker XLSX
wb2=Workbook(); ws=wb2.active; ws.title='Tracker'
ws['A1']='Professional Networking Tracker'; ws['A1'].font=Font(bold=True,size=14,color=NAVY)
headers=['Contact Name','Company','Designation','Platform','Connection Date','Reason for Connecting','Message Sent','Response Status','Follow-up Date','Last Interaction','Next Action','Notes']
row=3
for i,h in enumerate(headers,1):
    c=ws.cell(row=row,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor=NAVY); c.border=border; c.alignment=Alignment(horizontal='center',wrap_text=True)
ws.row_dimensions[row].height=30
row+=1; start=row
for i in range(20):
    for j in range(12): ws.cell(row=row,column=j+1).border=border
    row+=1
end=row-1
dv=DataValidation(type='list',formula1='"Connected,Pending,No Response,Replied"',allow_blank=True); ws.add_data_validation(dv); dv.add(f'H{start}:H{end}')
# dashboard
ws2=wb2.create_sheet('Dashboard')
ws2['A1']='Networking Dashboard'; ws2['A1'].font=Font(bold=True,size=14,color=NAVY)
labels=['Total Contacts','Messages Sent','Responses Received','Follow-ups Due','Active Conversations']
for i,l in enumerate(labels,3):
    ws2.cell(row=i,column=1,value=l).font=Font(bold=True)
    ws2.cell(row=i,column=2,value=f'=COUNTA(Tracker!A{start}:A{end})' if i==3 else 0)
widths=[16,14,18,12,14,14,14,16,14,16,16,24]
for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
wb2.save(os.path.join(OUT,'..','05_Networking','Professional_Networking_Tracker.xlsx'))
print('saved tracker')
print('ALL DONE')
