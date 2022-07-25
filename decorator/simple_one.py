def upper_case(func):
    def wrapper():
        f = func()
        return f.upper()

    return wrapper


def split_words(func):
    def wrpapper():
        f = func().split()
        return f

    return wrpapper


@split_words
@upper_case
def hello_function():
    return "the name is beautiful"


print(hello_function())
# result = upper_case(hello_function)
# print(result())
