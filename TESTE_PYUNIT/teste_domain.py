import unittest

from DOMAIN.carti import Carte
from DOMAIN.clienti import Client
from DOMAIN.inchirieri import Inchiriere
from VALIDATION.valid_carti import ValidCarte
from VALIDATION.valid_clienti import ValidClient
from VALIDATION.valid_inchirieri import ValidInchiriere


class TesteDomain(unittest.TestCase):

    def test_carti_domain(self):
        carte = Carte(1,"Abecedar","Abecedar","Ion")
        self.assertEqual(carte.get_id(),1)
        self.assertEqual(carte.get_nume(),"Abecedar")
        self.assertEqual(carte.get_descriere(),"Abecedar")
        self.assertEqual(carte.get_autor(),"Ion")
        acceeasi_carte = Carte(1,"Abecedar","Avecedar","Ion")
        self.assertTrue(carte.__eq__(acceeasi_carte))
        carte.set_nume("ABC")
        carte.set_autor("Noi")
        carte.set_descriere("ABC")
        self.assertEqual(carte.get_nume(),"ABC")
        self.assertEqual(carte.get_descriere(),"ABC")
        self.assertEqual(carte.get_autor() , "Noi")
        self.assertTrue(carte.__eq__(acceeasi_carte))


    def test_clienti_domain(self):
        client = Client(1,"Gigi","123")
        self.assertEqual(client.get_nume(),"Gigi")
        self.assertEqual(client.get_id(),1)
        self.assertEqual(client.get_CNP(),"123")
        acelasi_client = Client(1,"Gigi","123")
        self.assertTrue(client.__eq__(acelasi_client))
        client.set_nume("Igig")
        client.set_CNP("321")
        self.assertEqual(client.get_nume(),"Igig")
        self.assertEqual(client.get_CNP(),"321")
        self.assertTrue(client.__eq__(acelasi_client))

    def test_inchirieri_domain(self):
        inchiriere = Inchiriere(1,2,3)
        self.assertEqual(inchiriere.get_id(),1)
        self.assertEqual(inchiriere.get_client(),2)
        self.assertEqual(inchiriere.get_carte(),3)
        aceeasi_inchiriere = Inchiriere(1,2,3)
        self.assertTrue(inchiriere.__eq__(aceeasi_inchiriere))

        inchiriere.set_client(22)
        inchiriere.set_carte(44)
        self.assertEqual(inchiriere.get_carte(),44)
        self.assertEqual(inchiriere.get_client(),22)
        self.assertTrue(inchiriere.__eq__(aceeasi_inchiriere))

if __name__ == "__main__":
    unittest.main()