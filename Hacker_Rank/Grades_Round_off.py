def gradingStudents(grades):
    # Write your code here
    a = []
    for i in grades[1:]:
        if i < 38:
            a.append(i)
            continue
        if i > 38 and i % 5 == 0:
            a.append(i)
            continue
        if i > 38 and i % 5 != 0 and (str(i))[-1] == '3' or (str(i))[-1] == '8':
            a.append(i+2)
            continue
        if i > 38 and i % 5 != 0 and (str(i))[-1] == '4' or (str(i))[-1] == '9':
            a.append(i+1)
            continue
        if i > 38 and i % 5 != 0:
            a.append(i)
            continue
    return a
print(gradingStudents([23,56,75,68,98,34,54,76,985379857,857948354,8438,3254,5,32,545,435352,43,5325]))