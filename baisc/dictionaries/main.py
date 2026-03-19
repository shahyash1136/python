# dictionary = a collection {key:value} pairs ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(capitals.get("Japan"))
if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capita doesn't exists")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})

print(capitals)

capitals.pop("China")

print(capitals)

capitals.popitem()

print(capitals)

# capitals.clear()
#
# print(capitals)

# keys = capitals.keys()
#
# for key in capitals.keys():
#     print(key)

# for value in capitals.values():
#     print(value)

for key,value in capitals.items():
    print(f"{key}:{value}")