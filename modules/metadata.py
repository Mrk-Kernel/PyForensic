import os
import time

def get_metadata(filepath):
    if not os.path.exists(filepath):
        return {"error": "File not found"}
    
    stat = os.stat(filepath)
    return {
        "File Name"     : os.path.basename(filepath),
        "File Size"     : f"{stat.st_size} bytes",
        "Created"       : time.ctime(stat.st_ctime),
        "Modified"      : time.ctime(stat.st_mtime),
        "Last Accessed" : time.ctime(stat.st_atime),
        "Permissions"   : oct(stat.st_mode),
        "Owner UID"     : stat.st_uid,
    }
