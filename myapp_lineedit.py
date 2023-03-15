import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First App')

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText('Enter you text')

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
        
        widget.setInputMask('99/99/9999')

        self.setCentralWidget(widget)

    def return_pressed(self): # срабатывает при нажании на энтер
        print('Return pressed')
        self.centralWidget().setText('Boom!')
    
    def selection_changed(self): # возвращает выделенный фрагмент из текста
        print('Selection changed')
        print(self.centralWidget().selectedText())

    def text_changed(self, s): # при изменении текста
        print('Text changed ...')
        print(s)
    
    def text_edited(self, s): # при редактировании, только когда пользователь изменяет
        print('Text edited...')
        print(s)
    



app = QApplication([])

window = MainWindow()
window.show()

app.exec()