# Varibbles name
students_count = 1000
rating = 4.99
is_published = False
course_name = 'Python Programming'

# strings
print(students_count)
print(len(course_name))
print(course_name[0])
print(course_name[-1])
print(course_name[0:3])
print(course_name[0:])
print(course_name[:3])
print(course_name[:])

# escape sequences
course = "Python \"Programming"
print(course)

# formated string
first = "Yash"
last = "Shah"
print(f'{first} {last}')

# string methods
course = "  python programming     "
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.lstrip())
print(course.rstrip())
print(course.find('pro'))

# number
x = 1 + 2j
