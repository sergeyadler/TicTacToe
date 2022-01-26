#Tic Tac Toe Spiel
# Spielt das Tic-Tac-Toe-Spiel gegen einen Computer

#Globale Constanten



X="X"
O="O"
LEER=" "
TIE="Undentschieden"
NUM_SQUARES= 9


def inctuctions_zeigen():
    """Spielanweisungen anzeigen."""
    print(
        """
     Willkommen zur Tic-Tac-Toe.
     Dies wird ein Showdown zwischen Ihrem menschlichen Gehirn und meinem Siliziumprozessor sein.

     Sie machen Ihren Zug bekannt, indem Sie eine Zahl von 0 bis 8 eingeben. Die Zahl
     entspricht der Platinenposition wie abgebildet:
     
                0 | 1 | 2
                ---------
                3 | 4 | 5
                ---------
                6 | 7 | 8
     
     
            """
        )


def ask_yes_no(frage):
    """Stell eine JA oder NEIN Frage."""
    response =None
    while response not in ("y", "n"):
        response= input(frage).lower()

    return response    
   

def ask_nummer(frage,low,high):
    """Fragen Sie nach einer Nummer innerhalb eines Bereichs. """
    response =None
    while response not in range(low, high):
        response = int(input(frage))
        return response

def erste_schritt():
    """ Bestimmen Sie, ob der Player oder Computer zuerst gestartet wird. """
    go_erst = ask_yes_no("Wollen Sie ersten Schritt machen? (y/n): ")

    if go_erst== "y":
        print("\nDann machen Sie bitte Ihre erste Schritt")
        player=X
        computer=O
    else:
        print("\nDer Computer macht den ersten Schritt ")
        computer=X
        player=O
    return player, computer

def neu_spielfeld():
    """Neu Spielfeld erstellen"""
    feld=[]
    for square in range(NUM_SQUARES):
        feld.append(LEER)
    return feld

def spielfeld_zeigen(feld):
    """Spielfeld auf Bildschirm zeigen"""
    print("\n\t", feld[0], "|", feld[1], "|", feld[2])
    print("\t","---------")
    print("\n\t", feld[3], "|", feld[4], "|", feld[5])
    print("\t","---------")
    print("\n\t", feld[6], "|", feld[7], "|", feld[8])

def legale_schritte(feld):
    """List mit den legalen Schritten erstellen"""
    schritt_list= []
    for square in range(NUM_SQUARES):
        if feld[square] == LEER:
            schritt_list.append(square)
    return schritt_list


def gewinner(feld):
    """Bestimmen Sie den Gewinner des Spiels."""
    WAYS_TO_WIN=((0,1,2),(3,4,5),(6,7,8),
                 (0,3,6),(1,4,7),(2,5,8),
                 (0,4,8),(2,4,6,))
    
    for row in WAYS_TO_WIN:
        if feld[row[0]]==feld[row[1]]==feld[row[2]]!=LEER:
            gewinner= feld[row[0]]
            return gewinner

    if LEER not in feld:
        return TIE
    return None


def player_schritt(feld, player):
    """Player schritt geben"""
    legal=legale_schritte(feld)
    schritt= None
    while schritt not in legal:
        schritt= ask_nummer("Wohin wirden Sie ziehen?(0 - 8):", 0, NUM_SQUARES)
        if schritt not in legal:
             print("\nDieses Feld ist bereits besetzt, dummer Spieler. Wähle ein anderes.\n")
    print("Fine...")
    return schritt


def computer_schritt(feld, computer, player):
    """Der Computer Schritt machen"""
    # Erstellen Sie eine Kopie für die Arbeit, da die Funktion die Liste ändert
    feld = feld[:]
    # Die Beste positionen
    BESTE_SCHRITT=(4,0,2,6,8,1,3,5,7)
    
    print("Der Computer muss eine Square Nummer haben,", end="")

    # Wenn der Computer gewinnen kann, machen Sie diesen Schritt
    for schritt in legale_schritte(feld):
        feld[schritt]=computer
        if gewinner(feld)==computer:
            print(schritt)
            return schritt

        feld[schritt]=LEER 

    # Wenn ein Mensch gewinnen kann, blockiere diesen Zug
    for schritt in legale_schritte(feld):
        feld[schritt]=player
        if gewinner(feld)==player:
            print(schritt)
            return schritt

        feld[schritt]=LEER 

    for schritt in BESTE_SCHRITT:
        if schritt in legale_schritte(feld):
            print(schritt)
            return schritt


def next_zug(zug):
    """Switch ZUG"""
    if zug == X:
        return O
    else:
        return X

def gewinner_gratulieren(der_gewinner,computer,player):
    """Gewinner gratulieren"""
    if der_gewinner !=TIE:
        print(der_gewinner, "hat gewonnen!\n")
    else:
        print("Unentschieden!\n")
    if(der_gewinner)== computer:
        print ("Wie ich vorhergesagt habe, Mensch, bin ich wieder triumphierend. \n" \
               "Beweis, dass Computer Menschen in jeder Hinsicht überlegen sind.")
    elif  der_gewinner == player:
        print("Nein, nein! Es kann nicht sein! Irgendwie hast du mich reingelegt, Mensch. \n" \
               "Aber nie wieder! Ich, der Computer, schwöre es!")        
    elif der_gewinner == TIE:
        print("Du hattest das größte Glück, Mensch, und hast es irgendwie geschafft, mich zu binden. \n" \
               "Feiern Sie heute ... denn dies ist das Beste, was Sie jemals erreichen werden.")








def main():
    inctuctions_zeigen()
    computer, player = erste_schritt()
    zug = X
    feld = neu_spielfeld()
    spielfeld_zeigen(feld)

    while not gewinner(feld):
        if zug== player:
            schritt= player_schritt(feld, player)
            feld[schritt]=player
        else:
            schritt= computer_schritt(feld, computer,player)
            feld[schritt]= computer
        spielfeld_zeigen(feld)
        zug=next_zug(zug)

    der_gewinner= gewinner(feld)
    gewinner_gratulieren(der_gewinner,computer,player)

#Programm starten
main()
input("\n\nPress Enter key to quit.")    
