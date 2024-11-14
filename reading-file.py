#  Problem -2 Reading from a file

with open('shopping_list.txt', 'r') as file:
    for index, line in enumerate(file, start=1):
        print(f"Item {index}: {line.strip()}")
