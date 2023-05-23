from DOMAIN.inchirieri import Inchiriere
from INFRASTRUCTURE.repo_inchirieri import RepoInchirieri


class FisierRepoInchirieri(RepoInchirieri):

    def __init__(self,cale_fisier):
        RepoInchirieri.__init__(self)
        self.__cale_fisier = cale_fisier


    def __read_all_from_file(self):

        with open(self.__cale_fisier,"r") as f:
            lines = f.readlines()
            self._inchirieri.clear()
            for linie in lines:
                linie = linie.strip()
                if linie != "":
                    parti = linie.split(",")
                    id = int(parti[0])
                    id_client = int(parti[1])
                    id_carte = int(parti[2])
                    inchiriere = Inchiriere(id,id_client,id_carte)
                    self._inchirieri[id] = inchiriere

    def __write_all_to_file(self):

        with open(self.__cale_fisier,"w") as f:
            for inchiriere in self._inchirieri.values():
                f.write(str(inchiriere) + "\n")

    def clear_file(self):
        with open(self.__cale_fisier,"w") as f:
            pass

    def adauga(self,inchiriere):
        self.__read_all_from_file()
        RepoInchirieri.adauga(self,inchiriere)
        self.__write_all_to_file()

    def modifica(self,inchiriere):
        self.__read_all_from_file()
        RepoInchirieri.modifica(self,inchiriere)
        self.__write_all_to_file()

    def sterge(self,id_inchiriere):
        self.__read_all_from_file()
        RepoInchirieri.sterge(self,id_inchiriere)
        self.__write_all_to_file()

    def cauta(self,id_inchiriere):
        self.__read_all_from_file()
        return RepoInchirieri.cauta(self,id_inchiriere)

    def get_all(self):
        self.__read_all_from_file()
        return RepoInchirieri.get_all(self)

    def nr(self):
        self.__read_all_from_file()
        return RepoInchirieri.nr(self)