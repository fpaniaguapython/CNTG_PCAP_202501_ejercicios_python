import hashlib

def get_hex_sha256_digest(texto):
    sha256_engine = hashlib.sha256()
    sha256_engine.update(texto.encode()) # str.encode(): Return the string encoded to bytes. Encoding defaults to 'utf-8'
    # print("Digest:",sha256_engine.digest())
    # print("Hex Digest:", sha256_engine.hexdigest())
    return sha256_engine.hexdigest()

def get_binary_sha256_digest(texto):
    sha256_engine = hashlib.sha256()
    sha256_engine.update(texto.encode())
    return sha256_engine.digest()