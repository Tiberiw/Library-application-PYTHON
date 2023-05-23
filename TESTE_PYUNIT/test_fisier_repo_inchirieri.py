from unittest import TestCase

from DOMAIN.carti import Carte
from DOMAIN.clienti import Client
from DOMAIN.inchirieri import Inchiriere
from ERRORS.repo_error import RepoError
from INFRASTRUCTURE.fisier_repo_carti import FisierRepoCarti
from INFRASTRUCTURE.fisier_repo_clienti import FisierRepoClienti
from INFRASTRUCTURE.fisier_repo_inchirieri import FisierRepoInchirieri


class TestFisierRepoInchirieri(TestCase):

    def setUp(self) -> None:
        self.cale_fisier = "fisier_teste_inchirieri.txt"
        self.repo = FisierRepoInchirieri(self.cale_fisier)
        self.inchiriere = Inchiriere(1,1,1)

    def tearDown(self) -> None:
        self.repo.clear_file()

    def test_adauga(self):
        self.repo.adauga(self.inchiriere)

        with self.assertRaises(RepoError):
            self.repo.adauga(self.inchiriere)

    def test_modifica(self):
        self.repo.adauga(self.inchiriere)
        client_mod = "2"
        carte_mod = "2"
        inchiriere_mod = Inchiriere(1,client_mod,carte_mod)
        self.repo.modifica(inchiriere_mod)
        self.repo.sterge(1)
        with self.assertRaises(RepoError):
            self.repo.modifica(inchiriere_mod)

    def test_sterge(self):
        self.repo.adauga(self.inchiriere)
        self.assertEqual(self.repo.nr(),1)
        self.repo.sterge(1)
        self.assertEqual(self.repo.nr(),0)
        with self.assertRaises(RepoError):
            self.repo.sterge(1)

    def test_cauta(self):
        self.repo.adauga(self.inchiriere)
        carte_repo = self.repo.cauta(1)
        self.assertEqual(carte_repo.get_id(),1)
        self.assertEqual(carte_repo.get_client(),1)
        self.repo.sterge(1)
        with self.assertRaises(RepoError):
            self.repo.cauta(1)

    def test_get_all(self):
        lista = self.repo.get_all()
        self.assertEqual(len(lista),0)
        self.repo.adauga(self.inchiriere)
        lista = self.repo.get_all()
        self.assertEqual(len(lista),1)
        self.assertTrue(self.inchiriere.__eq__(lista[0]))
        inchiriere2 = Inchiriere(2,2,2)
        self.repo.adauga(inchiriere2)
        lista = self.repo.get_all()
        self.assertEqual(len(lista),2)
        self.assertTrue(self.inchiriere.__eq__(lista[0]))
        self.assertTrue(inchiriere2.__eq__(lista[1]))
        self.repo.sterge(2)
        lista = self.repo.get_all()
        self.assertEqual(len(lista),1)
        self.repo.sterge(1)
        lista = self.repo.get_all()
        self.assertEqual(len(lista),0)



    def test_nr(self):
        self.assertEqual(self.repo.nr(),0)
        self.repo.adauga(self.inchiriere)
        self.assertEqual(self.repo.nr(),1)
        inchiriere2 = Inchiriere(2, 2,2)
        self.repo.adauga(inchiriere2)
        self.assertEqual(self.repo.nr(),2)
        self.repo.sterge(1)
        self.assertEqual(self.repo.nr(),1)
        self.repo.sterge(2)
        self.assertEqual(self.repo.nr(),0)
