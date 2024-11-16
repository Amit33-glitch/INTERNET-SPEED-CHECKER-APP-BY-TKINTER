from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10**6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10**6), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

app = Tk()
app.title("Internet Speed Test")
app.geometry("500x700")
app.configure(bg="Red")

lab_title = Label(app, text="Internet Speed Test", font=("Time New Roman", 30, "bold"), bg="#801818", fg="White")
lab_title.place(x=60, y=40, height=50, width=380)

lab_down_label = Label(app, text="Download Speed", font=("Time New Roman", 30, "bold"), bg="#801818", fg="White")
lab_down_label.place(x=60, y=130, height=50, width=380)

lab_down = Label(app, text="00", font=("Time New Roman", 30, "bold"), bg="#801818", fg="White")
lab_down.place(x=60, y=200, height=50, width=380)

lab_up_label = Label(app, text="Upload Speed", font=("Time New Roman", 30, "bold"), bg="#801818", fg="White")
lab_up_label.place(x=60, y=270, height=50, width=380)

lab_up = Label(app, text="00", font=("Time New Roman", 30, "bold"), bg="#801818", fg="White")
lab_up.place(x=60, y=340, height=50, width=380)

button = Button(app, text="CHECK SPEED", font=("Time New Roman", 30, "bold"), relief=RAISED, bg="red", command=speedcheck)
button.place(x=60, y=410, height=50, width=380)

app.mainloop()