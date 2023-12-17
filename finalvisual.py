# Form implementation generated from reading ui file 'finalvisual.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow_fin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 370)
        MainWindow.setStyleSheet("background-color: rgb(223, 194, 149);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.check_service_1 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.check_service_1.setGeometry(QtCore.QRect(30, 90, 240, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.check_service_1.setFont(font)
        self.check_service_1.setStyleSheet("background-color: rgb(211, 205, 156);")
        self.check_service_1.setObjectName("check_service_1")
        self.svodn_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.svodn_label.setGeometry(QtCore.QRect(150, 0, 265, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.svodn_label.setFont(font)
        self.svodn_label.setStyleSheet("background-color: rgb(210, 245, 208);")
        self.svodn_label.setObjectName("svodn_label")
        self.service_or = QtWidgets.QLabel(parent=self.centralwidget)
        self.service_or.setGeometry(QtCore.QRect(30, 60, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.service_or.setFont(font)
        self.service_or.setStyleSheet("background-color: rgb(158, 171, 255);")
        self.service_or.setObjectName("service_or")
        self.check_service_2 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.check_service_2.setGeometry(QtCore.QRect(30, 110, 240, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.check_service_2.setFont(font)
        self.check_service_2.setStyleSheet("background-color: rgb(211, 205, 156);")
        self.check_service_2.setObjectName("check_service_2")
        self.check_service_3 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.check_service_3.setGeometry(QtCore.QRect(30, 130, 240, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.check_service_3.setFont(font)
        self.check_service_3.setStyleSheet("background-color: rgb(211, 205, 156);")
        self.check_service_3.setObjectName("check_service_3")
        self.check_service_4 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.check_service_4.setGeometry(QtCore.QRect(30, 150, 240, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.check_service_4.setFont(font)
        self.check_service_4.setStyleSheet("background-color: rgb(211, 205, 156);")
        self.check_service_4.setObjectName("check_service_4")
        self.nomer_or = QtWidgets.QLabel(parent=self.centralwidget)
        self.nomer_or.setGeometry(QtCore.QRect(360, 60, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nomer_or.setFont(font)
        self.nomer_or.setStyleSheet("background-color: rgb(158, 171, 255);")
        self.nomer_or.setObjectName("nomer_or")
        self.radioButton_first = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_first.setGeometry(QtCore.QRect(360, 90, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_first.setFont(font)
        self.radioButton_first.setStyleSheet("background-color: rgb(136, 193, 136);")
        self.radioButton_first.setObjectName("radioButton_first")
        self.radioButton_second = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_second.setGeometry(QtCore.QRect(360, 110, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_second.setFont(font)
        self.radioButton_second.setStyleSheet("background-color: rgb(136, 193, 136);")
        self.radioButton_second.setObjectName("radioButton_second")
        self.radioButton_third = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_third.setGeometry(QtCore.QRect(360, 130, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_third.setFont(font)
        self.radioButton_third.setStyleSheet("background-color: rgb(136, 193, 136);")
        self.radioButton_third.setObjectName("radioButton_third")
        self.radioButton_fourth = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_fourth.setGeometry(QtCore.QRect(360, 150, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_fourth.setFont(font)
        self.radioButton_fourth.setStyleSheet("background-color: rgb(136, 193, 136);")
        self.radioButton_fourth.setObjectName("radioButton_fourth")
        self.datatime_or = QtWidgets.QLabel(parent=self.centralwidget)
        self.datatime_or.setGeometry(QtCore.QRect(360, 180, 220, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.datatime_or.setFont(font)
        self.datatime_or.setStyleSheet("background-color: rgb(210, 245, 208);")
        self.datatime_or.setObjectName("datatime_or")
        self.dateEdit_in = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit_in.setGeometry(QtCore.QRect(450, 210, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.dateEdit_in.setFont(font)
        self.dateEdit_in.setStyleSheet("background-color: rgb(189, 217, 232);")
        self.dateEdit_in.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 2), QtCore.QTime(0, 0, 0)))
        self.dateEdit_in.setObjectName("dateEdit_in")
        self.date_label_in = QtWidgets.QLabel(parent=self.centralwidget)
        self.date_label_in.setGeometry(QtCore.QRect(360, 210, 90, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.date_label_in.setFont(font)
        self.date_label_in.setStyleSheet("background-color: rgb(189, 217, 232);")
        self.date_label_in.setObjectName("date_label_in")
        self.dateEdit_off = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit_off.setGeometry(QtCore.QRect(450, 240, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.dateEdit_off.setFont(font)
        self.dateEdit_off.setStyleSheet("background-color: rgb(216, 216, 160);")
        self.dateEdit_off.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 2), QtCore.QTime(0, 0, 0)))
        self.dateEdit_off.setObjectName("dateEdit_off")
        self.date_label_off = QtWidgets.QLabel(parent=self.centralwidget)
        self.date_label_off.setGeometry(QtCore.QRect(360, 240, 90, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.date_label_off.setFont(font)
        self.date_label_off.setStyleSheet("background-color: rgb(216, 216, 160);")
        self.date_label_off.setObjectName("date_label_off")
        self.end_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.end_button.setGeometry(QtCore.QRect(30, 310, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.end_button.setFont(font)
        self.end_button.setStyleSheet("background-color: rgb(85, 206, 89);")
        self.end_button.setObjectName("end_button")
        self.service_name_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.service_name_label.setGeometry(QtCore.QRect(30, 180, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.service_name_label.setFont(font)
        self.service_name_label.setStyleSheet("background-color: rgb(211, 125, 106);")
        self.service_name_label.setObjectName("service_name_label")
        self.service_summ = QtWidgets.QLabel(parent=self.centralwidget)
        self.service_summ.setGeometry(QtCore.QRect(30, 200, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.service_summ.setFont(font)
        self.service_summ.setStyleSheet("background-color: rgb(211, 125, 106);")
        self.service_summ.setText("")
        self.service_summ.setObjectName("service_summ")
        self.nomerlabelsum = QtWidgets.QLabel(parent=self.centralwidget)
        self.nomerlabelsum.setGeometry(QtCore.QRect(380, 305, 160, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nomerlabelsum.setFont(font)
        self.nomerlabelsum.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.nomerlabelsum.setObjectName("nomerlabelsum")
        self.nomer_sum = QtWidgets.QLabel(parent=self.centralwidget)
        self.nomer_sum.setGeometry(QtCore.QRect(380, 325, 160, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nomer_sum.setFont(font)
        self.nomer_sum.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.nomer_sum.setText("")
        self.nomer_sum.setObjectName("nomer_sum")
        self.nomersummrasch = QtWidgets.QPushButton(parent=self.centralwidget)
        self.nomersummrasch.setGeometry(QtCore.QRect(380, 270, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nomersummrasch.setFont(font)
        self.nomersummrasch.setStyleSheet("background-color: rgb(114, 161, 53);")
        self.nomersummrasch.setObjectName("nomersummrasch")
        self.all_label_sum = QtWidgets.QLabel(parent=self.centralwidget)
        self.all_label_sum.setGeometry(QtCore.QRect(30, 240, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.all_label_sum.setFont(font)
        self.all_label_sum.setStyleSheet("background-color: rgb(203, 73, 93);")
        self.all_label_sum.setObjectName("all_label_sum")
        self.all_sum = QtWidgets.QLabel(parent=self.centralwidget)
        self.all_sum.setGeometry(QtCore.QRect(30, 265, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.all_sum.setFont(font)
        self.all_sum.setStyleSheet("background-color: rgb(203, 73, 93);")
        self.all_sum.setText("")
        self.all_sum.setObjectName("all_sum")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.check_service_1.setText(_translate("MainWindow", "Персональный переводчик и гид 5000руб."))
        self.svodn_label.setText(_translate("MainWindow", "Сводная по заказу"))
        self.service_or.setText(_translate("MainWindow", "Выберите услуги"))
        self.check_service_2.setText(_translate("MainWindow", "Поход в горы с проводником 10000руб."))
        self.check_service_3.setText(_translate("MainWindow", "Прогулка на яхте 20000руб."))
        self.check_service_4.setText(_translate("MainWindow", "Экскурсия по городу 10000руб"))
        self.nomer_or.setText(_translate("MainWindow", "Выберите номер"))
        self.radioButton_first.setText(_translate("MainWindow", "Первый номер"))
        self.radioButton_second.setText(_translate("MainWindow", "Второй номер"))
        self.radioButton_third.setText(_translate("MainWindow", "Третий номер"))
        self.radioButton_fourth.setText(_translate("MainWindow", "Четвёртый номер"))
        self.datatime_or.setText(_translate("MainWindow", "Выберите дату приезда и дату отъезда"))
        self.date_label_in.setText(_translate("MainWindow", "Дата приезда"))
        self.date_label_off.setText(_translate("MainWindow", "Дата отъезда"))
        self.end_button.setText(_translate("MainWindow", "Оплатить"))
        self.service_name_label.setText(_translate("MainWindow", "Общая стоимость услуг:"))
        self.nomerlabelsum.setText(_translate("MainWindow", "Стоимость за номер:"))
        self.nomersummrasch.setText(_translate("MainWindow", "Рассчитать цену за номер"))
        self.all_label_sum.setText(_translate("MainWindow", "Стоимость всего:"))

        self.check_service_1.stateChanged.connect(self.update_order)
        self.check_service_2.stateChanged.connect(self.update_order)
        self.check_service_3.stateChanged.connect(self.update_order)
        self.check_service_4.stateChanged.connect(self.update_order)
        self.nomersummrasch.clicked.connect(self.calculate_sum)
        self.end_button.clicked.connect(self.op_final_window)

        self.db_connection = sqlite3.connect("hotel.db")
        self.update_order()

    def update_order(self):
        self.service_total = 0

        cursor = self.db_connection.cursor()

        if self.check_service_1.isChecked():
            cursor.execute("SELECT price FROM services WHERE id = 1")
            result = cursor.fetchone()
            if result:
                self.service_total += result[0]

        if self.check_service_2.isChecked():
            cursor.execute("SELECT price FROM services WHERE id = 2")
            result = cursor.fetchone()
            if result:
                self.service_total += result[0]

        if self.check_service_3.isChecked():
            cursor.execute("SELECT price FROM services WHERE id = 3")
            result = cursor.fetchone()
            if result:
                self.service_total += result[0]

        if self.check_service_4.isChecked():
            cursor.execute("SELECT price FROM services WHERE id = 4")
            result = cursor.fetchone()
            if result:
                self.service_total += result[0]

        cursor.close()

        self.service_summ.setText(f"Сумма: {self.service_total} руб.")

    def calculate_sum(self):
        selected_room = None
        if self.radioButton_first.isChecked():
            selected_room = "1"
        elif self.radioButton_second.isChecked():
            selected_room = "2"
        elif self.radioButton_third.isChecked():
            selected_room = "3"
        elif self.radioButton_fourth.isChecked():
            selected_room = "4"
        else:
            self.nomer_sum.setText("Выберите номер")
            return

        conn = sqlite3.connect("hotel.db")
        cursor = conn.cursor()
        query = f"SELECT price FROM room WHERE id='{selected_room}'"
        cursor.execute(query)
        price_per_day = cursor.fetchone()[0]

        date_in = self.dateEdit_in.date().toPyDate()
        date_out = self.dateEdit_off.date().toPyDate()

        if date_in >= date_out:
            self.nomer_sum.setText("Выберите правильную дату")
            return

        num_of_days = (date_out - date_in).days
        total_sum = price_per_day * num_of_days

        self.nomer_sum.setText(f"Сумма: {total_sum} руб.")

        self.all_sum_all = self.service_total + total_sum

        self.all_sum.setText(f"Сумма: {self.all_sum_all} руб.")

    def op_final_window(self):
        self.all_sum_all = str(self.all_sum_all) + " руб."
        self.fin_window = QMainWindow()
        self.fin_ui = Ui_MainWindow_check(self.all_sum_all)
        self.fin_ui.setupUi(self.fin_window)
        self.fin_window.show()

class Ui_MainWindow_check(object):
    def __init__(self, all_sum_all):
        self.all_sum_all = all_sum_all
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 150)
        MainWindow.setStyleSheet("background-color: rgb(223, 194, 149);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.yspeh_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.yspeh_label.setGeometry(QtCore.QRect(20, 30, 170, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.yspeh_label.setFont(font)
        self.yspeh_label.setStyleSheet("background-color: rgb(197, 255, 160);")
        self.yspeh_label.setObjectName("yspeh_label")
        self.yspeh_sum = QtWidgets.QLabel(parent=self.centralwidget)
        self.yspeh_sum.setGeometry(QtCore.QRect(190, 30, 140, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.yspeh_sum.setFont(font)
        self.yspeh_sum.setStyleSheet("background-color: rgb(197, 255, 160);")
        self.yspeh_sum.setText("")
        self.yspeh_sum.setObjectName("yspeh_sum")
        self.end_program = QtWidgets.QPushButton(parent=self.centralwidget)
        self.end_program.setGeometry(QtCore.QRect(90, 80, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.end_program.setFont(font)
        self.end_program.setStyleSheet("background-color: rgb(58, 159, 30);")
        self.end_program.setObjectName("end_program")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.yspeh_sum.setText(str(self.all_sum_all))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.yspeh_label.setText(_translate("MainWindow", "Вы успешно оплатили:"))
        self.end_program.setText(_translate("MainWindow", "Завершить"))
        self.end_program.clicked.connect(self.exit_program)
    def exit_program(self):
        QCoreApplication.quit()
