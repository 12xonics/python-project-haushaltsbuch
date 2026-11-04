from Kategorie import Kategorie
from Ausgabe import Ausgabe
from Einnahme import Einnahme
from UIManager import UIManager

class Haushaltsbuch:
    def __init__(self):
        self.ausgaben: list = []
        self.einnahmen: list = []

    def haushaltsbuch_starten():
        UIManager.render_main_menu()


    def ausgabe_buchen():
        pass

    def einnahme_buchen():
        pass

    def berechne_kontostand():
        pass

    def monatsbericht_ausgeben():
        pass

    def budget_setzen(kategorie: Kategorie):
        pass