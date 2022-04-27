from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly

class KPS:
    def __init__(self, komento):
        self.peli = None
        if komento.endswith("a"):
            self.peli = KPS.luo_pelaaja_vs_pelaaja_kps()
        if komento.endswith("b"):
            self.peli = KPS.luo_tekoaly_kps()
        if komento.endswith("c"):
            self.peli = KPS.luo_parempi_tekoaly_kps()
            
        
    def pelaa(self):
        self.peli.pelaa()
        
    @staticmethod
    def luo_parempi_tekoaly_kps():
        return KPSParempiTekoaly()
    
    @staticmethod
    def luo_pelaaja_vs_pelaaja_kps():
        return KPSPelaajaVsPelaaja()
    
    def luo_tekoaly_kps():
        return KPSTekoaly()