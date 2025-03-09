![Total Commit Days](https://img.shields.io/badge/total_commit_days-52-blue?cache=1741482820)
![Weekly Commit Days](https://img.shields.io/badge/weekly_commit_days-1-green?cache=1741482820)
# Velog


## Overview

This repository contains a Python script for automatically updating a blog with posts from a Velog RSS feed. The script fetches new posts from the RSS feed and saves them as Markdown files in the repository. It then commits and pushes these updates to GitHub.

The content of this repository is based on [rimgosu/velog](https://github.com/rimgosu/velog), with modifications made for improved readability and features.

## Features

- **Fetches Posts**: Retrieves posts from a Velog RSS feed.
- **Translates Titles**: Translates Korean titles to English based on Google Translate (Saves original title with hash to avoid duplicate posts)
- **Saves as Markdown**: Converts the posts to Markdown files.
- **Automatic Updates**: Scheduled to run daily to check for new posts.
- **Commits and Pushes**: Commits new posts and pushes changes to GitHub.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/becooq81/velog.git
cd velog
```

### 2. Configure the RSS Feed
Edit the `scripts/update_blog.py` file to set the RSS feed URL for your Velog blog. Update the `rss_url` variable with your feed URL.

### 3. Set Up GitHub Actions

To automate updates, configure GitHub Actions:

1. **Enable GitHub Actions Bot to write in your Repository**: Repository's Settings > Actions > General > Workflow Permissions > Choose 'Read and Write permissions'.
2. **Create a Personal Access Token (PAT)**: GitHub > Settings > Developer Settings > Personal access Tokens > Generate new token. Grant write packages privileges to the token. (Do not close the tab unless you completed the following steps. You cannot see the PAT again.)
3. **Add the PAT to Repository Secrets**: In your Velog GitHub repository, navigate to Settings > Secrets and Variables > Actions and add a new secret named GH_PAT with your PAT.
4. **Verify Workflow Configuration**: Ensure that the GitHub Actions workflow is configured correctly in `.github/workflows/update_blog.yml`.

## GitHub Actions Workflow
The provided GitHub Actions workflow is configured to run daily at midnight and performs the following steps:

1. **Checkout**: Checks out the repository.
2. **Set Up Python**: Installs Python and dependencies.
3. **Run the Update Script**: Executes the update_blog.py script.
4. **Commit Changes**: Commits new posts if any changes are detected.
5. **Push Changes**: Pushes the commits to the GitHub repository.
