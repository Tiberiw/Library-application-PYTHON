from ERRORS.valid_error import ValidError


class ValidCarte:

    def __init__(self):
        pass

    def valideaza(self,carte):
        '''
        valideaza o carte
        id-ul trebuie sa fie >= 0
        nume,descriere,autor != ""
        :param carte:
        :return:
        '''
        erori = ""
        if carte.get_id() < 0:
            erori+="id invalid!\n"
        if carte.get_nume() == "":
            erori+="nume invalid!\n"
        if carte.get_descriere() == "":
            erori+="descriere invalida!\n"
        if carte.get_autor() == "":
            erori+="autor invalid!\n"

        if len(erori) > 0:
            raise ValidError(erori)

    pass