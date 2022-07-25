def my_decorator(func):
    def wrapper(*args):
        data = {'first': args[0].upper(), 'second': args[1].upper()}
        return func(**data)
    return wrapper


def names(first, second):
    print("Your first name are {} and second name is {}".format(first, second))


name = my_decorator(names)
name('Jonh', 'Doe')
