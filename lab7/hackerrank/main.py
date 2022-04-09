# 1
# n = int(input())
# if n%2==1:
#     print("Weird")
# if n%2==0 and 1<n<6:
#     print("Not Weird")
# if n%2==0 and 5<n<21:
#     print("Weird")
# if n%2==0 and n>20:
#     print("Not Weird")


# 2
# a = int(input())
# b = int(input())
# print(a+b)
# print(a-b)
# print(a*b)


# 3
# a = int(input())
# b = int(input())
# print(a // b)
# print(a / b)


# 4
# n = int(input())
# for i in range(n):
#     print(i*i)


# 5
# def is_leap(year):
#     leap = False
#     if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#         leap = True
#
#     return leap
#
#
# year = int(input())
# print(is_leap(year))


# 6
# n = int(input())
# for i in range(1,n+1):
#     print(i, end='')


# 7
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# print([[ i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (( i + j + k) != n )])


# 8
# def mutate_string(string, position, character):
#     return string[:position] + character + string[position + 1:]
#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# 9
# print('Hello, World!')


# 10
# def swap_case(s):
#     res = ''
#     res = ''.join([i.lower() if i.isupper() else i.upper() for i in s])
#     return res
#
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)