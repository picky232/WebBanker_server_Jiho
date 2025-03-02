import hashlib


def Hashing(data):
    # SHA-256 해싱
    hashed = hashlib.sha256(data.encode()).hexdigest()

    return hashed