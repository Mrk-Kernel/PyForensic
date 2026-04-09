# 🛡️ PyForensic - Digital Forensic Analyzer

A Python-based digital forensics tool built on Kali Linux.

## 🔧 Features
- 📁 File Metadata Extraction
- 🔐 Hash Generation (MD5, SHA1, SHA256)
- 🧙 Magic Bytes / File Type Checker
- 📷 EXIF Data Extractor
- 🔤 String Extractor
- 🗑️ Deleted File Scanner
- 📄 PDF Report Generator
- 🖥️ Interactive Menu Mode (no args needed)

## ⚙️ Installation
git clone https://github.com/Mrk-Kernel/PyForensic.git
cd PyForensic
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo apt install libmagic1 -y

## 🚀 Usage

### Interactive Mode (Recommended)
Simply run without any arguments:

  python3 main.py

You will get a menu with the following options:
  [1] Analyze a File
  [2] Scan Directory for Deleted Files
  [3] Analyze File + Generate PDF Report
  [4] Full Analysis (File + Scan + Optional Report)
  [0] Exit

### CLI Mode
For scripting or direct usage, pass arguments directly:

  # Analyze a file
  python3 main.py --file /path/to/file

  # Scan a directory for deleted/suspicious files
  python3 main.py --scan /path/to/folder

  # Analyze a file and generate PDF report
  python3 main.py --file /path/to/file --report

  # Analyze + scan + report in one command
  python3 main.py --file /path/to/file --scan /path/to/folder --report

## 📄 Report Output
PDF reports are saved to the reports/ folder:
  reports/forensic_report.pdf

## 🖥️ Platform
- Kali Linux

## 👤 Author
Mrk-Kernel
GitHub: https://github.com/Mrk-Kernel
