from drink_data import MENU, resources
import os

def report(profits,drink_resources):
    for resource,amount in resources.items():
        if resource == "Water":
            print(f"{resource}: {amount}ml")
        elif resource == "Milk":
            print(f"{resource}: {amount}ml")
        elif resource == "Coffee":
            print(f"{resource}: {amount}g")

    print(f"Money: ${profits}")


def update_resources(count):
    for drink, info in MENU.items():
        if drink == order:
            if count == 2:
                resources["Water"] -= info["ingredients"]["water"]
                resources["Coffee"] -= info["ingredients"]["coffee"]
            
            elif count == 3:
                resources["Water"] -= info["ingredients"]["water"]
                resources["Milk"] -= info["ingredients"]["milk"]
                resources["Coffee"] -= info["ingredients"]["coffee"]



money = None
accurate_money = 0
while True:
    order = input("What drink would you like? (espresso (1),latte (2),cappuccino (3))\n> ")
    if order == "1":
        order = "espresso"
    elif order == "2":
        order = "latte"
    elif order == "3":
        order = "cappuccino"


    if order == "espresso" or order == "latte" or order == "cappuccino":
        water = resources["Water"]
        milk = resources["Milk"]
        coffee = resources["Coffee"]
        count = 0
        for drink, info in MENU.items():
            if drink == order:
                for key in info["ingredients"].keys():
                    count += 1

                if count == 2:
                    if info["ingredients"]["water"] <= water and info["ingredients"]["coffee"] <= coffee:
                        pass

                    else:
                        print(f"{drink}'s resources are not enough!")
                        count = False
                        break
                
                elif count == 3:
                    if info["ingredients"]["water"] <= water and info["ingredients"]["coffee"] <= coffee and info["ingredients"]["milk"] <= milk:
                        pass
                    
                    else:
                        print(f"{drink}'s resources are not enough!")
                        count = False
                        break

        if not count:
            continue
        try:
            quarters = int(input("How many quartures: "))
            dimes = int(input("How many dimes: "))
            nickles = int(input("How many nickles: "))
            pennies = int(input("How many pennies: "))
        except:
            print("Error, Enter integar values for currencies.")
            continue
        
        money = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
        
        accurate_money += round(MENU[order]['cost'],2)
        if MENU[order]["cost"] == money:
            print(f"Here is your {order}, Enjoy!")
            

            update_resources(count)

        
        elif MENU[order]["cost"] < money:
            os.system("clear")
            print(f"Here is ${accurate_money} in change.")
            print(f"Here is your {order}, Enjoy!")
            update_resources(count)

        else:
            print("Sorry that's not enough money. Money refunded.")

        
    elif order == "report":
        report( accurate_money ,resources)
    
    elif order == "exit":
        break

    else:
        print("Wrong Entry, please enter drink name or its number!")
    