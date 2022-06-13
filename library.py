

# Library


# Books
# Define a class, 'Book' 
# Book should have a book name
# Book should have an author name

# Customer
# Define a class 'Customer' 
# Customer should have a first name, last name, list of books they have rented



class Book:

    def __init__(self, p_bookName, p_authorName):
        self.bookName = p_bookName
        self.authorName = p_authorName

class Customer:

    def __init__(self, p_firstName, p_lastName):
        self.firstName = p_firstName
        self.lastName = p_lastName
        self.listOfBooks = []


customerOne = Customer('John', 'Smith')
customerOne.listOfBooks = [Book('Twilight', 'Jenny Craig'), Book('Wilbur', 'Jason')]


customerTwo = Customer('Nick', 'Meyer')
customerTwo.listOfBooks = [Book('SomeBook', 'SomeAuthor')]