import numpy as np


class DeuxVecteurs:
    premier_vecteur: np.ndarray[any, np.float64]
    deuxieme_vecteur: np.ndarray[any, np.float64]

    def __init__(self, premier_vecteur: np.ndarray[any, np.float64], deuxieme_vecteur: np.ndarray[any, np.float64]):
        self.premier_vecteur = premier_vecteur
        self.deuxieme_vecteur = deuxieme_vecteur

    def ProduitScalaire(self, premier_vecteur=None, deuxieme_vecteur=None):
        # Vérifiez les dimensions des deux vecteurs.
        somme = 0
        if premier_vecteur is not None and deuxieme_vecteur is not None:
            if premier_vecteur.ndim == deuxieme_vecteur.ndim:
                for premiere_composante, deuxieme_composante in np.nditer([premier_vecteur, deuxieme_vecteur]):
                    somme += premiere_composante * deuxieme_composante
            return somme
        else:
            if self.premier_vecteur.ndim == self.deuxieme_vecteur.ndim:
                for premiere_composante, deuxieme_composante in np.nditer([self.premier_vecteur, self.deuxieme_vecteur]):
                    somme += premiere_composante * deuxieme_composante
            return somme

    def NormeEuclidienne(self, vecteur):
        resultat = self.ProduitScalaire(vecteur, vecteur)
        return np.sqrt(resultat)

    def SimilariteCosinus(self):
        resultat = self.ProduitScalaire() / (self.NormeEuclidienne(self.premier_vecteur) * self.NormeEuclidienne(self.deuxieme_vecteur))
        return resultat

    def AfficherResultats(self):
        print(f"Le produit scalaire est {self.ProduitScalaire()}")
        print(f"La norme euclidienne du premier vecteur est {self.NormeEuclidienne(self.premier_vecteur)}")
        print(f"La norme euclidienne du deuxième vecteur est {self.NormeEuclidienne(self.deuxieme_vecteur)}")
        print(f"La similarité cosinus des deux vecteurs est {self.SimilariteCosinus()}")


if __name__ == '__main__':
    les_deux_vecteurs = DeuxVecteurs(np.array([3.0, 4.0], dtype=np.float64), np.array([4.0, -3.0], dtype=np.float64))
    les_deux_vecteurs.AfficherResultats()
