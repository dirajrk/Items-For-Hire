"""
|=============================|
|By Diraj Ravikumar (13255244)|
|=============================|
"""

print("Items for Hire - by Diraj Ravikumar\n")

num_lines = sum(1 for line in open('items.csv')) #counts the number of items present in items.csv
print("{} items loaded from items.csv".format(num_lines)) #shows the number of items present in items.csv

menu = ("\nMenu: \n(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd new item to stock \n(Q)uit")
print(menu)
choice = input(">>>")

def list_items():
    """
    A function to load items from items.csv

    Function list_items()

    item_count = 0
    items_hire = open items.csv
    read items.csv
    print serial number, name, description, price, hire from items.csv
    """

    item_count = 0
    with open('items.csv') as file:
        item_lines_list = file.readlines()
    for line in item_lines_list:
        name, desc, price, hire = line.split(',')
        print(item_count, " - ", name," (", desc, ") ", " = $", price, hire, end="")
        item_count += 1

def hire_items(): #A function to hire items from items.csv
    """

    """
    with open('items.csv') as file:
        item_lines_list = file.readlines()
    for line in item_lines_list:
        name, desc, price, hire = line.split(',')
        print(name," (", desc, ") ", " = $", price, end="")

while True:
    if choice == 'Q' or choice == 'q': #if user chooses to quit the program, it shows the number of items saved and breaks the program
        print("\n{} items saved to items.csv".format(num_lines))
        break
    elif choice == 'L' or choice == 'l': #list all the items

        print("All items on file (* indicates item is currently out):\n")
        list_items() #Calls the items load function

        print("\n",menu) #prints out the menu
        choice = input(">>>")

    elif choice == 'H' or choice == 'h': #hire an item
        print(menu)
        choice = input(">>>")
    elif choice == 'R' or choice == 'r': #return an item back
        print(menu)
        choice = input(">>>")
    elif choice == 'A' or choice == 'a': #add a new item to stock
        #NAME
        name = input("Item name: ")
        while len(name) < 0:
            print("Input cannot be blank")
            name = input("Item name: ")

        #DESCRIPTION
        desc = input("Description: ")

        #PRICE
        try:
            price = float(input("Price per day: $"))
            while price < 0:
                    print("Price must be >= $0 \nInvalid input; enter a valid number")
                    price = float(input("Item price: $"))
        except ValueError:
            print("Invalid input; enter a valid number")
            price = float(input("Item price: $"))

        new_item = open("items.csv", "a")
        print("{},{},{:.2f},{}".format(name, desc, price, "in"), file=new_item)
        print("\n{} ({}), ${:.2f} now available for hire.".format(name, desc, price))
        new_item.close()
        num_lines += 1

        print(menu)
        choice = input(">>>")
    else:
        #if the user chooses an option that is not available from the menu
        print("Invalid Option!")

        print(menu)
        choice = input(">>>")