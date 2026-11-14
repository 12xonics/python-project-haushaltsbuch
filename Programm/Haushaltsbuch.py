from Kategorie import Kategorie
from Buchung import Buchung
from Ausgabe import Ausgabe
from Einnahme import Einnahme

class Haushaltsbuch:
    def __init__(self):
        self.einnahmen: list[Einnahme] = []
        self.ausgaben: list[Ausgabe] = []
        self.kategorien: list[Kategorie] = []

    def haushaltsbuch_starten(self):
        """Läd bei vorhandener JSON die Daten in den Speicher oder legt die JSON Speicherdatei initial an."""

    def einnahme_hinzufügen(self, einnahme: Einnahme):
        self.einnahmen.append(einnahme)

    def ausgabe_hinzufügen(self, ausgabe: Ausgabe):
        self.ausgaben.append(ausgabe)

    def einnahme_entfernen(self, index: int):
        del self.einnahmen[index]

    def ausgabe_entfernen(self, index: int):
        del self.ausgaben[index]

    def kategorie_entfernen(self, index: int):
        del self.kategorien[index]


    def get_einnahmen(self) -> list:
        return self.einnahmen

    def get_ausgaben(self) -> list:
        return self.ausgaben

    def get_kategorien(self) -> list:
        return self.kategorien

    def berechne_kontostand():
        pass

    def monatsbericht_ausgeben():
        pass

    def kategorie_hinzufügen(self, bezeichnung:str, budget: float = None) -> bool:
        for kategorie in self.kategorien:
            if (kategorie.bezeichnung == bezeichnung.strip().capitalize()):
                return False
            
        neue_kategorie: Kategorie = Kategorie(bezeichnung)
        self.kategorien.append(neue_kategorie)
        return True

    def kategorien_anzeigen(self):
        print("Verfügbare Kategorien:")
        for kategorie in self.kategorien:
            print(f"* {kategorie}")

    def budget_setzen(kategorie: Kategorie):
        pass