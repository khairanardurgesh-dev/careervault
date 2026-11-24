#!/usr/bin/env python3
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.utils import get_column_letter

# ============================================================
# Job Application Tracker XLSX
# ============================================================
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Application Tracker"

# Styles
header_font = Font(name='Calibri', bold=True, size=11, color='FFFFFF')
header_fill = PatternFill(start_color='1F2B3D', end_color='1F2B3D', fill_type="solid")
accent_fill = PatternFill(start_color='3A5A7C', end_color='3A5A7C', fill_type="solid")
light_fill = PatternFill(start_color='D6E4F0', end_color='D6E4F0', fill_type="solid")
normal_font = Font(name='Calibri', size=11)
thin_border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

# Colors
green_fill = PatternFill(start_color='C6EFCE', end_color='C6EFCE', fill_type="solid")
blue_fill = PatternFill(start_color='DAEEF3', end_color='DAEEF3', fill_type="solid")

# Headers
headers = [
    "Company",
    "Job Title",
    "Job Link",
    "Application Date",
    "Application Source",
    "Status",
    "Recruiter Contact",
    "Next Follow-Up Date",
    "Interview Date",
    "Notes"
]

# Set column widths
for i, width in enumerate(col_widths := [25, 30, 40, 16, 25, 16, 22, 18, 16, 30], 1):
    ws.column_dimensions[get_column_letter(i)].width = width

# Write headers
for col_idx, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col_idx, value=header)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    cell.border = thin_border

# Write sample data rows
sample_data = [
    {
        "company": "Infosys",
        "jobTitle": "Junior Software Engineer",
        "jobLink": "https://www.infosys.com/careers",
        "appDate": "2026-11-01",
        "appSource": "Company Website",
        "status": "Applied",
        "recruiterContact": "hr@infosys.com",
        "nextFollowUp": "2026-11-15",
        "interviewDate": "",
        "notes": "Applied through careers portal"
    },
    {
        "company": "Wipro",
        "jobTitle": "Business Analyst",
        "jobLink": "https://www.wipro.com/careers",
        "appDate": "2026-10-28",
        "appSource": "Naukri.com",
        "status": "Follow-up Sent",
        "recruiterContact": "nil",
        "nextFollowUp": "2026-12-05",
        "interviewDate": "",
        "notes": "Referred by current employee"
    },
    {
        "company": "TCS",
        "jobTitle": "System Engineer",
        "jobLink": "https://www.tcs.com/careers",
        "appDate": "2026-11-10",
        "appSource": "LinkedIn",
        "status": "Shortlisted",
        "recruiterContact": "talent@tcs.com",
        "nextFollowUp": "2026-11-25",
        "interviewDate": "2026-11-28",
        "notes": "Called for technical round"
    }
]

for row_idx, data in enumerate(sample_data, 2):
    for col_idx, header in enumerate(headers, 1):
        value = data.get(header.lower().replace(" ", ""), "")
        cell = ws.cell(row=row_idx, column=col_idx, value=value)
        cell.font = normal_font
        cell.border = thin_border
        cell.alignment = Alignment(vertical='center', wrap_text=True)
        # Colour code status
        if col_idx == 6 and value:
            if value == "Shortlisted":
                cell.fill = green_fill
            elif value == "Applied":
                cell.fill = blue_fill

# Add instructions sheet
ws_instructions = wb.create_sheet("Instructions")
ws_instructions.column_dimensions['A'].width = 100

instructions = [
    "CAREERVAULT - Job Application Tracker",
    "",
    "How to use this workbook:",
    "",
    "1. ENTER new applications in the 'Application Tracker' sheet.",
    "2. Fill in all fields for each new job application.",
    "3. Update the 'Status' column as you progress (Applied, Shortlisted, Interview, Offer, Rejected).",
    "4. Fill in the 'Next Follow-Up Date' to track when to contact the recruiter again.",
    "5. Record the 'Interview Date' once scheduled.",
    "6. Use the 'Notes' column for any important details about the application.",
    "",
    "Status Colors:",
    "  Green: Shortlisted",
    "  Blue: Applied",
    "",
    "Key Fields:",
    "  - Company: Name of the company you applied to",
    "  - Job Title: Exact title of the position",
    "  - Job Link: URL to the job posting",
    "  - Application Date: Date you submitted the application",
    "  - Application Source: Where you found the job (Company Website, LinkedIn, Naukri, Referral, etc.)",
    "  - Status: Current application status",
    "  - Recruiter Contact: Email or name of your recruiter contact",
    "  - Next Follow-Up Date: When you should follow up next",
    "  - Interview Date: Scheduled interview date",
    "  - Notes: Any additional observations or action items",
    "",
    "Tips:",
    "  - Update this tracker weekly to stay on top of your job search",
    "  - Set calendar reminders for follow-up dates",
    "  - Keep a separate document for interview preparation notes",
    "  - Track which applications result in interviews and offers",
    "",
    "Generated by CareerVault Complete Job Switch System",
    "(Pilot Resource - PILOT - NOT FINAL COMMERCIAL RELEASE)"
]

for i, line in enumerate(instructions):
    ws_instructions.cell(row=i+1, column=1, value=line)
    if i > 3:
        ws_instructions.cell(row=i+1, column=1).font = normal_font
    else:
        ws_instructions.cell(row=i+1, column=1).font = Font(name='Calibri', size=11, bold=True, color='1A1A1A')

