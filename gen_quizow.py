import random

europe_capitals = {
    "Albania": "Tirana",    "Andora": "Andora la Vella",
    "Austria": "Wiedeń",    "Białoruś": "Mińsk",
    "Belgia": "Bruksela",    "Bośnia i Hercegowina": "Sarajewo",
    "Bułgaria": "Sofia",    "Chorwacja": "Zagrzeb",
    "Cypr": "Nikozja",    "Czechy": "Praga",
    "Dania": "Kopenhaga",    "Estonia": "Tallinn",
    "Finlandia": "Helsinki",    "Francja": "Paryż",
    "Grecja": "Ateny",    "Hiszpania": "Madryt",
    "Holandia": "Amsterdam",    "Irlandia": "Dublin",
    "Islandia": "Reykjavik",    "Liechtenstein": "Vaduz",
    "Litwa": "Wilno",    "Luksemburg": "Luksemburg",
    "Łotwa": "Ryga",    "Macedonia Północna": "Skopje",
    "Malta": "Valletta",    "Mołdawia": "Kiszyniów",
    "Monako": "Monako",    "Niemcy": "Berlin",
    "Norwegia": "Oslo",    "Polska": "Warszawa",
    "Portugalia": "Lizbona",    "Rosja": "Moskwa",
    "Rumunia": "Bukareszt",    "San Marino": "San Marino",
    "Serbia": "Belgrad",    "Słowacja": "Bratysława",
    "Słowenia": "Lublana",    "Szwajcaria": "Bern",
    "Szwecja": "Sztokholm",    "Turcja": "Ankara",
    "Ukraina": "Kijów",    "Węgry": "Budapeszt",
    "Wielka Brytania": "Londyn",    "Włochy": "Rzym",
}

for numer_quizu in range(2):

    #stworzenie pliku na pytania i odpowiedzi
    pytania = open(f"Quiz_nr{numer_quizu}.txt",'w')
    odpowiedzi = open(f"Quiz_nr{numer_quizu}_odpowiedzi.txt",'w')
    pytania.write("Quiz ze stolic Europy\n\n")

    panstwa = list(europe_capitals.keys())
    random.shuffle(panstwa)

    for nr_pytania in range(15):

        pyt = panstwa[nr_pytania]
        odp = europe_capitals[pyt]
        bledne = list(europe_capitals.values())
        del bledne[bledne.index(odp)]
        bledne = random.sample(bledne,3)
        opcje = bledne + [odp]
        random.shuffle(opcje)

        pytania.write(f"{nr_pytania+1}. {pyt} ma stolicę:\n")
        for i in range(4):
            pytania.write(f"   {'ABCD'[i]}. {opcje[i]}\n")
        pytania.write("\n")

        odpowiedzi.write(f"{nr_pytania+1}.{'ABCD'[opcje.index(odp)]}\n")

    pytania.close()
    odpowiedzi.close()
