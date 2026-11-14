from UI.UIRenderer import render_main_menu, render_error_message, clear_ui, render_success_message, render_information_message
from UI.input_int import input_int
from UI.input_buchung import input_betrag
from UI.input_yes_no import input_yes_no
from Enums.MenuPointer import PointingAt 
from Einnahme import Einnahme
from Ausgabe import Ausgabe
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
            clear_ui()
            render_main_menu()
            auswahl = input_int("Wähle mit einer Zahleneingabe das nächste Menu aus.")
            if auswahl and PointingAt.value_exists(auswahl):
                pointer = auswahl
            else:
                render_error_message("Es gibt kein Menu für diese Auswahl")

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
                        if eingabe.strip():
                            demo_haushaltsbuch.kategorie_hinzufügen(eingabe)
                            kategorie = Kategorie(eingabe.strip().upper())

                            steps += 1
                        else:
                            render_error_message("Es muss eine Kategorie angegeben werden")

                    case 2:
                        eingabe: str = input("Gib eine Beschreibung für deine Einnahme an (optional)")
                        beschreibung = eingabe.strip()

                        steps += 1

                    case 3:
                        clear_ui()
                        print(f"Betrag: {betrag}")
                        print(f"Kategorie: {kategorie.bezeichnung}")
                        print(f"Beschreibung: {beschreibung}")
                        eingabe = input_yes_no("Diese Einnahme buchen?")
                        if eingabe:
                            if eingabe == "J":
                                neue_einnahme: Einnahme = Einnahme(betrag, kategorie, beschreibung)
                                demo_haushaltsbuch.einnahme_hinzufügen(neue_einnahme)
                                done = True
                                pointer = PointingAt.MainMenu.value
                                render_success_message("Einnahme wurde erfolgreich gebucht")

                            else:
                                done = True
                                pointer = PointingAt.MainMenu.value
                                render_information_message("Vorgang erfolgreich abgebrochen")

                        else:
                            render_error_message("Ungültige Eingabe")
        
        case PointingAt.AusgabenErfassen.value:
            clear_ui()
            betrag: float = 0
            kategorie: Kategorie = None
            beschreibung: str = ""
            steps: int = 0
            done: bool = False

            while not done:
                match steps:

                    case 0:
                        eingabe: float = input_betrag("Gib den Betrag deiner Ausgabe an.")
                        if eingabe:
                            betrag = eingabe

                            steps += 1
                        else:
                            render_error_message("Eingegebener Betrag ungültig")

                    case 1:
                        demo_haushaltsbuch.kategorien_anzeigen()
                        eingabe: str = input("Gib die Kategorie deiner Ausgabe an")
                        if eingabe.strip():
                            demo_haushaltsbuch.kategorie_hinzufügen(eingabe)
                            kategorie = Kategorie(eingabe.strip().upper())

                            steps += 1
                        else:
                            render_error_message("Es muss eine Kategorie angegeben werden")

                    case 2:
                        eingabe: str = input("Gib eine Beschreibung für deine Ausgabe an (optional)")
                        beschreibung = eingabe.strip()

                        steps += 1

                    case 3:
                        clear_ui()
                        print(f"Betrag: {betrag}")
                        print(f"Kategorie: {kategorie.bezeichnung}")
                        print(f"Beschreibung: {beschreibung}")
                        eingabe = input_yes_no("Diese Ausgabe buchen?")
                        if eingabe:
                            if eingabe == "J":
                                neue_ausgabe: Ausgabe = Ausgabe(betrag, kategorie, beschreibung)
                                demo_haushaltsbuch.ausgabe_hinzufügen(neue_ausgabe)
                                done = True
                                pointer = PointingAt.MainMenu.value
                                render_success_message("Ausgabe wurde erfolgreich gebucht")

                            else:
                                done = True
                                pointer = PointingAt.MainMenu.value
                                render_information_message("Vorgang erfolgreich abgebrochen")

                        else:
                            render_error_message("Ungültige Eingabe")


        case PointingAt.EinnahmenAnzeigen.value:
            clear_ui()
            einnahmen: list = demo_haushaltsbuch.get_einnahmen()

            if len(einnahmen) == 0:
                print("\nKeine Einnahmen im System\n")
            else:
                print("ID / Datum / Betrag / Kategorie / Beschreibung")
                for i in range(len(einnahmen)):
                    print(f"[{i+1}] / {einnahmen[i].get_datum_formatted()} / {einnahmen[i].betrag} / {einnahmen[i].kategorie.bezeichnung} / {einnahmen[i].beschreibung}")

            eingabe = input("\n\nGebe del <id> ein um einen Eintrag zu löschen. Enter zum zurückkehren in das Hauptmenu").strip()
            if eingabe:
                splitted_eingabe = eingabe.split()
                try:
                    if (splitted_eingabe[0].upper() == "DEL") and (int(splitted_eingabe[1]) <= len(einnahmen)):
                            demo_haushaltsbuch.einnahme_entfernen(int(splitted_eingabe[1])-1)
                            render_success_message("Einnahme erfolgreich gelöscht.")
                    else:
                        raise Exception
                except:
                    render_error_message("Ungültige Eingabe")

            else:
                pointer = PointingAt.MainMenu.value


        case PointingAt.AusgabenAnzeigen.value:
            clear_ui()
            ausgaben: list = demo_haushaltsbuch.get_ausgaben()

            if len(ausgaben) == 0:
                print("\nKeine Ausgaben im System\n")
            else:
                print("ID / Datum / Betrag / Kategorie / Beschreibung")
                for i in range(len(ausgaben)):
                    print(f"[{i+1}] / {ausgaben[i].get_datum_formatted()} / {ausgaben[i].betrag} / {ausgaben[i].kategorie.bezeichnung} / {ausgaben[i].beschreibung}")

            eingabe = input("\n\nGebe del <id> ein um einen Eintrag zu löschen. Enter zum zurückkehren in das Hauptmenu").strip()
            if eingabe:
                splitted_eingabe = eingabe.split()
                try:
                    if (splitted_eingabe[0].upper() == "DEL") and (int(splitted_eingabe[1]) <= len(einnahmen)):
                            demo_haushaltsbuch.ausgabe_entfernen(int(splitted_eingabe[1])-1)
                            render_success_message("Ausgabe erfolgreich gelöscht")
                    else:
                        raise Exception
                except:
                    render_error_message("Ungültige Eingabe")

            else:
                pointer = PointingAt.MainMenu.value


        case PointingAt.KategorienAnzeigen.value:
            clear_ui()
            kategorien: list = demo_haushaltsbuch.get_kategorien()

            if len(kategorien) == 0:
                print("\nKeine Kategorien im System\n")
            else:
                print("ID / Bezeichnung / Budget")
                for i in range(len(kategorien)):
                    print(f"[{i+1}] / {kategorien[i].bezeichnung} {kategorien[i].budget}")

            eingabe = input("\n\nGebe del <id> ein um eine Kategorie zu löschen " \
            "\nGebe select <id> budget <budget> ein um ein Budget zu setzen " \
            "\nGebe select <id> budget remove ein um ein Budget zu entfernen \nEnter zum zurückkehren in das Hauptmenu")

            if eingabe:
                splitted_eingabe = eingabe.split()
                try:
                    match splitted_eingabe[0].upper():

                        case "DEL":
                            demo_haushaltsbuch.kategorie_entfernen(int(splitted_eingabe[1])-1)
                            render_success_message("Kategorie erfolgreich gelöscht")

                        case "SELECT":
                            if splitted_eingabe[2].upper() == "BUDGET":
                                if splitted_eingabe[3].upper() == "REMOVE":
                                    kategorien[int(splitted_eingabe[1])-1].set_budget(None)
                                    render_success_message("Budget erfolgreich entfernt")
                                else:
                                    kategorien[int(splitted_eingabe[1])-1].set_budget(float(splitted_eingabe[3]))
                                    render_success_message(f"Budget erfolgreich auf {splitted_eingabe[3]} gesetzt")

                        case _:
                            raise Exception

                except:
                    render_error_message("Ungültige Eingabe")

            else:
                pointer = PointingAt.MainMenu.value