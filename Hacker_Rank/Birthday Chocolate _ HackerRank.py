def birthday(s, d, m):
    a=0
    for i in range(len(s)):
        b=0
        c=0
        while(b<(m)):
            c+=s[i+b]
            b+=1
        if(c==d):
            a+=1
        if(i+b==len(s)):
            break
        print(b)
        print(c)
    return a

print(birthday([4,5,4,2,4,5,2,3,2,1,1,5,4],15,4))