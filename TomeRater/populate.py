from TomeRater import *
print() #give me some space
print() #give me some space

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139) #will print a message
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.get_most_read_book())


#A few of my own tests!---------------------------------------------------------
print() #give me some space

tester = TomeRater()

#Add Harry Potter of course
hp = Tome_Rater.create_novel("Harry Potter", "JK Rowling", 108470294)

#Add myself as a user with a book I've read
Tome_Rater.add_user("Alli Love", "allisbuddies@yahoo.com", user_books=[hp])

#Other users remember they've read Harry Potter too.
Tome_Rater.add_book_to_user(hp, "david@computation.org", 3)
Tome_Rater.add_book_to_user(hp, "alan@turing.com", 4)
#Harry Potter is the best, so let's cheat and give it some extra ratings...
hp.add_rating(4)
hp.add_rating(4)

print(Tome_Rater)
if Tome_Rater == Tome_Rater:
    print("Two of the same")
else:
    print("Not the same")
print(tester)
if Tome_Rater == tester:
    print("Two of the same")
else:
    print("Not the same")

#Print the same tests as before
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.get_most_read_book())



print() #give me some space
print() #give me some space
