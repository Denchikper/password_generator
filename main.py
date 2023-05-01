from PyQt5.QtGui import QClipboard
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import random
import string

class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load the UI file for the main window
        uic.loadUi('pass.ui', self)
        self.setWindowIcon(QIcon("./icon/key.png"))

        # Connect the Generate button to the generate_password method
        self.generate.clicked.connect(self.generate_password)

    def generate_password(self):
        length = self.lengthbox.value()
        use_digits = self.digit.isChecked()
        use_letters = self.alpha.isChecked()
        use_symbols = self.symbol.isChecked()

        #Проверка для одного чек бокса
        if not use_digits and not use_letters and not use_symbols:
            icon = QIcon("./icon/key.png")
            msg_box = QMessageBox()
            msg_box.setWindowIcon(icon)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Генератор паролей")
            msg_box.setText("Выберите хотя бы один параметр для генерации пароля.")
            msg_box.exec_()
            return
        if length == 0:
            icon = QIcon("./icon/key.png")
            msg_box = QMessageBox()
            msg_box.setWindowIcon(icon)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Генератор паролей")
            msg_box.setText("Укажите количество символов для генерации.")
            msg_box.exec_()
            return

        
        password = ''

        # Generate a random password of the specified length
        while len(password) < length:
            if use_digits:
                password += random.choice(string.digits)
            if use_letters:
                password += random.choice(string.ascii_letters)
            if use_symbols:
                password += random.choice(string.punctuation)

        # Add a "Copy" button to the message box
        msg = QMessageBox()
        icon = QIcon("./icon/key.png")
        msg.setWindowIcon(icon)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Сгенерированный пароль:")
        msg.setInformativeText(password)
        msg.setWindowTitle("Генератор паролей")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        yes_button = msg.button(QMessageBox.Yes)
        yes_button.setText("Да")
        no_button = msg.button(QMessageBox.No)
        no_button.setText("Отмена")
        copy_button = QPushButton('Копировать', msg)
        copy_button.clicked.connect(lambda: self.copy_password_to_clipboard(password))

        msg.addButton(copy_button, QMessageBox.AcceptRole)
        msg.exec_()

    def copy_password_to_clipboard(self, password):
        clipboard = QApplication.clipboard()
        clipboard.setText(password, QClipboard.Clipboard)

if __name__ == '__main__':
    app = QApplication([])
    window = PasswordGenerator()
    window.show()
    app.exec_()