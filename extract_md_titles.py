import os
import json

docs_dir = "data/docs"
index_file = "data/docs/index.json"
index_data = {}

# Ensure the directory exists
if not os.path.exists(docs_dir):
    print(f"Directory {docs_dir} does not exist.")
    exit(1)

# Process each Markdown file
for filename in os.listdir(docs_dir):
    if filename.endswith(".md"):
        file_path = os.path.join(docs_dir, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith("# "):  # Extract first H1 header
                    index_data[filename] = line.strip("# ").strip()
                    break

# Save the index.json file
with open(index_file, "w", encoding="utf-8") as json_file:
    json.dump(index_data, json_file, indent=4)

print(f"Index file created at {index_file}")
