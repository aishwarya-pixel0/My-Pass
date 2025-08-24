from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    #use list comprehension
    password_letters=[random.choice(letters) for _  in range(nr_letters)]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_symbols=[random.choice(letters) for _ in range(nr_symbols)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list=password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    #easier to paste the password while on the website using pyperclip module(copies the password on the clipboard)
    pyperclip.copy(password)
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data={
         web_name.get() : {
              "email": email.get(),
              "password" : password_entry.get(),
         }  
    }
    if len(web_name.get())==0 or len(password_entry.get())==0:
        messagebox.showinfo(title="Oops!",message="Please donot leave any fields empty")
    else:
        # is_ok = messagebox.askokcancel(title=web_name.get(),message=f"These are the details entered \nEmail : {email.get()}"
        #                     f"\nPassword : {password_entry.get()}\nDo you want to proceed?" )
        try:
            with open("data.json","r") as datafile:
                 #reading data to json file
                 data = json.load(datafile)
        except FileNotFoundError:
                 with open("data.json","w") as datafile:
                       json.dump(new_data,datafile,indent=4)
        else:
                 #updating the old data with new data
                 data.update(new_data)
                 with open("data.json","w") as datafile:
                    #writing data to a json file
                    json.dump(data,datafile,indent=4)
        finally:
                #clearing the screen after receiving input
                 web_name.delete(0,END)
                        # email.delete(0,END)
                 password_entry.delete(0,END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
      website=web_name.get()
      try:
        with open("data.json") as data_file:
                data = json.load(data_file)
      except FileNotFoundError:
            messagebox.showinfo(title="Error !",message="No Data File found.")
      else:
            if website in data:
                  email=data[website]["email"]
                  password=data[website]["password"]
                  messagebox.showinfo(title="website",message=f"Email : {email}\nPassword : {password}.")
            else:
                  messagebox.showinfo(title="Data Not Found !",message=f"No Details found for {website}.")
            
   



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pass")
window.config(padx=50,pady=50)
window.configure(bg="lightyellow")
pass_img = PhotoImage(file = "logo1.png")
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image=pass_img)
canvas.grid(column=1,row=0)

#labels
website_label = Label(text="Website : ",bg="lightblue")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username : ",bg="lightblue")
email_label.grid(column=0, row=2)
password_label = Label(text="Password : ",bg="lightblue")
password_label.grid(column=0, row=3)

#entries
web_name = Entry(width=33)
print(web_name.get())
#turns on cursor on the entry
web_name.focus()
#columnspan specifies the width of the entry box
web_name.grid(column=1,row=1)
#index 0 puts the cursor at the start before the string
#index 1 puts the cursor at the end after the string


email = Entry(width=53)
print(email.get())
email.grid(column=1,row=2,columnspan=2)
email.insert(0,"aishwaryasreepathy@gmail.com")

password_entry = Entry(width=33)
print(password_entry.get())
password_entry.grid(column=1,row=3)

#buttons
pas_but = Button(text="Generate Password",command=generate_password,bg="SteelBlue")
pas_but.grid(column=2, row=3)
add_but = Button(text="Add", width=45,command=save,bg="darkgoldenrod")
add_but.grid(column=1, row=5, columnspan=2)
search_but = Button(text="Search",width=15,command=find_password,bg="SteelBlue")
search_but.grid(column=2,row=1)
window.mainloop()