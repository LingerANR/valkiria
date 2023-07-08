import npyscreen
from lme_rsa import LmeRsa
import logging
from test_log_box import LogBoxTitle as LogBox
class EncryptForm(npyscreen.ActionForm):
    
    def create(self):
        self.show_atx = 63
        self.show_aty = 1
        self.file_path = self.add(npyscreen.TitleFilenameCombo, name = "File: ")
        self.key_path = self.add(npyscreen.TitleText, name = "Key: ")

    def on_ok(self):
        file = self.file_path.value
        key_encrypted = self.key_path.value
        LmeRsa.encrypt(self, file, key_encrypted)
        npyscreen.notify_confirm("File Encrypted . . .", "Success")
        self.parentApp.switchForm("MAIN")

    def beforeEditing( self ):
        logging.info("Sali de encrypt...")
        LogBox.update_logs()

    def afterEditing( self ):
        logging.info("Prueba de log")
        LogBox.update_logs()
        
        