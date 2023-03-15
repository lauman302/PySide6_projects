import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First App')

        widget = QListWidget()
        widget.addItems(['One', 'Two', 'Three'])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)
    
    def index_changed(self, i): # i не является индекс, а экземпляром QListItem
        print(i.text())
    
    def text_changed(self, s): # возвращает строкое представление
        print(s)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()