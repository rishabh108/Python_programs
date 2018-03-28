def smart_divide(fun):
    def inner(a,b):
        print("I am going to divide",a ,'and' ,b)
        if b==0:
            print("Cannot divided")
            return
        return fun(a,b)
    return  inner
@smart_divide
def divide(a,b):
    print(a/b)
    return

divide(4,0)

divide(5,2)