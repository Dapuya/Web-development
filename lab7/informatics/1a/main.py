import math


# a
# a = int(input())
# b = int(input())
#
# print(math.sqrt(a ** 2 + b ** 2))


# b
# a = int(input())
# b = a + 1
# c = a - 1
# print( (f"The next number for the number {a} is {b}. "))
# print( (f"The previous number for the number {a} is {c}. "))


# c
# a = int(input())
# b = int(input())
# c = int(b/a)
# print( c )


# d
# a = int(input())
# b = int(input())
# c = b%a
# print( c )


# e
# v = int(input())
# t = int(input())
# print((v*t)%109)


# f
# a = int(input())
# print(a%10)


# g
# a = int(input())
# print(a//10)


# h
# a = int(input())
# print(a%100//10)


# i
# a = int(input())
# b = a//100
# c = a%100//10
# d = a%10
# print(b+c+d)


# j
# a = int(input())
# print( 2*(a//2) +2 )


# k
# a = int(input())
# if a < 1440:
#     b = a//60
#     c = a%60
#     print(f"{b} {c}")
#     #print(b, " ", c)
# if a>1440:
#     d = int((a - (a//1440)*1440)//60)
#     e = int((a - (a//1440)*1440)%60)
#     print(f"{d} {e} ")
# if a==1440:
#     print(0, 0)


# l
# n = int(input())
# n %= 86400
# m = n % 3600
# print('{}:{:02d}:{:02d}'.format(n // 3600, m // 60, m % 60))


# m
# a = input ()
# b = input ()
# c = a
# a = b
# b = c
# print (a, b)


# n
# a = int(input())
# if a == 1:
#     print("9 45")
# if a == 2:
#     print("10 35")
# if a == 3:
#     print("11 35")
# if a == 4:
#     print("12 25")
# if a == 5:
#     print("13 25")
# if a == 6:
#     print("14 15")
# if a == 7:
#     print("15 15")
# if a == 8:
#     print("16 05")
# if a == 9:
#     print("17 05")
# if a == 10:
#     print("17 55")


# o
# a = int(input())
# b = int(input())
# n = int(input())
# r = a*n
# k = b*n
# if k >= 100:
#     r = r + k//100
#     k = k%100
# print(r, k)


# p
# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
# b1 = int(input())
# b2 = int(input())
# b3 = int(input())
# s1 = a1*3600 + a2*60 + a3
# s2 = b1*3600 + b2*60 + b3
# print(s2-s1)


# q
# n = int(input())
# m = int(input())
# print(m/n+(m%n+n-1)/n)


# r
# a = int(input())
# b = int(input())
# c = b%a
# if c == 0:
#     print(0)
# if c != 0:
#     print(a - c)


# s
# h = int(input())
# a = int(input())     # a > b
# b = int(input())
# print(int(1 + (h - b - 1) / (a - b)))


# t
# n = int(input())
# m = ((n%10)*1000+((n//10)%10)*100+((n//100)%10)*10+((n//1000)%10))
# print(m-n + 1)


# u
# n = int(input())
# m = int(input())
# x = n%m
# y = m%n
# print(x*y +1)


# v
# a=int(input())
# b=int(input())
# print((((a // b) * a) + ((b // a) * b)) // ((a // b) + (b // a)))
