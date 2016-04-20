"""
Name: Diraj Ravikumar       Student ID: 13255244
Date: 2x/04/2016

Program details: This program is used to hire or return items and it also allows new items to be added.
GitHub: https://github.com/dirajravikumar/DirajRavikumarA1
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
        if "out" in hire:
            print("{:<3d} - {:<40s} = ${:>7,.2f} *".format(item_count, name + " (" + desc + ") ", float(price)))
        else:
            print("{:<3d} - {:<40s} = ${:>7,.2f}".format(item_count, name + " (" + desc + ") ", float(price)))
        item_count += 1
    file.close()

def hire_items():
    """
    A function to hire items from items.csv

    Function hire_items()

    Display items available
    """
    item_count = 0
    list_num = []
    with open('items.csv') as file:
        item_lines_list = file.readlines()
    for index,line in enumerate(item_lines_list):
        name, desc, price, hire = line.split(',')
        if 'in' in hire:
            print("{:<3d} - {:<40s} = ${:>7,.2f}".format(item_count, name + " (" + desc + ") ", float(price)))
            list_num.append(item_count)
        item_count += 1
    if len(list_num) == 0:
        print("Currently no item is available to hire")
    else:
        try:
            replace = int(input("Enter the number of an item to hire:\n"))
            if replace in list_num:
                item_lines_list[replace] = item_lines_list[replace].replace('in', 'out')
                with open('items.csv', 'w') as file:
                    file.writelines(item_lines_list)
            else:
                print("Item is not available.\n")
        except:
            print("Invalid input")
    file.close()

while True:

    if choice == 'Q' or choice == 'q': #if user chooses to quit the program, it shows the number of items saved and breaks the program

        print("\n{} items saved to items.csv".format(num_lines))
        print("Have a nice day :)")
        break

    elif choice == 'L' or choice == 'l': #list all the items

        print("All items on file (* indicates item is currently out):\n")
        list_items() #Calls the items load function

        print("\n", menu) #prints out the menu
        choice = input(">>>")

    elif choice == 'H' or choice == 'h': #hire an item
        hire_items()

        print(menu)
        choice = input(">>>")

    elif choice == 'R' or choice == 'r': #return an item back
        item_count = 0
        list_num = []
        with open('items.csv') as file:
            item_lines_list = file.readlines()
        for index,line in enumerate(item_lines_list):
            name, desc, price, hire = line.split(',')
            if 'out' in hire:
                print("{:<3d} - {:<40s} = ${:>7,.2f} *".format(item_count, name + " (" + desc + ") ", float(price)))
                list_num.append(item_count)
            item_count += 1
        if len(list_num) == 0:
            print("Currently no item is available to return")
        else:
            try:
                replace = int(input("Enter the number of an item to return: \n"))
                if replace in list_num:
                    item_lines_list[replace] = item_lines_list[replace].replace('out', 'in')
                    with open('items.csv', 'w') as file:
                        file.writelines(item_lines_list)
                else:
                        print("Item is not available.\n")
            except:
                print("Invalid input")
        file.close()

        print(menu)
        choice = input(">>>")
        file.close()

    elif choice == 'A' or choice == 'a': #add a new item to stock
        #NAME
        name = input("Item name: ")
        while len(name) < 0:
            print("Input cannot be blank")
            name = input("Item name: ")

        #DESCRIPTION
        desc = input("Description: ")
        while len(desc) < 0:
            print("Input cannot be blank")
            desc = input(" Description: ")

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