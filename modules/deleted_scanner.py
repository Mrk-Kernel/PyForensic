import os

def scan_deleted(directory):
    found = []
    
    # Scan for common temp/hidden deleted file patterns
    patterns = [".Trash", ".deleted", "~", ".tmp"]
    
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                for pattern in patterns:
                    if file.endswith(pattern) or file.startswith("."):
                        full_path = os.path.join(root, file)
                        found.append(full_path)
        
        return {
            "Directory Scanned": directory,
            "Suspicious Files Found": len(found),
            "Files": found
        }
    except Exception as e:
        return {"error": str(e)}
