import json


class Filhantering:

    def __init__(self, filnamn="uppgifter.json") -> None:
        self.filnamn: str = filnamn
        

    def spara_fil(self, lista) -> None:
        """ Sparar JSON filen"""
        with open(self.filnamn, "w") as fil: # Öppnar i skrivläge
            json.dump(lista, fil, ensure_ascii=False)


    def ladda_fil(self, filnamn = "uppgifter.json") -> list:
        """ Öppnar JSON filen och returnerar som en lista, 
        om filen inte skulle finnas så returnerar den en tom lista."""
        try:
            with open(filnamn, "r") as fil: # Öppnar i läsläge
                return json.load(fil)
        except FileNotFoundError: # Om filen inte finns så skapas en tom lista
            return []
        