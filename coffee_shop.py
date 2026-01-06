def coffe_shop():
    name = input("Please enter your name")

    print(f"Welcome to our coffee shop\n Hi {name} Choose your drink:")

    print("\n1.Coffee\n2.Tea\n3.Lemon Tea\n4.Boost\n5.Milk\n6.Horlicks\n7.Ginger Tea\n8.Water\n9.Cappucino")

    choice = input("Enter your drink number: ")
    drink = {
        "1": "Coffee",
        "2": "Tea",
        "3": "Lemon Tea",
        "4": "Boost",
        "5": "Milk",
        "6": "Horlicks",
        "7": "Ginger Tea",
        "8" : "Water",
        "9" : "Cappucino"
    }
    if choice in drink:
        quantity = int(input("Enter the quantity"))
        price = [20, 10, 15, 25, 12, 18, 22, 10, 25]
        item = price[int(choice) - 1]
        total = quantity * item 
        print(f"{name}, you selected {drink[choice]}")
        if total > 150:
            discount = total*3/100
            print(f"Your total is {total} and discount is {discount}")
            print(f"{name}!Please wait for your order to be ready")
        elif total >= 150 and total <= 249:
            discount = total*5/100
            print(f"Your total is {total} and discount is {discount}")
            print(f"{name}!Please wait for your order to be ready")
        elif total > 250 and total <= 400:
            discount = total*7/100
            print(f"Your total is {total} and discount is {discount}")
            print(f"{name}!Please wait for your order to be ready")
        elif total >= 401 and total <= 600:
            discount = total*10/100
            print(f"Your total is {total} and discount is {discount}")
            print(f"{name}!Please wait for your order to be ready")
        else:
            print(f"Your total amount to be paid is {total}\nNote:{name} Add more items and get more discount")
            print(f"{name}!Please wait for your order to be ready")
            print("Thanks for visiting our coffee shop")
            print(f"{name}, Tell us your experience about the our coffee shop")
            experience = input("Enter your experience: ")
        print("Thank you for your feedback! have a nice day\n        Visit again          ")
    else:
        print(f"{name} your drink is not available, please select from the list")
coffe_shop()
