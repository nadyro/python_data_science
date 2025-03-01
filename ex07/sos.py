import sys
from ft_filter import ft_filter
from morse_dict import MORSE_DICT

def has_special_char(char: str):
    if (not char.isalnum() and not char.isspace()):
        return True
    return False


def find_special_char(characters: list[str]):
    hasSpecialChar = [x for x in ft_filter(has_special_char, characters)]
    if (len(hasSpecialChar) > 0):
        return True
    return False
    

def parse_args(args):
    if (len(args) == 2):
        if (not args[1]):
            return None
        characters = [x for x in args[1]]
        if (find_special_char(characters)):
            return None
        return True
    return None



def match_chars_with_morse(chars: list[str]):
    strToMorse = [MORSE_DICT[x.upper()] for x in chars]
    string = ''.join(strToMorse).strip()
    return string


def main():
    args = sys.argv
    try:
        if (parse_args(args) is None): 
            raise AssertionError("Arguments are bad.")
        print(match_chars_with_morse(args[1]))
    except AssertionError as inst:
        print(f"{AssertionError.__name__}: {inst}")
        exit()



if __name__ == "__main__":
    main()