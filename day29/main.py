from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def search():
    try:
        with open("data.json", "r") as pass_file:
            data = json.load(pass_file)
    except FileNotFoundError:
        messagebox.showinfo("Oops", "No password database exists")
    else:
        try:
            messagebox.showinfo("User Credentials",
                                f"Email: {data[website_input.get()]['email']}\n"
                                f"Password: {data[website_input.get()]['password']}")
            pyperclip.copy(data[website_input.get()]['password'])
        except KeyError as invalid_website:
            messagebox.showinfo("Invalid Website", f"No data saved for {invalid_website}")


def password_generator():
    letter_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = letter_list + number_list + symbol_list
    random.shuffle(password_list)
    password = ''.join(password_list)
    pass_input.insert(END, password)
    pyperclip.copy(password)


def on_add_click():
    if len(website_input.get()) == 0 or len(pass_input.get()) == 0 or len(email_input.get()) == 0:
        messagebox.showinfo("Empty Fields", "Please fill in all the required fileds.")
    else:
        new_data = {
            website_input.get(): {
                "email": email_input.get(),
                "password": pass_input.get()
            }
        }
        try:
            pass_file = open("data.json", "r")
        except FileNotFoundError:
            with open("data.json", "w") as pass_file:
                json.dump(new_data, pass_file, indent=4)
        else:
            data = json.load(pass_file)
            data.update(new_data)
            pass_file.close()
            with open("data.json", "w") as pass_file:
                json.dump(data, pass_file, indent=4)
                website_input.delete(0, END)
                pass_input.delete(0, END)
        finally:
            website_input.delete(0, END)
            pass_input.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1, sticky="EW")

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0, sticky="EW")

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0, sticky="EW")

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0, sticky="EW")

website_input = Entry(width=21)
website_input.grid(row=1, column=1, sticky="EW")
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(END, "abc@abc.com")

pass_input = Entry(width=21)
pass_input.grid(row=3, column=1, sticky="EW")

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky="EW")

pass_gen_button = Button(text="Generate Password!", command=password_generator)
pass_gen_button.grid(row=3, column=2, sticky="EW")

add_btn = Button(text="Add", width=36, command=on_add_click)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
