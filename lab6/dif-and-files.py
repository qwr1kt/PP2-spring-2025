import os

path= r"/Users/aliaskarmussin/Desktop/PP2-spring-2025/lab3"

#Task 1
print("Task1:")
def list_items(path):
    all_items = os.listdir(path)
    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    print("Directories:", directories)
    print("Files:", files)
    print("All Items:", all_items)

list_items(path)

#Task2
print("\n Task2:")
if os.path.exists(path):
    print(f"Yes, path {path} exists")
else:
    print(f"No,path {path} doesnt exists")

if os.access(path, os.W_OK):
    print(f"The path {path} are writable")
else:
    print(f"No,path {path} are not writable")

if os.access(path, os.X_OK):
    print(f"The path {path} are excecutable")
else:
    print(f"No,path {path} are not executable")


#Task3
print("\n Task3: ")
def test_path(path):
    if os.path.exists(path):
        print("The path exists.")
    
        dir_name = os.path.dirname(path)
        print("Directory portion:", dir_name)
    
        file_name = os.path.basename(path)
        print("Filename portion:", file_name)
    else:
        print("The path does not exist.")
test_path(path)

#Task 4
print("\n Task4: ")
with open("/Users/aliaskarmussin/Desktop/PP2-spring-2025/lab6/meme.txt", "r") as file:
    num_lines = sum(1 for line in file)
print("Total number of lines:", num_lines)

#Task5 
print("\n Task5: ")
my_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

with open("/Users/aliaskarmussin/Desktop/PP2-spring-2025/lab6/meme.txt", "w") as file:

    for item in my_list:

        file.write(item + "\n")

print("List has been written to text.txt")

#Task 6
for letter in range(ord('A'), ord('Z') + 1):
    with open(chr(letter) + ".txt", "w") as g:
        g.write(chr(letter))

#Task 7 
path = r"/Users/aliaskarmussin/Desktop/PP2-spring-2025/lab6/from.txt"
new_text = r"/Users/aliaskarmussin/Desktop/PP2-spring-2025/lab6/to.txt"

with open(path, 'r') as first, open(new_text, 'w') as second:
    for line in first:  
        second.write(line) 

#Task 8 
print("Task: 8")
path = r"/Users/aliaskarmussin/Desktop/PP2-spring-2025/A.txt"
def remove_file(ur_path):
    if os.path.exists(ur_path):
        if os.access(path, os.W_OK):
            os.remove(ur_path)
            print("File is removed succesfully")
        else:
            print("This file is not accesible")
    else:
        print(f"No, path {ur_path} doesnt exists")

remove_file(path)

