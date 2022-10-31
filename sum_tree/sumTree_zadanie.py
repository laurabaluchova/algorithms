# Implementacni test IB002 2015 - uloha 1 (max 10 bodu)
#
# Zadani:
#
# Vasi ulohou je implementovat dve funkce pro praci s datovou strukturou "Souctovy strom".
# Muzete si samozrejme pridat vlastni pomocne funkce.
#
# Souctovy strom je binarny strom, kde kazdy uzel ma nasledujici vlastnost:
# Pokud ma uzel alespon jednoho syna, potom je klic uzlu roven souctu klicu vsech jeho synu.
# Vsimnete si, ze uvedena veta je implikace. Listy stromu teda mohou obsahovat libovolne hodnoty.
# Z definice je strom, ktery neobsahuje zadne uzly, a strom, ktery obsahuje prave jeden uzel, 
# povazovan za souctovy.
#
# Priklad:
# souctove stromy      nesouctove stromy
#   53       47            53       47
#  /  \        \          /  \     /
# 21  32       47        21  21   23
#
#
# Vasi prvni ulohou je napsat funkci isSumTree, ktera overi, zda je strom souctovy.
#
# Vasi druhou ulohou je napsat funkci, ktera vybuduje souctovy 
# strom co nejmensi vysky ze zadaneho pole.
# Listy stromu budu prave prvky pole v poradi zleva doprava.
# Pro jednoduchost predpokladame, ze delka pole bude mocninou dvojky (toto je
# bez ujmy na obecnosti - pokud by to neplatilo, mohli bychom pridat na konec pole nuly).
# 
# Napriklad:
# Z pole [1,2,3,4] vznikne strom:
#      10
#    /    \
#   3      7
#  / \    / \
# 1   2  3   4


class SumTree:
    """
    Trida pro reprezentaci souctoveho stromu, 'root' je koren stromu a je typu Node, nebo None, pokud je strom prazdny.
    """
    def __init__(self):
        self.root = None


class Node:
    """
    Trida pro reprezentaci uzlu v souctovom strome.
    'key' je hodnota uzlu, ktera ma byt rovna souctu hodnot vsetch synu (pokud alespon jeden existuje).
    'parent' je rodic, tedy atribut typu Node pokud uzel neni koren, jinak None
    'left' je levy syn, tedy atribut typu Node pokud syn existuje, jinak None
    'right' analogicky jako left
    """
    def __init__(self):
        self.key = 0
        self.parent = None
        self.left = None
        self.right = None


def is_leaf(node):
    return node.left is None and node.right is None


def isSumTree(t):
    """
    isSumTree rozhodne, zda je strom souctovy.
    :param t: t strom typu SumTree
    :return: True pokud t je souctovy, jinak False
    """
    if t.root is None:
        return True

    return isSumTreeRecursive(t.root)


def isSumTreeRecursive(node):
    if node is None:
        return True

    is_current_node_correct = is_node_correct(node)

    is_right_correct = isSumTreeRecursive(node.right)
    is_left_correct = isSumTreeRecursive(node.left)

    return is_current_node_correct and is_right_correct and is_left_correct


def is_node_correct(node):
    if is_leaf(node):
        return True

    elif node.left is None:
        if node.key == node.right.key:
            return True
    elif node.right is None:
        if node.key == node.left.key:
            return True
    elif node.left.key + node.right.key == node.key:
        return True
    return False


def array_sum(array):
    my_sum = 0

    for i in range(0, len(array) - 1):
        my_sum += array[i]

    return my_sum


def buildSumTree(array):
    """
    Vybuduje souctovy strom co nejmensi vysky ze seznamu array.
    :param array: seznam cisel, jehoz delka je mocninou 2
    :return: souctovy strom (typu SumTree) vybudovany nad seznamom array
    """
    my_tree = SumTree()
    node_array = []

    if len(array) == 0:
        return my_tree

    if len(array) == 1:
        new_node = Node()
        new_node.key = array[0]
        my_tree.root = new_node
        return my_tree

    for i in range(0, len(array)):
        new_node = Node()
        new_node.key = array[i]
        node_array.append(new_node)

    buildSumTreeResursive(my_tree, node_array)
    return my_tree


