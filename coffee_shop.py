import tkinter as tk
from tkinter import messagebox

drinks = {
    "Coffee": 20,
    "Tea": 10,
    "Lemon Tea": 15,
    "Boost": 25,
    "Milk": 12,
    "Horlicks": 18,
    "Ginger Tea": 22,
    "Water": 10,
    "Cappuccino": 25
}

def calculate_bill():
    name = name_entry.get()
    drink = drink_var.get()
    quantity = qty_entry.get()

    if name == "" or quantity == "":
        messagebox.showwarning("Input Error", "Please enter all details")
        return

    quantity = int(quantity)
    price = drinks[drink]
    total = quantity * price

    discount = 0
    if total > 600:
        discount = total * 0.10
    elif total > 400:
        discount = total * 0.07
    elif total >= 250:
        discount = total * 0.05
    elif total > 150:
        discount = total * 0.03

    final_amount = total - discount

    result_text.set(
        f"Hi {name}\n"
        f"Drink: {drink}\n"
        f"Quantity: {quantity}\n"
        f"Total: ₹{total}\n"
        f"Discount: ₹{discount:.2f}\n"
        f"Final Amount: ₹{final_amount:.2f}\n"
        "Please wait for your order!"
    )
root = tk.Tk()
root.title("Coffee Shop")
root.geometry("400x450")
tk.Label(root, text="Coffee Shop", font=("Arial", 18, "bold")).pack(pady=10)
tk.Label(root, text="Enter your name").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text="Select your drink").pack(pady=5)
drink_var = tk.StringVar()
drink_var.set("Coffee")
drink_menu = tk.OptionMenu(root, drink_var, *drinks.keys())
drink_menu.pack()
tk.Label(root, text="Enter quantity").pack(pady=5)
qty_entry = tk.Entry(root)
qty_entry.pack()
tk.Button(root, text="Order Now", command=calculate_bill, bg="green", fg="white").pack(pady=15)
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, justify="left", font=("Arial", 11)).pack(pady=10)
root.mainloop()
