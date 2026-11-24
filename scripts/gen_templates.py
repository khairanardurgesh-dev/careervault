import os, sys
sys.path.insert(0, r'C:\Users\Quick\Desktop\CareerVault')
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\resume-mastery-system\01_Resume_Templates'

NAVY = RGBColor(0x1F,0x38,0x64)
BLUE = RGBColor(0x2E,0x5C,0x8A)
GREY = RGBColor(0x59,0x59,0x59)

def base_doc():
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(10.5)
    st.paragraph_format.space_after = Pt(4)
    st.paragraph_format.line_spacing = 1.08
    for s in doc.sections:
        s.top_margin = Inches(0.7); s.bottom_margin = Inches(0.7)
        s.left_margin = Inches(0.8); s.right_margin = Inches(0.8)
    return doc

def title(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True; r.font.size = Pt(20); r.font.color.rgb = NAVY
    p.paragraph_format.space_after = Pt(2)
    return p

def subtitle(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.size = Pt(11); r.font.color.rgb = GREY
    p.paragraph_format.space_after = Pt(8)
    return p

def h2(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text.upper())
    r.bold = True; r.font.size = Pt(12); r.font.color.rgb = BLUE
    p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(4)
    return p

def para(doc, text, bold=False, italic=False, size=10.5, space=4):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = bold; r.italic = italic; r.font.size = Pt(size)
    p.paragraph_format.space_after = Pt(space)
    return p

def bullet(doc, text):
    p = doc.add_paragraph(style='List Bullet')
    r = p.add_run(text); r.font.size = Pt(10.5)
    p.paragraph_format.space_after = Pt(2)
    return p

def placeholder(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text); r.italic = True; r.font.color.rgb = GREY; r.font.size = Pt(9.5)
    p.paragraph_format.space_after = Pt(6)
    return p

def add_contact(doc):
    p = doc.add_paragraph()
    r = p.add_run('Your Name'); r.bold=True; r.font.size=Pt(20); r.font.color.rgb=NAVY
    p.paragraph_format.space_after=Pt(0)
    p = doc.add_paragraph()
    r = p.add_run('City, State, India  |  +91-XXXXXXXXXX  |  email@example.com  |  linkedin.com/in/yourprofile')
    r.font.size=Pt(9.5); r.font.color.rgb=GREY
    p.paragraph_format.space_after=Pt(8)

def add_summary(doc, text):
    h2(doc,'Professional Summary')
    para(doc, text)

def add_skills(doc):
    h2(doc,'Core Skills')
    para(doc,'Skill 1  •  Skill 2  •  Skill 3  •  Skill 4  •  Skill 5  •  Skill 6', size=10)

def add_experience(doc):
    h2(doc,'Professional Experience')
    p = doc.add_paragraph(); r = p.add_run('Job Title — Company Name, City'); r.bold=True; r.font.size=Pt(11)
    p.paragraph_format.space_after=Pt(0)
    p = doc.add_paragraph(); r = p.add_run('Month Year – Month Year'); r.italic=True; r.font.size=Pt(9.5); r.font.color.rgb=GREY
    p.paragraph_format.space_after=Pt(4)
    bullet(doc,'Describe a key responsibility or achievement here.')
    bullet(doc,'Describe a second contribution or outcome here.')
    bullet(doc,'Describe a third measurable or qualitative result here.')

def add_education(doc):
    h2(doc,'Education')
    p = doc.add_paragraph(); r = p.add_run('Degree — Institution, City'); r.bold=True; r.font.size=Pt(11)
    p.paragraph_format.space_after=Pt(0)
    p = doc.add_paragraph(); r = p.add_run('Year of Completion'); r.italic=True; r.font.size=Pt(9.5); r.font.color.rgb=GREY
    p.paragraph_format.space_after=Pt(4)

def add_projects(doc):
    h2(doc,'Projects')
    p = doc.add_paragraph(); r = p.add_run('Project Name'); r.bold=True; r.font.size=Pt(11)
    p.paragraph_format.space_after=Pt(0)
    bullet(doc,'Describe project scope, tools used, and outcome.')

def add_certs(doc):
    h2(doc,'Certifications')
    bullet(doc,'Certification Name — Issuing Organisation (Year)')

def add_instructions(doc, template_id):
    doc.add_page_break()
    h2(doc,'How to Use This Template')
    para(doc,'This is a fictional example template. All placeholder text is shown in grey italics. Replace every placeholder with your own information before submitting.', italic=True)
    bullet(doc,'Replace the name, contact details, and links in the header.')
    bullet(doc,'Rewrite the professional summary to reflect your own background.')
    bullet(doc,'Update skills to match the target role.')
    bullet(doc,'Replace experience entries with your own roles and achievements.')
    bullet(doc,'Keep bullet points concise and evidence-based.')
    bullet(doc,'Remove sections that do not apply to you.')
    bullet(doc,'Do not invent metrics, employers, or certifications.')
    placeholder(doc, f'Template ID: {template_id}  |  CareerVault Resume Mastery System  |  Fictional placeholder content — replace before use.')

def make_template(template_id, family_name, title_text, summary_text, extra=None):
    doc = base_doc()
    add_contact(doc)
    title(doc, title_text)
    subtitle(doc, family_name)
    add_summary(doc, summary_text)
    add_skills(doc)
    add_experience(doc)
    if extra:
        extra(doc)
    add_education(doc)
    add_projects(doc)
    add_certs(doc)
    add_instructions(doc, template_id)
    fname = template_id.replace('CV-','CV-').replace('_','_') + '_' + title_text.replace(' & ','_').replace(' ','_') + '.docx'
    # simpler filename per spec
    return doc

# Define templates
templates = [
 ('CV-A01','Family A — Clean ATS Professional','Standard Professional','Results-oriented professional with experience delivering reliable outcomes across cross-functional teams. Skilled in clear communication, structured problem-solving, and consistent execution.'),
 ('CV-A02','Family A — Clean ATS Professional','Achievement-Focused Professional','Professional with a record of delivering measurable improvements in process efficiency, quality, and stakeholder satisfaction through disciplined execution.'),
 ('CV-A03','Family A — Clean ATS Professional','Compact One-Page Professional','Concise professional summary highlighting core competencies, key achievements, and relevant experience in a compact one-page format.'),
 ('CV-B01','Family B — Technology & Analytical','Software & Technology','Software professional with experience designing, developing, and maintaining applications. Comfortable working with modern engineering practices and cross-functional product teams.'),
 ('CV-B02','Family B — Technology & Analytical','Data & Business Analytics','Analytical professional with experience turning data into actionable insights for business decisions. Skilled in data preparation, analysis, and stakeholder reporting.'),
 ('CV-B03','Family B — Technology & Analytical','Technical Operations & QA','Technical operations professional with experience in quality assurance, process reliability, and continuous improvement across delivery teams.'),
 ('CV-C01','Family C — Business & Management','Business Analyst','Business analyst with experience translating stakeholder needs into clear requirements and supporting data-informed decisions across projects.'),
 ('CV-C02','Family C — Business & Management','Product & Project Management','Product and project professional with experience coordinating delivery, aligning stakeholders, and shipping outcomes within scope and timelines.'),
 ('CV-C03','Family C — Business & Management','Management & Operations','Operations professional with experience improving processes, managing teams, and delivering consistent operational outcomes.'),
 ('CV-D01','Family D — Finance & Commercial','Finance & Accounting','Finance professional with experience in reporting, analysis, and compliance. Skilled in accurate financial documentation and stakeholder communication.'),
 ('CV-D02','Family D — Finance & Commercial','Sales & Business Development','Sales professional with experience building pipelines, managing client relationships, and delivering revenue outcomes through structured selling.'),
 ('CV-D03','Family D — Finance & Commercial','Marketing & Growth','Marketing professional with experience in campaign execution, content, and growth initiatives supported by data and experimentation.'),
 ('CV-E01','Family E — Career Progression','Career Progression','Experienced professional demonstrating clear career progression through increasing responsibility, ownership, and impact over time.'),
 ('CV-E02','Family E — Career Progression','Career Transition','Professional transitioning into a new domain, bringing transferable skills, relevant projects, and a structured plan for the new role.'),
 ('CV-E03','Family E — Career Progression','Experience-Led Professional','Senior individual contributor with deep domain expertise, strong delivery record, and mentoring contributions across teams.'),
]

# Map template id to filename per spec
name_map = {
 'CV-A01':'CV-A01_Standard_Professional.docx',
 'CV-A02':'CV-A02_Achievement_Focused.docx',
 'CV-A03':'CV-A03_Compact_One_Page.docx',
 'CV-B01':'CV-B01_Software_Technology.docx',
 'CV-B02':'CV-B02_Data_Analytics.docx',
 'CV-B03':'CV-B03_Technical_Operations.docx',
 'CV-C01':'CV-C01_Business_Analyst.docx',
 'CV-C02':'CV-C02_Product_Project.docx',
 'CV-C03':'CV-C03_Management_Operations.docx',
 'CV-D01':'CV-D01_Finance_Accounting.docx',
 'CV-D02':'CV-D02_Sales_Business_Development.docx',
 'CV-D03':'CV-D03_Marketing_Growth.docx',
 'CV-E01':'CV-E01_Career_Progression.docx',
 'CV-E02':'CV-E02_Career_Transition.docx',
 'CV-E03':'CV-E03_Experience_Led.docx',
}

for tid, fam, ttitle, summ in templates:
    doc = make_template(tid, fam, ttitle, summ)
    path = os.path.join(OUT, name_map[tid])
    doc.save(path)
    print('saved', path)

print('ALL TEMPLATES DONE')
