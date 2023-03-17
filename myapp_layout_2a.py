import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QColor, QPalette


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

        layout = QVBoxLayout()

        layout.addWidget(Color('blue'))
        layout.addWidget(Color('yellow'))

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)



app = QApplication([])

window = MainWindow()
window.show()

app.exec()