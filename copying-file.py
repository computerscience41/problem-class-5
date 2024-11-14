# Problem - 9 Copying file contents 

try:
    with open('notes.txt', 'r') as source_file:
        content = source_file.read()
        
    with open('notes_backup.txt', 'w') as backup_file:
        backup_file.write(content)
except IOError as e:
    print(f"An error occurred: {e}")
