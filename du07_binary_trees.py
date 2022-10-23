# IB002 Extra domaci ukol 7.
#
# Souctovy strom je binarni strom, kde kazdy uzel ma nasledujici vlastnost:
# Pokud ma uzel alespon jednoho syna, potom je klic uzlu roven souctu klicu
# vsech jeho synu. Listy stromu tedy mohou obsahovat libovolne hodnoty.
# Za souctovy je povazovan i strom, ktery neobsahuje zadne uzly, a strom,
# ktery obsahuje prave jeden uzel.
#
# Muzete si samozrejme pridat vlastni pomocne funkce.
#
# Priklad:
# souctove stromy      nesouctove stromy
#   53       47            53       47
#  /  \        \          /  \     /
# 21  32       47        21  21   46
#             /  \                  \
#            1    46                 1

# Trida pro reprezentaci souctoveho stromu.
# root je koren stromu a je typu Node, nebo None, pokud je strom prazdny.

class SumTree:
    def __init__(self):
        self.root = None


# Trida pro reprezentaci uzlu v souctovem strome.
# key je hodnota uzlu, ktera ma byt rovna souctu hodnot vsech synu.

class Node:
    def __init__(self):
        self.key = 0
        self.parent = None
        self.left = None
        self.right = None


# Ukol 1.
# Vasim prvnim ukolem je napsat funkci, ktera vybuduje souctovy strom ze
# zadaneho pole. Listy stromu budou prave prvky pole v poradi zleva doprava.
# Pro jednoduchost predpokladame, ze delka pole bude mocninou dvojky (toto je
# bez ujmy na obecnosti - pokud by to neplatilo, mohli bychom pridat na konec
# pole nuly).
#
# Napriklad:
# Z pole [1,2,3,4] vznikne strom:
#      10
#    /    \
#   3      7
#  / \    / \
# 1   2  3   4

def buildSumTree(array):
    pass
    # TODO


# Ukol 2.
# Vasim druhym ukolem je napsat funkci isSumTree, ktera overi, zda je strom
# souctovy. Pokud ano, vraci True, jinak False.

def isSumTree(tree):
    pass
    # TODO
