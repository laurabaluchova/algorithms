"""***************************************************************************
 Implementacny test IB002 - uloha 1. (12 bodov)

 Zadanie:
 Ruzovo-modry strom je binarny strom obsahujuci celociselne kluce, v ktorom
 kazdy uzol ma bud modru alebo ruzovu farbu a navyse su splnene podmienky:
 1. koren stromu je ruzovy
 2. vsetky listy su modre (list je uzol, ktory nema ziadneho potomka)
 3. ziaden uzol nema rovnaku farbu ako niektory z jeho synov
 4. ak ma uzol prave jedneho syna, potom obsahuje cislo delitelne 2

 Vasou ulohou je napisat funkciu isPinkBlue, ktora skontroluje, ci je strom
 ruzovo-modry. Mozete samozrejme doplnit aj dalsie pomocne funkcie podla
 vlastneho uvazenia. Pre vase pohodlie mate k dispozicii obrazky stromov,
 ktore sa testuju v prilozenom maine.

 Po ukonceni prace nahrajte vas kod do odovzdavarne:

 Odovzdavajte len zdrojovy kod, NEODOVZDAVAJTE subory s nastaveniami pre IDE.
 ***************************************************************************"""
from __future__ import print_function #pre kompatibilitu s Python 3.x
PINK, BLUE = (0, 1) #na reprezentaciu farieb uzlov

"""Kazdy uzol si pamata svoj kluc, farbu, ukazatel na rodica a synov.
   Koren stromu ma ukazatel na rodica nastaveny na None, rovnako su na None
   nastavene ukazatele left a right ak prislusny syn neexistuje """


class Node:
    key = None
    color = None
    parent = None
    left = None
    right = None


def isPinkBlue(root):
    """
    Funkcia overi, ci strom je ruzovo-modry podla vyssie uvedenej definicie

    @type root: Node
    @param root koren stromu
    @return False ak strom nie je ruzovo-modry, True inak
    """
    if root is None:
        return False

    return is_pink_blue_recursive(root)


def is_pink_blue_recursive(node):
    if node is None:
        return True

    if node.parent is None and node.color != PINK:
        return False

    if is_leaf(node) and node.color != BLUE:
        return False

    if has_only_left_son(node) and node.left.color == node.color:
        return False

    if has_only_right_son(node) and node.right.color == node.color:
        return False

    if has_both_sons(node) and (node.right.color == node.color or node.left.color == node.color):
        return False

    if has_only_left_son(node) or has_only_right_son(node):
        if node.key % 2 != 0:
            return False

    is_left_correct = is_pink_blue_recursive(node.left)
    is_right_correct = is_pink_blue_recursive(node.right)

    return is_left_correct and is_right_correct


def is_leaf(node):
    return node.left is None and node.right is None


def has_only_left_son(node):
    return node.right is None and node.left is not None


def has_only_right_son(node):
    return node.left is None and node.right is not None


def has_both_sons(node):
    return node.left is not None and node.right is not None


def buildTreeFromArrays(keys, colors):
    """ Funkcia, ktora vybuduje testovaci strom:

    jednotlive prvky sa postupne vlozia do stromu na poziciu, ktora je urcena
    rovnako ako u (nevyvazeneho) binarneho vyhladavacieho stromu.
    
    Funkciu mozete pouzit na vybudovanie vlastneho testovacieho stromu.
    (ak vlastne testovacie stromy vytvarat nechcete, funkciu mozete ignorovat)
    !!! Funkciu pouzivaju aj testy, takze ju NEMENTE !!!
    
    Napr. pre vybudovanie strom4.png zavolajte:
    keys = [5,4,6,2,8,1,3,7,9]; strom = buildTreeFromArrays(keys,"PBBPPBBBB");

    @param keys zoznam klucov jednotlivych uzlov
    @param colors retazec farieb jednotlivych uzlov. P pre ruzovu, B pre modru
    @return vybudovany strom
    """
    root = None
    for i in range(len(colors)):
        root = insertNode(root, keys[i], BLUE if (colors[i] == 'B' or colors[i] == 'M') else PINK)
    return root


def main():
    """ testovaci main - NEMENIT

    ak chcete vas program otestovat na inych stromoch,
    tento main NEMENTE ale zakomentuje a pouzite vlastny
    """

    testTree = None
    success = 0
    
    print ("Testy:")
    print ("-------------------")

    for i in range(TEST_COUNT):
        testTree = buildTreeFromArrays(treeKeys[i],treeColors[i])
        print("Test %2d/%-2d - %s: "%(i+1,TEST_COUNT,testNames[i]),end="")
        res = isPinkBlue(testTree)
        print("%s"%("FAIL" if res!=expectedResults[i] else "OK"))
        if (res!=expectedResults[i]): print(failHints[i])
        else: success+=1;
    
    print ("-------------------")
    print ("SPRAVNE: %d/%d %s"%(success,TEST_COUNT,":-)" if (success==TEST_COUNT) else ":-("))



"""***************************************************************************
 * Nasledujuci kod (az do konca suboru) sluzi len pre ucely testov.
 * Nemusite mu venovat pozornost. NEMODIFIKOVAT.
 **************************************************************************"""
TEST_COUNT=10
testNames = [
    "prazdny strom (root==None)",
    "strom 1",
    "strom 2",
    "strom 3",
    "strom 4",
    "strom 5",
    "strom 6",
    "strom 7",
    "strom 8",
    "strom 9"
]

expectedResults = [False,False,False,True,False,True,False,True,True,False]

failHints = [
    "Prazdny strom nema ruzovy koren",
    "1-uzlovy ruzovy strom nema modre listy",
    "1-uzlovy modry strom nema ruzovy koren",
    "Vas program oznacil korektny strom za nekorektny",
    "Uzol s 1 synom musi obsahovat parne (sude) cislo",
    "Vas program oznacil korektny strom za nekorektny",
    "List stromu nesmie byt ruzovy",
    "Vas program oznacil korektny strom za nekorektny",
    "Vas program oznacil korektny strom za nekorektny",
    "Uzol nesmie mat rovnaku farbu ako jeho syn"
]

treeColors = [
    "",
    "P",
    "B",
    "PBBPPBBBB",
    "PB",
    "PB",
    "PBBPP",
    "PBBPPBB",
    "PBBPPBBBBPPPBBBBBB",
    "PBBPPBBBBPPBBBBBBB"
]

treeKeys = [
    [0], 
    [7],
    [3],
    [5,4,6,2,8,1,3,7,9],
    [5,4],
    [2,4],
    [2,1,4,3,5],
    [2,1,5,4,6,3,7],
    [10,8,20,2,18,1,6,14,19,4,12,16,3,5,11,13,15,17],
    [10,8,20,2,18,1,6,14,19,4,12,16,3,5,11,13,15,17]
]


def insertNode(root, key, color):
    newNode = Node()
    newNode.key = key
    newNode.color = color
    newNode.left = None
    newNode.right = None

    tmp = None #remembers parent
    subRoot = root
    while(subRoot != None):
        tmp = subRoot
        if(key < subRoot.key):
            subRoot = subRoot.left
        else: 
            subRoot = subRoot.right

    newNode.parent = tmp
    if(tmp != None):
        if(newNode.key < tmp.key):
            tmp.left = newNode
        else:
            tmp.right = newNode
    else: root = newNode
    
    return root


if __name__ == "__main__":
    main()

