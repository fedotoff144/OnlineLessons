"""Two advanced mathematical operations.

Integer, division and exponential."""

__all__ = ['div', 'exp']
_BEGINNING = 0
_CONTINUATION = 1


def div(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
        res //= item
    return res


def exp(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
        res **= item
    return res

#
# if __name__ == '__main__':
#