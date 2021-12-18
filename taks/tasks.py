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
def rimToNumber(x):
    rim = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    for i in range(len(x)):
        current = rim[x[i]]
        nexT = rim[x[i + 1]]
        if current < nexT:
            result += nexT - current
            continue
        else:
            result += current
    return result


print(rimToNumber('XIV'))
