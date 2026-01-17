from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA256
import secrets

salt = bytes.fromhex("e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3") #Mi identificador
master_secret = bytes.fromhex("a2cff885901a5449e9c448ba5b948a8c4ee377152b3f1acfa0148fb3a426db72") #Mi clave maestra
key1, key2 = HKDF(master_secret, 32, salt, SHA256, 2)

print("Clave key1: ", key1.hex()) # Clave de cifrado
print("Clave key2: ", key2.hex()) # Clave de MAC