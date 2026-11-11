import json

with open("haushaltsbuch.json", "r") as file:
    json_anzeigen = json.load(file) #wird als dict geladen
    print(json_anzeigen) 
    