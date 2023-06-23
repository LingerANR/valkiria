import npyscreen
from modules.lme_rsa import LmeRsa
from modules.test_main_form import MainForm
import logging
class DecryptForm(npyscreen.ActionForm):
    def create(self):
        self.show_atx = 63
        self.show_aty = 1
        self.file_path = self.add(npyscreen.TitleFilenameCombo, name="File to Decrypt: ")
        self.key_path = self.add(npyscreen.TitleFilenameCombo, name="Key: ")

    def on_ok(self):
        reader = self.parentApp.getForm("READER")
        file_decrypted = LmeRsa.decrypt(self, self.file_path.value, self.key_path.value)
        if not file_decrypted:
            npyscreen.notify_confirm("Incorrect Key", "E R R O R")
            log = "ERROR: Incorrect Key"
            logging.error(log)
        else:
            reader.load_file_content(file_decrypted)
            npyscreen.notify_confirm("File Decrypted", "Success")
            self.parentApp.switchForm("READER")
