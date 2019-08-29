# Inside method implementation if we are using instance variables then such type of methods are called instance methods.
# Inside instance method declaration,we have to pass self variable.
# def m1(self):
# By using self variable inside method we can able to access instance variables.
# Within the class we can call instance method by using self variable and from outside
# of the class we can call by using object reference.

class Students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Student Name",self.name)
        print("student Marks",self.marks)
    def grade(self):
        if self.marks>=60:
            print('You got First grade')
        elif self.marks>=50:
            print('You got Second grade')
        elif self.marks>=35:
            print('You got Third grade')

        else:
            print("you got Failed")
n=int(input("Please enter total students:"))
for i in range(n):
    name=input("Please enter name of Student:")
    marks=int(input("Please enter marks of the Student:"))

    s=Students(name,marks)
    s.display()
    s.grade()
