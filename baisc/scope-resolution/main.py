# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# def func1():
#     a = 1 #local scope
#     print(a)
#
# def func2():
#     b = 2 #local scope
#     print(b)
#
# func1()
# func2()

# Enclosed scope
# def func1():
#     x = 1
#
#     def func2():
#         print(x)
#
#     func2()
#
# func1()

# def func1():
#     print(x)
#
# def func2():
#     print(x)
#
# x = 3 # Global scope
# func1()
# func2()

from math import e #Built in variable scope
def func1():
    print(e)

e = 3

func1()