def buildSumTreeResursive(tree, node_array):
    sum_array = []

    for i in range(0, len(node_array), 2):
        new_node_key = node_array[i].key + node_array[i + 1].key
        new_node = Node()
        new_node.key = new_node_key
        new_node.left = node_array[i]
        new_node.right = node_array[i + 1]
        node_array[i].parent = new_node
        node_array[i + 1].parent = new_node
        if len(node_array) == 2:
            tree.root = new_node
            return
        sum_array.append(new_node)

    buildSumTreeResursive(tree, sum_array)














def main():
    """
    Hlavni funkce volana automaticky po spusteni programu.
    Pokud chcete krome dodanych testov spustit vlastni testovaci kod, dopiste ho sem.
    :return:
    """
    allTests()

########################################################################
###             Nasleduje kod testu, NEMODIFIKUJTE JEJ               ###
########################################################################

# Nize uvedene funkce jsou zamerne napsane zvlastnim zpusobem,
# aby z nich nebylo mozne ziskat napovedu k rieseni ulohy :-)


def allTests():
    success, total = map(sum, zip(*(testIsSumTree(),testBuildSumTree())))

    print ("-------------------")
    print ("CELKOVE SPRAVNE: %d/%d %s"%(success,total,":-)" if (success==total) else ":-("))

