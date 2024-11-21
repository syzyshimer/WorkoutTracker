import io
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>769</width>
    <height>601</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>40</y>
      <width>151</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>23</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Цвет №1</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>40</y>
      <width>151</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>23</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Цвет №2</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>530</x>
      <y>40</y>
      <width>151</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>23</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Цвет №3</string>
    </property>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>110</y>
      <width>171</width>
      <height>221</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QRadioButton" name="radioButton_1_1">
       <property name="text">
        <string>Синий</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup</string>
       </attribute>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_1_2">
       <property name="text">
        <string>Красный</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup</string>
       </attribute>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_1_3">
       <property name="text">
        <string>Зелёный</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup</string>
       </attribute>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>110</y>
      <width>171</width>
      <height>221</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_2">
     <item>
      <widget class="QRadioButton" name="radioButton_2_1">
       <property name="text">
        <string>Синий</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_2</string>
       </attribute>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_2_2">
       <property name="text">
        <string>Красный</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_2</string>
       </attribute>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_2_3">
       <property name="text">
        <string>Зелёный</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_2</string>
       </attribute>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_3">
    <property name="geometry">
     <rect>
      <x>530</x>
      <y>110</y>
      <width>171</width>
      <height>221</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_3">
     <item>
      <widget class="QRadioButton" name="radioButton_3_1">
       <property name="text">
        <string>Синий</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_3</string>
       </attribute>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_3_2">
       <property name="text">
        <string>Красный</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_3</string>
       </attribute>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_3_3">
       <property name="text">
        <string>Зелёный</string>
       </property>
       <attribute name="buttonGroup">
        <string notr="true">buttonGroup_3</string>
       </attribute>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="make_flag">
    <property name="geometry">
     <rect>
      <x>550</x>
      <y>350</y>
      <width>151</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Сделать флаг</string>
    </property>
   </widget>
   <widget class="QLabel" name="result">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>440</y>
      <width>401</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>9</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Text</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>769</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QToolBar" name="toolBar">
   <property name="windowTitle">
    <string>toolBar</string>
   </property>
   <attribute name="toolBarArea">
    <enum>TopToolBarArea</enum>
   </attribute>
   <attribute name="toolBarBreak">
    <bool>false</bool>
   </attribute>
  </widget>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="buttonGroup"/>
  <buttongroup name="buttonGroup_2"/>
  <buttongroup name="buttonGroup_3"/>
 </buttongroups>
</ui>"""

class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.color1 = ''
        self.color2 = ''
        self.color3 = ''
        self.color_group_1 = QButtonGroup()
        self.color_group_1.addButton(self.radioButton_1_1)
        self.color_group_1.addButton(self.radioButton_1_2)
        self.color_group_1.addButton(self.radioButton_1_3)
        self.color_group_1.buttonClicked.connect(self.color_picked1)

        self.color_group_2 = QButtonGroup()
        self.color_group_2.addButton(self.radioButton_2_1)
        self.color_group_2.addButton(self.radioButton_2_2)
        self.color_group_2.addButton(self.radioButton_2_3)
        self.color_group_2.buttonClicked.connect(self.color_picked2)

        self.color_group_3 = QButtonGroup()
        self.color_group_3.addButton(self.radioButton_3_1)
        self.color_group_3.addButton(self.radioButton_3_2)
        self.color_group_3.addButton(self.radioButton_3_3)
        self.color_group_3.buttonClicked.connect(self.color_picked3)

        self.make_flag.clicked.connect(self.flag)
        self.result.setText('')
        self.setFixedSize(769, 514)

    def color_picked1(self, id):
        for i in self.color_group_1.buttons():
            if i is self.color_group_1.checkedButton():
                self.color1 = i.text()

    def color_picked2(self, id):
        for i in self.color_group_2.buttons():
            if i is self.color_group_2.checkedButton():
                self.color2 = i.text()

    def color_picked3(self, id):
        for i in self.color_group_3.buttons():
            if i is self.color_group_3.checkedButton():
                self.color3 = i.text()

    def flag(self):
        self.result.setText('Цвета: ' + self.color1 + ', ' + self.color2 + ' и ' + self.color3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec())