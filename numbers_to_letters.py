import argparse

def parseArguments():
    parser = argparse.ArgumentParser(description='Apply every variation of a caesar cipher.')
    parser.add_argument('cipher', nargs='+', help='A list of characters or numbers', type=str)

    return parser.parse_args()

def convertFromAscii(numberList):
    return ''.join([chr(i) for i in numberList])

def convertToAscii(string):
    return ' '.join([str(ord(i)) for i in string])

def convertFromAlphaIndex(numberList, baseIndex=1):
    # baseIndex : Where to start indexing the alphabet (ie. a=1,b=2 by default)
    return ''.join([chr(i + baseIndex + ord('A')) for i in numberList])

def convertToAlphaIndex(numberList, baseIndex=1):
    # baseIndex : Where to start indexing the alphabet (ie. a=1,b=2 by default)
    string = []
    for i in numberList:
        if i.isupper():
            string.append(str( (ord(i) - ord('A')) + baseIndex ))
        elif i.islower():
            string.append(str( (ord(i) - ord('a')) + baseIndex ))
        else:
            string.append(str(i))

    return ' '.join(string)

def prettyPrint(string_list, labels):
    for i, string in enumerate(string_list):
        print(labels[i], ':',  string)

if __name__ == "__main__":
    args = parseArguments()
    print(args.cipher)

    # Check to see if numbers -> letters or vis versa
    if args.cipher[0][0].isdigit():
        numberList = [ int(i) for i in args.cipher ]
        asciiLetters = convertFromAscii(numberList)
        indexAlphabet0 = convertFromAlphaIndex(numberList, 0)
        indexAlphabet1 = convertFromAlphaIndex(numberList, 1)

        prettyPrint([asciiLetters, indexAlphabet0, indexAlphabet1], ['Ascii', 'Alphabet0', 'Alphabet1'])
        
    else:
        string = ' '.join(args.cipher)
        asciiNumbers = convertToAscii(string)
        alphabet0 = convertToAlphaIndex(string, 0)
        alphabet1 = convertToAlphaIndex(string, 1)

        prettyPrint([asciiNumbers, alphabet0, alphabet1], ["Ascii", "Alphabet0", "Alphabet1"])

    
