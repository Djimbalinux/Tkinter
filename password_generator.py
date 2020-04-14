import string
from random import randint, choice
from tkinter import *

def generate_password():
    password_min = 8
    password_max = 24
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    champ_password.delete(0, END)
    champ_password.insert(0, password)

#creer une fenetre
window = Tk()

window.title("Password_generator")
window.geometry("720x480")
window.minsize(320, 320)
window.config(bg="#4065A4")
window.iconbitmap("digital-key.ico")

#creer une boite
frame = Frame(window, bg='#4065A4')

#creer une image
width = 300
height = 300
image = PhotoImage(file='pword.png').zoom(35).subsample(32)

#creation d'un canevas
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)

#mettre l'image dans le canevas
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

#creer une sous boite
sub_frame = Frame(frame, bg='#4065A4')

#creer un titre
title = Label(sub_frame, text='Password', bg='#4065A4', font=('Helvetica', 20), fg='white')
title.pack()

#creer un champs
champ_password = Entry(sub_frame, bg='#4065A4', font=('Helvetica', 20), fg='white')
champ_password.pack()

#creer un bouton
clic_ok = Button(sub_frame, text='♦ Generate ♦', bg='#4065A4', font=('Helvetica', 20), fg='white', command=generate_password)
clic_ok.pack(fill=X)

#packer sub_frame
sub_frame.grid(row=0, column=1, sticky=W)
#Affiche la boite
frame.pack(expand=YES)

#Creation d'une barre de menu
menu_bar = Menu(window)

#creer un 1er menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New file", command=generate_password)
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

#Configurer notre fenetre pour ajouter le menu_bar
window.config(menu=menu_bar)

#Afficher la fenetre
window.mainloop()