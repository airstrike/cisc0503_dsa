from datetime import datetime, timezone

import os
import re

def clean_coverage_files(directory):
    # Regex pattern to match the filenames
    pattern = re.compile(r'd_[0-9a-zA-Z]{16}_')
    timestamp_pattern = re.compile(r'(,\s*)?created at \d{4}-\d{2}-\d{2} \d{2}:\d{2} [-+]\d{4}\s*', re.DOTALL)
    timestamp_tag_pattern = re.compile(r'<p id="timestamp">.*?</p>')

    # Get the current timestamp
    current_timestamp = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M %z")
    new_timestamp_tag = f'<p id="timestamp">{current_timestamp}</p>'

    # First, rename the files
    for filename in os.listdir(directory):
        if pattern.match(filename):
            new_name = pattern.sub('', filename)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Renamed {filename} to {new_name}")

    # Aggressively replace links in HTML files
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                content = file.read()

            updated_content = pattern.sub('', content)
            updated_content = timestamp_pattern.sub('', updated_content)

            with open(os.path.join(directory, filename), 'w', encoding='utf-8') as file:
                file.write(updated_content)

    # Update the index.html file
    with open('./html/index.html', 'r', encoding='utf-8') as file:
        index_content = file.read()

    updated_index_content = timestamp_tag_pattern.sub(new_timestamp_tag, index_content)

    with open('./html/index.html', 'w', encoding='utf-8') as file:
        file.write(updated_index_content)

    # Replace patterns in status.json
    status_file = os.path.join(directory, 'status.json')
    if os.path.exists(status_file):
        with open(status_file, 'r', encoding='utf-8') as file:
            content = file.read()

        updated_content = pattern.sub('', content)

        with open(status_file, 'w', encoding='utf-8') as file:
            file.write(updated_content)

# Call the function with your coverage directory
clean_coverage_files('./html/coverage')
