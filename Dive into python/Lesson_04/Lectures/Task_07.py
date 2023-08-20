# позиционные и ключевые параметры
# - (positional) позиционные параметры передаются согласно позиции
# - (keyword) ключевые параметры передаются согласно названию параметра
#
# Косая черта / и звёздочка * разделяют позиционные и ключевые параметры
# def func(positional_only, /, positional_or_keyword, *, keyword_only):
# pass


def standart_arg(arg):
    """Exeple simple function"""
    print(arg)


standart_arg(42)
standart_arg(arg=42)


def pos_only_arg(arg, /):
    """Пример только позиционной фунцкции"""
    print(arg)


pos_only_arg(42)


# pos_only_arg(arg=42) # positional-only arguments passed as keyword arguments: 'arg'


def kwd_only_arg(*, arg):
    """Пример только ключевой фунцкции"""
    print(arg)


# kwd_only_arg(42) # takes 0 positional arguments but 1 was given
kwd_only_arg(arg=42)

