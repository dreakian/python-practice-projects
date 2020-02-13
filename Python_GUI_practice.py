# Python GUI practice

#from tkinter import *

#window = Tk()
#window.geometry("500x500")
#window.configure(background="black")
#window.wm_title("Practice GUI exercise")

#top_frame = Frame(window)
#top_frame.pack(side="top")
#bottom_frame = Frame(window)
#bottom_frame.pack(side="bottom")

#username_label = Label(top_frame, text="Username", height=1, width=10)
#password_label = Label(window, text="Password", height=1, width=10)
#username_label.pack()
#password_label.pack()
#username_entry = Entry(top_frame)
#password_entry = Entry(top_frame)
#username_entry.pack()
#password_entry.pack()

#button_one = Button(bottom_frame, text="Button one", background="red", height=4, width=11)
#button_two = Button(bottom_frame, text="Button two", background="yellow", height=4, width=11)
#button_three = Button(bottom_frame, text="Button three", background="blue", height=4, width=11)
#button_four = Button(bottom_frame, text="Button four", background="green", height=4, width=11)
#button_one.pack(side=LEFT)
#button_two.pack(side=LEFT)
#button_three.pack(side=LEFT)
#button_four.pack(side=LEFT)

#window.mainloop()

# Python GUI practice

from tkinter import *

window = Tk()
window.geometry("335x335")
window.configure(background="black")
window.wm_title("Practice GUI exercise")

top_frame = Frame(window)
top_frame.grid()
bottom_frame = Frame(window)
bottom_frame.grid()

username_label = Label(top_frame, text="Username", height=1, width=10)
password_label = Label(top_frame, text="Password", height=1, width=10)
username_label.grid(row=0, column=0)
password_label.grid(row=1, column=0)
username_entry = Entry(top_frame)
password_entry = Entry(top_frame)
username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

button_one = Button(bottom_frame, text="Button one", background="red", height=4, width=11)
button_two = Button(bottom_frame, text="Button two", background="yellow", height=4, width=11)
button_three = Button(bottom_frame, text="Button three", background="blue", height=4, width=11)
button_four = Button(bottom_frame, text="Button four", background="green", height=4, width=11)
button_one.grid()
button_two.grid()
button_three.grid()
button_four.grid()

window.mainloop()

