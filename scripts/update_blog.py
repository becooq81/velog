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

# File to store original titles to translated title mappings
translation_cache_path = os.path.join(repo_path, 'title_translation_cache.json')

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

# Load the translation cache if it exists
if os.path.exists(translation_cache_path):
    with open(translation_cache_path, 'r', encoding='utf-8') as cache_file:
        translation_cache = json.load(cache_file)
else:
    translation_cache = {}

# Save each post as a file and commit
for entry in feed.entries:
    
    # Check if the title has already been translated and cached
    if entry.title in translation_cache:
        translated_title = translation_cache[entry.title]
    else:
        # Detect the language of the title
        detected_language = translator.detect(entry.title).lang
        
        # Translate title to English if needed
        translated_title = entry.title  # Default to original title
        if detected_language == 'ko':  # Assuming title is in Korean
            translated_title = translator.translate(entry.title, src='ko', dest='en').text
        
        # Cache the translation to ensure consistency across runs
        translation_cache[entry.title] = translated_title

    # Process translated title to create a valid filename
    translated_name = process_title(translated_title)
    
    # Create file path using the translated title
    file_path = os.path.join(posts_dir, translated_name)
    
    # Generate a hash of the original content
    content_hash = generate_content_hash(entry.description)

    # Check if the post (by translated title) has already been processed
    if translated_name in processed_hashes:
        # If the content has not changed, skip the update
        if processed_hashes[translated_name] == content_hash:
            print(f"Skipping unchanged post: {translated_title}")
            continue
    else:
        print(f"Processing new or updated post: {translated_title}")

    # If content is new or updated, mark it as processed
    processed_hashes[translated_name] = content_hash

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
        repo.git.commit('-m', f'Add or update post: {translated_title}')
        
# Push changes to repository
repo.git.push()

# Save the updated processed hashes to file
with open(hash_file_path, 'w', encoding='utf-8') as hash_file:
    json.dump(processed_hashes, hash_file, ensure_ascii=False, indent=4)

# Save the updated title translation cache to file
with open(translation_cache_path, 'w', encoding='utf-8') as cache_file:
    json.dump(translation_cache, cache_file, ensure_ascii=False, indent=4)
