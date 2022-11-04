# Implementacny test IB002 - uloha 2. (8 bodov)
#
# V tomto prikladu budete pracovat se stromem, reprezentujici hierarchii mnozin.
# Kazdy uzel obsahuje klic, jenz je prvkem mnoziny. Uzly obsahuji seznam potomku,
# jejichz klice jsou podmnozinou klice rodice. Konkretneji je datova
# struktura uzlu popsana nize u tridy Node.
#
# ======
#  UKOL
# ======
# Vasi ulohou bude v tomto zadani implementovat metodu findMinimalRootOfNodes.
# Ta jako vstup bere 2 uzly stromu, a vraci uzel, z nehoz se lze dostat do obou
# vstupnich uzlu (dostat je mysleno jen pohybem smerem dolu, tedy prechodem na potomky)
# a zaroven je tento uzel na nejnizsi mozne urovni (nejblize obeda zadanym uzlum).
#
# Okrajove pripady: v pripadech, ze je nejaky vstupni uzel null, nebo uzly nejsou
# stejneho stromu, vracejte null. Tyto pripady vsak nejsou testovany.
#
# Priklad:
# mejme nasledujici strom
#              a (= TreeSet.root)
#            /   \
#           b     c
#         /   \    \
#        d     e    f
#             / \    \
#            g   h    i
#
# findMinimalRootOfNodes(g,h) = e
# findMinimalRootOfNodes(d,h) = b
# findMinimalRootOfNodes(a,i) = a
# findMinimalRootOfNodes(h,i) = a
# findMinimalRootOfNodes(i,i) = i

# Struktura uzlu:
# Uzel obsahuje klic key (retezec), ktery je unikatni mezi svymy sourozenci,
# ale neni unikatni v cele strukture stromu, stejny klic mohou mit treba
# rodic-potomek, bratranci, nebo libovolne vzdalenejsi uzly.
#
# Uzel obsahuje ukazatele na rodice parent, koren stromu ma parent = None
# potomci jsou ulozeni v seznamu children, list stromu ma delku tohoto seznamu 0
#
# Pokud uznate za vhodne, muzete do struktury pridat dalsi informace.

class Node:
    key = None
    parent = None
    children = None


# Pomocna funkce pro vytvoreni noveho uzlu s danym klicem a rodicem.
def new_node(key, parent):
    n = Node()
    n.key = key
    n.parent = parent
    n.children = []
    if parent:
        parent.children.append(n)
    return n


# Nasledujici funkce pouze vytvari stromovou strukturu na testovani. Needitujte.
def init_tree():
    root = new_node("IB002 Algorithms and data structures I", None)

    # Algorithms
    algorithms = new_node("Algorithms", root)

    iterative = new_node("Iterative algorithms", algorithms)
    new_node("Fibonacci", iterative)
    new_node("Power", iterative)
    searchingIt = new_node("Searching algorithms", iterative)
    new_node("Select sort", searchingIt)
    new_node("Insert sort", searchingIt)
    new_node("Bubble sort", searchingIt)
    new_node("Heap sort", searchingIt)

    recursive = new_node("Recursive algorithms", algorithms)
    divideAndConquer = new_node("Divide and Conquer algorithms", recursive)
    searchingRe = new_node("Searching algorithms", divideAndConquer)
    new_node("Merge sort", searchingRe)
    new_node("Quick sort", searchingRe)

    randomized = new_node("Randomized algorithms", algorithms)
    new_node("Monte Carlo pi", randomized)

    # Data structures
    dataStructures = new_node("Data structures", root)

    dynamic = new_node("Dynamic data structures", dataStructures)

    graphs = new_node("Graphs", dynamic)
    new_node("Weighted graph", graphs)
    new_node("Unweighted graph", graphs)
    new_node("Directed graph", graphs)
    new_node("Undirected graph", graphs)
    new_node("Bipartited graph", graphs)

    trees = new_node("Trees", dynamic)
    new_node("Binary search tree", trees)
    new_node("Red black tree", trees)
    new_node("B tree", trees)
    new_node("B+ tree", trees)

    lists = new_node("Linear data structures", dynamic)
    new_node("List", lists)
    new_node("Queue", lists)
    new_node("Stack", lists)

    static = new_node("Static data structures", dataStructures)
    new_node("N-tuple", static)
    new_node("Array of static length", static)
    new_node("Primitive data types", static)

    return root


