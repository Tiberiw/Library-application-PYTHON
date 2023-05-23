from unittest import TestCase

from DOMAIN.carti import Carte
from DOMAIN.clienti import Client
from ERRORS.repo_error import RepoError
from INFRASTRUCTURE.fisier_repo_carti import FisierRepoCarti
from INFRASTRUCTURE.fisier_repo_clienti import FisierRepoClienti


class TestFisierRepoClienti(TestCase):

    def setUp(self) -> None:
        self.cale_fisier = "fisier_teste_clienti.txt"
        self.repo = FisierRepoClienti(self.cale_fisier)
        self.client = Client(1,"Ion","123")

    def tearDown(self) -> None:
        self.repo.clear_file()

    def test_adauga(self):
        self.repo.adauga(self.client)

        with self.assertRaises(RepoError):
            self.repo.adauga(self.client)

    def test_modifica(self):
        self.repo.adauga(self.client)
        CNP_mod = "321"
        nume_mod = "AAA"
        client_mod = Client(1,nume_mod,CNP_mod)
        self.repo.modifica(client_mod)
        self.repo.sterge(1)
        with self.assertRaises(RepoError):
            self.repo.modifica(client_mod)

    def test_sterge(self):
        self.repo.adauga(self.client)
        self.assertEqual(self.repo.nr(),1)
        self.repo.sterge(1)
        self.assertEqual(self.repo.nr(),0)
        with self.assertRaises(RepoError):
            self.repo.sterge(1)

    def test_cauta(self):
        self.repo.adauga(self.client)
        carte_repo = self.repo.cauta(1)
        self.assertEqual(carte_repo.get_id(),1)
        self.assertEqual(carte_repo.get_nume(),"Ion")
        self.repo.sterge(1)
        with self.assertRaises(RepoError):
            self.repo.cauta(1)

    def test_get_all(self):
        lista = self.repo.get_all()
        self.assertEqual(len(lista),0)
        self.repo.adauga(self.client)
        lista = self.repo.get_all()
        self.assertEqual(len(lista),1)
        self.assertTrue(self.client.__eq__(lista[0]))
        client2 = Client(2,"Manuel","456")
        self.repo.adauga(client2)
        lista = self.repo.get_all()
        self.assertEqual(len(lista),2)
        self.assertTrue(self.client.__eq__(lista[0]))
        self.assertTrue(client2.__eq__(lista[1]))
        self.repo.sterge(2)
        lista = self.repo.get_all()
        self.assertEqual(len(lista),1)
        self.repo.sterge(1)
        lista = self.repo.get_all()
        self.assertEqual(len(lista),0)



    def test_nr(self):
        self.assertEqual(self.repo.nr(),0)
        self.repo.adauga(self.client)
        self.assertEqual(self.repo.nr(),1)
        client2 = Client(2, "Manuel","456")
        self.repo.adauga(client2)
        self.assertEqual(self.repo.nr(),2)
        self.repo.sterge(1)
        self.assertEqual(self.repo.nr(),1)
        self.repo.sterge(2)
        self.assertEqual(self.repo.nr(),0)
