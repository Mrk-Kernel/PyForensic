import exifread

def get_exif(filepath):
    try:
        with open(filepath, "rb") as f:
            tags = exifread.process_file(f, stop_tag="UNDEF", details=False)
        
        if not tags:
            return {"info": "No EXIF data found"}
        
        result = {}
        for tag, value in tags.items():
            result[tag] = str(value)
        return result
    
    except Exception as e:
        return {"error": str(e)}
