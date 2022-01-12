from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def data_save():
    """Data is saved in a text file
    delete the data in website entry and password entry"""
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

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
            # data is save in data.xt
            with open('data.txt', 'a') as data:
                data.write(f'{website} | {email} | {password}\n')
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
            # show an info dialog that data is saved
            messagebox.showinfo(title="Data Save", message="Data is Save")


# ---------------------------- UI SETUP ------------------------------- #

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

website_entry = Entry(highlightthickness=2, width=50)
website_entry.grid(column=1, row=1, pady=2, padx=2, columnspan=2, sticky=W)
website_entry.focus()
email_entry = Entry(highlightthickness=2, width=50)
email_entry.grid(column=1, row=2, pady=2, padx=2, columnspan=2, sticky=W)
email_entry.insert(0, "konyak@yahoo.com")
pass_entry = Entry(highlightthickness=2, width=30)
pass_entry.grid(column=1, row=3, sticky=W)

generate_button = Button(text='Generate Password', highlightthickness=2)
generate_button.grid(column=2, row=3, pady=2, padx=2, sticky=E)
add_button = Button(text='Add', highlightthickness=2, width=42, command=data_save)
add_button.grid(column=1, row=4, pady=2, padx=2, columnspan=2, sticky=W)

window.mainloop()
