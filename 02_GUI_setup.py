from tkinter import *


class Converter:
    def __init__(self, parent):

        background_color = "light green"

        self.Converter_frame = Frame(width=400, height=400, bg=background_color, pady=10)
        self.Converter_frame.grid()

        self.temp_Converter_label = Label(self.Converter_frame,
                                          text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_Converter_label.grid(row=0)

        self.help_button = Button(self.Converter_frame,
                                  text="help",
                                  padx=10,
                                  pady=10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
