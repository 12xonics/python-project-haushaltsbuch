

from Kategorie import Kategorie
from Einnahme import Einnahme
from Ausgabe import Ausgabe
import json


def laden(haushaltsbuch):
    print("DEBUG: LADEN AUFGERUFEN")
    print("Einnahmen", len(haushaltsbuch.einnahmen))
    print("Ausgaben", len(haushaltsbuch.ausgaben))
    print("Kategorien", len(haushaltsbuch.kategorien))

    with open("haushaltsbuch.json", "r") as file:
        daten: dict = json.load(file)

# Kategorie laden

    for eintrag in daten["kategorien"] :     
        bezeichnung = eintrag["bezeichnung"]
        budget = eintrag ["budget"]
        
        kategorie = Kategorie(bezeichnung)
        kategorie.set_budget(budget)

        haushaltsbuch.kategorien.append(kategorie)

   # Einnahmen laden     

    for eintrag in daten["einnahmen"] :
        betrag = eintrag ["betrag"]
        beschreibung = eintrag["beschreibung"]
        kategorie_name = eintrag["kategorie"]

        kategorie = None

        for vorhandene_kategorie in haushaltsbuch.kategorien:
            if vorhandene_kategorie.bezeichnung == kategorie_name:
                kategorie = vorhandene_kategorie
                break

    if kategorie is None:
        kategorie = Kategorie (kategorie_name)
        haushaltsbuch.kategorien.append(kategorie)

        einnahme = Einnahme(betrag, kategorie, beschreibung)
        haushaltsbuch.einnahmen.append(einnahme)

# Ausgaben laden

    for eintrag in daten["ausgaben"]:
        betrag = eintrag ["betrag"]
        beschreibung = eintrag["beschreibung"]
        kategorie_name = eintrag["kategorie"]

        kategorie = None

    for vorhandene_kategorie in haushaltsbuch.kategorien:
        if vorhandene_kategorie.bezeichnung == kategorie_name:
            kategorie = vorhandene_kategorie
            break
    
        if kategorie is None:
            kategorie = Kategorie (kategorie_name)
            haushaltsbuch.kategorien.append(kategorie)

        ausgabe = Ausgabe(betrag, kategorie, beschreibung) 
        haushaltsbuch.ausgaben.append(ausgabe)
    

        


   
    
 

    


 