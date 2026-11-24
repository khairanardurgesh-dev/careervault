#!/usr/bin/env python3
"""Validation script for CareerVault content resources."""

import json
import os
import glob
from pathlib import Path

BASE_DIR = Path("C:/Users/Quick/Desktop/CareerVault")

errors = []
warnings = []
info = []


def add_error(msg, file_path=""):
    errors.append({"message": msg, "file": str(file_path)})


def add_warning(msg, file_path=""):
    warnings.append({"message": msg, "file": str(file_path)})


def add_info(msg, file_path=""):
    info.append({"message": msg, "file": str(file_path)})


def load_json(filepath):
    """Load a JSON file, return None if invalid."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        add_error(f"Failed to read JSON file: {e}", filepath)
        return None


def validate_required_fields(resource, required_fields, filepath):
    """Check that all required fields are present and non-empty."""
    missing = []
    for field in required_fields:
        if field not in resource or (resource[field] is None) or (isinstance(resource[field], str) and resource[field].strip() == ""):
            missing.append(field)
    if missing:
        add_error(f"Missing required fields: {', '.join(missing)}", filepath)


def validate_no_duplicate_ids(resources, id_field, filepath):
    """Check for duplicate resource IDs within a list."""
    ids = []
    dupes = []
    for r in resources:
        rid = r.get(id_field, "")
        if rid in ids:
            dupes.append(rid)
        ids.append(rid)
    if dupes:
        add_error(f"Duplicate {id_field} values: {', '.join(dupes)}", filepath)


def validate_enum_field(value, valid_values, field_name, filepath):
    """Check that an enum field has a valid value."""
    if value not in valid_values:
        add_error(f"Invalid {field_name}: '{value}'. Must be one of: {', '.join(valid_values)}", filepath)


def validate_schema(resource, schema_path, filepath):
    """Validate a resource against its JSON schema."""
    schema = load_json(schema_path)
    if schema is None:
        return
    # Simple validation: check that all schema-required fields exist in resource
    # (This is a basic check; full JSON Schema validation would require jsonschema library)
    required = schema.get("required", [])
    validate_required_fields(resource, required, filepath)


def check_pilot_mark(resource, filepath):
    """Check that pilot resources are marked as PILOT via the JSON 'pilot' field."""
    # Only warn about missing PILOT markers for resources explicitly marked as pilot=True
    # Resources with pilot=False or pilot missing are considered commercial/production content
    if resource.get("pilot") is True:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                file_content = f.read()
            if "PILOT" not in file_content.upper():
                add_warning(f"Pilot resource may not be marked as PILOT/NOT FINAL commercial release", filepath)
        except:
            pass


def main():
    print("=" * 60)
    print("CAREERVAULT - Content Validation")
    print("=" * 60)

    # 1. Validate all JSON schemas
    print("\n[1/5] Validating JSON schemas...")
    schema_dir = BASE_DIR / "schemas"
    for schema_file in sorted(schema_dir.glob("*.json")):
        resource_name = schema_file.stem
        # We don't have actual resources to validate against yet,
        # but we can validate the schemas are well-formed
        try:
            with open(schema_file, "r", encoding="utf-8") as f:
                json.load(f)
            add_info(f"Schema '{resource_name}' is well-formed JSON")
        except json.JSONDecodeError as e:
            add_error(f"Schema '{resource_name}' has JSON error: {e}")

    # 2. Validate pilot content resources
    print("\n[2/5] Validating pilot content resources...")
    content_dir = BASE_DIR / "content"

    # Interview questions
    int_files = glob.glob(str(content_dir / "interview-preparation" / "*.json"))
    int_required_fields = [
        "resourceId", "question", "module", "careerTrack", "relevantJobRoles",
        "experienceLevel", "intendedUser", "description", "purposeOfQuestion",
        "competencyAssessed", "answerFramework", "exampleAnswer",
        "weakAnswerPitfalls", "evaluationCriteria", "difficulty"
    ]
    for f in int_files:
        resource = load_json(f)
        if resource:
            validate_required_fields(resource, int_required_fields, f)
            # Check careerTrack is valid enum
            validate_enum_field(
                resource.get("careerTrack", ""),
                ["Track-A", "Track-B", "Track-C", "Track-D", "Track-E", "Track-F"],
                "careerTrack", f
            )
            # Check experienceLevel is valid
            validate_enum_field(
                resource.get("experienceLevel", ""),
                ["entry", "early-career", "mid-career"],
                "experienceLevel", f
            )
            # Check difficulty
            valid_difficulties = ["easy", "medium", "hard"]
            if resource.get("difficulty", "") not in valid_difficulties:
                add_error(
                    f"Invalid difficulty value: '{resource.get('difficulty', '')}'. Must be one of: {', '.join(valid_difficulties)}",
                    f
                )
            # Check pilot marker
            check_pilot_mark(resource, f)

    # Resume examples
    res_files = glob.glob(str(content_dir / "resume" / "*.json"))
    res_required_fields = [
        "resourceId", "title", "module", "careerTrack", "experienceLevel",
        "intendedUser", "description", "content", "examples", "creationDate",
        "reviewStatus", "version"
    ]
    for f in res_files:
        resource = load_json(f)
        if resource:
            validate_required_fields(resource, res_required_fields, f)
            validate_enum_field(
                resource.get("careerTrack", ""),
                ["Track-A", "Track-B", "Track-C", "Track-D", "Track-E", "Track-F"],
                "careerTrack", f
            )
            validate_enum_field(
                resource.get("experienceLevel", ""),
                ["entry", "early-career", "mid-career"],
                "experienceLevel", f
            )
            check_pilot_mark(resource, f)

    # Recruiter messages
    rec_files = glob.glob(str(content_dir / ".." / "templates" / "recruiter-messages" / "*.json"))
    # Actually let's search in the right place
    rec_files = glob.glob(str(BASE_DIR / "templates" / "recruiter-messages" / "*.json"))
    rec_required_fields = [
        "resourceId", "title", "module", "careerTrack", "relevantJobRoles",
        "experienceLevel", "intendedUser", "description", "messageType", "template",
        "placeholders", "creationDate", "reviewStatus", "version"
    ]
    for f in rec_files:
        resource = load_json(f)
        if resource:
            validate_required_fields(resource, rec_required_fields, f)
            validate_enum_field(
                resource.get("careerTrack", ""),
                ["Track-A", "Track-B", "Track-C", "Track-D", "Track-E", "Track-F"],
                "careerTrack", f
            )
            validate_enum_field(
                resource.get("experienceLevel", ""),
                ["entry", "early-career", "mid-career"],
                "experienceLevel", f
            )
            check_pilot_mark(resource, f)

    # Salary negotiation
    sal_files = glob.glob(str(BASE_DIR / "content" / "salary-negotiation" / "*.json"))
    sal_required_fields = [
        "resourceId", "title", "module", "careerTrack", "relevantJobRoles",
        "experienceLevel", "intendedUser", "description", "scenario",
        "fixedCompensation", "variableCompensation", "bonuses", "benefits",
        "deductions", "takeHomeSalary", "ctc", "assumptions", "creationDate",
        "reviewStatus", "version"
    ]
    for f in sal_files:
        resource = load_json(f)
        if resource:
            validate_required_fields(resource, sal_required_fields, f)
            # Check fixedCompensation has required sub-fields
            fc = resource.get("fixedCompensation", {})
            if not isinstance(fc, dict):
                add_error("fixedCompensation must be an object", f)
            else:
                for sub in ["annualBase", "monthlyBase", "payFrequency"]:
                    if sub not in fc:
                        add_error(f"fixedCompensation missing required field: {sub}", f)
            # Check deductions has required sub-fields
            ded = resource.get("deductions", {})
            if not isinstance(ded, dict):
                add_error("deductions must be an object", f)
            else:
                for sub in ["taxEstimate", "pfContribution"]:
                    if sub not in ded:
                        add_error(f"deductions missing required field: {sub}", f)
            # Check takeHomeSalary has required sub-fields
            th = resource.get("takeHomeSalary", {})
            if not isinstance(th, dict):
                add_error("takeHomeSalary must be an object", f)
            else:
                for sub in ["monthlyGross", "monthlyTakeHome", "calculationAssumptions"]:
                    if sub not in th:
                        add_error(f"takeHomeSalary missing required field: {sub}", f)
            validate_enum_field(
                resource.get("careerTrack", ""),
                ["Track-A", "Track-B", "Track-C", "Track-D", "Track-E", "Track-F"],
                "careerTrack", f
            )
            validate_enum_field(
                resource.get("experienceLevel", ""),
                ["entry", "early-career", "mid-career"],
                "experienceLevel", f
            )
            check_pilot_mark(resource, f)

    # Career roadmaps
    road_files = glob.glob(str(BASE_DIR / "content" / "career-roadmaps" / "*.json"))
    road_required_fields = [
        "resourceId", "title", "module", "careerTrack", "relevantJobRoles",
        "experienceLevel", "intendedUser", "description", "roadmapTitle",
        "timeframe", "weeklyActivities", "milestones", "creationDate",
        "reviewStatus", "version"
    ]
    for f in road_files:
        resource = load_json(f)
        if resource:
            validate_required_fields(resource, road_required_fields, f)
            validate_enum_field(
                resource.get("careerTrack", ""),
                ["Track-A", "Track-B", "Track-C", "Track-D", "Track-E", "Track-F"],
                "careerTrack", f
            )
            validate_enum_field(
                resource.get("experienceLevel", ""),
                ["entry", "early-career", "mid-career"],
                "experienceLevel", f
            )
            # Check weeklyActivities structure
            activities = resource.get("weeklyActivities", [])
            for i, activity in enumerate(activities):
                if not isinstance(activity, dict):
                    add_error(f"weeklyActivities[{i}] must be an object", f)
                else:
                    if "week" not in activity:
                        add_error(f"weeklyActivities[{i}] missing 'week' field", f)
                    if "activities" not in activity:
                        add_error(f"weeklyActivities[{i}] missing 'activities' field", f)
                    if "measurableTasks" not in activity:
                        add_error(f"weeklyActivities[{i}] missing 'measurableTasks' field", f)
            check_pilot_mark(resource, f)

    # 3. Check for duplicate resource IDs
    print("\n[3/5] Checking for duplicate resource IDs...")
    all_resources = []
    for f in int_files:
        r = load_json(f)
        if r:
            all_resources.append(r)
    for f in res_files:
        r = load_json(f)
        if r:
            all_resources.append(r)
    for f in rec_files:
        r = load_json(f)
        if r:
            all_resources.append(r)
    for f in sal_files:
        r = load_json(f)
        if r:
            all_resources.append(r)
    for f in road_files:
        r = load_json(f)
        if r:
            all_resources.append(r)

    seen_ids = []
    duplicate_ids = []
    for r in all_resources:
        rid = r.get("resourceId", "")
        if rid in seen_ids:
            duplicate_ids.append(rid)
        seen_ids.append(rid)
    if duplicate_ids:
        add_error(f"Duplicate resource IDs found: {', '.join(duplicate_ids)}")
    else:
        add_info("No duplicate resource IDs found")

    # 4. Check directory and package integrity
    print("\n[4/5] Checking directory and package integrity...")
    # Check that all expected directories exist
    expected_dirs = [
        "content/resume", "content/professional-profiles", "content/job-search",
        "content/interview-preparation", "content/salary-negotiation",
        "content/ai-career-assistant", "content/career-roadmaps", "content/career-advancement",
        "tracks/technology-it", "tracks/business-analysis", "tracks/product-project",
        "tracks/finance", "tracks/sales-marketing", "tracks/management-operations",
        "templates/resumes", "templates/recruiter-messages", "templates/interview-scorecards",
        "templates/trackers", "templates/assessments", "schemas", "output"
    ]
    for d in expected_dirs:
        full_path = BASE_DIR / d
        if not full_path.exists():
            add_error(f"Expected directory missing: {d}")
        else:
            add_info(f"Directory exists: {d}")

    # Check XLSX files exist
    xlsx_files = ["output/job-application-tracker.xlsx", "output/salary-offer-calculator.xlsx"]
    for xlsx in xlsx_files:
        xlsx_path = BASE_DIR / xlsx
        if xlsx_path.exists():
            size = xlsx_path.stat().st_size
            add_info(f"XLSX file exists: {xlsx} ({size} bytes)")
            # Try to open with openpyxl
            try:
                import openpyxl
                wb = openpyxl.load_workbook(xlsx_path)
                add_info(f"  - Sheets: {wb.sheetnames}")
            except Exception as e:
                add_error(f"  - Failed to open XLSX: {e}")
        else:
            add_error(f"XLSX file missing: {xlsx}")

    # 5. Summary
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)

    print(f"\nErrors: {len(errors)}")
    for err in errors:
        print(f"  [ERROR] {err['file']}: {err['message']}")

    print(f"\nWarnings: {len(warnings)}")
    for warn in warnings:
        print(f"  [WARNING] {warn['file']}: {warn['message']}")

    print(f"\nInfo: {len(info)}")
    for inf in info:
        print(f"  [INFO] {inf['file']}: {inf['message']}")

    if errors:
        print(f"\n! validation completed with {len(errors)} error(s).")
    else:
        print(f"\n+ validation completed successfully.")

    return len(errors) == 0


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)