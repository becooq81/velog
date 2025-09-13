import feedparser
import git
import os
import hashlib
import json
from googletrans import Translator

# Initialize the Google Translate API
translator = Translator()

# Velog RSS feed URL
rss_url = 'https://api.velog.io/rss/@becooq81'

# GitHub repository path
repo_path = '.'

# 'velog-posts' directory path
posts_dir = os.path.join(repo_path, 'velog-posts')

# File to store processed content hashes
hash_file_path = os.path.join(repo_path, 'processed_hashes.json')

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
    title = title.replace('.', '')  # Remove periods
    title = title.replace(',', '')  # Remove commas
    title += '.md'
    return title

# Define method to create a unique identifier for content
def generate_content_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

# Load the processed hashes from file if it exists
if os.path.exists(hash_file_path):
    with open(hash_file_path, 'r', encoding='utf-8') as hash_file:
        processed_hashes = json.load(hash_file)
else:
    processed_hashes = {}

# Track whether there are new or updated posts
has_changes = False

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
    has_changes = True

    # Create or overwrite the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(entry.description)

    # Stage the changes
    repo.git.add(file_path)
    print(f"Staged post: {translated_name}")

# Commit and push only if there were changes
if has_changes:
    repo.git.commit('-m', 'Add or update new Velog posts')
    repo.git.push()
    print("Changes pushed to repository.")
else:
    print("No new posts to update.")

# Save the updated processed hashes to file
with open(hash_file_path, 'w', encoding='utf-8') as hash_file:
    json.dump(processed_hashes, hash_file, ensure_ascii=False, indent=4)
