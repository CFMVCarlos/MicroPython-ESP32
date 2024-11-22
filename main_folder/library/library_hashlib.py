import binascii
import hashlib

# Example data
data = b"Hello, world!"

# Creating SHA256 hash object
sha256_hash = hashlib.sha256()
# Feeding data into the hash object
sha256_hash.update(data)
# Obtaining the digest (hash) in bytes
sha256_digest = sha256_hash.digest()
# Obtaining the hexadecimal representation of the digest
sha256_hexdigest = binascii.hexlify(sha256_digest)

print("SHA256 digest (bytes):", sha256_digest)
print("SHA256 hexdigest:", sha256_hexdigest)

# Creating SHA1 hash object
sha1_hash = hashlib.sha1()
sha1_hash.update(data)
sha1_digest = sha1_hash.digest()
sha1_hexdigest = binascii.hexlify(sha1_digest)

print("\nSHA1 digest (bytes):", sha1_digest)
print("SHA1 hexdigest:", sha1_hexdigest)

# Creating MD5 hash object
md5_hash = hashlib.md5()
md5_hash.update(data)
md5_digest = md5_hash.digest()
md5_hexdigest = binascii.hexlify(md5_digest)

print("\nMD5 digest (bytes):", md5_digest)
print("MD5 hexdigest:", md5_hexdigest)
