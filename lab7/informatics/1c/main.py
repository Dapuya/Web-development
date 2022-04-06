import math

# FOR

# a
# a = int(input())
# b = int(input())
# for i in range(a, b+1):
#     if i%2==0:
#         print(i)


# b
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# for i in range(a, b+1):
#     if i%d ==c:
#         print(i)


# c
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
# 	x = int(math.sqrt(i))
# 	if x * x == i: print(i, end = ' ')


# d
# x = int(input())
# d = int(input())
# print(str(x).count(str(d)))


# e
# x = int(input())
# summa = 0
# while x > 0:
#     temp = x%10
#     summa += temp
#     x //= 10
# print(summa)


# f
# x = int(input())
# summa = 0
# while x>0:
#     temp = x%10
#     x //= 10
#     summa *= 10
#     summa += temp
#
# print(summa)


# g
# x = int(input())
# for i in range(2, x + 1):
# 	if x % i == 0:
# 		print(i)
# 		break


# h
# x = int(input())
# for i in range(1, x + 1):
# 	if x % i == 0:
# 		print(i, end = ' ')


# i
# n = int(input())
# x = int(math.sqrt(n))
# cnt = 0
# for i in range(1, x):
#     if n % i == 0: cnt += 2
# if n % x == 0: cnt += 1
# print(cnt)


# j
# cnt = 0
# for i in range(100):
#     cnt += int(input())
# print(cnt)


# k
# n = int(input())
# summa = 0
# for i in range(0, n):
#     x = int(input())
#     summa += x
# print(summa)


# l
# print(int(input(), 2))


# m
# n = int(input())
# cnt = 0
# for i in range(0, n):
#     x = int(input())
#     if x == 0:
#         cnt += 1
# print(cnt)




#  WHILE

# a
# n = int(input())
# i = 1
# while n > 0 and i <= n:
#     x = int(math.sqrt(i))
#     if x * x == i:
#         print(i)
#     i += 1


# b
# n = int(input())
# i = 2
# while True:
#     if n % i == 0:
#         print(i)
#         break
#     i += 1


# c
# def check(x):
#     while x % 2 == 0:
#         x //= 2
#     return x == 1
#
# n = int(input())
#
# for i in range(1, n + 1):
#     if check(i):
#         print(i, end = ' ')


# d
# def check(x):
#     while x % 2 == 0:
#         x //= 2
#     return x == 1
#
# n = int(input())
# if check(n):
#     print('YES')
# else:
#     print('NO')


# e
x = int(input())
print(math.ceil(math.log2(x)))