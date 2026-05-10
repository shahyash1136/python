"""
- Write `Item` class: `item_id`, `title`, `genre`
- Write `Movie(Item)` that adds `release_year`
- Override `__str__` to print nicely: `"Inception (2010) - Sci-Fi"`
- Create 5 Movie objects
"""


class Item:
    def __init__(self, item_id, title, genre):
        self.item_id = item_id
        self.title = title
        self.genre = genre

    def __str__(self):
        return f"{self.title} - {self.genre}"


class Movie(Item):

    def __init__(self, item_id, title, genre, release_year):
        super().__init__(item_id, title, genre)
        self.release_year = release_year

    def __str__(self):
        return f"{self.title} ({self.release_year}) - {self.genre}"


movie1 = Movie("101", "Inception", "Sci-Fi", "2010")
movie2 = Movie("102", "Die Hard", "Action", "1988")
movie3 = Movie("103", "Raiders of the Lost Ark", "Adventure", "1981")
movie4 = Movie("104", "Some Like It Hot", "Comedy", "1959")
movie5 = Movie("105", "The Exorcist", "Horror", "1973")
print(movie1)
print(movie2)
print(movie3)
print(movie4)
print(movie5)
