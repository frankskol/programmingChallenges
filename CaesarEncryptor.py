def CaesarCipherEncrypt(textinput, shift):
    cipherText = ""
    for ch in textinput:
        if ch == " ":
           cipherText += " "
           continue
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift 
        if stayInAlphabet > ord('z'):
            stayInAlphabet -= 26
        finalLetter = chr(stayInAlphabet)
        cipherText += finalLetter
    return cipherText
while True:
    Text = input("Tell me the text to Cipher:\n")
    Cypher = int(input("What shall be the shift?\n"))
    print (CaesarCipherEncrypt(Text, Cypher))
    print ("Thank you for using the program! If you want to quit, press ESC, otherwise repeat the operation")
