**What is a schema mismatch in Umbraco Cloud**  
A schema mismatch happens when the content schema is different between the source environment and the target environment during a transfer or restore. Schema covers Document Types, Media Types, Data Types, Templates, and Dictionary items. The transfer/restore error message lists which schema items are out of sync.

---

**How to check for pending schema deployments**  
Before transferring content, confirm there are no pending schema deployments in the source environment. If you work locally, commit and push any schema changes via Git. If you use Umbraco Cloud, open the Umbraco Cloud Portal and check the source environment for pending deployments; deploy them before attempting the transfer.

---

**Resolving schema mismatch errors (recommended approach)**  
If the target environment is missing schema changes from the source, update the source schema and deploy the change so the target receives the update. Typical steps:
1. Make a small schema change in the source environment (for example, rename a property or add a temporary property on the mismatched Document Type).  
2. Deploy that change from the source environment to the target (via Git push or the Umbraco Cloud Portal).  
3. Retry the content transfer/restore once the deployment completes.

---

**Quick fix when you can’t deploy from source**  
If you cannot deploy from the source environment, you can manually make the equivalent schema changes on the target environment to match the source. Ensure Document Types, Media Types, Data Types, Templates, and Dictionary items have the same aliases and structures as in the source before retrying the transfer.

---

**Fixing mismatches in aliases or names**  
If the mismatch is only in aliases or names, update those fields so they match exactly between environments. Aliases must be identical for the transfer to succeed. You can change aliases/names directly in the target environment if that is easier than deploying from the source.

---

**How to avoid schema mismatches in the future**  
Keep environments in sync before moving content. Always deploy schema changes from the environment where they were created (or ensure your Git workflow pushes those changes). Use the Umbraco Cloud Portal to confirm deployments are completed before running transfers or restores.

---

**Video tutorial**  
How to fix Schema mismatches: https://www.youtube.com/embed/MLJzV8ASWm4?rel=0