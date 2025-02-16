def generate_num(N):
    for i in range(N, -1, -1):
        yield i  

N = int(input("Enter a number N: "))
for num in generate_num(N):
    print(num, end=" ")