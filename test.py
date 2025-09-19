import os

# Folder where test files will be created
TEST_DIR = "test_files"

# Make the directory if it doesn't exist
os.makedirs(TEST_DIR, exist_ok=True)

# List of test files with different extensions
files = [
    "document1.pdf",
    "document2.pdf",
    "image1.jpg",
    "image2.jpg",
    "image3.png",
    "script1.py",
    "script2.py",
    "archive1.zip",
    "archive2.zip",
    "notes.txt",
    "readme.md"
]

# Create empty files
for file_name in files:
    file_path = os.path.join(TEST_DIR, file_name)
    with open(file_path, "w") as f:
        f.write(f"Test content for {file_name}\n")

print(f"Created {len(files)} test files in '{TEST_DIR}' folder.")
