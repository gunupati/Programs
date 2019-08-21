import os
file = open('text1.txt','r')
file1 = open('text2.txt','w')

for i in file:
    xyz = i.split()

    x = int(xyz[0])

    y = int(xyz[1])

    z = int(xyz[2])

    result = catAndMouse(x, y, z)

    file1.write(result + '\n')

file1.close()
