import feedparser
import git
import os
import urllib.parse  # Import URL encoding library
from git.exc import GitCommandError

# Velog RSS feed URL
rss_url = 'https://api.velog.io/rss/@becooq81'

# GitHub repository path
repo_path = '.'

# '_posts' directory path
posts_dir = os.path.join(repo_path, '_posts')

# Create '_posts' if directory does not exist
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# Load repository
repo = git.Repo(repo_path)

# Double check git configuration
repo.git.config('--global', 'user.name', 'github-actions[bot]')
repo.git.config('--global', 'user.email', 'github-actions[bot]@users.noreply.github.com')

# Parse RSS feed
feed = feedparser.parse(rss_url)

# Save each post as a file and commit
for entry in feed.entries:
    # URL-encode the title to create a valid file name
    # Ensure that the title is encoded using UTF-8
    file_name = urllib.parse.quote(entry.title.encode('utf-8'))
    file_name += '.md'
    file_path = os.path.join(posts_dir, file_name)

    # Create file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            # Properly escape special characters in the title
            escaped_title = entry.title.replace(':', '&#58;').replace("'", '&#39;').replace('"', '&quot;')
            
            # Add front matter with escaped title
            front_matter = f"---\n"
            front_matter += f'title: "{escaped_title}"\n'
            front_matter += f"date: {entry.published}\n"
            front_matter += f"---\n\n"
            content = entry.description
            file.write(front_matter + content)  # Write contents into file

        # Commit on GitHub
        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title}')

# Push changes to repository
repo.git.push()
