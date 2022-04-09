def combo_string(a, b):
    if (len(a) < len(b)): return a + b + a
    return b + a + b


def extra_end(str):
    return str[-2:] + str[-2:] + str[-2:]


def first_half(str):
    return str[:len(str) // 2]


def first_two(str):
    return str[:2]


def hello_name(name):
    return 'Hello ' + name + '!'


def left2(str):
    return str[2:] + str[:2]


def make_abba(a, b):
    return a + b + b + a


def make_out_word(out, word):
    return out[:2] + word + out[2:]


def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'


def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'


def without_end(str):
    return str[1:-1]


def non_start(a, b):
  return a[1:] + b[1:]