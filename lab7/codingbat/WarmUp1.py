def sleep_in(weekday, vacation):
    return not weekday or vacation


def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile


def sum_double(a, b):
    if a == b: return 2 * (a + b)
    return a + b


def diff21(n):
    if n <= 21: return 21 - n
    return 2 * (n - 21)


def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)


def pos_neg(a, b, negative):
    if negative: return a < 0 and b < 0
    return a * b < 0


def not_string(str):
    if str[:3] != 'not': str = 'not ' + str
    return str


def missing_char(str, n):
    return str[:n] + str[n + 1:]


def front_back(str):
    if len(str) <= 1: return str
    mid = str[1:len(str) - 1]
    return str[-1] + mid + str[0]


def front3(str):
    s = str[:3]
    return s + s + s


def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10