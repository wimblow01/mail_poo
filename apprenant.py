class Apprenant:
    
    def __init__ (self, x):
        setattr(self, "id", x[0])
        setattr(self, "nom", x[1])
        setattr(self, "prenom", x[2])
        setattr(self, "mail", x[3])
    