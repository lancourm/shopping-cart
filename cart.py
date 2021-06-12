# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

total_price = 0
selected_ids = []

# A) Captures / scans product identifiers. 	8% 
# C) Instructs the user about, and handles, the "DONE" signal. 	10%
while True: #this is an infinite loop that will never finish until we command it to
    selected_id = input("Please select / scan a valid product id, or DONE: ") 
    if selected_id == "DONE":
        break 
    else:
        selected_ids.append(selected_id)


# D) Displays store info. 	8%
print("----------------------")
print("LANCOUR CORNER DELI")
print("QUEENS, NY")
print("CIRCA 2021")
print("www.LancourCornerDeli.com")
print("----------------------")

# E) Displays checkout date and time, in a human-friendly format.

import datetime
import time
e = datetime.datetime.now()
print ("CHECKOUT AT:")
print ("%s/%s/%s" % (e.day, e.month, e.year))
print (time.strftime("%I:%M"))

print("----------------------")


# F) Displays names and prices of all scanned products. 	15% - COMPLETED
#print("SELECTED PRODUCT: " + matching_product["name"], to_usd(matching_product["price"]))
print("SELECTED ITEMS: ")
for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    print(matching_product["name"] + " " + to_usd(matching_product["price"]))

print("----------------------")

# G) Displays tax and totals. 	15%

print("TOTAL PRICE: ", to_usd(total_price))
print("TAX: ", to_usd(total_price *.085))
print("FINAL PRICE INCLUDING TAX: ", to_usd(total_price * 1.085))

print("----------------------")

print("Thank you for shopping at Lancour Corner Deli!")
print("We hope to see you again soon!")
#for item in products:
    #total = total + item (NEED TO FIGURE OUT HOW TO FIND PRICE)



#HERE ARE ALL THE THINGS THAT NEED TO BE DONE - ORGANZIZE AND WRITE CODE ACCORDINGLY
# A) Captures / scans product identifiers. 	8% - COMPLETED
# B) Handles invalid inputs, fails gracefully on invalid product lookups. 	10%
# C) Instructs the user about, and handles, the "DONE" signal. 	10% - COMPLETED
# D) Displays store info. 	8% - COMPLETED
# E) Displays checkout date and time, in a human-friendly format. 	10% - COMPLETED
# F) Displays names and prices of all scanned products. 	15% - COMPLETED
# G) Displays tax and totals. 	15%
# H) Submitted via Git repository which reflects an incremental revision history. 	12%