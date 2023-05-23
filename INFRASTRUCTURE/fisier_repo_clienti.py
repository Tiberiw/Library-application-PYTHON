from DOMAIN.clienti import Client
from INFRASTRUCTURE.repo_clienti import RepoClienti


class FisierRepoClienti(RepoClienti):

    def __init__(self,calea_catre_fisier):
        RepoClienti.__init__(self)
        self.__calea_catre_fisier = calea_catre_fisier

    def __read_all_from_file(self):

        with open(self.__calea_catre_fisier,"r") as f:
            lines = f.readlines()
            self._Clienti.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_client = int(parts[0])
                    nume_client = parts[1]
                    CNP_client = parts[2]
                    client = Client(id_client,nume_client,CNP_client)
                    self._Clienti[id_client] = client

    def __write_all_to_file(self):
        with open(self.__calea_catre_fisier,"w") as f:
            for client in self._Clienti.values():
                f.write(str(client) + "\n")

    def clear_file(self):
        with open(self.__calea_catre_fisier,"w") as f:
            pass


    def adauga(self,client):
        self.__read_all_from_file()
        RepoClienti.adauga(self,client)
        self.__write_all_to_file()

    def modifica(self,client):
        self.__read_all_from_file()
        RepoClienti.modifica(self,client)
        self.__write_all_to_file()

    def sterge(self,id_client):
        self.__read_all_from_file()
        RepoClienti.sterge(self,id_client)
        self.__write_all_to_file()

    def cauta(self,id_client):
        self.__read_all_from_file()
        return RepoClienti.cauta(self,id_client)

    def get_all(self):
        self.__read_all_from_file()
        return RepoClienti.get_all(self)

    def nr(self):
        self.__read_all_from_file()
        return RepoClienti.nr(self)

