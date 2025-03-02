#Task 1
print("Task1:")
size_list = input("Write your list of numbers: ")
my_list = size_list.replace(" ", " * ")  
multiplay = eval(my_list+"1")
print(multiplay)

#Task 2 
print("\nTask2:")
def count_letters(word):
    upper = len(list(filter(str.isupper, word)))
    lower = len(list(filter(str.islower, word)))

    print("Uppers:", upper)
    print("Lowers:", lower)

streang = input("Enter your string: ")
count_letters(streang)


#Task 3
print("\nTask3:")
def palindrome_check(word):
    return word == "".join(reversed(word)) 

a = input("Enter your word to check:")  
if palindrome_check(a):
    print("Yes")  
else: 
    print("No")


#Task 4
import math
import time

print("\nTask4:")
def invoke_square():
    integer = int(input())
    ml_sec = int(input())
    time.sleep(ml_sec/1000)
    print(f"Square root of {integer} after {ml_sec} miliseconds is {math.sqrt(integer)}")
invoke_square()

#Task 5 
print("\nTask5:")
my_tuple = (True,True,True)
def check_tuple(t):
    return all(t)
print(check_tuple(my_tuple))