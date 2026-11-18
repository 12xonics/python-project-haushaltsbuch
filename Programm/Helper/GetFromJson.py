

from Kategorie import Kategorie
from Einnahme import Einnahme
from Ausgabe import Ausgabe
import json


def laden(haushaltsbuch):

    with open("haushaltsbuch.json", "r") as file:
        daten: dict = json.load(file)

# Kategorie laden

    for eintrag in daten["kategorien"] :     
        bezeichnung = eintrag["bezeichnung"]
        budget = eintrag ["budget"]
        kategorie = Kategorie(bezeichnung,budget)
        haushaltsbuch.kategorien.append(kategorie)

    

   # Einnahmen laden     

    for eintrag in daten["einnahmen"] :
        betrag = eintrag ["betrag"]
        beschreibung = eintrag["beschreibung"]
        kategorie = eintrag["kategorie"]
        #timestamp = eintrag ["timestamp"]

        einnahme = Einnahme(betrag, Kategorie(kategorie["bezeichnung"],kategorie["budget"]), beschreibung)#,timestamp)
        haushaltsbuch.einnahmen.append(einnahme)

    

# Ausgaben laden

    for eintrag in daten["ausgaben"]:
        betrag = eintrag ["betrag"]
        beschreibung = eintrag["beschreibung"]
        kategorie = eintrag["kategorie"]
        #timestamp = eintrag ["timestamp"]

        ausgabe = Ausgabe(betrag,Kategorie(kategorie["bezeichnung"],kategorie["budget"]), beschreibung)#timestamp) 
        haushaltsbuch.ausgaben.append(ausgabe)
    

        


   
    
 

    


 