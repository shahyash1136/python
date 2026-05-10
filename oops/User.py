"""
- **Code (1 hr):** Write a `User` class
    - `__init__(self, user_id, name)`
    - Method: `add_rating(item_id, score)` — store in a dict
    - Method: `get_ratings()` — return all ratings
    - Create 3 User objects, add ratings, print them
"""


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.ratings = {}

    def add_rating(self, item_id, score):
        self.ratings[item_id] = score  # item_id as key

    def get_ratings(self):
        return self.ratings


# Testing
user1 = User("1", "Yash Shah")
user1.add_rating("101", 5.5)
user1.add_rating("102", 4.0) 

user2 = User("2", "John Doe")
user2.add_rating("201", 4.5)

user3 = User("3", "Glenn Maxwell")
user3.add_rating("301", 8.5)

print(f"{user1.name}: {user1.get_ratings()}")
print(f"{user2.name}: {user2.get_ratings()}")
print(f"{user3.name}: {user3.get_ratings()}")

