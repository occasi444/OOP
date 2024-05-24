class BauplanKatzenKlasse():

    def __init__(self, rufname, farbe, alter):
        self.rufname = rufname
        self.farbe = farbe
        self.alter = alter
    
    def tut_miauen(self):
        print("miau")

Tommy = BauplanKatzenKlasse("Tommy", "mixed", 3)
