def weight_calculator(grams):
    ounces = 28.3495231 * grams
    return ounces
in_gram = float(input("Your product in grams:"))
print("Your product in ounches:",weight_calculator(in_gram))
