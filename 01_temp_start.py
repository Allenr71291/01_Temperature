from tkinter import *


class Converter:
    def __init__(self, parent):

        background_color = "light green"

        self.Converter_frame = Frame(width=400, height=400, bg=background_color)
        self.Converter_frame.grid()

        self.temp_Converter_label = Label(text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_Converter_label.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
