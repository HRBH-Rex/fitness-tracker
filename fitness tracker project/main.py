import json
import sys

def main():
    #login################################################################
    def login():
        while True:
            User = input("please enter User ID, or Quit?:")
            if User in accounts:#checks if ID is valid
                print("User ID valid")
                break
            elif User.casefold() == "quit":
                return#exits function without
            else:
                print("this is not a valid ID")
        while True:
            password = input("enter Password, or Quit?:") 
            if password == accounts[User]["Password"]:#checks if password matches accounts password
                print("password valid, welcome")
                break
            elif password.casefold() == "quit":#exits function, back to main
                return
            else:
                print("this password is not correct")
        return User#successful login, returns ID number
    ######################################################################
    #make account#########################################################
    def make_account():
        nonlocal accounts#allows function to access stored accounts.json file
        while True:
            new_N = input("please enter your desired Name:")#inputs new accounts username
            if new_N.casefold() == "quit" or new_N.casefold() == "admin":#some usernames are restricted to avoid conflicts/confusion
                print("this is a restricted username")
            else:
                break
        while True:
            while True:
                new_PW = input("create password:")#input new accounts password
                if new_PW.casefold() == "quit":#this is restricted to avoids conflicts
                    print("this is an invalid password")
                else:
                    break
            new_PW2 = input("confirm password:")#new accounts password confirmation
            if new_PW2.casefold() == new_PW.casefold():
                print("password confirmed")
                break
            else:
                print("passwords do not match")
                pass
        new_ID = len(accounts)+1#makes new accounts ID
        str(new_ID)#sets ID to string
        accounts[new_ID] = {"Name":new_N, "Password":new_PW, "Height":"Blank", "Weight":"Blank", "BMI":"Blank", "Status":"Blank"}#constructs new account
        with open("accounts.json", "w") as file:#saves new account to json file
            json.dump(accounts, file, indent=4)
        print(f"account created, your User ID is {new_ID}")

    ######################################################################
    #change_login_details######################################################
    def change_login_details():
        nonlocal accounts, User#allows function to access stored accounts.json file and user ID
        while True:
            choice = input("do you want to change your Name, Password or to go back?:")
            if choice.casefold() == "name":
                new_UN = input("please enter your new Name:")#input new Name
                if new_UN.casefold() == "quit" or new_UN.casefold() == "admin":#some usernames are restricted to avoid conflicts/confusion
                    print("this is a restricted Name")
                else:
                    accounts[User]["Name"] = new_UN#updates name
                    with open("accounts.json", "w") as file:#saves account changes to json file
                        json.dump(accounts, file, indent=4)
            elif choice.casefold() == "password":
                while True:
                    while True:
                        new_PW = input("create password:")#input new password
                        if new_PW.casefold() == "quit":#this is restricted to avoids conflicts
                            print("this is an invalid password")
                        else:
                            break
                    new_PW2 = input("confirm password:")#new password confirmation
                    if new_PW2.casefold() == new_PW.casefold():
                        print("password confirmed")
                        accounts[User]["Password"] = new_PW#updates password
                        with open("accounts.json", "w") as file:#saves account changes to json file
                            json.dump(accounts, file, indent=4)
                        break
                    else:
                        print("passwords do not match")
                        pass
            elif choice.casefold() == "back":#exits function, back to next choice
                break
            else:
                print("this is an invalid input")
    ######################################################################
    #calc_bmi#############################################################
    def calc_BMI():
        nonlocal accounts, User#allows function to access stored accounts.json file and user ID
        MIN_HEIGHT = 0.5#sets min_height constant
        while True:#enter height loop
            Height = input("please enter your Height in CM: ")#input height
            try:
                Height = float(Height)#sets height to float
                if Height > MIN_HEIGHT:#checks if height is above minimum
                    break
                else:
                    print("invalid Height, please enter above a minimum of 0.5")
                    pass
            except(ValueError):
                print("invalid input, plese enter a number")  

        while True:#enter weight loop
            Weight = input("please enter your Weight in kg: ")#input weight
            try:
                Weight = float(Weight)#sets weight to float
                break
            except(ValueError):
                print("invalid input, plese enter a number")  
        bmi = Weight*(Height**2)#calculates bmi
        if bmi < 18.5:
            Status = "Underweight"#decides bmi status
        elif bmi < 24.9:
            Status = "Healthy"#/\
        elif bmi < 29.9:
            Status = "Overweight"#/\
        else:
            Status = "Obese"#/\
        accounts[User]["Height"] = Height#updates uses account info
        accounts[User]["Weight"] = Weight#/\
        accounts[User]["BMI"] = bmi#/\
        accounts[User]["Status"] = Status#/\
        with open("accounts.json", "w") as file:#saves account changes to json file
            json.dump(accounts, file, indent=4)
        print(f"your BMI is {bmi}")#outputs bmi and status
        print(f"you are {Status}")#/\
    ######################################################################
    #view_my_info#########################################################
    def view_my_info():
        nonlocal accounts, User#allows function to access stored accounts.json file and user ID
        for key, value in accounts.items():#loops through all accounts while storing the key and value(implement search algorithm?)
            if key == User:#when it gets to the current users account
                print(f"ID:{key}")
                print(f"Name:{value["Name"]}")
                print(f"Height:{value["Height"]}")
                print(f"Weight:{value["Weight"]}")
                print(f"BMI:{value["BMI"]}")
                print(f"Status:{value["Status"]}") 
            else:#for non current user accounts
                pass

    ######################################################################
    #admin commands
    #view_all_members#################################################
    def view_all_members():
        nonlocal accounts#allows function to access stored accounts.json file
        for key, value in accounts:#loops through all accounts and stores the key and value
            if key == "1":#if user is admin
                pass
            else:#prints out all non admin accounts details
                print("#############")
                print(f"ID:{key}")
                print(f"Name:{value["Name"]}")
                print(f"Height:{value["Height"]}")
                print(f"Weight:{value["Weight"]}")
                print(f"BMI:{value["BMI"]}")
                print(f"Status:{value["Status"]}")

    ##################################################################
    #reset############################################################
    def reset():#resets accounts.json to whats in default_accounts.json
        with open("default_accounts.json", "r") as file:
            default_accounts = json.load(file)
        with open("accounts.json", "w") as file:
            json.dump(default_accounts, file, indent=4)

    ##################################################################
    #next choice##########################################################
    def next_choice():
        nonlocal accounts, User, log_out#allows function to access stored accounts.json file, user ID and logout condition
        while True:
            print(f"{accounts[User]["Name"]}")#prints out current users name
            with open("accounts.json", "r") as file:#updates stored accounts file to account for password/username changes post initial iteration
                accounts = json.load(file)
            command = input("what do you want to do next?(calc_BMI, view_my_info, change_login_details, log_out):")
            if command.casefold() == "calc_bmi":
                calc_BMI()
            elif command.casefold() == "view_my_info":
                view_my_info()
            elif command.casefold() == "change_login_details":
                change_login_details()
            elif command.casefold() == "log_out":
                log_out = True#puts logout condition to true and exits function
                break
            elif command.casefold() == "view_all_members" and User == "1":#only usable if user is admin
                view_all_members()
            elif command.casefold() == "reset" and User == "1":#only usable if user is admin
                reset()
            else:
                print("this is an invalid command")

    ######################################################################
    #main#################################################################
    with open("accounts.json", "r") as file:#initial store of accounts json file
        accounts = json.load(file)
    while True:
        choice = input("login, create_account or quit?:")
        if choice.casefold() == "login":
            User = login()
            log_out = False#creates logout condition and sets to false
            while log_out == False:
                next_choice()
        elif choice.casefold() == "create_account":
            make_account()
        elif choice.casefold() == "quit":
            break
        else:
            print("this is an invalid input")
    ######################################################################
main()
