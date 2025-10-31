import hashlib

def generate_md5(message):
    md5_hash=hashlib.md5()
    md5_hash.update(message.encode("utf-8"))
    return md5_hash.hexdigest()

text=input("Enter text to hash using MD5:")
md5_result=generate_md5(text)
print("Original Text",text)
print("MD5 Hash:",md5_result)