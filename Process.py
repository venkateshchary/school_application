import config1
from PyQt5.QtWidgets import (QMainWindow, QLineEdit,
                             QLabel, QFormLayout, QHBoxLayout, QAction, qApp ,QDialog)
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from login import Login


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 School_admin_app'
        self.left = 10
        self.top = 100
        self.width = config1.width
        self.height = config1.height
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        self.statusBar().showMessage('School Admin Tool')
        self.show()

    def addbox_text(self):

        self.textGenerated = QLineEdit(self)
        self.textGenerated.move(5, 106)
        self.textGenerated.resize(self.width-10, 80)
        self.textGenerated.setVisible(False)


    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        print("text: ", textboxValue)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    config1.width = screen_resolution.width()
    config1.height = screen_resolution.height()
    login = Login(config1.height, config1.width)

    if login.exec_() == QDialog.Accepted:
        window = App()
        window.show()
        sys.exit(app.exec_())
