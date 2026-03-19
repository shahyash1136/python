# List comprehension = A concise way to create lists in python compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# doubles = []
# for x in range(1,11):
#     doubles.append(x * 2)
#
# print(doubles)

# doubles = [x * 2 for x in range(1, 11)]
#
# print(doubles)

# triples = [y * 3 for y in range(1,11)]
# print(triples)

# squares = [z * z for z in range(1, 11)]
# print(squares)

# fruits = ['apple', 'orange', 'banana', 'coconut']
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# numbers = [1, -2, 3, -4, 5, -6, 8, -7]
# positive_num = [num for num in numbers if num >= 0]
# negative_num = [num for num in numbers if num < 0]
# even_num = [num for num in numbers if num % 2 == 0]
# odd_num = [num for num in numbers if num % 2 == 1]
# print(positive_num)
# print(negative_num)
# print(even_num)
# print(odd_num)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grade = [grade for grade in grades if grade >= 60]
print(passing_grade)