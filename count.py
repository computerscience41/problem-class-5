# Problem - 5 Counting words in a file

with open('shopping_list.txt', 'r') as file:
    word_count = sum(len(line.split()) for line in file)
    print(f"Total number of words (items): {word_count}")
