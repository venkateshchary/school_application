import config1
from PyQt5 import QtCore, QtNetwork
from PyQt5.QtWidgets import (QLineEdit,
                             QLabel, QDialog,
                             QVBoxLayout, QPushButton, QMessageBox,)


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
        postData = QtCore.QUrlQuery()
        postData.addQueryItem("username", self.textName.text())
        postData.addQueryItem("password", self.textPass.text())
        qnam = QtNetwork.QNetworkAccessManager()
        reply = qnam.post(QtNetwork.QNetworkRequest(QtCore.QUrl(config1.login_url)), postData.toString(QtCore.QUrl.FullyEncoded).encode())
        loop = QtCore.QEventLoop()
        reply.finished.connect(loop.quit)
        loop.exec_()
        code = reply.attribute(QtNetwork.QNetworkRequest.HttpStatusCodeAttribute)
        if code == 200:
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'User not Found or Password wrong')
            self.textName.setText("")
            self.textPass.setText("")



