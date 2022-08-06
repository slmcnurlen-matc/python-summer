#!/usr/bin/env

BOOK1 = dict()
BOOK1 = {}
BOOK2 = dict()
BOOK3 = dict()
BOOKSHELF = dict()

BOOK1['PAGE1'] = 'This is page 1'
BOOK1['PAGE1'] = 'This is page 2'
BOOK1['PAGE1'] = 'This is page 3'
BOOK1['PAGE1'] = 'This is page 4'

BOOK2['PAGE1'] = 'This is page 1'
BOOK2['PAGE2'] = 'This is page 2'
BOOK2['PAGE3'] = 'This is page 3'
BOOK2['PAGE4'] = 'This is page 4'

BOOK3['PAGE1'] = 'This is page 1'
BOOK3['PAGE2'] = 'This is page 2'
BOOK3['PAGE3'] = 'This is page 3'
BOOK3['PAGE4'] = 'This is page 4'

BOOKSHELF = {'FAREWELL TO ARMS' : BOOK1, 'ANOTHER BOOK' : BOOK2, 'STAR WARS' : BOOK3}

booksearch = input("What book are you looking for? ")
found = 0
for book in BOOKSHELF.keys():
    if book == booksearch:
        temp1 = BOOKSHELF[book]
        print("Book Name: " + book + " Page Number: " + temp1['PAGE2'])
        found = 1
if found != 1:
    print("No book found")