"""
- `__init__(self, user_id, name)`
- Method: `add_rating(item_id, score)` — store in a dict
- Method: `get_ratings()` — return all ratings
- Create 3 User objects, add ratings, print them
- Add private attribute `_ratings` to User class
- Add `@property` for `average_rating`
- Test: user with 5 ratings — does average compute correctly?
"""

from statistics import mean


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self._ratings = {}  # Single underscore (standard convention)

    def add_rating(self, item_id, score):
        """Add a rating for an item"""
        self._ratings[item_id] = score

    def get_ratings(self):
        """Return all ratings"""
        return self._ratings

    @property
    def average_rating(self):
        """Calculate average rating (returns 0 if no ratings)"""
        if not self._ratings:
            return 0.0
        return mean(self._ratings.values())

    def __str__(self):
        """String representation"""
        return f"{self.name} (ID: {self.user_id}) - Avg: {self.average_rating:.2f}"


# Testing
user1 = User("1", "Yash Shah")
user1.add_rating("101", 5.5)
user1.add_rating("102", 4.0)
user1.add_rating("103", 8.2)
user1.add_rating("104", 6.3)
user1.add_rating("105", 3.0)

user2 = User("2", "John Doe")
user2.add_rating("201", 4.5)

user3 = User("3", "Glenn Maxwell")
# No ratings - test empty case

# Display results
print(user1)
print(f"Ratings: {user1.get_ratings()}\n")

print(user2)
print(f"Ratings: {user2.get_ratings()}\n")

print(user3)
print(f"Ratings: {user3.get_ratings()}\n")

# Edge case test
print(f"User with no ratings - Average: {user3.average_rating}")
