class Person:
    def __init__(self, name, surname, age):
        self.__name = self.set_name(name)
        self.__surname = self.set_surname(surname)
        self.__age = self.set_age(age)

    def set_name(self, name):
        return name.title()

    def set_surname(self, surname):
        return surname.title()

    def set_age(self, age):
        if 90 > age > 18:
            return age
        else:
            raise Exception('Недопустимый возраст.')

    def get_info(self):
        return self.__name, self.__surname


class Employee:
    def manager_salary(self):
        return 13000

    def agent_salary(self, sales):
        percent = sales / 100 * 5
        return 5000 + percent

    def worker_salary(self, hours):
        return 100 * hours


class Manager(Person, Employee):
    def __init__(self, name, surname, age):
        super(Manager, self).__init__(name, surname, age)
        self.salary = self.manager_salary()


class Agent(Person, Employee):
    def __init__(self, name, surname, age, sales):
        super(Agent, self).__init__(name, surname, age)
        self.salary = self.agent_salary(sales)


class Worker(Person, Employee):
    def __init__(self, name, surname, age, hours):
        super(Worker, self).__init__(name, surname, age)
        self.salary = self.worker_salary(hours)


def create_list_employee():
    for _ in range(3):
        print('Добавляем менеджеров:')
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        age = int(input('Введите возраст: '))
        employee_list.append(Manager(name, surname, age))

    for _ in range(3):
        print('\nДобавляем агентов:')
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        age = int(input('Введите возраст: '))
        sales = int(input('На какую сумму продал {}: '.format(name)))
        employee_list.append(Agent(name, surname, age, sales))

    for _ in range(3):
        print('\nДобавляем рабочих:')
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        age = int(input('Введите возраст: '))
        hours = int(input('Сколько часов отработал {}: '.format(name)))
        employee_list.append(Worker(name, surname, age, hours))


employee_list = []
create_list_employee()
print()
for employee in employee_list:
    print(' '.join(employee.get_info()), employee.salary)
