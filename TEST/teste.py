from DOMAIN.carti import Carte
from DOMAIN.clienti import Client
from DOMAIN.inchirieri import Inchiriere
from ERRORS.repo_error import RepoError
from ERRORS.valid_error import ValidError
from VALIDATION.valid_carti import ValidCarte
from VALIDATION.valid_clienti import ValidClient
from VALIDATION.valid_inchirieri import ValidInchiriere
from INFRASTRUCTURE.repo_carti import RepoCarti
from INFRASTRUCTURE.repo_clienti import RepoClienti
from INFRASTRUCTURE.repo_inchirieri import RepoInchirieri
from BUSINESS.service_carti import ServiceCarti
from BUSINESS.service_clienti import ServiceClienti
from BUSINESS.service_inchirieri import ServiceInchirieri


class Test:

    def __init__(self):
        self.__validare_carti = ValidCarte()
        self.__validare_clienti = ValidClient()
        self.__validare_inchiriere = ValidInchiriere()
        self.__repo_carti = RepoCarti()
        self.__repo_clienti = RepoClienti()
        self.__repo_inchirieri = RepoInchirieri()
        self.__service_carti = ServiceCarti(self.__validare_carti,self.__repo_carti)
        self.__service_clienti = ServiceClienti(self.__validare_clienti,self.__repo_clienti)
        self.__service_inchirieri = ServiceInchirieri(self.__validare_inchiriere,self.__repo_inchirieri,self.__repo_clienti,self.__repo_carti)


    def __ruleaza_teste_domain(self):
        id_carte = 1
        nume_carte = "ab"
        descriere_carte = "cd"
        autor_carte = "ef"
        carte1 = Carte(id_carte,nume_carte,descriere_carte,autor_carte)
        assert(carte1.get_id() == id_carte)
        assert(carte1.get_nume() == nume_carte)
        assert(carte1.get_descriere() == descriere_carte)
        assert(carte1.get_autor() == autor_carte)
        acelasi_id_carte = id_carte
        carte2 = Carte(acelasi_id_carte,nume_carte,descriere_carte,autor_carte)
        assert(carte2.__eq__(carte1) == True)
        id_nou_carte = 2
        nume_nou_carte = "abc"
        descriere_nou_carte = "def"
        autor_nou_carte = "ghi"
        carte2.set_id(id_nou_carte)
        carte2.set_nume(nume_nou_carte)
        carte2.set_descriere(descriere_nou_carte)
        carte2.set_autor(autor_nou_carte)
        assert(carte2.get_id() == id_nou_carte)
        assert(carte2.get_nume() == nume_nou_carte)
        assert(carte2.get_descriere() == descriere_nou_carte)
        assert(carte2.get_autor() == autor_nou_carte)
        assert(carte2.__eq__(carte1) == False)





        id_client = 1
        nume_client = "ab"
        CNP_client = "cd"
        client1 = Client(id_client, nume_client, CNP_client)
        assert (client1.get_id() == id_client)
        assert (client1.get_nume() == nume_client)
        assert (client1.get_CNP() == CNP_client)
        acelasi_id_client = id_client
        client2 = Client(acelasi_id_client, nume_client, CNP_client)
        assert (client2.__eq__(client1) == True)
        id_nou_client = 2
        nume_nou_client = "abc"
        CNP_nou_client = "def"
        client2.set_id(id_nou_client)
        client2.set_nume(nume_nou_client)
        client2.set_CNP(CNP_nou_client)
        assert (client2.get_id() == id_nou_client)
        assert (client2.get_nume() == nume_nou_client)
        assert (client2.get_CNP() == CNP_nou_client)
        assert (client2.__eq__(client1) == False)





        id_inc = 1
        client_inc = 1
        carte_inc = 1
        inc1 = Inchiriere(id_inc,client_inc,carte_inc)
        assert(inc1.get_id() == id_inc)
        assert(inc1.get_client() == client_inc)
        assert(inc1.get_carte() == carte_inc)
        acelasi_id_inc = id_inc
        inc2 = Inchiriere(acelasi_id_inc,client_inc,carte_inc)
        assert(inc2.__eq__(inc1) == True)
        id_nou_inc = 2
        client_nou_inc = 2
        carte_nou_inc = 2
        inc2.set_id(id_nou_inc)
        inc2.set_client(client_nou_inc)
        inc2.set_carte(carte_nou_inc)
        assert(inc2.get_id() == id_nou_inc)
        assert(inc2.get_client() == client_nou_inc)
        assert(inc2.get_carte() == carte_nou_inc)
        assert(inc2.__eq__(inc1) == False)


    def __ruleaza_teste_validare(self):
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
        carte_invalida = Carte(id_carte_invalid,nume_carte_invalid,descriere_carte_invalid,autor_carte_invalid)
        try:
            self.__validare_carti.valideaza(carte_invalida)
            assert False
        except ValidError as ve:
            assert(str(ve) == "id invalid!\nnume invalid!\ndescriere invalida!\nautor invalid!\n")





        id_client = 1
        nume_client = "ab"
        CNP_client = "cd"
        client1 = Client(id_client,nume_client,CNP_client)
        self.__validare_clienti.valideaza(client1)
        id_client_invalid = -1
        nume_client_invalid = ""
        CNP_client_invalid = ""
        client_invalid = Client(id_client_invalid,nume_client_invalid,CNP_client_invalid)
        try:
            self.__validare_clienti.valideaza(client_invalid)
            assert False
        except ValidError as ve:
            assert(str(ve) == "id invalid!\nnume invalid!\nCNP invalid!\n")

        id_inc = 1
        client_inc = 1
        carte_inc = 1
        inc1 = Inchiriere(id_inc,client_inc,carte_inc)
        self.__validare_inchiriere.valideaza(inc1)
        id_inchiriere_invalid = -1
        client_inc_invalid = -1
        carte_inc_invalid = -1
        inc_invalid = Inchiriere(id_inchiriere_invalid,client_inc_invalid,carte_inc_invalid)
        try:
            self.__validare_inchiriere.valideaza(inc_invalid)
            assert False
        except ValidError as ve:
            assert(str(ve) == "id invalid!\nid client invalid!\nid carte invalid!\n")

    def __ruleaza_teste_repository(self):
        id_carte = 1
        nume_carte = "ab"
        descriere_carte = "cd"
        autor_carte = "ef"
        carte1 = Carte(id_carte,nume_carte,descriere_carte,autor_carte)
        self.__repo_carti.adauga(carte1)
        assert(self.__repo_carti.nr() == 1)
        lista_carti = self.__repo_carti.get_all()
        assert(len(lista_carti) == 1)
        assert(carte1.__eq__(lista_carti[0]) == True)
        acelasi_id = id_carte
        carte2 = Carte(acelasi_id,nume_carte,descriere_carte,autor_carte)
        try:
            self.__repo_carti.adauga(carte2)
            assert False
        except RepoError as re:
            assert(str(re) == "carte existenta!")
        assert(self.__repo_carti.nr() == 1)
        id_carte_2 = 2
        nume_carte_2 = "abc"
        descriere_carte_2 = "def"
        autor_carte_2 = "ghi"
        carte2 = Carte(id_carte_2,nume_carte_2,descriere_carte_2,autor_carte_2)
        self.__repo_carti.adauga(carte2)
        assert(self.__repo_carti.nr() == 2)
        lista_carti = self.__repo_carti.get_all()
        assert(len(lista_carti) == 2)
        assert(carte1.__eq__(lista_carti[0]) == True)
        assert(carte2.__eq__(lista_carti[1]) == True)
        id_carte_3 = 3
        nume_carte_3 = "abcd"
        descriere_carte_3 = "efgh"
        autor_carte_3 = "ijkl"
        carte3 = Carte(id_carte_3,nume_carte_3,descriere_carte_3,autor_carte_3)
        self.__repo_carti.adauga(carte3)
        assert(self.__repo_carti.nr() == 3)
        lista_carti = self.__repo_carti.get_all()
        assert(len(lista_carti) == 3)
        assert(carte1.__eq__(lista_carti[0]))
        assert(carte2.__eq__(lista_carti[1]))
        assert(carte3.__eq__(lista_carti[2]))
        clona_carte_3 =self.__repo_carti.cauta(id_carte_3)
        assert(clona_carte_3.get_id() == id_carte_3)
        assert(clona_carte_3.get_nume() == nume_carte_3)
        assert(clona_carte_3.get_descriere() == descriere_carte_3)
        assert(clona_carte_3.get_autor() == autor_carte_3)
        id_inexistent = 99
        try:
            carte_inexistenta = self.__repo_carti.cauta(id_inexistent)
            assert False
        except RepoError as re:
            assert(str(re) == "carte inexistenta!")
        nume_carte_3_nou = "a"
        descriere_carte_3_nou = "a"
        autor_carte_3_nou = "a"
        carte_modificata = Carte(id_carte_3,nume_carte_3_nou,descriere_carte_3_nou,autor_carte_3_nou)
        self.__repo_carti.modifica(carte_modificata)
        clona_carte_3 = self.__repo_carti.cauta(id_carte_3)
        assert(clona_carte_3.get_id() == id_carte_3)
        assert(clona_carte_3.get_nume() == nume_carte_3_nou)
        assert(clona_carte_3.get_descriere() == descriere_carte_3_nou)
        assert(clona_carte_3.get_autor() == autor_carte_3_nou)
        self.__repo_carti.sterge(id_carte_3)
        assert(self.__repo_carti.nr() == 2)
        lista_carti = self.__repo_carti.get_all()
        assert(carte1.__eq__(lista_carti[0]) == True)
        assert(carte2.__eq__(lista_carti[1]) == True)
        try:
            self.__repo_carti.modifica(carte_modificata)
            assert False
        except RepoError as re:
            assert(str(re) == "carte inexistenta!")
        try:
            self.__repo_carti.sterge(id_carte_3)
            assert False
        except RepoError as re:
            assert(str(re) == "carte inexistenta!")
        self.__repo_carti.sterge(id_carte_2)
        assert(self.__repo_carti.nr() == 1)
        self.__repo_carti.sterge(id_carte)
        assert(self.__repo_carti.nr() == 0)
        lista_carti = self.__repo_carti.get_all()
        assert(lista_carti == [])





        id_client = 1
        nume_client = "ab"
        CNP_client = "cd"
        client1 = Client(id_client,nume_client,CNP_client)
        self.__repo_clienti.adauga(client1)
        assert(self.__repo_clienti.nr() == 1)
        lista_clienti = self.__repo_clienti.get_all()
        assert(len(lista_clienti) == 1)
        assert(client1.__eq__(lista_clienti[0]) == True)
        acelasi_id = id_client
        client2 = Client(acelasi_id,nume_client,CNP_client)
        try:
            self.__repo_clienti.adauga(client2)
            assert False
        except RepoError as re:
            assert(str(re) == "client existent!")
        assert(self.__repo_clienti.nr() == 1)
        id_client_2 = 2
        nume_client_2 = "abc"
        CNP_client_2 = "def"
        client2 = Client(id_client_2,nume_client_2,CNP_client_2)
        self.__repo_clienti.adauga(client2)
        assert(self.__repo_clienti.nr() == 2)
        lista_clienti = self.__repo_clienti.get_all()
        assert(len(lista_clienti) == 2)
        assert(client1.__eq__(lista_clienti[0]) == True)
        assert(client2.__eq__(lista_clienti[1]) == True)
        id_client_3 = 3
        nume_client_3 = "abcd"
        CNP_client_3 = "efgh"
        client3 = Client(id_client_3,nume_client_3,CNP_client_3)
        self.__repo_clienti.adauga(client3)
        assert(self.__repo_clienti.nr() == 3)
        lista_clienti = self.__repo_clienti.get_all()
        assert(len(lista_clienti) == 3)
        assert(client1.__eq__(lista_clienti[0]))
        assert(client2.__eq__(lista_clienti[1]))
        assert(client3.__eq__(lista_clienti[2]))
        clona_client_3 =self.__repo_clienti.cauta(id_client_3)
        assert(clona_client_3.get_id() == id_client_3)
        assert(clona_client_3.get_nume() == nume_client_3)
        assert(clona_client_3.get_CNP() == CNP_client_3)
        id_inexistent = 99
        try:
            client_inexistent = self.__repo_clienti.cauta(id_inexistent)
            assert False
        except RepoError as re:
            assert(str(re) == "client inexistent!")
        nume_client_3_nou = "a"
        CNP_client_3_nou = "a"
        client_modificata = Client(id_client_3,nume_client_3_nou,CNP_client_3_nou)
        self.__repo_clienti.modifica(client_modificata)
        clona_client_3 = self.__repo_clienti.cauta(id_client_3)
        assert(clona_client_3.get_id() == id_client_3)
        assert(clona_client_3.get_nume() == nume_client_3_nou)
        assert(clona_client_3.get_CNP() == CNP_client_3_nou)
        self.__repo_clienti.sterge(id_client_3)
        assert(self.__repo_clienti.nr() == 2)
        lista_clienti = self.__repo_clienti.get_all()
        assert(client1.__eq__(lista_clienti[0]) == True)
        assert(client2.__eq__(lista_clienti[1]) == True)
        try:
            self.__repo_clienti.modifica(client_modificata)
            assert False
        except RepoError as re:
            assert(str(re) == "client inexistent!")
        try:
            self.__repo_clienti.sterge(id_client_3)
            assert False
        except RepoError as re:
            assert(str(re) == "client inexistent!")
        self.__repo_clienti.sterge(id_client_2)
        assert(self.__repo_clienti.nr() == 1)
        self.__repo_clienti.sterge(id_client)
        assert(self.__repo_clienti.nr() == 0)
        lista_clienti = self.__repo_clienti.get_all()
        assert(lista_clienti == [])




        id_inc1 = 1
        client_inc1 = 1
        carte_inc1 = 1
        inc1 = Inchiriere(id_inc1,client_inc1,carte_inc1)
        self.__repo_inchirieri.adauga(inc1)
        assert(self.__repo_inchirieri.nr() == 1)
        lista_inchirieri = self.__repo_inchirieri.get_all()
        assert(len(lista_inchirieri) == 1)
        assert(lista_inchirieri[0] == inc1)
        acelasi_id = id_inc1
        aceeasi_inc = Inchiriere(acelasi_id,client_inc1,carte_inc1)
        try:
            self.__repo_inchirieri.adauga(aceeasi_inc)
            assert False
        except RepoError as re:
            assert(str(re) == "inchiriere existenta!")
        assert(self.__repo_inchirieri.nr() == 1)
        id_inc2 = 2
        client_inc2 = 2
        carte_inc2 = 2
        inc2 = Inchiriere(id_inc2,client_inc2,carte_inc2)
        self.__repo_inchirieri.adauga(inc2)
        assert(self.__repo_inchirieri.nr() == 2)
        lista_inchirieri = self.__repo_inchirieri.get_all()
        assert(lista_inchirieri[0] == inc1)
        assert(lista_inchirieri[1] == inc2)
        clona_inc2 = self.__repo_inchirieri.cauta(id_inc2)
        assert(inc2.__eq__(clona_inc2) == True)
        id_inc3 = 3
        client_inc3 = 3
        carte_inc3 = 3
        inc3 = Inchiriere(id_inc3,client_inc3,carte_inc3)
        try:
            inc_inexistent = self.__repo_inchirieri.cauta(id_inc3)
            assert False
        except RepoError as re:
            assert(str(re) == "inchiriere inexistenta!")
        client_inc3_nou = 33
        carte_inc3_nou = 33
        inc_nou = Inchiriere(id_inc3,client_inc3_nou,carte_inc3_nou)
        try:
            self.__repo_inchirieri.modifica(inc_nou)
            assert False
        except RepoError as re:
            assert(str(re) == "inchiriere inexistenta!")
        self.__repo_inchirieri.adauga(inc3)
        assert(self.__repo_inchirieri.nr() == 3)
        lista_inchirieri = self.__repo_inchirieri.get_all()
        assert(inc1.__eq__(lista_inchirieri[0]))
        assert(inc2.__eq__(lista_inchirieri[1]))
        assert(inc3.__eq__(lista_inchirieri[2]))
        self.__repo_inchirieri.modifica(inc_nou)
        clona_inc_nou = self.__repo_inchirieri.cauta(id_inc3)
        assert(clona_inc_nou.get_id() == id_inc3)
        assert(clona_inc_nou.get_client() == client_inc3_nou)
        assert(clona_inc_nou.get_carte() == carte_inc3_nou)
        id_inexistent = -1
        try:
            self.__repo_inchirieri.sterge(id_inexistent)
            assert False
        except RepoError as re:
            assert(str(re) == "inchiriere inexistenta!")
        self.__repo_inchirieri.sterge(id_inc3)
        assert(self.__repo_inchirieri.nr() == 2)
        try:
            inc3_sters = self.__repo_inchirieri.cauta(id_inc3)
            assert False
        except RepoError as re:
            assert(str(re) == "inchiriere inexistenta!")
        self.__repo_inchirieri.sterge(id_inc2)
        assert(self.__repo_inchirieri.nr() == 1)
        self.__repo_inchirieri.sterge(id_inc1)
        assert(self.__repo_inchirieri.nr() == 0)
        lista_inchirieri = self.__repo_inchirieri.get_all()
        assert(lista_inchirieri == [])


    def __ruleaza_teste_service(self):
        id_carte = 1
        nume_carte = "ab"
        descriere_carte = "cd"
        autor_carte = "ef"
        carte1 = Carte(id_carte, nume_carte, descriere_carte, autor_carte)
        self.__service_carti.adauga(id_carte,nume_carte,descriere_carte,autor_carte)
        assert (self.__service_carti.nr() == 1)
        lista_carti = self.__service_carti.get_all()
        assert (len(lista_carti) == 1)
        assert (carte1.__eq__(lista_carti[0]) == True)
        acelasi_id = id_carte
        carte2 = Carte(acelasi_id, nume_carte, descriere_carte, autor_carte)
        try:
            self.__service_carti.adauga(acelasi_id,nume_carte,descriere_carte,autor_carte)
            assert False
        except RepoError as re:
            assert (str(re) == "carte existenta!")
        assert (self.__service_carti.nr() == 1)
        id_carte_2 = 2
        nume_carte_2 = "abc"
        descriere_carte_2 = "def"
        autor_carte_2 = "ghi"
        carte2 = Carte(id_carte_2, nume_carte_2, descriere_carte_2, autor_carte_2)
        self.__service_carti.adauga(id_carte_2,nume_carte_2,descriere_carte_2,autor_carte_2)
        assert (self.__service_carti.nr() == 2)
        lista_carti = self.__service_carti.get_all()
        assert (len(lista_carti) == 2)
        assert (carte1.__eq__(lista_carti[0]) == True)
        assert (carte2.__eq__(lista_carti[1]) == True)
        id_carte_3 = 3
        nume_carte_3 = "abcd"
        descriere_carte_3 = "efgh"
        autor_carte_3 = "ijkl"
        carte3 = Carte(id_carte_3, nume_carte_3, descriere_carte_3, autor_carte_3)
        self.__service_carti.adauga(id_carte_3,nume_carte_3,descriere_carte_3,autor_carte_3)
        assert (self.__service_carti.nr() == 3)
        lista_carti = self.__service_carti.get_all()
        assert (len(lista_carti) == 3)
        assert (carte1.__eq__(lista_carti[0]))
        assert (carte2.__eq__(lista_carti[1]))
        assert (carte3.__eq__(lista_carti[2]))
        clona_carte_3 = self.__service_carti.cauta(id_carte_3)
        assert (clona_carte_3.get_id() == id_carte_3)
        assert (clona_carte_3.get_nume() == nume_carte_3)
        assert (clona_carte_3.get_descriere() == descriere_carte_3)
        assert (clona_carte_3.get_autor() == autor_carte_3)
        id_inexistent = 99
        try:
            carte_inexistenta = self.__service_carti.cauta(id_inexistent)
            assert False
        except RepoError as re:
            assert (str(re) == "carte inexistenta!")
        nume_carte_3_nou = "a"
        descriere_carte_3_nou = "a"
        autor_carte_3_nou = "a"
        carte_modificata = Carte(id_carte_3, nume_carte_3_nou, descriere_carte_3_nou, autor_carte_3_nou)
        self.__service_carti.modifica(id_carte_3,nume_carte_3_nou,descriere_carte_3_nou,autor_carte_3_nou)
        clona_carte_3 = self.__service_carti.cauta(id_carte_3)
        assert (clona_carte_3.get_id() == id_carte_3)
        assert (clona_carte_3.get_nume() == nume_carte_3_nou)
        assert (clona_carte_3.get_descriere() == descriere_carte_3_nou)
        assert (clona_carte_3.get_autor() == autor_carte_3_nou)
        self.__service_inchirieri.sterge_carte(id_carte_3)
        assert (self.__service_carti.nr() == 2)
        lista_carti = self.__service_carti.get_all()
        assert (carte1.__eq__(lista_carti[0]) == True)
        assert (carte2.__eq__(lista_carti[1]) == True)
        try:
            self.__service_carti.modifica(id_carte_3,nume_carte_3_nou,descriere_carte_3_nou,autor_carte_3_nou)
            assert False
        except RepoError as re:
            assert (str(re) == "carte inexistenta!")
        try:
            self.__service_inchirieri.sterge_carte(id_carte_3)
            assert False
        except RepoError as re:
            assert (str(re) == "carte inexistenta!")
        self.__service_inchirieri.sterge_carte(id_carte_2)
        assert (self.__service_carti.nr() == 1)
        self.__service_inchirieri.sterge_carte(id_carte)
        assert (self.__service_carti.nr() == 0)
        lista_carti = self.__service_carti.get_all()
        assert (lista_carti == [])


        id_client = 1
        nume_client = "ab"
        CNP_client = "cd"
        client1 = Client(id_client, nume_client, CNP_client)
        self.__service_clienti.adauga(id_client,nume_client,CNP_client)
        assert (self.__service_clienti.nr() == 1)
        lista_clienti = self.__service_clienti.get_all()
        assert (len(lista_clienti) == 1)
        assert (client1.__eq__(lista_clienti[0]) == True)
        acelasi_id = id_client
        client2 = Client(acelasi_id, nume_client, CNP_client)
        try:
            self.__service_clienti.adauga(acelasi_id,nume_client,CNP_client)
            assert False
        except RepoError as re:
            assert (str(re) == "client existent!")
        assert (self.__service_clienti.nr() == 1)
        id_client_2 = 2
        nume_client_2 = "abc"
        CNP_client_2 = "def"
        client2 = Client(id_client_2, nume_client_2, CNP_client_2)
        self.__service_clienti.adauga(id_client_2,nume_client_2,CNP_client_2)
        assert (self.__service_clienti.nr() == 2)
        lista_clienti = self.__service_clienti.get_all()
        assert (len(lista_clienti) == 2)
        assert (client1.__eq__(lista_clienti[0]) == True)
        assert (client2.__eq__(lista_clienti[1]) == True)
        id_client_3 = 3
        nume_client_3 = "abcd"
        CNP_client_3 = "efgh"
        client3 = Client(id_client_3, nume_client_3, CNP_client_3)
        self.__service_clienti.adauga(id_client_3,nume_client_3,CNP_client_3)
        assert (self.__service_clienti.nr() == 3)
        lista_clienti = self.__service_clienti.get_all()
        assert (len(lista_clienti) == 3)
        assert (client1.__eq__(lista_clienti[0]))
        assert (client2.__eq__(lista_clienti[1]))
        assert (client3.__eq__(lista_clienti[2]))
        clona_client_3 = self.__service_clienti.cauta(id_client_3)
        assert (clona_client_3.get_id() == id_client_3)
        assert (clona_client_3.get_nume() == nume_client_3)
        assert (clona_client_3.get_CNP() == CNP_client_3)
        id_inexistent = 99
        try:
            client_inexistent = self.__service_clienti.cauta(id_inexistent)
            assert False
        except RepoError as re:
            assert (str(re) == "client inexistent!")
        nume_client_3_nou = "a"
        CNP_client_3_nou = "a"
        client_modificata = Client(id_client_3, nume_client_3_nou, CNP_client_3_nou)
        self.__service_clienti.modifica(id_client_3,nume_client_3_nou,CNP_client_3_nou)
        clona_client_3 = self.__service_clienti.cauta(id_client_3)
        assert (clona_client_3.get_id() == id_client_3)
        assert (clona_client_3.get_nume() == nume_client_3_nou)
        assert (clona_client_3.get_CNP() == CNP_client_3_nou)
        self.__service_inchirieri.sterge_client(id_client_3)
        assert (self.__service_clienti.nr() == 2)
        lista_clienti = self.__service_clienti.get_all()
        assert (client1.__eq__(lista_clienti[0]) == True)
        assert (client2.__eq__(lista_clienti[1]) == True)
        try:
            self.__service_clienti.modifica(id_client_3,nume_client_3_nou,CNP_client_3_nou)
            assert False
        except RepoError as re:
            assert (str(re) == "client inexistent!")
        try:
            self.__service_inchirieri.sterge_client(id_client_3)
            assert False
        except RepoError as re:
            assert (str(re) == "client inexistent!")
        self.__service_inchirieri.sterge_client(id_client_2)
        assert (self.__service_clienti.nr() == 1)
        self.__service_inchirieri.sterge_client(id_client)
        assert (self.__service_clienti.nr() == 0)
        lista_clienti = self.__service_clienti.get_all()
        assert (lista_clienti == [])





        id_client = 1
        nume_client = "ab"
        CNP_client = "cd"
        client1 = Client(id_client, nume_client, CNP_client)
        self.__service_clienti.adauga(id_client,nume_client,CNP_client)
        id_carte = 1
        nume_carte = "ab"
        descriere_carte = "cd"
        autor_carte = "ef"
        carte1 = Carte(id_carte, nume_carte, descriere_carte, autor_carte)
        self.__service_carti.adauga(id_carte, nume_carte, descriere_carte, autor_carte)
        id_inc = 1
        self.__service_inchirieri.adauga(id_inc,id_client,id_carte)
        assert(self.__service_inchirieri.nr() == 1)
        lista_inchirieri = self.__service_inchirieri.get_all()
        assert(len(lista_inchirieri) == 1)
        inc1 = Inchiriere(id_inc,id_client,id_carte)
        assert(inc1.__eq__(lista_inchirieri[0]) == True)
        acelasi_id = id_inc
        aceeasi_inc = Inchiriere(acelasi_id,id_client,id_carte)
        try:
            self.__service_inchirieri.adauga(acelasi_id,id_client,id_carte)
            assert False
        except RepoError as re:
            assert(str(re) == "inchiriere existenta!")
        assert(self.__service_inchirieri.nr() == 1)
        id_client_2 = 2
        nume_client_2 = "abc"
        CNP_client_2 = "def"
        client2 = Client(id_client_2, nume_client_2, CNP_client_2)
        self.__service_clienti.adauga(id_client_2,nume_client_2,CNP_client_2)
        id_carte_2 = 2
        nume_carte_2 = "abc"
        descriere_carte_2 = "def"
        autor_carte_2 = "ghi"
        carte2 = Carte(id_carte_2, nume_carte_2, descriere_carte_2, autor_carte_2)
        self.__service_carti.adauga(id_carte_2, nume_carte_2, descriere_carte_2, autor_carte_2)
        id_inc2 = 2
        inc2 = Inchiriere(id_inc2,id_client_2,id_carte_2)
        self.__service_inchirieri.adauga(id_inc2,id_client_2,id_carte_2)
        assert(self.__service_inchirieri.nr() == 2)
        lista_inchirieri = self.__service_inchirieri.get_all()
        assert(inc1.__eq__(lista_inchirieri[0]) == True)
        assert(inc2.__eq__(lista_inchirieri[1]) == True)
        assert(len(lista_inchirieri) == 2)
        id_client_3 = 3
        nume_client_3 = "abcd"
        CNP_client_3 = "efgh"
        client3 = Client(id_client_3, nume_client_3, CNP_client_3)
        self.__service_clienti.adauga(id_client_3,nume_client_3,CNP_client_3)
        id_carte_3 = 3
        nume_carte_3 = "abcd"
        descriere_carte_3 = "efgh"
        autor_carte_3 = "ijkl"
        carte3 = Carte(id_carte_3, nume_carte_3, descriere_carte_3, autor_carte_3)
        self.__service_carti.adauga(id_carte_3, nume_carte_3, descriere_carte_3, autor_carte_3)
        id_inc3 = 3
        inc3 = Inchiriere(id_inc3,id_client_3,id_carte_3)
        self.__service_inchirieri.adauga(id_inc3,id_client_3,id_carte_3)
        assert(self.__service_inchirieri.nr() == 3)
        lista_inchirieri = self.__service_inchirieri.get_all()
        assert(inc1.__eq__(lista_inchirieri[0]) == True)
        assert(inc2.__eq__(lista_inchirieri[1]) == True)
        assert(inc3.__eq__(lista_inchirieri[2]) == True)
        clona_inc_3 = self.__service_inchirieri.cauta(id_inc3)
        assert (clona_inc_3.get_id() == id_inc3)
        assert (clona_inc_3.get_client() == id_client_3)
        assert (clona_inc_3.get_carte() == id_carte_3)

        id_inexistent = 99
        try:
            inc_inexistent = self.__service_inchirieri.cauta(id_inexistent)
            assert False
        except RepoError as re:
            assert (str(re) == "inchiriere inexistenta!")

        id_client_3_nou = 1
        id_carte_3_nou = 1
        inc_modificata = Inchiriere(id_inc3, id_client_3_nou, id_carte_3_nou)
        self.__service_inchirieri.modifica(id_inc3,id_client_3_nou,id_carte_3_nou)
        clona_inc3 = self.__service_inchirieri.cauta(id_inc3)
        assert (clona_inc3.get_id() == id_inc3)
        assert (clona_inc3.get_client() == id_client_3_nou)
        assert (clona_inc3.get_carte() == id_carte_3_nou)
        self.__service_inchirieri.sterge(id_inc3)
        assert (self.__service_inchirieri.nr() == 2)
        lista_inchirieri = self.__service_inchirieri.get_all()
        assert(inc1.__eq__(lista_inchirieri[0]) == True)
        assert(inc2.__eq__(lista_inchirieri[1]) == True)
        try:
            self.__service_inchirieri.modifica(id_inc3,id_client_3_nou,id_carte_3_nou)
            assert False
        except RepoError as re:
            assert (str(re) == "inchiriere inexistenta!")
        try:
            self.__service_inchirieri.sterge(id_inc3)
            assert False
        except RepoError as re:
            assert (str(re) == "inchiriere inexistenta!")
        self.__service_inchirieri.sterge(id_inc2)
        assert (self.__service_inchirieri.nr() == 1)
        self.__service_inchirieri.sterge(id_inc)
        assert (self.__service_inchirieri.nr() == 0)
        lista_inchirieri = self.__service_inchirieri.get_all()
        assert (lista_inchirieri == [])
        self.__service_inchirieri.sterge_carte(1)
        self.__service_inchirieri.sterge_carte(2)
        self.__service_inchirieri.sterge_carte(3)
        self.__service_inchirieri.sterge_client(1)
        self.__service_inchirieri.sterge_client(2)
        self.__service_inchirieri.sterge_client(3)
        try:
            self.__service_inchirieri.adauga(1,1,1)
            assert False
        except RepoError as re:
            assert(str(re) == "client inexistent!")
        self.__service_clienti.adauga(1,"a","b")

        try:
            self.__service_inchirieri.adauga(1,1,1)
            assert False
        except RepoError as re:
            assert(str(re) == "carte inexistenta!")
        self.__service_inchirieri.sterge_client(1)
        assert (self.__service_carti.nr() == 0)
        assert (self.__service_clienti.nr() == 0)
        assert (self.__service_inchirieri.nr() == 0)
