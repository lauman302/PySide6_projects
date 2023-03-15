import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QCheckBox
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First App')

        widget = QCheckBox('This is a checkbox')
#        widget.setCheckState(Qt.CheckState.Checked)
#        widget.setCheckState(Qt.CheckState.PartiallyChecked)
        widget.setTristate(True) # три состояния выбора

        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.CheckState.Checked)
        print(s)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()