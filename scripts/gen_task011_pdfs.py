import os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\career-advancement-toolkit'
NAVY = colors.HexColor('#1F3864'); BLUE=colors.HexColor('#2E5C8A'); GREY=colors.HexColor('#595959')
styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=18, textColor=NAVY, spaceAfter=10)
H2 = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=14, textColor=BLUE, spaceAfter=6, spaceBefore=12)
BODY = ParagraphStyle('BODY', parent=styles['BodyText'], fontSize=10.5, leading=14, spaceAfter=6)
BULLET = ParagraphStyle('BULLET', parent=styles['BodyText'], fontSize=10.5, leading=14, leftIndent=16, spaceAfter=3)

def pdf(path, title, sections):
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=0.8*inch, rightMargin=0.8*inch, topMargin=0.7*inch, bottomMargin=0.7*inch)
    story=[Paragraph(title,H1), Paragraph('CareerVault Career Advancement Toolkit. Fictional illustrative content.', ParagraphStyle('sub',parent=BODY,italic=True,fontSize=9,textColor=GREY)), Spacer(1,12)]
    for t,paras in sections:
        story.append(Paragraph(t,H2))
        for p in paras:
            if p.startswith('BULLET:'): story.append(Paragraph('• '+p[7:],BULLET))
            else: story.append(Paragraph(p,BODY))
        story.append(Spacer(1,6))
    doc.build(story); print('saved',path)

tracks = ['Technology & IT','Business Analysis','Product & Project Management','Finance','Sales & Marketing','Management & Operations']

# Handbook (18 chapters)
hs = [(f'Chapter {i} — {t}', [f'Practical guidance for {t.lower()}.', 'Indian workplace examples.', 'Common mistakes, exercises, linked worksheets.']) for i,t in enumerate(['Understanding Career Advancement','Building Long-Term Career Vision','Choosing Career Growth Path','Current Professional Value','Setting Career Objectives','Improving Workplace Performance','Building Evidence of Impact','Promotion Readiness','Promotion Conversations','Leadership Capabilities','IC to Manager Transition','Communication and Influence','Stakeholder Relationships','High-Value Skills','Internal Mobility','Professional Reputation','Career Setbacks and Stagnation','12-Month Advancement Plan'],1)]
pdf(os.path.join(OUT,'Career_Advancement_Handbook.pdf'),'Career Advancement Handbook',hs)

# First-Time Manager Toolkit
pdf(os.path.join(OUT,'leadership','First_Time_Manager_Toolkit.pdf'),'First-Time Manager Toolkit', [('Topics', ['IC to manager transition, new responsibilities, team expectations, delegation, 1:1s, feedback, performance management, conflict, meetings, trust, team development, managing upward, common mistakes.']), ('Checklist', ['30-day manager transition checklist.'])])

# Internal Mobility Guide
pdf(os.path.join(OUT,'skills-and-mobility','Internal_Mobility_Strategy_Guide.pdf'),'Internal Mobility Strategy Guide', [('Topics', ['Internal opportunities, adjacent teams, transferable skills, internal relationships, communicating career interests, internal applications, internal interviews, lateral moves, transition planning.']), ('Templates', ['Practical message templates and decision frameworks.'])])

# Reputation Checklist
pdf(os.path.join(OUT,'professional-brand','Professional_Reputation_Checklist.pdf'),'Professional Reputation Checklist', [('Checks', [f'Check {i}: actionable reputation review item.' for i in range(1,41)])])

# Career Stagnation Playbook
pdf(os.path.join(OUT,'career-recovery','Career_Stagnation_and_Recovery_Playbook.pdf'),'Career Stagnation and Recovery Playbook', [('Topics', ['Feeling stuck, lack of learning, limited manager support, delayed promotion, skill obsolescence, loss of motivation, role mismatch, lack of visibility, internal mobility, external switch.']), ('Process', ['Structured decision process and recovery plans. No medical advice.'])])

# 6 career-track guides
for tr in tracks:
    slug = tr.replace(' & ','_').replace(' ','_')
    pdf(os.path.join(OUT,'career-track-guides',f'{slug}_Career_Advancement_Guide.pdf'), f'{tr} Career Advancement Guide', [('Content', ['Career progression possibilities, specialist/management pathways, skills for progression, demonstrating impact, portfolio examples, leadership expectations, stakeholder management, promotion prep, professional development, internal mobility, 12-month growth plan.'])])

# START_HERE and LICENSE
pdf(os.path.join(OUT,'START_HERE.pdf'),'START HERE', [('Purpose',['Practical career advancement and growth toolkit.']), ('Folders',['career-planning','performance-and-promotion','leadership','skills-and-mobility','professional-brand','career-recovery','career-track-guides'])])
pdf(os.path.join(OUT,'licence','PERSONAL_USE_LICENCE.pdf'),'Personal Use Licence', [('Usage',['Personal use within CareerVault bundle.']), ('No guarantees',['No promotions or salary increases guaranteed.'])])
print('PDFS DONE')
