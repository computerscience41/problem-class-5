#  Problem - 10 Handling multiple Exception

try:
    with open('shopping_list.txt', 'r') as source_file:
        content = source_file.read()

    with open('List_backup.txt', 'w') as backup_file:
        backup_file.write(content)

except FileNotFoundError:
    print("The file 'shopping_list.txt' was not found.")

except IOError:
    print("An error occurred while writing to 'List_backup.txt'.")

