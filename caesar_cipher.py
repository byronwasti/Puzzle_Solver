import argparse

def parseArguments():
    parser = argparse.ArgumentParser(description='Apply every variation of a caesar cipher.')
    parser.add_argument('characters', nargs='+', help='A list of characters', type=str)

    return parser.parse_args()

def caesarCipher(string, shift):
    new_string = []
    for i in string:

        c = ord(i)
        if c >= 65 and c <= 90: # Capital letter
            c = (( (c-65) + shift) % 26) + 65
        elif c >= 97 and c <= 122:
            c = (( (c-97) + shift) % 26) + 97
        else:
            pass

        new_string.append(chr(c))

    return ''.join(new_string)

def applyAllCiphers(string):
    all_strings = []
    for i in range(1,26):
        all_strings.append(caesarCipher(string, i))

    return all_strings

def prettyPrint(string_list):
    for i, string in enumerate(string_list):
        print(i+1, ':',  string)

if __name__ == "__main__":
    args = parseArguments()
    string = ' '.join(args.characters)

    prettyPrint(applyAllCiphers(string))
