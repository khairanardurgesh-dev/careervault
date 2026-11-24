import os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\resume-mastery-system\03_Workbooks'
NAVY = '1F3864'; BLUE='2E5C8A'; GREY='F2F2F2'
thin = Side(style='thin', color='BFBFBF')
border = Border(left=thin,right=thin,top=thin,bottom=thin)

# ---- Job Description Matching Worksheet ----
wb = Workbook()
ws = wb.active
ws.title = 'Job Match'
ws['A1'] = 'Job Description to Resume Matching Worksheet'
ws['A1'].font = Font(bold=True, size=14, color=NAVY)
ws['A2'] = 'CareerVault Resume Mastery System — Manual assessment tool. Not an ATS ranking algorithm.'
ws['A2'].font = Font(italic=True, size=9, color='595959')
ws.merge_cells('A1:F1'); ws.merge_cells('A2:F2')

row = 4
ws.cell(row=row, column=1, value='Target Job Title').font = Font(bold=True)
ws.cell(row=row, column=2, value='').fill = PatternFill('solid', fgColor=GREY)
ws.cell(row=row, column=2).border = border
row += 2
headers = ['Requirement (from JD)', 'Type', 'Your Evidence', 'Match (1-5)', 'Resume Section to Update', 'Action']
for i,h in enumerate(headers, start=1):
    c = ws.cell(row=row, column=i, value=h)
    c.font = Font(bold=True, color='FFFFFF'); c.fill = PatternFill('solid', fgColor=NAVY); c.border = border
    c.alignment = Alignment(horizontal='center', wrap_text=True)
ws.row_dimensions[row].height = 30
row += 1
start = row
for i in range(15):
    for j in range(6):
        c = ws.cell(row=row, column=j+1)
        c.border = border
        if j == 3:
            c.alignment = Alignment(horizontal='center')
    row += 1
end = row-1
# data validation for match 1-5
from openpyxl.worksheet.datavalidation import DataValidation
dv = DataValidation(type='list', formula1='"1,2,3,4,5"', allow_blank=True)
ws.add_data_validation(dv)
dv.add(f'D{start}:D{end}')
# summary
row += 1
ws.cell(row=row, column=1, value='Overall Match Score (average of Match column):').font = Font(bold=True)
ws.cell(row=row, column=2, value=f'=IFERROR(AVERAGE(D{start}:D{end}),"")').font = Font(bold=True)
ws.cell(row=row, column=2).number_format = '0.00'
row += 1
ws.cell(row=row, column=1, value='Interpretation: 1=Poor, 2=Weak, 3=Partial, 4=Good, 5=Strong match. Manual assessment only — not an ATS score.')
ws.cell(row=row, column=1).font = Font(italic=True, size=9, color='595959')
ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=6)

# second sheet: instructions
ws2 = wb.create_sheet('Instructions')
ws2['A1'] = 'How to Use'
ws2['A1'].font = Font(bold=True, size=14, color=NAVY)
instr = [
 '1. Enter the target job title in the Job Match sheet.',
 '2. List each requirement from the job description in column A.',
 '3. Mark Type as Required or Preferred.',
 '4. Add your evidence (experience, project, skill) in column C.',
 '5. Score match 1-5 in column D.',
 '6. Note which resume section to update in column E.',
 '7. Write the customisation action in column F.',
 '8. Review the overall match score and prioritise gaps.',
 '',
 'This is a transparent manual assessment tool. It does not reproduce an actual ATS ranking algorithm and does not generate ATS scores.',
]
for i,t in enumerate(instr, start=3):
    ws2.cell(row=i, column=1, value=t)
widths = [40,12,40,10,22,40]
for i,w in enumerate(widths, start=1):
    ws.column_dimensions[get_column_letter(i)].width = w
wb.save(os.path.join(OUT, 'Job_Description_Resume_Matching_Worksheet.xlsx'))
print('saved matching')

# ---- Resume Quality Scorecard ----
wb2 = Workbook()
ws = wb2.active
ws.title = 'Scorecard'
ws['A1'] = 'Resume Quality Scorecard'
ws['A1'].font = Font(bold=True, size=14, color=NAVY)
ws['A2'] = 'CareerVault Resume Mastery System — Manual assessment. Score does not predict hiring success or ATS performance.'
ws['A2'].font = Font(italic=True, size=9, color='595959')
ws.merge_cells('A1:D1'); ws.merge_cells('A2:D2')

criteria = [
 ('Role Relevance', 0.15),
 ('Clarity', 0.12),
 ('Achievement Quality', 0.15),
 ('Experience Presentation', 0.13),
 ('Skills Relevance', 0.12),
 ('Structure', 0.10),
 ('Readability', 0.08),
 ('Accuracy', 0.08),
 ('Formatting Consistency', 0.07),
]
row = 4
for i,h in enumerate(['Criterion','Weight','Score (1-5)','Weighted Score'], start=1):
    c = ws.cell(row=row, column=i, value=h)
    c.font = Font(bold=True, color='FFFFFF'); c.fill = PatternFill('solid', fgColor=NAVY); c.border = border
    c.alignment = Alignment(horizontal='center')
row += 1
start = row
for name, w in criteria:
    ws.cell(row=row, column=1, value=name).border = border
    ws.cell(row=row, column=2, value=w).number_format = '0%'
    ws.cell(row=row, column=2).border = border
    ws.cell(row=row, column=3, value=3).border = border
    ws.cell(row=row, column=3).alignment = Alignment(horizontal='center')
    ws.cell(row=row, column=4, value=f'=B{row}*C{row}').border = border
    ws.cell(row=row, column=4).number_format = '0.00'
    row += 1
end = row-1
row += 1
ws.cell(row=row, column=1, value='Total Weighted Score').font = Font(bold=True)
ws.cell(row=row, column=4, value=f'=SUM(D{start}:D{end})').font = Font(bold=True)
ws.cell(row=row, column=4).number_format = '0.00'
total_row = row
row += 2
ws.cell(row=row, column=1, value='Interpretation:').font = Font(bold=True)
row += 1
for t in ['0.00 - 0.40: Needs significant improvement','0.41 - 0.60: Fair, with clear gaps','0.61 - 0.80: Good, minor improvements','0.81 - 1.00: Strong, ready to submit']:
    ws.cell(row=row, column=1, value=t).font = Font(size=9)
    row += 1
row += 1
ws.cell(row=row, column=1, value='Recommendations:').font = Font(bold=True)
row += 1
ws.cell(row=row, column=1, value='Review criteria scoring 1-2 first. Rewrite achievement bullets, align skills to JD, and verify formatting consistency.').font = Font(size=9, italic=True)
for col,w in zip('ABCD',[32,10,12,16]):
    ws.column_dimensions[col].width = w
# data validation for score 1-5
dv = DataValidation(type='list', formula1='"1,2,3,4,5"', allow_blank=True)
ws.add_data_validation(dv)
dv.add(f'C{start}:C{end}')
wb2.save(os.path.join(OUT, 'Resume_Quality_Scorecard.xlsx'))
print('saved scorecard')
