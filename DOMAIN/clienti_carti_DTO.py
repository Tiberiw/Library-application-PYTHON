class Client_Carti:

    def __init__(self,nume,nr_carti):
        self.__nume_client = nume
        self.__nr_carti = nr_carti

    def __str__(self):
        return f"clientul {self.__nume_client} cu un numar de {self.__nr_carti} carti inchiriate"

    def __lt__(self, other):
        return self.__nume_client < other.__nume_client

    def get_nume(self):
        return self.__nume_client

    def get_nr(self):
        return self.__nr_carti