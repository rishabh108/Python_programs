class A:
    def __init__(self):
        print('A')


class B:
    def __init__(self):
        print('B')
        super().__init__()


class C(A, B):
    pass


C()
