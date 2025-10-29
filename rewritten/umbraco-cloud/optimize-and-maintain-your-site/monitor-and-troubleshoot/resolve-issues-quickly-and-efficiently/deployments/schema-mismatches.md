**What is a schema mismatch error in Umbraco Cloud?**
A schema mismatch error appears when transferring or restoring content between two Umbraco Cloud environments that do not have the same schema. The schema includes Document Types, Media Types, Data Types, Templates, and Dictionary items.

When the structure of these items differs between the source and target environments, transfers or restores can fail with a schema mismatch message.

---

**How to identify the cause of a schema mismatch**
The error message lists the specific schema items that are mismatched. Use this information to determine which Document Type, Media Type, Data Type, Template, or Dictionary item needs to be aligned between environments.

---

**Resolve schema mismatches by deploying pending changes**
First, check for pending deployments in the source environment. If working locally, commit and push any schema changes via Git. If transferring between Umbraco Cloud environments, open the Umbraco Cloud Portal and deploy any pending schema changes.

If there are no pending deployments, make a small change to the mismatched schema item in the source environment (for example, edit and save the affected Document Type) and deploy that change. This applies the update to the target environment and brings the schemas into sync.

---

**Fix mismatches involving aliases or names**
If the mismatch is caused by differences in aliases or names, update these values in the target environment to match the source. Aligning the aliases or names allows the transfer to complete successfully.

---

**Prevent future schema mismatches**
Keep environments in sync by deploying schema changes regularly and only through the standard deployment flow (Git commits/pushes for local work or the Umbraco Cloud Portal for environment-to-environment deployments). Regular, incremental deployments help avoid drift and reduce transfer or restore failures.