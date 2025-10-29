**Understanding Umbraco Cloud Environments**  
Umbraco Cloud environments serve as workspaces and Git repositories for developing, building, and publishing websites. In projects with multiple environments, each environment acts as a branch from the main repository. This structure facilitates the movement of both content and structure files between environments. For more details, refer to the Deployment section.

---

**Types of Environments in Umbraco Cloud**  
There are two main types of environments in Umbraco Cloud: **Mainline Environments** and **Flexible Environments**. The mainline environment serves as the root deployment pipeline for managing code and content flow. The left-most mainline environment, also known as the Development environment, connects to your local machine using Git, while the right-most environment is typically the Live or Production environment. Flexible environments branch off from mainline environments, allowing for independent development workflows.

---

**Environment Components**  
Each Umbraco Cloud environment includes both a Git repository and a live site folder, located at `/site/wwwroot/`. When changes are pushed from the local machine to the Git repository at `/site/repository/`, they are subsequently copied to the live site. Configuration settings are managed using an `appSettings.json` file, which can be tailored for each environment.

---

**Setting Up Configuration Files**  
To establish specific configurations for different environments, duplicate the `appSettings.json` file and rename it to `appSettings.{EnvironmentAlias}.json`, where `EnvironmentAlias` is derived from the `DOTNET_ENVIRONMENT` variable. This variable can be found in the Environment Variables section of Kudu on the environment. Further details are provided in the ASP.NET Configuration documentation.

---

**Team Management in Environments**  
Team members added through the Umbraco Cloud Portal become backoffice users in your environments. Users can also be added directly in the backoffice, although they won't have deployment capabilities between environments. Additional information can be found in the Team Members article.

---

**Database Structure in Umbraco Cloud**  
Each environment within Umbraco Cloud is equipped with its SQL Azure database. You have comprehensive access to these databases, allowing for the creation of custom tables. Instructions on connecting to your Umbraco Cloud databases are available in the Database article.

---

**Using Kudu (Power Tools)**  
Kudu serves as a dashboard for browsing and editing files within your environments. It is advisable to use Kudu only when following specific guides. More information on accessing and utilizing Kudu can be found in the Power Tools article.

---

**Accessing Environment History**  
Every Umbraco Cloud environment features a Git repository and its associated Git history. This history can be viewed in a simplified format within the Cloud Portal under the **History** option, accessible through the action menu for each environment. Here, users can examine file changes made within the environment.