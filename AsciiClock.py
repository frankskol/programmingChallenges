from datetime import datetime
import os

def asciiReturner(numero):
    ascii = []
    if numero == 0:
        ascii.append(" 0000 ")
        ascii.append("00  00")
        ascii.append("00  00")
        ascii.append("00  00")
        ascii.append(" 0000 ")
    elif numero == 1:
        ascii.append("1111  ")
        ascii.append("  11  ")
        ascii.append("  11  ")
        ascii.append("  11  ")
        ascii.append("111111")
    elif numero == 2:
        ascii.append(" 2222 ")
        ascii.append("22  22")
        ascii.append("  22  ")
        ascii.append(" 22   ")
        ascii.append("222222")
    elif numero == 3:
        ascii.append(" 3333 ")
        ascii.append("33  33")
        ascii.append("   33 ")
        ascii.append("33  33")
        ascii.append(" 3333 ")
    elif numero == 4:
        ascii.append("44  44")
        ascii.append("44  44")
        ascii.append("444444")
        ascii.append("    44")
        ascii.append("    44")
    elif numero == 5:
        ascii.append("555555")
        ascii.append("55    ")
        ascii.append("55555 ")
        ascii.append("    55")
        ascii.append("55555 ")
    elif numero == 6:
        ascii.append(" 6666 ")
        ascii.append("66    ")
        ascii.append("66666 ")
        ascii.append("66  66")
        ascii.append(" 6666 ")
    elif numero == 7:
        ascii.append("777777")
        ascii.append("   77 ")
        ascii.append("  77  ")
        ascii.append(" 77   ")
        ascii.append("77    ")
    elif numero == 8:
        ascii.append(" 8888 ")
        ascii.append("88  88")
        ascii.append(" 8888 ")
        ascii.append("88  88")
        ascii.append(" 8888 ")
    elif numero == 9:
        ascii.append(" 9999 ")
        ascii.append("99  99")
        ascii.append(" 99999")
        ascii.append("    99")
        ascii.append(" 9999 ")
    return ascii
def printClock(tempo):

    primeiroDigito = tempo.hour // 10
    segundoDigito = tempo.hour % 10
    terceiroDigito = tempo.minute // 10
    quartoDigito = tempo.minute % 10
    quintoDigito = tempo.second // 10
    sextoDigito = tempo.second % 10
    primeiroDigito = asciiReturner(primeiroDigito)
    segundoDigito = asciiReturner(segundoDigito)
    terceiroDigito = asciiReturner(terceiroDigito)
    quartoDigito = asciiReturner(quartoDigito)
    quintoDigito = asciiReturner(quintoDigito)
    sextoDigito = asciiReturner(sextoDigito)
    pontoVirgula = ["  **  ", "  **  ", "      ", "  **  ", "  **  " ]
    for i in range(0, 5):
        print (primeiroDigito[i], segundoDigito[i], pontoVirgula[i], terceiroDigito[i], quartoDigito[i], pontoVirgula[i], quintoDigito[i], sextoDigito[i])
    


    
clear = lambda: os.system('cls')
clockTime = datetime.now().time()
printClock(clockTime)
while True:
    if clockTime.second != datetime.now().time().second:
        clear()
        printClock(clockTime)
        clockTime = datetime.now().time()