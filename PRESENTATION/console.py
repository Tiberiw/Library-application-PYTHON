from ERRORS.repo_error import RepoError
from ERRORS.valid_error import ValidError


class UI:

    def __init__(self,service_carti,service_clienti,service_inchirieri):
        self.__service_carti = service_carti
        self.__service_clienti = service_clienti
        self.__service_inchirieri = service_inchirieri
        self.__comenzi = {
            "add_carte" : self.__ui_add_carte,
            "add_client" : self.__ui_add_client,
            "add_inchiriere" : self.__ui_add_inchiriere,
            "del_carte" : self.__ui_del_carte,
            "del_client" : self.__ui_del_client,
            "del_inchiriere" : self.__ui_del_inchiriere,
            "modif_carte" : self.__ui_modif_carte,
            "modif_client" : self.__ui_modif_client,
            "modif_inchiriere" : self.__ui_modif_inchiriere,
            "search_carte" : self.__ui_search_carte,
            "search_client" : self.__ui_search_client,
            "search_inchiriere" : self.__ui_search_inchiriere,
            "print_carti" : self.__ui_print_carti,
            "print_clienti" : self.__ui_print_clienti,
            "print_inchirieri" : self.__ui_print_inchirieri,
            "nr_carti" : self.__ui_nr_carti,
            "nr_clienti" : self.__ui_nr_clienti,
            "nr_inchirieri" : self.__ui_nr_inchirieri,
            "top_carti" : self.__ui_top_carti,
            "add_carti_random" : self.__ui_add_carti_random,
            "add_clienti_random" : self.__ui_add_clienti_random,
            "20%_clienti" : self.__ui_20_clienti,
            "clienti_carti_nume" : self.__ui_clienti_carti_nume,
            "clienti_carti_nr" : self.__ui_clienti_carti_nr,
            "carti_litera" : self.__ui_carti_litera

        }

    def __ui_add_carti_random(self,params):
        '''
        adauga carti random in lista
        :param params: int
        :return: list
        '''
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        nr = int(params[0])
        self.__service_carti.adauga_random(nr)
        print(f"{nr} carti adaugate cu succes!")
        pass

    def __ui_add_clienti_random(self,params):
        '''
        adauga clienti random in lista
        :param params: int
        :return: list
        '''
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        nr = int(params[0])
        self.__service_clienti.adauga_random(nr)
        print(f"{nr} clienti au fost adaugati cu succes!")
        pass

    def __ui_add_carte(self,params):
        '''
        adauga o carte in lista
        :param params: id nume descriere carte
        :return: -
        '''
        if len(params) != 4:
            print("Sunt necesari 4 parametri!")
            return
        if params[0].isdigit() == False:
            raise ValueError

        id = int(params[0])
        nume = params[1]
        descriere = params[2]
        autor = params[3]
        self.__service_carti.adauga(id,nume,descriere,autor)
        print("Carte adaugata cu succes!")

    def __ui_add_client(self,params):
        '''
        adauga un client in lista
        :param params: int nume CNP
        :return:
        '''
        if len(params) != 3:
            print("Sunt necesari 3 parametri!")
            return
        if params[0].isdigit() == False:
            raise ValueError

        id = int(params[0])
        nume = params[1]
        CNP = params[2]
        self.__service_clienti.adauga(id,nume,CNP)
        print("Client adaugat cu succes!")

    def __ui_add_inchiriere(self,params):
        '''
        adauga o inchiriere in lista.
        :param params: int int int
        :return:
        '''
        if len(params) != 3:
            print("Sunt necesari 3 parametri!")
            return
        if params[0].isdigit() == False or params[1].isdigit() == False or params[2].isdigit() == False:
            raise ValueError
        id = int(params[0])
        client = int(params[1])
        carte = int(params[2])
        self.__service_inchirieri.adauga(id,client,carte)
        print("Inchiriere adaugata!")

    def __ui_del_carte(self,params):
        '''
        sterge o carte din lista
        :param params: int
        :return: -
        '''
        if len(params) != 1:
            print("Este necesar un parametru!")
            return
        if params[0].isdigit() == False:
            raise ValueError

        id = int(params[0])
        self.__service_inchirieri.sterge_carte(id)
        print(f"Cartea cu id {id} stearsa cu succes!")

    def __ui_del_client(self,params):
        '''
        sterge un client din lista
        :param params: int
        :return: -
        '''
        if len(params) != 1:
            print("Este necesar un parametru!")
            return
        if params[0].isdigit() == False:
            raise ValueError

        id = int(params[0])
        self.__service_inchirieri.sterge_client(id)
        print(f"Clientul cu id {id} sters cu succes!")

    def __ui_del_inchiriere(self,params):
        '''
        sterge o inchiriere din lista
        :param params: int
        :return: -
        '''
        if len(params) != 1:
            print("Este necesar un parametru!")
            return
        if params[0].isdigit() == False:
            raise ValueError

        id = int(params[0])
        self.__service_inchirieri.sterge(id)
        print(f"Inchirierea cu id {id} stearsa cu succes!")

    def __ui_modif_carte(self,params):
        '''
        modifica o carte din lista
        :param params: int str str str
        :return: -
        '''
        if len(params) != 4:
            print("Sunt necesari 4 parametri!")
            return
        if params[0].isdigit() == False:
            raise ValueError

        id = int(params[0])
        nume = params[1]
        descriere = params[2]
        autor = params[3]
        self.__service_carti.modifica(id,nume,descriere,autor)
        print("Cartea a fost modificata!")

    def __ui_modif_client(self,params):
        if len(params) != 3:
            print("Sunt necesari 3 parametri!")
            return
        if params[0].isdigit() == False:
            raise ValueError
        id = int(params[0])
        nume = params[1]
        CNP = params[2]
        self.__service_clienti.modifica(id,nume,CNP)
        print("Clientul a fost modificat!")

    def __ui_modif_inchiriere(self,params):
        if len(params) != 3:
            print("Sunt necesari 3 parametri!")
            return
        if params[0].isdigit() == False or params[1].isdigit() == False or params[2].isdigit() == False:
            raise ValueError
        id = int(params[0])
        client = int(params[1])
        carte = int(params[2])
        self.__service_inchirieri.modifica(id,client,carte)
        print("Inchirierea a fost modificata!")

    def __ui_search_carte(self,params):
        if len(params) != 1:
            print("Este necesar un parametru!")
            return
        if params[0].isdigit() == False:
            raise ValueError
        id = int(params[0])
        carte = self.__service_carti.cauta(id)
        print(carte)

    def __ui_search_client(self,params):
        if len(params) != 1:
            print("Este necesar un parametru!")
            return
        if params[0].isdigit() == False:
            raise ValueError
        id = int(params[0])
        client = self.__service_clienti.cauta(id)
        print(client)

    def __ui_search_inchiriere(self,params):
        if len(params) != 1:
            print("Este necesar un parametru!")
            return
        if params[0].isdigit() == False:
            raise ValueError
        id = int(params[0])
        inscriere = self.__service_inchirieri.cauta(id)
        print(inscriere)


    def __ui_print_carti(self,params):
        if len(params) != 0:
            print("Nu sunt necesari parametri!")
        lista_carti = self.__service_carti.get_all()
        if len(lista_carti) == 0:
            print("Nu exista carti!")
            return
        for carte in lista_carti:
            print(carte)

    def __ui_print_clienti(self,params):
        if len(params) != 0:
            print("Nu sunt necesari parametri!")
        lista_clienti = self.__service_clienti.get_all()
        if len(lista_clienti) == 0:
            print("Nu exista clienti!")
            return
        for client in lista_clienti:
            print(client)

    def __ui_print_inchirieri(self,params):
        if len(params) != 0:
            print("Nu sunt necesari parametri!")
        lista_inchirieri = self.__service_inchirieri.get_all()
        if len(lista_inchirieri) == 0:
            print("Nu exista inchirieri!")
            return
        for inc in lista_inchirieri:
            print(inc)

    def __ui_nr_carti(self,params):
        if len(params) != 0:
            print("Nu sunt necesari parametri!")
        nr = self.__service_carti.nr()
        if nr == 0:
            print("Nu exista carti!")
        elif nr == 1:
            print("Exista o carte")
        else:
            print(f"Exista {nr} carti")

    def __ui_nr_clienti(self,params):
        if len(params) != 0:
            print("Nu sunt necesari parametri!")
        nr = self.__service_clienti.nr()
        if nr == 0:
            print("Nu exista clienti!")
        elif nr == 1:
            print("Exista un client")
        else:
            print(f"Exista {nr} clienti")

    def __ui_nr_inchirieri(self,params):
        if len(params) != 0:
            print("Nu sunt necesari parametri!")
        nr = self.__service_inchirieri.nr()
        if nr == 0:
            print("Nu exista clienti!")
        elif nr == 1:
            print("Exista un client")
        else:
            print(f"Exista {nr} clienti")

    def __ui_top_carti(self,params):
        if len(params) != 0:
            print("Nu sunt necesari parametri!")
        top_carti = self.__service_inchirieri.rap_top_carti()
        if len(top_carti) == 0:
            print("Nu exista inchirieri!")
            return
        print("\tCele mai inchiriate carti:")
        for carte in top_carti:
            print(f"ID: {carte.get_id()}  NUME: {carte.get_nume()}  DESCRIERE: {carte.get_descriere()}  AUTOR:{carte.get_autor()}")

    def __ui_20_clienti(self,params):
        '''
        Afiseaza primii 20% dintre cei mai activi clienti : (nume client si numarul de carti inchiriate)
        :param params: -
        :return: -
        '''
        if len(params) != 0:
            print("Nu sunt necesari parametri!")
        clienti = self.__service_inchirieri.rap_20_clienti()
        if len(clienti) == 0:
            print("Nu exista inchirieri!")
            return
        print("\tTop 20% cei mai activi clienti:")
        for client in clienti:
            print(client)

    def __ui_clienti_carti_nume(self,params):
        '''
        Afiseaza clientii cu cartile inchiriate ordonati dupa nume
        :return:
        '''
        if len(params) != 0:
            print("Nu sunt necesari parametri!")
        clienti = self.__service_inchirieri.rap_clienti_carti_nume()
        if len(clienti) == 0:
            print("Nu exista inchirieri")
            return
        print("\tClienti cu carti inchiriate:")
        for client in clienti:
            print(client)

    def __ui_clienti_carti_nr(self,params):
        '''
        Afiseaza clientii cu carti inchiriate ordonati dupa nr de carti inchiriate
        :param params: -
        :return: -
        '''
        if len(params) != 0:
            print("Nu sunt necesari parametri!")
        clienti = self.__service_inchirieri.rap_clienti_carti_nr()
        if len(clienti) == 0:
            print("Nu exista inchirieri")
            return
        print("\tClienti cu carti inchiriate:")
        for client in clienti:
            print(client)


    def __ui_carti_litera(self,params):
        '''

        :param params:
        :return:
        '''
        if len(params) != 1:
            print("Un singur parametru necesar!")
            return

        initiala = params[0]
        lista_clienti = self.__service_inchirieri.get_clienti_litera(initiala)
        if len(lista_clienti) == 0:
            print(f"Nu exista clienti cu initiala {initiala}")
            return
        for client in lista_clienti:
            print(client)



    def run(self):

        while True:
            comanda = input(">>>")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parti = comanda.split()
            nume_comanda = parti[0]
            params = parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda](params)
                except ValueError:
                    print("ValueError : tip invalid!")
                except ValidError as ve:
                    print(f"ValidError : {ve} ")
                except RepoError as re:
                    print(f"RepoError : {re} ")
            else:
                print("Comanda invalida!")