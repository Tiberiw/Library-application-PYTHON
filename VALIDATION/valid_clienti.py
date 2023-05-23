from ERRORS.valid_error import ValidError


class ValidClient:

    def __init__(self):
        pass

    def valideaza(self,client):
        '''
        valideaza clientul client
        id client trbuie sa fie >= 0
        nume,CNP != ""
        :param client:
        :return:
        '''
        erori = ""
        if client.get_id() < 0:
            erori+="id invalid!\n"
        if client.get_nume() == "":
            erori+="nume invalid!\n"
        if client.get_CNP() == "":
            erori+="CNP invalid!\n"

        if len(erori) > 0:
            raise ValidError(erori)