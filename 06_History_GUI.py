from tkinter import *
from functools import partial

# 1.43 into history GUI part 2


class Converter:
    def __init__(self, parent):

        background_color = "light green"

        self.all_calc_list = ['1 degrees C is -17.2 degrees F',
                              '2 degrees C is -16.7 degrees F',
                              '3 degrees C is -16.1 degrees F',
                              '4 degrees C is 39.2 degrees F',
                              '5 degrees C is -15 degrees F',
                              '6 degrees C is 42.8 degrees F',
                              '7 degrees C is 44.6 degrees F']

        self.Converter_frame = Frame(width=400, height=400, bg=background_color, pady=10)
        self.Converter_frame.grid()

        self.temp_Converter_label = Label(self.Converter_frame,
                                          text="Calculation History",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_Converter_label.grid(row=0)

        self.history_button = Button(self.Converter_frame,
                                  text="History",
                                  padx=10,
                                  pady=10, command=self.history)
        self.history_button.grid(row=1)

    def history(self):
        print("You asked for History")
        get_history = History(self)
        get_history.history_text.configure(text="History text goes here")


class History:
    def __init__(self, partner):

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
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent"
                                                           "calculations. Please use"
                                                           "the export button to create"
                                                           "a text file of all your calculations"
                                                           "for this session",
                               justify=LEFT, width=40, bg=background, wrap=250,
                                  font="arial 10 italic", fg="maroon")
        self.history_text.grid(row=1)

        # History Output goes here... (row 3)

        # Export / Dismiss Buttons Frame (row 2)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(Row=3, pady=10)

        # Export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.history_frame, text="Dismiss", width=10, bg=background,
                                  command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_history(self, partner):
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
