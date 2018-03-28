class overload:

    def add(a, b):
        return a + b

    def add(a, b, c):
        return a + b + c


obj1 = overload()
print (obj1.add(4, 7, 8))