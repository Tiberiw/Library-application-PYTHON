from unittest import TestCase

from BUSINESS.service_carti import ServiceCarti
from BUSINESS.service_clienti import ServiceClienti
from BUSINESS.service_inchirieri import ServiceInchirieri
from DOMAIN.carti import Carte
from DOMAIN.clienti import Client
from DOMAIN.inchirieri import Inchiriere
from ERRORS.repo_error import RepoError
from ERRORS.valid_error import ValidError
from INFRASTRUCTURE.fisier_repo_carti import FisierRepoCarti
from INFRASTRUCTURE.fisier_repo_clienti import FisierRepoClienti
from INFRASTRUCTURE.fisier_repo_inchirieri import FisierRepoInchirieri
from INFRASTRUCTURE.repo_carti import RepoCarti
from INFRASTRUCTURE.repo_clienti import RepoClienti
from INFRASTRUCTURE.repo_inchirieri import RepoInchirieri
from VALIDATION.valid_carti import ValidCarte
from VALIDATION.valid_clienti import ValidClient
from VALIDATION.valid_inchirieri import ValidInchiriere


class TestServiceInchirieri(TestCase):

    def setUp(self):
        self.__validare_inchiriere = ValidInchiriere()
        self.__validare_carte = ValidCarte()
        self.__validare_client = ValidClient()
        self.__cale_fisier_inchirieri = "fisier_teste_inchirieri.txt"
        self.__repo_inchirieri = FisierRepoInchirieri(self.__cale_fisier_inchirieri)
        self.__cale_fisier_clienti = "fisier_teste_clienti.txt"
        self.__repo_clienti = FisierRepoClienti(self.__cale_fisier_clienti)
        self.__cale_fisier_carti = "fisier_teste_carti.txt"
        self.__repo_carti = FisierRepoCarti(self.__cale_fisier_carti)
        self.__service_inchirieri = ServiceInchirieri(self.__validare_inchiriere,self.__repo_inchirieri,self.__repo_clienti,self.__repo_carti)
        self.__service_carti = ServiceCarti(self.__validare_carte,self.__repo_carti)
        self.__service_clienti = ServiceClienti(self.__validare_client,self.__repo_clienti)
        self.carte = Carte(1,"Abecedar","Abecedar","Ion")
        self.client = Client(1,"Gigel","123")
        self.inchiriere = Inchiriere(1,1,1)
        self.client2 = Client(2,"Gigel","1234")
        self.carte2 = Carte(2,"Culegere","Clh","Marian")

    def tearDown(self):
        self.__repo_carti.clear_file()
        self.__repo_clienti.clear_file()
        self.__repo_inchirieri.clear_file()

    def test_adauga(self):
        inchiriere = Inchiriere(1,1,1)
        with self.assertRaises(RepoError):
            self.__service_inchirieri.adauga(1,1,1)
        self.__repo_clienti.adauga(self.client)
        with self.assertRaises(RepoError):
            self.__service_inchirieri.adauga(1,1,1)
        self.__repo_carti.adauga(self.carte)
        self.__service_inchirieri.adauga(1,1,1)
        acceasi_inchiriere = Inchiriere(1,1,1)
        with self.assertRaises(RepoError):
            self.__service_inchirieri.adauga(1,1,1)
        inchiriere_gresita1 = Inchiriere(-1,1,1)
        inchiriere_gresita2 = Inchiriere(2,-1,1)
        inchiriere_gresita3 = Inchiriere(2,1,-1)
        with self.assertRaises(ValidError):
            self.__service_inchirieri.adauga(-1,1,1)
        with self.assertRaises(RepoError):
            self.__service_inchirieri.adauga(2,-1,1)
        with self.assertRaises(RepoError):
            self.__service_inchirieri.adauga(2,1,-1)
        self.assertEqual(self.__service_inchirieri.nr(),1)

    def test_modifica(self):
        inchiriere = Inchiriere(1,1,1)
        with self.assertRaises(RepoError):
            self.__service_inchirieri.modifica(1,2,2)
        self.__repo_clienti.adauga(self.client)
        with self.assertRaises(RepoError):
            self.__service_inchirieri.modifica(1,2,2)
        self.__repo_carti.adauga(self.carte)
        self.__service_inchirieri.adauga(1,1,1)
        client2 = Client(2,"Gigel","1234")
        carte2 = Carte(2,"Culegere","Clh","Marian")
        self.__repo_clienti.adauga(client2)
        self.__repo_carti.adauga(carte2)
        self.__service_inchirieri.modifica(1,2,2)
        inchiriere_gresita1 = Inchiriere(-1,1,1)
        inchiriere_gresita2 = Inchiriere(2,-1,1)
        inchiriere_gresita3 = Inchiriere(2,1,-1)
        with self.assertRaises(ValidError):
            self.__service_inchirieri.modifica(-1,1,1)
        with self.assertRaises(RepoError):
            self.__service_inchirieri.modifica(2,-1,1)
        with self.assertRaises(RepoError):
            self.__service_inchirieri.modifica(2,1,-1)
        self.assertEqual(self.__service_inchirieri.nr(),1)

    def test_sterge(self):
        with self.assertRaises(RepoError):
            self.__service_inchirieri.sterge(1)
        with self.assertRaises(RepoError):
            self.__service_inchirieri.sterge(-1)
        self.__repo_clienti.adauga(self.client)
        self.__repo_carti.adauga(self.carte)
        self.__service_inchirieri.adauga(1,1,1)
        self.assertEqual(self.__repo_inchirieri.nr(),1)
        with self.assertRaises(RepoError):
            self.__service_inchirieri.sterge(2)
        self.assertEqual(self.__repo_inchirieri.nr(), 1)
        self.__repo_clienti.adauga(self.client2)
        self.__repo_carti.adauga(self.carte2)
        self.__service_inchirieri.adauga(2,2,2)
        self.assertEqual(self.__repo_inchirieri.nr(),2)
        self.__service_inchirieri.sterge(2)
        self.assertEqual(self.__repo_inchirieri.nr(), 1)
        self.__service_inchirieri.sterge(1)

    def test_cauta(self):
        with self.assertRaises(RepoError):
            non = self.__service_inchirieri.cauta(1)
        with self.assertRaises(RepoError):
            non = self.__service_inchirieri.cauta(-1)
        self.__repo_clienti.adauga(self.client)
        self.__repo_carti.adauga(self.carte)
        self.__service_inchirieri.adauga(1,1,1)
        self.assertEqual(self.__repo_inchirieri.nr(),1)
        with self.assertRaises(RepoError):
            non = self.__service_inchirieri.cauta(2)
        self.assertEqual(self.__repo_inchirieri.nr(), 1)
        self.__repo_clienti.adauga(self.client2)
        self.__repo_carti.adauga(self.carte2)
        self.__service_inchirieri.adauga(2,2,2)

        inc2 = self.__service_inchirieri.cauta(2)
        self.assertEqual(inc2.get_id() , 2)
        self.assertEqual(inc2.get_client(), 2)
        inc1 = self.__service_inchirieri.cauta(1)
        self.assertEqual(inc1.get_id(), 1)
        self.assertEqual(inc1.get_client(), 1)

    def test_get_all(self):
        lista = self.__service_inchirieri.get_all()
        self.assertEqual(len(lista), 0)
        self.assertEqual(lista, [])
        self.__service_carti.adauga(1,"a","b","c")
        self.__service_carti.adauga(2, "aa", "bb", "cc")
        self.__service_carti.adauga(3, "aaa", "bbb", "ccc")
        self.__service_clienti.adauga(1,"a","b")
        self.__service_clienti.adauga(2, "a", "b")
        self.__service_clienti.adauga(3, "a", "b")
        self.__service_inchirieri.adauga(1,1,1)
        self.__service_inchirieri.adauga(2,2,1)
        self.__service_inchirieri.adauga(3,3,1)
        self.__service_inchirieri.adauga(4,1,2)
        self.__service_inchirieri.adauga(5,2,2)
        self.__service_inchirieri.adauga(6,3,3)
        lista = self.__service_inchirieri.get_all()
        self.assertEqual(len(lista), 6)


        self.__service_inchirieri.sterge(6)
        lista = self.__service_inchirieri.get_all()
        self.assertEqual(len(lista), 5)

        self.__service_inchirieri.sterge(5)
        lista = self.__service_inchirieri.get_all()
        self.assertEqual(len(lista), 4)

    def test_nr(self):
        num = self.__service_inchirieri.nr()
        self.assertEqual(num, 0)
        self.__service_carti.adauga(1, "a", "b", "c")
        self.__service_carti.adauga(2, "aa", "bb", "cc")
        self.__service_carti.adauga(3, "aaa", "bbb", "ccc")
        self.__service_clienti.adauga(1, "a", "b")
        self.__service_clienti.adauga(2, "a", "b")
        self.__service_clienti.adauga(3, "a", "b")
        self.__service_inchirieri.adauga(1, 1, 1)
        self.__service_inchirieri.adauga(2, 2, 1)
        self.__service_inchirieri.adauga(3, 3, 1)
        self.__service_inchirieri.adauga(4, 1, 2)
        self.__service_inchirieri.adauga(5, 2, 2)
        self.__service_inchirieri.adauga(6, 3, 3)
        num = self.__service_inchirieri.nr()
        self.assertEqual(num, 6)

        self.__service_inchirieri.sterge(6)
        num = self.__service_inchirieri.nr()
        self.assertEqual(num, 5)

        self.__service_inchirieri.sterge(5)
        num = self.__service_inchirieri.nr()
        self.assertEqual(num, 4)

    def test_sterge_client(self):

        id_client = 1
        nume_client = "ab"
        CNP_client = "cd"
        client1 = Client(id_client, nume_client, CNP_client)
        self.__service_clienti.adauga(id_client, nume_client, CNP_client)

        id_client_2 = 2
        nume_client_2 = "abc"
        CNP_client_2 = "def"
        client2 = Client(id_client_2, nume_client_2, CNP_client_2)
        self.__service_clienti.adauga(id_client_2, nume_client_2, CNP_client_2)

        id_client_3 = 3
        nume_client_3 = "abcd"
        CNP_client_3 = "efgh"
        client3 = Client(id_client_3, nume_client_3, CNP_client_3)
        self.__service_clienti.adauga(id_client_3, nume_client_3, CNP_client_3)

        self.__service_inchirieri.sterge_client(id_client_3)
        self.assertEqual(self.__service_clienti.nr() , 2)
        lista_clienti = self.__service_clienti.get_all()
        self.assertTrue (client1.__eq__(lista_clienti[0]))
        self.assertTrue (client2.__eq__(lista_clienti[1]))
        with self.assertRaises(RepoError):
            self.__service_inchirieri.sterge_client(id_client_3)
        self.__service_inchirieri.sterge_client(id_client_2)
        assert (self.__service_clienti.nr() == 1)
        self.__service_inchirieri.sterge_client(id_client)
        assert (self.__service_clienti.nr() == 0)

    def test_sterge_carte(self):
        id_carte = 1
        nume_carte = "aa"
        descriere_carte = "aa"
        autor_carte = "aa"
        carte1 = Carte(id_carte, nume_carte, descriere_carte,autor_carte)
        self.__service_carti.adauga(id_carte, nume_carte, descriere_carte,autor_carte)

        id_carte2 = 2
        nume_carte2 = "bb"
        descriere_carte2 = "bb"
        autor_carte2 = "bb"
        carte2 = Carte(id_carte2, nume_carte2, descriere_carte2,autor_carte2)
        self.__service_carti.adauga(id_carte2, nume_carte2, descriere_carte2,autor_carte2)

        id_carte3 = 3
        nume_carte3 = "cc"
        descriere_carte3 = "cc"
        autor_carte3 = "cc"
        carte3 = Carte(id_carte3, nume_carte3, descriere_carte3, autor_carte3)
        self.__service_carti.adauga(id_carte3, nume_carte3, descriere_carte3, autor_carte3)

        self.__service_inchirieri.sterge_carte(id_carte3)
        self.assertEqual(self.__service_carti.nr() , 2)
        lista_carti = self.__service_carti.get_all()
        self.assertTrue (carte1.__eq__(lista_carti[0]))
        self.assertTrue (carte2.__eq__(lista_carti[1]))
        with self.assertRaises(RepoError):
            self.__service_inchirieri.sterge_carte(id_carte3)
        self.__service_inchirieri.sterge_carte(id_carte2)
        assert (self.__service_carti.nr() == 1)
        self.__service_inchirieri.sterge_carte(id_carte)
        assert (self.__service_carti.nr() == 0)

    def test_rap_top_carti(self):
        top = self.__service_inchirieri.rap_top_carti()
        self.assertEqual(len(top), 0)
        self.__service_carti.adauga(1,"a","b","c")
        self.__service_carti.adauga(2, "aa", "bb", "cc")
        self.__service_carti.adauga(3, "aaa", "bbb", "ccc")
        self.__service_clienti.adauga(1,"a","b")
        self.__service_clienti.adauga(2, "a", "b")
        self.__service_clienti.adauga(3, "a", "b")
        self.__service_inchirieri.adauga(1,1,1)
        self.__service_inchirieri.adauga(2,2,1)
        self.__service_inchirieri.adauga(3,3,1)
        self.__service_inchirieri.adauga(4,1,2)
        self.__service_inchirieri.adauga(5,2,2)
        self.__service_inchirieri.adauga(6,3,3)
        top_carti = self.__service_inchirieri.rap_top_carti()
        self.assertEqual(len(top_carti) , 3)
        carte1 = self.__service_carti.cauta(1)
        carte2 = self.__service_carti.cauta(2)
        carte3 = self.__service_carti.cauta(3)
        self.assertTrue(carte1.__eq__(top_carti[0]))
        self.assertTrue(carte2.__eq__(top_carti[1]))
        self.assertTrue(carte3.__eq__(top_carti[2]))
        self.__service_carti.adauga(4,"aaaa","bbbb","cccc")
        self.__service_inchirieri.adauga(7,1,4)
        top_carti = self.__service_inchirieri.rap_top_carti()
        self.assertEqual(len(top_carti), 4)
        carte1 = self.__service_carti.cauta(1)
        carte2 = self.__service_carti.cauta(2)
        carte3 = self.__service_carti.cauta(3)
        carte4 = self.__service_carti.cauta(4)
        self.assertTrue(carte1.__eq__(top_carti[0]))
        self.assertTrue(carte2.__eq__(top_carti[1]))
        self.assertTrue(carte3.__eq__(top_carti[3]))
        self.assertTrue(carte4.__eq__(top_carti[2]))


    def test_rap_20_clienti(self):
        self.__service_carti.adauga(1, "a", "b", "c")
        self.__service_carti.adauga(2, "aa", "bb", "cc")
        self.__service_carti.adauga(3, "aaa", "bbb", "ccc")
        self.__service_clienti.adauga(1, "a", "b")
        self.__service_clienti.adauga(2, "a", "b")
        self.__service_clienti.adauga(3, "a", "b")
        self.__service_inchirieri.adauga(1, 1, 1)
        self.__service_inchirieri.adauga(2, 2, 1)
        self.__service_inchirieri.adauga(3, 3, 1)
        self.__service_inchirieri.adauga(4, 1, 2)
        self.__service_inchirieri.adauga(5, 2, 2)
        self.__service_inchirieri.adauga(6, 3, 3)
        raport = self.__service_inchirieri.rap_20_clienti()
        self.assertEqual(len(raport),0)
        self.__service_clienti.adauga(4, "d", "d")
        self.__service_clienti.adauga(5, "e", "e")
        self.__service_clienti.adauga(6, "sase", "sase")
        self.__service_inchirieri.adauga(7, 4, 1)
        self.__service_inchirieri.adauga(8, 4, 2)
        self.__service_inchirieri.adauga(9, 5, 3)
        self.__service_inchirieri.adauga(10, 6, 1)
        self.__service_inchirieri.adauga(11, 6, 2)
        self.__service_inchirieri.adauga(12, 6, 3)
        top_20_clienti = self.__service_inchirieri.rap_20_clienti()
        self.assertEqual(len(top_20_clienti) , 1)
        self.assertEqual(top_20_clienti[0].get_nume() , "sase")
        self.assertEqual(top_20_clienti[0].get_nr() , 3)
        self.__service_clienti.adauga(7,"sapte","sapte")
        self.__service_clienti.adauga(8,"opt","opt")
        self.__service_clienti.adauga(9,"noua","noua")
        self.__service_clienti.adauga(10,"zece","zece")
        self.__service_inchirieri.adauga(13, 7, 1)
        self.__service_inchirieri.adauga(14, 8, 1)
        self.__service_inchirieri.adauga(15, 9, 1)
        self.__service_inchirieri.adauga(16, 10, 1)
        top_20_clienti = self.__service_inchirieri.rap_20_clienti()
        self.assertEqual(len(top_20_clienti) , 2)
        self.assertEqual(top_20_clienti[1].get_nume(), "d")
        self.assertEqual(top_20_clienti[1].get_nr(), 2)
        self.__service_inchirieri.adauga(17,1,3)
        top_20_clienti = self.__service_inchirieri.rap_20_clienti()
        self.assertEqual(len(top_20_clienti) , 2)
        self.assertEqual(top_20_clienti[0].get_nume() , "sase")
        self.assertEqual(top_20_clienti[0].get_nr() , 3)
        self.assertEqual(top_20_clienti[1].get_nume() , "a")
        self.assertEqual(top_20_clienti[1].get_nr() , 3)


    def test_rap_clienti_carti_nr(self):
        clienti_carti_nr = self.__service_inchirieri.rap_clienti_carti_nr()
        self.assertEqual(len(clienti_carti_nr) , 0)

        self.__service_carti.adauga(1, "a", "b", "c")
        self.__service_carti.adauga(2, "aa", "bb", "cc")
        self.__service_carti.adauga(3, "aaa", "bbb", "ccc")
        self.__service_clienti.adauga(1, "a", "b")
        self.__service_clienti.adauga(2, "a", "b")
        self.__service_clienti.adauga(3, "a", "b")
        self.__service_inchirieri.adauga(1, 1, 1)
        self.__service_inchirieri.adauga(2, 2, 1)
        self.__service_inchirieri.adauga(3, 3, 1)
        self.__service_inchirieri.adauga(4, 1, 2)
        self.__service_inchirieri.adauga(5, 2, 2)
        self.__service_inchirieri.adauga(6, 3, 3)

        clienti_carti_nr = self.__service_inchirieri.rap_clienti_carti_nr()
        self.assertEqual(len(clienti_carti_nr) , 3)
        self.assertEqual (clienti_carti_nr[0].get_nr() , 2)
        self.assertEqual (clienti_carti_nr[1].get_nr() , 2)
        self.assertEqual(clienti_carti_nr[2].get_nr() , 2)

        self.__service_clienti.adauga(4, "d", "d")
        self.__service_clienti.adauga(5, "e", "e")
        self.__service_clienti.adauga(6, "sase", "sase")
        self.__service_inchirieri.adauga(7, 4, 1)
        self.__service_inchirieri.adauga(8, 4, 2)
        self.__service_inchirieri.adauga(9, 5, 3)
        self.__service_inchirieri.adauga(10, 6, 1)
        self.__service_inchirieri.adauga(11, 6, 2)
        self.__service_inchirieri.adauga(12, 6, 3)


        clienti_carti_nr = self.__service_inchirieri.rap_clienti_carti_nr()
        self.assertEqual(len(clienti_carti_nr) , 6)
        self.assertEqual (clienti_carti_nr[0].get_nr() , 3)
        self.assertEqual (clienti_carti_nr[1].get_nr() , 2)
        self.assertEqual(clienti_carti_nr[2].get_nr() , 2)
        self.assertEqual(clienti_carti_nr[3].get_nr() , 2)
        self.assertEqual(clienti_carti_nr[4].get_nr() , 2)
        self.assertEqual(clienti_carti_nr[5].get_nr() , 1)


    def test_rap_clienti_carti_nume(self):
        clienti_carti_nume = self.__service_inchirieri.rap_clienti_carti_nume()
        self.assertEqual(len(clienti_carti_nume) , 0)
        self.__service_carti.adauga(1, "a", "b", "c")
        self.__service_carti.adauga(2, "aa", "bb", "cc")
        self.__service_carti.adauga(3, "aaa", "bbb", "ccc")
        self.__service_clienti.adauga(1, "a", "b")
        self.__service_clienti.adauga(2, "a", "b")
        self.__service_clienti.adauga(3, "a", "b")
        self.__service_inchirieri.adauga(1, 1, 1)
        self.__service_inchirieri.adauga(2, 2, 1)
        self.__service_inchirieri.adauga(3, 3, 1)
        self.__service_inchirieri.adauga(4, 1, 2)
        self.__service_inchirieri.adauga(5, 2, 2)
        self.__service_inchirieri.adauga(6, 3, 3)

        clienti_carti_nume = self.__service_inchirieri.rap_clienti_carti_nume()
        self.assertEqual(len(clienti_carti_nume) , 3)
        self.assertEqual(clienti_carti_nume[0].get_nume() , "a")
        self.assertEqual(clienti_carti_nume[1].get_nume() , "a")
        self.assertEqual(clienti_carti_nume[2].get_nume() , "a")

        self.__service_clienti.adauga(4, "d", "d")
        self.__service_clienti.adauga(5, "e", "e")
        self.__service_clienti.adauga(6, "sase", "sase")
        self.__service_inchirieri.adauga(7, 4, 1)
        self.__service_inchirieri.adauga(8, 4, 2)
        self.__service_inchirieri.adauga(9, 5, 3)
        self.__service_inchirieri.adauga(10, 6, 1)
        self.__service_inchirieri.adauga(11, 6, 2)
        self.__service_inchirieri.adauga(12, 6, 3)

        clienti_carti_nume = self.__service_inchirieri.rap_clienti_carti_nume()
        self.assertEqual(len(clienti_carti_nume) , 6)

        self.assertEqual(clienti_carti_nume[0].get_nume() , "a")
        self.assertEqual(clienti_carti_nume[1].get_nume() , "a")
        self.assertEqual(clienti_carti_nume[2].get_nume() , "a")
        self.assertEqual(clienti_carti_nume[3].get_nume() , "d")
        self.assertEqual(clienti_carti_nume[4].get_nume() , "e")
        self.assertEqual(clienti_carti_nume[5].get_nume() , "sase")
