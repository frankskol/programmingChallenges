
def getMessage():

    print('Enter your message:')

    return input()


while True:
    message = getMessage()
    reversed = message[::-1]
    print('Your reversed text is:')
    print(reversed)