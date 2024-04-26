class Kalkulaator:
    
    pi = 3.14
    
    def _init_(self, arv1, arv2, raadius):
        self.arv1 = arv1
        self.arv2 = arv2
        self.raadius = raadius

    def summa(self):
        self.summa = self.arv1 + self.arv2
        print("Nende kahe arvu summa on",self.summa)
    
    def vahe(self):
        self.vahe = self.arv1 - self.arv2
        print("Nende kahe arvu vahe on",self.vahe)
        
    def korrutis(self):
        self.korrutis = self.arv1 * self.arv2
        print("Nende kahe arvu korrutis on",self.korrutis)
    
    def jagatis(self):
        self.jagatis = self.arv1 / self.arv2
        print("Nende kahe arvu jagatis on",self.jagatis)
    
    def ring(self):
        self.ring = self.pi * (self.raadius*2)
        print("Ringi ümbermõõt on",self.ring)
        
    def tulemus(self):
        print("Nende kahe arvu summa on",self.summa, "Nende kahe arvu vahe on",self.vahe, "Nende kahe arvu korrutis on", self.korrutis, "Nende kahe arvu jagatis on", self.jagatis, "Ringi ümbermõõt on", self.ring)
     
arvYks = Kalkulaator()
arvYks.arv1 = 6
arvYks.arv2 = 3
arvYks.raadius = 4

arvYks.tulemus()

