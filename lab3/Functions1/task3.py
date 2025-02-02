def puzzle(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    return f"Chickens: {chickens}, Rabbits: {rabbits}"
print(puzzle(35,94))