def countApplesAndOranges(s, t, a, b, apples, oranges):
    sam_house_range=range(s,t+1)
    print(sam_house_range)
    ap=0
    o=0
    for i in apples:
        if a+i in sam_house_range:
            ap +=1
    for j in oranges:
        if b+j in sam_house_range:
            o +=1
    return (ap,o)
print(countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6]))