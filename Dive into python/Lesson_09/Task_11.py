"""
Декораторы functools

- Декоратор wraps
✔ __name__ получает имя декорируемой функции
✔ help() возвращает справку декорируемой функции

def count(param):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
        ...
            return result
        return wrapper
    return deco
"""
