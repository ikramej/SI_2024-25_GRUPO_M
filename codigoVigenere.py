# Alfabeto indicado (52 caracteres)
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_LEN = len(ALPHABET)


def vigenere_cipher(text, key, mode='encode'):
    result = ""
    key_length = len(key)
    key_indices = [ALPHABET.index(k) for k in key]

    for i, char in enumerate(text):
        if char in ALPHABET:
            text_index = ALPHABET.index(char)
            key_index = key_indices[i % key_length]

            if mode == 'encode':
                new_index = (text_index + key_index) % ALPHABET_LEN
            elif mode == 'decode':
                new_index = (text_index - key_index) % ALPHABET_LEN

            result += ALPHABET[new_index]
        else:
            result += char  # Por si hay caracteres fuera del alfabeto

    return result

cipher_text = "mvltykycmjfqlu"
key = "URJC"

# Decodificar
decoded = vigenere_cipher(cipher_text, key, mode='decode')
print("Texto descifrado:", decoded)

