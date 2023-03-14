import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PySide6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First App')

        button = QPushButton('Press Me')
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print('Clicked')


app = QApplication([])

window = MainWindow()
window.show()

app.exec()