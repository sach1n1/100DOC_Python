from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


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
        is_ok = messagebox.askokcancel(title=website_input.get(),
                                       message=f"Details Entered:\n"
                                               f"Email: {email_input.get()}\n"
                                               f"Password: {pass_input.get()}")
        if is_ok:
            with open("pass.txt", "a") as pass_file:
                    pass_file.write(f"{website_input.get()} | {email_input.get()} | {pass_input.get()}\n")
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

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(END, "abc@abc.com")

pass_input = Entry(width=21)
pass_input.grid(row=3, column=1, sticky="EW")

pass_gen_button = Button(text="Generate Password!", command=password_generator)
pass_gen_button.grid(row=3, column=2, sticky="EW")

add_btn = Button(text="Add", width=36, command=on_add_click)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
