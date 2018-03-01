<<<<<<< HEAD

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


def getTranslatedMessage(mode, message):

    translated = ''

    for symbol in message:

        if symbol.isalpha():
        #testing for letters
        #reverse encryption
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
                    num = 97
                    #upper A
                    num += (25- key)
                elif symbol.islower():
                    num = 65
                    #lower A
                    num += (25 - key)
            if mode[0] == 'e':    
                if symbol.isupper():
                    num = 122
                    #upper Z
                    num -= key
                elif symbol.islower():
                    num = 90
                    #lower Z
                    num -= key

            translated += chr(num)
        
        elif ord(symbol) > 47 and ord(symbol) < 58:
        #if its a number
        #d10 encryption
            if ord(symbol) == 48:
                key = 57
            #0 will be counted as the 10   
            elif ord(symbol) == 49:
                key = 56
            elif ord(symbol) == 50:
                key = 55
            elif ord(symbol) == 51:
                key = 54
            elif ord(symbol) == 52:
                key = 53
            elif ord(symbol) == 53:
                key = 52
            elif ord(symbol) == 54:
                key = 51
            elif ord(symbol) == 55:
                key = 50
            elif ord(symbol) == 56:
                key = 49
            elif ord(symbol) == 57:
                key = 48                
            translated += chr(key)    
            
        else:

            translated += symbol

    return translated
while True:
    mode = getMode()

    message = getMessage()
    translate = getTranslatedMessage(mode, message)
    reversed = translate[::-1]
    print('Your translated text is:')
=======

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


def getTranslatedMessage(mode, message):

    translated = ''

    for symbol in message:

        if symbol.isalpha():
        #testing for letters
        #reverse encryption
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
                    num = 97
                    #upper A
                    num += (25- key)
                elif symbol.islower():
                    num = 65
                    #lower A
                    num += (25 - key)
            if mode[0] == 'e':    
                if symbol.isupper():
                    num = 122
                    #upper Z
                    num -= key
                elif symbol.islower():
                    num = 90
                    #lower Z
                    num -= key

            translated += chr(num)
        
        elif ord(symbol) > 47 and ord(symbol) < 58:
        #if its a number
        #d10 encryption
            if ord(symbol) == 48:
                key = 57
            #0 will be counted as the 10   
            elif ord(symbol) == 49:
                key = 56
            elif ord(symbol) == 50:
                key = 55
            elif ord(symbol) == 51:
                key = 54
            elif ord(symbol) == 52:
                key = 53
            elif ord(symbol) == 53:
                key = 52
            elif ord(symbol) == 54:
                key = 51
            elif ord(symbol) == 55:
                key = 50
            elif ord(symbol) == 56:
                key = 49
            elif ord(symbol) == 57:
                key = 48                
            translated += chr(key)    
            
        else:

            translated += symbol

    return translated
while True:
    mode = getMode()

    message = getMessage()
    translate = getTranslatedMessage(mode, message)
    reversed = translate[::-1]
    print('Your translated text is:')
>>>>>>> 810b4a4cacf1d6373264fe00551aa01d502d68fa
    print(reversed)