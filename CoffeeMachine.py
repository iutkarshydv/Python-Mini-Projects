machine = {"Water": 300, "Milk": 200, "Coffee": 100}
espresso = {"Water": 50, "Milk": 0, "Coffee": 30}
cappuccino = {"Water": 100, "Milk": 150, "Coffee": 20}
latte = {"Water": 150, "Milk": 100, "Coffee": 30}
glass = {"Water": 0, "Milk": 0, "Coffee": 0}

option = input("What would you like to drink?")
if option == "report":
    print(machine)
elif option == "espresso":
    if machine["Water"] >= espresso["Water"] & machine["Milk"] >= espresso["Milk"] & machine["Coffee"] >= espresso["Coffee"]:
        glass["Water"] = espresso["Water"]
        machine["Water"] = machine["Water"]-espresso["Water"]
        glass["Milk"] = espresso["Milk"]
        machine["Milk"] = machine["Milk"] - espresso["Milk"]
        glass["Coffee"] = espresso["Coffee"]
        machine["Coffee"] = machine["Coffee"] - espresso["Coffee"]
    else:
        print("Sorry, We do not have sufficient stock")
elif option == "cappuccino":
    if machine["Water"] >= cappuccino["Water"] & machine["Milk"] >= cappuccino["Milk"] & machine["Coffee"] >= cappuccino["Coffee"]:
        glass["Water"] = cappuccino["Water"]
        machine["Water"] = machine["Water"]-cappuccino["Water"]
        glass["Milk"] = cappuccino["Milk"]
        machine["Milk"] = machine["Milk"]-cappuccino["Milk"]
        glass["Coffee"] = cappuccino["Coffee"]
        machine["Water"] = espresso["Water"]-cappuccino["Water"]
elif option == "latte":
    if machine["Water"] >= latte["Water"] & machine["Milk"] >= latte["Milk"] & machine["Coffee"] >= latte["Coffee"]:
        glass["Water"] = latte["Water"]
        machine["Water"] = machine["Water"]-latte["Water"]
        glass["Milk"] = latte["Milk"]
        machine["Milk"] = machine["Milk"]-latte["Milk"]
        glass["Coffee"] = latte["Coffee"]
        machine["Coffee"]=machine["Coffee"]-latte["Coffee"]
else:
    print("Invalid option")

print(glass)
print(machine)