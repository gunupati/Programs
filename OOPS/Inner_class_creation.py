class outer:
    def __init__(self):
        print('Outer class object creation')
    class inner:
        def __init__(self):
            print('inner class object creation')
        def m1(self):
            print("inner class method")
o=outer()
i=o.inner()
i.m1()