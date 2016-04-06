#By Diraj Ravikumar (13255244)

print("Items for Hire by Diraj Ravikumar")

items_hire = open("items.csv","a")

num_lines = sum(1 for line in open('items.csv'))
print("\n{} items loaded from items.csv".format(num_lines))
print("\n")
print("Menu:")
print("(L)ist all items")
print("(H)ire an item")
print("(R)eturn an item")
print("(A)dd new item to stock")
print("(Q)uit")

choice = input()

while True:
    if choice == 'Q' or choice == 'q':
        print("Finished")
        break
    elif choice == 'L' or choice == 'l':
        print("L")
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

        choice = input()