from abc import ABC, abstractmethod
from operator import le

class Habitant:

    def __init__(self, nom, prénom, age, adresse):
        """Initialise un habitant avec un nom, un âge, une adresse et une liste d'animaux."""
        self.nom = nom
        self.prénom = prénom
        self.age = age
        self.adresse = adresse
        
    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        """Méthode abstraite pour calculer le nombre d'années avant la retraite."""
        pass

    def __str__(self):
        """Renvoie une chaine de caractères représentant l'habitant."""
        return f"{self.prénom} {self.nom}, {self.age} ans, habite à {self.adresse}"
    

class Adulte(Habitant):

    def __init__(self, nom, prénom, age, adresse):
        """Initialise un adulte avec un nom, un âge, une adresse et une liste d'animaux."""
        if age < 18:
            raise ValueError("Age inférieur à 18 ans.")
        
        super().__init__(nom, prénom, age, adresse)

    def calcul_nombre_annee_avant_retraite(self):
        """Calcul le nombre d'années avant la retraite pour un adulte."""
        if self.age < 62:
            return 62 - self.age
        else:
            return "Deja a la retraite"

class Enfant(Habitant):
    def __init__(self, nom, prénom, age, adresse, animaux=None):
        """Initialise un enfant avec un nom, un âge, une adresse et une liste d'animaux."""
        if age >= 18:
            raise ValueError("Age supérieur ou égal à 18 ans")

        super().__init__(nom, prénom, age, adresse)

    def calcul_nombre_annee_avant_retraite(self):
        """Calcul le nombre d'années avant la retraite pour un enfant."""
        return "Erreur: un enfant ne peut pas calculer sa retraite"


def affichage(h: Habitant):
    """Affiche les informations d'un habitant."""
    return str(h)

#Instance de la classe Adulte et Enfant pour les tests
adulte = Adulte("Dupont", "Marie", 35, "Rue A")
enfant = Enfant("Martin", "Lucas", 12, "Rue B")

# Test des méthodes de la classe Adulte et Enfant
assert affichage(adulte) == "Marie Dupont, 35 ans, habite à Rue A"
assert affichage(enfant) == "Lucas Martin, 12 ans, habite à Rue B"
assert adulte.calcul_nombre_annee_avant_retraite() == 27
assert "enfant" in enfant.calcul_nombre_annee_avant_retraite()
try:
    Enfant("Oups", "Marie", 25, "Rue C")
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass

#Question 3 :
#le fait de rendre calcul_nombre_annee_avant_retraite abstraite
#dans Habitant garantit que toutes les sous-classes doivent
#implémenter cette méthode, assurant ainsi que l'appel à cette
#méthode via le polymorphisme dans affichage sera toujours valide
#et fonctionnera correctement pour tous les types d'habitants.