from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# AES-GCM --> (Datos Asociados + Datos a cifrar) + key + nonce

texto_gcm_bytes = bytes("Pense que este ejercicio seria mas dificil", "utf-8")
key_bytes  = bytes.fromhex('E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74')
#nonce_bytes = get_random_bytes(8)
nonce_bytes = bytes.fromhex('39561c9c7bf97b9c9121d2d59a9121d2')
print("Nonce hex=", nonce_bytes.hex())
datos_asociados_bytes = bytes("Ejercicio 12","utf-8")
cifrador = AES.new(key_bytes,AES.MODE_GCM,nonce=nonce_bytes)
cifrador.update(datos_asociados_bytes)
texto_cifrado_bytes,mac_bytes = cifrador.encrypt_and_digest(texto_gcm_bytes)
print("Texto cifrado:", texto_cifrado_bytes.hex())
print("MAC:", mac_bytes.hex())