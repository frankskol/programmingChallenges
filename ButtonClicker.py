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
		#Creates the buttons
		self.button = Button (self)
		self.button ["text"] = "Total clicks: 0"
		self.button["command"] = self.update_count
		self.button.grid()
	def update_count(self):
		self.button_clicks += 1
		self.button["text"] = "Total Clicks: " + str(self.button_clicks)
root = Tk()
root.title("Button Click Counter")
root.geometry ("300x150")

app = Application(root)

root.mainloop()
