# booleans

# task 1
# def function(x):
#     if  x  > 0:return x + 1
#     else:return x

# task 2
# def function(x):
#     if  x > 0:
#         return x + 1
#     else:
#         return x - 2

# task 3
# def function(x):
#     if x > 0:
#         return x + 1
#     elif x == 0:
#         return 10
#     else:
#         return x - 2

# task 4
# def function(n1, n2, n3):
#     l = []
#     l.append(n1)
#     l.append(n2)
#     l.append(n3)
#     n = 0
#     for i in l:
#         if i > 0:
#             n += 1
#     return n


# print(function(1, 2, -5))

# task 5
# def palindrome(s):
# return str(s)[::-1] == str(s)


# task 6
# def rimToNumber(x):
#     rim = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100,
#         "D": 500,
#         "M": 1000
#     }
#     result = 0
#     for i in range(len(x)):
#         current = rim[x[i]]
#         nexT = rim[x[i + 1]]
#         if current < nexT:
#             result += nexT - current
#             continue
#         else:
#             result += current
#     return result


# print(rimToNumber('XIV'))
#  not worked

from faker import Faker
import random
faker = Faker()
# with open('README', 'w+') as R:
#     for i in range(100):
#         if i % 2 == 0:
#             R.writelines(f'Juft: {i}\n')
#         else:
#             R.writelines(f'Toq: {i}\n')

# with open('SOME.html', 'w+') as htmlFile:
#     for i in range(100):
#         el = f'<tr>It is <i><u>{i}</u></i> number</tr>'
#         htmlFile.write(
#             f"""
#                 <html>
#                 <head>
#                     <title>Document</title>
#                 </head>
#                 <body>
#                     <table>
#                         {el}
#                     </table>
#                 </body>
#             """
#         )

# with open(
#     'MyFIle.txt',
#     'w+'
# ) as users:
#     for i in range(300):
#         users.writelines(
#             faker.name() + '\n'
#         )
# with open(
#     'MyFIle.txt', 'r+'
# ) as readAbleFile:
#     print(readAbleFile.read().count('John'))


with open(
    'staffs.txt',
    'w+'
) as File:
    users = []
    for i in range(10):
        user = {}
        user['name'] = faker.name()
        user['age'] = random.randint(10, 110)
        user['salary'] = str(random.randint(10, 1000)) + ' $'
        File.writelines(
            str(user) + '\n'
        )
