class CompteBancaire:
    nom = 'Dupont'
    solde = 1000
    def __init__(self,nom,solde):
        self.nom = nom
        self.solde = solde
    
    def depot(self,somme):
        self.solde += somme
    
    def retrait(self,somme):
        self.solde -= somme

    def affiche(self):
        print(self.solde)


compte1 = CompteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()