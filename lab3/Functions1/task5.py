from itertools import permutations

def print_permutations(s):
    perms = permutations(s)
    
    for perm in perms:
        print(''.join(perm))

user_input = input("Enter a string: ")
print_permutations(user_input)