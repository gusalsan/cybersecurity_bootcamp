from cryptography.hazmat.primitives.asymmetric import ed25519

# 1. Leer clave privada (SOLO primeros 32 bytes si el archivo tiene 64)
with open("ed25519-priv", "rb") as f:
    all_bytes = f.read()

# Si el archivo tiene 64 bytes, toma solo los primeros 32
if len(all_bytes) == 64:
    private_bytes = all_bytes[:32]
    print(f"Tomando primeros 32 bytes de {len(all_bytes)} totales")
else:
    private_bytes = all_bytes

print(f"Clave privada ({len(private_bytes)} bytes): {private_bytes.hex()}")

# 2. Crear clave privada (FORMA CORRECTA en cryptography)
private_key = ed25519.Ed25519PrivateKey.from_private_bytes(private_bytes)

# 3. Obtener clave pública
public_key = private_key.public_key()
print(f"Clave pública: {public_key.public_bytes_raw().hex()}")

# 4. Mensaje
msg = "El equipo está preparado para seguir con el proceso, necesitaremos más recursos."
msg_bytes = msg.encode('utf-8')

# 5. Firmar (FORMA CORRECTA en cryptography)
signature = private_key.sign(msg_bytes)

# 6. Mostrar firma
print(f"\n**FIRMA GENERADA (64 bytes en hexadecimal):**")
print(signature.hex())
print(f"Longitud: {len(signature)} bytes")

# 7. Verificar (FORMA CORRECTA en cryptography)
try:
    public_key.verify(signature, msg_bytes)
    print("La firma es válida (verificación interna)")
except Exception as e:
    print(f"Error en verificación: {e}")