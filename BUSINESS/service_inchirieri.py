from BUSINESS.sortari import Sortari
from DOMAIN.clienti_carti_DTO import Client_Carti
from DOMAIN.inchirieri import Inchiriere
from DOMAIN.clienti_20 import Client_20


class ServiceInchirieri:

    def __init__(self,validare_inchirieri,repo_inchirieri,repo_clienti,repo_carti):
        self.__validare_inchiriere = validare_inchirieri
        self.__repo_inchirieri = repo_inchirieri
        self.__repo_clienti = repo_clienti
        self.__repo_carti = repo_carti
        self.__sorter = Sortari()

    def adauga(self,id_inc,id_client,id_carte):
        '''
        adauga o inchiriere in lista de inchirieri
        :param id_inc: int
        :param id_client: int
        :param id_carte: int
        :return: -
        '''
        client = self.__repo_clienti.cauta(id_client)
        carte = self.__repo_carti.cauta(id_carte)
        inchiriere = Inchiriere(id_inc,id_client,id_carte)
        self.__validare_inchiriere.valideaza(inchiriere)
        self.__repo_inchirieri.adauga(inchiriere)

    def modifica(self,id_inc,id_client,id_carte):
        '''
        modifica o inchiriere din lista de inchirieri
        :param id_inc: int
        :param id_client: int
        :param id_carte: int
        :return: -
        '''
        client = self.__repo_clienti.cauta(id_client)
        carte = self.__repo_carti.cauta(id_carte)
        inchiriere = Inchiriere(id_inc,id_client,id_carte)
        self.__validare_inchiriere.valideaza(inchiriere)
        self.__repo_inchirieri.modifica(inchiriere)

    def sterge(self,id_inc):
        '''
        sterge o inchiriere din lista de inchirieri
        :param id_inc: int
        :return:
        '''
        self.__repo_inchirieri.sterge(id_inc)

    def cauta(self,id_inc):
        '''
        cauta o inchiriere din lista de inchirieri
        :param id_inc: int
        :return: inchiriere
        '''
        return self.__repo_inchirieri.cauta(id_inc)

    def get_all(self):
        '''
        returneaza o lista cu toate inchirierile
        :return: list
        '''
        return self.__repo_inchirieri.get_all()

    def nr(self):
        '''
        returneaza numarul de inchirieri din lista
        :return: int
        '''
        return self.__repo_inchirieri.nr()

    def sterge_client(self,id_client):
        '''
        sterge un client si inchirierile lui
        :param id_client: int
        :return: -
        '''
        client = self.__repo_clienti.cauta(id_client)
        lista_inchirieri = self.__repo_inchirieri.get_all()
        inchirieri_client = []
        for inchiriere in lista_inchirieri:
            if inchiriere.get_client() == id_client:
                inchirieri_client.append(inchiriere)
        for inchiriere in inchirieri_client:
            self.__repo_inchirieri.sterge(inchiriere.get_id())
        self.__repo_clienti.sterge(id_client)

    def sterge_carte(self,id_carte):
        '''
        sterge o carte si toate inchirierile sale
        :param id_carte: int
        :return: -
        '''
        carte = self.__repo_carti.cauta(id_carte)
        lista_inchirieri = self.__repo_inchirieri.get_all()
        inchirieri_carte = []
        for inchiriere in lista_inchirieri:
            if inchiriere.get_carte() == id_carte:
                inchirieri_carte.append(inchiriere)
        for inchiriere in inchirieri_carte:
            self.__repo_inchirieri.sterge(inchiriere.get_id())
        self.__repo_carti.sterge(id_carte)

    def rap_top_carti(self):
        #raport cu cele mai imprumutate carti. Afiseaza cartile in ordine descrescatoare
        #:return: list
        inchirieri = self.__repo_inchirieri.get_all()
        carti = {}
        for inchiriere in inchirieri:
            if inchiriere.get_carte() not in carti:
                carti[inchiriere.get_carte()] = 1
            else:
                carti[inchiriere.get_carte()] += 1
        #==========================================================================
        carti_sortate = self.__sorter.BubbleSort(list(carti.items()),"1",True)
        #carti_sortate = sorted(carti.items(), key=lambda kv: kv[1], reverse=True)
        #===========================================================================
        top = []
        for carti in carti_sortate:
            top.append(self.__repo_carti.cauta(carti[0]))

        #top.sort(key=lambda x:x.get_nume())
        return top


   # def rap_top_carti(self,toate_inchirierile = self.__repo_inchirieri.get_all()):


    #def rap_top_carti_rec(self):


    def rap_20_clienti(self):
        '''
        raport cu top 20% cei mai activi clienti. Returneaza o lista cu clientii. Daca nu sunt cel putin 5 clienti cu inchirieri
        va returna lista goala
        :return: list
        '''
        info_clienti = {}
        clienti_20 = []
        inchirieri = self.__repo_inchirieri.get_all()
        for inchiriere in inchirieri:
            id_client_inchiriere = inchiriere.get_client()
            if id_client_inchiriere not in info_clienti:
                info_clienti[id_client_inchiriere] = 1
            else:
                info_clienti[id_client_inchiriere] += 1

        for id_client in info_clienti:
            client = self.__repo_clienti.cauta(id_client)
            client_20_dto = Client_20(client.get_nume(),info_clienti[id_client])
            clienti_20.append(client_20_dto)
        '''
        ================================================
        '''
        clienti_20_sortati = self.__sorter.ShellSort(clienti_20,"<","nume",True)
        #clienti_20.sort(key = lambda x:x.get_nume())
        #clienti_20.sort(reverse = True)
        clienti_20 = clienti_20_sortati
        '''
        ==============================================
        '''
        len_clienti_20 = len(clienti_20)
        len_clienti_20 = int(len_clienti_20*1/5)
        return clienti_20[:len_clienti_20]

    def rap_clienti_carti_nr(self):
        '''
        returneaza clientii cu carti inchiriate ordonati dupa numarul de carti
        :return: list
        '''
        info_clienti = {}
        clienti_20 = []
        inchirieri = self.__repo_inchirieri.get_all()
        for inchiriere in inchirieri:
            id_client_inchiriere = inchiriere.get_client()
            if id_client_inchiriere not in info_clienti:
                info_clienti[id_client_inchiriere] = 1
            else:
                info_clienti[id_client_inchiriere] += 1

        for id_client in info_clienti:
            client = self.__repo_clienti.cauta(id_client)
            client_20_dto = Client_20(client.get_nume(),info_clienti[id_client])
            clienti_20.append(client_20_dto)
        '''
        ================================================
        '''
        clienti_20_sortati = self.__sorter.BubbleSort(clienti_20, "nr", True)
        # clienti_20.sort(reverse = True)
        clienti_20 = clienti_20_sortati
        '''
        ==============================================
        '''

        return clienti_20

    '''
     def rap_clienti_carti_nume(self):
        
        #returneaza clientii cu carti inchiriate ordonati dupa nume
        #:return: list
        
        info_clienti = {}
        clienti_20 = []
        inchirieri = self.__repo_inchirieri.get_all()
        for inchiriere in inchirieri:
            id_client_inchiriere = inchiriere.get_client()
            if id_client_inchiriere not in info_clienti:
                info_clienti[id_client_inchiriere] = 1
            else:
                info_clienti[id_client_inchiriere] += 1

        for id_client in info_clienti:
            client = self.__repo_clienti.cauta(id_client)
            client_20_dto = Client_20(client.get_nume(),info_clienti[id_client])
            clienti_20.append(client_20_dto)
        
        #================================================
        
        clienti_20_sortati = self.__sorter.ShellSort(clienti_20, "nume")
        # clienti_20.sort(reverse = True)
        clienti_20 = clienti_20_sortati
        
        #==============================================
        
        return clienti_20_sortati
    '''

    def rap_clienti_carti_nume(self):

        toate_inchirierile = self.__repo_inchirieri.get_all()
        info_clienti = {}
        clienti_dto = []

        self.rap_clienti_carti_nume_rec1(toate_inchirierile,info_clienti)

        for id_client in info_clienti:
            clienti_dto.append(info_clienti[id_client])

        solutie = self.__sorter.ShellSort(clienti_dto,"nume","nr",False)

        return solutie

    def rap_clienti_carti_nume_rec1(self,toate_inchirierile,info_clienti):

        if toate_inchirierile == []:
            return

        inchiriere = toate_inchirierile[0]
        id_client = inchiriere.get_client()
        client = self.__repo_clienti.cauta(id_client)
        if id_client not in info_clienti:
            client_dto = Client_20(client.get_nume(),1)
            info_clienti[id_client] = client_dto
        else:
            client_dt0 = info_clienti[id_client]
            nr_carti = client_dt0.get_nr()
            new_cl = Client_20(client.get_nume(),nr_carti+1)
            info_clienti[id_client] = new_cl

        return self.rap_clienti_carti_nume_rec1(toate_inchirierile[1:],info_clienti)



    '''
    
    
    '''
    def get_clienti_litera(self,litera):
        #returneaza o lista cu toti clientii ce detin inchirieri si initiala numelui este "litera"
        #:param litera:
        #:return:

        inchirieri = self.__repo_inchirieri.get_all()
        info_clienti = {}
        for inchiriere in inchirieri:
            id_client = inchiriere.get_client()
            if id_client not in info_clienti:
                info_clienti[id_client] = inchiriere.get_carte()

        lista = []
        for id_client in info_clienti:
            client = self.__repo_clienti.cauta(id_client)
            carte = self.__repo_carti.cauta(info_clienti[id_client])
            nume_carte = carte.get_nume()
            if nume_carte[0] == litera:
                lista.append(client)

        return lista






