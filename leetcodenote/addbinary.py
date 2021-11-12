import time


def t(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        func(*args, **kwargs)
        end = time.time_ns()
        print(end-start)
        return end-start
    return wrapper


@t
def addbinRecursive(x, y):

    def inner(x, y):
        if y == 0:
            return x
        else:
            return inner(x ^ y, (x & y) << 1)
    b = inner(x, y)
    return b


@t
def addbinIterative(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    # print(x)
    return x


# print(addbinRecursive(545666, 111123))
print(addbinRecursive(54534634563461251243512341324566654534634563461251243512341324566654534634563461251243512234234232342342423434132456665453463456346125124351234132456612124242434233336,
                      545346345634612512435123413245666545346345634612512435123413245666545346345634612512435123413245666545346345634612512435123413245666))
