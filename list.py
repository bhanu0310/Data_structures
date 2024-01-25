def first_second(my_list):
    my_list.sort()
    ma=max(my_list)
    n=my_list.count(ma)
    
    return my_list[len(my_list)-1],my_list[len(my_list)-1-n]
myList = [84,85,86,85,90,90,90,85,83,23,45,84,1,2,0]
print(first_second(myList))
