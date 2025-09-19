# 📂 File Organizer

![File Organizer Banner](assets/banner.png)

A simple yet powerful Python CLI tool to organize files in any directory by their extensions.  
Built with [Click](https://click.palletsprojects.com/) 🖱️ and [Rich](https://rich.readthedocs.io/) 🌈.

---

## ✨ Features

- 🗂️ Automatically organizes files into subfolders based on extensions  
- 🛠️ Supports **dry-run mode** (simulate without making changes)  
- 🔄 Handles duplicate filenames gracefully (`file_1.pdf`, `file_2.pdf`, …)  
- 🎨 Beautiful console output with **tables, colors, and progress bars**  
- 💻 Works on **Windows, macOS, and Linux**  

---

## 📦 Installation

### 1️⃣ Clone the repository


```bash
git clone https://github.com/coderdigi01/file-organizer.git

cd file-organizer

Install in editable mode
pip install -e .

UTF-8 Fix for Windows
set PYTHONUTF8=1

```
## Usage
``` bash
file-organizer C:\Users\YourName\Downloads --dry-run -v
