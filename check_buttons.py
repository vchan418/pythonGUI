from Tkinter import *

class Application(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		Label(self, 
			  text = "Choose your favorite movie genres"
			  ).grid(row = 0, column = 0, sticky = W)

		Label(self, 
			  text = "Select all that apply"
			  ).grid(row = 1, column = 0, sticky = W)

		# Comedy check button
		self.comedy = BooleanVar()
		Checkbutton(self, 
					text = "Comedy", 
					variable = self.comedy, 
					command = self.update_text
					).grid(row = 2, column = 0, sticky = W)

		# Drama check button
		self.drama = BooleanVar()
		Checkbutton(self, 
					text = "Drama", 
					variable = self.drama, 
					command = self.update_text
					).grid(row = 3, column = 0, sticky = W)
		
		# Romance check button
		self.romance = BooleanVar()
		Checkbutton(self,
					text = "Romance", 
					variable = self.romance, 
					command = self.update_text
					).grid(row = 4, column = 0, sticky = W)

		self.result = Text(self, width=40, height=5, wrap=WORD)
		self.result.grid(row=5, column=0)

	def update_text(self):
		likes = ""

		if self.comedy.get():
			likes += "Comedy "
		
		if self.drama.get():
			likes += "Drama "

		if self.romance.get():
			likes += "Romance"

		self.result.delete(0.0, END)
		self.result.insert(0.0, likes)

root = Tk()
root.title("Check Button Tests")
root.geometry("400x200")

app = Application(root)
root.mainloop()