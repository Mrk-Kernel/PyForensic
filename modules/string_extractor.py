def extract_strings(filepath, min_length=4):
    strings_found = []
    
    try:
        with open(filepath, "rb") as f:
            data = f.read()
        
        current = ""
        for byte in data:
            char = chr(byte)
            if char.isprintable() and char != ' ':
                current += char
            else:
                if len(current) >= min_length:
                    strings_found.append(current)
                current = ""
        
        return {
            "Total Strings Found": len(strings_found),
            "Strings": strings_found[:100]  # Show first 100
        }
    except Exception as e:
        return {"error": str(e)}
