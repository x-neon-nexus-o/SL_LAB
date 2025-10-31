import hashlib

def generate_sha1(message):
    sha1_hash=hashlib.sha1()
    sha1_hash.update(message.encode("utf-8"))
    return sha1_hash.hexdigest()

text=input("Enter text to hash using SHA-1:")
sha1_result=generate_sha1(text)
print("Original Text",text)
print("SHA-1 Hash:",sha1_result)