from tkinter import *
from tkinter import messagebox

timer_id = None
remaining_time = 0

def start_timer(total_time, interval):
    global timer_id, remaining_time
    if remaining_time > 0:
        total_time = remaining_time
        remaining_time = 0
    minutes = total_time // 60
    seconds = total_time % 60
    zegar.config(text=f"{minutes:02d}:{seconds:02d}")
    if total_time > 0:
        timer_id = window.after(1000, start_timer, total_time - 1, interval)
    else:
        if interval == 25 * 60:
            nr_sesji.config(text="Przerwa")
            start_break_timer(5 * 60)
        else:
            sesja()

def start_break_timer(total_time):
    minutes = total_time // 60
    seconds = total_time % 60
    zegar.config(text=f"{minutes:02d}:{seconds:02d}")
    window.after(1000, start_timer, total_time - 1, 0)

def sesja():
    start.config(text="STOP", command=zatrzymaj)
    nr_sesji.config(text="Czas na naukę")
    powtorzenia = ilosc.get()

    if not powtorzenia.isdigit() or int(powtorzenia) <= 0:
        messagebox.showerror("Błąd", "Musisz wprowadzić dodatnią liczbę!")
        start.config(text="START", command=sesja)
        return None
    
    for i in range(1, int(powtorzenia) + 1):  # Poprawiona iteracja
        start_timer(25 * 60, 25 * 60)

    

def zatrzymaj():
    global remaining_time
    start.config(text="START", command=sesja)
    if timer_id is not None:  # Sprawdzenie, czy timer_id nie jest None
        window.after_cancel(timer_id)
        minutes, seconds = zegar.cget("text").split(":")
        remaining_time = int(minutes) * 60 + int(seconds)

def resetuj():
    global remaining_time
    start.config(text="START", command=sesja)
    if timer_id is not None:  # Sprawdzenie, czy timer_id nie jest None
        window.after_cancel(timer_id)
        remaining_time = 0
    zegar.config(text="25:00")


window = Tk()
window.title("POMODORO SESSIONS")

tytul = Label(window, text="Sesje pomodoro, czyli skuteczna nauka z przerwami")
tytul.grid(row=0, column=1)

zegar = Label(window, text="25:00")
zegar.grid(row=1, column=1)

nr_sesji = Label(window,text="Liczba sesji")
nr_sesji.grid(row=1,column=2)

start = Button(window, text="START", command=sesja)
start.grid(row=2, column=1)

reset = Button(window, text="RESET", command=resetuj)
reset.grid(row=2, column=0)



NUMERIC = StringVar()
ilosc = Entry(window, textvariable=NUMERIC)
ilosc.insert(END, '1')
ilosc.grid(row=2, column=2)

window.mainloop()
