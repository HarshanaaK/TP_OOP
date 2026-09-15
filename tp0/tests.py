import unittest
from tuples import afficher_releve,recalibrer
from ensembles import robots_double_mission, ajouter_robots_mission

class TestJournalDeBord(unittest.TestCase):
    """Tests pour les fonctions sur les relevés (tuples)."""
    def test_recalibrer_capteur_existant(self):
        releve_test = [("laser_avant", 2.35, "m"), ("laser_arriere", 1.10, "m"), ("gyroscope", 87.5, "deg")]
        resultat = recalibrer(releve_test, "laser_avant", 2.40)
        self.assertEqual(resultat[0],("laser_avant", 2.40, "m"))
        self.assertEqual(resultat[1],("laser_arriere", 1.10, "m"))
        self.assertEqual(resultat[2],("gyroscope", 87.5, "deg"))
  
    """Cas limite : le capteur demande n’existe pas."""  
    def test_recalibrer_capteur_absent(self):

        releve_test = [("laser_avant", 2.35, "m"), ("laser_arriere", 1.10, "m"), ("gyroscope", 87.5, "deg")]
        resultat = recalibrer(releve_test, "capteur_absent", 2.40)
        self.assertEqual(resultat[0],("laser_avant", 2.35, "m"))
        self.assertEqual(resultat[1],("laser_arriere", 1.10, "m"))
        self.assertEqual(resultat[2],("gyroscope", 87.5, "deg"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