#  TESTE CLIENTI_CARTI_NR SI CLIENTI_CARTI_NUME CAND NU SUNT ENTITATI IN LISTA ------------------------------------------
        clienti_carti_nume = self.__service_inchirieri.rap_clienti_carti_nume()
        assert(clienti_carti_nume == [])
        clienti_carti_nr = self.__service_inchirieri.rap_clienti_carti_nr()
        assert(clienti_carti_nr == [])
        top_carti = self.__service_inchirieri.rap_top_carti()
        assert(top_carti == [])
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
        assert(len(top_carti) == 3)
        carte1 = self.__service_carti.cauta(1)
        carte2 = self.__service_carti.cauta(2)
        carte3 = self.__service_carti.cauta(3)
        assert(carte1.__eq__(top_carti[0]) == True)
        assert(carte2.__eq__(top_carti[1]) == True)
        assert(carte3.__eq__(top_carti[2]) == True)
        top_20_clienti = self.__service_inchirieri.rap_20_clienti()
        assert(top_20_clienti == [])
        self.__service_clienti.adauga(4,"d","d")
        self.__service_clienti.adauga(5, "e", "e")
        self.__service_clienti.adauga(6, "sase", "sase")
        self.__service_inchirieri.adauga(7,4,1)
        self.__service_inchirieri.adauga(8, 4, 2)
        self.__service_inchirieri.adauga(9, 5, 3)
        self.__service_inchirieri.adauga(10, 6, 1)
        self.__service_inchirieri.adauga(11, 6, 2)
        self.__service_inchirieri.adauga(12, 6, 3)
        top_20_clienti = self.__service_inchirieri.rap_20_clienti()
        assert(len(top_20_clienti) == 1)
        assert(top_20_clienti[0].get_nume() == "sase")
        assert(top_20_clienti[0].get_nr() == 3)
        clienti_carti_nume = self.__service_inchirieri.rap_clienti_carti_nume()
        assert(len(clienti_carti_nume) == 6)
        assert(clienti_carti_nume[0].get_nume() == "a")
        assert (clienti_carti_nume[1].get_nume() == "a")
        assert (clienti_carti_nume[2].get_nume() == "a")
        assert (clienti_carti_nume[3].get_nume() == "d")
        assert (clienti_carti_nume[4].get_nume() == "e")
        assert (clienti_carti_nume[5].get_nume() == "sase")
        clienti_carti_nr = self.__service_inchirieri.rap_clienti_carti_nr()
        assert(len(clienti_carti_nr) == 6)
        assert (clienti_carti_nr[0].get_nr() == 3)
        assert (clienti_carti_nr[1].get_nr() == 2)
        assert (clienti_carti_nr[2].get_nr() == 2)
        assert (clienti_carti_nr[3].get_nr() == 2)
        assert (clienti_carti_nr[4].get_nr() == 2)
        assert (clienti_carti_nr[5].get_nr() == 1)




    def run(self):
        self.__ruleaza_teste_domain()
        print("DOMAIN TEST - OK")
        self.__ruleaza_teste_validare()
        print("VALIDATION TEST - OK")
        self.__ruleaza_teste_repository()
        print("REPOSITORY TEST - OK")
        self.__ruleaza_teste_service()
        print("SERVICE TEST - OK")
