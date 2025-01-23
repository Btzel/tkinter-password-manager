from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator
import json
from random import randint

class Interface:
    def __init__(self):
        # MAIN WINDOW
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)

        # CANVAS
        self.canvas = Canvas(width=200, height=200)
        self.logo_image = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_image)
        self.canvas.grid(column=1, row=0, padx=(30, 0))

        # LABELS
        self.website_label = Label(text="Website: ", )
        self.website_label.grid(column=0, row=1, sticky=E)
        self.email_username_label = Label(text="Email/Username: ", )
        self.email_username_label.grid(column=0, row=2, sticky=E)
        self.password_label = Label(text="Password: ", )
        self.password_label.grid(column=0, row=3, sticky=E)

        # ENTRIES
        self.website_entry = Entry(width=50)
        self.website_entry.grid(column=1, row=1, columnspan=2, sticky=E, pady=1)
        self.website_entry.focus()
        self.email_username_entry = Entry(width=50)
        self.email_username_entry.grid(column=1, row=2, columnspan=2, sticky=E, pady=1)
        self.email_username_entry.insert(index=0, string="buraktsoftware@gmail.com")
        self.password_entry = Entry(width=31)
        self.password_entry.grid(column=1, row=3, sticky=E, padx=(0, 5), pady=1)

        # BUTTONS
        self.generate_password_button = Button(text="Generate Password", width=14,command=self.generate_password)
        self.generate_password_button.grid(column=2, row=3, sticky=E)
        self.add_button = Button(text="Add", width=47,command=self.data_modifier)
        self.add_button.grid(column=1, row=4, columnspan=2, sticky=E, pady=2)

        # DATA
        self.website = ""
        self.email_username = ""
        self.password = ""
        self.data = {}

    def data_modifier(self):
        if (len(self.website_entry.get()) == 0
                or len(self.email_username_entry.get()) == 0
                or len(self.password_entry.get()) == 0):
            messagebox.showwarning("Warning.", "Fill the empty spaces before you save!")
        else:
            self.website = self.website_entry.get()
            self.email_username = self.email_username_entry.get()
            self.password = self.password_entry.get()
            self.data = {
                self.website: {
                    "email or username": self.email_username,
                    "password": self.password,
                }
            }
            will_save = messagebox.askokcancel(title="Save",message=f"There are the details entered:\n"
                                                                    f"Website: {self.website}\n"
                                                                    f"Email or Username: {self.email_username}\n"
                                                                    f"Password: {self.password}\n"
                                                                    f"Are you sure to save?")
            if will_save:
                self.save_password()

    def save_password(self):
        try:
            with open("data.json", "r") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(self.data, file, indent=4)
        except JSONDecodeError:
            with open("data.json", "a") as file:
                json.dump(self.data, file, indent=4)
        else:
            existing_data.update(self.data)
            with open("data.json", "w") as file:
                json.dump(existing_data, file, indent=4)
        finally:
            self.website_entry.delete(0,END)
            self.password_entry.delete(0,END)

    def generate_password(self):
        password_generator = PasswordGenerator(randint(6,8), randint(4,6), randint(4,6))
        self.password = password_generator.generate_password()
        self.password_entry.delete(0,END)
        self.password_entry.insert(0,string=self.password)


interface = Interface()
interface.window.mainloop()