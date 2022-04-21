from queue import Empty


class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = 0
        self.edellinen_operaatio = Empty


class Summa: 
    def __init__(self, io, syote):
        self.io = io
        self.syote = syote
    
    def suorita(self):
        self.io.edellinen_operaatio = self
        self.io.edellinen = self.io.tulos
        self.io.tulos = self.io.tulos + int(self.syote())
        
    def kumoa(self):
        self.io.tulos = self.io.edellinen
        
        
class Erotus: 
    def __init__(self, io, syote):
        self.io = io
        self.syote = syote
    
    def suorita(self):
        self.io.edellinen_operaatio = self
        self.io.edellinen = self.io.tulos
        self.io.tulos = self.io.tulos - int(self.syote())
        
    def kumoa(self):
        self.io.tulos = self.io.edellinen
        
class Nollaus:
    def __init__(self, io, syote):
        self.io = io
        self.syote = syote
        
    def suorita(self):
        self.io.edellinen_operaatio = self
        self.io.edellinen = self.io.tulos
        self.io.tulos = 0
        
    def kumoa(self):
        self.io.tulos = self.io.edellinen


class Kumoa:
    def __init__(self, io, syote):
        self.io = io
        self.syote = syote
        
    def suorita(self):
       self.io.edellinen_operaatio.kumoa()
    
    def kumoa(self):
        self.io.tulos = 0   
    
        