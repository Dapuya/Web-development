# This is a sample Python script.
# a
# def min4(a, b, c, d):
#     return min(min(a, b), min(c, d))
#
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(min4(a,b,c,d))


# b
# def power(a, n):
#     return a ** int(n)
#
#
# a = [float(x) for x in input().split()]
# print(power(a[0], a[1]))


# c
# def xor(a, b):
#     return a ^ b
#
#
# a = [int(x) for x in input().split()]
# print(xor(a[0], a[1]))


# g
def power(a, n):
    return (a**n)


a, n = input().split(' ')
print(power(float(a), int(n)))

