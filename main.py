#Todo app
from meny_val import Meny as m #importerar meny_val där jag har funktioner för menyn



def meny(): #Funktion som skriver ut och hanterar vad användaren väljer
    lista = m([])

    print("Välkommen till din Todolista")
    while True:
        print(" 1. Lägg till i listan\n 2. Ta bort från listan\n 3. Visa listan\n 4. Spara listan\n 5. Avsluta programmet")
        val = input(">")

    
        if val == "1":
            lista.lägg_till_uppgifter()
        elif val == "2":
            lista.ta_bort_uppgifter()
        elif val == "3":
            lista.visa_lista()
        elif val == "4":
            pass
            #sparar litan
        elif val == "5":
            print("Programmet avslutas")
            exit()
        else:
            print("Du måste välja mellan valen på menyn")
            exit()


if __name__ == "__main__":
    meny()
