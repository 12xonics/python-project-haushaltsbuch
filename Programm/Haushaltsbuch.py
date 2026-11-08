from Kategorie import Kategorie
from Buchung import Buchung
from Ausgabe import Ausgabe
from Einnahme import Einnahme

class Haushaltsbuch:
    def __init__(self):
        self.buchungen: list[Buchung] = []
        self.kategorien: list[Kategorie] = []
        self.kontostand: float = 0

    def haushaltsbuch_starten(self):
        """Läd bei vorhandener JSON die Daten in den Speicher oder legt die JSON Speicherdatei initial an."""

    def buchung_hinzufügen(self, einnahme: Einnahme):
        self.buchungen.append(einnahme)

    def berechne_kontostand():
        pass

    def monatsbericht_ausgeben():
        pass

    def kategorie_hinzufügen(self, bezeichnung:str, budget: float = None) -> bool:
        for kategorie in self.kategorien:
            if (kategorie.bezeichnung == bezeichnung.strip().upper()):
                return False
            
        neue_kategorie: Kategorie = Kategorie(bezeichnung.strip().upper(), budget)
        self.kategorien.append(neue_kategorie)
        return True

    def kategorien_anzeigen(self):
        print("Verfügbare Kategorien:")
        for kategorie in self.kategorien:
            print(f"- {kategorie.bezeichnung}")

    def budget_setzen(kategorie: Kategorie):
        pass