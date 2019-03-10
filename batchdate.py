import config1
from PyQt5.QtWidgets import (QMainWindow, QLineEdit,
                             QAction, qApp, QDialog, QPushButton)
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon


def batchDate():
    print("called in batchdate :")
    textGenerated = QLineEdit()
    textGenerated.move(5, 106)