#
# TODO:
# Naprogramujte nasledujici funkci, ktera dostane dva uzly stromu jako
# parametry a vrati jejich nejnizsiho spolecneho predchudce, viz popis vyse.
#
def find_minimal_root(first, second):
    if first == second:
        return first

    nodes_with_same_depth = make_depths_same(first, second)
    first = nodes_with_same_depth[0]
    second = nodes_with_same_depth[1]

    while first is not None or second is not None:
        first_parent = first
        second_parent = second

        if first_parent == second_parent:
            return first_parent

        first = first.parent
        second = second.parent


def depth_from_root(node):
    depth = 0

    while node is not None:
        depth += 1
        node = node.parent

    return depth


def make_depths_same(first, second):
    first_node_depth = depth_from_root(first)
    second_node_depth = depth_from_root(second)
    difference_between_depths = abs(first_node_depth - second_node_depth)

    list_with_new_nodes = []

    if first_node_depth == second_node_depth:
        list_with_new_nodes.append(second)
        list_with_new_nodes.append(first)

    elif first_node_depth > second_node_depth:
        for i in range(0, difference_between_depths):
            first = first.parent
        list_with_new_nodes.append(second)
        list_with_new_nodes.append(first)

    else:
        for i in range(0, difference_between_depths):
            second = second.parent
        list_with_new_nodes.append(second)
        list_with_new_nodes.append(first)

    return list_with_new_nodes

#
# Jednoduchy prehledny vypis stromu
# Prochazi stromem do hloubky a vypisuje v preorder tak, ze kazdy
# klic je odtabovan tolikrat, na kolikate urovni ve stromu je
# strom
#      a
#    /   \
#   b     c
#  /
# d
# je zapsan:
#  a
#      b
#          d
#      c

def simple_print(node, level):
    print ("\t"*level, node.key)
    for c in node.children:
        simple_print(c, level + 1)


#
# Nalezne uzel se zadanym klicem, v pripade vice uzlu se stejnym klicem
# vraci prvni nalezeny pruchodem DFS
#
def find(node, key):
    if key is None:
        return None
    if key == node.key:
        return node
    for c in node.children:
        result = find(c, key)
        if result:
            return result
    return None


#
# Nasleduje kod testuje funkcionalitu. Neupravujte.
#
root = init_tree()
simple_print(root, 0)


def test(root, first, second, expectation):
    first_node = find(root, first)
    second_node = find(root, second)
    result = find_minimal_root(first_node, second_node)
    if result.key == expectation:
        print ("OK")
    else:
        print ("Chyba, nalezeny uzel mel byt " + expectation + ", vas uzel byl " + result.key)

# test 1
print("Test 1.:")
test(root,
     "IB002 Algorithms and data structures I",
     "Algorithms",
     "IB002 Algorithms and data structures I")

# test 2
print("Test 2.:")
test(root,
     "Algorithms",
     "Algorithms",
     "Algorithms")

# test 3
print("Test 3.:")
test(root,
     "Heap sort",
     "Select sort",
     "Searching algorithms")

# test 4
print("Test 4.:")
test(root,
    "Graphs",
    "Directed graph",
    "Graphs")

# test 5
print("Test 5.:")
test(root,
    "B+ tree",
    "Power",
    "IB002 Algorithms and data structures I")

# test 6
print("Test 6.:")
test(root,
    "Data structures",
    "Merge sort",
    "IB002 Algorithms and data structures I")
