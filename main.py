from Tkinter import *

root = Tk()

root.title("Labeler")
root.geometry("500x150")

app = Frame(root)
app.grid()

button1 = Button(app, text = "hehehehehe")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text = "This is the second button")

button3 = Button(app)
button3.grid()
button3["text"] = "This is the third button"

# label = Label(app, text = "this is the label")

# label.grid()

root.mainloop()