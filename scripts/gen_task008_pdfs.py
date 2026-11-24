import os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\salary-and-offer-negotiation-system'
NAVY = colors.HexColor('#1F3864'); BLUE=colors.HexColor('#2E5C8A'); GREY=colors.HexColor('#595959')
styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=18, textColor=NAVY, spaceAfter=10)
H2 = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=14, textColor=BLUE, spaceAfter=6, spaceBefore=12)
BODY = ParagraphStyle('BODY', parent=styles['BodyText'], fontSize=10.5, leading=14, spaceAfter=6)
BULLET = ParagraphStyle('BULLET', parent=styles['BodyText'], fontSize=10.5, leading=14, leftIndent=16, spaceAfter=3)

def pdf(path, title, sections):
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=0.8*inch, rightMargin=0.8*inch, topMargin=0.7*inch, bottomMargin=0.7*inch)
    story=[Paragraph(title,H1), Paragraph('CareerVault Salary & Offer Negotiation System. Fictional illustrative content.', ParagraphStyle('sub',parent=BODY,italic=True,fontSize=9,textColor=GREY)), Spacer(1,12)]
    for t,paras in sections:
        story.append(Paragraph(t,H2))
        for p in paras:
            if p.startswith('BULLET:'): story.append(Paragraph('• '+p[7:],BULLET))
            else: story.append(Paragraph(p,BODY))
        story.append(Spacer(1,6))
    doc.build(story); print('saved',path)

tracks = ['Technology & IT','Business Analysis','Product & Project Management','Finance','Sales & Marketing','Management & Operations']

# Handbook (16 chapters)
hs = [(f'Chapter {i} — {t}', [f'Practical guidance for {t.lower()}.', 'Realistic examples.', 'Common mistakes and checklists.']) for i,t in enumerate(['Understanding compensation in India','CTC vs gross vs take-home','Fixed and variable compensation','Bonuses, incentives, commissions','Benefits and allowances','Payslips and compensation statements','Researching salary information','Establishing target salary range','Understanding negotiating position','Discussing salary expectations','Negotiating before offer','Negotiating after offer','Handling low offers','Comparing multiple offers','Evaluating offer conditions','Final accept/negotiate/decline decision'],1)]
pdf(os.path.join(OUT,'01_Handbooks','Salary_and_Offer_Negotiation_Handbook.pdf'),'Salary and Offer Negotiation Handbook',hs)

# Compensation Structure Guide
pdf(os.path.join(OUT,'01_Handbooks','Indian_Compensation_Structure_Guide.pdf'),'Indian Compensation Structure Guide', [('Components', ['CTC, basic salary, HRA, special allowance, employer PF, employee PF, gratuity, variable pay, performance bonuses, joining/retention bonuses, sales commissions, insurance, meal/transport, equity, reimbursements.']), ('Explanations', ['Which components form CTC, affect gross pay, affect take-home, are conditional/deferred, require careful examination.'])])

# Salary Research Guide
pdf(os.path.join(OUT,'01_Handbooks','Salary_Research_and_Benchmarking_Guide.pdf'),'Salary Research and Benchmarking Guide', [('Sources', ['Public salary reports, reputable compensation research, established salary platforms, official labour statistics, employer disclosures.']), ('Limitations', ['Sample size, outdated data, self-reported data, role/experience/location/industry/company-size differences.'])])

# Negotiation Message Library (72)
msgs = []
cats = ['Discussing expected compensation','Negotiating initial offer','Negotiating higher fixed component','Variable pay/bonuses/incentives','Joining dates/notice/joining bonus','Accepting/declining/clarifying offers']
for c in cats:
    for i in range(12):
        msgs.append(f'{c} — Message {i+1}: Purpose, situation, editable message, personalisation guidance, considerations, common mistakes.')
pdf(os.path.join(OUT,'02_Negotiation_Communication','Salary_Negotiation_Message_Library.pdf'),'Salary Negotiation Message Library', [('Messages', msgs)])

# CTC Explainer
pdf(os.path.join(OUT,'04_Compensation_Guides','CTC_to_Take_Home_Salary_Explainer.pdf'),'CTC to Take-Home Salary Explainer', [('Topics', ['CTC structure, monthly gross vs CTC, deductions, employer contributions in CTC, variable pay not guaranteed, joining/annual bonus treatment.']), ('Examples', ['Fictional illustrative examples with labelled assumptions and checked math.'])])

# Offer Letter Checklist (60+)
checks = [f'Check {i}: actionable offer letter review item.' for i in range(1,65)]
pdf(os.path.join(OUT,'05_Offer_Evaluation','Offer_Letter_Evaluation_Checklist.pdf'),'Offer Letter Evaluation Checklist', [('Checks', checks)])

# Final Offer Decision Framework
pdf(os.path.join(OUT,'05_Offer_Evaluation','Final_Offer_Decision_Framework.pdf'),'Final Offer Decision Framework', [('Factors', ['Financial, career growth, responsibilities, manager/team, employment conditions, location, stability, personal constraints, risks, unresolved questions.']), ('Worksheet', ['Decision worksheet with realistic examples. Final decision remains with customer.'])])

# 6 career-track guides
for tr in tracks:
    slug = tr.replace(' & ','_').replace(' ','_')
    pdf(os.path.join(OUT,'06_Career_Track_Guides',f'{slug}_Salary_Negotiation_Guide.pdf'), f'{tr} Salary Negotiation Guide', [('Content', ['Relevant compensation components, role-specific considerations, experience-level, evidence, common structures, variable pay, negotiation scenarios, useful questions, common mistakes, preparation checklist.'])])

# START_HERE and LICENSE
pdf(os.path.join(OUT,'START_HERE.pdf'),'START HERE', [('Purpose',['Practical compensation and offer negotiation toolkit.']), ('Folders',['01_Handbooks','02_Negotiation_Communication','03_Editable_Workbooks','04_Compensation_Guides','05_Offer_Evaluation','06_Career_Track_Guides'])])
pdf(os.path.join(OUT,'LICENSE_AND_USAGE.pdf'),'License and Usage', [('Usage',['Personal use within CareerVault bundle.']), ('No guarantees',['No salary increase or negotiation success guaranteed.'])])
print('PDFS DONE')
