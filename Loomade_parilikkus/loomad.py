class loomad:
    def __init__(self, haalitsus):
        self.haalitsus = haalitsus
    
    def valjasta_haalitsus(self):
        print(self.haalitsus)
    
    
class lehm(loomad):
    def __init__(self, haalitsus):
        super().__init__(haalitsus)    
        
    def valjasta_lehmHaalitsus(self):
        super().valjasta_haalitsus()    
        print("Lehm teeb " + self.haalitsus)
    
    
class kass(loomad):
    def __init__(self, haalitsus):
        super().__init__(haalitsus)    
        
    def valjasta_kassHaalitsus(self):
        super().valjasta_haalitsus()
        print("Kass teeb " + self.haalitsus)


class lind(loomad):
    def __init__(self, haalitsus):
        super().__init__(haalitsus)    
        
    def valjasta_lindHaalitsus(self):
        super().valjasta_haalitsus()
        print("Lind teeb " + self.haalitsus)


class part(loomad):   
    def __init__(self, haalitsus):
        super().__init__(haalitsus)    
          
    def valjasta_partHaalitsus(self):
        super().valjasta_haalitsus()
        print("Part teeb " + self.haalitsus)
      
      
lehm = lehm("MMMMMMMUUUU")
lehm.valjasta_lehmHaalitsus()

kass = kass("Miäu")
kass.valjasta_kassHaalitsus()
        
lind = lind("Tsiu")
lind.valjasta_lindHaalitsus()
        
part = part("Prääks")        
part.valjasta_partHaalitsus()    