import pyttsx3, pygame
import PyPDF2, nltk
import random, time

def is_english(wyraz):
    return wyraz.lower() in set(nltk.corpus.words.words())

def wyraz(pdf_reader):
    numpages = len(pdf_reader.pages)

    while True:
        text = pdf_reader.pages[random.randint(1, numpages)].extract_text()
        lines = text.split("\n")
        random_line = random.choice(lines)

        if " - " in random_line:
            ang, pol = random_line.split(" - ")
            wyrazenie = ang.split()
            if is_english(wyrazenie[0].strip().lower()):
                return ang.strip(), pol.strip()
                
def z_pliku(plik):
   
    while True:
        plik.seek(0)
        lines = plik.readlines()
        random_line = random.choice(lines)
        if " - " in random_line:
                return random_line.split(" - ")

def nagranie(speaker,ang):
    speaker.save_to_file(ang, "ang.mp3",)
    speaker.runAndWait()
    speaker.stop()

def gra(speaker,zrodlo,opt,punkty):
    if opt == 1 :
        ang, pol = wyraz(zrodlo)
    elif opt == 2:
        ang, pol = z_pliku(zrodlo)

    nagranie(speaker,ang)
    sound = pygame.mixer.Sound("ang.mp3")
                    
    for i in range(2):
        time.sleep(1)
        sound.play()
        if i == 2:
             print("Sprobuj jeszcze raz!!!")

        slowo = input("Wpisz slowo po angielsku: ").strip().lower()

        if slowo == ang.lower():
            punkty += 1
            break    

    else:
        print("Oj nie udało się odgadnąć słowa :(")
        if opt == 1:
            f = open("do_nauki.txt","a+",encoding="utf-8")
            f.write(ang+" - "+pol+"\n")
            f.close()

    print(f"Po angielsku: {ang} i po polsku: {pol}")
    return punkty

def main():
    try:
        sciezka = "C:\\Users\\Dell\\Desktop\\Agnieszka\\python\\nauka_ang_ze_słuchu\\angielski_slownik_tematyczny_2016.pdf"
        speaker = pyttsx3.init()
        speaker.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
        pygame.mixer.init()
        punkty = 0
        
        plan = int(input("Jaki plan na dzisiaj\n1.Nauka słówek\t2.Powtarzanie słowek: "))
        if plan == 1:
            with open(sciezka, "rb") as pdf_file:
                nltk.download('words')
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                           
                while punkty < 2:
                    punkty = gra(speaker,pdf_reader,plan,punkty)
                    
        elif plan == 2:
            try: 
                with open("do_nauki.txt", "r",encoding="utf-8",errors="ignore") as file1:
                    while punkty < 2:
                        punkty = gra(speaker,file1,plan,punkty)
                    file1.close()
            except FileNotFoundError:
                print("Plik ze słówkami nie istnieje :(")
            except Exception as e:
                print(f"Wystąpił błąd: {e}")

        print(f"Dziś pora już kończyć udało ci sie odpowiedzec na {punkty} zagadek :)")
        print("W pliku masz słowka, które sprawiły ci problem poćwicz je!")

    except FileNotFoundError:
        print("Nie można znaleźć pliku PDF.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

main()
