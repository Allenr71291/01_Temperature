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
                                          text="Export Calculations",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_Converter_label.grid(row=0)

        self.history_button = Button(self.Converter_frame,
                                  text="Export",
                                  padx=10,pady=10,
                                  command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

    def history(self, calc_history):
        history(self, calc_history)


class history:
    def __init__(self, partner, calc_history):

        background = "light sky blue"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (history Box)
        self.history_box = Toplevel()

        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Sets up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="History / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent "
                                                           "calculations. Please use"
                                                           "the export button to create"
                                                           "a text file of all your calculations"
                                                           "for this session",
                               justify=LEFT, width=40, bg=background, wrap=250,
                                  font="arial 10 italic", fg="maroon")
        self.history_text.grid(row=1)

        # History Output goes here... (row 3)

        # Generate string from list of calculations...
        history_string = ""

        if len(calc_history) >=7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history)
                                               - item - 1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                              calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your calculation "
                                              "history. You can use the "
                                              "export button to save this "
                                              "data to a text file if "
                                              "desired.")

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background,font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Buttons Frame (row 2)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 10 ",
                                    command=lambda: self.export(calc_history))

        self.export_button.grid(row=0, column=0)

        # Dismiss button (col 1)
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss",
                                  font="Arial 10 ",
                                  command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def close_history(self, partner):
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)


class Export:
    def __init__(self, partner, calc_history):

        print(calc_history)

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
        self.export_text = Label(self.export_frame, text="Enter a filename in the box "
                                                         "below and press the Save "
                                                         "button to save your calculation "
                                                         "history to a word file. " ,
                                    justify=LEFT, width=40, bg=background, wrap=250,
                                    font="arial 10 italic", fg="maroon")
        self.export_text.grid(row=1)

        # Export / Dismiss Buttons Frame (row 2)
        self.export_dismiss_frame = Frame(self.export_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 10 ",
                                    command=lambda: self.export(self.all_calc_list))
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
