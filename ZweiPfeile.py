import numpy as np

class BeidenPfeile:
    DerErstePfeil: np.ndarray[any, np.float64]
    DerZweitePfeile: np.ndarray[any, np.float64]
    def __init__(self, DerErstePfeil: np.ndarray[any, np.float64], DerZweitePfeil: np.ndarray[any, np.float64]):
        self.DerErstePfeil=DerErstePfeil
        self.DerZweitePfeil=DerZweitePfeil
    def SkalarProdukt(self,DerErstePfeil=None,DerZweitePfeil=None):
        #U(Umlaut)berpru(Umlaut)fen Sie the die Abmessungen der beiden Pfeile
        Summe=0
        if DerErstePfeil is not None and DerZweitePfeil is not None:
            if DerErstePfeil.ndim == DerZweitePfeil.ndim:
                for DieErsteKomponente,DieZweiteKomponente in np.nditer([DerErstePfeil,DerZweitePfeil]): 
                    Summe += DieErsteKomponente*DieZweiteKomponente
            return Summe
        else:
            if self.DerErstePfeil.ndim == self.DerZweitePfeil.ndim:
                for DieErsteKomponente,DieZweiteKomponente in np.nditer([self.DerErstePfeil,self.DerZweitePfeil]): 
                    Summe += DieErsteKomponente*DieZweiteKomponente
            return Summe
    def EuklidischLange(self,DerPfeil):
        DieRuckkehr=self.SkalarProdukt(DerPfeil,DerPfeil)
        return np.sqrt(DieRuckkehr) 
    def Koinus_Ahnlichkeit(self):
        DieRuckkehr=self.SkalarProdukt()/(self.EuklidischLange(self.DerErstePfeil)*self.EuklidischLange(self.DerZweitePfeil))
        return DieRuckkehr
    def IchDruckeDieConsequenzAus(self):
        print(f"Das Skalarprodukt ist {self.SkalarProdukt()}")
        print(f"Die Euklidische Norm Des Ersten Pfeils ist {self.EuklidischLange(self.DerErstePfeil)}")
        print(f"Die Euklidische Norm Des Zweiten Pfeils ist {self.EuklidischLange(self.DerZweitePfeil)}")
        print(f"Die Kosinus-Ahnlichkeit des ersten Pfeils und des zweiten Pfeils is {self.Koinus_Ahnlichkeit()}")
if __name__== '__main__':
    DieBeidenPfeile=BeidenPfeile(np.array([3.0,4.0],dtype=np.float64),np.array([4.0,-3.0],dtype=np.float64))
    DieBeidenPfeile.IchDruckeDieConsequenzAus()

