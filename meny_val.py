
class Meny:

    uppgifter = []

    def __init__(self, uppgifter: list):
        self.uppgifter = uppgifter

    def lägg_till_uppgifter(self): #Ber användaren att skriva vad han vill lägga in i listan och lägger till i listan
        uppgift = input("Skriv uppgiften du vill lägga till: ")
        self.uppgifter.append(uppgift)
        print(f"{uppgift} tillagd!")
        while True:
            print("Vill du lägga till flera saker i listan? y=ja n=nej")
            val = input(">")
            if val == "y":
                self.lägg_till_uppgifter()
            elif val == "n":
                print("Går tillbaka till menyn")
                break
            elif val != "y" or val != "n":
                print("Du måste svara ja eller nej. y/n")
            break


    def visa_lista(self, uppgifter): #Skriver ut vad som finns i listan
        print("Att göra: ")
        for uppgift in self.uppgifter:
            print(f" {uppgift}")


    def ta_bort_uppgifter(self):#Skriver först ut allt som finns i listan och frågar sedan användaren vad i listan han vill ta bort
        self.visa_lista()
        print("Vad vill du ta bort i listan")
        uppgift = input(">")
        self.uppgifter.remove(uppgift)
        print(f"{uppgift} borttagen ur listan")


        
