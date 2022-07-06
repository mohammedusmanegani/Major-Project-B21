from PyQt5.QtWidgets import QDial, QDialog, QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys


class UI(QDialog):
    def __init__(self):
        super(UI, self).__init__()
        # Loading the ui
        uic.loadUi("image.ui", self)

        # Define widgets
        self.button = self.findChild(QPushButton, "pushButton")
        self.label = self.findChild(QLabel, "label")

        self.button1 = self.findChild(QPushButton, "pushButton_2")
        self.label1 = self.findChild(QLabel, "label_2")

        # button action
        self.button.clicked.connect(self.clicker)
        self.button1.clicked.connect(self.clicker1)
        self.show()

    def clicker(self):
        fileName = QFileDialog.getOpenFileName(
            self, "Open File", "c:", "All Files (*);;PNG Files (*.png);;Jpg Files (*.jpg)")
        # open a image
        self.pixmap = QPixmap(fileName[0])
        # add pic to the label
        self.label.setPixmap(self.pixmap)

    def clicker1(self):
        fileName = QFileDialog.getOpenFileName(
            self, "Open File", "c:", "All Files (*);;PNG Files (*.png);;Jpg Files (*.jpg)")
        # open a image
        self.pixmap = QPixmap(fileName[0])
        # add pic to the label
        self.label1.setPixmap(self.pixmap)


app = QApplication(sys.argv)
UIwindow = UI()
sys.exit(app.exec_())
