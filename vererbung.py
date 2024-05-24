class Tier:
    
    def __init__(self, rasse, geschlecht, alter):
        self.rasse = rasse
        self.geschlecht = geschlecht
        self.alter = alter

    def printAlter(self):
        print ("Alter: ", self.alter)

tier_1 = Tier("Husky", "mänlich", 7)

tier_1.printAlter()