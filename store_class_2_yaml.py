import yaml
from dataclasses import dataclass, asdict

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

# Create an instance of Book
my_book = Book("1984", "George Orwell", 328, 9.99)

# Convert the data class instance to a dictionary
book_dict = asdict(my_book)

# Write the dictionary to a YAML file
with open('book.yaml', 'w') as file:
    yaml.dump(book_dict, file)