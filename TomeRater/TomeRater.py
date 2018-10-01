class User(object):
    def __init__(self, name, email): #(..., string, string)
        self.name = name
        self.email = email
        self.books = {} #{book:rating}

    def get_email(self):
        return self.email

    def change_email(self, address): #(..., string{should be an email address})
        self.email = address
        print(self.name + "'s email has been updated!")

    def __repr__(self):
        sentence = self.name + " with email " + self.email + " and " + str(len(self.books)) + " books read."
        return sentence

    def __eq__(self, other_user): #(..., UserClassObject{has: .name, .email, .books})
        if (self.name == other_user.name) and (self.email == other_user.email): # comparing two sets of strings
            return True
        else:
            return False

    def read_book(self, book, rating=None): #(..., BookClassObjecr{has .title, .isbn, .ratings})
        self.books[book] = rating #add a book to the self.books dictionary

    def get_average_rating(self):
        count = 0
        total = 0
        for i in self.books:
            temp = self.books[i]
            if temp == None:
                pass
            else:
                count += 1
                total += temp
        if count == 0:
            count = 1
        return total/count


#parent class for books
class Book(object):
    def __init__(self, title, isbn): #(..., string, int)
        self.title = title
        self.isbn = isbn
        self.ratings = [] #(empty string to hold a rating for each reader)

    def __hash__(self): #make it hashable
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_num): #(..., int)
        self.isbn = new_num
        print(self.title + "'s ISBN has been updated.")

    def add_rating(self, rating): #(..., int{0-4 only})
        if rating == None:
            pass
        elif rating >= 0 and rating <= 4: #just make sure...
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if (self.title == other_book.title) and (self.isbn == other_book.isbn):
            return True
        else:
            return False

    def __repr__(self):
        return self.title

    def get_average_rating(self):
        count = 0
        total = 0
        for i in self.ratings:
            if i == None:
                pass
            else:
                count += 1
                total += i
        if count == 0:
            count = 1
        return total/count


#fiction and nonfiction child classes of book
class Fiction(Book):
    def __init__(self, title, author, isbn): #(..., string, int, string)
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + " by " + self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn): #(..., string, int, string, string)
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return self.title + ", a " + self.level + " manual on " + self.subject



#Start TomeRater ---------------------------------------------------------------
class TomeRater():
    def __init__(self):
        #A TomeRater object has two dictionaries
        self.users = {} #{email:user}
        self.books = {} #{book:times it's been read}

    def __repr__(self):
        return str(len(self.users)) + " readers who have read a total of " + str(len(self.books)) + " books."

    def __eq__(self, other):
        maybe = True
        for i in self.users:
            if i in other.users:
                pass
            else:
                maybe = False
        for i in self.books:
            if i in other.books:
                pass
            else:
                maybe = False
        return maybe

    def create_book(self, title, isbn):
        #Call to init in BookClass
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, isbn, author):
        #Call to init in FictionClass
        new_novel = Fiction(title, isbn, author)
        return new_novel

    def create_non_fiction(self, title, isbn, subject, level):
        #Call to init in NonFictionClass
        new_manual = Non_Fiction(title, isbn, subject, level)
        return new_manual

    def add_book_to_user(self, book, email, rating=None): #(.users{email:user} .books{book:# been read}, .title .isbn .ratings, string, int)
        if email in self.users:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email " + email)

    def add_user(self, name, email, user_books=None): #(.users{email:user} .books{book:# been read}, string, [.title, .isbn, .ratings[]])
        new = User(name, email)
        self.users[email] = new
        if user_books == None:
            pass
        else:
            for each in user_books:
                self.add_book_to_user(each, email)

#Analysis Methods
    def print_catalog(self): #(.users{email:user} .books{book:# been read})
        for i in self.books:
            print(i)

    def print_users(self): #(.users{email:user} .books{book:# been read})
        for i in self.users:
            print(self.users[i])

    def get_most_read_book(self): #(.users{email:user} .books{book:# been read})
        x = 0 #to compare each # of reads with the previous book
        y = [] #to hold the book (or books) that have been read the most
        for i in self.books:
            if self.books[i] > x:
                y = []
                y.append(i)
                x = self.books[i]
            elif self.books[i] == x:
                y.append(i)
            else:
                continue
        return y[0] #if multiple books are tied for first, we return just the first
        #we can return y if we want a list of all the most read books (maybe rare anyway)

    def highest_rated_book(self):
        x = 0 #hold the top rating
        y = [] #hold top rated book
        for i in self.books:
            temp = i.get_average_rating()
            if temp > x:
                x = temp
                y = []
                y.append(i)
            elif temp == x:
                y.append(i)
            else:
                continue
        return y[0] #if multiple books are tied for first, we return just the first
        #we can return y if we want a list of all the most positive users (maybe rare anyway)

    def most_positive_user(self):
        x = 0 #hold the most positive average
        y = [] #hold most positive user
        for i in self.users:
            temp = self.users[i].get_average_rating()
            if temp == None:
                pass
            elif temp > x:
                x = temp
                y = []
                y.append(self.users[i])
            elif temp == x:
                y.append(self.users[i])
            else:
                continue
        return y[0] #if multiple users are tied for first, we return just the first
        #we can return y if we want a list of all the most positive users (maybe rare anyway)
