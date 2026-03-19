# collection = single "variable" used to story multiple values
#       List = [] ordered and changeable. Duplicates OK
#       Set  = {} unordered and immutable, but Add/Remove OK. No duplicates
#      Tuple = () ordered and unchangeable. Duplicates OK. Faster

# fruits = ["apple", "orange", "banana", "coconut"]
#
# # print(fruits[::-1])
#
# # for fruit in fruits:
# #     print(fruit)
# #
# # print(dir(fruits))
#
# # print(len(fruits))
# # print("pineapple" in fruits)
# fruits[0] = "pineapple"
#
# fruits.append("apple")
#
# fruits.remove("apple")
#
# fruits.insert(0,"apple")
#
# fruits.sort()
#
# fruits.reverse()
# #fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("banana"))
#
# print(fruits)
#
# # for fruit in fruits:
# #     print(fruits)

# fruits = {"apple", "orange", "banana", "coconut"}
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
#
# print(fruits)

fruits = ("apple", "orange", "banana", "coconut")
print(fruits.index('apple'))
print(fruits.count("coconut"))
print(fruits)