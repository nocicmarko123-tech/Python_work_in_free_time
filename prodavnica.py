import math
        """DOBRODOŠLI U ONLINE LIDL"""
class Prodavnica:
    """ Počettni uvod u digitalnu prodavnicu"""
    def __init__(self, kupac, cene, ):
        self.kupac = kupac
        self.cene = cene

    def pitanje_kupca(self):
        if self.kupac == "enter":
            print("DOBRODOŠAO U LIDL- ONLINE PRODAVNICU")
