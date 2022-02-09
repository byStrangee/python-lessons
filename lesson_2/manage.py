# my_range = range(0, 10, 2)
# for i in my_range:
#       print(i)

##################

# while True:
#       me = input('40*20+50=')
#       if me == '850':
#             break

###################

# while True:
#       fruit = input('fruit name\n')
#       if fruit == 'stop':
#             break

##################

# sums = 0
# while True:
#       num = input('>>> ')
#       if num == '/stop':
#             break
#       sums += int(num)
# print(sums)

##################

# for i in range(10):
#       if i % 2 == 0:print(i)

# print(max(123,132,132,1))
# print(max([1,32,456,78941,654]))
# print(sum([46,5465,4165465,4165]))

# import os
# print(os.path)


import random
# print(random.random() * 5) 

# print(random.randint(10,50))

# print(random.randrange(5,15))

# arr = [456,465,46464,646,46]

# random.shuffle(arr)

# print(arr)
# ar = [1,2,3,45,6,4,798]
# st = 'Hello world'
# print(random.sample(ar, 3))

# print(random.sample(range(300) , 5))

# arr = [1,2,3,45,78]

# print(random.choice(arr))

# sTr = "Hello world"

# print(sTr[0:-5])

# age = 11
# nn = "hello %s" %age

# ag = 44
# nnb = "hello {0}".format(ag)
# ## ## ##
      # a = 99
      # name = f"Strange, age = {a}"
      # print(name)
###########
      # Strings methods
###########
      #1
text = "new jersey 45 a new house"

# print(text.strip('4'))
# ######################
# print(text.lstrip('n'))
# #######################
# print(text.rstrip('n'))
# #######################
# print(text.split(' '))
# #######################
# print(text.rsplit(' '))
# #######################
# print(" ".join(['hello', 'world']))
# #######################
# print(text.upper())
# #######################
# print(text.lower())
# #######################
# print(text.capitalize())
# #######################
# print(text.title())
# #######################
# print(text.find('new'))
# #######################
# print(text.index('j'))
# #######################
# print(text.count('s'))
# #######################
# print(text.startswith('n'))
# #######################
# print(text.endswith('e'))
# #######################
# print(text.replace(' ', ''))
# boolean returner methods
###########
# print("salom44".isalnum()) # space also symbol , numbers and letters
# #######################
# print("sad".isalpha()) # only letters 
# #######################
# print("14".isdigit()) # only symbols
# #######################
# print("".isnumeric()) # only numbers and also rim numbers
# #######################
# print(text.isupper()) 
# #######################
# print(text.islower())
# #######################
# print("Salom Asdasd".istitle())
#######################
# print(text.isprintable())
# def main(num, length):
#       letters = "qwertyuiopasdfghjklzxcvbnm"
#       upperLetters = letters.upper()
#       symbols = '!@#$%^&*(}){"|?><+=~`'
#       numbers = '123456789'
#       password = letters + upperLetters + symbols + numbers
#       generatedPassword = ''
#       for a in range(num):
#             for y in range(length):
#                   r = random.choice(password)
#                   generatedPassword += r
#             print(generatedPassword)
# print(main(4,15))