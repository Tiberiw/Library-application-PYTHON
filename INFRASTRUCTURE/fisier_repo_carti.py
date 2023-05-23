from DOMAIN.carti import Carte
from INFRASTRUCTURE.repo_carti import RepoCarti


class FisierRepoCarti(RepoCarti):

    def __init__(self,cale_fisier):
        RepoCarti.__init__(self)
        self.__cale_fisier = cale_fisier

    def __read_all_from_file(self):

        with open(self.__cale_fisier,"r") as f:
            lines = f.readlines()
            self._Carti.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id = int(parts[0])
                    nume = parts[1]
                    descriere = parts[2]
                    autor = parts[3]
                    carte = Carte(id,nume,descriere,autor)
                    self._Carti[id] = carte


    def __write_all_to_file(self):

        with open(self.__cale_fisier,"w") as f:
            for carte in self._Carti.values():
                f.write(str(carte) + "\n")

    def clear_file(self):
        with open(self.__cale_fisier,"w") as f:
            pass

    def adauga(self,carte):
        self.__read_all_from_file()
        RepoCarti.adauga(self,carte)
        self.__write_all_to_file()

    def modifica(self,carte):
        self.__read_all_from_file()
        RepoCarti.modifica(self,carte)
        self.__write_all_to_file()

    def sterge(self,id_carte):
        self.__read_all_from_file()
        RepoCarti.sterge(self,id_carte)
        self.__write_all_to_file()

    def cauta(self,id_carte):
        self.__read_all_from_file()
        return RepoCarti.cauta(self,id_carte)

    def get_all(self):
        self.__read_all_from_file()
        return RepoCarti.get_all(self)

    def nr(self):
        self.__read_all_from_file()
        return RepoCarti.nr(self)