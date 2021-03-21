class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.all_grades = []

    def lecturer_rating(self):
        for val in self.grades.values():
            self.all_grades += val

    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.all_grades < lecturer.all_grades

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} ' \
               f'\nСредняя оценка за лекции: {round(sum(self.all_grades) / len(self.all_grades), 1)}'


lecturer_1 = Lecturer('Oleg', 'Buligyn')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Алена', 'Батицкая')
lecturer_2.courses_attached += ['Git']


class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.all_grades = []

    def lecturer_score(self, lecturer, course, grades):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades and 0 < grades < 10:
                lecturer.grades[course] += [grades]
            else:
                lecturer.grades[course] = [grades]
        else:
            return 'Ошибка'

    def student_rating(self):
        for val in self.grades.values():
            self.all_grades += val

    def __lt__(self, student):
        if isinstance(student, Student):
            return self.all_grades < self.all_grades

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние занятия: ' \
               f'{round(sum(self.all_grades) / len(self.all_grades), 1)} ' \
               f'\nКурсы в процессе изучения: {self.courses_in_progress}' \
               f'\nЗавершенные курсы: {self.finished_courses}'


student_1 = Student('Olga', 'Star')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Elena', 'Solopan')
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']


class Reviewer(Mentor):
    def student_score(self, student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grades]
            else:
                student.grades[course] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


reviewer_1 = Reviewer('Some', 'Body')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Any', 'Body')
reviewer_2.courses_attached += ['Git', 'Python']

print('Информация о проверяющих:')
print(reviewer_1)
print()
print(reviewer_2)
print()

student_1.lecturer_score(lecturer_1, 'Python', 10)
student_1.lecturer_score(lecturer_1, 'Python', 9)
student_1.lecturer_score(lecturer_1, 'Git', 9)
student_2.lecturer_score(lecturer_1, 'Git', 8)
student_1.lecturer_score(lecturer_2, 'Git', 8)
student_2.lecturer_score(lecturer_2, 'Git', 8)

lecturer_1.lecturer_rating()
lecturer_2.lecturer_rating()

print('Информация о лекторах:')
print(lecturer_1)
print()
print(lecturer_2)
print()

reviewer_1.student_score(student_1, 'Python', 8)
reviewer_1.student_score(student_1, 'Python', 8)
reviewer_2.student_score(student_1, 'Python', 9)
reviewer_2.student_score(student_1, 'Git', 10)
reviewer_2.student_score(student_2, 'Git', 8)

student_1.student_rating()
student_2.student_rating()

print('Информация о студентах:')
print(student_1)
print()
print(student_2)
print()

print('Средняя оценка за лекции у lecturer_1 больше, чем у lecturer_2 ?')
print(lecturer_1 > lecturer_2)
print()
print('Средняя оценка за домашние задания у student_1 больше, чем у student_2 ?')
print(student_1 > student_2)

student_list = [student_1, student_2]


def average_grade_students(course):

    average_grade_student_course = 0
    counter = 0
    for student in student_list:
        if course in student.courses_in_progress:
            average_grade_student_course += sum(student.grades[course]) / len((student.grades[course]))
            counter += 1
        else:
            pass
    return round((average_grade_student_course/counter), 1)


print()
print('Средняя оценка за домашние задания по всем студентам в рамках курса Python:')
print(average_grade_students('Python'))
print()
print('Средняя оценка за домашние задания по всем студентам в рамках курса Git:')
print(average_grade_students('Git'))
print()

lecturer_list = [lecturer_1, lecturer_2]


def average_grade_lecturers(course):

    average_grade_lecturer_course = 0
    counter = 0
    for lecturer in lecturer_list:
        if course in lecturer.courses_attached:
            average_grade_lecturer_course += sum(lecturer.grades[course]) / len(lecturer.grades[course])
            counter += 1
        else:
            pass
    return round((average_grade_lecturer_course/counter), 1)


print('Средняя оценка за лекции по всем лекторам в рамках курса Python:')
print(average_grade_lecturers('Python'))
print()
print('Средняя оценка за лекции по всем лекторам в рамках курса Git:')
print(average_grade_lecturers('Git'))