def get_number(index):
    number=0
    for i in range(0,index+1):
        if(i==0): number=number+0
        elif(i%2==0): number=number-1
        elif(i%2==1): number=number+4
    print(number)
get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15