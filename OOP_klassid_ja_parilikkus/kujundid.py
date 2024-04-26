class Kujund:
    def __init__(self, pindala):
        self.pindala = None
        
    def valjasta_pindala(self):
        print(self.pindala)
        
        
class Ring(Kujund):
    def __init__(self, raadius, pindala):
        super().__init__(pindala)
        self.raadius = raadius
        
    def arvutaPindala(self):
        self.pindala = 3.14 * self.raadius**2
        
    def valjasta_pindala(self):
        super().valjasta_pindala()
        print("Ringi pindala on " + str(self.pindala))
        
        
class Ristkylik(Kujund):        
    def __init__(self, pindala, korgus, laius):
        super().__init__(pindala)
        self.korgus = korgus
        self.laius = laius
        
    def arvutaPindala(self):
            self.pindala = self.laius * self.korgus
                
    def valjasta_pindala(self):
        super().valjasta_pindala()
        print("RistKüliku pindala on " + str(self.pindala))



        
ringYks = Ring(2, 1)
ringYks.arvutaPindala()
ringYks.valjasta_pindala()

ringKaks = Ring(5, 1)
ringKaks.arvutaPindala()
ringKaks.valjasta_pindala()


ristkylikYks = Ristkylik(4, 6, 3)
ristkylikYks.arvutaPindala()
ristkylikYks.valjasta_pindala()

ristkylikKaks = Ristkylik(4, 14, 4)
ristkylikKaks.arvutaPindala()
ristkylikKaks.valjasta_pindala()