# Save workbook
wb.save("output/job-application-tracker.xlsx")
print("Job Application Tracker saved successfully.")

# ============================================================
# Salary/Offer Comparison Calculator XLSX
# ============================================================
wb2 = openpyxl.Workbook()
ws2 = wb2.active
ws2.title = "Offer Comparison"

# Styles
header2_font = Font(name='Calibri', bold=True, size=11, color='FFFFFF')
header2_fill = PatternFill(start_color='1F2B3D', end_color='1F2B3D', fill_type="solid")
section_fill = PatternFill(start_color='2C3E50', end_color='2C3E50', fill_type="solid")
section_font = Font(name='Calibri', bold=True, size=11, color='ECF0F1')
normal_font2 = Font(name='Calibri', size=11)
money_format = '#,##0.00'
thin_border2 = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

# Section 1: Offer 1
row = 1
cell_hdr = ws2.cell(row=row, column=1, value="OFFER 1")
cell_hdr.font = section_font
cell_hdr.fill = section_fill
ws2.merge_cells('A1:B1')

row = 2

offer1_fields = [
    ("Annual Fixed Pay (CTC)", 0, True),
    ("Joining Bonus", 0, False),
    ("Annual Bonus (Target)", 0, False),
    ("Variable Pay (Target %)", 0, False),
    ("Benefits (Monthly Estimate)", 0, False)
]

for field_name, default, is_mandatory in offer1_fields:
    ws2.cell(row=row, column=1, value=field_name).font = normal_font2
    ws2.cell(row=row, column=1).border = thin_border2
    cell = ws2.cell(row=row, column=2, value=default)
    cell.font = normal_font2
    cell.border = thin_border2
    cell.number_format = money_format
    row += 1

row += 1  # blank row

# Section 2: Offer 2
ws2.cell(row=row, column=1, value="OFFER 2").font = section_font
ws2.cell(row=row, column=1).fill = section_fill
ws2.merge_cells('A' + str(row) + ':B' + str(row))
row += 2

offer2_fields = [
    ("Annual Fixed Pay (CTC)", 0, True),
    ("Joining Bonus", 0, False),
    ("Annual Bonus (Target)", 0, False),
    ("Variable Pay (Target %)", 0, False),
    ("Benefits (Monthly Estimate)", 0, False)
]

for field_name, default, is_mandatory in offer2_fields:
    ws2.cell(row=row, column=1, value=field_name).font = normal_font2
    ws2.cell(row=row, column=1).border = thin_border2
    cell = ws2.cell(row=row, column=2, value=default)
    cell.font = normal_font2
    cell.border = thin_border2
    cell.number_format = money_format
    row += 1

row += 1  # blank row

# Section 3: Calculations
ws2.cell(row=row, column=1, value="CALCULATIONS").font = section_font
ws2.cell(row=row, column=1).fill = section_fill
ws2.merge_cells('A' + str(row) + ':B' + str(row))
row += 2

calc_fields = [
    ("Annual Fixed Pay Difference", "=B2-B8", True),
    ("Joining Bonus Difference", "==B3-B9", True),
    ("Annual Bonus Difference", "=B4-B10", True),
    ("Estimated Variable Pay Difference", "=B5-B11", True),
    ("Total CTC Difference", "=B12-B16", True),
    ("Estimated Monthly Gross (Offer 1)", "=B2/12", True),
    ("Estimated Monthly Gross (Offer 2)", "=B8/12", True),
    ("Estimated Monthly Take-Home (Offer 1)", "=B14*(1-0.3)", True),
    ("Estimated Monthly Take-Home (Offer 2)", "=B15*(1-0.3)", True)
]

for field_name, formula, is_mandatory in calc_fields:
    ws2.cell(row=row, column=1, value=field_name).font = normal_font2
    ws2.cell(row=row, column=1).border = thin_border2
    cell = ws2.cell(row=row, column=2, value=formula)
    cell.font = Font(name='Calibri', bold=True, size=11, color='2C3E50')
    cell.border = thin_border2
    cell.number_format = money_format
    row += 1

row += 1

# Assumptions
ws2.cell(row=row, column=1, value="ASSUMPTIONS").font = section_font
ws2.cell(row=row, column=1).fill = section_fill
ws2.merge_cells('A' + str(row) + ':B' + str(row))
row += 2

assumptions = [
    "Tax rate: 30% (estimate only - varies by income slab and regime)",
    "Benefits include: health insurance, company contributions, etc.",
    "Variable pay at target percentage of fixed CTC",
    "All amounts in INR",
    "Monthly take-home is gross minus estimated tax deductions",
    "Consult a tax professional for official calculations"
]

for i, assumption in enumerate(assumptions):
    ws2.cell(row=row+i, column=1, value=assumption).font = normal_font2
    ws2.cell(row=row+i, column=1).border = thin_border2
    ws2.cell(row=row+i, column=1).alignment = Alignment(wrap_text=True)

# Set column widths
ws2.column_dimensions['A'].width = 40
ws2.column_dimensions['B'].width = 25

# Save workbook
wb2.save("output/salary-offer-calculator.xlsx")
print("Salary Offer Comparison Calculator saved successfully.")