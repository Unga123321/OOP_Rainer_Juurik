class Seade:
    
    km = 20
    
    def _init_(self, tooteKood, nimetus, hind_kmta):
        self.tooteKood = tooteKood
        self.nimetus = nimetus
        self.hind_kmta = hind_kmta
        self.hind_kmga = None
    
    def kmHind(self):
        self.kmHind = self.hind_kmta * (1 + self.km / 100)
        print("Toote hind on", self.kmHind)
    
    def tekstiks(self):
        print("Toode mille tootekood on", self.tooteKood, "Mille nimetus on", self.nimetus, "mille hind käibemaksuta on", self.hind_kmta, "mille hind käibemaksuga on", self.hind_kmga)
    
    def get_nimetus(self):
        print(self.nimetus)

    def get_tootekood(self):
        print(self.tooteKood)
    
    def get_hind_kmga(self):
        print(self.hind_kmga)
    
    def set_tooteKood(self):
        self.tooteKood = kood
    def set_nimetus(self):
        self.nimetus = nimi
    def set_hind_kmga(self):
        set_hind_kmga = hind_kmga
        
seadeYks = Seade()
seadeYks = Seade(17243, "Krõbe Pelmeen", 2.99)
seadeYks.set.kmHind(60)



seadeKaks = Seade(19274, "Makita akutrell", 55.99)
seadeKaks.tekstiks()



    
    