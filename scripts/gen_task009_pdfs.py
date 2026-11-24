import os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\ai-career-assistant-toolkit'
NAVY = colors.HexColor('#1F3864'); BLUE=colors.HexColor('#2E5C8A'); GREY=colors.HexColor('#595959')
styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=18, textColor=NAVY, spaceAfter=10)
H2 = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=14, textColor=BLUE, spaceAfter=6, spaceBefore=12)
BODY = ParagraphStyle('BODY', parent=styles['BodyText'], fontSize=10.5, leading=14, spaceAfter=6)
BULLET = ParagraphStyle('BULLET', parent=styles['BodyText'], fontSize=10.5, leading=14, leftIndent=16, spaceAfter=3)

def pdf(path, title, sections):
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=0.8*inch, rightMargin=0.8*inch, topMargin=0.7*inch, bottomMargin=0.7*inch)
    story=[Paragraph(title,H1), Paragraph('CareerVault AI Career Assistant Toolkit. Fictional illustrative content.', ParagraphStyle('sub',parent=BODY,italic=True,fontSize=9,textColor=GREY)), Spacer(1,12)]
    for t,paras in sections:
        story.append(Paragraph(t,H2))
        for p in paras:
            if p.startswith('BULLET:'): story.append(Paragraph('• '+p[7:],BULLET))
            else: story.append(Paragraph(p,BODY))
        story.append(Spacer(1,6))
    doc.build(story); print('saved',path)

tracks = ['Technology & IT','Business Analysis','Product & Project Management','Finance','Sales & Marketing','Management & Operations']

# Handbook (16 chapters)
hs = [(f'Chapter {i} — {t}', [f'Practical guidance for {t.lower()}.', 'Example prompts.', 'Common mistakes and exercises.']) for i,t in enumerate(['Introduction to AI-assisted career development','How AI assistants work','Choosing an AI assistant','Writing effective prompts','Providing useful context','Improving and refining responses','AI for career planning','AI for resume improvement','AI for profile optimisation','AI for job-search research','AI for interview preparation','AI for recruiter communication','AI for salary negotiations','AI for skill development','Verifying AI-generated information','Repeatable AI-assisted workflow'],1)]
pdf(os.path.join(OUT,'01_Handbook','AI_Career_Assistant_Handbook.pdf'),'AI Career Assistant Handbook',hs)

# Master Prompt Library (120 prompts)
cats = ['Career discovery and positioning','Resume improvement','LinkedIn and professional branding','Job description and company analysis','Job search and application strategy','Interview preparation','Recruiter communication','Salary and offer negotiation','Skill-gap analysis and learning','Career growth and decision-making']
prompts = []
for c in cats:
    for i in range(12):
        prompts.append(f'{c} — Prompt {i+1}: Objective, use case, required inputs, copy-ready prompt, expected output, personalisation, verification, failure modes.')
pdf(os.path.join(OUT,'02_Master_Prompt_Library','Master_AI_Career_Prompt_Library.pdf'),'Master AI Career Prompt Library', [('Prompts', prompts)])

# 6 career-track prompt libraries (15 each)
for tr in tracks:
    slug = tr.replace(' & ','_').replace(' ','_')
    ps = [f'{tr} — Prompt {i+1}: career positioning, role analysis, resume, achievement writing, skill-gap, interview practice, domain prep, company research, recruiter communication, career development.' for i in range(15)]
    pdf(os.path.join(OUT,'03_Career_Track_Prompt_Libraries',f'{slug}_AI_Prompt_Library.pdf'), f'{tr} AI Prompt Library', [('Prompts', ps)])

# 6 AI toolkits
for name in ['AI_Resume_Improvement_Toolkit','AI_Interview_Preparation_Toolkit','AI_Job_Search_and_Research_Toolkit','AI_Professional_Communication_Toolkit','AI_Salary_and_Negotiation_Toolkit','AI_Career_Development_Toolkit']:
    pdf(os.path.join(OUT,'05_Career_Workflow_Toolkits',f'{name}.pdf'), name.replace('_',' '), [('Workflows', [f'Workflow {i+1}: objective, steps, prompts, expected output, human review checklist, failure modes.' for i in range(15)])])

# Fact-checking guide
pdf(os.path.join(OUT,'07_Quality_and_Safety','AI_Output_Quality_and_Fact_Checking_Guide.pdf'),'AI Output Quality and Fact-Checking Guide', [('Topics', ['Hallucinations, fabricated facts, incorrect calculations, outdated info, misleading summaries, missing context, unsupported claims, bias, inconsistency, false confidence.']), ('Exercises', [f'Verification exercise {i+1}.' for i in range(20)])])

# Privacy guide
pdf(os.path.join(OUT,'07_Quality_and_Safety','AI_Privacy_and_Safe_Usage_Guide.pdf'),'AI Privacy and Safe Usage Guide', [('Topics', ['Personal info, phone, email, address, government IDs, bank details, payslips, offer letters, contracts, confidential employer info, proprietary code, client info, internal docs.']), ('Safe/Unsafe', ['Safe and unsafe example prompts.'])])

# Tool directory
pdf(os.path.join(OUT,'08_Tool_Directory','AI_Career_Tool_Selection_Directory.pdf'),'AI Career Tool Selection Directory', [('Tools', ['ChatGPT, Google Gemini, Claude, Microsoft Copilot, Perplexity and others: website, primary use, career workflows, availability, free/paid, limitations, privacy, suitability.'])])

# Quick reference
pdf(os.path.join(OUT,'09_Quick_Reference','AI_Career_Assistant_Quick_Reference.pdf'),'AI Career Assistant Quick Reference', [('Content', ['Reusable prompt framework, personalisation instructions, useful examples, verification checklist, privacy checklist, common mistakes, suggested module workflow.'])])

# START_HERE and LICENSE
pdf(os.path.join(OUT,'START_HERE.pdf'),'START HERE', [('Purpose',['Practical AI-assisted career toolkit.']), ('Folders',['01_Handbook','02_Master_Prompt_Library','03_Career_Track_Prompt_Libraries','04_Prompt_Engineering','05_Career_Workflow_Toolkits','06_Workflow_Playbooks','07_Quality_and_Safety','08_Tool_Directory','09_Quick_Reference'])])
pdf(os.path.join(OUT,'LICENSE_AND_USAGE.pdf'),'License and Usage', [('Usage',['Personal use within CareerVault bundle.']), ('No guarantees',['No job outcomes guaranteed.'])])
print('PDFS DONE')
