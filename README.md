# 📂 File Organizer

A Python CLI tool to organize files by their extensions.  
Built with [Click](https://click.palletsprojects.com/) and [Rich](https://rich.readthedocs.io/).

---

## ✨ Features
- Organizes files in a directory by extension
- Creates subfolders like `pdf`, `jpg`, `zip`, etc.
- Supports **dry-run mode** (no changes, just preview)
- Handles duplicate filenames automatically (`file_1.pdf`, `file_2.pdf`, …)
- Beautiful output with progress bars and tables (powered by Rich)

---

## 📦 Installation

Clone this repository and install locally in editable mode:

```bash
git clone https://github.com/YOUR-USERNAME/file-organizer.git
cd file-organizer
pip install -e .

---
## Tell Python to use UTF-8
Run Python with UTF-8 mode:

```bash
set PYTHONUTF8=1
