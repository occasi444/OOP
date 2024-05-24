class Tier:
    
    def __init__(self, rasse, geschlecht, alter):
        self.rasse = rasse
        self.geschlecht = geschlecht
        self.alter = alter

    def printAlter(self):

        # self.alter wird umgewandelt und dan mit Punkt verkettet
        print("Der " +self.rasse+ " ist", str(self.alter) + ".")
