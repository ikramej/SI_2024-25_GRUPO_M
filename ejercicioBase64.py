import base64

def encode_base64(text):
    # Codifica el texto (str) a Base64
    text_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(text_bytes)
    return base64_bytes.decode('utf-8')

def decode_base64(encoded_text):
    # Decodifica texto en Base64 a texto normal
    base64_bytes = encoded_text.encode('utf-8')
    text_bytes = base64.b64decode(base64_bytes)
    return text_bytes.decode('utf-8')


base64_input = "VVJKQ3tTTTRMTF9CNFMzXzY0fQ=="
decoded_text = decode_base64(base64_input)

print("Texto decodificado:", decoded_text)
