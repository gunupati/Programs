# Inside method implementation if we are using only class variables (static variables), then such type
# of methods we should declare as class method.
# We can declare class method explicitly by using @classmethod decorator.
# For class method we should provide cls variable at the time of declaration
# We can call classmethod by using classname or object reference variable


class Animal():
    legs=4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs'.format(name,cls.legs))
Animal.walk('Dog')
Animal.walk('Cat')