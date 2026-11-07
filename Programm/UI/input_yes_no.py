def input_yes_no(message: str) -> str:
    eingabe: str = input(f"{message} (J/N)")
    if eingabe.strip().upper() == "J" or eingabe.strip().upper() == "N":
        return eingabe.strip().upper()
    return None