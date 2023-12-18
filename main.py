import sqlite3
import matplotlib.pyplot as plt
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog

from design import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QtGui.QIcon('Project_icon.jpg'))
        con = sqlite3.connect("database_for_project_activity.db")
        # Создание курсора
        cur = con.cursor()
        self.students = list(map(lambda x: x[0], cur.execute('''SELECT s.name FROM students as s''').fetchall()))
        self.teachers = list(map(lambda x: x[0], cur.execute('''SELECT t.teacher FROM teachers as t''').fetchall()))
        self.subjects = list(map(lambda x: x[0], cur.execute('''SELECT s.subject FROM subjects as s''').fetchall()))
        self.classes = list(map(lambda x: x[0], cur.execute('''SELECT c.class FROM classes as c''').fetchall()))
        self.years = list(map(lambda x: x[0], cur.execute('''SELECT y.year FROM years as y''').fetchall()))
        self.project_names = list(map(lambda x: x[0], cur.execute('''SELECT mt.project_name
                                                                     FROM main_table as mt''').fetchall()))
        con.close()
        self.setWindowTitle("База данных проектной деятельности учащихся")
        self.app = app
        self.add_new_student.clicked.connect(self.add_student)
        self.enquiry_name.clicked.connect(self.build_table_name)
        self.enquiry_teacher.clicked.connect(self.build_table_teacher)
        self.enquiry_class.clicked.connect(self.build_table_class)
        self.add_new_inform.clicked.connect(self.add_new_information)
        self.take_inform.clicked.connect(self.take_inform_func)

    def add_student(self):
        con = sqlite3.connect("database_for_project_activity.db")
        # Создание курсора
        cur = con.cursor()
        student_name = str(self.inp_surname.text() + ' ' + self.inp_name.text() + ' ' + self.inp_otchestvo.text())
        if self.inp_surname.text() == '' or self.inp_name.text() == '' or \
                self.inp_otchestvo.text() == '' or \
                not self.inp_score.text().isdigit() or not self.inp_grade.text().isdigit():
            em = QMessageBox()
            em.setText("Проверьте корректность введенных данных!")
            em.setWindowTitle("Ошибка")
            em.exec_()
            return
        elif self.inp_teacher.text() not in self.teachers:
            em = QMessageBox()
            em.setText("Некорректный ввод данных в ячейке Преподаватель!")
            em.setWindowTitle("Ошибка")
            em.exec_()
            return
        elif self.inp_project_name.text() in self.project_names and \
                self.project_names.index(self.inp_project_name.text()) == self.students.index(student_name) and \
                student_name in self.students:
            em = QMessageBox()
            em.setText("Данный экземпляр уже есть в базе!")
            em.setWindowTitle("Ошибка")
            em.exec_()
            return
        elif str(self.inp_subject.text()[0].upper() + self.inp_subject.text()[1:]) not in self.subjects:
            em = QMessageBox()
            em.setText("Некорректный ввод данных в ячейке Предмет!")
            em.setWindowTitle("Ошибка")
            em.exec_()
            return
        elif str(self.inp_class.text()[0] + self.inp_class.text()[1].lower()) not in self.classes:
            em = QMessageBox()
            em.setText("Некорректный ввод данных в ячейке Класс!")
            em.setWindowTitle("Ошибка")
            em.exec_()
            return
        elif self.inp_year.text() not in self.years:
            em = QMessageBox()
            em.setText("Некорректный ввод данных в ячейке Год!")
            em.setWindowTitle("Ошибка")
            em.exec_()
            return
        else:
            # Выполнение запроса и получение всех результатов
            new_id = cur.execute('''SELECT id FROM main_table WHERE 
                                          id = (SELECT MAX(id) FROM main_table)''').fetchone()
            year_id = cur.execute(f'''SELECT years.id FROM years WHERE 
                                      years.year=('{self.inp_year.text()}')''').fetchone()
            last_student_id = cur.execute('''SELECT id FROM students WHERE 
                                                   id = (SELECT MAX(id) FROM students)''').fetchone()
            if student_name not in self.students:
                cur.execute(f'''INSERT INTO students(id, name) VALUES(
                                        {int(last_student_id[0]) + 1}, ('{student_name}'))''')
                add_student_id = cur.execute(f'''SELECT s.id FROM students as s 
                                                                 WHERE s.name=('{student_name}')''').fetchone()
            else:
                add_student_id = cur.execute(f'''SELECT s.id FROM students as s 
                                                 WHERE s.name=('{student_name}')''').fetchone()
            add_subject_id = cur.execute(f'''SELECT subjects.id FROM subjects
                                         WHERE subjects.subject=('{self.inp_subject.text()}')''').fetchone()
            add_teacher_id = cur.execute(f'''SELECT teachers.id FROM teachers
                                         WHERE teachers.teacher=('{self.inp_teacher.text()}')''').fetchone()
            add_class_id = cur.execute(f'''SELECT classes.id FROM classes
                                         WHERE classes.class=('{self.inp_class.text()[0] + self.inp_class.
                                       text()[1].lower()}')''').fetchone()
            cur.execute(
                f'''INSERT INTO main_table(id,student_id,project_name,
                    subject_id,teacher_id, year_id, score, class_id, grade) 
                        VALUES ('{int(new_id[0]) + 1}','{int(add_student_id[0])}',
                         '{self.inp_project_name.text()}', 
                         '{int(add_subject_id[0])}', '{int(add_teacher_id[0])}',
                         '{int(year_id[0])}', '{int(self.inp_score.text())}',
                         '{int(add_class_id[0])}', '{int(self.inp_grade.text())}')''').fetchall()
            QMessageBox.about(self, "Результат", "Ученик успешно добавлен!")
            self.students = list(map(lambda x: x[0], cur.execute('''SELECT s.name FROM 
            students as s''').fetchall()))
            self.teachers = list(map(lambda x: x[0], cur.execute('''SELECT t.teacher 
            FROM teachers as t''').fetchall()))
            self.subjects = list(map(lambda x: x[0], cur.execute('''SELECT s.subject 
            FROM subjects as s''').fetchall()))
            self.classes = list(map(lambda x: x[0], cur.execute('''SELECT c.class
             FROM classes as c''').fetchall()))
            self.years = list(map(lambda x: x[0], cur.execute('''SELECT y.year 
            FROM years as y''').fetchall()))
            self.project_names = list(map(lambda x: x[0], cur.execute('''SELECT mt.project_name
                                                                    FROM main_table as mt''').fetchall()))
        con.commit()
        con.close()


    def take_inform_func(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите ФИО ученика",
                                                "ФИО ученика:")
        con = sqlite3.connect("database_for_project_activity.db")
        # Создание курсора
        cur = con.cursor()
        if ok_pressed and name in self.students:
            stud_id = cur.execute(f'''SELECT students.id FROM students
                                                WHERE (students.name='{name}')''').fetchone()
            year, ok_pressed1 = QInputDialog.getText(self, "Введите период, за который нужна информация",
                                                     "Учебный год(20хх-20хх):")
            surname = name.split()[0]
            new_name = name.split()[1]
            fname = name.split()[2]
            if ok_pressed1 and year[:4].isdigit() and \
                    year[5:].isdigit() and len(year.split('-')) == 2 and year in self.years:
                year_id = cur.execute(f'''SELECT years.id FROM years WHERE years.year=('{year}')''').fetchone()
                project_name = cur.execute(f'''SELECT mt.project_name FROM main_table as mt
                                                WHERE mt.year_id={year_id[0]} AND 
                                                mt.student_id={stud_id[0]}''').fetchone()[0]
                class_ = cur.execute(f'''SELECT class FROM classes
                                                    WHERE classes.id=(SELECT mt.class_id FROM main_table as mt
                                                    WHERE mt.year_id={year_id[0]} AND 
                                                    mt.student_id={stud_id[0]})''').fetchone()[0]
                score = cur.execute(f'''SELECT mt.score FROM main_table as mt
                                                               WHERE mt.year_id={year_id[0]} AND 
                                                               mt.student_id={stud_id[0]}''').fetchone()[0]
                grade = cur.execute(f'''SELECT mt.grade FROM main_table as mt
                                                            WHERE mt.year_id={year_id[0]} AND 
                                                            mt.student_id={stud_id[0]}''').fetchone()[0]
                teacher = cur.execute(f'''SELECT teachers.teacher FROM teachers
                                                    WHERE teachers.id=(SELECT mt.teacher_id FROM main_table as mt
                                                    WHERE mt.year_id={year_id[0]} AND 
                                                    mt.student_id={stud_id[0]})''').fetchone()[0]
                subject = cur.execute(f'''SELECT subjects.subject FROM subjects
                                                    WHERE subjects.id=(SELECT mt.subject_id FROM main_table as mt
                                                    WHERE mt.year_id={year_id[0]} AND 
                                                    mt.student_id={stud_id[0]})''').fetchone()[0]
                self.inp_subject.setText(subject)
                self.inp_project_name.setText(project_name)
                self.inp_surname.setText(surname)
                self.inp_name.setText(new_name)
                self.inp_otchestvo.setText(fname)
                self.inp_year.setText(year)
                self.inp_teacher.setText(teacher)
                self.inp_grade.setText(str(grade))
                self.inp_score.setText(str(score))
                self.inp_class.setText(class_)
        else:
            em = QMessageBox()
            em.setText("Информация отсутствует!")
            em.setWindowTitle("Ошибка")
            con.close()
            em.exec_()
            return
        con.close()



    def build_table_name(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите ФИО ученика",
                                                "ФИО ученика:")
        con = sqlite3.connect("database_for_project_activity.db")
        # Создание курсора
        cur = con.cursor()
        if ok_pressed and name in self.students:
            time_period, ok_pressed1 = QInputDialog.getText(self, "Введите промежуток времени",
                                                            "Года(20xx-20xx):")
            if ok_pressed1 and time_period[:4].isdigit() and \
                    time_period[5:].isdigit() and len(time_period.split('-')) == 2:
                n = 0
                grades = []
                scores = []
                years = []
                start_year = int(time_period[:4])
                last_year = int(time_period[5:])
                for i in range(int(last_year - start_year)):
                    year = str(int(start_year) + n) + '-' + str(int(start_year) + n + 1)
                    years.append(year)
                    n += 1
                for j in years:
                    mark = cur.execute(f'''SELECT mt.grade FROM main_table as mt
                                                WHERE mt.year_id=(SELECT years.id FROM years
                                                WHERE years.year='{j}') AND 
                                                mt.student_id=(SELECT students.id FROM students
                                                WHERE students.name='{name}')''').fetchone()
                    score = cur.execute(f'''SELECT mt.score FROM main_table as mt
                                                WHERE mt.year_id=(SELECT years.id FROM years
                                                WHERE years.year='{j}') AND 
                                                mt.student_id=(SELECT students.id FROM students
                                                WHERE students.name='{name}')''').fetchone()
                    if mark is None:
                        years.pop(years.index(j))
                        break
                    else:
                        grades.append(mark[0])
                        scores.append(score[0])
                if len(grades) != 0:
                    self.mid_grade.setText(str(round(sum(grades) / len(grades), 2)))
                    self.max_grade.setText(str(max(grades)))
                    self.min_grade.setText(str(min(grades)))
                    self.min_score.setText(str(min(scores)))
                    self.mid_score.setText(str(round(sum(scores) / len(scores), 2)))
                    self.max_score.setText(str(max(scores)))
                if len(grades) >= 1:
                    fig, ax = plt.subplots(figsize=(4, 4))
                    plt.title('Успеваемость ученика в заданный период')
                    ax.plot(years, grades)
                    ax.grid(True)
                    plt.show()
                else:
                    em = QMessageBox()
                    em.setText("Информация отсутствует!")
                    em.setWindowTitle("Ошибка")
                    em.exec_()
                    return
            else:
                em = QMessageBox()
                em.setText("Проверьте корректность введенных данных!")
                em.setWindowTitle("Ошибка")
                em.exec_()
                return
        else:
            em = QMessageBox()
            em.setText("Проверьте корректность введенных данных!")
            em.setWindowTitle("Ошибка")
            em.exec_()
            return
        con.close()

    def build_table_teacher(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите ФИО преподавателя",
                                                "ФИО преподавателя:")
        con = sqlite3.connect("database_for_project_activity.db")
        # Создание курсора
        cur = con.cursor()
        if ok_pressed and name not in self.teachers:
            QMessageBox.about(self, "Ошибка!", "Данного преподавателя нет в базе!")
        else:
            if ok_pressed:
                time_period, ok_pressed1 = QInputDialog.getText(self, "Введите промежуток времени",
                                                                "Года(20xx-20xx):")
                if ok_pressed1 and time_period[:4].isdigit() and \
                        time_period[5:].isdigit() and len(time_period.split('-')) == 2:
                    n = 0
                    grades = []
                    scores = []
                    grade_5 = 0
                    grade_4 = 0
                    grade_3 = 0
                    grade_2 = 0
                    years = []
                    labels = ['Оценка 5', 'Оценка 4', 'Оценка 3', 'Оценка 2']
                    start_year = int(time_period[:4])
                    last_year = int(time_period[5:])
                    for i in range(int(last_year - start_year)):
                        year = str(int(start_year) + n) + '-' + str(int(start_year) + n + 1)
                        years.append(year)
                        n += 1
                    for j in years:
                        marks = cur.execute(f'''SELECT mt.grade FROM main_table as mt
                                                        WHERE mt.year_id=(SELECT years.id FROM years
                                                        WHERE years.year='{j}') AND 
                                                        mt.teacher_id=(SELECT teachers.id FROM teachers
                                                        WHERE teachers.teacher='{name}')''').fetchall()
                        score = cur.execute(f'''SELECT mt.score FROM main_table as mt
                                                        WHERE mt.year_id=(SELECT years.id FROM years
                                                        WHERE years.year='{j}') AND 
                                                        mt.teacher_id=(SELECT teachers.id FROM teachers
                                                        WHERE teachers.teacher='{name}')''').fetchall()
                        if marks is None:
                            break
                        else:
                            for sc in score:
                                scores.append(sc[0])
                            for mark in marks:
                                grades.append(mark[0])
                            for grade in grades:
                                if int(grade) == 5:
                                    grade_5 += 1
                                elif int(grade) == 4:
                                    grade_4 += 1
                                elif int(grade) == 3:
                                    grade_3 += 1
                                elif int(grade) == 2:
                                    grade_2 += 1
                    grades_kol = [grade_5, grade_4, grade_3, grade_2]
                    for kol in grades_kol:
                        ind = grades_kol.index(kol)
                        if kol == 0 and grades_kol[ind] == grade_5:
                            grades_kol.pop(ind)
                            labels.pop(0)
                        elif kol == 0 and grades_kol[ind] == grade_4:
                            grades_kol.pop(ind)
                            labels.pop(1)
                        elif kol == 0 and grades_kol[ind] == grade_3:
                            grades_kol.pop(ind)
                            labels.pop(2)
                        elif kol == 0 and grades_kol[ind] == grade_2:
                            grades_kol.pop(ind)
                            labels.pop(3)
                    if len(grades) != 0:
                        self.mid_grade.setText(str(round(sum(grades) / len(grades), 2)))
                        self.max_grade.setText(str(max(grades)))
                        self.min_grade.setText(str(min(grades)))
                        self.min_score.setText(str(min(scores)))
                        self.mid_score.setText(str(round(sum(scores) / len(scores), 2)))
                        self.max_score.setText(str(max(scores)))
                    if len(grades) >= 1:
                        fig, ax = plt.subplots(figsize=(4, 4))
                        plt.title('Успеваемость у преподавателя в заданный период')
                        ax.pie(grades_kol, labels=labels, autopct='%1.1f%%')
                        ax.grid(True)
                        plt.show()
                    else:
                        em = QMessageBox()
                        em.setText("Информация отсутствует!")
                        em.setWindowTitle("Ошибка")
                        em.exec_()
                        return
                else:
                    em = QMessageBox()
                    em.setText("Проверьте корректность введенных данных!")
                    em.setWindowTitle("Ошибка")
                    em.exec_()
                    return
        con.close()

    def build_table_class(self):
        student_class, ok_pressed = QInputDialog.getText(self, "Введите цифру и букву класса",
                                                         "Класс:")
        if ok_pressed and student_class in self.classes:
            class_year, ok_pressed1 = QInputDialog.getText(self, "Введите год обучения",
                                                           f"Год(20xx-20xx) обучения класса {student_class}:")
            con = sqlite3.connect("database_for_project_activity.db")

            # Создание курсора
            cur = con.cursor()
            if ok_pressed1 and class_year in self.years:
                time_period, ok_pressed2 = QInputDialog.getText(self, "Введите промежуток времени",
                                                                "Года(20xx-20xx):")
                if ok_pressed2 and time_period[:4].isdigit() and \
                        time_period[5:].isdigit() and len(time_period.split('-')) == 2:
                    n = 0
                    mid_grades = []
                    years = []
                    grades_2 = []
                    scores = []
                    start_year = int(time_period[:4])
                    last_year = int(time_period[5:])
                    if len(student_class) == 3:
                        letter = student_class[2]
                    else:
                        letter = student_class[1]
                    for i in range(int(last_year - start_year)):
                        year = str(int(start_year) + n) + '-' + str(int(start_year) + n + 1)
                        years.append(year)
                        n += 1
                    for j in years:
                        dif_years = int(class_year[:4]) - int(j[:4])
                        students = cur.execute(f'''SELECT mt.student_id FROM main_table as mt WHERE
                                                       mt.year_id=(SELECT years.id FROM years WHERE
                                                       years.year='{j}') AND mt.class_id=(SELECT classes.id
                                                       FROM classes WHERE classes.class = 
                                                       ('{str(int(student_class[:-1]) - dif_years) +
                                                          letter}'))''').fetchall()
                        grades = []
                        for stud in students:
                            grade = cur.execute(f'''SELECT mt.grade FROM main_table as mt WHERE
                                                       mt.student_id={stud[0]}''').fetchone()
                            score = cur.execute(f'''SELECT mt.score FROM main_table as mt WHERE
                                                       mt.student_id={stud[0]}''').fetchone()
                            if grade is None:
                                break
                            else:
                                grades.append(grade[0])
                                grades_2.append(grade[0])
                                scores.append(score[0])
                        if len(grades) != 0:
                            mid = (sum(grades)) / len(grades)
                            mid_grades.append(round(mid, 2))
                        else:
                            years.pop(years.index(j))
                    if len(grades_2) != 0:
                        self.mid_grade.setText(str(round(sum(grades_2) / len(grades_2), 2)))
                        self.max_grade.setText(str(max(scores)))
                        self.min_grade.setText(str(min(scores)))
                        self.min_score.setText(str(min(grades_2)))
                        self.mid_score.setText(str(round(sum(scores) / len(scores), 2)))
                        self.max_score.setText(str(max(grades_2)))
                    if len(mid_grades) >= 1:
                        fig, ax = plt.subplots(figsize=(4, 4))
                        plt.title('Среднаяя успеваемость класса в заданный период')
                        ax.plot(years, mid_grades, 'bo--')
                        ax.grid(True)
                        plt.show()
                    else:
                        em = QMessageBox()
                        em.setText("Информация отсутствует!")
                        em.setWindowTitle("Ошибка")
                        em.exec_()
                        return
            else:
                em = QMessageBox()
                em.setText("Проверьте корректность введенных данных!")
                em.setWindowTitle("Ошибка")
                em.exec_()
                return
            con.close()
        else:
            em = QMessageBox()
            em.setText("Проверьте корректность введенных данных!")
            em.setWindowTitle("Ошибка")
            em.exec_()
            return

    def add_new_information(self):
        new_item, ok_pressed = QInputDialog.getItem(self, "Выберите новый пункт для \
                                                      добавления в базу данных", "Наименование пункта:",
                                                    ("Предмет", "Преподаватель", "Класс", "Год"), 0, False)
        if ok_pressed:
            new_name, ok_pressed1 = QInputDialog.getText(self, "Введите название",
                                                         "Название, год или имя:")
            if ok_pressed1:
                if new_item == 'Предмет' and len(new_name) != 0:
                    self.add_new_subject(new_name)
                elif new_item == 'Преподаватель' and len(new_name.split()) == 3:
                    self.add_new_teacher(new_name)
                elif new_item == 'Класс' and (new_name[0].isdigit() and new_name[1].isalpha()) \
                        and len(new_name) == 2:
                    self.add_new_class(new_name)
                elif new_item == 'Год' and len(new_name.split('-')) == 2 and new_name[:4].isdigit() \
                        and new_name[5:].isdigit():
                    self.add_new_year(new_name)
                else:
                    em = QMessageBox()
                    em.setText("Проверьте корректность введенных данных!")
                    em.setWindowTitle("Ошибка")
                    em.exec_()
                    return

    def add_new_subject(self, item):
        con = sqlite3.connect("database_for_project_activity.db")
        # Создание курсора
        cur = con.cursor()
        if item in self.subjects:
            em = QMessageBox()
            em.setText("Данный предмет уже есть в базе!")
            em.setWindowTitle("Ошибка")
            em.exec_()
        else:
            new_id = int(cur.execute('''SELECT id FROM subjects WHERE 
                                          id = (SELECT MAX(id) FROM subjects)''').fetchone()[0]) + 1
            cur.execute(f'''INSERT INTO subjects(id, subject) VALUES({new_id}, ('{item}'))''')
            self.subjects = list(map(lambda x: x[0], cur.execute('''SELECT s.subject FROM subjects as s''').fetchall()))
            QMessageBox.about(self, "Результат", "Предмет успешно добавлен!")
        con.commit()
        con.close()

    def add_new_teacher(self, item):
        con = sqlite3.connect("database_for_project_activity.db")

        # Создание курсора
        cur = con.cursor()
        if item in self.teachers:
            em = QMessageBox()
            em.setText("Данный учитель уже есть в базе!")
            em.setWindowTitle("Ошибка")
            em.exec_()
        else:
            new_id = int(cur.execute('''SELECT id FROM teachers WHERE 
                                                  id = (SELECT MAX(id) FROM teachers)''').fetchone()[0]) + 1
            cur.execute(f'''INSERT INTO teachers(id, teacher) VALUES({new_id}, ('{item}'))''')
            self.teachers = list(map(lambda x: x[0], cur.execute('''SELECT t.teacher FROM teachers as t''').fetchall()))
            QMessageBox.about(self, "Результат", "Учитель успешно добавлен!")
        con.commit()
        con.close()

    def add_new_class(self, item):
        con = sqlite3.connect("database_for_project_activity.db")

        # Создание курсора
        cur = con.cursor()
        if item in self.classes:
            em = QMessageBox()
            em.setText("Данный класс уже есть в базе!")
            em.setWindowTitle("Ошибка")
            em.exec_()
        else:
            new_id = int(cur.execute('''SELECT id FROM classes WHERE 
                                                  id = (SELECT MAX(id) FROM classes)''').fetchone()[0]) + 1
            cur.execute(f'''INSERT INTO classes(id, class) VALUES({new_id}, ('{item}'))''')
            self.classes = list(map(lambda x: x[0], cur.execute('''SELECT c.class FROM classes as c''').fetchall()))
            QMessageBox.about(self, "Результат", "Класс успешно добавлен!")
        con.commit()
        con.close()

    def add_new_year(self, item):
        con = sqlite3.connect("database_for_project_activity.db")

        # Создание курсора
        cur = con.cursor()
        if item in self.classes:
            em = QMessageBox()
            em.setText("Данный класс уже есть в базе!")
            em.setWindowTitle("Ошибка")
            em.exec_()
        else:
            new_id = int(cur.execute('''SELECT id FROM years WHERE 
                                                  id = (SELECT MAX(id) FROM years)''').fetchone()[0]) + 1
            cur.execute(f'''INSERT INTO years(id, year) VALUES({new_id}, ('{item}'))''')
            self.years = list(map(lambda x: x[0], cur.execute('''SELECT y.year FROM years as y''').fetchall()))
            QMessageBox.about(self, "Результат", "Год успешно добавлен!")
        con.commit()
        con.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = MyMainWindow()
    example.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
