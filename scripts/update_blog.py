import feedparser
import git
import os
from git.exc import GitCommandError

# Velog RSS feed URL
rss_url = 'https://api.velog.io/rss/@becooq81'

# GitHub repository path
repo_path = '.'

# 'velog-posts' directory path
posts_dir = os.path.join(repo_path, 'velog-posts')

# Create 'velog-posts' if directory does not exist
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
    
    # Remove or replace invalid characters from file's name
    file_name = entry.title
    file_name = file_name.replace('/', '-')  # replace slash with hyphen
    file_name = file_name.replace('\\', '-')  # replace back slash with hyphen
    
    # Replace any additional characters if necessary
    file_name += '.md'
    file_path = os.path.join(posts_dir, file_name)
    
    # Create file if not exists
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)  # Write contents into file
        
        # Commit on GitHub
        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title}')
        
# Push changes to repository
repo.git.push()
