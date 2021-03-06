import json
import string
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """generate random password"""
    pass_list = [random.choice(string.ascii_letters) for _ in range(random.randint(8, 10))] + \
                [str(random.randint(0, 9)) for _ in range(random.randint(2, 4))] + \
                [random.choice(['!', '#', '$', '&', '*', '+']) for _ in range(random.randint(2, 4))]
    random.shuffle(pass_list)
    password_string = "".join(pass_list)
    pass_entry.insert(0, password_string)
    pyperclip.copy(password_string)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def data_save():
    """Data is saved in a json file
    delete the data in website entry and password entry"""
    website = website_entry.get().capitalize()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    # add condition if all data is filled
    if len(website) == 0 and len(password) == 0:
        messagebox.showinfo(title="Check Info", message="Website info and Password info is empty")
    elif website == "":
        messagebox.showinfo(title="Check Info", message="Website info is empty")
    elif password == "":
        messagebox.showinfo(title="Check Info", message="Password info s empty")
    else:
        all_is_filled = messagebox.askokcancel(title="Check Info", message=f"Website: {website}"
                                                                           f"\nEmail: {email}"
                                                                           f'\nPassword: {password}'
                                                                           f'\nDo you want to save?')
        if all_is_filled:
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                pass_entry.delete(0, END)
                # show an info dialog that data is saved
                messagebox.showinfo(title="Data Save", message="Data is Save")


# ---------------------------- UI SETUP ------------------------------- #

def data_no_found():
    messagebox.showinfo(title='Error', message='No Data Found')


def search_data():
    website = website_entry.get().capitalize()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        data_no_found()

    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email : {email}'
                                                       f'\nPassword : {password}')
        else:
            data_no_found()


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='white')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:', bg='white')
website_label.grid(column=0, row=1)
email_label = Label(text='Email/Username:', bg='white')
email_label.grid(column=0, row=2)
pass_label = Label(text='Password:', bg='white')
pass_label.grid(column=0, row=3)


website_entry = Entry(highlightthickness=2, width=30)
website_entry.grid(column=1, row=1, pady=2, padx=2, columnspan=2, sticky=W)
website_entry.focus()
email_entry = Entry(highlightthickness=2, width=50)
email_entry.grid(column=1, row=2, pady=2, padx=2, columnspan=2, sticky=W)
email_entry.insert(0, "konyak@yahoo.com")
pass_entry = Entry(highlightthickness=2, width=30)
pass_entry.grid(column=1, row=3, sticky=W)

search_button = Button(text='Search', width=15, command=search_data)
search_button.grid(column=2, row=1, pady=2, padx=2, sticky=E)
generate_button = Button(text='Generate Password', highlightthickness=2, command=generate_password)
generate_button.grid(column=2, row=3, pady=2, padx=2, sticky=E)
add_button = Button(text='Add', highlightthickness=2, width=42, command=data_save)
add_button.grid(column=1, row=4, pady=2, padx=2, columnspan=2, sticky=W)

window.mainloop()
