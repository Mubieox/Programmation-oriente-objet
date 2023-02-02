from random import randint, shuffle

class Boite:
    def __init__(self,longueur,largeur,hauteur):
        assert longueur<=largeur<=hauteur,"Les trois dimensions doivent être : longueur>=largeur>=hauteur"
        self.longueur,self.largeur,self.hauteur=longueur,largeur,hauteur
    
    def volume(self):
        self.volume=self.longueur*self.largeur*self.hauteur
        print(f"Le volume est {self.volume}.")
    
    def rentredans(self,another):
        if self.largeur<another.largeur and self.longueur<another.longueur and self.hauteur<another.hauteur:
            return True
        else:
            return False

"""LB=[]
for i in range(50):
    random1=randint(0,25)
    random2=random1+randint(0,15)
    random3=random2+randint(0,10)
    LB.append(Boite(random1,random2,random3))

Ordre=[]
for i in range(49):
    for j in range(50):
        if LB[j].rentredans(LB[i])==True:
            Ordre.append([j,i])
print(Ordre)
Ordre=sorted(Ordre,key=lambda boite : boite[1],reverse=True)
print(Ordre)"""

class Horloge:
    def __init__(self,heures,minutes,secondes):
        self.heures,self.minutes,self.secondes=heures,minutes,secondes
        self.hr,self.mnr,self.sr=0,0,0
    def ticTac(self):
        self.secondes+=1
        if self.secondes==60:
            self.secondes=0
            self.minutes+=1
            if self.minutes==60:
                self.minutes=0
                self.heures+=1
                if self.heures==24: self.heures=0
        if self.heures==self.hr and self.minutes==self.mnr and self.secondes==self.sr: print("le reveil sonne !")
    def reveil(self,h,mn,s): self.hr,self.mnr,self.sr=h,mn,s
    def __repr__(self): return "Heure actuelle : {}:{}:{}, reveil réglé pour : {}:{}:{}.".format(self.heures,self.minutes,self.secondes,self.hr,self.mnr,self.sr)

"""Heure1=Horloge(15,59,20)
print(repr(Heure1))
Heure1.reveil(17,0,0)
print(repr(Heure1))
for i in range(60**2+40):
    Heure1.ticTac()
    print(repr(Heure1))
print(repr(Heure1))"""

class chien:
    def __init__(self,nom,points_de_santé,aboiement): self.nom,self.santé,self.ab=nom,points_de_santé,aboiement
    def mordre(self,chien): chien.santé-=3
    def manger(self): self.santé+=10
    def grogner(self): return "Grrr... "+self.ab
    def machouiller(self,chaîne):
        chaîne=chaîne.split()
        shuffle(chaîne)
        print(chaîne)
    def __repr__(self): return "{} à {} points de santé et fait {}.".format(self.nom,self.santé,self.ab)

"""Chien1=chien("Médor",15,"Oh Yeah")
Chien2=chien("Jean",20,"Blurgh")
Chien1.mordre(Chien2)
print(Chien1.grogner())
print(Chien2.grogner())
Chien1.machouiller("Hum ta bon goût!")
print(repr(Chien1))
print(repr(Chien2))"""

class Monde:
    def __init__(self,dimension,duree_repousse):
        self.dr=duree_repousse
        self.d=dimension
        carte=[]
        for i in range(self.d):
            carte.append([])
            for j in range(self.d):
                carte[i].append(0)
        self.c=carte
    def HerbePousse(self):
        for i in range(self.d):
            for j in range(self.d):
                self.c[i][j]+=1

monde1=Monde(50,30)
monde1.HerbePousse()
print(monde1.c)