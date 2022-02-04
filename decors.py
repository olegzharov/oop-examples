
def mydecorator(function):

    def wrapper(*args, **kwargs):
        print('I \'m decorating your function')
        ret_value = function(*args, **kwargs)
        return  ret_value
    return wrapper

@mydecorator
def h_w(person):
    # print(f'Hello {person}')
    return f'Hello {person}'
# mydecorator(h_w)()
h_w('Oleg')
print(h_w('Mike'))
