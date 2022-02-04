# class Person:
#     def __init__(self, name, age):
#         self.name: str = name
#         self.age: int = age
#
#     def __del__(self):
#         print('Object is beign deleted')
#
# p = Person('Oleg', 56)
# print(p.__dict__)
# print(p)

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'X: {self.x}, Y: {self.y}'
# OR def __repr__:
    def __len__(self):
        return 10

    def __call__(self, *args, **kwargs):
        print('Hello, I was called')
v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2
print(v3.x)
print(v3.y)
print(v3)
print(len(v3))
v3()