from habitant_protege import Habitant

class Village:

    def __init__(self, nom):
        """Initialise le nom du village et une liste vide habitants"""
        self.nom = nom
        self.habitants = []

    def ajouter_habitant_composition(self,nom,age,adresse, animaux=None):
        """Ajoute un habitant au village en utilisant la composition"""
        habitant = Habitant(nom, age, adresse, animaux)
        self.habitants.append(habitant)

    def ajouter_habitant_agregation(self, habitant):
        """Ajoute un habitant au village en utilisant l'agrégation"""
        self.habitants.append(habitant)

    def get_habitants(self):
        """Retourne la liste des habitants du village"""
        return self.habitants

    def afficher_habitants(self):
        """Affiche chaque habitant du village"""
        for habitant in self.habitants:
            print(f"{habitant.get_nom} : {habitant.get_age}, {habitant.get_adresse}, {habitant.get_animaux}")

#instance de la classe Village
pytown = Village("PyTown")
autre_village = Village("VillageVoisin")

#instanciation d'un habitant
elise = Habitant("Elise", 28, "Rue B", {"poules": 10})

# Test des méthodes de la classe Village
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
pytown.ajouter_habitant_agregation(elise)
autre_village.ajouter_habitant_agregation(elise) # meme habitant dans 2 villages

# Test des méthodes de la classe Village
assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()


"""Question 3: ajouter_habitant_composition est dépendant de la classe habitant
car elle crére une instance habitant à l'intérieur de la méthode,
tandis que la méthode ajouter_habitant_agregation ne dépend pas de la classe habitant
car elle prend un objet habitant en paramétre ainsi si on supprime la classe habitant la méthode peut toujours exister
et  fonctionner avec d'autre classes."""