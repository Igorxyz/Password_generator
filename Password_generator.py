#!/usr/bin/python3

import sys
import time
import getpass

def generate_string(options_list):
    print()
    while True:
        try:
            password_len = int(input("Choose password length: "))
            print("Concatenatig string from list {} with length {}".format(options_list, password_len))
            password_string = ""
            for number in options_list:
                password_string = password_string + options_content[number]
            print("Password string: {}".format(password_string))
            generate_password(password_string, password_len)
            break
        except ValueError:
            print("Unrecognized value. Please try again...")
            continue
    print("End of password_generate function...")
    sys.exit()

def generate_password(input_str, input_len):
    import random
    print("Generating password from input string:\n{}".format(input_str))
    print( "*" * 80)
    print()
    user_password = []
    for i in range(0, input_len):
        user_password.append(random.choice(input_str))
    print(term_colors.WARN + "Password: {}".format("".join(user_password)) + term_colors.NORM)

class term_colors:
    WARN = '\033[93m'
    NORM = '\033[0m'

program_start = time.time()
user_options = []

try:
    print("CLI PASSWORD GENERATOR")
    print("*" * 80)

    password_options = {
            "1": "Lower-case letters",
            "2": "Upper-case letters",
            "3": "Numbers",
            "4": "Special characters",
            "5": "Generate password",
            "6": "Exit"
            }

    options_content = {
            "1": "abcdefghijklmnopqrstxyz",
            "2": "abcdefghijklmnopqrstxyz".upper(),
            "3": "1234567890",
            "4": "!@#%"
            }

    print(term_colors.WARN + "Available options: " + term_colors.NORM)
    for key in password_options.keys():
        print("{} ---> {}".format(key, password_options[key]))
        time.sleep(0.25)

    while True: 
        user_input = input("Choose an option: ")
        if (user_input in password_options.keys()):
            if (user_input == "6"):
                print("Exiting program...")
                sys.exit()
            elif (user_input == "5"):
                if (user_options):
                    generate_string(user_options)
                else:
                    print("Cannot generate password without any options...")
                    print("Try again")
                    continue
            elif (user_input in ("1", "2", "3", "4")):
                if (user_input in user_options):
                    print(term_colors.WARN + "Input already in options" +term_colors.NORM)
                    continue
                user_options.append(user_input)
                print("User options status: {}".format(user_options))
                continue

        else:
            print(term_colors.WARN + "Please choose a number from list." + term_colors.NORM)
            continue 

except KeyboardInterrupt:
    print()
    print(term_colors.WARN + "Program interrupted by the user: {}".format(getpass.getuser()) + term_colors.NORM)
    sys.exit()
except ValueError:
    print()
    print(term_colors.WARN + "Incorrect input type" + term_colors.NORM)
    sys.exit()

program_end = time.time()
print("Execution time: {}".format(round(float(program_end - program_start), 2)))
