# call the function with your file please don't forget to write file's full name
def get_staff(file):
      with open(file, 'r+') as file:
            staf = []
            for i in file.readlines():
                  user  = {}
                  info = i
                  info = info.replace('\n' , '')
                  info = info.split('-')
                  user['name'] = info[0]
                  user['age'] = info[1]
                  user['salary'] = info[2]
                  staf.append(user)
      return staf


print(
      get_staff('text.txt')
)
print(
      round(15)
)


even_squares = [x * x for x in range(25) if x % 2 == 0]

print(even_squares)
