class Inimene:

    def __init__(self, nimi, vanus):
        self.nimi = nimi
        self.vanus = vanus
    
    def valjasta_nimi(self):
        print(self.nimi)
        
    def valjasta_Vanus(self):
        print(self.vanus)
        
    def valjasta_vanus(self):
        self.vanane = self.vanus + 1
        print(self.vanane)



class Opilane(Inimene):

    def __init__(self, nimi, vanus, ryhm, keskmineHinne, energia, puhatudAeg):
        super().__init__(nimi)
        super().__init__(vanus)
        self.ryhm = ryhm
        self.keskmineHinne = keskmineHinne
        self.energia = energia
        self.puhatudAeg = puhatudAeg
        

    def valjasta_ryhm(self):
        print(self.ryhm)
    
    def valjasta_keskmineHinne(self):
        print(self.keskmineHinne)
        
    def valjasta_energia(self):
        print(self.energia)
     
    def valjasta_puhatudAeg(self):
        print(self.puhatudAeg)
    
    def opi(self):
        self.keskmineHinne = self.keskmineHinne + 0.1
        if (self.keskmineHinne <= 2):
            self.keskmineHinne = 2
        elif (self.keskmineHinne >= 5):
            self.keskmineHinne = 5
            
        if (self.energia <= 30):
            print("Õppida ei saa, energiat on liiga vähe!")
        else:
            print("Energiat on piisavalt et õppida.")
        
    def puhka(self):
        saadudEnergia = self.puhatudAeg * 10
        self.energia = self.energia + saadudEnergia
        
        
    def valjasta_opilaseInfo(self):
        super().valjasta_nimi()
        super().valjasta_vanus()
        print("Õpilane nimega " + self.nimi + ", kes on " + self.vanus + " aastat vana, kes on osa rühmast " + self.ryhm + ", kelle keskmine hinne on " + self.keskmineHinne + ", energia tase on " + self.energia)
        



class Opetaja(Inimene):
    
    def __init__(self, nimi, vanus, energia, puhatudAeg):
        super().__init__(nimi)
        super().__init__(vanus)
        self.energia = energia
        self.puhatudAeg = puhatudAeg
        
    def opeta(self):
        if (energia <= 20):
            print("Õpetada ei saa, energiat on liiga vähe!")
        else:
            print("Energiat on piisavalt et õpetada.")

    def puhka(self):
        saadudEnergia = puhatudAeg * 15
        self.energia = self.energia + saadudEnergia

    def valjasta_opetajaInfo(self):
        super(valjasta_nimi)
        super(valjasta_vanus)
        print("Õpetaja, kelle nimi on " + self.nimi + ", kelle vanus on " + self.vanus + ", tema energja tase on " + self.energia)
     
opilane = Opilane("Juhan Peterson","17","24B","3.8","42","1")
opilane.valjasta_ryhm()
opilane.valjasta_keskmineHinne()
opilane.valjasta_energia()
opilane.valjasta_puhatudAeg()
opilane.opi()
opilane.puhka()
opilane.valjasta_opilaseInfo()


opetaja = Opetaja("Albert Saar","38","60","2")
opetaja.opeta()
opetaja.puhka()
opetaja.valjasta_opetajaInfo()
