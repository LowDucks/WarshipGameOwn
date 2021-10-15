import unittest
from Class_Start import Start


class TestStartFunctions(unittest.TestCase):

    def test_startserver(self):
        '[FAILED TO START SERVER]'
        serverObj = Start()
        self.assertTrue(serverObj.startServer())
        print('[SERVER IS STARTED]\n')

    def test_forbindSpillere(self):
        '[FAILED TO CONNECT PLAYERS]'
        forbindObj = Start()
        self.assertTrue(forbindObj.forbindSpillere())
        print('[PLAYERS ARE CONNECTED]\n')


    def test_loadSpilData(self):
        '[FAILED TO LOAD GAME DATA]'
        loadObj = Start()
        self.assertTrue(loadObj.loadSpilData())
        print('[GAME DATA IS LOADED]\n')

    def test_aktiverSpil(self):
        '[FAILED TO START GAME]'
        aktiverObj = Start()
        self.assertTrue(aktiverObj.aktiverSpil())
        print('[GAME IS ACTIVATED]\n')


if __name__ == '__main__':
    unittest.main()
