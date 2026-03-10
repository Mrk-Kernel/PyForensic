import magic
import os

def check_magic(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    
    try:
        detected_type = magic.from_file(filepath, mime=True)
        description   = magic.from_file(filepath)
        return {
            "File Extension"  : ext if ext else "None",
            "Detected MIME"   : detected_type,
            "Description"     : description,
            "Extension Match" : "✅ MATCH" if ext[1:] in detected_type else "⚠️ MISMATCH - Possible disguise!"
        }
    except Exception as e:
        return {"error": str(e)}
