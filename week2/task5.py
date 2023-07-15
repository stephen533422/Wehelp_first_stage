def find_index_of_car(seats, status, number):
    seats_left=[]
    max_int=2**63-1
    min=max_int
    min_index=-1
    for i in range(0,len(seats)):
        if(status[i] and seats[i]-number>=0):
            seats_left.append(seats[i]-number)
        else:
            seats_left.append(max_int)
        if(seats_left[i]<min):
            min=seats_left[i]
            min_index=i
    print(min_index)
find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2