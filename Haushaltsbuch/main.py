from UI.UIRenderer import render_main_menu
from UI.input_int import input_int
from Enums.MenuPointer import PointingAt 
from enum import Enum

running: bool = True
pointer: int = PointingAt.MainMenu.value

while running:
    match pointer:

        case PointingAt.MainMenu.value:
            render_main_menu()
            auswahl = input_int("Wähle mit einer Zahleneingabe das nächste Menu aus.")
            if auswahl and PointingAt.value_exists(auswahl):
                pointer = auswahl
            else:
                print("Ungültige Eingabe.")

        case PointingAt.EinnahmenErfassen.value:
            print("Test Einnahme Erfassen")
            

        case PointingAt.AusgabenErfassen.value:
            break

