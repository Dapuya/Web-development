import math

# a
# n = int(input())
# a = list(input().split(' '))
# for i in range(0, n):
#     if i%2==0:
#         print(a[i], end=' ')


# b
# n = int(input())
# a = list(input().split(' '))
# for i in range(0, n):
#     if a[i]%2==0:
#         print(a[i], end=' ')


# c
# n = int(input())
# a = [int(x) for x in input().split()]
# cnt = 0
# for i in a:
# 	if i > 0: cnt += 1
# print(cnt)


# d
# n = int(input())
# a = [int(x) for x in input().split()]
# cnt = 0
# for i in range(1, n):
# 	if a[i] > a[i - 1]: cnt += 1
# print(cnt)


# e
# n = int(input())
# a = [int(x) for x in input().split()]
# for i in range(1, n):
#     if a[i] * a[i - 1] > 0:
#         print('YES')
#         exit()
# print('NO')


# f
# n = int(input())
# a = [int(x) for x in input().split()]
# cnt = 0
# for i in range(1, n - 1):
#     if a[i] > a[i - 1] and a[i] > a[i + 1]: cnt += 1
# print(cnt)


# g
n = int(input())
a = [int(x) for x in input().split()]
for i in range(n-1, -1, -1):
	print(a[i], end=' ')
