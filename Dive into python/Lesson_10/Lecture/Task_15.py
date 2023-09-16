"""
MRO
Аббревиатура MRO — method resolution order переводится как “порядок разрешения
методов”. Относится этот порядок не только к методам, но и ко всем атрибутам
класса. Это внутренний механизм, определяющий порядок наследования.

● ClassName.mro
"""


class A:
    def __init__(self):
        print('Init class A')
        self.data_a = 'A'


class B:
    def __init__(self):
        print('Init class B')
        self.data_b = 'B'


class C:
    def __init__(self):
        print('Init class C')
        self.data_c = 'C'


class D:
    def __init__(self):
        print('Init class D')
        self.data_d = 'D'


class X1(A, C):
    def __init__(self):
        print('Init class X1')
        super().__init__()


class X2(B, D):
    def __init__(self):
        print('Init class X2')
        super().__init__()


class X3(A, D):
    def __init__(self):
        print('Init class X3')
        super().__init__()


class Z(X1, X2, X3):
    def __init__(self):
        print('Init class Z')
        super().__init__()


print(*Z.mro(), sep='\n')
# <class '__main__.Z'>
# <class '__main__.X1'>
# <class '__main__.X2'>
# <class '__main__.B'>
# <class '__main__.X3'>
# <class '__main__.A'>
# <class '__main__.C'>
# <class '__main__.D'>
# <class 'object'>

"""
🔥 Важно! Не стоит из родительских классов обращаться к аргументам и
методам дочерних классов или классов того же уровня наследования.
"""