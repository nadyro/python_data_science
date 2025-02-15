def ft_filter(callback, iterable):
    """ft_filter(function or None, iterable) --> ft_filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    if (callback is None):
        newList = iter([i for i in iterable if (bool(i))])
        return newList

    if all(False for _ in iterable):
        return iter(iterable)

    newList = iter([i for i in iterable if (callback(i))])
    return newList
