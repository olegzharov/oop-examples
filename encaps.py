class Person:

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

# для доступа к ним надо определить вот что
    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        if value == 'Oleg':
            self.__name = value
        else:
            raise ValueError

    @staticmethod
    def mymethod():
        print('My method called')

p1 = Person('Mike', 56, 'm')
print(p1.Name)
p1.Name='Oleg'
print(p1.Name)
Person.mymethod()
p1.mymethod()