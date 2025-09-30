#Todo app
from meny_val import Meny as m #Importerar funktioner för menyn
from spara import Filhantering #Importerar filhantering



def meny(): 
    """Funktion som skriver ut och hanterar vad användaren väljer"""
    
    fil = Filhantering()
    uppgifter: list = fil.ladda_fil()
    lista: list = m(uppgifter)

    print("Välkommen till din Todolista")
    while True: #Loopar igenom menyn tills användaren väljer att avsluta programmet
        print("-----Meny-----")
        print(" 1. Lägg till i listan\n 2. Ta bort från listan\n 3. Visa listan\n 4. Spara listan\n 5. Avsluta programmet")
        val: str = input(">")

    
        if val == "1":
            lista.lägg_till_uppgifter()
        elif val == "2":
            lista.ta_bort_uppgifter()
            fil.spara_fil(lista.uppgifter) # Sparar listan efter att användaren har tagit bort något i den
        elif val == "3":
            lista.visa_lista()
        elif val == "4":
            fil.spara_fil(lista.uppgifter)
            print("Listan sparad!")
        elif val == "5":
            print("Programmet avslutas")
            exit()
        else:
            print("Du måste välja mellan valen på menyn")
            exit()


if __name__ == "__main__":
    meny()
