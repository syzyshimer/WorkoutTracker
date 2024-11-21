import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton

code_morse = {'A': '.-', 'B': '-...',

                   'C': '-.-.', 'D': '-..', 'E': '.',

                   'F': '..-.', 'G': '--.', 'H': '....',

                   'I': '..', 'J': '.---', 'K': '-.-',

                   'L': '.-..', 'M': '--', 'N': '-.',

                   'O': '---', 'P': '.--.', 'Q': '--.-',

                   'R': '.-.', 'S': '...', 'T': '-',

                   'U': '..-', 'V': '...-', 'W': '.--',

                   'X': '-..-', 'Y': '-.--', 'Z': '--..'}

class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 200, 520, 60)
        self.setWindowTitle('Азбука Морзе 2')

        self.self.calculate_button = QPushButton('->', self)
        self.calculate_button.move(220, 30)
        self.calculate_button.setGeometry(160, 55, 50, 20)
        self.calculate_button.clicked.connect(self.calculate)


        self.result = QLineEdit(self)
        self.result.move(0, 30)
        self.output.resize(520, 30)
        self.result.setEnabled(False)
        b = 0

    def morse_code(self):
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MorseCode()
    ex.show()
    sys.exit(app.exec())