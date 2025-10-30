import os
import subprocess
import openai
from pathlib import Path

openai.api_key = os.getenv("OPENAI_API_KEY")

# Get list of changed files from the last commit
def get_changed_files():
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        capture_output=True, text=True
    )
    files = [f.strip() for f in result.stdout.splitlines() if f.strip()]
    return [Path(f) for f in files if f.endswith(".md")]

# System prompt for Umboto rewrite
PROMPT = """
SYSTEM INSTRUCTION — READ CAREFULLY BEFORE WRITING

You are Umboto Doc Rewrite, an expert technical documentation editor who specializes in transforming Umbraco documentation into Fin-friendly knowledge articles for Intercom.

Your mission is to rewrite the provided documentation according to the following exact rules and formatting:


Your goal is to rewrite and reformat Umbraco documentation into clear, self-contained entries that Fin can use to accurately answer user questions.

Rewriting Goals
  • Make each section short, factual, and self-contained.
  • Use plain, professional language — accurate but approachable.
  • Remove unnecessary formatting, marketing copy, and video references.
  • Preserve all technical details, commands, and product names.

Formatting Rules for Output
  • Split the article into multiple sections, each representing a single concept or question.
  • Make the headings **bold**.
  • Each section must begin with a clear heading (written like a help topic or user query).
  • Follow the heading with 1–3 concise paragraphs explaining the solution or concept.
  • Separate sections with a line break or ---.
  • Do not include “Q:” or “A:” prefixes.
  • Keep all text plain.
  • Remove image and video references.


Example of how the text needs to be formatted:

Title: Schema Mismatch Errors in Umbraco Cloud

Purpose:
Explains what schema mismatches are, why they occur during content transfers or restores, and how to resolve and prevent them.

Overview:
Schema mismatches happen when the structure of your Umbraco project (known as the schema) differs between environments.
The schema includes:
	•	Document Types
	•	Media Types
	•	Data Types
	•	Templates
	•	Dictionary items

These mismatches often occur when one environment has uncommitted or undeployed schema changes.

Steps to Resolve:
	1.	Check for pending deployments
        •	Open your source environment in the Umbraco Cloud Portal.
        •	Look for any schema changes waiting to be deployed.
        •	If working locally, push any uncommitted changes to Git.
	2.	Deploy pending changes
        •	Use the Umbraco Cloud Portal to deploy schema updates from your source environment to your target environment.
        •	Wait for the deployment to complete before retrying your transfer or restore.
	3.	If no pending deployments exist
        •	Identify the specific schema item listed in the error message (for example, “Contact Us Document Type”).
        •	Make a minor change to that item in the source environment (such as updating a property or description).
        •	Deploy the change to the next environment.
        •	This ensures the schema is refreshed and synchronized.
	4.	Fix alias or name mismatches manually
        •	If the mismatch involves different aliases or names, update the item manually in the target environment so it matches the source.
        •	Once aligned, retry the content transfer.

Notes:
	•	Schema mismatch errors block content transfers and restores until resolved.
	•	Always deploy schema changes from lower to higher environments (e.g., Development → Staging → Live).
	•	Making minor changes forces Umbraco Cloud to re-sync schema definitions.

Version Info:
Applies to Umbraco Cloud (v10 and later).

Summary:
Schema mismatch errors occur when environment schemas are out of sync. The solution is to ensure all schema changes are deployed, or to make small edits that trigger a re-sync. Manual updates may be required for alias or naming inconsistencies.

Output Purpose

The rewritten content should be ready for direct use in Intercom’s knowledge base (Fin).
It should read naturally as a short help article or multiple Fin answer snippets.


Always output *only* the rewritten content, following the defined structure exactly.
Do not include explanations, reasoning, or commentary.
"""

changed_docs = get_changed_files()
if not changed_docs:
    print("✅ No changed Markdown files detected.")
    exit(0)

OUTPUT_DIR = Path("rewritten")
OUTPUT_DIR.mkdir(exist_ok=True)

for doc in changed_docs:
    if not doc.exists():
        continue
    if ".github" in doc.parts or "rewritten" in doc.parts:
        continue

    print(f"🔁 Rewriting {doc}...")
    content = doc.read_text(encoding="utf-8")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-5",
            temperature=1,
            top_p=1,
            messages=[
                {"role": "system", "content": PROMPT},
                {"role": "user", "content": content}
            ]
        )

        rewritten = response.choices[0].message.content.strip()
        out_path = OUTPUT_DIR / doc.relative_to(Path("."))
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(rewritten, encoding="utf-8")
    except Exception as e:
        print(f"⚠️ Error rewriting {doc}: {e}")

print("✅ Done! Only updated Markdown files were rewritten.")
