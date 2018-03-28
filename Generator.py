def my_gen():
    n = 1
    print('This is printed first  ',n)
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second ',n)
    yield n

    n += 1
    print('This is printed at last',n)
    yield n

a = my_gen()
next(a)
next(a)
next(a)