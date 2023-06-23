import rsa
import os
from cryptography.fernet import Fernet
import logging
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

    def encrypt(self, file_path, fernet_key_encrypted):
        logging.info("Entre a lmrsa: ENCRYPT . . .")
        with open(file_path, "rb") as file:
            file_content = file.read()
        with open(".rsa/private_lme_rsa.pem", "rb") as file:
            private_key = rsa.PrivateKey.load_pkcs1(file.read())
        with open(fernet_key_encrypted, "rb") as file:
            fernet_key_content = file.read()
        fernet_key = rsa.decrypt(fernet_key_content, private_key)
        fernet = Fernet(fernet_key)
        encrypted_content = fernet.encrypt(file_content)
        file_path_encrypted = file_path + ".lme"
        with open(file_path_encrypted, "wb") as file:
            file.write(encrypted_content)
        os.remove(file_path)
        return True

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

    def decrypt(self, file_path, fernet_key_encrypted):
        try:
            with open(fernet_key_encrypted, "rb") as file:
                fernet_content_encrypted = file.read()
            with open(".rsa/private_lme_rsa.pem", "rb") as file:
                private_key = rsa.PrivateKey.load_pkcs1(file.read())
            fernet_key = rsa.decrypt(fernet_content_encrypted, private_key)
            fernet = Fernet(fernet_key)
            with open(file_path, "rb") as file:
                content_encrypted = file.read()
            decrypted_content = fernet.decrypt(content_encrypted)
            decrypted_file_path = file_path[:-4]
            with open(decrypted_file_path, "wb") as file:
                file.write(decrypted_content)
            return decrypted_file_path
        except rsa.pkcs1.DecryptionError as e:
            return False