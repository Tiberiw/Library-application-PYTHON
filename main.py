from INFRASTRUCTURE.fisier_repo_carti import FisierRepoCarti
from INFRASTRUCTURE.fisier_repo_clienti import FisierRepoClienti
from INFRASTRUCTURE.fisier_repo_inchirieri import FisierRepoInchirieri
from TESTE_PYUNIT.teste_domain import TesteDomain
from VALIDATION.valid_carti import ValidCarte
from VALIDATION.valid_clienti import ValidClient
from VALIDATION.valid_inchirieri import ValidInchiriere
from INFRASTRUCTURE.repo_carti import RepoCarti
from INFRASTRUCTURE.repo_clienti import RepoClienti
from INFRASTRUCTURE.repo_inchirieri import RepoInchirieri
from BUSINESS.service_carti import ServiceCarti
from BUSINESS.service_clienti import ServiceClienti
from BUSINESS.service_inchirieri import ServiceInchirieri
from TEST.teste import Test
from PRESENTATION.console import UI

def main():
    validare_carte = ValidCarte()
    validare_client = ValidClient()
    validare_inchiriere = ValidInchiriere()

    repo_carti = RepoCarti()
    fisier_carti = "carti.txt"
    repo_carti_fisier = FisierRepoCarti(fisier_carti)

    repo_clienti = RepoClienti()
    fisier_clienti = "clienti.txt"
    repo_clienti_fisier = FisierRepoClienti(fisier_clienti)

    repo_inchirieri = RepoInchirieri()
    fisier_inchirieri = "inchirieri.txt"
    repo_inchirieri_fisier = FisierRepoInchirieri(fisier_inchirieri)

    service_carti = ServiceCarti(validare_carte,repo_carti_fisier)
    service_clienti = ServiceClienti(validare_client,repo_clienti_fisier)
    service_inchirieri = ServiceInchirieri(validare_inchiriere,repo_inchirieri_fisier,repo_clienti_fisier,repo_carti_fisier)

    test = Test()
    test.run()

    consola = UI(service_carti,service_clienti,service_inchirieri)
    consola.run()



main()