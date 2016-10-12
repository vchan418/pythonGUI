from Tkinter import *

class Application(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.instruction = Label(self)
		self.instruction["text"] = "Enter the password here:"
		self.instruction.grid(row = 0, column = 0, sticky = W)

		self.password = Entry(self)
		self.password.grid(row = 0, column = 1, sticky = W)

		self.submit_button = Button(self)
		self.submit_button["text"] = "Submit"
		self.submit_button["command"] = self.reveal
		self.submit_button.grid(row = 2, column = 0, sticky = W)

		self.text = Text(self)
		self.text["width"] = 40
		self.text["height"] = 10
		self.text["wrap"] = WORD
		self.text.grid(row = 3, column = 0, columnspan = 2, sticky = W)

	def reveal(self):
		content = self.password.get()
		if content == "password":
			message = "good job"
		else:
			message = "Wrong password"
		self.text.delete(0.0, END)
		self.text.insert(0.0, message)

root = Tk()
root.title("Buttons using class")
root.geometry("400x200")

app = Application(root)
root.mainloop()
