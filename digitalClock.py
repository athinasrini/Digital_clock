from tkinter import Tk, Label
window = Tk()
window.title("Digital Clock")
window.geometry("600x300")
window.configure(bg="darkgreen")
label = Label(window, text="SriniA..!!",font=("Arial Black",78,"bold"),bg="darkgreen",fg="yellow")
label.pack(pady=100)
window.mainloop()
