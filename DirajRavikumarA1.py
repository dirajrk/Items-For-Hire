#By Diraj Ravikumar (13255244)

print("Items for Hire by Diraj Ravikumar")

import csv

cr = csv.reader(open("items.csv","rb"))

print("Menu:")
print("(L)ist all items")
print("(H)ire an item")
print("(R)eturn an item")
print("(A)dd new item to stock")
print("(Q)uit")
