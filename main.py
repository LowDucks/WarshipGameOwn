from Class_Offline import Offline
from Class_Online import Online
from Class_Client_Server_Login import Client_Server_Login
from Class_Start import Start
from Class_Skibe import Skibe
from Class_Spil import Spil


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def integrationsTest_af_Offline_Start():
    offLineSpiller = Offline()
    return offLineSpiller.spilModComputer()

def integrationsTest_af_Online_Start():
    return True





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("Integrations tests for slagskibsspillet")
    #Her testes om alle integrationer er korrekte
    if integrationsTest_af_Offline_Start():
        print("integrationsTest_af_Offline_Start udført korrekt")
    else:
        print("integrationsTest_af_Offline_Start fejler")

    if integrationsTest_af_Online_Start():
        print("integrationsTest_af_Online_Start udført korrekt")
    else:
        print("integrationsTest_af_Online_Start fejler")
