import rsa
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import serialization
import os

class LmeRsa:

    def generate_key_pair():
        public_key, private_key = rsa.newkeys(1024)
        with open(".rsa/public_lme_rsa.pem", "wb") as file:
            file.write(public_key.save_pkcs1("PEM"))
        with open(".rsa/private_lme_rsa.pem", "wb") as file:
            file.write(private_key.save_pkcs1("PEM"))
        with open(".fernet/lme.key", "wb") as file:
            file.write(Fernet.generate_key())
        LmeRsa.encrypt_fernet_key(".fernet/lme.key")
        return True

    def encrypt_fernet_key(key):
        with open(key, "rb") as file:
            fernet_key = file.read()
        with open(".rsa/public_lme_rsa.pem", "rb") as file:
            public_key = rsa.PublicKey.load_pkcs1(file.read())
        encrypted_fernet_key = rsa.encrypt(fernet_key, public_key)
        with open(".fernet/lme.key", "wb") as file:
            file.write(encrypted_fernet_key)
        return True

    # def encrypt(self, file_path, public_key_path):
    #     with open(file_path, "rb") as file:
    #         content = file.read()
    #     with open(public_key_path, "rb") as file:
    #         public_key = rsa.PublicKey.load_pkcs1(file.read())
    #     encrypted_content = rsa.encrypt(content, public_key)
    #     encrypted_file_path = file_path + ".lme"
    #     with open(encrypted_file_path, "wb") as file:
    #         file.write(encrypted_content)
    #     os.remove(file_path)

    def encrypt( self,  archivo, password ):
        # Configuración de parámetros
        salt = os.urandom(16)
        iterations = 100000
        key_length = 32  # Tamaño de clave de 256 bits
        iv_length = 16  # Tamaño del vector de inicialización de 128 bits

        # Generar clave derivada de la contraseña
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=key_length,
            salt=salt,
            iterations=iterations,
            backend=default_backend()
        )
        key = kdf.derive(password.encode('utf-8'))

        # Generar un vector de inicialización aleatorio
        iv = os.urandom(iv_length)

        # Cifrar el archivo PDF
        input_file = archivo
        output_file = archivo + '.cursed'

        # Leer el archivo PDF
        with open(input_file, "rb") as file:
            plaintext = file.read()

        # Aplicar el cifrado
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_plaintext = padder.update(plaintext) + padder.finalize()

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

        # Guardar el archivo cifrado
        with open(output_file, "wb") as file:
            file.write(salt + iv + ciphertext)




    ##################################
    # OLD ENCRYPT METHOD
    ###############################

    # def encrypt(self, file_path, fernet_key_encrypted):
    #     logging.info("Entre a lmrsa: ENCRYPT . . .")
    #     with open(file_path, "rb") as file:
    #         file_content = file.read()
    #     with open(".rsa/private_lme_rsa.pem", "rb") as file:
    #         private_key = rsa.PrivateKey.load_pkcs1(file.read())
    #     with open(fernet_key_encrypted, "rb") as file:
    #         fernet_key_content = file.read()
    #     fernet_key = rsa.decrypt(fernet_key_content, private_key)
    #     fernet = Fernet(fernet_key)
    #     encrypted_content = fernet.encrypt(file_content)
    #     file_path_encrypted = file_path + ".lme"
    #     with open(file_path_encrypted, "wb") as file:
    #         file.write(encrypted_content)
    #     os.remove(file_path)
    #     return True
##############################################################################
    # def decrypt(self, file_path, private_key_path):
    #     with open(file_path, "rb") as file:
    #         content = file.read()
    #     with open(private_key_path, "rb") as file:
    #         private_key = rsa.PrivateKey.load_pkcs1(file.read())
    #     decrypted_content = rsa.decrypt(content, private_key)
    #     decrypted_file_path = file_path[:-4]
    #     with open(decrypted_file_path, "wb") as file:
    #         file.write(decrypted_content)
    #     return decrypted_file_path

    def decrypt(self, archivo_cifrado, password):
        # Leer el archivo cifrado
        with open(archivo_cifrado, "rb") as file:
            contenido_cifrado = file.read()

        # Obtener los valores de salt, iv y ciphertext del archivo cifrado
        salt = contenido_cifrado[:16]
        iv = contenido_cifrado[16:32]
        ciphertext = contenido_cifrado[32:]

        # Generar la clave derivada de la contraseña y el salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(password.encode('utf-8'))

        # Descifrar el contenido
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        # Eliminar el relleno (padding)
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
        archivo_descifrado = archivo_cifrado[:-7]
        # Guardar el contenido descifrado en un nuevo archivo
        with open(archivo_descifrado, "wb") as file:
            file.write(plaintext)
        return archivo_descifrado
    #################################################
    # OLD DECRYPT
    # #################################################

    # def decrypt(self, file_path, fernet_key_encrypted):
    #     try:
    #         with open(fernet_key_encrypted, "rb") as file:
    #             fernet_content_encrypted = file.read()
    #         with open(".rsa/private_lme_rsa.pem", "rb") as file:
    #             private_key = rsa.PrivateKey.load_pkcs1(file.read())
    #         fernet_key = rsa.decrypt(fernet_content_encrypted, private_key)
    #         fernet = Fernet(fernet_key)
    #         with open(file_path, "rb") as file:
    #             content_encrypted = file.read()
    #         decrypted_content = fernet.decrypt(content_encrypted)
    #         decrypted_file_path = file_path[:-4]
    #         with open(decrypted_file_path, "wb") as file:
    #             file.write(decrypted_content)
    #         return decrypted_file_path
    #     except rsa.pkcs1.DecryptionError as e:
    #         return False