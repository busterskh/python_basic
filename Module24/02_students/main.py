class Student:

    def __init__(self, name, group, academic_performance):
        self.name = name
        self.group = group
        self.academic_performance = academic_performance

    def output_info(self):
        print('\nФИ: {}\nГруппа: {}\nУспеваемость: {}\n'.format(self.name,
                                                                self.group,
                                                                ', '.join(self.academic_performance)
                                                                )
              )


def create_students_list():
    for _ in range(10):
        name = input('Введите имя студента: ')
        group = input('Введите группу: ')
        academic_performance = input('Введите успеваемость через пробел: ').split()
        middle_rating = sum(int(i) for i in academic_performance) / len(academic_performance)
        i_student = Student(name, group, academic_performance)
        students_list.append((middle_rating, i_student))


students_list = []
create_students_list()
students_list.sort(reverse=True)

for student in students_list:
    student[1].output_info()
