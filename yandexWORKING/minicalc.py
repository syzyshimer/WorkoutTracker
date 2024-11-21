import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber


class MiniCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 500, 400, 150)
        self.setWindowTitle('Миникалькулятор')

        self.calculate_button = QPushButton('->', self)
        self.calculate_button.move(220, 30)
        self.calculate_button.setGeometry(160, 55, 50, 20)
        self.calculate_button.clicked.connect(self.calculate)

        self.number_1 = QLineEdit(self)
        self.number_1.move(20, 33)

        self.number_2 = QLineEdit(self)
        self.number_2.move(20, 80)

        self.label = QLabel(self)
        self.label.setText("Первое число(целое):")
        self.label.move(20, 15)

        self.label = QLabel(self)
        self.label.setText("Второе число(целое):")
        self.label.move(20, 60)

        self.label = QLabel(self)
        self.label.setText("Сумма:")
        self.label.move(220, 20)

        self.label = QLabel(self)
        self.label.setText("Разность:")
        self.label.move(220, 50)

        self.label = QLabel(self)
        self.label.setText("Произведение:")
        self.label.move(220, 80)

        self.label = QLabel(self)
        self.label.setText("Частное:")
        self.label.move(220, 110)

        self.result_sum = QLCDNumber(self)
        self.result_sum.move(330, 18)

        self.result_sub = QLCDNumber(self)
        self.result_sub.move(330, 50)

        self.result_mul = QLCDNumber(self)
        self.result_mul.move(330, 80)

        self.result_div = QLCDNumber(self)
        self.result_div.move(330, 110)


    def calculate(self):
        n1 = int(self.number_1.text())
        n2 = int(self.number_2.text())

        sub_result = n1 - n2
        sum_result = n1 + n2
        mul_result = n1 * n2

        if n2 != 0:
            div_result = round(n1 / n2, 3)
        else:
            div_result = "Error"

        self.result_sub.display(sub_result)
        self.result_sum.display(sum_result)
        self.result_mul.display(mul_result)

        if isinstance(div_result, str):
            self.result_div.display('Error')
        else:
            self.result_div.display(div_result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiniCalculator()
    ex.show()
    sys.exit(app.exec())
