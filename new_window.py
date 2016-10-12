from Tkinter import *

class Application(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.submit_button = Button(self,
									text = "Create new window",
									command = self.create_window
									).grid(row = 1, column = 0, sticky = W)

	def create_window(self):
		window = Toplevel(self)
		window.wm_title("Window opened")

		window.geometry("400x200")
		label = Label(window, text = "This is a window")
		label.grid(row = 0, column = 0, sticky = W)


if __name__ == "__main__":
	root = Tk()
	root.title("Create new window")
	root.geometry("400x200")

	app = Application(root)
	root.mainloop()
