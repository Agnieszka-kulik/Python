from tkinter import *
from tkinter import messagebox
import pygame

timer_id = None
remaining_time = 0

def sesja(powtorzenia):
    start.config(text="STOP", command=zatrzymaj)

    if int(powtorzenia) <= 0:
        return None
    
    if not powtorzenia.isdigit():
        messagebox.showerror("Błąd", "Musisz wprowadzić dodatnią liczbę!")
        start.config(text="START", command=sesja)
        return None
    
    nr_sesji.config(text=f"1/{powtorzenia}")
    
    powtorzenia = int(powtorzenia)  # Konwersja na liczbę całkowitą
    
    while powtorzenia > 0:
        # Uruchomienie pierwszej sesji nauki
        start_timer(10, 10, powtorzenia)
        
        # Dodatkowo, uruchomienie sesji przerwy
        window.after(10 * 1000 * powtorzenia, start_break, powtorzenia)
        powtorzenia -= 1  # Odejmujemy 1 od liczby powtórzeń po każdej sesji

def start_break(powt):
    nr_sesji.config(text="Przerwa")
    start_timer(5, 5, powt)

def start_timer(total_time, interval, powt):
    global timer_id, remaining_time
    if remaining_time > 0:
        total_time = remaining_time
        remaining_time = 0
    minutes = total_time // 60
    seconds = total_time % 60
    zegar.config(text=f"{minutes:02d}:{seconds:02d}")
    
    if total_time > 0:
        timer_id = window.after(1000, start_timer, total_time - 1, interval, powt)
    else:
        if interval == 10:
            sound = pygame.mixer.Sound("sound.mp3")
            start_break(powt - 1)
        else:
            return None


def zatrzymaj():
    global remaining_time
    start.config(text="START", command=sesja)
    if timer_id is not None: 
        window.after_cancel(timer_id)
        minutes, seconds = zegar.cget("text").split(":")
        remaining_time = int(minutes) * 60 + int(seconds)

def resetuj():
    global remaining_time
    start.config(text="START", command=sesja)
    if timer_id is not None: 
        window.after_cancel(timer_id)
        remaining_time = 0
    zegar.config(text="25:00")

pygame.mixer.init()
window = Tk()
window.title("POMODORO SESSIONS")

tytul = Label(window, text="Sesje pomodoro, czyli skuteczna nauka z przerwami")
tytul.grid(row=0, column=1)

zegar = Label(window, text="25:00")
zegar.grid(row=1, column=1)

nr_sesji = Label(window,text="Liczba sesji")
nr_sesji.grid(row=1,column=2)

NUMERIC = StringVar()
ilosc = Entry(window, textvariable=NUMERIC)
ilosc.insert(END, '1')
ilosc.grid(row=2, column=2)

start = Button(window, text="START", command=lambda:sesja(ilosc.get()))
start.grid(row=2, column=1)

reset = Button(window, text="RESET", command=resetuj)
reset.grid(row=2, column=0)

window.mainloop()
