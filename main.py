import argparse
import os
import sys
from colorama import Fore, Style, init
from modules.metadata         import get_metadata
from modules.hasher           import hash_file
from modules.magic_checker    import check_magic
from modules.exif_extractor   import get_exif
from modules.string_extractor import extract_strings
from modules.deleted_scanner  import scan_deleted
from modules.reporter         import generate_report

init(autoreset=True)

# ─────────────────────────────────────────────
#  BANNER
# ─────────────────────────────────────────────
def banner():
    print(Fore.CYAN + """
██████╗ ██╗   ██╗███████╗ ██████╗ ██████╗ ███████╗███╗   ██╗███████╗██╗ ██████╗
██╔══██╗╚██╗ ██╔╝██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██║██╔════╝
██████╔╝ ╚████╔╝ █████╗  ██║   ██║██████╔╝█████╗  ██╔██╗ ██║███████╗██║██║
██╔═══╝   ╚██╔╝  ██╔══╝  ██║   ██║██╔══██╗██╔══╝  ██║╚██╗██║╚════██║██║██║
██║        ██║   ██║     ╚██████╔╝██║  ██║███████╗██║ ╚████║███████║██║╚██████╗
╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝
    """ + Style.RESET_ALL)
    print(Fore.YELLOW + "        🔍 Digital File & Disk Forensic Analyzer  |  By: Mrk-Kernel\n")
    print(Fore.WHITE + "─" * 80 + Style.RESET_ALL)

# ─────────────────────────────────────────────
#  PRINT SECTION
# ─────────────────────────────────────────────
def print_section(title, data):
    print(Fore.GREEN + f"\n{'─'*60}")
    print(Fore.GREEN + f"  {title}")
    print(Fore.GREEN + f"{'─'*60}" + Style.RESET_ALL)
    if isinstance(data, dict):
        for k, v in data.items():
            print(f"  {Fore.CYAN}{k:<25}{Style.RESET_ALL}: {v}")
    elif isinstance(data, list):
        for item in data:
            print(f"  {Fore.WHITE}- {item}{Style.RESET_ALL}")
    else:
        print(f"  {data}")

# ─────────────────────────────────────────────
#  CORE ANALYSIS
# ─────────────────────────────────────────────
def analyze_file(filepath, make_report=False):
    if not os.path.exists(filepath):
        print(Fore.RED + f"\n  [✗] File not found: {filepath}")
        return

    print(Fore.YELLOW + f"\n  [*] Analyzing: {filepath}")
    all_data = {}

    meta = get_metadata(filepath)
    print_section("📁  File Metadata", meta)
    all_data["File Metadata"] = meta

    hashes = hash_file(filepath)
    print_section("🔐  File Hashes", hashes)
    all_data["File Hashes"] = hashes

    magic_info = check_magic(filepath)
    print_section("🧙  Magic Bytes / File Type", magic_info)
    all_data["File Type"] = magic_info

    exif = get_exif(filepath)
    print_section("📷  EXIF Data", exif)
    all_data["EXIF Data"] = exif

    strings = extract_strings(filepath)
    print_section("🔤  Extracted Strings", {"Total Strings Found": strings["Total Strings Found"]})
    all_data["Strings"] = {"Total Found": strings["Total Strings Found"]}

    if make_report:
        os.makedirs("reports", exist_ok=True)
        generate_report(all_data)

    return all_data


def scan_directory(directory):
    if not os.path.isdir(directory):
        print(Fore.RED + f"\n  [✗] Directory not found: {directory}")
        return

    deleted = scan_deleted(directory)
    print_section("🗑️   Deleted / Suspicious File Scan", {
        "Directory Scanned"     : deleted.get("Directory Scanned", directory),
        "Suspicious Files Found": deleted.get("Suspicious Files Found", 0),
    })
    files = deleted.get("Files", [])
    if files:
        print(Fore.YELLOW + "\n  Suspicious Files:")
        for f in files:
            print(f"    {Fore.RED}- {f}{Style.RESET_ALL}")
    else:
        print(Fore.GREEN + "\n  No suspicious files found ✅")

    return deleted

# ─────────────────────────────────────────────
#  INTERACTIVE MENU
# ─────────────────────────────────────────────
def interactive_menu():
    while True:
        print(Fore.CYAN + "\n  ┌─────────────────────────────────────┐")
        print(Fore.CYAN +   "  │           MAIN MENU                 │")
        print(Fore.CYAN +   "  ├─────────────────────────────────────┤")
        print(Fore.WHITE +  "  │  [1]  Analyze a File                │")
        print(Fore.WHITE +  "  │  [2]  Scan Directory (Deleted Files) │")
        print(Fore.WHITE +  "  │  [3]  Analyze File + Generate Report │")
        print(Fore.WHITE +  "  │  [4]  Full Analysis (File + Scan)    │")
        print(Fore.RED   +  "  │  [0]  Exit                          │")
        print(Fore.CYAN  +  "  └─────────────────────────────────────┘" + Style.RESET_ALL)

        choice = input(Fore.YELLOW + "\n  pyforensic> " + Style.RESET_ALL).strip()

        if choice == "1":
            filepath = input(Fore.WHITE + "  Enter file path: " + Style.RESET_ALL).strip()
            analyze_file(filepath, make_report=False)

        elif choice == "2":
            directory = input(Fore.WHITE + "  Enter directory path: " + Style.RESET_ALL).strip()
            scan_directory(directory)

        elif choice == "3":
            filepath = input(Fore.WHITE + "  Enter file path: " + Style.RESET_ALL).strip()
            os.makedirs("reports", exist_ok=True)
            analyze_file(filepath, make_report=True)

        elif choice == "4":
            filepath  = input(Fore.WHITE + "  Enter file path: "      + Style.RESET_ALL).strip()
            directory = input(Fore.WHITE + "  Enter directory to scan: " + Style.RESET_ALL).strip()
            data = analyze_file(filepath, make_report=False)
            scan_directory(directory)
            gen = input(Fore.YELLOW + "\n  Generate PDF report? (y/n): " + Style.RESET_ALL).strip().lower()
            if gen == "y" and data:
                os.makedirs("reports", exist_ok=True)
                generate_report(data)

        elif choice == "0":
            print(Fore.CYAN + "\n  [*] Goodbye! Stay forensic 🔍\n")
            sys.exit(0)

        else:
            print(Fore.RED + "  [!] Invalid option. Try again.")

        input(Fore.WHITE + "\n  Press Enter to return to menu..." + Style.RESET_ALL)

# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────
def main():
    banner()

    parser = argparse.ArgumentParser(
        description="PyForensic - Digital Forensic Analyzer",
        epilog="Run without arguments to enter interactive mode."
    )
    parser.add_argument("--file",   help="Path to file to analyze")
    parser.add_argument("--scan",   help="Directory to scan for deleted files")
    parser.add_argument("--report", action="store_true", help="Generate PDF report")
    args = parser.parse_args()

    # ── CLI mode ──────────────────────────────
    if args.file or args.scan:
        all_data = {}

        if args.file:
            data = analyze_file(args.file, make_report=False)
            if data:
                all_data.update(data)

        if args.scan:
            deleted = scan_directory(args.scan)
            if deleted:
                all_data["Deleted Files"] = deleted

        if args.report and all_data:
            os.makedirs("reports", exist_ok=True)
            generate_report(all_data)

    # ── Interactive mode ──────────────────────
    else:
        print(Fore.YELLOW + "  No arguments provided — launching interactive mode.\n")
        interactive_menu()


if __name__ == "__main__":
    main()
