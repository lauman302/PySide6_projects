import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First App')

        widget = QLabel('Hello')
        widget.setPixmap(QPixmap('pyqt_logo.jpg'))
        widget.setScaledContents(True) # позволяет растягивать окно с изображением

        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        print('Clicked')
    
    def the_button_was_toggled(self, checked):
        print('Checked?', checked)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()