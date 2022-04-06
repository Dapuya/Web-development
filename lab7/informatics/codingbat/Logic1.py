def cigar_party(cigars, is_weekend):
    if is_weekend: return 40 <= cigars
    return 40 <= cigars <= 60



def date_fashion(you, date):
  if you <= 2 or date <= 2: return 0
  if you >= 8 or date >= 8: return 2
  return 1


def squirrel_play(temp, is_summer):
  if is_summer: return 60 <= temp <= 100
  return 60 <= temp <= 90


def caught_speeding(speed, is_birthday):
  if is_birthday: speed -= 5
  if speed <= 60: return 0
  elif speed >= 81: return 2
  elif 80 >= speed >= 61: return 1


def sorta_sum(a, b):
    if 10 <= a + b <= 19: return 20
    return a + b


def alarm_clock(day, vacation):
    if vacation:
        if day == 0 or day > 5:
            return 'off'
        else:
            return '10:00'
    else:
        if day == 0 or day > 5:
            return '10:00'
        else:
            return '7:00'



def love6(a, b):
  return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6


def in1to10(n, outside_mode):
  if outside_mode:
    return n <= 1 or n >= 10
  else:
    return n >= 1 and n <= 10



def near_ten(num):
  a = num % 10
  return (10 - (10-a)) <= 2 or (10 - a) <= 2