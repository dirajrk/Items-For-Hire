"""
Name: Diraj Ravikumar       Student ID: 13255244
Date: 2x/04/2016

Program details: This program is used to hire or return items and it also allows new items to be added.
GitHub: https://github.com/dirajravikumar/DirajRavikumarA1
"""

print("Items for Hire - by Diraj Ravikumar\n")

#counts the number of items present in items.csv
num_lines = sum(1 for line in open('items.csv'))

#shows the number of items present in items.csv
print("{} items loaded from items.csv".format(num_lines))


#prints the menu
menu = ("\nMenu: \n(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd new item to stock \n(Q)uit")
print(menu)
#the user choice
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
    file.close() # every file needs to be closed after their job is done

def hire_items():
    """
    A function to hire items from items.csv

    Function hire_items()

    Display items available
    """
    item_count = 0
    list_num = []
    with open('items.csv') as file:
        item_lines_list = file.readlines() #reads the items from csv file to check if any items require to be hired
    for index,line in enumerate(item_lines_list):
        name, desc, price, hire = line.split(',')
        if 'in' in hire: # prints out the items available to hire
            print("{:<3d} - {:<40s} = ${:>7,.2f}".format(item_count, name + " (" + desc + ") ", float(price)))
            list_num.append(item_count)
        item_count += 1
        # when there is no item available to hire
    if len(list_num) == 0:
        print("Currently no item is available to hire")
    else:
        try:
            # asks the user the item they want to hire
            replace = int(input("Enter the number of an item to hire:\n"))
            if replace in list_num:
                item_lines_list[replace] = item_lines_list[replace].replace('in', 'out')
                with open('items.csv', 'w') as file:
                    file.writelines(item_lines_list) # overwrites the status of an available item that is no longer going to be available
            else:
                print("Item is not available.\n") # when the user chooses the wrong item
        except:
            print("Invalid input")
    file.close() # every file needs to be closed after their job is done

while True:

    if choice == 'Q' or choice == 'q':
        #if user chooses to quit the program, it shows the number of items saved, thanks the user and breaks the program
        print("\n{} items saved to items.csv".format(num_lines))
        print("Have a nice day :)")
        break

    elif choice == 'L' or choice == 'l':
        #if the user chooses to list all the items
        print("All items on file (* indicates item is currently out):\n")
        #Calls the items load function
        list_items()

        print("\n", menu) #prints out the menu
        choice = input(">>>")

    elif choice == 'H' or choice == 'h':
        #if the user chooses to hire an item

        #Calls the hire items function
        hire_items()

        print(menu)
        choice = input(">>>")

    elif choice == 'R' or choice == 'r': #return an item back
        item_count = 0
        list_num = []
        with open('items.csv') as file:
            item_lines_list = file.readlines() #reads the items from csv file to check if any items require to be returned
        for index,line in enumerate(item_lines_list):
            name, desc, price, hire = line.split(',')
            if 'out' in hire: # prints out the items available to return
                print("{:<3d} - {:<40s} = ${:>7,.2f} *".format(item_count, name + " (" + desc + ") ", float(price)))
                list_num.append(item_count)
            item_count += 1
            # when there is no item available to return
        if len(list_num) == 0:
            print("Currently no item is available to return")
        else:
            try:
                #asks the user the item they want to return
                replace = int(input("Enter the number of an item to return: \n"))
                if replace in list_num:
                    item_lines_list[replace] = item_lines_list[replace].replace('out', 'in')
                    with open('items.csv', 'w') as file:
                        file.writelines(item_lines_list)# overwrites the status of an item when it gets returned

                else:
                        print("Item is not available.\n")# when the user chooses a wrong item
            except:
                print("Invalid input")

        #calls the menu
        print(menu)
        choice = input(">>>")
        file.close() #every file needs to be closed after their job is done

    elif choice == 'A' or choice == 'a':
        #adds a new item to items.csv

        #NAME of the item
        name = input("Item name: ")
        while len(name) < 0:
            print("Input cannot be blank")
            name = input("Item name: ")

        #DESCRIPTION of the item
        desc = input("Description: ")
        while len(desc) < 0:
            print("Input cannot be blank")
            desc = input(" Description: ")

        #PRICE section where the user inputs the price per day
        try:
            price = float(input("Price per day: $"))
            while price < 0:
                print("Price must be >= $0 \nInvalid input; enter a valid number")
                price = float(input("Item price: $"))

            #when the user tries to enter a non-float value (string or punctuation)
        except ValueError:
            print("Invalid input; enter a valid number")
            price = float(input("Item price: $"))
        #stores the new item in items.csv as it gets appended
        new_item = open("items.csv", "a")
        print("{},{},{:.2f},{}".format(name, desc, price, "in"), file=new_item)
        print("\n{} ({}), ${:.2f} now available for hire.".format(name, desc, price))
        new_item.close()
        num_lines += 1

        #calls the menu
        print(menu)
        choice = input(">>>")

    else:
        #if the user chooses an option that is not available from the menu
        print("Invalid Option!")

        #calls the menu
        print(menu)
        choice = input(">>>")