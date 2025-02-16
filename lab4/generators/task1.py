def gen_square(n): 
    for i in range(1, n+1):
        yield i**2

n=int(input("Enter a number:"))

for square in gen_square(n): 
    print(square, end=' ')