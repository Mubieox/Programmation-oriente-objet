class Complexe:
    
    def __init__(self,re,im):
        self.re, self.im = re, im
        
    def module(self):
        pass
    
    def argument(self):
        pass
    
    def __add__ (self, other): 
        return Complexe(self.re + other.re, self.im + other.im)
    
    def afficher(self): 
        print(str(self.re)+ " + i " + str(self.im))
        
"""comp=Complexe(1,8)
comp2=Complexe(5,9)
comp3=comp+comp2
comp3.afficher()"""

#ACT1
#1°
class Rectangle:
    
    def __init__(self,longueur,largeur):
        self.longueur, self.largeur = longueur, largeur
    
    def perimetre(self):
        return(2*self.longueur+2*self.largeur)
    
    def surface(self):
        return(self.longueur*self.largeur)
    
    def __str__(self):
        return f"Rectangle ({self.longueur} cm x {self.largeur} cm) : Surface de {self.surface()} cm2 ; Périmètre de {self.perimetre()} cm"
    

"""rectangle1=Rectangle(10,5)
print(rectangle1)"""

#2°
class CompteBancaire:
    
    def __init__(self,numero,prenom,nom,solde):
        self.numero, self.prenom, self.nom, self.solde = numero, prenom, nom, solde
    
    def __str__(self):
        return f"N° compte : {self.numero}  | Prénom : {self.prenom}    | Nom : {self.nom}    | Solde : {self.solde}"
    
    def versement(self,argent):
        self.solde+=argent
        
    def retrait(self,argent):
        self.solde-=argent
    
    def transferer(self,argent,compte):
        self.solde-=argent
        compte.solde+=argent
    
    def afficher(self):
        print(f"Prénom : {self.prenom}    | Nom : {self.nom}    | Solde : {self.solde}")
    

"""compte1=CompteBancaire(7777777,"John","DOE",10000)
print(compte1)
compte2=CompteBancaire(88888888,"Patrick","DOE",156000)
compte1.transferer(50,compte2)
compte1.afficher()
compte2.afficher()"""

#ACT2

class Player:
    
    def __init__(self,pseudo,health,attack):
        self.pseudo, self.health, self.attack = pseudo, health, attack
        self.weapon=None
    
    def get_pseudo(self):
        print(self.pseudo)
    
    def get_health(self):
        print(self.health)
        
    def get_attack(self):
        print(self.attack)
    
    def damage(self,joueur):
        degat=joueur.attack
        if joueur.weapon!=None:
            self.health-=degat+joueur.weapon.damage
        else:
            self.health-=degat
    
    def attack_player(self,joueur):
        print(f"{self.pseudo} attaque {joueur.pseudo}")
        joueur.damage(self)
            
    def set_weapon(self,weapon):
        self.weapon = weapon
    
    def has_weapon(self):
        if self.weapon==None:
            print(f"{self.pseudo} n'as pas d'arme")
        else:
            print(f"{self.pseudo} as {self.weapon}")
    
    def __str__(self):
        return f"Player : {self.pseudo}  | Points de vie : {self.health} | Points d'attaque : {self.attack}"



class Weapon:
     
    def __init__(self,name,damage):
        self.name, self.damage = name, damage
    
    def get_name(self):
        print(self.name)
    
    def get_damage_amount(self):
        print(self.damage)
    
    def __str__(self):
        return f"Arme : {self.name}   | Dégats infligés : {self.damage}"
    


class Warrior(Player):
    
    def __init__(self, pseudo, health, attack, armor):
        super().__init__(pseudo, health, attack)
        self.armor = armor
    
    def blade(self,armor):
        self.armor = armor
    
    def damage(self,joueur):
        if self.armor==0:
            degat=joueur.attack
            if joueur.weapon!=None:
                self.health-=degat+joueur.weapon.damage
            else:
                self.health-=degat
        else:
            self.armor-=1
    
    def __str__(self):
        return Player.__str__(self)+f"  | Armure : {self.armor}"



"""player1=Player("Obi-Wan",30,5)
player2=Player("Anakin",40,10)
print(player1)
print(player2)
weapon1=Weapon("Sabre Jedi",10)
weapon2=Weapon("Sabre Sith",15)
player1.set_weapon(weapon1)
player2.set_weapon(weapon2)
player2.attack_player(player1)
print(player1)
print(player2)
player1.attack_player(player2)
print(player1)
print(player2)"""

warrior1=Warrior("Stormtrooper",10,1,5)
print(warrior1)
player3=Player("Han Solo",15,5)
print(player3)
player3.attack_player(warrior1)
print(warrior1)
player3.attack_player(warrior1)
print(warrior1)
player3.attack_player(warrior1)
print(warrior1)
player3.attack_player(warrior1)
print(warrior1)
player3.attack_player(warrior1)
print(warrior1)
player3.attack_player(warrior1)
print(warrior1)
warrior1.blade(5)
print(warrior1)
