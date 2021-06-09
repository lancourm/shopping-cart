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


# D) Displays store info. 	8%
print("----------------------")
print("LANCOUR CORNER DELI")
print("QUEENS, NY")
print("CIRCA 2021")
print("----------------------")

# A) Captures / scans product identifiers. 	8% 

selected_ids = [] #this creates an empty list

while True: #this is an infinite loop that will never finish until 
    choice = input("Please select / scan a valid product id: ")
    print("When finished, type DONE")  # C) Instructs the user about, and handles, the "DONE" signal. 	10%
    if choice.upper() == "DONE":
        break    
    else:
        selected_ids.append(choice) #this adds each product to the list
        # we could choose to display the selected product's name and price here, but let's do it later instead
    print(choice)

print("WE HAVE REACHED THE END OF THE LOOP")
print(selected_ids)

# 2) Perform product lookups to determine what the product's name and price are
# selected_ids = ["1", "2", "3", "2", "1"]

for choice in selected_ids:
    print(choice)
    # lookup the corresponding product!
    # or maybe display the selected product's name and price
matching_products = [p for p in products if str(p["id"]) == str(choice)]
    #matching_product = products["id"]
print(matching_products["name"], matching_products["price"])


#HERE ARE ALL THE THINGS THAT NEED TO BE DONE - ORGANZIZE AND WRITE CODE ACCORDINGLY
# A) Captures / scans product identifiers. 	8% - COMPLETED
# B) Handles invalid inputs, fails gracefully on invalid product lookups. 	10%
# C) Instructs the user about, and handles, the "DONE" signal. 	10% - COMPLETED
# D) Displays store info. 	8% - COMPLETED
# E) Displays checkout date and time, in a human-friendly format. 	10%
# F) Displays names and prices of all scanned products. 	15%
# G) Displays tax and totals. 	15%
# H) Submitted via Git repository which reflects an incremental revision history. 	12%