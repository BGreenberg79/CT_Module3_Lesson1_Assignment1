# Task 1 Restaurant Menu Update

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

def new_category(menu, category):
    if category not in menu:
        menu[category] = {}
        print(f"{category} Category has been added to the menu")
    else:
        print(f"{category} is already a category on the menu")

def new_item(menu, category, item, price):
    if category in menu and item not in menu[category]:
        menu[category][item] = price
        print(f"{item} has been added at ${price} to the {category} category of the menu.")
    elif category in menu and item in menu[category]:
        print(f"{item} in the {category} category has already been added to the menu.")
    else:
        print(f"{category} category has not been added to menu yet.")

def price_update(menu, category, item, price):
    if category in menu and item in menu[category]:
        menu[category][item] = price
        print(f"The new price of {item} is ${price}")
    else:
        print("Category or Item has not been added to menu")

def remove_item(menu, category, item):
    if category in menu and item in menu[category]:
        menu[category].pop(item)
        print(f"{item} was removed from the menu.")
    else:
        print("Category or dish has not been added and thus cannot be removed.")

new_category(restaurant_menu, "Beverages")
new_item(restaurant_menu, "Beverages", "Wine", 9.99)
new_item(restaurant_menu, "Beverages", "Coca-Cola", 2.99)
price_update(restaurant_menu, "Main Course", "Steak", 17.99)
remove_item(restaurant_menu, "Starters", "Bruschetta")
'''
To solve this prolem I created four functions. One function was creating a new category that checked if a category wasn't already in 
the menu and if it wasn't created that category with an empty dictionary as a value. The second function was to add new items.
That function worked with an if/elif/else chain where a key value pair of item:price was assigned to any category in the menu with the syntax of 
menu[category][item] = price. The elif statement would check if an item already added to that category was the item we were attempting to add, and the else would catch if 
the user attempted to add an item that's in a non-existant category.
Price update works with a similar if/else block where if category is in menu and item is in menu[category] we will reassign a new price as the innermost value by sing the syntax
menu[category][item] = price again and printing a slightly different print block to state the new price point.
The remove item function woks also as a similar if/else block but this time uses the pop function to remove the item we are trying to remove.
Notably I did not assign the return of this pop method as in this case we are interested in the key being removed more than it's value (price) and that is reflected in the f-string print statement that follows the method.
'''