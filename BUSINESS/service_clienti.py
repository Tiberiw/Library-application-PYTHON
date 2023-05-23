from DOMAIN.clienti import Client
import random
import string

from ERRORS.repo_error import RepoError


class ServiceClienti:

    def __init__(self,validare_clienti,repo_clienti):
        self.__validare_client = validare_clienti
        self.__repo_clienti = repo_clienti

    def adauga(self,id,nume,CNP):
        '''
        adauga un client in lista de clienti
        :param id: int
        :param nume: str
        :param CNP: str
        :return: -
        '''
        client = Client(id,nume,CNP)
        self.__validare_client.valideaza(client)
        self.__repo_clienti.adauga(client)

    def adauga_random(self,nr):
        '''
        adauga random nr clienti in lista de clienti
        :param nr: int
        :return: -
        '''
        for i in range(nr):
            try:

                id = random.randint(1,2000)
                nume = ''.join(random.choice(string.ascii_letters) for i in range(5))
                CNP = ''.join(random.choice(string.ascii_letters) for i in range(5))
                client = Client(id,nume,CNP)
                self.__validare_client.valideaza(client)
                self.__repo_clienti.adauga(client)
            except RepoError as re:
                i = i - 1
                continue


    def cauta(self,id):
        '''
        cauta clientul cu id-ul id
        :param id: int
        :return: clinet
        '''
        return self.__repo_clienti.cauta(id)

    def modifica(self,id,nume,CNP):
        '''
        modifica clientul cu id-ul id. Modifica numele si CNP-ul
        :param id: int
        :param nume: str
        :param CNP: str
        :return: -
        '''
        client = Client(id,nume,CNP)
        self.__validare_client.valideaza(client)
        self.__repo_clienti.modifica(client)

    def get_all(self):
        '''
        returneaza o lista cu toti clientii adaugati
        :return: lista
        '''
        return self.__repo_clienti.get_all()

    def nr(self):
        '''
        returneaza numarul de clienti din lista
        :return: int
        '''
        return self.__repo_clienti.nr()
