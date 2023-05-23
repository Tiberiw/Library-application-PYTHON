from unittest import TestCase

from DOMAIN.clienti import Client
from ERRORS.repo_error import RepoError
from INFRASTRUCTURE.fisier_repo_clienti import FisierRepoClienti


class TestRepoClienti(TestCase):


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


    def test_sterge(self):
        self.repo.adauga(self.client)
        self.assertEqual(self.repo.nr(),1)
        self.repo.sterge(1)
        self.assertEqual(self.repo.nr(),0)
        with self.assertRaises(RepoError):
            self.repo.sterge(1)
