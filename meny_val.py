from datetime import datetime #importerar datetime för att kunna få ut vilken dag användaren lägger in saker i listan
class Meny:

    

    def __init__(self, uppgifter: list):
        self.uppgifter = uppgifter

    def lägg_till_uppgifter(self):#Ber användaren att skriva vad han vill lägga in i listan och lägger till i listan
        while True: #Ber användaren att skriva vad han vill lägga in i listan och lägger till i listan

            datum = datetime.now().strftime("%Y/%m/%d") #datetime.now returnerar datum och tid. strftime returnerar en string för datum %Y = 0000 %m = 00 %d= 00

            uppgift_text = input("Skriv uppgiften du vill lägga till: ")

            uppgift = {"text": uppgift_text, "datum": datum}

            self.uppgifter.append(uppgift)

            print(f"{uppgift_text} tillagd! (Datum: {datum})")
            
            while True:
                print("Vill du lägga till flera saker i listan? y=ja n=nej")
                val = input(">").lower() #Använder lower om det skulle vara så att användaren skriver Y/N istället för y/n
                if val == "y":#Om användaren väljer "y" hoppar den ut ur loopen och ber användaren att skriva in en till uppgift
                    break
                elif val == "n": #Om användaren väljer "n" så går den tillbaka till menyn
                    print("Går tillbaka till menyn")
                    return
                elif val != "y" and val != "n":
                    print("Du måste svara ja eller nej. y/n")


    def visa_lista(self): #Skriver ut vad som finns i listan
        print("Att göra: ")
        for uppgift in self.uppgifter:
            print(f' {uppgift["text"]} ("tillagd: {uppgift["datum"]})')


    def ta_bort_uppgifter(self):#Skriver först ut allt som finns i listan och frågar sedan användaren vad i listan han vill ta bort
        self.visa_lista()
        print("Vad vill du ta bort i listan")
        uppgift = input(">")
        for uppgift in self.uppgifter:
            if uppgift["text"] == uppgift:
                self.uppgifter.remove(uppgift)
                print(f"{uppgift} borttagen ur listan")
        else:
            print("Det du skrev finns inte med i listan")


        
