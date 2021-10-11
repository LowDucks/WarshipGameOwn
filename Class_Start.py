# from Class_Offline import spilModComputer
# from Class_Online import Online
# import Class_Client_Server_Login

class Start:

    def startServer(self):
        # Tjek om spillet kører online mod spiller eller offline mod en AI.
        # Hvis Online, kør serveren, så den er klar til at forbinde spilerne.
        # Hvis Offline gør AI klar på det niveau der er valgt.

        if self.check()==True:
         print("returnerer True til Offline objekt")
         return True


    def forbindSpillere(self):
        # if online = True, forbind begge spillere til serveren.
        # tjek at begge spillere kan modtage og sende data til server.
        # Tjek at begge spillere har loadet spillet korrekt... check()
        # Diceroll omkring, hvem der får lov til at starte.

        return True

    def loadSpilData(self):
        # Load mappets grid hvor man skal kunne placere skibe på
        # Tjek at spillerne kan connect
        # Load Spillernes data
        #
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

        print("Inde i check funktion")
        if (self.aktiverSpil(self) and self.loadSpilData(self) and self.forbindSpillere(self) == True):
            print("Alle funktioner er startet korrekt")
            return True

Start.check(Start)
