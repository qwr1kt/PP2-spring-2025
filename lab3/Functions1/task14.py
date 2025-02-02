def weight_calculator(grams):
    ounces = 28.3495231 * grams
    return ounces
in_gram = float(input("Your product in grams:"))
print("Your product in ounches:",weight_calculator(in_gram))




def temperature(F):
    C = (5 / 9) * (F - 32)
    return C

F=float(input("Temperature in Fahrenheit: "))
print("In Celsius:",temperature(F))



def puzzle(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    return f"Chickens: {chickens}, Rabbits: {rabbits}"
print(puzzle(35,94))



def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

numbers_str = input("enter list numbers: ")
numbers_list = list(map(int, numbers_str.split()))

print("Prime numbers:", filter_prime(numbers_list))



from itertools import permutations

def print_permutations(s):
    perms = permutations(s)
    for perm in perms:
        print(''.join(perm))

user_input = input("Enter a string: ")
print_permutations(user_input)




def rev_sentence(sentence):
    rev=list(sentence.split())
    rev.reverse()
    for i in rev:
        print(i, end =" ")

text=input()
rev_sentence(text)



def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))



def spy_game(my_list):
    norm = [0,0,7]
    new = [x for x in my_list if (x ==0 or x==7)]
    if new==norm:
       print("True")
    else: 
        print("False")
    
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0])



import math
def volumespher(radius):
    V=(4*math.pi*(radius**3))/3
    return V
    
radius=float(input("radius:"))
print(volumespher(radius))



def uniqe(my_list):
    set_list=[]
    for i in my_list:
        if i not in set_list:
            set_list.append(i)
    print(set_list)

uniqe([1,1,2,3,4,4,5,5,5,5])



def is_polyndrome(my_string):
    return my_string == my_string[::-1]

print(is_polyndrome("abba"))
print(is_polyndrome("apple"))



def histogram(nums):
    for i in nums: 
        print("*"*i)

nums = [4, 9, 7]
histogram(nums)



import random
def guess_the_number():
    player_name = input("Hello! What is your name?")
    print(f"Well,{player_name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    attempts = 0  

    while True:
            guess = int(input("Take a guess."))  
            attempts += 1

            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Good job,{player_name}! You guessed my number in {attempts} guesses!")
                break  
      
guess_the_number()


