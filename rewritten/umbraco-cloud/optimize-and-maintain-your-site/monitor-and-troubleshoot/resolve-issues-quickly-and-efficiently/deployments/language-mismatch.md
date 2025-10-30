**Understanding “Languages in source and destination site do not match” errors**  
This error appears in Umbraco Cloud when dictionary items reference a language that no longer exists in the backoffice. It is typically triggered after deleting a language from the Settings dashboard while dictionary items still store translations for that language.

You will see an extraction error with a red indicator in the Cloud environment. The detailed message reads: “Languages in source and destination site do not match.”

---

**When this error occurs**  
The mismatch occurs in either of these scenarios:
- Adding a new environment (commonly Development or Staging) to a project that already has dictionary items.
- Creating a new project from a baseline that includes dictionary items.

It happens when all of the following are true in the source environment: you had at least two backoffice languages, you created dictionary items with translations, and you then deleted one of the languages.

---

**Preventive fix: Resave dictionary items after deleting a language (Method 1)**  
After deleting any backoffice language, resave all dictionary items in the source environment. This updates their stored translations to match the current languages.

If you do this before creating a new environment or child project, the new instance should provision without the mismatch error.

---

**Corrective fix: Edit dictionary UDA files to remove deleted languages (Method 2)**  
If the new environment already exists and shows the error, remove the deleted language entries directly from the UDA files, then run a manual extraction.

Steps:
1. Open the target environment via KUDU tools: ../../power-tools/
2. Navigate to site/wwwroot/data/revision and locate the dictionary item UDA files.
3. Edit each affected UDA file to delete the section that references the removed language.
4. Save the files and run a manual extraction: ../../power-tools/manual-extractions.md
5. In the backoffice, resave the dictionary items to log changes to Git and ensure consistency for future deployments.

---

**Avoiding language mismatches in future**  
Before deleting a language, plan to resave all dictionary items that include translations for that language. Always ensure environments and baselines are aligned on configured languages prior to creating new environments or child projects.

Links:
- KUDU tools: ../../power-tools/
- Manual extractions: ../../power-tools/manual-extractions.md