ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cesar_cipher(text, shift):
    result = ""
    text = text.upper()

    for char in text:
        if char in ALPHABET:
            index = ALPHABET.index(char)
            new_index = (index + shift) % len(ALPHABET)
            result += ALPHABET[new_index]
        else:
            result += char

    return result

# Texto cifrado
cipher_text = "ROGZZ3P4O_Q1J3"
# Desplazamiento de -3 pero ponemos 3 para no cambiarlo dentro del algoritmo
shift = 3

# Descifrar
decoded_text = cesar_cipher(cipher_text, shift)
print("Texto descifrado:", decoded_text)
