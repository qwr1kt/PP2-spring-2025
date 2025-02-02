def temperature(F):
    C = (5 / 9) * (F - 32)
    return C

F=float(input("Temperature in Fahrenheit: "))
print("In Celsius:",temperature(F))