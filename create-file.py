#problem -1  Creating and writing to a new file

with open('shopping_list.txt', 'w') as file:
    file.write("Apples\n")
    file.write("Bananas\n")
    file.write("Oranges\n")
    file.write("Bread\n")
    file.write("Milk\n")

