from UI.UIRenderer import render_main_menu, render_error_message, clear_ui, render_success_message, render_information_message
from UI.input_int import input_int
from UI.input_buchung import input_betrag
from UI.input_yes_no import input_yes_no
from Enums.MenuPointer import PointingAt 
from Einnahme import Einnahme
from Kategorie import Kategorie
from Haushaltsbuch import Haushaltsbuch

demo_haushaltsbuch: Haushaltsbuch = Haushaltsbuch()

demo_haushaltsbuch.kategorie_hinzufügen("Essen")
demo_haushaltsbuch.kategorie_hinzufügen("Auto")
demo_haushaltsbuch.kategorie_hinzufügen("Schule")

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
                render_error_message("Ungültige Eingabe")

        case PointingAt.EinnahmenErfassen.value:
            clear_ui()

            betrag: float = 0
            kategorie: Kategorie = None
            beschreibung: str = ""
            steps: int = 0
            done: bool = False

            while not done:
                match steps:

                    case 0:
                        eingabe: float = input_betrag("Gib den Betrag deiner Einnahme an.")
                        if eingabe:
                            betrag = eingabe

                            steps += 1
                        else:
                            render_error_message("Eingegebener Betrag ungültig")

                    case 1:
                        demo_haushaltsbuch.kategorien_anzeigen()
                        eingabe: str = input("Gib die Kategorie deiner Einnahme an")
                        demo_haushaltsbuch.kategorie_hinzufügen(eingabe)
                        kategorie = Kategorie(eingabe.strip().upper())

                        steps += 1

                    case 2:
                        eingabe: str = input("Gib eine Beschreibung für deine Einnahme an (optional)")
                        beschreibung = eingabe

                        steps += 1

                    case 3:
                        print(f"Betrag: {betrag}")
                        print(f"Kategorie: {kategorie.bezeichnung}")
                        print(f"Beschreibung: {beschreibung}")
                        eingabe = input_yes_no("Diese Einnahme buchen?")
                        if eingabe:
                            if eingabe == "J":
                                neue_einnahme: Einnahme = Einnahme(betrag, kategorie, beschreibung)
                                demo_haushaltsbuch.einnahme_buchen(neue_einnahme)
                                done = True
                                pointer = PointingAt.MainMenu.value
                                render_success_message("Einnahme wurde erfolgreich gebucht")

                            else:
                                done = True
                                pointer = PointingAt.MainMenu.value
                                render_information_message("Vorgang erfolgreich abgebrochen")

                        else:
                            render_error_message("Ungültige Eingabe")

