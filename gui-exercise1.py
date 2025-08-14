"""
Opgave "GUI step 1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk

padx = 15
pady = 10

mainwindow = tk.Tk()
mainwindow.geometry("150x160")
mainwindow.title("my first GUI")

frame1 = tk.LabelFrame(mainwindow, text="Container")
frame1.grid(column=0, row=0, padx=padx, pady=pady, sticky=tk.N)

label1 = tk.Label(frame1, text="Id")
label1.grid(column=0, row=2, padx=padx, pady=pady)

entry1 = tk.Entry(frame1, width=5)
entry1.grid(column=0, row=4, padx=padx, pady=pady)

button1 = tk.Button(frame1, text="Create")
button1.grid(column=0, row=6, padx=padx, pady=pady)

if __name__ == "__main__":
    mainwindow.mainloop()