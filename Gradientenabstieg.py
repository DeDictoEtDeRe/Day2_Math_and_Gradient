# -*- coding: utf-8 -*-
import numpy as np
from typing import final
import pandas as pd
import matplotlib.pyplot as plt
def plot_loss(loss_array: np.ndarray):
    """Plots a 1D NumPy array of np.float64 loss values instantly."""
    plt.plot(loss_array)
    plt.title('Loss vs. Iteration')
    plt.xlabel('Iteration')
    plt.ylabel('Loss')
    plt.grid(True)
    plt.show()
class Gradientenabstieg:
    DieUnabhangigeVariable: np.ndarray[any,np.dtype[np.float64]]
    DieAbhangigeVariable: np.ndarray[any,np.dtype[np.float64]]
    DieLernraten: np.float64
    def __init__(self,DieUnabhangigeVariable: np.ndarray[any,np.dtype[np.float64]]|None=None,DieAbhangigeVariable: np.ndarray[any,np.dtype[np.float64]]|None=None,DieLernraten:np.float64|None=None):
        self.DieUnabhangigeVariable=DieUnabhangigeVariable
        self.DieAbhangigeVariable=DieAbhangigeVariable
        self.DieLernraten=DieLernraten
    def SummeDerUnabhangigenVariable(self):
        if self.DieUnabhangigeVariable.ndim == 1:
            return np.sum(self.DieAbhangigeVariable)
        else:
            raise ValueError("Die Abmessung des Pfeils ist nicht erwunscht.")
    def SummeDerAbhangigenVariable(self):
        if self.DieAbhangigeVariable.ndim == 1:
            return np.sum(self.DieAbhangigeVariable)
        else:
            raise ValueError("Die Abmessung des Pfeils ist nicht erwunscht.")
    def SummeDesQuadratsDerUnabhangigenVariable(self):
        if self.DieUnabhangigeVariable.ndim == 1:
            return self.DieUnabhangigeVariable @ self.DieUnabhangigeVariable
        else:
            raise ValueError("Die Abmessung des Pfeils ist nicht erwunscht.")
    def SummeDerProdukteAusUnabhangigerUndAbhangigerVariablen(self):
        if self.DieUnabhangigeVariable.ndim == 1 and self.DieAbhangigeVariable.ndim == 1:
            return self.DieUnabhangigeVariable @ self.DieAbhangigeVariable
        else:
            raise ValueError("Die Abmessung des Pfeils ist nicht erwunscht.")
    def BerechnenSieDenVerlust(self,DerVektorAusSteigungUndAchsenabschnitt):
        Zeitweilige=self.DieAbhangigeVariable-(DerVektorAusSteigungUndAchsenabschnitt[0]*self.DieUnabhangigeVariable+DerVektorAusSteigungUndAchsenabschnitt[1]*np.ones(self.DieAbhangigeVariable.size))
        Zeitweilige=Zeitweilige**2
        return Zeitweilige
    def Ausfuhren(self,DasAbbruchkriterium):
        DerVektorAusSteigungUndAchsenabschnitt=np.array([0,0]).T
        MaximaleAnzahlDerIterationen: final=100
        DieAnzahlDerElementeImDatenVektor=self.DieUnabhangigeVariable.size
        #Verlustfuktion
        DerQuadratischeFehler=np.zeros(MaximaleAnzahlDerIterationen)
        for Iterator in range(MaximaleAnzahlDerIterationen):
            self.TrainingsschrittAusfuhren(DerVektorAusSteigungUndAchsenabschnitt, DieAnzahlDerElementeImDatenVektor)
            vorubergehend=self.BerechnenSieDenVerlust(DerVektorAusSteigungUndAchsenabschnitt)
            DerQuadratischeFehler[Iterator]=vorubergehend
            if Iterator !=0 :
                if np.abs(DerQuadratischeFehler[Iterator]-DerQuadratischeFehler[Iterator]) <= DasAbbruchkriterium:
                    break
        return DerQuadratischeFehler        
    def TrainingsschrittAusfuhren(self,DerVektorAusSteigungUndAchsenabschnitt:np.ndarray[any,np.dtype[np.float64]],DieAnzahlDerElementeImDatenVektor):
        DerGradientDesQuadratischenFehler=np.array([[2*self.SummeDesQuadratsDerUnabhangigenVariable(),2*self.SummeDerUnabhangigenVariable()],[2*self.SummeDerUnabhangigenVariable(), 2*DieAnzahlDerElementeImDatenVektor]])@DerVektorAusSteigungUndAchsenabschnitt\
        -np.array([2*self.SummeDerProdukteAusUnabhangigerUndAbhangigerVariablen(),2*self.SummeDerAbhangigenVariable()]).T
        DerVektorAusSteigungUndAchsenabschnitt=DerVektorAusSteigungUndAchsenabschnitt-self.DieLernraten*DerGradientDesQuadratischenFehler     
    def UberfuhrenSieDieSpalteInDieUnabhangigeVariableUndDieStorvariable(self,Dateiname):
        DateiDeskriptor=pd.read_csv(Dateiname)
        self.DieUnabhangigeVariable=DateiDeskriptor['x'].to_numpy(dtype=np.float64)
        self.DieAbhangigeVariable=DateiDeskriptor['y'].to_numpy(dtype=np.float64)
    def EineBeliebigeVariableAndern(self,DerNameDerVariable,NeuerWert):
        setattr(self,DerNameDerVariable,NeuerWert)
    def Hauptsachlich(self):
        self.UberfuhrenSieDieSpalteInDieUnabhangigeVariableUndDieStorvariable("linear_data.csv")
        DerQuadratischeFehler=self.Ausfuhren(np.power(10,-3))
        self.EineBeliebigeVariableAndern("DieLernraten", np.float64(0.05))
        plot_loss(DerQuadratischeFehler)
        self.EineBeliebigeVariableAndern("DieLernraten", np.float64(5.00))
        plot_loss(DerQuadratischeFehler)
        return None    
        
if __name__ == "__main__":
    DerGradientenabstieg=Gradientenabstieg()
    DerGradientenabstieg.Hauptsachlich()

        

