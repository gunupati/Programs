#Print Even numbers in a list using Lambda function
my_list = [3,5,2,11,6,8]
list_Even_Numbers = filter(lambda varX: varX % 2 == 0,range(100))
print(list_Even_Numbers)
