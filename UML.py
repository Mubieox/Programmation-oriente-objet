class Date:
    def __init__(self,jour,mois,annee):
        self.j,self.m,self.a=jour,mois,annee
        assert (jour<=31  and (mois==1 or mois==3 or mois==5 or mois==7 or mois==8 or mois==10 or mois==12)) or (jour<=30 and (mois==4 or mois==6 or mois==9 or mois==11)) or (mois==2 and ((annee/4==annee//4 and jour<=29) or (annee/4!=annee//4 and jour<=28))), "Veuillez rentrer une date valide."
    def __repr__(self):
        mois=["","janvier","février","mars","avril","mais","juin","juillet","août","septembre","octobre","novembre","decembre"]
        return f"{self.j} {mois[self.m]} {self.a}"
    def __lt__(self,other):
        if self.a<other.a or (self.a==other.a and self.m<other.m) or (self.a==other.a and self.m==other.m and self.j<other.j):
            return True
        else:
            return False

"""date1=Date(11,6,2005)
date2=Date(10,11,2058)
print(date1,date2)
print(date1<date2)"""

class Personne:
    def __init__(self,taille,poids,âge):
        self.t,self.p,self.a=taille,poids,âge
    def imc(self):
        return self.p/self.t**2
    def interpretation(self):
        if self.imc()<=18.5:
            print("Insuffisance pondérale")
        elif self.imc()>=30:
            print("Obésité")

personne1=Personne(1.73,72,17)
personne1.interpretation()
print(personne1.imc())
