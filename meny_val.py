from datetime import datetime #importerar datetime för att kunna få ut vilken dag användaren lägger in saker i listan
from spara import Filhantering

röd = "\033[91m" #ANSI-kod för att göra text röd
grön = "\033[92m" #ANSI-kod för att göra text grön
reset = "\033[0m" #ANSI-kod för att texten ska gå tillbaka till vit igen
class Meny:

    fil = Filhantering()

    def __init__(self, uppgifter: list):
        self.uppgifter: list = uppgifter


    def lägg_till_uppgifter(self) -> None:
        """Ber användaren att skriva vad han vill lägga in i listan och lägger till i listan"""
        while True:  

            datum: str = datetime.now().strftime("%Y/%m/%d") # Datetime.now returnerar datum och tid. strftime returnerar en string för datum %Y = 0000 %m = 00 %d= 00

            uppgift_text: str = input(f"{röd}För att gå tillbaka till menyn skriv 'avbryt'{reset}\nSkriv uppgiften du vill lägga till:").capitalize() # Ber användaren att skriva ner en uppgift till listan
            if uppgift_text == "Avbryt":
                break
            uppgift: dict[str, str] = {"text": uppgift_text, "datum": datum} # Skapar en dictionary med nycklar: text och datum

            self.uppgifter.append(uppgift) # Lägger till uppgiften i listan

            print(f"{grön}{uppgift_text} tillagd! (Datum: {datum}){reset}") # Bekräftar användaren att uppgiften är tillagd
            
            while True:
                print(f"Vill du lägga till flera saker i listan? {grön}y=ja{reset} {röd}n=nej{reset}") # Frågar användaren om han vill lägga till mer i listan
                val = input(f"{grön}>{reset}").lower() #Använder lower om det skulle vara så att användaren skriver Y/N istället för y/n
                if val == "y":#Om användaren väljer "y" hoppar den ut ur loopen och ber användaren att skriva in en till uppgift
                    break
                elif val == "n": #Om användaren väljer "n" så går den tillbaka till menyn
                    print("Går tillbaka till menyn")
                    return
                elif val != "Y" and val != "n": # Felhantering om användaren skulle skriva något annat
                    print("Du måste svara ja eller nej. y/n")
            

    def visa_lista(self) -> None:
        """Skriver ut vad som finns i listan"""
        if not self.uppgifter: # Kollar om listan är tom
            print("Listan är tom. Du har inget att göra idag!\n Går tillbaka till menyn")
            return
        print("Att göra: ") #Skriver ut vad som finns i listan
        for uppgift in self.uppgifter:
            print(f' {uppgift["text"]} (Tillagd: {uppgift["datum"]})')
            


    def ta_bort_uppgifter(self) -> None:
        """Skriver först ut allt som finns i listan och frågar sedan användaren vad i listan han vill ta bort"""
        self.visa_lista() # Visar användaren vad som finns i listan
        print(f"{röd}För att gå tillbaka till menyn skriv 'avbryt'{reset}\nVad vill du ta bort i listan") # Ber avnvändaren att skriva vad han vill ta bort
        ta_bort: str = input(f"{grön}>{reset}").capitalize()
        if ta_bort == "Avbryt":
            return
        for uppgift in self.uppgifter:
            if uppgift["text"] == ta_bort:
                self.uppgifter.remove(uppgift)
                print(f"{röd}{uppgift['text']} borttagen ur listan{reset}")
                break
        else:
            print("Det du skrev finns inte med i listan")


    
