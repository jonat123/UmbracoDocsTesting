**Understanding schema mismatches in Umbraco Cloud**  
Schema mismatches occur when the schema in the source environment does not match the target environment during a content transfer or restore. Schema includes Document Types, Media Types, Data Types, Templates, and Dictionary items. The error message will list the specific items that differ and block the operation.

---

**Fixing schema mismatch errors during transfer or restore**  
Follow these steps when a schema mismatch error appears.

Steps:
1. Review the error message to identify the specific schema items that differ (e.g., a particular Document Type).
2. Check for pending deployments in the source environment:
   - If working locally, commit and push any changes via Git.
   - If transferring between Umbraco Cloud environments, use the Umbraco Cloud Portal to deploy pending schema changes.
3. If there are no pending deployments, make a minor edit to the mismatched schema item in the source environment (for example, open and save the affected Document Type).
4. Deploy the change to the next environment to update the target schema.
5. Retry the content transfer or restore.
6. If the mismatch involves aliases or names, align them manually on the target environment to allow the transfer, then retry.

---

**Avoiding schema mismatches in the future**  
Keep environments in sync before moving content.

Steps:
1. Always deploy schema changes from the environment where they were created before transferring content.
2. Verify there are no pending deployments in the source environment via Git or the Umbraco Cloud Portal.
3. Make small schema edits and deploy if deployments appear stuck or changes are not detected.