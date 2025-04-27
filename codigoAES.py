from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Clave e IV: deben ser de 16 bytes (AES-128 = 128 bits = 16 bytes)
key = b"SeguridadInforma"
iv = b"SeguridadInforma"

def encrypt_aes_cbc_hex(plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(plaintext.encode(), AES.block_size)
    encrypted = cipher.encrypt(padded)
    return encrypted.hex()

def decrypt_aes_cbc_hex(hex_input):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_bytes = bytes.fromhex(hex_input)
    decrypted = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)
    return decrypted.decode()

hex_input = "F55228945ACF1A291DB0C84409852406"

# Decodificar
decrypted_text = decrypt_aes_cbc_hex(hex_input)
print("Texto descifrado:", decrypted_text)
