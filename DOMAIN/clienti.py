class Client:

    def __init__(self,id,nume,CNP):
        self.__id_client = id
        self.__nume_client = nume
        self.__CNP_client = CNP

    def get_id(self):
        return self.__id_client

    def get_nume(self):
        return self.__nume_client

    def get_CNP(self):
        return self.__CNP_client

    def set_id(self,id):
        self.__id_client = id

    def set_nume(self,nume):
        self.__nume_client = nume

    def set_CNP(self,CNP):
        self.__CNP_client = CNP

    def __eq__(self, other):
        return self.__id_client == other.__id_client

    def __str__(self):
        return f"{self.__id_client},{self.__nume_client},{self.__CNP_client}"

