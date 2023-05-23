import unittest

from DOMAIN.carti import Carte
from DOMAIN.clienti import Client
from DOMAIN.inchirieri import Inchiriere
from ERRORS.valid_error import ValidError
from VALIDATION.valid_carti import ValidCarte
from VALIDATION.valid_clienti import ValidClient
from VALIDATION.valid_inchirieri import ValidInchiriere


class TesteValidator(unittest.TestCase):

    def setUp(self):
        self.__validare_carti = ValidCarte()
        self.__validare_clienti = ValidClient()
        self.__validare_inchirieri = ValidInchiriere()

    def test_carti(self):
        id_carte = 1
        nume_carte = "ab"
        descriere_carte = "cd"
        autor_carte = "ef"
        carte1 = Carte(id_carte,nume_carte,descriere_carte,autor_carte)
        self.__validare_carti.valideaza(carte1)
        id_carte_invalid = -1
        nume_carte_invalid = ""
        descriere_carte_invalid = ""
        autor_carte_invalid = ""
        carte_invalida1 = Carte(id_carte_invalid,nume_carte,descriere_carte,autor_carte)
        with self.assertRaises(ValidError):
            self.__validare_carti.valideaza(carte_invalida1)
        carte_invalida2 = Carte(id_carte,nume_carte_invalid,descriere_carte,autor_carte)
        with self.assertRaises(ValidError):
            self.__validare_carti.valideaza(carte_invalida2)
        carte_invalida3 = Carte(id_carte,nume_carte,descriere_carte_invalid,autor_carte)
        with self.assertRaises(ValidError):
            self.__validare_carti.valideaza(carte_invalida3)
        carte_invalida4 = Carte(id_carte,nume_carte,descriere_carte,autor_carte_invalid)
        with self.assertRaises(ValidError):
            self.__validare_carti.valideaza(carte_invalida4)


    def test_clienti(self):
        id_client = 1
        nume_client = "ab"
        CNP_client = "cd"
        client1 = Client(id_client,nume_client,CNP_client)
        self.__validare_clienti.valideaza(client1)
        id_client_invalid = -1
        nume_client_invalid = ""
        CNP_client_invalid = ""
        client_invalid1 = Client(id_client_invalid,nume_client,CNP_client)
        with self.assertRaises(ValidError):
            self.__validare_clienti.valideaza(client_invalid1)
        client_invalid2 = Client(id_client,nume_client_invalid,CNP_client)
        with self.assertRaises(ValidError):
            self.__validare_clienti.valideaza(client_invalid2)
        client_invalid3 = Client(id_client,nume_client,CNP_client_invalid)
        with self.assertRaises(ValidError):
            self.__validare_clienti.valideaza(client_invalid3)

    def test_inchirieri(self):
        id_inc = 1
        client_inc = 1
        carte_inc = 1
        inc1 = Inchiriere(id_inc, client_inc, carte_inc)
        self.__validare_inchirieri.valideaza(inc1)
        id_inchiriere_invalid = -1
        client_inc_invalid = -1
        carte_inc_invalid = -1
        inc_invalid1 = Inchiriere(id_inchiriere_invalid, client_inc, carte_inc)
        with self.assertRaises(ValidError):
            self.__validare_inchirieri.valideaza(inc_invalid1)
        inc_invalid2 = Inchiriere(id_inc, client_inc_invalid, carte_inc)
        with self.assertRaises(ValidError):
            self.__validare_inchirieri.valideaza(inc_invalid2)
        inc_invalid3 = Inchiriere(id_inc, client_inc, carte_inc_invalid)
        with self.assertRaises(ValidError):
            self.__validare_inchirieri.valideaza(inc_invalid3)

if __name__ == "__main__":
    unittest.main()