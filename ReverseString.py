from tkinter import *

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
		self.entrytext = Entry(self)
		self.entrytext.grid(row = 1, column = 0, columnspan = 2, sticky = W+E+N+S)
		
		
		self.revertido = Button(self, text = "Reverse", command = self.reverse_string)
		self.revertido.grid(row = 2, column = 0, columnspan = 2, sticky = W+E+N+S)
		
		self.instruction = Label (self, text = "Type in something to reverse:")
		self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W+E+N+S)

		self.text = Text(self, width = 29, height = 2, wrap = WORD)
		self.text.grid(row = 3, column = 0, columnspan = 2, sticky = W+E+N+S)
		
	
	def reverse_string(self):
		texto = str(self.entrytext.get())
		new_word = ""
		length = len(texto)
		for item in range(length -1,-1,-1):
			new_word += texto[item]
		self.text.delete(0.0, END)
		self.text.insert(0.0, new_word)
root = Tk()
root.title("Revert String")
root.geometry ("240x110")

app = Application(root)

root.mainloop()
