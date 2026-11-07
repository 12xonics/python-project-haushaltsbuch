def input_betrag(message: str) -> float:
    """Nimmt einen Float als Userinput entgegen und checkt ob dieser die Kriterien für einen Betrag erfüllt. Gibt None zurück wenn dem nicht so ist."""
    eingabe = input(message)
    try:
        converted_eingabe = float(eingabe)
        if converted_eingabe > 0:
            return converted_eingabe
        raise Exception("Betrag kleiner oder gleich 0.")
    except:
        return None