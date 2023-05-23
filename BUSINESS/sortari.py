from DOMAIN.carti import Carte
from DOMAIN.clienti import Client
from DOMAIN.inchirieri import Inchiriere
from DOMAIN.clienti_20 import Client_20
from DOMAIN.clienti_carti_DTO import Client_Carti


class Sortari:

    def __init__(self):
       pass

    def __compare(self,element1,element2,comparator):
        if isinstance(element1,Carte) and isinstance(element2,Carte):
            if comparator == "nume":
                return element1.get_nume() > element2.get_nume()
            if comparator == "descriere":
                return element1.get_descriere() > element2.get_descriere()
            if comparator == "autor":
                return element1.get_autor() > element2.get_autor()

        if isinstance(element1,Client) and isinstance(element2,Client):
            if comparator == "nume":
                return element1.get_nume() > element2.get_nume()
            if comparator == "CNP":
                return element1.get_CNP() > element2.get_CNP()

        if isinstance(element1,Client_20) and isinstance(element2,Client_20):
            if comparator == "nume":
                return element1.get_nume() > element2.get_nume()
            if comparator == "nr":
                return element1.get_nr() > element2.get_nr()

        if isinstance(element1,Client_Carti) and isinstance(element2,Client_Carti):
            if comparator == "nume":
                return element1.get_nume() > element2.get_nume()
            if comparator == "nr":
                return element1.get_nr() > element2.get_nr()

        if type(element1) is tuple and type(element2) is tuple:
            comparator = int(comparator)
            return element1[comparator] > element2[comparator]

        return element1 > element2



    def BubbleSort(self,l,comparator,rev=False):
        '''

        Caz fovarabil : O(1)
        Can nefavorabil : O(n`2)

        '''

        sortat = False
        while not sortat:
            sortat = True
            for i in range(0, len(l) - 1):
                if self.__compare(l[i],l[i+1],comparator):
                    l[i],l[i+1] = l[i+1],l[i]
                    sortat = False


        if not rev:
            return l
        l = list(reversed(l))
        return l

    def ShellSort(self,l,comparator,comp2,rev=False):

        l = self.BubbleSort(l,comp2,False)

        interval = len(l)//2
        while interval > 0:
            for i in range(interval,len(l)):
                primul_el = l[i]
                j = i
                while j-interval >= 0 and self.__compare(l[j-interval],primul_el,comparator):
                    l[j] = l[j-interval]
                    j = j - interval

                l[j] = primul_el
            interval//=2

        if not rev:
            return l

        l = list(reversed(l))
        return l