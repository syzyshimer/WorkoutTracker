import sys

from PIL.ImageQt import QPixmap
from PyQt6.QtCore import QDate
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QTableWidgetItem
from PyQt6.QtSql import QSqlDatabase, QSqlQuery


class WorkoutTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('projectPYQT.ui', self)
        self.setWindowTitle('Мои Тренировки')
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
        self.timeTable.resizeRowsToContents()
        self.timeTable.resizeColumnsToContents()
        self.timeTable.horizontalHeader().setStretchLastSection(True)

        self.setFixedSize(834, 580)

        self.window1 = Warmup()
        self.window2 = Arms()
        self.window3 = Legs()
        self.window4 = Back()
        self.window5 = Breast()

        self.warmup.clicked.connect(self.show_warmup)
        self.arms.clicked.connect(self.show_arms)
        self.legs.clicked.connect(self.show_legs)
        self.back.clicked.connect(self.show_back)
        self.breast.clicked.connect(self.show_breast)

        self.load_data()

    def load_data(self):
        self.timeTable.setRowCount(0)
        query = QSqlQuery("SELECT * FROM workout ORDER BY date DESC")
        row = 0
        while query.next():
            work_id = query.value(0)
            date = query.value(1)
            calories = query.value(2)
            long = query.value(3)
            type = query.value(4)
            description = query.value(5)

            self.timeTable.insertRow(row)
            self.timeTable.setItem(row, 0, QTableWidgetItem(str(work_id)))
            self.timeTable.setItem(row, 1, QTableWidgetItem(date))
            self.timeTable.setItem(row, 2, QTableWidgetItem(str(calories)))
            self.timeTable.setItem(row, 3, QTableWidgetItem(str(long)))
            self.timeTable.setItem(row, 4, QTableWidgetItem(str(type)))
            self.timeTable.setItem(row, 5, QTableWidgetItem(str(description)))
            row += 1

    def add_workout(self):
        date = self.currentDate.date().toString('yyyy-MM-dd')
        calories = self.cal_info.text()
        long = self.long_info.text()
        type = self.type_info.text()
        discription = self.disc_info.text()

        query = QSqlQuery("""
                            INSERT INTO workouts (date, calories, long, type, discription)
                            VALUES (?, ?, ?, ?, ?)
                            """)

        query.addBindValue(date)
        query.addBindValue(calories)
        query.addBindValue(long)
        query.addBindValue(type)
        query.addBindValue(discription)
        query.exec()

        self.currentDate.setDate(QDate.currentDate())
        self.cal_info.clear()
        self.long_info.clear()
        self.type_info.clear()
        self.disc_info.clear()

        self.load_table()

    def button_click(self):
        self.add_btn.clicked.connect(self.add_workout)
        self.del_btn.clicked.connect(self.delete_workout)

    def delete_workout(self):
        selected_row = self.timeTable.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "ОШИБКА", "Пожалуйста, выберите ряд")

        work_id = int(self.timeTable.item(selected_row, 0).text())
        confirm = QMessageBox.question(self, "Вы уверены?", 'Удалить данную тренировку', QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.No:
            return

        query = QSqlQuery()
        query.prepare("DELETE FROM workouts WHERE id = ?")
        query.addBindValue(work_id)
        query.exec()

        self.load_data

    def show_warmup(self):
        if self.window1.isVisible():
            self.window1.hide()
        else:
            self.window1.show()

    def show_arms(self):
        if self.window2.isVisible():
            self.window2.hide()
        else:
            self.window2.show()

    def show_legs(self):
        if self.window3.isVisible():
            self.window3.hide()
        else:
            self.window3.show()

    def show_back(self):
        if self.window4.isVisible():
            self.window4.hide()
        else:
            self.window4.show()

    def show_breast(self):
        if self.window5.isVisible():
            self.window5.hide()
        else:
            self.window5.show()

class Warmup(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Разминка')
        self.label = QLabel(self)
        self.pixmap = QPixmap('warmup.jpg')
        self.label.setPixmap(self.pixmap)
        self.setCentralWidget(self.label)
        self.setFixedSize(self.pixmap.width(), self.pixmap.height())


class Arms(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Руки')
        self.label = QLabel(self)
        self.pixmap = QPixmap('arms.png')
        self.label.setPixmap(self.pixmap)
        self.setCentralWidget(self.label)
        self.setFixedSize(self.pixmap.width(), self.pixmap.height())


class Legs(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ноги')
        self.label = QLabel(self)
        self.pixmap = QPixmap('legs.png')
        self.label.setPixmap(self.pixmap)
        self.setCentralWidget(self.label)
        self.setFixedSize(self.pixmap.width(), self.pixmap.height())


class Back(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Спина')
        self.label = QLabel(self)
        self.pixmap = QPixmap('back.jpg')
        self.label.setPixmap(self.pixmap)
        self.setCentralWidget(self.label)
        self.setFixedSize(self.pixmap.width(), self.pixmap.height())


class Breast(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Грудь')
        self.label = QLabel(self)
        self.pixmap = QPixmap('breast.png')
        self.label.setPixmap(self.pixmap)
        self.setCentralWidget(self.label)
        self.setFixedSize(self.pixmap.width(), self.pixmap.height())


db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("workout.db")

query = QSqlQuery()
query.exec("""
            CREATE TABLE IF NOT EXISTS workout (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                calories REAL,
                long REAL,
                type REAL,
                description TEXT
            )
            """)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WorkoutTracker()
    ex.show()
    sys.exit(app.exec())