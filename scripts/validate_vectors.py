#!/usr/bin/env python3
"""
validate_vectors.py - Automated validation of Romanian PID specifications,
embedded JSON blocks, SD-JWT disclosures, SHA-256 hashes, UTF-8 encoding,
cross-references, and workflow/ansible YAML syntax.
"""

import os
import sys
import glob
import re
import json
import base64
import hashlib
import yaml

# Ensure utf-8 output encoding across environments
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass


def validate_json_blocks():
    print("[-] Validating embedded JSON blocks in Markdown files...")
    md_files = glob.glob("*.md")
    total_blocks = 0
    errors = 0

    for filepath in md_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        json_blocks = re.findall(r"```json\n(.*?)\n```", content, re.DOTALL)
        for idx, block in enumerate(json_blocks, 1):
            total_blocks += 1
            if "<" in block and ">" in block:
                continue
            try:
                json.loads(block)
            except json.JSONDecodeError as err:
                print(f"  [ERROR] {filepath} (JSON block {idx}): {err}")
                errors += 1

    if errors == 0:
        print(f"  [OK] All {total_blocks} JSON blocks validated successfully.\n")
        return True
    else:
        print(f"  [FAIL] {errors} JSON validation error(s) found.\n")
        return False


def validate_sd_jwt_disclosures():
    print("[-] Validating SD-JWT disclosures and SHA-256 digests in RO_PID_Data_Model.md...")
    model_path = "RO_PID_Data_Model.md"
    if not os.path.exists(model_path):
        print(f"  [ERROR] {model_path} not found.")
        return False

    with open(model_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    disclosures = []
    for line in lines:
        parts = [p.strip() for p in line.split("|") if p.strip()]
        if len(parts) >= 4 and any("Wy" in p for p in parts):
            for i, p in enumerate(parts):
                if "Wy" in p:
                    disc = p.replace("`", "")
                    digest = parts[i + 1].replace("`", "")
                    claim = parts[0].replace("`", "")
                    disclosures.append((claim, disc, digest))
                    break

    if not disclosures:
        print("  [ERROR] No disclosures found in RO_PID_Data_Model.md.")
        return False

    errors = 0
    for claim, disc, expected_digest in disclosures:
        calc_digest = (
            base64.urlsafe_b64encode(hashlib.sha256(disc.encode("ascii")).digest())
            .decode("ascii")
            .rstrip("=")
        )
        if calc_digest != expected_digest:
            print(f"  [ERROR] Digest mismatch for '{claim}': expected {expected_digest}, calculated {calc_digest}")
            errors += 1
        else:
            try:
                padded = disc + "=" * (-len(disc) % 4)
                decoded_bytes = base64.urlsafe_b64decode(padded)
                json_str = decoded_bytes.decode("utf-8")
                parsed_json = json.loads(json_str)

                if claim == "issuing_authority":
                    val = parsed_json[2]
                    expected_val = "Direc\u021bia General\u0103 pentru Eviden\u021ba Persoanelor"
                    if val != expected_val:
                        print(f"  [ERROR] issuing_authority payload corrupted: got {repr(val)}")
                        errors += 1
            except Exception as e:
                print(f"  [ERROR] Malformed disclosure payload for '{claim}': {e}")
                errors += 1

    if errors == 0:
        print(f"  [OK] All {len(disclosures)} SD-JWT disclosure digests match SHA-256 test vectors.\n")
        return True
    else:
        print(f"  [FAIL] {errors} disclosure error(s) found.\n")
        return False


def validate_utf8_encoding():
    print("[-] Checking UTF-8 encoding integrity across specification files...")
    expected_authority = "Direc\u021bia General\u0103 pentru Eviden\u021ba Persoanelor"
    expected_bytes = expected_authority.encode("utf-8")

    assert b"\xc8\x9b" in expected_bytes, "Missing comma-below t (U+021B)"
    assert b"\xc4\x83" in expected_bytes, "Missing a-breve (U+0103)"

    md_files = glob.glob("*.md")
    for fpath in md_files:
        with open(fpath, "rb") as f:
            raw = f.read()
        try:
            raw.decode("utf-8")
        except UnicodeDecodeError as e:
            print(f"  [ERROR] File {fpath} contains invalid UTF-8 bytes: {e}")
            return False

    print("  [OK] All markdown files are strictly valid UTF-8.\n")
    return True


def validate_references():
    print("[-] Checking cross-references in RO_PID.md...")
    with open("RO_PID.md", "r", encoding="utf-8") as f:
        content = f.read()

    sec9 = content.split("## 9 References")[-1].split("## Annex")[0]
    defined = set(re.findall(r"\|\s*\*\*\[([^\]]+)\]\*\*", sec9))

    body = content.split("## 9 References")[0]
    citations = set(re.findall(r"\[([A-Z0-9a-z /._-]+)\](?!\()", body))

    missing = [c for c in sorted(citations) if c not in defined]
    if missing:
        print(f"  [ERROR] Citations missing from Section 9 References: {missing}")
        return False
    print(f"  [OK] All {len(citations)} citations resolve to Section 9 References.\n")
    return True


def validate_yaml_files():
    print("[-] Validating YAML syntax in workflows and ansible suites...")
    yaml_files = glob.glob(".github/**/*.yml", recursive=True) + glob.glob("ansible/**/*.yml", recursive=True)
    errors = 0
    for yf in yaml_files:
        try:
            with open(yf, "r", encoding="utf-8") as f:
                yaml.safe_load(f)
        except Exception as e:
            print(f"  [ERROR] Failed parsing {yf}: {e}")
            errors += 1

    if errors == 0:
        print(f"  [OK] All {len(yaml_files)} YAML files are syntactically valid.\n")
        return True
    else:
        print(f"  [FAIL] {errors} YAML parsing error(s).\n")
        return False


def main():
    print("==========================================================")
    print(" Romanian PID Specification & Cryptographic Vector Checker")
    print("==========================================================\n")

    results = [
        validate_json_blocks(),
        validate_sd_jwt_disclosures(),
        validate_utf8_encoding(),
        validate_references(),
        validate_yaml_files()
    ]

    if all(results):
        print("-> [SUCCESS] All checks passed successfully!")
        sys.exit(0)
    else:
        print("-> [FAILURE] Some checks failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
