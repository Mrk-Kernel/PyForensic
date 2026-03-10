import argparse
from colorama import Fore, Style, init
from modules.metadata       import get_metadata
from modules.hasher         import hash_file
from modules.magic_checker  import check_magic
from modules.exif_extractor import get_exif
from modules.string_extractor import extract_strings
from modules.deleted_scanner  import scan_deleted
from modules.reporter         import generate_report

init(autoreset=True)

def banner():
    print(Fore.CYAN + """
██████╗ ██╗   ██╗███████╗ ██████╗ ██████╗ ███████╗███╗   ██╗███████╗██╗ ██████╗
██╔══██╗╚██╗ ██╔╝██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██║██╔════╝
██████╔╝ ╚████╔╝ █████╗  ██║   ██║██████╔╝█████╗  ██╔██╗ ██║███████╗██║██║     
██╔═══╝   ╚██╔╝  ██╔══╝  ██║   ██║██╔══██╗██╔══╝  ██║╚██╗██║╚════██║██║██║     
██║        ██║   ██║     ╚██████╔╝██║  ██║███████╗██║ ╚████║███████║██║╚██████╗
╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝
    """ + Style.RESET_ALL)
    print(Fore.YELLOW + "        🔍 Digital File & Disk Forensic Analyzer | By: You\n")

def print_section(title, data):
    print(Fore.GREEN + f"\n{'='*50}")
    print(Fore.GREEN + f"  {title}")
    print(Fore.GREEN + f"{'='*50}" + Style.RESET_ALL)
    if isinstance(data, dict):
        for k, v in data.items():
            print(f"  {Fore.CYAN}{k:<25}{Style.RESET_ALL}: {v}")
    elif isinstance(data, list):
        for item in data:
            print(f"  - {item}")

def main():
    banner()
    parser = argparse.ArgumentParser(description="PyForensic - File Forensic Analyzer")
    parser.add_argument("--file",   help="Path to file to analyze")
    parser.add_argument("--scan",   help="Directory to scan for deleted files")
    parser.add_argument("--report", action="store_true", help="Generate PDF report")
    args = parser.parse_args()

    all_data = {}

    if args.file:
        print(Fore.YELLOW + f"\n[*] Analyzing: {args.file}")

        meta = get_metadata(args.file)
        print_section("📁 File Metadata", meta)
        all_data["File Metadata"] = meta

        hashes = hash_file(args.file)
        print_section("🔐 File Hashes", hashes)
        all_data["File Hashes"] = hashes

        magic_info = check_magic(args.file)
        print_section("🧙 Magic Bytes / File Type", magic_info)
        all_data["File Type"] = magic_info

        exif = get_exif(args.file)
        print_section("📷 EXIF Data", exif)
        all_data["EXIF Data"] = exif

        strings = extract_strings(args.file)
        print_section("🔤 Extracted Strings", {"Total Found": strings["Total Strings Found"]})
        all_data["Strings"] = {"Total Found": strings["Total Strings Found"]}

    if args.scan:
        deleted = scan_deleted(args.scan)
        print_section("🗑️ Deleted File Scan", deleted)
        all_data["Deleted Files"] = deleted

    if args.report and all_data:
        generate_report(all_data)

if __name__ == "__main__":
    main()
