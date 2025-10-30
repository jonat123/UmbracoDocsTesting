**Understanding schema mismatches in Umbraco Cloud**  
Schema mismatches occur when the schema in your source environment does not match the schema in your target environment during a content transfer or restore. Schema includes Document Types, Media Types, Data Types, Templates, and Dictionary items.  
The error message will list the specific items that are out of sync, so you can identify what needs updating.

---

**Fixing schema mismatch errors during transfer or restore**  
First, check for pending deployments in your source environment. If you are working locally, commit and push any schema changes through Git. If you are transferring between two Umbraco Cloud environments, use the Umbraco Cloud Portal to view and deploy pending changes.  
If there are no pending deployments, resolve the mismatch by updating the schema in the source environment and deploying it to the next environment:
- Make a minor change to the mismatched schema item in the source environment (for example, the specific Document Type listed in the error).
- Deploy the change to the target environment to bring schemas back in sync.

Example error message image: images/schema-mismatch-on-transfer_v10.png

---

**Resolving alias or name mismatches**  
If the mismatches are due to differences in aliases or names, align them manually on the target environment. Once the aliases or names match, retry the content transfer or restore.

---

**Avoiding schema mismatches in future**  
Before transferring or restoring content, ensure both environments have the same schema. Deploy all schema changes from the source environment first.  
Use the Umbraco Cloud Portal to confirm there are no pending deployments, and always commit and push local schema changes before attempting a transfer.

---

**Additional resources**  
Watch the walkthrough: https://www.youtube.com/embed/MLJzV8ASWm4?rel=0  
Example error message image: images/schema-mismatch-on-transfer_v10.png