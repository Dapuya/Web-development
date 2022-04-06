def make_bricks(small, big, goal):
	if big * 5 == goal or small == goal:
		return True
	if big * 5 > goal:
		goal %= 5
		return goal <= small
	goal -= big * 5
	return goal <= small


def lone_sum(a, b, c):
    if a != b and a != c and b != c:
        return a + b + c
    if a != b and a != c and b == c:
        return a
    if a != b and a == c and b != c:
        return b
    if a == b and a == c and b == c:
        return 0
    if a == b and a != c and b != c:
        return c


def lucky_sum(a, b, c):
  	n = [a, b, c]
  	s = 0
  	for i in range(3):
            if n[i] == 13:
                break
            s += n[i]
  	return s


def fix_teen(n):
    if n < 13 or n > 19:
        return True
    if n == 15 or n == 16:
        return True
    return False


def no_teen_sum(a, b, c):
    s = 0
    n = [a, b, c]
    for i in n:
        if fix_teen(i):
            s += i
    return s



def round_sum(a, b, c):
  	return round10(a) + round10(b) + round10(c)

def round10(num):
    r = num % 10
    if r >= 5: return num + 10 - r
    else: return num - r



def close_far(a, b, c):
  	if abs(b - a) <= 1 and abs(c - a) >= 2 and abs(c - b) >= 2: return True
  	if abs(c - a) <= 1 and abs(b - a) >= 2 and abs(c - b) >= 2: return True
  	return False



def make_chocolate(small, big, goal):
	if big * 5 == goal: return 0
	if big * 5 > goal:
		goal %= 5
		if goal <= small: return goal
		return -1
	goal -= big * 5
	if goal <= small: return goal
	return -1