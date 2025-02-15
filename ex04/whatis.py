import sys

if len(sys.argv) > 1:
    try:
        isNumeric = False
        try:
            int(sys.argv[1])
            isNumeric = True
        except ValueError:
            isNumeric = False

        assert isNumeric, "argument is not an integer"
        assert len(sys.argv) < 3, "more than one argument is provided"
        if int(sys.argv[1]) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except AssertionError as inst:
        print(f"{AssertionError.__name__}: {inst}")
