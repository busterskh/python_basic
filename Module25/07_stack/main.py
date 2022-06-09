class Steck:
    def __init__(self):
        self.__steck = []

    def __str__(self):
        return '; '.join(self.__steck)

    def push(self, element):
        self.__steck.append(element)

    def pop(self):
        if len(self.__steck) == 0:
            return None
        else:
            self.__steck.pop()


class TaskManager:
    def __init__(self):
        self.task_data = dict()

    def __str__(self):
        display = []
        if self.task_data:
            for i_priority in sorted(self.task_data.keys()):
                display.append("\n{0} {1}".format(str(i_priority), self.task_data[i_priority]))

        return " ".join(display)

    def new_task(self, task, priority):
        if priority not in self.task_data:
            self.task_data[priority] = Steck()
        self.task_data[priority].push(task)

    def delete(self, priority):
        if priority in self.task_data:
            self.task_data[priority].pop()


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
