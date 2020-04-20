class DateNaissance:

    def __init__(self , jour , mois , annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee
    
    def ToString(self):
        return str(str(self.jour) + " / " + str(self.mois) + " / " + str(self.annee))
    


class Personne(DateNaissance):
    def __init__(self , nom , prenom , DateNaissance):
        self.nom = nom 
        self.prenom = prenom
        self.dateNaissance = DateNaissance
        
    
    def afficher(self):
        print("Nom: "+str(self.nom))
        print("Prénom: "+str(self.prenom))
        print("Date de naissance: " + self.dateNaissance.ToString())


P = Personne("Ilyass","Math",DateNaissance(1,7,1982))
P.afficher()