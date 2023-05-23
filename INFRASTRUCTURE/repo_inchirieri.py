from ERRORS.repo_error import RepoError


class RepoInchirieri:

    def __init__(self):
        self._inchirieri = {}

    def adauga(self,inchiriere):
        if inchiriere.get_id() in self._inchirieri:
            raise RepoError("inchiriere existenta!")
        self._inchirieri[inchiriere.get_id()] = inchiriere

    def modifica(self,inchiriere):
        if inchiriere.get_id() not in self._inchirieri:
            raise RepoError("inchiriere inexistenta!")
        self._inchirieri[inchiriere.get_id()] = inchiriere

    def sterge(self,id):
        if id not in self._inchirieri:
            raise RepoError("inchiriere inexistenta!")
        del self._inchirieri[id]

    def cauta(self,id):
        if id not in self._inchirieri:
            raise RepoError("inchiriere inexistenta!")
        return self._inchirieri[id]

    def get_all(self):
        lista_inc = []
        for inc in self._inchirieri:
            lista_inc.append(self._inchirieri[inc])
        return lista_inc

    def nr(self):
        return len(self._inchirieri)