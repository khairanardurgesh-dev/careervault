import os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\job-search-operating-system'
NAVY = colors.HexColor('#1F3864'); BLUE=colors.HexColor('#2E5C8A'); GREY=colors.HexColor('#595959')
styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=18, textColor=NAVY, spaceAfter=10)
H2 = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=14, textColor=BLUE, spaceAfter=6, spaceBefore=12)
BODY = ParagraphStyle('BODY', parent=styles['BodyText'], fontSize=10.5, leading=14, spaceAfter=6)
BULLET = ParagraphStyle('BULLET', parent=styles['BodyText'], fontSize=10.5, leading=14, leftIndent=16, spaceAfter=3)

def pdf(path, title, sections):
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=0.8*inch, rightMargin=0.8*inch, topMargin=0.7*inch, bottomMargin=0.7*inch)
    story=[Paragraph(title,H1), Paragraph('CareerVault Job Search Operating System. Fictional illustrative content.', ParagraphStyle('sub',parent=BODY,italic=True,fontSize=9,textColor=GREY)), Spacer(1,12)]
    for t,paras in sections:
        story.append(Paragraph(t,H2))
        for p in paras:
            if p.startswith('BULLET:'): story.append(Paragraph('• '+p[7:],BULLET))
            else: story.append(Paragraph(p,BODY))
        story.append(Spacer(1,6))
    doc.build(story); print('saved',path)

tracks = ['Technology & IT','Business Analysis','Product & Project Management','Finance','Sales & Marketing','Management & Operations']

# Handbook (14 chapters)
hs = [(f'Chapter {i} — {t}', [f'Practical guidance for {t.lower()}.', 'Step-by-step implementation.', 'Common mistakes and checklists.']) for i,t in enumerate(['Understanding the Indian job market','Defining target role and direction','Identifying suitable companies','Building target-company list','Finding job opportunities','Evaluating job descriptions','Understanding requirements and eligibility','Prioritising opportunities','Customising applications','Managing application pipelines','Recruiter communication','Networking and referral strategy','Screening-call preparation','Measuring progress and improving search'],1)]
pdf(os.path.join(OUT,'01_Handbook','Job_Search_Operating_System_Handbook.pdf'),'Job Search Operating System Handbook',hs)

# Platform Directory
pdf(os.path.join(OUT,'02_Platform_Directory','Indian_Job_Search_Platform_Directory.pdf'),'Indian Job Search Platform Directory', [('Platforms', ['LinkedIn Jobs, Naukri, Indeed India, Foundit, Instahyre, Wellfound, Cutshort, Hirist, iimjobs, company career pages.', 'Each platform: purpose, relevant profiles, career tracks served, features, limitations, access, usage advice, last verified date.']), ('Direct Channels', ['Company career pages, referrals, professional communities, legitimate recruitment agencies.'])])

# JD Analysis Toolkit
pdf(os.path.join(OUT,'04_Job_Description_Analysis','Job_Description_Analysis_Toolkit.pdf'),'Job Description Analysis Toolkit', [('Framework', ['Job title, responsibilities, required/preferred skills, experience, education, tools, industry, location, salary, seniority, red flags, suitability.']), ('Worked Examples', [f'{tr} — worked example {i+1}.' for tr in tracks for i in range(2)])])

# Recruiter Communication Library (72 messages)
msgs = []
cats = ['Application-related','Recruiter outreach','Follow-up','Referral request','Interview coordination','Post-interview/status update']
for c in cats:
    for i in range(12):
        msgs.append(f'{c} — Message {i+1}: Purpose, situation, editable template, personalisation guidance, common mistakes.')
pdf(os.path.join(OUT,'07_Communication','Job_Search_Recruiter_Communication_Library.pdf'),'Job Search Recruiter Communication Library', [('Messages', msgs)])

# Scam Prevention
pdf(os.path.join(OUT,'09_Safety','Job_Search_Scam_Prevention_Guide.pdf'),'Job Search Scam Prevention Guide', [('Topics', ['Fake job offers, recruitment fee scams, fake interviews, impersonated recruiters, fraudulent websites, identity misuse, OTP/banking requests, suspicious assessment links, fake WFH offers, unofficial channels, misleading salary promises, suspicious contracts.']), ('Verification', ['Employer identity, official domains, recruiter identity, job ads, interview comms, written offers, money/sensitive info requests.', 'Government cybercrime reporting resources.'])])

# Screening Prep
qs = [f'{tr} — Screening question {i+1} with truthful response framework.' for tr in tracks for i in range(5)]
pdf(os.path.join(OUT,'10_Screening','Recruiter_Screening_Preparation_Guide.pdf'),'Recruiter Screening Preparation Guide', [('Topics', ['Tell me about yourself, current role, reason for switching, notice period, compensation, location, work arrangement, relevant experience, availability, career goals, questions to ask.']), ('Questions', qs)])

# 6 career-track guides
for tr in tracks:
    slug = tr.replace(' & ','_').replace(' ','_')
    pdf(os.path.join(OUT,'12_Career_Track_Guides',f'{slug}_Job_Search_Guide.pdf'), f'{tr} Job Search Guide', [('Content', ['Common job titles, experience levels, suitable channels, employer categories, skills to highlight, portfolio/evidence, search terms, JD evaluation, application customisation, networking, screening topics, common mistakes, sample weekly strategy.'])])

# START_HERE and LICENSE
pdf(os.path.join(OUT,'START_HERE.pdf'),'START HERE', [('Purpose',['Practical job-search implementation toolkit.']), ('Folders',['01_Handbook','02_Platform_Directory','03_Company_Research','04_Job_Description_Analysis','05_Application_Tracking','06_Strategy_Planning','07_Communication','08_Weekly_Planning','09_Safety','10_Screening','11_Performance_Review','12_Career_Track_Guides'])])
pdf(os.path.join(OUT,'LICENSE_AND_USAGE.pdf'),'License and Usage', [('Usage',['Personal use within CareerVault bundle.']), ('No guarantees',['No job offers, interviews, or responses guaranteed.'])])
print('PDFS DONE')
