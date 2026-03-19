# groceries = {
#     ("apple", "orange", "banana", "coconut"),
#     ("celery", "carrots", "potatoes"),
#     ("chicken", "fish", "turkey")
# }
#
# for collection in groceries:
#     for value in collection:
#         print(value, end=" ")
#     print()

num_pad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#")
)
for row in num_pad:
    for value in row:
        print(value, end=" ")
    print()
