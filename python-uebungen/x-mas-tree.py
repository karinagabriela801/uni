#Number of rows for the tree
rows = 10

#Loop through each row
for i in range(rows):
    for j in range(rows-i-1):
        print(" ", end="")
    for k in range(2 * i +1):
        print("*", end="")
    print()

for i in range(2):
    for j in range(rows-2):
        print(" ", end="")
    print("***")

