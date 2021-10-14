class Start:

    def __init__(self, OnlineMode, addr):
        self.onlineMode = OnlineMode
        self.addr = addr
        print(self.onlineMode)

        self.modeTest = False

        if self.onlineMode == True:
            print("[Starter WARSHIPGAME i ONLINE-mode]")
            self.modeTest = True
        elif self.onlineMode == False:
            print("[Starter WARSHIPGAME i OFFLINE-mode]")
            self.modeTest = True
        else:
            print('[Error] - onlineMode must be a boolean')

        if self.modeTest == False : print("fejl")

    def startServer(self):
        # Tjek om spillet kører online mod spiller eller offline mod en AI.
        # Hvis Online, kør serveren, så den er klar til at forbinde spilerne.
        # Hvis Offline gør AI klar på det niveau der er valgt.
        #placeholder:
        print(self.onlineMode)
        online = True
        return True
    startServer()
    def forbindSpillere(self):
        # if online = True, forbind begge spillere til serveren.
        # tjek at begge spillere kan modtage og sende data til server.
        # Tjek at begge spillere har loadet spillet korrekt... check()
        # Diceroll omkring, hvem der får lov til at starte.
        print(self.startServer(1))
        print("snask")
        return True

    def loadSpilData(self):
        # Load mappets grid hvor man skal kunne placere skibe på
        # Tjek at spillerne kan connect
        # Load Spillernes data

        return True

    def aktiverSpil(self):
        # Hent de angivne indstillinger for spillet. Hvis offline, start AI-programmet.
        # Konstruer koordinatsystem, hvor spillet skal foregå.
        return True

    def check(self):
        #Check alle funktionerne virker som de skal.
        #Tjek for andre mulige fejl
        #Hvis der er fejl tjek over alle igen, hvis de jo f.eks er connection kan det være det lykkes anden gang.
        #Hvis alle funktioner virker og der ikke er nogen fejl, gå videre til Class_Spil

        print("Kører unittest af Class_start.py")
        if (self.aktiverSpil(self) and self.loadSpilData(self) and self.forbindSpillere(self) == True):
            print("Alle funktioner er startet korrekt", "\n")
            return True

Start(True,111)

#Start.check(Start)
