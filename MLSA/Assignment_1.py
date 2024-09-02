#Testing for card validity
Card_no= input("Enter your card no:")
Card_no= [int(num) for num in str(Card_no)]
Card_no= Card_no[::-1]


for i in range(1,len(Card_no),2):
    Card_no[i] *= 2
    if Card_no[i] > 9:
        Card_no[i]-=9
        if sum(Card_no) % 10 == 0:
            print("Valid card!")
        else:
            print("Invalid card")

            
        

#A simple inventory
Inventory = {}

#Adding new product
def adding_product(product_name, quantity,category,Prices,Quantity_Threshold,Sales):
    Inventory[product_name] = quantity, category, Prices, Quantity_Threshold, Sales
    print(f"{product_name} added to inventory")


#Removing existing inventory
def removing_existing_inventory(product_name):
    if product_name  in Inventory:
        del Inventory[product_name]
        print(f"{product_name} removed succesfully")
    else:
        print("Not found in the Inventory")


#Update product quantities
def update_inventory(product_name,quantity):
    if product_name in Inventory:
        Inventory[product_name] = quantity
        print(f"Inventory successfully updated")

    else:
        print("Inventory name not found")

#search inventory
def searching_inventory(product_name):
    if product_name in Inventory:
        print(f"{product_name} found in Inventory")
    else:
        print("Product name not found in inventory")

#display Inventory
def display_inventory():
    for product_name, quantity in Inventory.items():
        print(f"{product_name}:{quantity}")

