
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

## ⚙️ Installation
git clone https://github.com/Mrk-Kernel/PyForensic.git
cd PyForensic
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo apt install libmagic1 -y

## 🚀 Usage
python3 main.py --file /path/to/file
python3 main.py --file /path/to/file --report
python3 main.py --scan /path/to/folder

## 🖥️ Platform
- Kali Linux

## 👤 Author
Mrk-Kernel
GitHub: https://github.com/Mrk-Kernel
