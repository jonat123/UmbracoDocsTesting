**Understanding schema mismatches in Umbraco Cloud**

Schema mismatches occur when the structure of your project (the schema) is different between the source and target environments. The schema includes Document Types, Media Types, Data Types, Templates, and Dictionary items.

These mismatches block content transfers and restores until the environments are brought back into sync.

---

**How schema mismatch errors appear**

When a transfer or restore fails, the error message lists the specific schema items that are out of sync. Use this information to identify which Document Type, Data Type, Template, or other item needs attention.

---

**Resolve mismatches by deploying pending changes**

First, check for pending deployments in the source environment. If you are working locally, commit and push any schema changes to Git. For transfers between Umbraco Cloud environments, use the Umbraco Cloud Portal to review and deploy any pending changes from the source to the target.

Once all pending deployments are completed, retry the transfer or restore.

---

**Resolve mismatches when no pending deployments exist**

If no pending deployments are shown, make a small change to the mismatched schema item in the source environment (for example, update the description or a property on the affected Document Type).

Deploy this change to the next environment. This forces the schema to update in the target environment and brings it back in sync.

---

**Fix alias or name mismatches**

If the mismatch involves different aliases or names, update the item manually in the target environment so it matches the source. After aligning the item, retry the content transfer.

---

**Prevent future schema mismatches**

Before transferring content, ensure all schema changes are committed, pushed, and deployed from the source environment. Use the Umbraco Cloud Portal to verify there are no pending schema changes.

Keeping schema changes deployed promptly helps maintain synchronization across environments and prevents transfer or restore failures.