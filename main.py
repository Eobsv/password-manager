import email
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    pass_letters = [choice(letters) for _ in range(0, nr_letters)]
    pass_symbols = [choice(symbols) for _ in range(0, nr_symbols)]
    pass_numbers = [choice(numbers) for _ in range(0, nr_numbers)]

    password_list = pass_numbers + pass_letters + pass_symbols
    shuffle(password_list)

    password_shuffled = "".join(password_list)
    password_entry.insert(0, password_shuffled)
    pyperclip.copy(password_shuffled)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warnign", message="You left some box empty")
    else:
        is_ok = messagebox.askokcancel(title="Website", message=f"There are the details entered: \nEmail: {email}"
                                                                f"\nPassword: {password} \n Is it ok to save?")
        if is_ok:
            try:
                with open('data.json', mode='r') as data_file:
                    data = json.load(data_file)
            except (FileNotFoundError, json.JSONDecodeError):
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open('data.json', mode='w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

        # print(data) # type is dict
# ------------------------- FIND PASS ----------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open('data.json', mode='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No data")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}'
                                                       f'\nPassword: {password}')
        else:
            messagebox.showinfo(title="Error", message="No such website")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PW mng")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1, sticky="EW")
email_entry = Entry(width=37)
email_entry.insert(0, "fake@mail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
generate_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, columnspan=2, sticky="EW")


window.mainloop()
