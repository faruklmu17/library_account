#this is a small library collection 

available_books = [

"The Fault in Our Stars", "The Hunger Games", "To All the Boys I've Loved Before",

"Harry Potter and the Sorcerer's Stone", "The Perks of Being a Wallflower",

"Looking for Alaska", "The Hate U Give", "The Maze Runner",

"Divergent", "Eleanor & Park"

]


class LibraryAccount:


    def __init__(self,user_name,available_books,borrowed_books):
        self.user_name = user_name
        self.available_books = available_books
