
def getMode():

    while True:

        print('Do you wish to encrypt or decrypt a message?')

        mode = input().lower()

        if mode in 'encrypt e decrypt d'.split():

            return mode

        else:

            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():

    print('Enter your message:')

    return input()


def getTranslatedMessage(mode, message, key):

    translated = ''

    for symbol in message:

        if symbol.isalpha():
            if symbol.upper() == 'A':
                key = 0
            elif symbol.upper() == 'B':
                key = 1
            elif symbol.upper() == 'C':
                key = 2
            elif symbol.upper() == 'D':
                key = 3
            elif symbol.upper() == 'E':
                key = 4
            elif symbol.upper() == 'F':
                key = 5
            elif symbol.upper() == 'G':
                key = 6
            elif symbol.upper() == 'H':
                key = 7
            elif symbol.upper() == 'I':
                key = 8
            elif symbol.upper() == 'J':
                key = 9
            elif symbol.upper() == 'K':
                key = 10
            elif symbol.upper() == 'L':
                key = 11
            elif symbol.upper() == 'M':
                key = 12
            elif symbol.upper() == 'N':
                key = 13
            elif symbol.upper() == 'O':
                key = 14
            elif symbol.upper() == 'P':
                key = 15
            elif symbol.upper() == 'Q':
                key = 16
            elif symbol.upper() == 'R':
                key = 17
            elif symbol.upper() == 'S':
                key = 18
            elif symbol.upper() == 'T':
                key = 19
            elif symbol.upper() == 'U':
                key = 20
            elif symbol.upper() == 'V':
                key = 21
            elif symbol.upper() == 'W':
                key = 22
            elif symbol.upper() == 'X':
                key = 23
            elif symbol.upper() == 'Y':
                key = 24
            elif symbol.upper() == 'Z':
                key = 25    
            
            if mode[0] == 'd':
                if symbol.isupper():
                    num = ord(65)

                    num += (25- key)
                elif symbol.islower():
                    num = ord(97)

                    num += (25 - key)
            if mode[0] == 'e':    
                if symbol.isupper():
                    num = ord(90)

                    num -= key
                elif symbol.islower():
                    num = ord(122)

                    num -= key

            translated += chr(num)

        else:

            translated += symbol

    return translated

mode = getMode()

message = getMessage()

print('Your translated text is:')

print(getTranslatedMessage(mode, message, key))