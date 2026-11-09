def render_main_menu():
    """Rendert im Terminal das Hauptmenu."""
    print("-=-=-= Erfassung =-=-=-")
    print("[1] Einnahme erfassen.")
    print("[2] Ausgabe erfassen.")
    print("")
    print("-=-=-= Anzeigen =-=-=-")
    print("[3] Einnahmen anzeigen.")
    print("[4] Ausgaben anzeigen.")
    print("[5] Kategorien anzeigen.")
    print("[6] Monatsbericht.")
    print("")
    print("-=-=-= Kontostand =-=-=-")
    print("[7] Kontostand berechnen.")

def render_error_message(message: str):
    """Rendert im Terminal eine Fehlermeldung. Meldung kann über die Stringübergabe bestimmt werden."""
    clear_ui()
    print(f"!!! {message} !!!")
    input("Enter drücken zum weiter machen.")
    clear_ui()

def render_success_message(message: str):
    """Rendert im Terminal eine Erfolgsmeldung. Meldung kann über die Stringübergabe bestimmt werden."""
    clear_ui()
    print(f">>> {message} <<<")
    input("Enter drücken zum weiter machen.")
    clear_ui()

def render_information_message(message: str):
    """Rendert im Terminal eine Informationsmeldung. Meldung kann über die Stringübergabe bestimmt werden."""
    clear_ui()
    print(f"[ {message} ]")
    input("Enter drücken zum weiter machen.")
    clear_ui()

def clear_ui():
    """Entfernt den Inhalt im Terminal"""
    for i in range (100):
        print("")

    
