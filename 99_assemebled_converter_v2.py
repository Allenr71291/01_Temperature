from tkinter import *
from functools import partial
import random


class Converter:
    def __init__(self):

        # Formatting variables
        background_color = "springgreen2"

        # Initialise list to hold calculation history
        self.all_calculations = []

        # Converter Frame
        self.converter_frame = Frame(bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                            font="Arial 19 bold",
                                            bg=background_color,
                                            padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # user instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                        text="Type in the amount to be "
                                             "converted and then push "
                                             "one of the buttons below...",
                                    font="Arial 10 italic", wrap=290,
                                    justify=LEFT, bg=background_color,
                                    padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3) colours: darkseagreen4 springgreen4
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  bg="DarkSeaGreen4", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="SpringGreen4", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
                                     fg="purple", bg=background_color, pady=10,
                                     text="Conversion goes here")
        self.converted_label.grid(row=4)

        # History / help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                       text="Calculation History", width=15,
                                       command=lambda: self.history(self.all_calculations))
        self.calc_hist_button.grid(row=0, column=0)

        if len(self.all_calculations) == 0:
            self.calc_hist_button.config(state=DISABLED)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5, command=self.help)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):

        error = "#ffafaf"
        # Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"
            self.to_convert_entry.configure(bg="white")

            # Check amount and convert to Farhrenheit
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) +32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            # Check and convert to Centigrade
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees C is {} degrees F".format(to_convert, celsius)

            else:
                answer = "Too Cold!"
                has_errors = "yes"

            # Convert to C

            # Round!!!

            # Display answer
            if has_errors != "yes":
                self.all_calculations.append(answer)
                self.calc_hist_button.config(state=NORMAL)
                self.converted_label.configure(text=answer, fg="blue")
                print(self.all_calculations)
            else:
                self.converted_label.configure(text="This is too cold! \nPlease "
                                                    "enter a new value!", fg="red")
                self.to_convert_entry.configure(bg=error)
                print("This is too cold! Please enter a new value!")

        except ValueError:
            self.converted_label.configure(text="Enter a number!!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded

    def help(self):
        print("You asked for help")
        get_help = Help(self)

        help_text="Help text goes here"

        get_help.help_text.configure(text=help_text)

    def history(self, calc_history):
        History(self, calc_history)


class Help:
    def __init__(self, partner):
        background = "light yellow"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (Help Box)
        self.help_box = Toplevel()

        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Sets up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg=background,
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class History:
    def __init__(self, partner, calc_history):

        background = "light sky blue"

        # disable history button
        partner.calc_hist_button.config(state=DISABLED)

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

        if len(calc_history) > 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history)
                                               - item - 1] + "\n"

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
                                bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Buttons Frame (row 2)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 10 ")
        self.export_button.grid(row=0, column=0)

        # Dismiss button (col 1)
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss",
                                  font="Arial 10 ",
                                  command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def close_history(self, partner):
        partner.calc_hist_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()