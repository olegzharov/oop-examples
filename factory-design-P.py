from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def person_method(self):
        """ Interface Method"""

class Student(IPerson):
    def __init__(self):
        self.name = 'Basic Student Name'

    def person_method(self):
        print('I\'m student')

class Teacher(IPerson):
    def __init__(self):
        self.name ='Basic Teacher Name'

    def person_method(self):
        print('I\'m teacher')

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == 'Student':
            return Student()
        elif person_type == 'Teacher':
            return Teacher()
        else:
            raise ValueError

if __name__ == '__main__':
    choice = input('What type of person do you want to create?\n')
    person = PersonFactory.build_person(choice)
    person.person_method()



# doesn't work
# p1 = IPerson()
# p1.person_method()
# s1 = Student()
# s1.person_method()
# t1 = Teacher()
# t1.person_method()

