import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                               QVBoxLayout, QWidget, QGridLayout)


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First App')

        layout = QGridLayout()


        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('yellow'), 1, 0)
        layout.addWidget(Color('purple'), 1, 1)
        layout.addWidget(Color('purple'), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)



app = QApplication([])

window = MainWindow()
window.show()

app.exec()