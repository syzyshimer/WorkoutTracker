import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('upload.ui', self)
        self.initUI()


    def initUI(self):
        [i.clicked.connect(self.run) for i in self.buttonGroup_digits.buttons()]
        [i.clicked.connect(self.calc) for i in self.buttonGroup_binary.buttons()]

        self.btn_eq.clicked.connect(self.result)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_fact.clicked.connect(self.fact)
        self.btn_dot.clicked.connect(self.run)
        self.btn_sqrt.clicked.connect(self.sqrt)

        self.data = ''
        self.data_choice = ''

    def clear(self):
        self.data = ''
        self.data_choice = ''
        self.table.display('')

    def sqrt(self):
        if self.data_choice:
            self.data_choice += '**0.5'
            self.result()

    def true_fact(self, n):
        if n < 0:
            return -1
        if n == 0:
            return 1
        else:
            return n * self.true_fact(n - 1)

    def fact(self):
        if self.data_choice :
            self.data_choice = "self.true_fact({})".format(self.data_choice)
            print(self.data_choice)
            self.result()

    def result(self):
        self.data = eval(self.data_choice)
        self.data_choice = str(self.data)
        self.table.display(self.data)
        self.data = ''

    def calc(self):
        if self.data_choice:
            self.result()
            if self.data_choice[-1] not in ['+', '-', '/', '*']:
                self.data_choice += self.sender().text()
            else:
                self.data_choice = self.data_choice[0:len(self.data_choice) - 1] + self.sender().text()
            self.data_choice = self.data_choice.replace('^', '**')

    def run(self):
        if self.sender().text() == '.':
            if '.' in self.data:
                return
        if self.data != '0' or (self.data == '0' and self.sender().text() == '.'):
            self.data = self.data + self.sender().text()
            self.data_choice = self.data_choice + self.sender().text()
            self.table.display(self.data)
        else:
            self.data = self.sender().text()
            self.data_choice = self.sender().text()
            self.table.display(self.data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())