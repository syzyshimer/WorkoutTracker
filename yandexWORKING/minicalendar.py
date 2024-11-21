import io
import sys

from PyQt6.QtCore import QDate
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow

temp = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>644</width>
    <height>371</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="horizontalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>641</width>
      <height>331</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_2">
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout">
       <item>
        <layout class="QVBoxLayout" name="verticalLayout">
         <item>
          <widget class="QTimeEdit" name="timeEdit"/>
         </item>
         <item>
          <widget class="QCalendarWidget" name="calendarWidget"/>
         </item>
         <item>
          <widget class="QLineEdit" name="lineEdit"/>
         </item>
         <item>
          <widget class="QPushButton" name="addEventBtn">
           <property name="text">
            <string>Добавить Событие</string>
           </property>
          </widget>
         </item>
        </layout>
       </item>
      </layout>
     </item>
     <item>
      <widget class="QListWidget" name="eventList"/>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>644</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>"""


class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(temp)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.addEventBtn.clicked.connect(self.run)
        self.eventList.setSortingEnabled(True)
        

    def run(self):
        self.date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        self.plan = self.lineEdit.text()
        self.dt = self.timeEdit.time().toString()
        self.eventList.addItem(f'{self.date} {self.dt} - {self.plan}')
        self.eventList.sortItems(QtCore.Qt.DescendingOrder)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplePlanner()
    ex.show()
    sys.exit(app.exec())