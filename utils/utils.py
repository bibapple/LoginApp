import hashlib


def hash_code(original, salt="LoginApp"):
    h = hashlib.sha256()
    original += salt
    h.update(original.encode())
    return h.hexdigest()

