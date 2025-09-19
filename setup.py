from setuptools import setup

setup(
    name="file-organizer",
    version="0.1.0",
    py_modules=["file_organizer"],  # because you have file_organizer.py
    install_requires=[
        "click",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "file-organizer=file_organizer:organize_files",
        ],
    },
    author="Tarun Kumar",
    description="A Python CLI tool to organize files by extension",
    long_description=open("README.md").read() if open("README.md", "r", encoding="utf-8") else "",
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
)
