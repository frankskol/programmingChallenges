def calculo_de_imc ():
	while True:
		try:
			Peso = float(input("Me diga seu peso:\n"))
			break
		except:
			print ("Você não digitou um número. Tente novamente")
	while True:
		try:
			Altura = float(input ("Agora me diga sua altura em metros:\n"))
			break
		except:
			print ("Você não digitou um número. Tente novamente")
	IMC = float(Peso/(Altura*Altura))
	IMC = round(IMC, 1)
	print ("O seu IMC é de " + str(IMC))
	if IMC > 31.1:
		print ("Você está no nível de obesidade")
	elif IMC >= 27.8:
		print ("Você está acima do peso")
	elif IMC >= 26.4:
		print ("Você está levemente acima do peso")
	elif IMC >= 20.7:
		print ("Você está no peso normal")
	else:
		print ("Você está abaixo do peso")
	print ("Muito obrigado por utilizar nossa calculadora :)\nCaso deseje sair do programa, pressione Alt + F4")
print ("Olá! Essa é uma calculadora de IMC")
refazer = True
Refazer = False
while refazer:
		calculo_de_imc()
