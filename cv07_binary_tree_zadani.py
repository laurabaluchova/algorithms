import sys


class Node:
    """Trida Node slouzi k reprezentaci uzlu ve strome.

    Atributy:
        key     klic daneho uzlu
        parent  reference na rodice uzlu (None, pokud neexistuje)
        left    reference na leveho potomka (None, pokud neexistuje)
        right   reference na praveho potomka (None, pokud neexistuje)
    """
    def __init__(self):
        self.key = 0
        self.parent = None
        self.right = None
        self.left = None


class BinarySearchTree:
    """Trida Binary_search_tree slouzi k reprezentaci binarniho vyhledavaciho
    stromu.

    Atributy:
        root    reference na korenovy uzel typu Node
    """
    def __init__(self):
        self.root = None


def insert(tree, key):
    """Vlozi novy uzel s klicem 'key' do stromu 'tree'."""
    if tree.root is None:
        tree.root = Node()
        tree.root.key = key
        return

    insert_recursive(key, tree.root)


def insert_recursive(key, node):
    if node.key < key and node.right is None:
        node.right = Node()
        node.right.key = key
        return

    if node.key > key and node.left is None:
        node.left = Node()
        node.left.key = key
        return

    if node.key < key:
        return insert_recursive(key, node.right)

    return insert_recursive(key, node.left)


def search(tree, key):
    """Vyhleda uzel s klicem 'key' ve strome 'tree'. Vrati uzel s hledanym
    klicem. Pokud se klic 'key' ve strome nenachazi, vraci None.
    """
    return search_recursive(key, tree.root)


def search_recursive(key, node):
    if node.key == key:
        return node

    if is_leaf(node):
        return None

    if node.key > key:
        return search_recursive(key, node.left)

    return search_recursive(key, node.right)


def is_leaf(node):
    return node.left is None and node.right is None


def delete(tree, node):
    """Smaze uzel 'node' ze stromu 'tree' a obnovi vlastnost vyhledavaciho
    stromu.
    """
    pass
    # TODO


def height(tree):
    """Vraci vysku stromu 'tree'."""
    if tree.root is None:
        return 0

    return height_recursive(tree, tree.root)


def height_recursive(tree, current_node):
    if current_node is None:
        return 0

    left_height = height_recursive(tree, current_node.left) + 1
    right_height = height_recursive(tree, current_node.right) + 1

    return max(left_height, right_height)


def is_correct_bst(tree):
    """Overi, zdali je strom 'tree' korektni binarni vyhledavaci strom.
    Pokud ano, vraci True, jinak False.
    """
    pass
    # TODO


# Dodatek k graphvizu:
# Graphviz je nastroj, ktery vam umozni vizualizaci datovych struktur,
# coz se hodi predevsim pro ladeni. Tento program generuje nekolik
# souboru neco.dot v mainu. Vygenerovane soubory nahrajte do online
# nastroje pro zobrazeni graphvizu:
# http://sandbox.kidstrythisathome.com/erdos/
# nebo http://www.webgraphviz.com/- zvlada i vetsi grafy.
#
# Alternativne si muzete nainstalovat prekladac z jazyka dot do obrazku
# na svuj pocitac.
def make_graphviz(node, f):
    if (node is None):
        return

    if (node.left is not None):
        f.write("\"%i\" -> \"%i\"\n" % (node.key, node.left.key))
        make_graphviz(node.left, f)
    else:
        f.write("L{} [label=\"\",color=white]\n{} -> L{}\n"
                .format(id(node), node.key, id(node)))

    if (node.right is not None):
        f.write("\"%i\" -> \"%i\"\n" % (node.key, node.right.key))
        make_graphviz(node.right, f)
    else:
        f.write("R{} [label=\"\",color=white]\n{} -> R{}\n"
                .format(id(node), node.key, id(node)))


def make_graph(tree, fileName):
    f = open(fileName, 'w')
    f.write("digraph Tree {\n")
    f.write("node [color=lightblue2, style=filled];\n")
    if (tree is not None) and (tree.root is not None):
        make_graphviz(tree.root, f)
    f.write("}\n")
    f.close()


