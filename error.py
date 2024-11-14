#  Problem - 4 Handling FileNotFoundError

try:
    with open('grocery_list.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'grocery_list.txt' was not found.")
