from unittest import TestCase

from DOMAIN.carti import Carte
from ERRORS.repo_error import RepoError
from INFRASTRUCTURE.fisier_repo_carti import FisierRepoCarti


class TestFisierRepoCarti(TestCase):

    def setUp(self) -> None:
        self.cale_fisier = "fisier_teste_carti.txt"
        self.repo = FisierRepoCarti(self.cale_fisier)
        self.carte = Carte(1,"Abecedar","Abecedar","Ion")

    def tearDown(self) -> None:
        self.repo.clear_file()

    def test_adauga(self):
        self.repo.adauga(self.carte)

        with self.assertRaises(RepoError):
            self.repo.adauga(self.carte)

    def test_modifica(self):
        self.repo.adauga(self.carte)
        nume_mod = "ABC"
        descriere_mod = "ABC"
        autor_mod = "AAA"
        carte_mod = Carte(1,nume_mod,descriere_mod,autor_mod)
        self.repo.modifica(carte_mod)
        self.repo.sterge(1)
        with self.assertRaises(RepoError):
            self.repo.modifica(carte_mod)

    def test_sterge(self):
        self.repo.adauga(self.carte)
        self.assertEqual(self.repo.nr(),1)
        self.repo.sterge(1)
        self.assertEqual(self.repo.nr(),0)
        with self.assertRaises(RepoError):
            self.repo.sterge(1)

    def test_cauta(self):
        self.repo.adauga(self.carte)
        carte_repo = self.repo.cauta(1)
        self.assertEqual(carte_repo.get_id(),1)
        self.assertEqual(carte_repo.get_nume(),"Abecedar")
        self.repo.sterge(1)
        with self.assertRaises(RepoError):
            self.repo.cauta(1)

    def test_get_all(self):
        lista = self.repo.get_all()
        self.assertEqual(len(lista),0)
        self.repo.adauga(self.carte)
        lista = self.repo.get_all()
        self.assertEqual(len(lista),1)
        self.assertTrue(self.carte.__eq__(lista[0]))
        carte2 = Carte(2,"Manual","Manual","Vasile")
        self.repo.adauga(carte2)
        lista = self.repo.get_all()
        self.assertEqual(len(lista),2)
        self.assertTrue(self.carte.__eq__(lista[0]))
        self.assertTrue(carte2.__eq__(lista[1]))
        self.repo.sterge(2)
        lista = self.repo.get_all()
        self.assertEqual(len(lista),1)
        self.repo.sterge(1)
        lista = self.repo.get_all()
        self.assertEqual(len(lista),0)



    def test_nr(self):
        self.assertEqual(self.repo.nr(),0)
        self.repo.adauga(self.carte)
        self.assertEqual(self.repo.nr(),1)
        carte2 = Carte(2, "Manual", "Manual", "Vasile")
        self.repo.adauga(carte2)
        self.assertEqual(self.repo.nr(),2)
        self.repo.sterge(1)
        self.assertEqual(self.repo.nr(),1)
        self.repo.sterge(2)
        self.assertEqual(self.repo.nr(),0)
