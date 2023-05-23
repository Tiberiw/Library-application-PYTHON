import string
import random

from DOMAIN.carti import Carte
from ERRORS.repo_error import RepoError


class ServiceCarti:

    def __init__(self,validare_carti,repo_carti):
        self.__validare_carte = validare_carti
        self.__repo_carti = repo_carti


    def adauga(self,id,nume,descriere,autor):
        '''
        adauga o carte in lista de carti
        :param id: int
        :param nume: str
        :param descriere: str
        :param autor: str
        :return: -
        '''
        carte = Carte(id,nume,descriere,autor)
        self.__validare_carte.valideaza(carte)
        self.__repo_carti.adauga(carte)

    def cauta(self,id):
        '''
        cauta cartea cu id-ul id in lista de carti
        :param id: int
        :return: carte
        '''
        return self.__repo_carti.cauta(id)

    def modifica(self,id,nume,descriere,autor):
        '''
        modifica cartea cu id-ul id.
        :param id: int
        :param nume: str
        :param descriere: str
        :param autor: str
        :return:
        '''
        carte = Carte(id,nume,descriere,autor)
        self.__validare_carte.valideaza(carte)
        self.__repo_carti.modifica(carte)

    def get_all(self):
        '''
        returneaza o lista cu toate cartile
        :return: list
        '''
        return self.__repo_carti.get_all()

    def nr(self):
        '''
        returneaza numarul total de carti din lista
        :return: int
        '''
        return self.__repo_carti.nr()

    def adauga_random(self,nr):
        '''
        adauga random nr carti in lista
        :param nr: int
        :return:
        '''
        for i in range(nr):
            try:
                id = random.randint(1,2000)
                nume = ''.join(random.choice(string.ascii_letters) for i in range(5))
                descriere = ''.join(random.choice(string.ascii_letters) for i in range(5))
                autor = ''.join(random.choice(string.ascii_letters) for i in range(5))
                carte = Carte(id,nume,descriere,autor)
                self.__validare_carte.valideaza(carte)
                self.__repo_carti.adauga(carte)
            except RepoError as re:
                i = i - 1
                continue

