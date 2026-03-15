import json
import os
admin= "rishit"
isrunning = True
print("wlecome to the bank !!")
atm_data = {
    "bank_vault": 500000,
    "total_users": 3,      
    "users": {
        "1001": {         
            "name": "Rahul Sharma",
            "pin": 1234,
            "balance": 5000
        },
        "1002": {         
            "name": "Priya Verma",
            "pin": 9999,
            "balance": 125000
        },
        "1003": {          
            "name": "Rahul Sharma", 
            "pin": 5555,
            "balance": 500
        }
    }
}
if os.path.exists("atm_details.json"):
    with open("atm_details.json", "r") as f:
        data = json.load(f)
else:
    data = atm_data  
    with open("atm_details.json", "w") as f:
        json.dump(data, f, indent=3, sort_keys=True)
def save_data():
    with open("atm_details.json", "w") as f:
        json.dump(data, f, indent=3, sort_keys=True)
def add_user():
    user_id = str(1000 + data["total_users"] + 1)
    data["total_users"]+=1
    print(f"your user id is: {user_id}")
    print("remember it for further uses")
    user_name = input("enter your name")
    balance = int(input("enter your inital balance"))
    pin = int(input("enter your 4 digit pin"))
    data["users"][user_id] = {
    "balance": balance,
    "name": user_name,
    "pin": pin
    }
    data["bank_vault"] += balance
    save_data()
    print("you have been succesfully registered with the bank !!!")
def withdraw(user_id):
    user_pin = data["users"][user_id]["pin"]
    pin = int(input("enter your pin: "))
    if pin == user_pin:
        bank_balance = data["bank_vault"]
        user_balance = data["users"][user_id]["balance"]
        print(f"your current balance is: {user_balance}")
        takeout = int(input("enter the amount you want to withdraw"))
        if takeout > 0 :
            if takeout > user_balance:
                print("insufficient funds")
            else:
                if takeout> bank_balance:
                    print("bank does not have sufficent funds...")
                    print("try again later ")
                else:
                    data["users"][user_id]["balance"]-= takeout
                    data["bank_vault"] -= takeout
        else:
            print("enter a number greater than ZERO !!!")
    else:
        print("wrong pin...")
    save_data()
def deposit(user_id):
    user_pin = data["users"][user_id]["pin"]
    pin = int(input("enter your pin: "))
    if pin == user_pin:
        bank_balance = data["bank_vault"]
        user_balance = data["users"][user_id]["balance"]
        print(f"your current balance is: {user_balance}")
        putin = int(input("enter the amount you want to deposit"))
        if putin >= 0 :
            data["users"][user_id]["balance"]+= putin
            data["bank_vault"] += putin
        else:
            print("enter the amount greater than ZERO")
    else:
        print("wrong pin !!!")
    save_data()
def check_balance(user_id):
    user_balance = data["users"][user_id]["balance"]
    user_name = data["users"][user_id]["name"]
    user_pin = data["users"][user_id]["pin"]
    pin = int(input("enter your pin"))
    if pin == user_pin :
        print(f" {user_name} have {user_balance} in account number {user_id}")
    else:
        print("wrong pin ...")
while isrunning:
    user_id = input("enter your user id: ")
    if user_id in data["users"]:
        print("press")
        print("1. for withdrawls ")
        print("2. for deposits ")
        print("3. check balance")
        print("4. exit")
        user_choice = int(input("enter your choice: "))
        if user_choice == 1:
            withdraw(user_id)
        elif user_choice == 2:
            deposit(user_id)
        elif user_choice == 3:
            check_balance(user_id)
        elif user_choice == 4:
            print("thank you for choosing us !!! ")
            isrunning = False
        else:
            print("enter a valid choice")
            isrunning = False
    elif user_id == "0000":
        admin_password = input("enter the admin password: ")
        if admin_password == admin:
            print(f"the bank currently have: {data['bank_vault']}")
            print(f"total no of users in bank is: {data['total_users']}")
            choice = input("do you want to see the list of people registed with the bank ?? (y/n): ").lower()
            if choice == "y":
                for i in data["users"]:
                    print(f"{data['users'][i]['name']} - {i} - {data['users'][i]['balance']}")
        else:
            print("enter a valid admin password ")
    
    else:
        print("you are not registered with the bank...")
        choice= input("do you want to be registered with the bank ?? (y/n)").lower()
        if choice == "y":
            add_user()
        else:
            print("thank you for choosing us ")
            isrunning = False
