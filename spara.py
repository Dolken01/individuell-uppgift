import json
from meny_val import Meny as m

def spara_fil(self, filnamn = "uppgifter.json"):
    with open(filnamn, "w", encoding="utf-8") as fil