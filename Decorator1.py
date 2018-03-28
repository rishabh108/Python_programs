def first(func):
    def inner():
        print("Inner")
        func()
    return inner
@first
def sec():
    print("Second")

sec()