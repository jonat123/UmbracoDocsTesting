**Schema mismatch errors when transferring or restoring content**  
Schema mismatches occur when the structure (schema) in the source environment differs from the target environment. Schema includes Document Types, Media Types, Data Types, Templates, and Dictionary items. Transfers or restores fail when those schema items are not in sync.

---

**How Umbraco indicates schema mismatches**  
Umbraco shows a schema mismatch error that lists the specific schema items preventing the transfer or restore. Use the error details to identify which Document Type, Media Type, Data Type, Template, or Dictionary item differs.

---

**Basic steps to resolve schema mismatches**  
1. Check the source environment for pending deployments.  
2. If working locally, push any uncommitted changes via Git.  
3. If using Umbraco Cloud, deploy pending changes from the Umbraco Cloud Portal.  
Deploying pending schema changes from the source will usually bring the target environment into sync and allow the transfer.

---

**If there are no pending deployments: make and deploy a minor schema change**  
If the source has no pending deployments but the target still reports a mismatch, make a small, safe change to the mismatched schema item in the source (for example, add or rename a property temporarily). Then deploy that change to the next environment. This forces the schema to update on the target and resolves the mismatch.

---

**Resolving differences in aliases or names**  
If the mismatch is only about aliases or names, you can manually edit the alias or name on the target environment to match the source. Once the aliases/names match, the content transfer should succeed.

---

**Preventing schema mismatches in future**  
Always ensure schema changes are deployed from the source before transferring content. Use the Umbraco Cloud Portal to confirm all schema changes are deployed between environments. Adopt a workflow where schema changes are deployed first, then content is transferred or restored.

---

**Quick pre-transfer checklist**  
- Confirm no pending deployments in the source environment.  
- Push local Git commits if working locally.  
- Verify Document Types, Media Types, Data Types, Templates, and Dictionary items match.  
- If necessary, apply minor schema change and deploy or update aliases/names on the target.