**PathTooLongException during transfers or restores in Umbraco Cloud**

If content transfers or restores fail in Umbraco Cloud with a PathTooLongException, one or more media files likely have names that are too long. Media items with file names longer than 80 characters can cause deployment failures between Cloud environments.

The error typically blocks the operation until the long-named media files are corrected.

---

**What the error looks like**

You may see an error similar to: System.IO.PathTooLongException: The specified path, file name, or both are too long. The fully qualified file name must be less than 260 characters, and the directory name must be less than 248 characters.

This is due to Windows path length limits combined with long media file names stored in Umbraco.

---

**Why this happens (long paths and filename limits)**

Windows enforces path length limits (generally 260 characters for a full path). In Umbraco Cloud, media file names longer than 80 characters can lead to paths that exceed these limits during deployment, resulting in a PathTooLongException.

Shortening media file names prevents paths from exceeding the OS limits and allows deployments to complete.

---

**Identify media items with overly long paths**

Connect to your Live environment database to locate problematic media. Instructions for connecting are here: ../../../../build-and-customize-your-solution/set-up-your-project/databases/cloud-database/local-database.md#connecting-to-your-local-umbraco-installation

Run this SQL query to list media entries with long paths:
SELECT TOP (2000) [id],
[path],
LEN(path) AS valueLength
FROM [dbo].[umbracoMediaVersion]
WHERE LEN(path) > 80
AND path IS NOT NULL
ORDER BY LEN(path) DESC;

Use the returned ids or paths to find the corresponding media items in the Umbraco backoffice.

---

**Fix the issue by renaming and re-uploading media**

In the Umbraco backoffice, locate each reported media item, note where it’s used in content, and remove it. Rename the original file so the file name is 80 characters or fewer, then re-upload it to Media.

After re-adding the media, update any content that referenced the old item to point to the new media. This resolves the path length issue and allows transfers or restores to proceed.