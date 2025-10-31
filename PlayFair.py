def generate_key_matrix(key):
    key = key.lower().replace('j', 'i')
    unique = []
    for char in key:
        if char.isalpha() and char not in unique:
            unique.append(char)
    for char in 'abcdefghiklmnopqrstuvwxyz':
        if char not in unique:
            unique.append(char)
    return [unique[i:i+5] for i in range(0, 25, 5)]


def preprocess_text(text):
    text = text.lower().replace('j', 'i').replace(' ', '')
    i = 0
    pairs = []
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'x'
        if a == b:
            pairs.append((a, 'x'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2
    return pairs


def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)


def encrypt_pair(pair, matrix):
    a, b = pair
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)
    if r1 == r2:
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
    elif c1 == c2:
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]


def playfair_encrypt(plaintext, key):
    matrix = generate_key_matrix(key)
    print("Key Matrix:")
    for row in matrix:
        print(row)
    pairs = preprocess_text(plaintext)
    print("\nDigraphs:", pairs)
    encrypted = ''.join(encrypt_pair(pair, matrix) for pair in pairs)
    return encrypted.upper()


# Example usage
plaintext = "crypto is too easy"
key = "infosec"
ciphertext = playfair_encrypt(plaintext, key)
print("\nCiphertext:", ciphertext)
