def double_char(str):
  s = ''
  for i in str:
    s += i * 2
  return s


def count_hi(str):
  return str.count('hi')



def cat_dog(str):
  return True if str.count('cat') == str.count('dog') else False


def count_code(str):
  count = 0
  for i in range(len(str)):
    if str[i:i+2] == "co" and str[i+3:i+4] == "e":
      count+=1
  return count


def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return True if (a in b or b in a) and a[-1] == b[-1] else False


def xyz_there(str):
  if str[:3] == "xyz":
    return True
  for i in range(1, len(str) - 2):
    if str[i-1] != "." and str[i:i+3] == "xyz":
      return True
  return False