import random
import datetime
import re

# age, name , weight = input('age\n'), input('name\n'), input('weight\n')
#
# user = (age, name, weight)
#
# print(user)


# def delete_duplicates(arr):
#     return list(set(arr))
#
#
# print(delete_duplicates([1, 2, 3, 5, 5]))
#
# _ = {1, 1, 3, 4, 6, 15, 15, 1}
#
# for __ in _:
#     print(type(__))
#
# _2 = {'str', 'me'}
#
# _all = _.union(_2)
#
# # _all.update('sad')  # only iterable data
#
# _all.add('sad')
#
# # _all.remove('2')  # if given argument is not exist in set object it throws error
#
# _all.discard(1)  # if given argument is not exist in set object it doesn't throw error
#
# _clone_set = _all.copy()
#
# print(_all)

# nums = set(list(range(20)))

# print(nums)

# TASK 1

# def biggest_one(a, b, c):
#     return max([a, b, c])
#
#
# def smallest_one(a, b, c):
#     return min([a, b, c])
#
#
# def add_small_ones(a, b, c):
#     _list = [a, b, c]
#     _list.sort()
#     return _list[0] + _list[1]
#
#
# def mul_biggest_ones(a, b, c):
#     _list = [a, b, c]
#     _list.sort(reverse=True)
#     return _list[0] * _list[1]


# print(biggest_one(1, 2, 3))
# print(smallest_one(4, 5, 6))
# print(add_small_ones(3, 4, 5))
# print(mul_biggest_ones(10, 5, 15))


# def unnamed_task(a, b, c):
#     for i in range(a):
#         b += c + 1
#         if b >= 100:
#             print('Iteration broke out')
#             break
#     else:
#         print('The end')
#
#
# unnamed_task(
#     10, 10, 10
# )

# def is_pizza_enough(pizza, people):
#     return pizza % people == 0


# _list = [random.randint(0, 200) for x in range(50)]
# k = 0
# kn = 0
#
# for i in _list:
#     if i % 2 == 0:
#         k += 1
#     else:
#         kn += 1
# else:
#     print(f'Juft {k}\nToq {kn}')


# def sort_k_n(arr):
#     k = []
#     for i in arr:
#         if i % 2 == 0:
#             k.append("Juft " + str(i))
#         else:
#             k.insert(0, "Toq " + str(i))
#     print(k)
# # Or
#
# def sort_k_n(arr):
#     k , n = [], []
#     for i in arr:
#         if i % 2 == 0:
#             k.append(i)
#         else:
#             n.append(i)
#     else:
#         k.append('|$|')
#         k.extend(n)
#         print(k)

#  Dictionary
import time

# _dict = {
#     "name": "Strange",
#     "age": 15,
#     "more": {
#         "more > 1": "sad"
#     }
# }
#
# # print(_dict)
#
#
# __dict = {
#     "name": "Name",
#     "name": "Sad"
# }
# # __dict.name = "Sad"
#
#
# __dict_empty = {
#     "sad" : 1,
#     "SAD" : 'sad'
# }
#
# print(__dict_empty.pop('sad'))
# print(__dict_empty)
# person = {
#     "name": 'sad',
#     "age": 'sad'
# }
#
# import datetime
#
# import locale
#
# locale.setlocale(locale.LC_ALL, "uz_Latn_uz")
#
# dt = datetime.datetime.now()
#
# # Date
#
# hours = dt.hour + 12  # 12 for 24 hour support
#
# minutes = dt.minute
#
# td1 = datetime.timedelta(hours=hours, minutes=minutes)
#
# td2 = datetime.timedelta(hours=2)
#
# # print(td1 - td2)
# import time
#
# t = time.strftime("%d:%m:%Y:%M:%S:%D:%j:%A:%I:%p:%z")
# print(t)

# def del_dup(s):
#     a = {}
#     for i in s:
#         a[i] = a[i] + 1 if a.get(i) else 1
#     return "".join(list(a.keys()))
#
#
# def most_used_charOf(s):
#     a = {}
#     for i in s:
#         a[i] = a[i] + 1 if a.get(i) else 1
#     maxCount = 0
#     maxChar = ''
#     for i in a:
#         if a[i] > maxCount:
#             maxCount = a[i]
#             maxChar = i
#
#     return {
#         "max_used_char": maxChar,
#         "count": maxCount
#     }
#
# print(
#     most_used_charOf('hello world')
# )


def task1(s):
    a = list(s)
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            a.pop(i)
            a.append('')
    return "".join(a)


def task2(s):
    temp = ''
    for i in range(len(s)):
        if i % 2 == 0:
            temp += s[i].upper()
        else:
            temp += s[i].lower()
    return temp

# print(task2("hello"))


def task3(x):
    a = x[::-1]
    d = ""
    for i, s in enumerate(a):
        d += str(i) + s
    return d[::-1]


def task4(x):
    s = "abcdefghijklmnopqrstuvwxyz"
    up = {}
    d = 1
    for i in s:
        up[i] = d
        d += 1
    t = ''
    for i in x:
        t += i + str(up[i])
    return t


task5 = lambda __: [ord(_) for _ in __]


def task6(x):
    s = "aoeuyi"
    d = ''
    for i in x:
        d += i * 2 if i in s else i
    return d


def task7(x, y):
    t1 = re.split('[.:]', x)
    t1 = [int(_) for _ in t1]
    t2 = re.split('[.:]', y)
    t2 = [int(_) for _ in t2]
    d1 = datetime.datetime(day=t1[0], month=t1[1], year=t1[2], hour=t1[3], minute=t1[4], second=t1[5])
    d2 = datetime.datetime(day=t2[0], month=t2[1], year=t2[2], hour=t2[3], minute=t2[4], second=t2[5])
    return d1 - d2


def task8(x, y):
    t1 = x.split(':')
    t1 = [int(_) for _ in t1]
    d1 = datetime.timedelta(hours=t1[0], minutes=t1[1])
    d2 = datetime.timedelta(hours=y)
    print(d1 + d2)

task8("22:30", 7)
# print(task7("02.12.2022.18:32:24", "02.12.2021.13:00:14"))


