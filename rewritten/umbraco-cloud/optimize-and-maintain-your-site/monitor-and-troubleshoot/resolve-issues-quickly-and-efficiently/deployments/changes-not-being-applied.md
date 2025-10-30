**Deployments complete but no changes appear in Umbraco Cloud**  
If deployments finish but no changes are applied, custom Config Transforms may be failing during data extraction. This happens when you have added custom transforms to your project and one or more is invalid or incompatible (../../../../build-and-customize-your-solution/set-up-your-project/project-settings/config-transforms.md).

Config Transforms run on every data extraction, so the issue will persist until the transform files are corrected or removed. The Umbraco Cloud Portal typically will not show an error for this; you need to check Kudu.

Links: Config Transforms (../../../../build-and-customize-your-solution/set-up-your-project/project-settings/config-transforms.md)

---

**Confirming a config transform failure in Kudu**  
Use Kudu on the affected environment to verify whether a transform failed (../../power-tools/).

- Open Kudu (../../power-tools/) and go to site > deployments.  
- Find the latest deployment folder (use the active file to identify the current deployment ID).  
- If the folder only contains log.log and status.xml (and is missing commits.uc and manifest), an error occurred.  
- Open log.log and search for XmlTransform entries or errors like "'xdt' is an undeclared prefix".

Links: Kudu (../../power-tools/)

---

**Fixing a failed config transform**  
- Identify the transform file referenced in log.log and ensure the XML is valid. Use an XML validator such as https://www.xmlvalidation.com/.  
- Update the transform file in your local solution and deploy to Cloud.  
- Run a Schema Deployment From Data File to re-extract the previously deployed schema (../../../../build-and-customize-your-solution/handle-deployments-and-environments/deployment/deploy-dashboard.md#deploy-operations).

Links: XML validator (https://www.xmlvalidation.com/), Deploy operations (../../../../build-and-customize-your-solution/handle-deployments-and-environments/deployment/deploy-dashboard.md#deploy-operations)

---

**Why this happens and how to avoid it**  
Invalid or misconfigured Config Transforms block the extraction process, so schema and content changes are not applied even though the deployment completes. This can surface as warnings when pushing from local, but Cloud often only shows it in Kudu logs.

Validate and test your transform files before committing. Ensure the Kudu deployment folder for the latest deployment includes commits.uc and manifest along with log.log and status.xml.