def coffee_shop(name, drink, ):
    if drink == "coffee":
        print(f"wow! that's a good choice, {name} \nwait for 5 minuts and take your order")
        return f"{name}, please take your coffee"        
    elif drink == "tea":
        print(f"wow that's a good choice, {name} \nwait for 5 minuts and take your order")
        return f"{name}, please take your tea"
    elif drink == "boost":
        print(f"wow that's a good choice, {name} \nwait for 5 minuts and take your order")
        return f"{name}, please take your boost"
    elif drink == "horlicks":
        print(f"wow that's a good choice, {name} \nwait for 5 minuts and take your order")
        return f"{name}, please take your horlicks"
    elif drink == "milk":
        print(f"wow that's a good choice, {name} \nwait for 5 minuts and take your order")
        return f"{name}, please take your milk"
    elif drink == "water":
        print(f"wow that's a good choice, {name} \nwait for 5 minuts and take your order")
        return f"{name}, please take your water"
    elif drink == "juice":
        print(f"wow that's a good choice, {name} \nwait for 5 minuts and take your order")
        return f"{name}, please take your juice"
    else:
        return f"{name}, please enter a valid drink"
# coffee_shop(input("Enter your name: "), input("Enter your drink (coffee, tea, boost, horlicks, milk, water, juice): "))
print(f"{coffee_shop(input("Enter your name: "), input("Enter your drink (coffee, tea, boost, horlicks, milk, water, juice): "))}")
