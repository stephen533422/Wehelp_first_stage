# -*- coding: UTF-8 -*-
def func(*data):
    # print(data)
    # print(type(data))
    # *data是用來接受任意多個參數並將其放入<tuple>中
    name = []
    tag = False
    for i in range(0,len(data)):
        name.append((data[i][1]))
    for i in range(0,len(name)):
        if(name.count(name[i])==1):
            tag = True
            print(data[i])
    if(tag==False):
        print("沒有")
func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有