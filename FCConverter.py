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
		self.instruction = Label (self, text = "Type in a temperature:")
		self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W+E+N+S)
		
		self.temperature = Entry(self)
		self.temperature.grid(row = 1, column = 0, columnspan = 2, sticky = W+E+N+S)
		
		self.fahrenheit_converter = Button(self, text = "Convert to Fahrenheit", command = self.fahrenheit)
		self.fahrenheit_converter.grid(row = 2, column = 0, sticky = W+E+N+S)
		
		self.celsius_converter = Button(self, text = "Convert to Celsius", command = self.celsius)
		self.celsius_converter.grid(row = 2, column = 1, sticky = W+E+N+S)
		
		self.text = Text(self, width = 29, height = 2, wrap = WORD)
		self.text.grid(row = 3, column = 0, columnspan = 2, sticky = W+E+N+S)
	
	def celsius(self):
		#Display message based on temperature typed in
		try:
			message = float(self.temperature.get())
			message = ((message - 32) *5/9)
			message = str(round(message, 1)) + "ºC"
		except:
			message = "You didn't type a number"
		self.text.delete(0.0, END)
		self.text.insert(0.0, message)
	def fahrenheit(self):
		#Display message based on temperature typed in
		try:
			message = float(self.temperature.get())
			message = ((message*9/5) + 32)
			message = str(round(message, 1)) + "ºF"
		except:
			message = "You didn't type a number"
		self.text.delete(0.0, END)
		self.text.insert(0.0, message)
root = Tk()
root.title("Fahrenheit/Celsius Converter")
root.geometry ("240x110")

app = Application(root)

root.mainloop()