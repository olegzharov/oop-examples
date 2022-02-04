# Proxy Design Pattern
from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def person_method(self):
        """ Interface Method"""


class Person(IPerson):

    def person_method(self):
        print('I\'m person')


class ProxyPerson:

    def __init__(self):
        self.person = Person()

    def person_method(self):
        print('I\'m proxy method functionality')
        self.person.person_method()


p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()
