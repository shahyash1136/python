# function = A bock of reusable code place() after the function name to invoke it

# def happy_bithday(name,age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} year's old!")
#     print("Happy birthday to you!")
#     print()
#
#
# happy_bithday("Bro", 20)
# happy_bithday("Steve", 30)
# happy_bithday("Joe", 40)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")
#
# display_invoice("BroCode",42.50,"01/01")

# return = statement used to end a function and send a result back to the caller
# def add(x, y):
#     z = x + y
#     return z
#
# def sub(x, y):
#     z = x - y
#     return z
#
# def muliiply(x, y):
#     z = x * y
#     return z
#
# def divide(x, y):
#     z = x / y
#     return z
#
# print(add(1, 2))
# print(sub(1, 2))
# print(muliiply(1, 2))
# print(divide(1, 2))

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return  first + " " + last

full_name = create_name("yash","shah")
print(full_name)