import config1
from PyQt5.QtWidgets import (QMainWindow, QLineEdit,
                             QAction, qApp, QDialog, QPushButton)
from PyQt5.QtWidgets import QApplication, QCalendarWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from login import Login
import batchdate


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
        self.menubar()
        self.calender()
        self.root_buttons()
        self.statusBar().showMessage('School Admin Tool')
        self.show()

    def root_buttons(self):
        self.attendace_btn = QPushButton('Attendance', self)
        self.attendace_btn.clicked.connect(self.class_btn)
        self.attendace_btn.move(50, 30)
        self.performance_btn = QPushButton('Performance', self)
        self.performance_btn.clicked.connect(self.class_btn)
        self.performance_btn.move(150, 30)
        self.bonafide_btn = QPushButton('Bonafide', self)
        self.bonafide_btn.clicked.connect(self.class_btn)
        self.bonafide_btn.move(250, 30)

    def class_btn(self):
        pass


    def calender(self):
        self.cal = QCalendarWidget(self)
        self.cal.resize(200, 150)
        self.cal.setGridVisible(True)
        self.cal.move(self.width-210, 25)

    def menubar(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

    def addbox_text(self,):
        print("called: ", self.clicked_class.text())
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
