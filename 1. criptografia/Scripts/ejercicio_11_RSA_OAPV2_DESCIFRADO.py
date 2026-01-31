from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import os


#RSA OAEP Bueno para cifrar. 
#Proceso de carga firma
my_path = os.path.abspath(os.getcwd())
path_file_priv = my_path + "/clave-rsa-oaep-publ.pem"
keypub = RSA.importKey(open(path_file_priv).read())



clave_simetrica = bytes.fromhex("e2cff885901a5449e9c448ba5b948a8c4ee377152b3f1acfa0148fb3a426db72")

#decryptor = PKCS1_OAEP.new(keypriv,SHA256)
#decrypted = decryptor.decrypt(MensajeCifrado)

encryptor = PKCS1_OAEP.new(keypub, SHA256)
cifrado_nuevo = encryptor.encrypt(clave_simetrica)


print("Cifrado:", cifrado_nuevo.hex())
print("--------------------------------------------------")