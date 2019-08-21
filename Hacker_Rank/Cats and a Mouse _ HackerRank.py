def catAndMouse(x, y, z):

    d1 = abs(z - x)
    d2 = abs(z - y)
    if d2 > d1:
        return ('Cat A')
    if d1 > d2:
        return ('Cat B')
    if d1 == d2:
        return ('Mouse C')
# print(catAndMouse(84,17,18))
if __name__=='__main__':
    file = open('text1.txt', 'r')
    file1 = open('text2.txt', 'w')

    for i in file:
        xyz = i.split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        file1.write( '{} \n'.format(result))

    file1.close()