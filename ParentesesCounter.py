from tkinter import *

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()
def parChecker(symbolString):
	s = Stack()
	balanceamento = True
	indice = 0
	while indice < len(symbolString) and balanceamento:
		symbol = symbolString[indice]
		if symbol == "(":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanceamento = False
			else:
				s.pop()
		indice = indice + 1
	if balanceamento and s.isEmpty():
		return ("Está balanceado.")
	else:
		return ("Não está balanceado.")
		 
		 
class Application(Frame):
	"""A GUI application for Fahrenheit and Celsius Conversion"""
	def __init__(self, master):
		#Initializes Frame
		Frame.__init__(self, master)
		self.grid()
		self.button_clicks = 0
		self.create_widgets()
		
	def create_widgets(self):
		#Create button, text and entry widgets
		self.instruction = Label (self, text = "Type in something to check parentheses:")
		self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W+E+N+S)
		
		self.entrytext = Entry(self, width = 42)
		self.entrytext.grid(row = 1, column = 0, columnspan = 2, sticky = W+E+N+S)
		
		self.checker = Button(self, height = 2, text = "Reverse", command = self.check_parentheses)
		self.checker.grid(row = 2, column = 0, columnspan = 2, sticky = W+E+N+S)

		self.text = Text(self, width = 42, height = 3, wrap = WORD)
		self.text.grid(row = 3, column = 0, columnspan = 2, sticky = W+E+N+S)
		
	def check_parentheses(self):
		cont1 = 0
		cont2 = 0
		texto = str(self.entrytext.get())
		length = len(texto)
		for i in range (0,length):
			if texto[i] == "(":
				cont1 += 1
			elif texto[i] == ")":
				cont2 += 1
		balanceado = parChecker(texto)
		self.text.delete(0.0, END)
		self.text.insert(0.0, (str(cont1) + " Aberturas de parênteses e " + str(cont2) + " Fechamentos de parênteses.\n" + balanceado))
	

		
root = Tk()
root.title("Contador de Parênteses")
root.geometry ("345x140")

app = Application(root)

root.mainloop()
	