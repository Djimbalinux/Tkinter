from tkinter import *
import webbrowser

def open_chanel():
    webbrowser.open_new("https://www.youtube.com/channel/UCG9r0px4f69nerGQZVz0LIw")

#creation d'une premiere fenetre
window = Tk()

#renommer la fenetre
window.title("Djimbalinux App")

#Dimensions de la fenetre
window.geometry("720x480")

#Taille minimale
window.minsize(300, 250)

#insertion d'un nouveau logo
window.iconbitmap("logo.ico")

#changer la couleur de fond
window.config(background='#376053')

#Ajouter une boite
frame = Frame(window, bg='#376053') #bd=1, relief=SUNKEN)

#ajouter un premier text
label_title = Label(frame, text='Welcome to Application', font=('Fantasy', 40), bg='#376053', fg='white')
label_title.pack()

#ajouter un sous_titre
label_subtitle = Label(frame, text="Hey c'est ☻ Djimbalinux 2.0 au commande ♫♫♫", font=('Fantasy', 25), bg='#376053', fg='white')
label_subtitle.pack()

#Ajout de bouton
clic = Button(frame, text='♦ Ouvrir YouTube ♦', bg='white', font=('Fantasy', 20),fg='#376053', command=open_chanel)
clic.pack(pady=25, fill=X)

#frame pack
frame.pack(expand=YES)

#affichage de la fenetre
window.mainloop()