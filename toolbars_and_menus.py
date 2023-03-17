import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QToolBar, QLabel, QStatusBar
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First App')

        label = QLabel('Hello')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My main toolbar')
        self.addToolBar(toolbar)

        button_action = QAction('Your button', self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.onMytoolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self)) # отображение панели снизу с информацией из метода StatusTip
    
    def onMytoolBarButtonClick(self, s):
        print('click', )


app = QApplication([])

window = MainWindow()
window.show()

app.exec()