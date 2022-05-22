class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in mentor.courses_attached and course in self.courses_in_progress:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average_score = float(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])))
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {average_score}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def average_score_work(self):
        res_1 = float(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])))
        return res_1

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Не студент")
            return
        if self.average_score_work() > other.average_score_work():
            return f'Средний балл у {self.name} {self.surname} ({self.average_score_work()}) - ВЫШЕ, ' \
                   f'чем среднний бал у {other.name} {other.surname} ({other.average_score_work()})!'
        if self.average_score_work() < other.average_score_work():
            return f'Средний балл у {self.name} {self.surname} ({self.average_score_work()}) - НИЖЕ, ' \
                   f'чем среднний бал у {other.name} {other.surname} ({other.average_score_work()})!'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        average_score = float(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])))
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {average_score}'
        return res

    def average_score_work(self):
        res_1 = float(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])))
        return res_1

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Не лектор")
            return
        if self.average_score_work() > other.average_score_work():
            return f'Средний балл у {self.name} {self.surname} ({self.average_score_work()}) - ВЫШЕ, ' \
                   f'чем среднний бал у {other.name} {other.surname} ({other.average_score_work()})!'
        if self.average_score_work() < other.average_score_work():
            return f'Средний балл у {self.name} {self.surname} ({self.average_score_work()}) - НИЖЕ, ' \
                   f'чем среднний бал у {other.name} {other.surname} ({other.average_score_work()})!'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


def course_student_average_score(student_list, course):
    new_list = []
    for student in student_list:
        if course in student.courses_in_progress:
            new_list.append(student.grades[course])
            average_score = float(sum(sum(new_list, [])) / len(sum(new_list, [])))
    return print(f'Средняя оценка СТУДЕНТОВ по курсу "{course}": {average_score}')


def course_lector_average_score(lector_list, course):
    new_list = []
    for lector in lector_list:
        if course in lector.courses_attached:
            new_list.append(lector.grades[course])
            average_score = float(sum(sum(new_list, [])) / len(sum(new_list, [])))
    return print(f'Средняя оценка ЛЕКТОРА по курсу "{course}": {average_score}')

#Параметры экземпляров

july_student = Student("July", "Sun")
july_student.courses_in_progress += ["Python", "Java", "English", "History"]
july_student.add_courses("'Как управлять миром и не сойти с ума'")

harry_student = Student("Harry", "Potter")
harry_student.courses_in_progress += ["Python", "Java", "French", "History"]
harry_student.add_courses("'мОлоко не мАлоко: основы русского языка'")

johny_lecturer = Lecturer("Johny", "Walker")
johny_lecturer.courses_attached += ["English", "French", "History"]
july_student.rate_hw(johny_lecturer, "English", 10)
july_student.rate_hw(johny_lecturer, "History", 8)
harry_student.rate_hw(johny_lecturer, "French", 8)
harry_student.rate_hw(johny_lecturer, "History", 7)

jack_lecturer = Lecturer("Jack", "Daniels")
jack_lecturer.courses_attached += ["Python", "Java"]
july_student.rate_hw(jack_lecturer, "Python", 8)
july_student.rate_hw(jack_lecturer, "Java", 7)
harry_student.rate_hw(jack_lecturer, "Python", 9)
harry_student.rate_hw(jack_lecturer, "Java", 10)

tony_check = Reviewer("Tony", "Stark")
tony_check.courses_attached += ["English", "French", "History"]
tony_check.rate_hw(july_student, "English", 8)
tony_check.rate_hw(july_student, "History", 7)
tony_check.rate_hw(harry_student, "French", 9)
tony_check.rate_hw(harry_student, "History", 10)

hulk_check = Reviewer("Hulk", "Green")
hulk_check.courses_attached += ["Python", "Java"]
hulk_check.rate_hw(july_student, "Python", 10)
hulk_check.rate_hw(july_student, "Java", 7)
hulk_check.rate_hw(harry_student, "Python", 9)
hulk_check.rate_hw(harry_student, "Java", 8)

student_list_1 = [harry_student, july_student]
lector_list_1 = [johny_lecturer, jack_lecturer]

#Вывод информации

print(july_student)
print()
print(harry_student)
print()
print(johny_lecturer)
print()
print(jack_lecturer)
print()
print(tony_check)
print()
print(hulk_check)
print()

print(harry_student > july_student)
print(july_student > harry_student) #почему про студента пишет, а если поставить "лектора", то выдает ошибку (вместо "Не студент")?
harry_student.__lt__(hulk_check) #почему в таком выводе возращает "Не студент", но ничего не возращает, если указать студента (july_student)?
print()

print(jack_lecturer > johny_lecturer)
print(johny_lecturer > jack_lecturer)
jack_lecturer.__lt__(hulk_check)
print()

course_student_average_score(student_list_1, "Python")
course_lector_average_score(lector_list_1, "Python")
course_student_average_score(student_list_1, "Java")
course_lector_average_score(lector_list_1, "Java")
course_student_average_score(student_list_1, "History")
course_lector_average_score(lector_list_1, "History")
course_student_average_score(student_list_1, "English")
course_lector_average_score(lector_list_1, "English")
course_student_average_score(student_list_1, "French")
course_lector_average_score(lector_list_1, "French")


