from tkinter import *
from functools import partial


class Converter:
    def __init__(self, parent):

        background_color = "light green"

        self.all_calc_list = ['1 degrees C is -17.2 degrees F',
                              '5 degrees C is -15 degrees F',
                              '6 degrees C is 42.8 degrees F',
                              '7 degrees C is 44.6 degrees F']

        self.Converter_frame = Frame(width=400, height=400, bg=background_color, pady=10)
        self.Converter_frame.grid()

        self.temp_Converter_label = Label(self.Converter_frame,
                                          text="Calculation export",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_Converter_label.grid(row=0)

        self.export_button = Button(self.Converter_frame,
                                    text="export", padx=10,pady=10,
                                    command=lambda: self.export(self.all_calc_list))
        self.export_button.grid(row=1)

    def export(self, calc_export):
        print("you want to export")
        Export(self, calc_export)


class Export:
    def __init__(self, partner, calc_export):

        background = "light sky blue"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (export Box)
        self.export_box = Toplevel()

        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Sets up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # export text (label, row 1)
        self.export_text = Label(self.export_frame, text= "Here are your most recent "
                                                           "calculations. Please use"
                                                           "the export button to create"
                                                           "a text file of all your calculations"
                                                           "for this session",
                               justify=LEFT, width=40, bg=background, wrap=250,
                                  font="arial 10 italic", fg="maroon")
        self.export_text.grid(row=1)

        # export Output goes here... (row 3)

        # Generate string from list of calculations...
        export_string = ""

        if len(calc_export) >=7:
            for item in range(0, 7):
                export_string += calc_export[len(calc_export)
                                               - item - 1]+"\n"

        else:
            for item in calc_export:
                export_string += calc_export[len(calc_export) -
                                              calc_export.index(item) - 1] + "\n"
                self.export_text.config(text= "Here is your calculation "
                                              "export. You can use the "
                                              "export button to save this "
                                              "data to a text file if "
                                              "desired.")

        # Label to display calculation export to user
        self.calc_label = Label(self.export_frame, text=export_string,
                                bg=background,font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Buttons Frame (row 2)
        self.export_dismiss_frame = Frame(self.export_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 10 ")
        self.export_button.grid(row=0, column=0)

        # Dismiss button (col 1)
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss",
                                  font="Arial 10 ",
                                  command=partial(self.close_export, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def close_export(self, partner):
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
