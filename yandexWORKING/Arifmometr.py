import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel


class Arifmometr(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(800, 500, 250, 100)
        self.setWindowTitle('Арифмометр')

        self.add_button = QPushButton('+', self)
        self.add_button.setGeometry(50, 10, 20, 20)
        self.add_button.clicked.connect(self.ad_button)

        self.substract_button = QPushButton('-', self)
        self.substract_button.setGeometry(67, 10, 20, 20)
        self.substract_button.clicked.connect(self.subst_button)

        self.multiply_button = QPushButton('*', self)
        self.multiply_button.setGeometry(84, 10, 20, 20)
        self.multiply_button.clicked.connect(self.multi_button)

        self.first_value = QLineEdit("0", self)
        self.first_value.setGeometry(10, 10, 40, 20)

        self.second_value = QLineEdit("0", self)
        self.second_value.setGeometry(104, 10, 40, 20)

        self.result = QLineEdit("0", self)
        self.result.setGeometry(165, 10, 40, 20)
        self.result.setEnabled(False)

        self.label = QLabel(self)
        self.label.setText("=")
        self.label.move(150, 10)

    def ad_button(self):
        self.result.setText(str(int(self.first_value.text()) + int(self.second_value.text())))

    def subst_button(self):
        self.result.setText(str(int(self.first_value.text()) - int(self.second_value.text())))

    def multi_button(self):
        self.result.setText(str(int(self.first_value.text()) * int(self.second_value.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Arifmometr()
    ex.show()
    sys.exit(app.exec())