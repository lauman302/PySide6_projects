import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First App')

        widget = QLabel('Hello')
        font = widget.font()
        font.setPointSize(40)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        print('Clicked')
    
    def the_button_was_toggled(self, checked):
        print('Checked?', checked)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()