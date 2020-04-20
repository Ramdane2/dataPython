class Lettre:
    def __init__(self ,adresseDestination ,adresseExpedition, poids , modeExpedition , format):
        self.poids = poids
        self.modeExpedition = modeExpedition
        self.adresseDestination = adresseDestination
        self.adresseExpedition = adresseExpedition
        self.format = format
        self.calculTimbrer()
    
    def calculTimbrer(self):
        prixBase = {}
        prixBase["A3"] = 3.5
        prixBase["A4"] = 2.5

        self.montant = prixBase[self.format] + 1 * (self.poids /1000)


    def ToString(self):
        print("Lettre")
        print("Adresse destination: " + self.adresseDestination)
        print("Adresse expedition: " + self.adresseExpedition)
        print("Poids: " + str(self.poids) + "grammes")
        print("Mode: " + self.modeExpedition)
        print("Format: " + self.format)
        print("Prix du timbre : " + str(self.montant))
        

class Colis:
    def __init__(self, adresseDestination, adresseExpedition, poids, modeExpedition, volume):
        self.poids = poids
        self.modeExpedition = modeExpedition
        self.adresseDestination = adresseDestination
        self.adresseExpedition = adresseExpedition
        self.volume = volume
        self.calculTimbrer()

    def calculTimbrer(self):
        self.montant = 0.25 * self.volume + (self.poids / 1000)

    def ToString(self):
        print("Colis")
        print("Adresse destination: " + self.adresseDestination)
        print("Adresse expedition: " + self.adresseExpedition)
        print("Poids: " + str(self.poids) + " grammmes")
        print("Mode: " + self.modeExpedition)
        print("Volume: " + str(self.volume) + " litres")
        print("Prix du timbre : " + str(self.montant))




L1=Colis("Marrakeche","Barcelone",3500,"expresse",2.25)
L1.ToString()

