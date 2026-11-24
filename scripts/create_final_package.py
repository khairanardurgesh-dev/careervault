import os, json, hashlib, zipfile
from datetime import datetime

BASE = r'C:\Users\Quick\Desktop\CareerVault\output'

# Module folder mapping
modules = {
 '01_Resume_Mastery': 'resume-mastery-system',
 '02_Professional_Profile_Optimisation': 'professional-profile-optimisation-system',
 '03_Job_Search_Operating_System': 'job-search-operating-system',
 '04_Interview_Preparation_Vault': 'interview-preparation-vault',
 '05_Salary_and_Offer_Negotiation': 'salary-and-offer-negotiation-system',
 '06_AI_Career_Assistant_Toolkit': 'ai-career-assistant-toolkit',
 '07_90_Day_Job_Switch_Programme': '90-day-job-switch-programme',
 '08_Career_Advancement_Toolkit': 'career-advancement-toolkit',
}

# Count files per module
module_info = {}
for folder, src in modules.items():
    src_path = os.path.join(BASE, src)
    count = 0
    for root, dirs, files in os.walk(src_path):
        for f in files:
            if not f.startswith('.') and not f.endswith('.pyc'):
                count += 1
    module_info[folder] = {'source_folder': src, 'file_count': count}

# Build manifest
manifest = {
 'product_name': 'CareerVault Complete Job Switch System',
 'brand': 'CareerVault',
 'product_version': '1.0.0',
 'release_date': datetime.now().strftime('%Y-%m-%d'),
 'currency': 'INR',
 'price_in_paise': 399900,
 'modules': [
  {'id': '01', 'name': 'Resume Mastery System', 'version': '1.0.0', 'folder': '01_Resume_Mastery', **module_info['01_Resume_Mastery']},
  {'id': '02', 'name': 'Professional Profile Optimisation System', 'version': '1.0.0', 'folder': '02_Professional_Profile_Optimisation', **module_info['02_Professional_Profile_Optimisation']},
  {'id': '03', 'name': 'Job Search Operating System', 'version': '1.0.0', 'folder': '03_Job_Search_Operating_System', **module_info['03_Job_Search_Operating_System']},
  {'id': '04', 'name': 'Interview Preparation Vault', 'version': '1.0.0', 'folder': '04_Interview_Preparation_Vault', **module_info['04_Interview_Preparation_Vault']},
  {'id': '05', 'name': 'Salary & Offer Negotiation System', 'version': '1.0.0', 'folder': '05_Salary_and_Offer_Negotiation', **module_info['05_Salary_and_Offer_Negotiation']},
  {'id': '06', 'name': 'AI Career Assistant Toolkit', 'version': '1.0.0', 'folder': '06_AI_Career_Assistant_Toolkit', **module_info['06_AI_Career_Assistant_Toolkit']},
  {'id': '07', 'name': '90-Day Job Switch Programme', 'version': '1.0.0', 'folder': '07_90_Day_Job_Switch_Programme', **module_info['07_90_Day_Job_Switch_Programme']},
  {'id': '08', 'name': 'Career Advancement Toolkit', 'version': '1.0.0', 'folder': '08_Career_Advancement_Toolkit', **module_info['08_Career_Advancement_Toolkit']},
 ],
 'total_files': sum(m['file_count'] for m in module_info.values()),
 'checksums': {},
 'release_status': 'final'
}

# Calculate checksums for key files
key_files = [
 'CAREERVAULT_START_HERE.pdf',
 'LICENCE/PERSONAL_USE_LICENCE.pdf',
]
for kf in key_files:
    path = os.path.join(BASE, kf)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            manifest['checksums'][kf] = hashlib.sha256(f.read()).hexdigest()

# Save manifest
manifest_path = os.path.join(BASE, 'PRODUCT_VERSION_MANIFEST.json')
with open(manifest_path, 'w') as f:
    json.dump(manifest, f, indent=2)
print('Manifest saved:', manifest_path)

# Create ZIP package
zip_path = os.path.join(BASE, 'CareerVault_Complete_Job_Switch_System_v1.0.zip')
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    # START_HERE
    zf.write(os.path.join(BASE, 'CAREERVAULT_START_HERE.pdf'), 'CareerVault_Complete_Job_Switch_System_v1.0/START_HERE.pdf')
    # Licence
    zf.write(os.path.join(BASE, 'career-advancement-toolkit', 'licence', 'PERSONAL_USE_LICENCE.pdf'), 'CareerVault_Complete_Job_Switch_System_v1.0/LICENCE/PERSONAL_USE_LICENCE.pdf')
    # Manifest
    zf.write(manifest_path, 'CareerVault_Complete_Job_Switch_System_v1.0/PRODUCT_VERSION_MANIFEST.json')
    # Modules
    for folder, src in modules.items():
        src_path = os.path.join(BASE, src)
        for root, dirs, files in os.walk(src_path):
            for f in files:
                if f.startswith('.') or f.endswith('.pyc'):
                    continue
                full = os.path.join(root, f)
                rel = os.path.relpath(full, src_path)
                arc = os.path.join('CareerVault_Complete_Job_Switch_System_v1.0', folder, rel)
                zf.write(full, arc)
    # Module START_HERE files if they exist
    for folder, src in modules.items():
        starthere = os.path.join(BASE, src, 'START_HERE.pdf')
        if os.path.exists(starthere):
            arc = os.path.join('CareerVault_Complete_Job_Switch_System_v1.0', folder, 'START_HERE.pdf')
            zf.write(starthere, arc)

# Calculate ZIP checksum
with open(zip_path, 'rb') as f:
    manifest['checksums']['CareerVault_Complete_Job_Switch_System_v1.0.zip'] = hashlib.sha256(f.read()).hexdigest()

# Update manifest with ZIP checksum
with open(manifest_path, 'w') as f:
    json.dump(manifest, f, indent=2)

print('ZIP created:', zip_path)
print('ZIP size:', os.path.getsize(zip_path), 'bytes')
print('Done')