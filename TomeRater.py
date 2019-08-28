#Create TomeRater

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        for email in self.users:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {}!".format(email))

    def add_user(self, name, email, user_books = None):
        if email in self.users.keys():
            print("This user already exists")
            return None
        if '@' in email and ('.com' in email or '.edu' in email or '.org' in email):
            new_user = User(name, email)
            self.users[email] = new_user
            if user_books is not None:
                for book in user_books:
                    self.add_book_to_user(book, email)
                return None
            else:
                print("Invalid email address!")
            return None
            

    def print_catalog(self):
        for book in self.books:
            print(book)
            
    def print_users(self):
        for user in self.users:
            print(user)

    def most_read_book(self):
        most_read_count = 0
        most_read_book = None
        for book, book_read_count in self.books.items():
            if book_read_count > most_read_count:
                most_read_count = book_read_count
                most_read_book = book
        return most_read_book

    def highest_rated_book(self):
        highest_average_rate = 0
        highest_rated_book = None
        for book in self.books.keys():
            if book.get_average_rating() > highest_average_rate:
                highest_average_rate = book.get_average_rating()
                highest_rated_book = book
        return highest_rated_book
    
    
    def most_positive_user(self):
        most_positive_user = ""
        highest_average_rating = 0
        for user in self.users.values():
            average_rating = user.get_average_rating()
            if average_rating > highest_average_rating:
                highest_average_rating = average_rating
                most_positive_user = user.name
        return most_positive_user
       

# Create a User        

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email
    
    def change_email(self, address):
        self.address = address
        print("User {} email has been updated!".format(self.name))

    def read_book(self, book, rating = None):
        self.rating = rating
        self.books[book] = rating

    def get_average_rating(self):
        user_ratings = [self.books[book] for book in self.books if self.books[book] is not None]
        if user_ratings:
            average_user_rating = sum(user_ratings) / len(user_ratings)
            return average_user_rating
            
    def __repr__(self):
        print ("User {} , email: {}, books read: {}". format(self.name, self.email, len(self.books)))
       

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

#Create a Book

class Book(object):

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        if type(title) is str:
            return self.title
        else:
            print("Title is not a string")

    def get_isbn(self):
        if type(isbn) is int:
            return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print ("This book's {} ISBN has been updated".format(self.isbn))

    def add_rating(self, rating):
        self.rating = rating
        if rating is None:
            print("No rating for the book {}".format(self.title))
        elif self.rating >= 0 and self.rating <= 4:
            return self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        book_ratings = [rating for rating in self.ratings if rating is not None]
        if book_ratings:
            average_book_rating = sum(book_ratings) / len(book_ratings)
            return average_book_rating    
    
    def __eq__(self, other_book):
        if self.title ==other_book.title  and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))
        

# Fiction books

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)



# Non-fiction books

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)