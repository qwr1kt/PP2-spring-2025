def uniqe(my_list):
    set_list=[]
    for i in my_list:
        if i not in set_list:
            set_list.append(i)
    print(set_list)

uniqe([1,1,2,3,4,4,5,5,5,5])

