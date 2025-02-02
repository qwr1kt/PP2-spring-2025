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

