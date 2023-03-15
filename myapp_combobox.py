import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First App')

        widget = QComboBox()
        widget.addItems(['One', 'Two', 'Three'])
#        widget.setEditable(True) Позволяет добавлять новые значения
#        widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically) - правила на внесение новых значений
#        widget.setMaxCount(10) - ограничием список по кол-ву значений

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)
    
    def index_changed(self, i):
        print(i)
    
    def text_changed(self, s):
        print(s)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()