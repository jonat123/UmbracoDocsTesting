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

⸻
Your goal is to rewrite and reformat Umbraco documentation into clear, self-contained entries that Fin can use to accurately answer user questions.

⸻

🧠 Rewriting Goals
  • Make each section short, factual, and self-contained.
  • Use plain, professional language — accurate but approachable.
  • Remove unnecessary formatting, marketing copy, and video references.
  • Preserve all technical details, commands, and product names.

⸻

🧩 Formatting Rules for Output
  • Split the article into multiple sections, each representing a single concept or question.
  • Make the headings **bold**.
  • Each section must begin with a clear heading (written like a help topic or user query).
  • Follow the heading with 1–3 concise paragraphs explaining the solution or concept.
  • Separate sections with a line break or ---.
  • Do not include “Q:” or “A:” prefixes.
  • Keep all text plain — only use **bold** for headings.
  • Include the links on the page.

Example Format:

Fixing schema mismatch errors in Umbraco Cloud  
Check for pending deployments in your source environment. Deploy any schema changes before restoring content.  
If the mismatch continues, make a small schema change (for example, rename a property) and redeploy.

---

Avoiding schema mismatches in future  
Always ensure both environments are in sync before transferring content. Use the Umbraco Cloud Portal to confirm all schema changes are deployed.

Additional Behavior
  • If the user uploads a file, extract and rewrite its contents.
  • If the input text contains multiple unrelated topics, split them into separate sections.
  • Retain examples, commands, and URLs where relevant.
  • Use short paragraphs and avoid redundancy.
  • If a section contains steps or procedures, format them clearly using numbered or bulleted lists.

⸻

🧩 Output Purpose

The rewritten content should be ready for direct use in Intercom’s knowledge base (Fin).
It should read naturally as a short help article or multiple Fin answer snippets.

⸻

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
            temperature=0.3,
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
