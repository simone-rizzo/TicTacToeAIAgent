from Game import Game, Azione
from appJar import gui
import atlastk as Atlas

def alpha_beta(game, state):
    def max_value(state, alpha, beta):
        if game.terminal_test(state):
            # se in state il gioco e' concluso restituisci il risultato
            return game.utility(state)
        v = - float('inf')  # v e' inizializzato a - infinito
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a), alpha, beta))
            if v >= beta:  # taglio beta
                #print('MAX: stato %s - utilita\' %s - TAGLIO BETA (alpha = %s, beta = %s)' % (state, v, alpha, beta))
                return v
            alpha = max(alpha, v)  # aggiorna il migliore per MAX
        #print('MAX: stato %s - utilita\' %s - (alpha = %s, beta = %s)' % (state, v, alpha, beta))
        return v

    def min_value(state, alpha, beta):
        if game.terminal_test(state):
            # se in state il gioco e' concluso restituisci il risultato
            return game.utility(state)
        v = float('inf')  # v e' inizializzato a + infinito
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a), alpha, beta))
            if v <= alpha:  # taglio alpha
                #print('MIN: stato %s - utilita\' %s - TAGLIO ALPHA (alpha = %s, beta = %s)' % (state, v, alpha, beta))
                return v
            beta = min(beta, v)  # aggiorna il migliore per MIN
        #print('MIN: stato %s - utilita\' %s - (alpha = %s, beta = %s)' % (state, v, alpha, beta))
        return v

    # inizializza alpha e beta
    alpha = - float('inf')
    beta = float('inf')
    game.print()
    best_action = None
    # esegue un ciclo esterno di max_value "controllato"
    # memorizzando la mossa migliore
    for a in game.actions(state):
        v = min_value(game.result(state, a), alpha, beta)
        if v > alpha:
            # se lo score della mossa a e' il migliore fino a qui
            # allora memorizza la mossa a
            best_action = a
            alpha = v
    #print("Lazione selezionata e "+str(best_action.x)+","+str(best_action.y))
    return best_action


def minimax_decision(game, state):
    def max_value(state):
        if game.terminal_test(state):
            # se in state il gioco e' concluso restituisci il risultato
            val = game.utility(state)
            # game.print2(state)
            # print(val)
            return val
        v = - float('inf') # v e' inizializzato a - infinito
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a)))
         #print('MAX: stato {} - utilita\' {}'.format(state, v))
        return v

    def min_value(state):
        if game.terminal_test(state):
            # se in state il gioco e' concluso restituisci il risultato
            val = game.utility(state)
            # game.print2(state)
            # print(val)
            return val
        v = float('inf') # v e' inizializzato a + infinito
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a)))
        print('MIN: stato {} - utilita\' {}'.format(state, v))
        return v

    best_action = max(game.actions(state), key=lambda x: min_value(game.result(state, x)))
    # best_action e' l'argomento (l'azione) che massimizza l'output di min_value
    print("L\'azione selezionata e\' {}".format(best_action))
    return best_action


def pressButton(button):
    coord = str(button).split(".")
    x = int(coord[0])
    y = int(coord[1])
    a = Azione(x, y, "o")
    game.mettiSimbolo(a)
    app.setButton(button, "o")
    if game.terminal_test(game.matrix):
        if app.questionBox("E' finito", "Il gioco è terminato vuoi rigiocare?", parent=None):
            game.nuovaPartita()
            pulisciBottoni()
    else:
        aia = alpha_beta(game, game.matrix)
        game.mettiSimbolo(aia)
        nuovoID = str(aia.x) + "." + str(aia.y)
        app.setButton(nuovoID, "x")
        if game.terminal_test(game.matrix):
            if app.questionBox("E' finito", "Il gioco è terminato vuoi rigiocare?", parent=None):
                game.nuovaPartita()
                pulisciBottoni()



game = Game()
app = gui("TicTacToe AI", "500x500")
app.setBg("LightYellow")
app.setSticky("news")
app.setExpand("both")
app.setFont(40)
app.addButton("0.0", pressButton,  0, 0)
app.addButton("0.1", pressButton,  0, 1)
app.addButton("0.2", pressButton,  0, 2)
app.addButton("1.0", pressButton,  1, 0)
app.addButton("1.1", pressButton,  1, 1)
app.addButton("1.2", pressButton,  1, 2)
app.addButton("2.0", pressButton,  2, 0)
app.addButton("2.1", pressButton,  2, 1)
app.addButton("2.2", pressButton,  2, 2)
app.setButton("0.0", " ")
app.setButton("0.1", " ")
app.setButton("0.2", " ")
app.setButton("1.0", " ")
app.setButton("1.1", " ")
app.setButton("1.2", " ")
app.setButton("2.0", " ")
app.setButton("2.1", " ")
app.setButton("2.2", " ")


def pulisciBottoni():
    app.setButton("0.0", " ")
    app.setButton("0.1", " ")
    app.setButton("0.2", " ")
    app.setButton("1.0", " ")
    app.setButton("1.1", " ")
    app.setButton("1.2", " ")
    app.setButton("2.0", " ")
    app.setButton("2.1", " ")
    app.setButton("2.2", " ")
# add labels & entries
# in the correct row & column


if __name__ == '__main__':
    app.go()

    """a = Azione(0, 0, "x")
    game.mettiSimbolo(a)
    a = Azione(0, 1, "o")
    game.mettiSimbolo(a)
    # a = Azione(0, 2, "x")
    # game.mettiSimbolo(a)
    a = Azione(1, 1, "o")
    game.mettiSimbolo(a)
    # a = Azione(2, 1, "o")
    # game.mettiSimbolo(a)
    # a = Azione(2, 2, "o")
    # game.mettiSimbolo(a)
    game.print()
    # print(game.utility(game.matrix))
    aia = minimax_decision(game, game.matrix)
    game.mettiSimbolo(aia)
    print(str(aia.x) + " " + str(aia.y) + " " + aia.c)
    game.print()"""

    """while not game.terminal_test(game.matrix):

        num1 = int(input())
        num2 = int(input())
        a = Azione(num1, num2, "o")
        game.mettiSimbolo(a)
        game.print()
        if game.terminal_test(game.matrix):
            break
        aia = alpha_beta(game, game.matrix)
        game.mettiSimbolo(aia)
        print(str(aia.x) + " " + str(aia.y) + " " + aia.c)
        game.print()
        if game.terminal_test(game.matrix):
            break"""


