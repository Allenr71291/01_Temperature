from tkinter import *
from functools import partial


class Converter:
    def __init__(self, parent):

        background_color = "light green"

        self.Converter_frame = Frame(width=400, height=400, 
                                     bg=background_color, 
                                     pady=10)
        self.Converter_frame.grid()

        self.temp_Converter_label = Label(self.Converter_frame,
                                          text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_Converter_label.grid(row=0)

        self.export_button = Button(self.Converter_frame,
                                  text="Export",
                                  padx=10,
                                  pady=10, command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        print("You asked for export")
        get_export = Export(self)
        get_export.export_text.configure(text="Export text goes here")


class Export:
    def __init__(self, partner):

        background = "light yellow"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (Export Box)
        self.export_box = Toplevel()

        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Sets up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.export_frame, text="Dismiss", width=10, bg=background,
                                  command=partial(self.close_export, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_export(self, partner):
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()





# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
