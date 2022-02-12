import math
# def mostCharOf(s):
#     o = {}
#     for i in s:
#         o[i] = o[i] + 1 if bool(o.get(i)) else 1
#     count = 0
#     max_char = ""
#     for i in o.keys():
#         if o[i] > count:
#             count = o[i]
#             max_char = i
#     return {
#         "most_used_char": max_char,
#         "count": count
#     }

def main():
    task1 = lambda x: x ** 3
    task2 = lambda x: ", ".join([x ** i for i in range(2, 5)])
    task3 = lambda x, y: (x + y) / 2
    task4 = lambda x, y, z: f"P = { x + y + z }"
    task5 = lambda x, y: f"P = ${ (x * 2) + (y * 2) }\nS = { x * y }"
    task7 = lambda x: f"{x}"[::-1]
    task8 = lambda x, y: int(f"{x}{y}")
    task9 = lambda x, y: int(f"{y}{x}")
    task10 = None
    def task11(x, y):
        return x if x > y else y
    def task12(*args):
        s = list(args)
        s.sort()
        return  s
    def task13(*args):
        s = list(args)
        s.sort(reverse=True)
        return  s
    def task14(a,b,c):
        s = [a, b, c]
        s.insert(0,s[len(s) - 1])
        s.pop()
        return s
    def task15(a, b, c):
        s = [a, b, c]
        s.append(s[0])
        s.pop(0)
        return s
    def task16(n):
        if n > 0:
            return '1'
        else:
            return '-1' if n != 0 else 0
    def task17(a,b,c):
        d = b ** 2 - 4 * a * c
        if d > 0:
            return  2
        elif d == 0:
            return  1
        else:
            return 'yechimga ega emas'
    task18 = lambda rad: 3.14 * (rad ** 2)

    def task19(r1, r2):
        r1 = r1 ** 2 * 3.14
        r2 = r2 ** 2 * 3.14
        return r1 - r2 if r1 > r2 else r2 - r1

    def task20(a, b):
        c = math.sqrt((a ** 2) + (b ** 2))
        return  a + b + c
    def task21(a, b):
        sum = 0
        if a > b:
            pass
        else:
            for i in range(a, b):
                sum += i
        return sum
    def task22(a, b, op):
        if op == 1:
            return a - b
        elif op == 2:
            return a * b
        elif op == 3:
            return a / b
        else:
            return a + b
    def task23(x, y):
        if x > 0 and y > 0:
            return 'I'
        elif x > 0 and y < 0:
            return 'II'
        elif y < 0 and x < 0:
            return 'III'
        elif x < 0 and y > 0:
            return  'IV'
        else:
            return 0
    task24 = lambda x: True if x % 2 == 0 else False
    task25 = lambda x: True  if math.sqrt(x) % 2 == 0 else False
    def fib(n):
        f0 = 0
        f1 = 1
        for  i in range(2, n + 1):
            f = f0 + f1
            f0 = f1
            f1 = f
        return f
    def task26(k):
        while k > 1:
            k /= 5
        if k == 1.0:
            return  True
        else:
            return  False
    def task27(k, n):
        while k > 1:
            k /= n
        if k == 1.0:
            return  True
        else:
            return  False

    task28 = lambda x: True if x % 2 == 0 else False
    task29 = lambda x: len(str(x))
    task30 = lambda k, n: str(k)[n - 1]
    task31 = lambda st: str(st) == str(st)[::-1]
    def task33(d):
        return d / (180 / math.pi)

    def task34(x):
        s = 1
        for i in range(1,x + 1):
            s *= i
        print(s)


if __name__ == '__main__':
    main()