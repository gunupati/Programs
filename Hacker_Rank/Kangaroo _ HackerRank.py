
def kangaroo(x1, v1, x2, v2):
    a=x1+v1
    b=x2+v2
    c,d=0,0
    e=x1 + x2 + v1 + v2
    for i in range(e):
        if a==b:
            return('YES')
            break
        else:
            a +=v1
            b +=v2
    if a!=b:
        return('NO')
print(kangaroo(0,3,4,2))