from ERRORS.repo_error import RepoError


class RepoClienti:

    def __init__(self):
        self._Clienti = {}

    def adauga(self,client):
        if client.get_id() in self._Clienti:
            raise RepoError("client existent!")
        self._Clienti[client.get_id()] = client

    def modifica(self,client):
        if client.get_id() not in self._Clienti:
            raise RepoError("client inexistent!")
        self._Clienti[client.get_id()] = client

    def sterge(self,id_client):
        if id_client not in self._Clienti:
            raise RepoError("client inexistent!")
        del self._Clienti[id_client]

    def cauta(self,id_client):
        '''
                if id_client not in self._Clienti:
            raise RepoError("client inexistent!")
        return self._Clienti[id_client]

        '''
        return self.__cauta_rec1(id_client,list(self._Clienti.keys()))

    def __cauta_rec1(self,id_client,lista):
        if lista == []:
            raise RepoError("client inexistent!")
        if id_client == lista[0]:
            return self._Clienti[id_client]
        return self.__cauta_rec1(id_client,lista[1:])



    def get_all(self):
        list_clienti = []
        '''
                for id_clienti in self._Clienti:
            list_clienti.append(self._Clienti[id_clienti])
        return list_clienti
        '''
        return self.get_all_rec(list(self._Clienti.values()),list_clienti)


    def get_all_rec(self,lista_inc,lista_clienti):
        if lista_inc == []:
            return lista_clienti
        lista_clienti.append(lista_inc[0])
        return self.get_all_rec(lista_inc[1:],lista_clienti)

    def nr(self):
        return len(self._Clienti)