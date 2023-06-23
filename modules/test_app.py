import npyscreen
import curses
from modules.test_encrypt_form import EncryptForm
from modules.test_decrypt_form import DecryptForm
from modules.test_main_form import MainForm
from modules.test_read_file_form import ReadFile
from modules.test_make_file import MakeFileForm

class MyApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Main Menu", lines=38, columns=135)
        self.addForm("ENCRYPT",EncryptForm, name = "Encrypt", lines=20, columns=70)
        self.addForm("DECRYPT",DecryptForm, name = "Decrypt", lines=20, columns=70)
        self.addForm("READER",ReadFile, name = "File", lines=35, columns=70)
        self.addForm("MAKE", MakeFileForm, name = "Make File", lines=35, columns=70)

