class Carte:

    def __init__(self,id,nume,descriere,autor):

        self.__id_carte = id
        self.__nume_carte = nume
        self.__descriere_carte = descriere
        self.__autor_carte = autor

    def get_id(self):
        '''
        returneaza id-ul cartii
        :return: int
        '''
        return self.__id_carte

    def get_nume(self):
        '''
        returneaza numele unei carti
        :return: str
        '''
        return self.__nume_carte

    def get_descriere(self):
        '''
        returneaza descrierea unei carti
        :return: str
        '''
        return self.__descriere_carte

    def get_autor(self):
        '''
        returneaza autorul unei carti
        :return: str
        '''
        return self.__autor_carte

    def set_id(self,id):
        '''

        :param id:
        :return:
        '''
        self.__id_carte = id

    def set_nume(self,nume):
        self.__nume_carte = nume

    def set_descriere(self,descriere):
        self.__descriere_carte = descriere

    def set_autor(self,autor):
        self.__autor_carte = autor

    def __eq__(self, other):
        return self.__id_carte == other.__id_carte

    def __str__(self):
        return f"{self.__id_carte},{self.__nume_carte},{self.__descriere_carte},{self.__autor_carte}"