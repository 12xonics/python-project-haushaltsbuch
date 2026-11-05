def input_int(message: str) -> int:
    """Nimmt eine Zahl als Userinput entgegen."""
    string = input(message).strip()
    try:
       zahl = int(string)
       return zahl
    except:
        return None 
