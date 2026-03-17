#8create a class book with a constructor that initial..title and author.display the book details
class Book():
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print(self.title,self.author)
book=Book("power of your subconcious mind","joseph murphy")
book.display()