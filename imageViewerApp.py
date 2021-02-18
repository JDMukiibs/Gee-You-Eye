import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path


class Gallery(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("My Gallery")
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=tk.W+tk.E+tk.N+tk.S)

        # Make rows and columns expandable
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Open the directory and create a list of images
        self.image_list = []
        basepath = Path('images/')
        images_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
        for image in images_in_basepath:
            self.image_list.append(ImageTk.PhotoImage(Image.open(image)))

        # Label that will display the images as we go through them
        # If there are no images, a message saying no images will be displayed
        # Otherwise we show the images.
        if not self.image_list:
            self.my_label = tk.Label(self, text="No images in gallery!")
            self.my_label.grid(row=0, column=0, columnspan=3, sticky=tk.W+tk.E+tk.N+tk.S)
            self.my_label.rowconfigure(0, weight=1)
            self.my_label.columnconfigure(0, weight=1)

            # Exit Button
            self.exit_button = tk.Button(self, text="Exit Gallery", command=self.quit())
            self.exit_button.grid(row=1, column=0, columnspan=3, sticky=tk.W+tk.E+tk.N+tk.S)
        else:
            self.my_label = tk.Label(image=self.image_list[0])
            self.my_label.grid(row=0, column=0, columnspan=3, sticky=tk.W+tk.E+tk.N+tk.S)

        # Buttons for navigation
        self.back_button = tk.Button(self, text="<<", command=self.back, state=tk.DISABLED)
        self.back_button.grid(row=1, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

        self.exit_button = tk.Button(self, text="Exit Gallery", command=self.quit())
        self.exit_button.grid(row=1, column=1, sticky=tk.W + tk.E + tk.N + tk.S)

        self.forward_button = tk.Button(self, text=">>", command=lambda: self.forward(2))
        self.forward_button.grid(row=1, column=2, sticky=tk.W + tk.E + tk.N + tk.S)

    def forward(self, image_number):
        self.my_label.grid_forget()  # Use this to get rid of previous image so that new image and old image don't overlap with each other

        # Create the space for the new image.
        self.my_label = tk.Label(image=self.image_list[image_number-1])
        self.my_label.grid(row=0, column=0, columnspan=3, sticky=tk.W+tk.E+tk.N+tk.S)

        # Updating buttons for navigation
        self.forward_button = tk.Button(self, text=">>", command=lambda: self.forward(image_number+1))
        self.forward_button.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S)

        self.back_button = tk.Button(self, text="<<", command=lambda: self.back(image_number-1))
        self.back_button.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        # 3 because I am testing with 3 images
        if image_number == 3:
            self.forward_button = tk.Button(self, text=">>", state=tk.DISABLED)

    def back(self, image_number):
        self.my_label.grid_forget()

        self.my_label = tk.Label(image=self.image_list[image_number - 1])
        self.my_label.grid(row=0, column=0, columnspan=3, sticky=tk.W+tk.E+tk.N+tk.S)

        # Updating buttons for navigation
        self.forward_button = tk.Button(self, text=">>", command=lambda: self.forward(image_number + 1))
        self.forward_button.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S)
        self.back_button = tk.Button(self, text="<<", command=lambda: self.back(image_number - 1))
        self.back_button.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        # 1 would mean we are at the first image and so we can't go back because we are back where we started.
        if image_number == 1:
            self.back_button = tk.Button(self, text="<<", state=tk.DISABLED)


if __name__ == "__main__":
    Gallery().mainloop()
