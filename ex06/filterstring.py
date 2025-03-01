import sys
from ft_filter import ft_filter


def handleArgsType(args):
    argIsInt = False
    try:
        int(args[2])
        argIsInt = True
    except Exception:
        argIsInt = False
        pass
    if isinstance(args[1], str) and argIsInt:
        return True
    return None


def hasPunc(word):
    has = False
    for i in word:
        if not str(i).isalnum() and not str(i).isspace():
            has = True
    return has


def filter_string(args):
    split = str(args[1]).split()
    string = [x for x in ft_filter(lambda w: not hasPunc(w), split)]
    integer = int(args[2])
    list = [word for word in string if (len(word) > integer)]
    return list


def main():
    """Output a list of words from argv[1]\
          that have a length greater than argv[2]"""
    try:
        if (len(sys.argv) == 3):
            if handleArgsType(sys.argv):
                print(filter_string(sys.argv))
            else:
                raise AssertionError("Bad args types.")
        else:
            raise AssertionError("2 arguments must be provided.")
    except AssertionError as inst:
        print(f"{AssertionError.__name__}: {inst}")


if __name__ == "__main__":
    main()
