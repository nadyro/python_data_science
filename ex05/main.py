import sys


class StringElements:
    """Data object for counting the elements of the string"""
    uppercase = 0
    lowercase = 0
    punctuation = 0
    digits = 0
    spaces = 0


def handleNoArgs():
    """In the case where user provides no inline args,
    handleNoArgs prompts the user for a new args"""

    print("What is the text to count?")
    for line in sys.stdin:
        if ('q' == line.rstrip()):
            break
        handleCounting(line)
        break


def handlePrints(strElem: StringElements, string: str):
    """Display results of the counting operations."""

    print(f"The text contains {len(string)} characters: ")
    print(f"{strElem.uppercase} upper letters")
    print(f"{strElem.lowercase} lower letters")
    print(f"{strElem.punctuation} punctuation marks")
    print(f"{strElem.spaces} spaces")
    print(f"{strElem.digits} digits")


def handleCounting(string: str):
    """Function to count the number of each occurences"""

    strElem = StringElements()
    for letter in string:
        if (letter.isupper()):
            strElem.uppercase += 1
        elif (letter.islower()):
            strElem.lowercase += 1
        elif letter == "\r":
            strElem.spaces += 1
        elif (letter.isspace()):
            strElem.spaces += 1
        elif (not letter.isalnum() and not letter.isspace()):
            strElem.punctuation += 1
        elif (letter.isdigit()):
            strElem.digits += 1
    handlePrints(strElem, string)


def main():
    """This is the main function"""

    try:

        if (len(sys.argv) < 2):
            handleNoArgs()
        elif (len(sys.argv) == 2):
            string = sys.argv[1]
            handleCounting(string)
        else:
            raise AssertionError("more than one argument is provided")
    except AssertionError as inst:
        print(f"{AssertionError.__name__}: {inst}")


if __name__ == "__main__":
    main()
