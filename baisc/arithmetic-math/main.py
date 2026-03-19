import math

friends = 0
# friends = friends + 1
friends += 1

# friends = friends - 2
friends -= 2

# friends = friends * 3
friends *= 3

# friends = friends / 2
friends /= 2

# friends = friends ** 2
friends **= 2

friends = 10
remainder = friends % 3

print(remainder)

x = 3.14
y = -4
z = 5
result = round(x)
result = abs(y)
result = pow(y,3)
result = max(x,y,z)
result = min(x,y,z)
print(result)

x = 9
print(math.pi)
print(math.e)
result = math.sqrt(x)
print(result)
x = 9.1
result = math.ceil(x)
print(result)
x = 9.9
result = math.floor(x)
print(result)

# Exercise calculate circumference of circle
pie = math.pi
radius = float(input("Enter the circle radius: "))
c = 2 * pie * radius
print(f'Circumference of your circle is: {round(c,2)}cm')

# Exercise calculate area of circle
pie = math.pi
radius = float(input("Enter the circle radius: "))
area = pie * pow(radius,2)
print(f"Area of circle is: {round(area,2)} cm^2")

# Exercise hypotenuse of a right triangle
a = float(input("Enter side a value: "))
b = float(input("Enter side b value: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The hypotenuse of a right triangle is: {round(c, 2)}")
