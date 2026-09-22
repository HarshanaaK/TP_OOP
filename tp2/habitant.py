class Habitant:

    def __init__(self, nom, age, adresse, animaux=None):
        """Initialise un habitant avec un nom, un âge, une adresse et une liste d'animaux."""
        self.nom = nom
        self.age = age
        self.adresse = adresse
        self.animaux = animaux if animaux is not None else []

    def affichage_adresse(self):
        """Affiche l'adresse de l'habitant."""
        print(f"{self.nom} habite à {self.adresse}")

    def compte_animal(self, animal):
        """Retourne le nombre d'animaux de type 'animal' que possède l'habitant."""
        return self.animaux.get(animal, 0)

# instance de la classe Habitant
h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})

# Test des méthodes de la classe Habitant
assert h1.nom == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0

h1.affichage_adresse() # affiche "Aldric habite a Rue A"