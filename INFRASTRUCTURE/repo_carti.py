from ERRORS.repo_error import RepoError


class RepoCarti:

    def __init__(self):
        self._Carti = {}

    def adauga(self,carte):
        '''
        adauga o coarte in repo
        :param carte: carte
        :return: -
        '''
        if carte.get_id() in self._Carti:
            raise RepoError("carte existenta!")
        self._Carti[carte.get_id()] = carte

    def modifica(self,carte):
        '''
        modifica o carte din repo
        :param carte: carte
        :return:
        '''
        if carte.get_id() not in self._Carti:
            raise RepoError("carte inexistenta!")
        self._Carti[carte.get_id()] = carte

    def cauta(self,id_carte):
        '''
        cauta o carte din repo
        :param id_carte: int
        :return:
        '''
        if id_carte not in self._Carti:
            raise RepoError("carte inexistenta!")
        return self._Carti[id_carte]

    def sterge(self,id_carte):
        '''
        sterge o carte din repo
        :param id_carte: int
        :return:
        '''
        if id_carte not in self._Carti:
            raise RepoError("carte inexistenta!")
        del self._Carti[id_carte]

    def get_all(self):
        '''
        returneaza o lista cu toate cartile din repo
        :return: list
        '''
        list_carti = []
        for id_carti in self._Carti:
            list_carti.append(self._Carti[id_carti])
        return list_carti

    def nr(self):
        '''
        returneaza numarul de carti din repo
        :return: int
        '''
        return len(self._Carti)