def test_insert():
    print("Test 1. insert: ", end='')
    tree = BinarySearchTree()

    insert(tree, 3)

    if (tree.root is None) or (tree.root.key != 3):
        print("NOK - chybne vkladani do prazdneho stromu")
    else:
        insert(tree, 1)

        if (tree.root.key != 3) or (tree.root.left.key != 1):
            print("NOK - chybne vkladani do leveho podstromu")
        else:
            insert(tree, 5)
            if (tree.root.key != 3) or (tree.root.right.key != 5):
                print("NOK - chybne vkladani do praveho podstromu")
            else:
                insert(tree, 2)
                if (tree.root.left.right.key != 2):
                    print("NOK - chybne vkladani do leveho podstromu")
                else:
                    insert(tree, 4)
                    if (tree.root.right.left.key != 4):
                        print("NOK - chybne vkladani do praveho podstromu")
                    else:
                        print("OK")

    try:
        make_graph(tree, "insert.dot")
        print("Vykresleny strom najdete v souboru insert.dot")
    except:
        print("Ve vykreslovani nastala chyba")


def init_test_tree():
    tree = BinarySearchTree()

    nodes = [Node() for _ in range(7)]
    for i in range(7):
        nodes[i].key = i

    tree.root = nodes[3]

    tree.root.left = nodes[1]
    nodes[1].parent = tree.root
    nodes[1].left = nodes[0]
    nodes[0].parent = nodes[1]
    nodes[1].right = nodes[2]
    nodes[2].parent = nodes[1]

    tree.root.right = nodes[5]
    nodes[5].parent = tree.root
    nodes[5].left = nodes[4]
    nodes[4].parent = nodes[5]
    nodes[5].right = nodes[6]
    nodes[6].parent = nodes[5]

    return tree


def test_delete():
    print("Test 2. delete: ", end='')
    tree = init_test_tree()

    delete(tree, tree.root.left.left)

    if (tree.root.left.key != 1) or (tree.root.left.left is not None):
        print("NOK - chybne mazani listu")
    else:
        delete(tree, tree.root)
        if ((tree.root is None) or
                (tree.root.key != 4) or
                (tree.root.left.key != 1) or
                (tree.root.left.left is not None)):
            print("NOK - chybne mazani korenu")
        else:
            delete(tree, tree.root.left)
            if (tree.root.left.key != 2):
                print("NOK - chybne mazani uzlu v levem podstrome")
            else:
                print("OK")

    try:
        make_graph(tree, "delete.dot")
        print("Vykresleny strom najdete v souboru delete.dot")
    except:
        print("Ve vykreslovani nastala chyba")


def test_search():
    print("Test 3. search: ", end='')
    tree = init_test_tree()

    node = search(tree, 3)

    if (node is None) or (node.key != 3):
        print("NOK - chybne hledani korene s hodnotou 3")
    else:
        node = search(tree, 2)
        if (node is None) or (node.key != 2):
            print("NOK - chybne hledani listu s hodnotou 2")
        else:
            node = search(tree, 7)
            if (node is not None):
                print("NOK - hledani prvku, ktery se ve strome nevyskytuje")
            else:
                print("OK")

    try:
        make_graph(tree, "search.dot")
        print("Vykresleny strom najdete v souboru search.dot")
    except:
        print("Ve vykreslovani nastala chyba")


def test_height():
    print("Test 4. height: ", end='')
    tree = init_test_tree()
    h = height(tree)
    if (h != 3):
        print("NOK - vyska 3 != vase vyska {}".format(h))
    else:
        n = Node()
        n.key = 7
        tree.root.right.right.right = n
        n.parent = tree.root.left.right
        h = height(tree)
        if (h != 4):
            print("NOK - vyska 4 != vase vyska {}".format(h))
        else:
            print("OK")

    try:
        make_graph(tree, "height.dot")
        print("Vykresleny strom najdete v souboru height.dot")
    except:
        print("Ve vykreslovani nastala chyba")


def test_is_correct_bst():
    print("Test 5. is_correct_bst: ", end='')
    tree = init_test_tree()

    if not is_correct_bst(tree):
        print("NOK - strom je korektni binarni vyhledavaci strom")
    else:
        tree.root.key = 0
        tree.root.left.left = None
        if is_correct_bst(tree):
            print("NOK - strom neni korektni binarni vyhledavaci strom")
        else:
            tree.root.key = 3
            tree.root.left.right.key = 4
            tree.root.right.left.key = 2
            if is_correct_bst(tree):
                print("NOK - strom neni korektni binarni vyhledavaci strom")
            else:
                print("OK")

    try:
        make_graph(tree, "correct.dot")
        print("Vykresleny strom najdete v souboru correct.dot")
    except:
        print("Ve vykreslovani nastala chyba")


if __name__ == '__main__':
    test_insert()
    test_delete()
    test_search()
    test_height()
    test_is_correct_bst()
