**Understanding schema mismatches on Umbraco Cloud**  
Schema mismatches occur when the schema in your source and target environments are not in sync during a content transfer or restore. Schema includes Document Types, Media Types, Data Types, Templates, and Dictionary items.  
The error message lists the exact items that differ so you can identify what needs to be updated.

---

**Fixing schema mismatch errors**  
1) Check for pending deployments in the source environment.  
- Working locally: commit and push any schema changes via Git.  
- Between Cloud environments: use the Umbraco Cloud Portal to review and deploy pending changes.

2) If no deployments are pending, make a minor change to the mismatched schema item in the source environment (for example, update a property or display name on the affected Document Type).  
3) Deploy the change to the next environment. This updates the target schema and brings both environments into sync.

---

**Resolving alias or name mismatches**  
If the mismatches are due to differences in aliases or names, align them manually on the target environment to match the source.  
After updating, retry the transfer or restore. Consider deploying a small change from the source afterward to ensure both environments remain synchronized.

---

**Avoiding schema mismatches in future**  
Always deploy schema changes before transferring or restoring content. Confirm both environments are in sync using the Umbraco Cloud Portal.  
Adopt a consistent deployment flow so schema updates move through environments before content transfers.