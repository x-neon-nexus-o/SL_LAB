def encrypt(text, s):
    result = ""
    # Traverse text
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():  # Explicitly check for lowercase
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            # Keep non-alphabet characters as is (spaces, numbers, symbols)
            result += char
    return result

# Check the function
text = "FAMT"
s = 4
print("Text : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))
