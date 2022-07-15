#!/usr/bin/env python3
print("Name: Sam McNurlen")
"""
Sam McNurlen
This script will loop through a sequence emulating elements of a scenes in the move Jurassic Park.
"""

password_database = {"Username" : "dnedry",
                     "Password" : "please"
                    }

command_database = {"reboot"   : "OK. I will reboot all park systems.",
                    "shutdown" : "OK. I will shut down all park systems.",
                    "done"     : "I hate all this hacker stuff."
                    }

white_rabbit_object = 0
counter = 0
while white_rabbit_object == 0:
    while counter < 3:
        input_user = input("Username: ")
        input_password = input("Password: ")
        if input_user == password_database['Username'] and input_password == password_database['Password']:
            white_rabbit_object = 1
            counter = 3
            print("Hi, Dennis. You're still the best hacker in Jurassic Park.")
            print(f"Commands: {command_database.keys()}")
            command = input("Enter a command: ")
            if command == "reboot":
                print(f"{command_database['reboot']}")
            elif command == "shutdown":
                print(f"{command_database['shutdown']}")
            elif command == "done":
                print(f"{command_database['done']}")
            else:
                print("The Lysine Contingency has been put into effect.")
        else:
            counter += 1
            if counter == 3:
                print("You didn't say the magic word.\n"*25)
            else:
                print(f"You didn't say the magic word. {counter}")