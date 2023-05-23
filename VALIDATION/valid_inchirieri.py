from ERRORS.valid_error import ValidError


class ValidInchiriere:

    def __init__(self):
        pass

    def valideaza(self,inchiriere):
        '''
        valideaza inchirierea inchiriere
        :param inchiriere: inchiriere
        :return:
        '''
        erori = ""
        if inchiriere.get_id() < 0:
            erori+="id invalid!\n"
        if inchiriere.get_client() < 0:
            erori+="id client invalid!\n"
        if inchiriere.get_carte() < 0:
            erori+="id carte invalid!\n"

        if len(erori) > 0:
            raise ValidError(erori)