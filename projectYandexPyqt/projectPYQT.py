import sys

from PIL.ImageQt import QPixmap
from PyQt6.QtCore import QDate
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QTableWidgetItem
import sqlite3

class WorkoutTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('projectPYQT.ui', self)
        self.setWindowTitle('Мои Тренировки')
        self.db = DataBase()
        self.initUI()
        self.button_click()

    def initUI(self):
        self.currentDate.setDate(QDate.currentDate())

        self.cal_info.setPlaceholderText("Количество калорий")
        self.type_info.setPlaceholderText("Тип тренировки")
        self.long_info.setPlaceholderText("Продолжительность")
        self.disc_info.setPlaceholderText("Свое описание")

        self.timeTable.setColumnCount(6)
        self.timeTable.setHorizontalHeaderLabels(['Номер', 'Дата', 'Калории','Продолжительность', 'Тип', 'Описание'])

        self.setFixedSize(986, 614)

        self.warmup.clicked.connect(lambda: self.show_body('warmup'))
        self.arms.clicked.connect(lambda: self.show_body('arms'))
        self.legs.clicked.connect(lambda: self.show_body('legs'))
        self.back.clicked.connect(lambda: self.show_body('back'))
        self.breast.clicked.connect(lambda: self.show_body('breast'))

        self.load_data()

    def show_body(self, part):
        self.body_window = Body(part)
        if self.body_window.isVisible():
            self.body_window.hide()
        else:
            self.body_window.show()

    def load_data(self):
        data = self.db.fetch_data()

        if data:
            self.timeTable.setRowCount(len(data))
            self.timeTable.setColumnCount(len(data[0]))
            for row_index, row_data in enumerate(data):
                for column_index, item in enumerate(row_data):
                    self.timeTable.setItem(row_index, column_index, QTableWidgetItem(str(item)))

    def add_workout(self):
        date = self.currentDate.date().toString('yyyy-MM-dd')
        calories = float(self.cal_info.text())
        type = self.type_info.text()
        long = float(self.long_info.text())
        discription = self.disc_info.text()

        self.db.add_data(date, calories, long, type, discription)

        self.currentDate.setDate(QDate.currentDate())
        self.cal_info.clear()
        self.long_info.clear()
        self.type_info.clear()
        self.disc_info.clear()

        self.load_data()

    def delete_workout(self):
        selected_row = self.timeTable.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите ряд!")

        work_id = int(self.timeTable.item(selected_row, 0).text())
        confirm = QMessageBox.question(self, "Вы уверены?", 'Удалить данную тренировку?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if confirm == QMessageBox.StandardButton.Yes:
            self.db.delete_data(work_id)
            self.load_data()


    def update_workout(self):
        selected_row = self.timeTable.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите ряд!.")

        work_id = int(self.timeTable.item(selected_row, 0).text())
        date = self.currentDate.date().toString('yyyy-MM-dd')
        calories = float(self.cal_info.text())
        type = self.type_info.text()
        long = float(self.long_info.text())
        discription = self.disc_info.text()

        self.db.update_data(work_id, date, calories, type, long, discription)
        self.load_data()

    def button_click(self):
        self.add_btn.clicked.connect(self.add_workout)
        self.del_btn.clicked.connect(self.delete_workout)
        self.update_btn.clicked.connect(self.update_workout)

class Body(QMainWindow):
    def __init__(self, part):
        self.pictures = {'warmup': 'warmup.jpg', 'arms': 'arms.png', 'legs': 'legs.png',
                         'back': 'back.jpg', 'breast': 'breast.png'}
        super().__init__()
        self.setWindowTitle('Руки')
        self.label = QLabel(self)
        self.pixmap = QPixmap(self.pictures[part])
        self.label.setPixmap(self.pixmap)
        self.setCentralWidget(self.label)
        self.setFixedSize(self.pixmap.width(), self.pixmap.height())


class DataBase:
    def __init__(self):
        super().__init__()
        self.create_table()

    def create_table(self):
        con = sqlite3.connect('workouts.db')
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS workout (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                calories REAL,
                long REAL,
                type TEXT,
                description TEXT
                )
                ''')
        con.commit()
        con.close()

    def add_data(self, date, calories, long, type, disc):
        con = sqlite3.connect('workouts.db')
        cur = con.cursor()
        query = f"INSERT INTO workout (date, calories, long, type, description) VALUES (?, ?, ?, ?, ?)"
        cur.execute(query, (date, calories, long, type, disc))
        con.commit()
        con.close()

    def delete_data(self, work_id):
        con = sqlite3.connect('workouts.db')
        cur = con.cursor()
        query = f'DELETE FROM workout WHERE id = ?'
        cur.execute(query, (work_id,))
        con.commit()
        con.close()

    def update_data(self, work_id, date, calories, type, long, disc):
        con = sqlite3.connect('workouts.db')
        cur = con.cursor()
        query = f'UPDATE workout SET date = ?, calories = ?, long = ?, type = ?, description = ? WHERE id = ?'
        cur.execute(query, (date, calories, long, type, disc, work_id))
        con.commit()
        con.close()

    def fetch_data(self):
        con = sqlite3.connect('workouts.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM workout ORDER BY date DESC')
        return cur.fetchall()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WorkoutTracker()
    ex.show()
    sys.exit(app.exec())