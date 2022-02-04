# Singleton Design Pattern
from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def print_data():
        """ Implement in child class"""


class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            print('Error!')
            PersonSingleton('Default Name, 0')
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            print(f'Instance: {PersonSingleton.__instance}')
            raise Exception('Singleton cannot be instantiated more than once')
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f'Name: {PersonSingleton.__instance.name}, Age: '
              f'{PersonSingleton.__instance.age}')


p = PersonSingleton('Mike', 30)
print(p)
p.print_data()

#exception
# p2 = PersonSingleton('Bob', 30)
p2 = PersonSingleton.get_instance()
print(p2)
p2.print_data()