class Tudeng:
    def __init__(self, nimi, tudengiKood, oppeAste, teadusKond):
        self.nimi = nimi
        self.tudengiKood = tudengiKood
        self.oppeAste = oppeAste
        self.teadusKond = teadusKond
    
    def valjasta_nimi(self):
        print(self.nimi)
     
    def valjasta_tudengiKood(self):
        print(self.tudengiKood) 

    def valjasta_oppeAste(self):
        print(self.oppeAste)
        
    def valjasta_teaduskond(self):
        print(self.teaduskond)    

class Teaduskond:
    def __init__(self, nimi, juhataja):
        self.nimi = nimi
        self.juhataja = juhataja
     
    def valjasta_nimi(self):
        print(self.nimi)
        
    def valjasta_juhataja(self):
        print(self.juhataja)
        
 
class BakalaureuseTudeng(Tudeng):
    def __init__(self, nimi, tudengiKood, teadusKond, loputooTeema):
        super().__init__(nimi)
        super().__init__(tudengiKood)
        super().__init__(teadusKond)
        self.loputooTeema = loputooTeema
        
    def valjasta_loputooTeema(self):
        print(self.loputooTeema)
        
    def valjasta_opilane(self):    
        super().valjasta_nimi()
        super().valjasta_tudengiKood()
        super().valjasta_teaduskond()
        print("Õpilane nimega " + self.nimi + " , kelle  tudengikood on " + self.tudengiKood + " , kuulub " + self.teaduskond + " teaduskonda lõputöö teema on " + self.loputooTeema + " .")
   
class MagistriTudeng(Tudeng):
    def __init__(self, nimi, tudengiKood, teaduskond, juhendaja):
        super().__init__(nimi)
        super().__init__(tudengiKood)
        super().__init__(teaduskond)
        self.juhendaja = juhendaja
        
    def valjasta_juhendaja(self):
        print(self.juhendaja)
          
    def valjasta_opilane(self):
        super().valjasta_nimi()
        super().valjasta_tudengiKood()
        super().valjasta_oppeAste()
        super().valjasta_teaduskond()
        print("Õpilane nimega " + self.nimi + " , kellel on " + self.oppeAste + " õppeaste, kuulub " + self.teaduskond + " teaduskonda, tema juhendaja on" + self.juhendaja)

 
esimene_Teaduskond = Teaduskond("Põllumajandus","Juhan Jakobson")

opilane1 = BakalaureuseTudeng("Young-Soo Valary","6256","Põllumajandus","Kartulite ajalugu")
opilane1.valjasta_loputooTeema()
opilane1.valjasta_opilane()

BakalaureuseTudeng2 = BakalaureuseTudeng("Alemayehu Leo","23465","Põllumajandus","Kuidas mõjutab putukate tõrje köögiviljadele")
BakalaureuseTudeng2.valjasta_loputooTeema()
BakalaureuseTudeng2.valjasta_opilane

MagistriTudeng = MagistriTudeng("Colton Mandi","8375","Põllumajandus","H")
MagistriTudeng.valjasta_juhendaja()
MagistriTudeng.valjasta_opilane() 


teine_Teaduskond = Teaduskond("","")

BakalaureuseTudeng2 = BakalaureuseTudeng("Youcef Noyabrina","8885","Põllumajandus","Juhan Jakobson")
BakalaureuseTudeng2.valjasta_loputooTeema()
BakalaureuseTudeng2.valjasta_opilane

BakalaureuseTudeng2 = BakalaureuseTudeng("Kal-El Zelda","77","","")
BakalaureuseTudeng2.valjasta_loputooTeema()
BakalaureuseTudeng2.valjasta_opilane

MagistriTudeng2 = MagistriTudeng("Noak Indira","5676","","")
MagistriTudeng2.valjasta_juhendaja()
MagistriTudeng2.valjasta_opilane() 


kolmas_Teaduskond = Teaduskond("","")
       
BakalaureuseTudeng1 = BakalaureuseTudeng("Jeffry Baker","172","","")
BakalaureuseTudeng1.valjasta_loputooTeema()
BakalaureuseTudeng1.valjasta_opilane()

BakalaureuseTudeng2 = BakalaureuseTudeng("Dagoberto Yalwa","2563","","")
BakalaureuseTudeng2.valjasta_loputooTeema()
BakalaureuseTudeng2.valjasta_opilane

MagistriTudeng1 = MagistriTudeng("Johan Madisson","1221","","")
MagistriTudeng1.valjasta_juhendaja()
MagistriTudeng1.valjasta_opilane()