def testIsSumTree():
    TEST_COUNT = 10
    testNames = [
        "prazdny strom (root==None)",
        "strom s jednim uzlem",
        "maly korektni strom 1",
        "maly korektni strom 2",
        "maly nekorektni strom 1",
        "maly nekorektni strom 2",
        "velky korektni strom 1",
        "velky korektni strom 2",
        "velky nekorektni strom 1",
        "velky nekorektni strom 2",
    ]

    expectedResults = [True, True, True, True, False, False, True, True, False, False]

    failHints = [
        "Vas program oznacil prazdny strom za nesouctovy, podle definice je takovy strom souctovy.",
        "Vas program oznacil strom s jedinym uzlem za nesuctovy, podla definice je takovy strom souctovy.",
        "Vas program oznacil nize nacrtnuty strom za nesouctovy: ",
        "Vas program oznacil nize nacrtnuty strom za nesouctovy: ",
        "Vas program oznacil nize nacrtnuty strom za souctovy: ",
        "Vas program oznacil nize nacrtnuty strom za souctovy: ",
        "Vas program oznacil nize nacrtnuty strom za nesouctovy: ",
        "Vas program oznacil nize nacrtnuty strom za nesouctovy: ",
        "Vas program oznacil nize nacrtnuty strom za souctovy: ",
        "Vas program oznacil nize nacrtnuty strom za souctovy: "
    ]

    printTrees = [False, False, True, True, True, True, True, True, True, True]

    treeCodes = [
        [],
        [47],
        [47, None, 47],
        [53, 21, 32],
        [28, 7],
        [53, 21, 21],
        [120, 28, 92, 6, 22, 38, 54, 1, 5, 9, 13, 17, 21, 25, 29, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [6, 3, 3, None, 3, 3, None, None, None, 1, 2, None, 3],
        [120, 28, 92, 6, 22, 38, 54, 1, 5, None, 13, 17, 21, 25, 29, 0, 1, 2, 3, None, None, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16],
        [121, 28, 92, 6, 22, 38, 54, 1, 5, 9, 13, 17, 21, 25, 29, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    ]

    success = 0

    print ("Testy isSumTree:")
    print ("-------------------")

    for i in range(TEST_COUNT):
        testTree = listToTree(treeCodes[i])
        print("XXXXXXXXXXXXXXXXXXXXXXXX  TEST %2d/%-2d  XXXXXXXXXXXXXXXXXXXXXXXX"%(i+1,TEST_COUNT))
        print("%s: "%(testNames[i]),end="")
        res = isSumTree(testTree)
        if (res is None):
            print("FAIL, funkce isSumTree vratila None")
            continue
        print("%s"%("FAIL" if res!=expectedResults[i] else "OK"))
        if (res!=expectedResults[i]):
            print(failHints[i])
            if printTrees[i]: printTree(testTree)
        else: success+=1;
        print ()

    print ("SPRAVNE: %d/%d %s"%(success,TEST_COUNT,":-)" if (success==TEST_COUNT) else ":-("))
    print ("-------------------")

    return (success,TEST_COUNT)

def testBuildSumTree():
    TEST_COUNT = 5
    testNames = [
        "jednoprvkovy seznam",
        "dvouprvkovy seznam",
        "ctyrprvkovy seznam",
        "osmiprvkovy seznam",
        "sestnactiprvkovy seznam"
    ]

    lists = [
        [47],
        [28,7],
        [8,12,19,91],
        [2,3,5,7,11,13,17,19],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    ]

    expectedLists = [
        [47]+[None]*62,
        [35,28,7]+[None]*60,
        [130,20,110,8,12,19,91]+[None]*56,
        [77,17,60,5,12,24,36,2,3,5,7,11,13,17,19]+[None]*48,
        [120,28,92,6,22,38,54,1,5,9,13,17,21,25,29,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]+[None]*32
    ]
    success = 0

    print ("Testy buildSumTree:")
    print ("-------------------")

    for i in range(TEST_COUNT):
        print("XXXXXXXXXXXXXXXXXXXXXXXX  TEST %2d/%-2d  XXXXXXXXXXXXXXXXXXXXXXXX"%(i+1,TEST_COUNT))
        print("%s: "%(testNames[i]),end="")

        tree = buildSumTree(lists[i])
        if (tree is None):
            print("FAIL, funkce buildSumTree vratila None")
            continue
        ok = True
        if (not checkParents(tree)):
            print ("Nektery z uzluv vaseho stromu nema spravne nastaveneho rodica.")
            ok = False

        res = treeToList(tree)
        print("%s"%("FAIL" if res!=expectedLists[i] or not ok else "OK"))
        if (res!=expectedLists[i] or not ok):
            print("Zadany seznam byl "+str(lists[i]))
            print("Vas program vybudoval nize uvedeny strom (zobrazuje se maximalne 5 urovni stromu)")
            printTree(tree)
        else: success+=1;
        print ()

    print ("SPRAVNE: %d/%d %s"%(success,TEST_COUNT,":-)" if (success==TEST_COUNT) else ":-("))
    print ("-------------------")
    return (success, TEST_COUNT)

def getNodeValueByCode(t,code,depth):
    node = t.root
    for i in range(depth-1,-1,-1):
        node = (node.right if code&(1<<i) else node.left) if node is not None else None
    if node is None: return None
    return node.key

def treeToList(t):
    codes = list(range(1))+list(range(2))+list(range(4))+list(range(8))+list(range(16))+list(range(32))
    depths = [0] + [1]*2 + [2]*4 + [3]*8 + [4]*16 + [5]*32
    return [getNodeValueByCode(t,codes[i],depths[i]) for i in range(63)]

def listToTree(L):
    t = SumTree()
    nodes = [None]+[(Node() if k is not None else None) for k in L]+[None]*32
    for i in range(1,len(L)+1):
        if nodes[i] is not None:
            nodes[i].key = L[i-1]
            nodes[i].left = nodes[2*i]
            nodes[i].right = nodes[2*i+1]
            nodes[i].parent = nodes[i//2]
    t.root = nodes[1]
    return t

def printTree(tree):
    treeTemplate = "                               %4s\n" \
                   "              %4s                            %4s\n" \
                   "      %4s            %4s            %4s            %4s\n" \
                   "  %4s    %4s    %4s    %4s    %4s    %4s    %4s    %4s\n" \
                   "%4s%4s%4s%4s%4s%4s%4s%4s%4s%4s%4s%4s%4s%4s%4s%4s"
    toString = lambda x: "" if x is None else str(x)

    print ("------------------------- Nacrt stromu -------------------------")
    print (treeTemplate%tuple(map(toString,treeToList(tree)[:31])))
    print ("------------------------- Konec nacrtu -------------------------")

def checkParents(tree):
    return checkParentsRecursive(tree.root,None)

def checkParentsRecursive(node,parentShouldBe):
    if node is None: return True
    if node.parent is not parentShouldBe: return False
    return checkParentsRecursive(node.left, node) and checkParentsRecursive(node.right,node)

if __name__ == '__main__':
    main()


