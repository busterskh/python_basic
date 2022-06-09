class MyDict:
    __dictionary = dict()

    def __init__(self, **kwargs):
        self.set_key(**kwargs)

    def set_key(self, **kwargs):
        for key, value in kwargs.items():
            self.__dictionary[key] = value

    def get_key(self):
        search_key = input('Какой ключ ищем? ')
        if search_key in self.__dictionary.keys():
            return self.__dictionary[search_key]
        else:
            return 0


my_dict = MyDict(name="Tom", age=28, gender="man", family_status="free")
print(my_dict.get_key())
