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

class Employer(Personne):
    def __init__(self,Personne, salaire):
        self.salaire = salaire
        self.personne = Personne
    
    def afficher(self):
        self.personne.afficher()
        print("Salaire: " + str(self.salaire))
        
class Chef(Employer):
    def __init__(self, Employer, Service):
        self.employer = Employer
        self.service = Service
    
    def afficher(self):
        self.employer.afficher()
        print("Service: " + str(self.service))

P = Chef(Employer((Personne("Ilyass","Math",DateNaissance(1,7,1982))),7856),"Ressource humaine")
P.afficher()