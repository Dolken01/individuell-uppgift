import json


class Filhantering:

    def __init__(self, filnamn="uppgifter.json"):
        self.filnamn = filnamn
        

    def spara_fil(self, lista):
        with open(self.filnamn, "w", encoding="utf-8") as fil:
            json.dump(lista, fil, ensure_ascii=False)


    def ladda_fil(self, filnamn = "uppgifter.json"):
        with open(filnamn, "r", encoding="utf-8") as fil:
            return json.load(fil)
        