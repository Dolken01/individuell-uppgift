#Todo app
from meny_val import Meny as m #Importerar funktioner för menyn
from spara import Filhantering #Importerar filhantering
blå = "\033[94m" #ANSI-kod för att göra text blå
grön = "\033[92m" #ANSI-kod för att göra text grön
röd = "\033[91m" #ANSI-kod för att göra text röd
gul = "\033[33m"

reset = "\033[0m" #ANSI-kod för att texten ska gå tillbaka till vit igen

def meny(): 
    """Funktion som skriver ut och hanterar vad användaren väljer"""
    
    fil = Filhantering()
    uppgifter: list = fil.ladda_fil()
    lista: list = m(uppgifter)

    print(f"{gul}Välkommen till din Todolista{reset}")
    while True: #Loopar igenom menyn tills användaren väljer att avsluta programmet
        print(f"{blå}|{reset}{blå}▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔{reset}{blå}|{reset}")
        print(f"{blå}|{reset}           {gul}Meny{reset}           {blå}|{reset}")
        print(f"{blå}|{reset}                          {blå}|{reset}")
        print(f"{blå}|{reset} {gul}1. Lägg till i listan{reset}    {blå}|{reset}\n{blå}|{reset} {gul}2. Ta bort från listan{reset}   {blå}|{reset}\n{blå}|{reset} {gul}3. Visa listan{reset}           {blå}|{reset}\n{blå}|{reset} {gul}4. Spara listan{reset}          {blå}|{reset}\n{blå}|{reset} {gul}5. Avsluta programmet{reset}    {blå}|{reset}")
        print(f"{blå}▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔{reset}")
        val: str = input(f"{grön}>{reset}")
        

    
        if val == "1":
            lista.lägg_till_uppgifter()
        elif val == "2":
            lista.ta_bort_uppgifter()
            fil.spara_fil(lista.uppgifter) # Sparar listan efter att användaren har tagit bort något i den
        elif val == "3":
            lista.visa_lista()
        elif val == "4":
            fil.spara_fil(lista.uppgifter)
            print(f"{grön}Listan sparad!{reset}")
        elif val == "5":
            print(f"{röd}Programmet avslutas{reset}")
            exit()
        else:
            print(f"{röd}Du måste välja mellan valen på menyn{reset}")
            exit()
        


if __name__ == "__main__":
    meny()


