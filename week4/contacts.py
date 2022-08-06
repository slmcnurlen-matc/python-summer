#!/usr/bin/env python3

contacts = dict()

person1 = dict()
person1["fname"] = "Jack"
person1["lname"] = "Harkness"
person1["phone"] = "555-5555"
person1["age"] = 200

person2 = dict()
person2["fname"] = "Martha"
person2["lname"] = "Jones"
person2["phone"] = "555-6666"
person2["age"] = 80

person3 = dict()
person3["fname"] = "Sally"
person3["lname"] = "Sparrow"
person3["phone"] = "555-7777"
person3["age"] = 30

person4 = dict()
person4["fname"] = "Gwen"
person4["lname"] = "Cooper"
person4["phone"] = "555-8888"
person4["age"] = 42

contacts["Harkness"] = person1
contacts["Jones"] = person2
contacts["Sparrow"] = person3
contacts["cooper"] = person4

while True:
    search = input("Who are you looking for?: ")
    if search == "DONE":
        print("We are done!")
        break
    for contact in contacts:
        if contact == search:
            print("==============================================")
            print(f"Found your contact {search}")
            print(f" First Name   : {contacts[contact]['fname']}")
            print(f" Last Name    : {contacts[contact]['lname']}")
            print(f" Phone Number : {contacts[contact]['phone']}")
            print(f" Age          : {contacts[contact]['age']}")