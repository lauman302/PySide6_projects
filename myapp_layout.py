import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
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

        widget = Color('red')

        self.setCentralWidget(widget)



app = QApplication([])

window = MainWindow()
window.show()

app.exec()