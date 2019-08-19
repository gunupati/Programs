def getMoneySpent(keyboards, drives, b):
    c=[]
    for y in keyboards:
        for x in drives:
            # if (x+y) <= b:
            #     # print(x+y)
            if (x+y) <= b:
                c.append((x+y))

    if len(c)==0:
        return -1
    else:
        return max(c)

#     return max([sum([x,y]) for x in keyboards for y in drives if sum([x,y]) <= b]+[-1])
print(getMoneySpent([40,50,60],[5,8,12],60))