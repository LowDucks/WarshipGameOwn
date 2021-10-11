
class Offline:

    startSpil = Start()
    print("offlineStart er inititialiseret")



    def spilModComputer(self):
        print("spilModComputer Startet")

        startBool =self.startSpil.startServer()
        return True
