from ft_filter import ft_filter

f = [True, "1", 2, (1, 2), False, ()]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def cb(item):
    """Callback to test ft_filter"""
    return isinstance(item, tuple)


def isEven(item):
    return item % 2 != 0


def main():
    """This is the main function"""
    print([x for x in ft_filter(isEven, numbers)])
    print([x for x in filter(isEven, numbers)])
    print(ft_filter.__doc__)


if __name__ == "__main__":
    main()
