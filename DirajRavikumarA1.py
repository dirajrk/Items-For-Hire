#By Diraj Ravikumar (13255244)

print("Items for Hire by Diraj Ravikumar\n")

import csv

items_hire = open("items.csv","r") #opens the .csv file
items_hire_reader = csv.DictReader(items_hire,fieldnames=['itemName','desc','price','hire']) #used to read the lines in csv and separate them by their commas
#items_hire_writer=csv.writer(items_hire)

num_lines = sum(1 for line in open('items.csv')) #counts the number of items present in items.csv

def list_items(): #A function to load items from items.csv
    """
    Pseudo code coming soon.
    """
    item_count = 0
    for i in items_hire_reader:
        if i['hire'] == 'out':
            out = "*"
            print(item_count, ' - ', i['itemName'], '(', i['desc'], ')', '= $', i['price'], out)
        else:
            print(item_count, ' - ', i['itemName'], '(', i['desc'], ')', '= $', i['price'])
        item_count += 1


print("{} items loaded from items.csv".format(num_lines)) #shows the number of items present in items.csv

print("\nMenu:")
print("(L)ist all items")
print("(H)ire an item")
print("(R)eturn an item")
print("(A)dd new item to stock")
print("(Q)uit")

choice = input(">>>")

while True:
    if choice == 'Q' or choice == 'q':
        print("\n{} items saved to items.csv".format(num_lines))
        break
    elif choice == 'L' or choice == 'l':
        print("All items on file (* indicates item is currently out):")
        list_items() #Calls the items load function
        print("\n")
        print("Menu:")
        print("(L)ist all items")
        print("(H)ire an item")
        print("(R)eturn an item")
        print("(A)dd new item to stock")
        print("(Q)uit")
        choice = input(">>>")
    elif choice == 'H' or choice == 'h':
        print("H")
    elif choice == 'R' or choice == 'r':
        print("R")
    elif choice == 'A' or choice == 'a':
        print("A")
    else:
        print("Invalid Option!")
        print("Menu:")
        print("(L)ist all items")
        print("(H)ire an item")
        print("(R)eturn an item")
        print("(A)dd new item to stock")
        print("(Q)uit")

        choice = input(">>>")