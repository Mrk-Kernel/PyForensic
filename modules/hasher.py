import hashlib
def hash_file(filepath):
    hashes = {}
    algorithms = ["md5", "sha1", "sha256"]
    
    try:
        with open(filepath, "rb") as f:
            data = f.read()
            for algo in algorithms:
                h = hashlib.new(algo)
                h.update(data)
                hashes[algo.upper()] = h.hexdigest()
    except Exception as e:
        return {"error": str(e)}
    
    return hashes
