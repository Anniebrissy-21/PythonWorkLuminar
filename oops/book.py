class Book:
    book_id:int
    book_title:str
    book_author:str
    year_of_publication:int

    def __init__(self,id,title,author,year):
        self.book_id=id
        self.book_title=title
        self.book_author=author
        self.year_of_publication=year

    def __str__(self):
        return self.book_title

    def display_book(self):
        print(self.book_id,self.book_title,self.book_author,self.year_of_publication)

obj1=Book(101,"The Adventures","jjdau",2020)

obj1.display_book()
print(obj1)