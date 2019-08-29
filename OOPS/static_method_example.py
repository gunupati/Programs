# In general these methods are general utility methods.
# Inside these methods we won't use any instance or class variables.'
# Here we won't provide self or cls arguments at the time of declaration.
# We can declare static method explicitly by using @staticmethod decorator
# We can access static methods by using classname or object reference

class MaheshMath:
    @staticmethod
    def add(a,b):
        print('The sum of ',a+b)
    def multiply(a,b):
        print('The multiply of ',a*b)
    def sub(a,b):
        print('The sub of ',a-b)
    def devide(a,b):
        print('The devide of ',a/b)

MaheshMath.add(10,2)
MaheshMath.multiply(10,2)
MaheshMath.sub(10,5)
MaheshMath.devide(10,5)