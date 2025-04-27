def xor_cipher(text, key):
    result = ""
    key_length = len(key)

    for i, char in enumerate(text):
        xor_char = chr(ord(char) ^ ord(key[i % key_length]))
        result += xor_char

    return result


cipher_text = "({!+8b*+"
key = "XOR"

# Descifrar
decoded = xor_cipher(cipher_text, key)
print("Texto descifrado:", decoded)

