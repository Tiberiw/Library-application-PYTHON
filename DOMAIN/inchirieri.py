class Inchiriere:

    def __init__(self,id,client,carte):
        self.__id_inchiriere = id
        self.__client_inchiriere = client
        self.__carte_inchiriere = carte

    def get_id(self):
        '''
        returneaza id-ul unei inchirieri
        :return:
        '''
        return self.__id_inchiriere

    def get_client(self):
        return self.__client_inchiriere

    def get_carte(self):
        return self.__carte_inchiriere

    def set_id(self,id):
        self.__id_inchiriere = id

    def set_client(self,client):
        self.__client_inchiriere = client

    def set_carte(self,carte):
        self.__carte_inchiriere = carte

    def __eq__(self, other):
        return self.__id_inchiriere == other.__id_inchiriere

    def __str__(self):
        return f"{self.__id_inchiriere},{self.__client_inchiriere},{self.__carte_inchiriere}"