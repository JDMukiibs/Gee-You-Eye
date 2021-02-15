import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Learn to Do stuff")

my_img = ImageTk.PhotoImage(Image.open("My best Valorant game to date.png"))
my_label = tk.Label(image=my_img)
my_label.pack()

button_quit = tk.Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()
