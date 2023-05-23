from unittest import TestCase

from BUSINESS.service_clienti import ServiceClienti
from DOMAIN.clienti import Client
from ERRORS.repo_error import RepoError
from ERRORS.valid_error import ValidError
from INFRASTRUCTURE.fisier_repo_clienti import FisierRepoClienti
from VALIDATION.valid_clienti import ValidClient


class TestServiceClienti(TestCase):


    def setUp(self):
        self.__validare_client = ValidClient()
        self.__cale_fisier_clienti = "fisier_teste_clienti.txt"
        self.__repo_clienti = FisierRepoClienti(self.__cale_fisier_clienti)
        self.__service_clienti = ServiceClienti(self.__validare_client, self.__repo_clienti)

    def tearDown(self):
        self.__repo_clienti.clear_file()

    def test_adauga(self):
        client = Client(1, "aa", "11")
        self.__service_clienti.adauga(1, "aa", "11")
        acelasi_client = Client(1, "aa", "11")
        with self.assertRaises(RepoError):
            self.__service_clienti.adauga(1, "aa", "11")
        with self.assertRaises(ValidError):
            self.__service_clienti.adauga(-1, "bb", "11")
        with self.assertRaises(ValidError):
            self.__service_clienti.adauga(2, "", "11")
        with self.assertRaises(ValidError):
            self.__service_clienti.adauga(2, "aa", "")
        self.assertEqual(self.__service_clienti.nr(), 1)

    def test_cauta(self):
        with self.assertRaises(RepoError):
           non = self.__service_clienti.cauta(1)
        client = Client(1, "aa", "11")
        self.__service_clienti.adauga(1, "aa", "11")
        client_repo = self.__service_clienti.cauta(1)
        self.assertTrue(client.__eq__(client_repo))
        with self.assertRaises(RepoError):
            self.__service_clienti.cauta(2)




    def test_modifica(self):
        with self.assertRaises(RepoError):
            self.__service_clienti.modifica(1,"aa","22")
        client = Client(1, "aa", "11")
        self.__service_clienti.adauga(1, "aa", "11")
        with self.assertRaises(RepoError):
            self.__service_clienti.modifica(2, "aa", "11")
        with self.assertRaises(ValidError):
            self.__service_clienti.modifica(1, "", "11")
        with self.assertRaises(ValidError):
            self.__service_clienti.modifica(1, "aa", "")

