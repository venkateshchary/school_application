import sys
import config1
from PyQt5.QtWidgets import (QMainWindow, QLineEdit,
                             QWidget, QLabel , QDialog,
                             QVBoxLayout, QPushButton, QMessageBox)


class Login(QDialog):
    def __init__(self, height, width, parent=None):
        super(Login, self).__init__(parent)
        self.resize(300, 300)
        size = self.geometry()
        self.move((width-size.width())/2, (height-size.height())/2)
        username = QLabel("Username", self)
        username.move(100, 35)
        self.textName = QLineEdit(self)
        password = QLabel("Password", self)
        password.move(100, 110)
        self.textPass = QLineEdit(self)
        self.textPass.setEchoMode(QLineEdit.Password)
        self.buttonLogin = QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        # TODO: Connect to flask application to check login credentials
        if self.textName.text() == '12345' and self.textPass.text() == '12345@88':
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'Bad user or password')
