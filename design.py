# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 464)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setItalic(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(160, 40, 211, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inp_surname = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.inp_surname.setFont(font)
        self.inp_surname.setObjectName("inp_surname")
        self.verticalLayout_2.addWidget(self.inp_surname)
        self.inp_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.inp_name.setFont(font)
        self.inp_name.setObjectName("inp_name")
        self.verticalLayout_2.addWidget(self.inp_name)
        self.inp_otchestvo = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.inp_otchestvo.setFont(font)
        self.inp_otchestvo.setObjectName("inp_otchestvo")
        self.verticalLayout_2.addWidget(self.inp_otchestvo)
        self.inp_class = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.inp_class.setFont(font)
        self.inp_class.setObjectName("inp_class")
        self.verticalLayout_2.addWidget(self.inp_class)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(370, 40, 141, 171))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_10.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_17.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_18.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_18)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(510, 40, 311, 176))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.inp_teacher = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.inp_teacher.setFont(font)
        self.inp_teacher.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         opacity: 0;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.inp_teacher.setObjectName("inp_teacher")
        self.verticalLayout_4.addWidget(self.inp_teacher)
        self.inp_subject = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.inp_subject.setFont(font)
        self.inp_subject.setObjectName("inp_subject")
        self.verticalLayout_4.addWidget(self.inp_subject)
        self.inp_year = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.inp_year.setFont(font)
        self.inp_year.setObjectName("inp_year")
        self.verticalLayout_4.addWidget(self.inp_year)
        self.inp_project_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.inp_project_name.setFont(font)
        self.inp_project_name.setObjectName("inp_project_name")
        self.verticalLayout_4.addWidget(self.inp_project_name)
        self.inp_score = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.inp_score.setFont(font)
        self.inp_score.setObjectName("inp_score")
        self.verticalLayout_4.addWidget(self.inp_score)
        self.inp_grade = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.inp_grade.setFont(font)
        self.inp_grade.setObjectName("inp_grade")
        self.verticalLayout_4.addWidget(self.inp_grade)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 250, 161, 31))
        self.label_3.setStyleSheet("background-color:rgb(168, 129, 50);\n"
"border-radius: 15px;\n"
"color: \"white\";")
        self.label_3.setObjectName("label_3")
        self.add_new_student = QtWidgets.QPushButton(self.centralwidget)
        self.add_new_student.setGeometry(QtCore.QRect(40, 190, 121, 31))
        self.add_new_student.setStyleSheet("background-color:rgb(168, 129, 50);\n"
"border-radius: 15px;\n"
"color: \"white\";")
        self.add_new_student.setObjectName("add_new_student")
        self.add_new_inform = QtWidgets.QPushButton(self.centralwidget)
        self.add_new_inform.setGeometry(QtCore.QRect(180, 190, 121, 31))
        self.add_new_inform.setStyleSheet("background-color:rgb(168, 129, 50);\n"
"border-radius: 15px;\n"
"color: \"white\";")
        self.add_new_inform.setObjectName("add_new_inform")
        self.enquiry_name = QtWidgets.QPushButton(self.centralwidget)
        self.enquiry_name.setGeometry(QtCore.QRect(100, 290, 141, 31))
        self.enquiry_name.setStyleSheet("background-color: rgb(23, 135, 255);\n"
"border-radius: 5px;\n"
"color: \"white\"")
        self.enquiry_name.setObjectName("enquiry_name")
        self.enquiry_teacher = QtWidgets.QPushButton(self.centralwidget)
        self.enquiry_teacher.setGeometry(QtCore.QRect(100, 330, 141, 31))
        font = QtGui.QFont()
        font.setItalic(True)
        self.enquiry_teacher.setFont(font)
        self.enquiry_teacher.setStyleSheet("background-color: rgb(23, 135, 255);\n"
"border-radius: 5px;\n"
"color: \"white\"")
        self.enquiry_teacher.setObjectName("enquiry_teacher")
        self.enquiry_class = QtWidgets.QPushButton(self.centralwidget)
        self.enquiry_class.setGeometry(QtCore.QRect(100, 370, 141, 31))
        self.enquiry_class.setStyleSheet("background-color: rgb(23, 135, 255);\n"
"border-radius: 5px;\n"
"color: \"white\"")
        self.enquiry_class.setObjectName("enquiry_class")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(380, 230, 131, 201))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.mid_score_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.mid_score_label.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.mid_score_label.setObjectName("mid_score_label")
        self.verticalLayout_5.addWidget(self.mid_score_label)
        self.mid_grade_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.mid_grade_label.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.mid_grade_label.setObjectName("mid_grade_label")
        self.verticalLayout_5.addWidget(self.mid_grade_label)
        self.max_grade_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.max_grade_label.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.max_grade_label.setObjectName("max_grade_label")
        self.verticalLayout_5.addWidget(self.max_grade_label)
        self.min_grade_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.min_grade_label.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.min_grade_label.setObjectName("min_grade_label")
        self.verticalLayout_5.addWidget(self.min_grade_label)
        self.max_score_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.max_score_label.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.max_score_label.setObjectName("max_score_label")
        self.verticalLayout_5.addWidget(self.max_score_label)
        self.min_score_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.min_score_label.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.min_score_label.setObjectName("min_score_label")
        self.verticalLayout_5.addWidget(self.min_score_label)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(510, 230, 71, 201))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.mid_score = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.mid_score.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.mid_score.setObjectName("mid_score")
        self.verticalLayout_6.addWidget(self.mid_score)
        self.mid_grade = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.mid_grade.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.mid_grade.setObjectName("mid_grade")
        self.verticalLayout_6.addWidget(self.mid_grade)
        self.max_score = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.max_score.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.max_score.setObjectName("max_score")
        self.verticalLayout_6.addWidget(self.max_score)
        self.min_score = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.min_score.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.min_score.setObjectName("min_score")
        self.verticalLayout_6.addWidget(self.min_score)
        self.max_grade = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.max_grade.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.max_grade.setObjectName("max_grade")
        self.verticalLayout_6.addWidget(self.max_grade)
        self.min_grade = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.min_grade.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.min_grade.setObjectName("min_grade")
        self.verticalLayout_6.addWidget(self.min_grade)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, -40, 911, 551))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("MainFon.jpg"))
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 131, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setEnabled(False)
        self.label.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setEnabled(False)
        self.label_9.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("QLabel {\n"
"         color: red;\n"
"         font: bold 16px;\n"
"         background: transparent;\n"
"         border: none;\n"
"         margin: 0px;\n"
"         padding: 0px;\n"
"      }")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.take_inform = QtWidgets.QPushButton(self.centralwidget)
        self.take_inform.setGeometry(QtCore.QRect(610, 310, 131, 41))
        self.take_inform.setStyleSheet("background-color:rgb(168, 129, 50);\n"
"border-radius: 15px;\n"
"color: \"white\";")
        self.take_inform.setObjectName("take_inform")
        self.label_8.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.label_3.raise_()
        self.add_new_student.raise_()
        self.add_new_inform.raise_()
        self.enquiry_name.raise_()
        self.enquiry_teacher.raise_()
        self.enquiry_class.raise_()
        self.verticalLayoutWidget_5.raise_()
        self.verticalLayoutWidget_6.raise_()
        self.verticalLayoutWidget.raise_()
        self.take_inform.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">Преподаватель:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">Предмет:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Harlow Solid Italic\'; font-size:16px; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">Год(20xx-20xx):</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">Тема проекта:</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">Баллы:</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">Оценка:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Создать диаграмму по:</span></p></body></html>"))
        self.add_new_student.setText(_translate("MainWindow", "Добавить в базу"))
        self.add_new_inform.setText(_translate("MainWindow", "Добавить новое..."))
        self.enquiry_name.setText(_translate("MainWindow", "по ФИО ученика"))
        self.enquiry_teacher.setText(_translate("MainWindow", "по ФИО преподавателя"))
        self.enquiry_class.setText(_translate("MainWindow", "по классу обучения"))
        self.mid_score_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-style:italic; text-decoration: underline; color:#ffffff;\">Средний балл:</span></p></body></html>"))
        self.mid_grade_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-style:italic; text-decoration: underline; color:#ffffff;\">Средняя оценка:</span></p></body></html>"))
        self.max_grade_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-style:italic; text-decoration: underline; color:#ffffff;\">Макс. оценка:</span></p></body></html>"))
        self.min_grade_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-style:italic; text-decoration: underline; color:#ffffff;\">Мин. оценка:</span></p></body></html>"))
        self.max_score_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-style:italic; text-decoration: underline; color:#ffffff;\">Макс. балл:</span></p></body></html>"))
        self.min_score_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-style:italic; text-decoration: underline; color:#ffffff;\">Мин. балл:</span></p></body></html>"))
        self.mid_score.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">0</span></p></body></html>"))
        self.mid_grade.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">0</span></p></body></html>"))
        self.max_score.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">0</span></p></body></html>"))
        self.min_score.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">0</span></p></body></html>"))
        self.max_grade.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">0</span></p></body></html>"))
        self.min_grade.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">0</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">Фамилия:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">Имя:</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">Отчество:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">Класс:</span></p></body></html>"))
        self.take_inform.setText(_translate("MainWindow", "Сведения об ученике\n"
" по ФИО"))
