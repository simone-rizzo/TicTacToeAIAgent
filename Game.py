from copy import copy, deepcopy

class Azione:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

class Game:

    def __init__(self):
        self.matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def nuovaPartita(self):
        self.matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    def ciao(self):
        self.matrix[0][0] = "x"
        print(self.matrix[0][0])

    #ritorna se il gioco è terminato
    #oppure se uno ha vinto
    def terminal_test(self, stato):
       if self.ha_vintoTipo(stato, "x"):
           return True
       if self.ha_vintoTipo(stato, "o"):
           return True
       for i in stato:
           for j in i:
               if j == " ":
                   return False
       return True

    #ritorna se hai vinto oppure se hai perso
    def utility(self, stato):
        r = 0
        c = "x"
        if self.ha_vintoTipo(stato, "o"):
            return -1
        #orizzontali per riga
        if stato[0][0] == c and stato[0][1] == c and stato[0][2] == c:
            return 1
        if stato[1][0] == c and stato[1][1] == c and stato[1][2] == c:
            return 1
        if stato[2][0] == c and stato[2][1] == c and stato[2][2] == c:
            return 1
        #parti verticali per colonna
        if stato[0][0] == c and stato[1][0] == c and stato[2][0] == c:
            return 1
        if stato[0][1] == c and stato[1][1] == c and stato[2][1] == c:
            return 1
        if stato[0][2] == c and stato[1][2] == c and stato[2][2] == c:
            return 1
        #mancano quelli obliqui
        if stato[0][0] == c and stato[1][1] == c and stato[2][2] == c:
            return 1
        if stato[0][2] == c and stato[1][1] == c and stato[2][0] == c:
            return 1
        return r

    def ha_vintoTipo(self, stato, c):
        #c = "o"
        #orizzontali per riga
        if stato[0][0] == c and stato[0][1] == c and stato[0][2] == c:
            return True
        if stato[1][0] == c and stato[1][1] == c and stato[1][2] == c:
            return True
        if stato[2][0] == c and stato[2][1] == c and stato[2][2] == c:
            return True
        # parti verticali per colonna
        if stato[0][0] == c and stato[1][0] == c and stato[2][0] == c:
            return True
        if stato[0][1] == c and stato[1][1] == c and stato[2][1] == c:
            return True
        if stato[0][2] == c and stato[1][2] == c and stato[2][2] == c:
            return True
        # mancano quelli obliqui
        if stato[0][0] == c and stato[1][1] == c and stato[2][2] == c:
            return True
        if stato[0][2] == c and stato[1][1] == c and stato[2][0] == c:
            return True
        return False

    #ritorna la lista delle possibili azioni dallo stato corrente
    def actions(self, state):
        c = self.capisciIlSegno(state)
        actions = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == " ":
                    a = Azione(i, j, c)
                    actions.append(a)
        return actions

    def capisciIlSegno(self, stato):
        nx = 0
        no = 0
        for i in stato:
            for j in i:
                if j == "o":
                    no = no+1
                if j == "x":
                    nx = nx+1
        if nx >= no:
            return "o"
        else:
            return "x"

    #non so se va creata una nuova matrice
    def result(self, stato, azione):
        newstate = deepcopy(stato)
        newstate[azione.x][azione.y] = azione.c
        return newstate
        """stato[azione.x][azione.y] = azione.c
        return stato"""


    def print(self):
        for i in self.matrix:
            print("|"+i[0]+"|"+i[1]+"|"+i[2]+"|")

    def print2(self, stato):
        for i in stato:
            print("|"+i[0]+"|"+i[1]+"|"+i[2]+"|")


    def mettiSimbolo(self, azione):
        if self.matrix[azione.x][azione.y] == " ":
            self.matrix[azione.x][azione.y] = azione.c

