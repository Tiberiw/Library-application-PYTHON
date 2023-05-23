from unittest import TestCase

from BUSINESS.service_carti import ServiceCarti
from DOMAIN.carti import Carte
from ERRORS.repo_error import RepoError
from ERRORS.valid_error import ValidError
from INFRASTRUCTURE.fisier_repo_carti import FisierRepoCarti
from VALIDATION.valid_carti import ValidCarte


class TestServiceCarti(TestCase):

    def setUp(self):
        self.__validare_carte = ValidCarte()
        self.__cale_fisier_carti = "fisier_teste_carti.txt"
        self.__repo_carti = FisierRepoCarti(self.__cale_fisier_carti)
        self.__service_carti = ServiceCarti(self.__validare_carte, self.__repo_carti)

    def tearDown(self):
        self.__repo_carti.clear_file()

    def test_adauga(self):
        carte = Carte(1, "aa", "aa","aa")
        self.__service_carti.adauga(1, "aa", "aa","aa")
        acelasi_carte = Carte(1, "aa", "aa", "aa")
        with self.assertRaises(RepoError):
            self.__service_carti.adauga(1, "aa", "aa", "aa")
        with self.assertRaises(ValidError):
            self.__service_carti.adauga(-1, "bb", "bb", "bb")
        with self.assertRaises(ValidError):
            self.__service_carti.adauga(2, "", "bb", "bb")
        with self.assertRaises(ValidError):
            self.__service_carti.adauga(2, "aa", "", "aa")
        self.assertEqual(self.__service_carti.nr(), 1)

    def test_cauta(self):
        with self.assertRaises(RepoError):
           non = self.__service_carti.cauta(1)
        carte = Carte(1, "aa", "aa", "aa")
        self.__service_carti.adauga(1, "aa", "aa", "aa")
        carte_repo = self.__service_carti.cauta(1)
        self.assertTrue(carte.__eq__(carte_repo))
        with self.assertRaises(RepoError):
            self.__service_carti.cauta(2)

    def test_modifica(self):
        with self.assertRaises(RepoError):
            self.__service_carti.modifica(1,"aa","aa", "aa")
        carte = Carte(1, "aa", "aa", "aa")
        self.__service_carti.adauga(1, "aa", "aa", "aa")
        with self.assertRaises(RepoError):
            self.__service_carti.modifica(2, "aa", "aa", "aa")
        with self.assertRaises(ValidError):
            self.__service_carti.modifica(1, "", "aa", "aa")
        with self.assertRaises(ValidError):
            self.__service_carti.modifica(1, "aa", "", "aa")

