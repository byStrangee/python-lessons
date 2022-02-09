
#
# def numsOf(s):
#     s = str(s)
#     nums = ""
#     for i in s:
#         if i.isdigit():
#             nums += i
#     return nums


# def main():
#     a = list(range(1, 6))
#     for _ in map(lambda n: n + n ** n, a):
#         print(_)
#     def foo(x, y):
#         for i in range(1, x + y):
#             yield (x ** y) + (x - y)
#     #
#     # for i in foo(30, 20):
#     #     print(i)
#
# print(__name__)
# if __name__ == '__main__':
#     main()


# x = lambda s: "".join(list(set(s)))

# numsOf = lambda s: "".join([i for i in s if i.isdigit()])

def how(x, y):
    count = 0
    for i in range(x + 1, y):
        if y % i == 0:
            count += 1
    return count


print(
    how(2, 20)
)
# print(numsOf("abs1000asd"))