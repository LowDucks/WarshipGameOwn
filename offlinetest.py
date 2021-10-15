#Henter pakken unitest til programmet så man kan unittest
import unittest
#Henter Class Offline til programmet
from Class_Offline import Offline

#Her defineres Test-Klassen som startes fra main nedenunder
class TestOfflineMethods(unittest.TestCase):
    #Her defineres alle de tests man ønsker at udføree
    def test_spilModComputer(self):
        "spilModComputer Startet"
        offlineObject = Offline()
        self.assertTrue(offlineObject.spilModComputer())

    def test_pingServer(self):
        "Pinger server"
        self.assertTrue(True)



#Main metode her starter programmet altid at køre
if __name__ == '__main__':
    unittest.main()
