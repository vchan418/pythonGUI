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

		self.favorite = StringVar()
		
		# Default select one of the things so that they arent all checked
		self.favorite.set("comedy.")

		Radiobutton(self,
					text = "Comedy",
					variable = self.favorite,
					value = "comedy.",
					command = self.update_text
					).grid(row = 2, column = 0, sticky = W)

		Radiobutton(self,
					text = "Drama",
					variable = self.favorite,
					value = "drama.",
					command = self.update_text
					).grid(row = 3, column = 0, sticky = W)

		Radiobutton(self,
					text = "Romance",
					variable = self.favorite,
					value = "romance.",
					command = self.update_text
					).grid(row = 4, column = 0, sticky = W)
		self.result = Text(self,
						   width = 40,
						   height = 5,
						   wrap = WORD)
		self.result.grid(row = 5, column = 0)

	def update_text(self):
		message = "Your favorite type of movie is %s" % self.favorite.get()
		self.result.delete(0.0, END)
		self.result.insert(0.0, message)

root = Tk()
root.title("Check Button Tests")
root.geometry("400x200")

app = Application(root)
root.mainloop()