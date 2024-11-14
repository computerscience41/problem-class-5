# Problem - 7 Reading a file safely

with open('notes.txt', 'r') as file:
    for line in file:
        print(line.strip())
