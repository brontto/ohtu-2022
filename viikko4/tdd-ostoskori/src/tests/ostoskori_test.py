import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(),0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(),1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_oikea(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        
        self.assertEqual(self.kori.hinta(), 3)
        
    def test_kahden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_oikein(self):
        maito = Tuote("Maito", 3)
        banaani = Tuote("Banaan", 2)
        
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(banaani)
        
        self.assertEqual(self.kori.hinta(), 5)
    
    def test_kahde_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tarvaraa(self):
        maito = Tuote("Maito", 3)
        banaani = Tuote("Banaan", 2)
        
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(banaani)
        
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        
    def test_kahde_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tarvaraa(self):
        maito = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        
    def test_kahde_saman_tuotteen_lisaamisen_jalkeen_hinta_oikein(self):
        maito = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        
        self.assertEqual(self.kori.hinta(), 6)
        
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostokset = self.kori.ostokset()
        
        self.assertEqual(len(ostokset), 1)
        
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
        
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)
        
        
    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        
        ostos = self.kori.ostokset()[0]
        
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 2)
        
    def test_kahdesta_tuotteesta_toinen_poistetaan(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        
        self.kori.poista_tuote(maito)
        
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 1)
        
        
    def test_tuote_poistetaan_kokonaan(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        
        
        self.kori.poista_tuote(maito)
        
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)
        
    def test_tyhjennetaan_kori_lisaysten_jalkeen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        
        self.kori.tyhjenna()
        
        self.assertTrue(not bool(self.kori.ostokset()))
        