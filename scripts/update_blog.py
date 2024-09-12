import feedparser
import git
import os
import hashlib
from git.exc import GitCommandError
from googletrans import Translator

# Initialize the Google Translate API
translator = Translator()

# Velog RSS feed URL
rss_url = 'https://api.velog.io/rss/@becooq81'

# GitHub repository path
repo_path = '.'

# 'velog-posts' directory path
posts_dir = os.path.join(repo_path, '_posts')

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

# Define method to process titles
def process_title(title):
    title = title.replace('/', '-')  # Replace slash with hyphen
    title = title.replace('\\', '-')  # Replace backslash with hyphen
    title = title.replace(' ', '-')  # Replace space with hyphen
    title += '.md'
    return title

# Define method to create a unique identifier for content
def generate_content_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

# Track content hashes to avoid redundant uploads
processed_hashes = {}

# Save each post as a file and commit
for entry in feed.entries:
    
    # Detect the language of the title
    detected_language = translator.detect(entry.title).lang
    
    # Translate title to English if the detected language is Korean
    translated_title = entry.title  # Default to original title
    if detected_language == 'ko':
        translated_title = translator.translate(entry.title, src='ko', dest='en').text

    # Process translated title to create a valid filename
    translated_name = process_title(translated_title)
    
    # Create file path using the translated title
    file_path = os.path.join(posts_dir, translated_name)
    
    # Generate a hash of the original content
    content_hash = generate_content_hash(entry.description)

    # Check if this content hash has already been processed
    if content_hash in processed_hashes:
        # Skip to avoid redundant uploads
        print(f"Skipping already processed post: {entry.title}")
        continue
    
    # If content is new, mark it as processed
    processed_hashes[content_hash] = translated_name

    # Check if the file exists and if its content has changed
    content_changed = True
    new_content = entry.description
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            existing_content = file.read()
        if existing_content == new_content:
            content_changed = False
    
    # Create or overwrite the file only if content has changed
    if content_changed:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)  # Write the post content into the file

        # Stage and commit the changes
        repo.git.add(file_path)
        repo.git.commit('-m', f'Add or update post: {translated_name}')
        
# Push changes to repository
repo.git.push()
