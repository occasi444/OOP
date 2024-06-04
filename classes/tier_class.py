class Tier:
    
    def __init__(self, rasse, geschlecht, alter):
        self.rasse = rasse
        self.geschlecht = geschlecht
        self.alter = alter

    def printAlter(self):

        # self.alter wird umgewandelt und dan mit Punkt verkettet
        print("Der " +self.rasse+ " ist", str(self.alter) + ".")

class Hund(Tier):

    def __init__ (self, rasse, geschlecht, alter, farbe):
        
        super().__init__ (rasse, geschlecht, alter)

        self.farbe = farbe

Bello = Hund("labrador", "mänlich", 12, "braun")

print (Bello.farbe)   
