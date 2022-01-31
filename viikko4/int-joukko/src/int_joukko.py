

class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kasvatuskoko = kasvatuskoko
        self.joukko = [0] * kapasiteetti
        self.osoitin = 0

    def kuuluu(self, n):
        return n in self.joukko

    def lisaa(self, n):
        
        if not self.kuuluu(n):
            self.joukko[self.osoitin] = n
            self.osoitin += 1

        if self.osoitin >= len(self.joukko):
            self.kasvata()
            
    def kasvata(self):
        self.joukko = self.joukko + [0] * (self.osoitin + self.kasvatuskoko)
    
    def poista(self, n):
        
        if self.kuuluu(n):
            indeksi = self.joukko.index(n, 0, self.osoitin)
            self.joukko[indeksi] = 0
            self.siirra(indeksi)
            self.osoitin -=1
        

    def siirra(self, indeksi): 
        for i in range(indeksi, self.osoitin - 1):
            self.joukko[i] = self.joukko[i+1]
        
        
    
    def hae_osoitin(self):
        return self.osoitin

    def to_int_list(self):
        taulu = [0] * self.osoitin

        for i in range(0, len(taulu)):
            taulu[i] = self.joukko [i]

        return taulu
    
    
    @staticmethod
    def yhdiste(a, b):
        b_lista = b.to_int_list()

        for i in range(0, len(b_lista)):
            a.lisaa(b_lista[i])

        return a

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
                if a_taulu[i] in b_taulu:
                    y.lisaa(a_taulu[i])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            if a_taulu[i] not in b_taulu:
                z.lisaa(a_taulu[i])

        return z

    def __str__(self):
        if self.osoitin == 0:
            return "{}"
        elif self.osoitin == 1:
            return "{" + str(self.joukko   [0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.osoitin - 1):
                tuotos = tuotos + str(self.joukko  [i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.joukko  [self.osoitin - 1])
            tuotos = tuotos + "}"
            return tuotos
