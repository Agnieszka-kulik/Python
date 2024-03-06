from tkinter import *
from tkinter import ttk, messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

API_key = "e9775a3dedb04da6952953625cd7b5b3"

#funkcja pokazująca obecną pogodę
def obecna_temp():
    city = rozwijana_lista.get()
    kod = "https://api.openweathermap.org/data/2.5/weather"
    request_url = f"{kod}?q={city}&appid={API_key}&units=metric"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data["main"]["temp"]

        wyswietlanie_pog = Label(window,text=f"{city}:\nWeather: {weather}\nTemperature: {temperature} celsius")
        wyswietlanie_pog.grid(row=4,column=0)

        #print(city+":")
        #print("Weather:", weather)
        #print("Temperature:", temperature, "celsius")

    else:
        messagebox.showinfo(title="Wiadomość o błędzie",message="Takie miasto nie istnieje")
        print("An error occurred.")
        usun_z_listy()

#pomoaga stworzyć dane osi x na wykresie
def konf_dni(date):
    chwil = date.split("-")
    mies = chwil[1]
    dzien, godz = chwil[-1].split(" ")
    godz = godz[0:2]

    return f"{dzien}.{mies} godz.{godz}"

#wyświetla prognozę na najbliższe godziny/dni
def prog():
    city = rozwijana_lista.get()
    kod = "https://api.openweathermap.org/data/2.5/forecast"
    request_url = f"{kod}?q={city}&appid={API_key}&units=metric"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()

        teperaturka_do_wykresu = []
        dni = []

        for i, forecast in enumerate(data['list']):
            date = forecast['dt_txt']
            dni.append(konf_dni(date))

            weather = forecast['weather'][0]['description']
            temperature = forecast['main']['temp']        
            teperaturka_do_wykresu.append(temperature)

            #print(f"{i+1} Date: {date}, Weather: {weather}, Temperature: {temperature} Celsius")

        fig, ax = plt.subplots()
        ax.plot(dni, teperaturka_do_wykresu, linewidth=2.0)
        ax.tick_params(axis='x', rotation=270)
        plt.title(f"Prognoza na najbliższe godziny i dni dla {city}")

        # Dodanie pionowych linii oddzielających dni
        for i in range(len(dni)-1):
            if dni[i][:-10] != dni[i+1][:-10]:
                ax.axvline(x=i+0.5, color='gray', linestyle='--')

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=4, column=1,  padx=5, pady=5)

    else:
        messagebox.showinfo(title="Wiadomość o błędzie",message="Takie miasto nie istnieje")
        print("An error occurred.",response.text)
        usun_z_listy()


#jeśli miasto nie istnieje to usuwa je z listy
def usun_z_listy():
    opcja = rozwijana_lista.get()
    pole_tekstowe = ""
    if opcja in rozwijana_lista["values"]:
        rozwijana_lista["values"] = [item for item in rozwijana_lista["values"] if item != opcja]
        rozwijana_lista.set(opcje[0])
        
#dodaje nowe miasto do listy
def dodaj_do_listy():
    opcja = pole_tekstowe.get()
    if opcja.strip() != "":
        opcja = opcja[0].upper() + opcja[1:].lower()
        lista_choc = rozwijana_lista["values"]
        lista_choc = list(lista_choc)
        lista_choc.append(opcja)
        lista_choc = list(set(lista_choc))
        lista_choc.sort()
        rozwijana_lista["values"] = lista_choc
        rozwijana_lista.set(opcja)


window = Tk()
window.title("Aplikacja pogody")
window.config(background="grey")
icon = PhotoImage(file="ikonka.png")
window.iconphoto(True,icon)
    
naglowek = Label(window,text="POGODA",
                        font=("Arial",40,"bold"),
                        fg = "white",
                        bg = "black",
                        padx = 10, pady = 10)
naglowek.grid(row=0,column=1)

etykieta = Label(window, text="Wybierz lub dodaj miasto:")
etykieta.grid(row=1, column=0, padx=5, pady=5)

opcje = ["Istebna","Krakow","Warszawa"]
opcje.sort()
rozwijana_lista = ttk.Combobox(window, values=opcje)
rozwijana_lista.grid(row=1, column=1, padx=5, pady=5)
rozwijana_lista.set(opcje[0])

etykieta_opcji = Label(window, text="Wpisz własne miasto:")
etykieta_opcji.grid(row=2, column=0, padx=5, pady=5)

pole_tekstowe = Entry(window)
pole_tekstowe.grid(row=2, column=1, padx=5, pady=5)

przycisk_dodaj = Button(window, text="Dodaj do listy",command=dodaj_do_listy)
przycisk_dodaj.grid(row=2, column=3, padx=5, pady=5)

city = rozwijana_lista.get()

teraz = Button(window,
                text= "Wyświetl obecną temperaturę",
                command=obecna_temp,
                font=("Arial",10),
                fg = "white",
                bg = "black",
                padx = 10, pady = 10)
teraz.grid(row=3, column=0, padx=5, pady=5)

prognoza = Button(window,
                text= "Wyświetl prognozę na najbliższe godziny i dni",
                command=prog,
                font=("Arial",10),
                fg = "white",
                bg = "black",
                padx = 10, pady = 10)
prognoza.grid(row=3, column=1, padx=5, pady=5)


window.mainloop()