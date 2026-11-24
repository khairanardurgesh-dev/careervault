import os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\professional-profile-optimisation-system'
NAVY = colors.HexColor('#1F3864'); BLUE=colors.HexColor('#2E5C8A'); GREY=colors.HexColor('#595959')
styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=18, textColor=NAVY, spaceAfter=10)
H2 = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=14, textColor=BLUE, spaceAfter=6, spaceBefore=12)
BODY = ParagraphStyle('BODY', parent=styles['BodyText'], fontSize=10.5, leading=14, spaceAfter=6)
BULLET = ParagraphStyle('BULLET', parent=styles['BodyText'], fontSize=10.5, leading=14, leftIndent=16, spaceAfter=3)

def pdf(path, title, sections):
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=0.8*inch, rightMargin=0.8*inch, topMargin=0.7*inch, bottomMargin=0.7*inch)
    story=[Paragraph(title,H1), Paragraph('CareerVault Professional Profile Optimisation System. Fictional illustrative content.', ParagraphStyle('sub',parent=BODY,italic=True,fontSize=9,textColor=GREY)), Spacer(1,12)]
    for t,paras in sections:
        story.append(Paragraph(t,H2))
        for p in paras:
            if p.startswith('BULLET:'): story.append(Paragraph('• '+p[7:],BULLET))
            else: story.append(Paragraph(p,BODY))
        story.append(Spacer(1,6))
    doc.build(story); print('saved',path)

tracks = ['Technology & IT','Business Analysis','Product & Project Management','Finance','Sales & Marketing','Management & Operations']

# Handbook
hs = []
for i,t in enumerate(['Professional branding fundamentals','How recruiters evaluate profiles','Career positioning strategy','LinkedIn profile structure','Writing headlines','Writing About sections','Experience and achievements','Skills, endorsements, certifications','Featured section and portfolio','Professional activity and credibility','Networking and recruiter communication','Profile audit and maintenance'],1):
    hs.append((f'Chapter {i} — {t}', [f'Practical guidance for {t.lower()}.', 'Good and bad examples included.', 'Common mistakes and exercises.']))
pdf(os.path.join(OUT,'01_Handbooks','Professional_Profile_Optimisation_Handbook.pdf'),'Professional Profile Optimisation Handbook',hs)

# Headline Library (72 examples)
heads = []
for tr in tracks:
    for i in range(12):
        heads.append(f'{tr} — Headline {i+1}: Target role example with clear positioning and relevant keywords (fictional, illustrative).')
pdf(os.path.join(OUT,'02_Profile_Libraries','LinkedIn_Headline_Library.pdf'),'LinkedIn Headline Library', [('Headline Examples', heads), ('Adaptation', ['Replace placeholders with truthful information.', 'Avoid keyword stuffing and inflated titles.'])])

# About Section Library (36 examples)
abouts = []
for tr in tracks:
    for i in range(6):
        abouts.append(f'{tr} — About example {i+1}: Fictional candidate profile with complete About section, structural breakdown and personalisation instructions.')
pdf(os.path.join(OUT,'02_Profile_Libraries','LinkedIn_About_Section_Library.pdf'),'LinkedIn About Section Library', [('About Examples', abouts)])

# Networking Message Library (60 messages)
msgs = []
cats = ['Recruiter outreach','Hiring manager','Referral request','Connection request','Follow-up','Professional networking']
for c in cats:
    for i in range(10):
        msgs.append(f'{c} — Message {i+1}: Purpose, situation, editable template, personalisation instructions, what not to say.')
pdf(os.path.join(OUT,'05_Networking','Professional_Networking_Message_Library.pdf'),'Professional Networking Message Library', [('Messages', msgs)])

# Content toolkit (30 frameworks)
fw = []
for tr in tracks:
    for i in range(5):
        fw.append(f'{tr} — Framework {i+1}: Purpose, structure, example, adaptation instructions.')
pdf(os.path.join(OUT,'06_Content_Toolkit','LinkedIn_Content_and_Credibility_Toolkit.pdf'),'LinkedIn Content and Credibility Toolkit', [('Frameworks', fw)])

# 30-day plan
plan = []
for w in range(1,5):
    plan.append((f'Week {w}', [f'Daily tasks for week {w}.', 'Estimated effort and completion checkboxes.', 'Weekly review questions.']))
pdf(os.path.join(OUT,'07_Action_Plan','30_Day_Professional_Profile_Improvement_Plan.pdf'),'30-Day Professional Profile Improvement Plan', plan)

# Checklist (50+)
checks = [f'Check {i}: actionable profile review item.' for i in range(1,55)]
pdf(os.path.join(OUT,'08_Checklists','Professional_Profile_Review_Checklist.pdf'),'Professional Profile Review Checklist', [('Checks', checks)])

# START_HERE and LICENSE
pdf(os.path.join(OUT,'START_HERE.pdf'),'START HERE', [('Purpose',['Self-guided profile optimisation toolkit.']), ('Folders',['01_Handbooks','02_Profile_Libraries','03_Editable_Templates','04_Workbooks','05_Networking','06_Content_Toolkit','07_Action_Plan','08_Checklists'])])
pdf(os.path.join(OUT,'LICENSE_AND_USAGE.pdf'),'License and Usage', [('Usage',['Personal use within CareerVault bundle.']), ('No guarantees',['No recruiter visibility or job outcome guaranteed.'])])
print('PDFS DONE')
