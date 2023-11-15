import os
import re

def clean_coverage_files(directory):
    # Regex pattern to match the filenames
    pattern = re.compile(r'd_[0-9a-zA-Z]{16}_')

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

            with open(os.path.join(directory, filename), 'w', encoding='utf-8') as file:
                file.write(updated_content)

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
