import random


# Implementacni test IB002 2015 - uloha 1 (max 10 bodu)
# Zadani:
# 
# Vasim ukolem v tomto implementacnim testu bude spravne propojit listy
# binarniho vyhledavaciho stromu do jednosmerne zretezeneho seznamu.
# Vice informaci najdete nize u funkce link_leaves, kterou mate implementovat.

# Trida Tree slouzi k uchovani informaci o stromu
# atribut root je odkaz na koren stromu
# atribut first bude odkaz na prvni uzel seznamu (po provedeni funkce link_leaves)
# atribut last bude odkaz na posledni uzel seznamu (po provedeni funkce link_leaves)
class Tree:
    def __init__(self):
        self.root = None
        self.first = None
        self.last = None


# Trida Node slouzi k uchovani informaci uzlu ve strome
# atribut key je hodnota ulozena v uzlu
# atribut parent je odkaz na rodice uzlu
# atribut left je odkaz na levy podstrom
# atribut right je odkaz na pravy podstrom
# atribut next je odkaz na nasledujici (tedy smerem doprava) list
# u vnitrnich uzlu stromu ponechte next = None, nastavujte jen listy 
class Node:
    def __init__(self):
        self.key = 0
        self.parent = None
        self.left = None
        self.right = None
        self.next = None


# TODO: implementujte tuto funkci
# Vstupem funkce je strom 'tree', ktery je typu 'Tree'. Tento strom muze byt i prazdny.
# Vas algoritmus ma projit strom 'tree' a vsem listum priradit odkaz 'next' na nasledujici
# list napravo od uzlu. Nejpravejsi list ma hodnotu 'next' rovnu None.
# Hodnoty odkazu 'next' zustanou v uzlech, ktere nejsou listy, nezmenene.
#
# O vstupnim stromu nevite nic vic, nez ze jde o binarni vyhledavaci strom
# (zejmena nemusi byt vyvazeny).
#
# Dale jeste stromu 'tree' nastavte atributy 'first' a 'last', ktere odkazuji
# na prvni (nejlevejsi) a posledni (nejpravejsi) list stromu.
# Prazdny strom ma odkazy 'first' i 'last' nastaveny
# na None. Strom s jednim listem ma 'first' i 'last' nastaven na tento jediny list.
#
# Priklad: mejme nasledujici strom:
#                   e
#            ______/ \______
#           c               j
#       ___/ \___       ___/ \___
#      b         d     g         l
#     /               / \       / \
#    a               f   h     k   m
#                         \         \
#                          i         n
#
# Po volani link_leaves bude tree.first = a, tree.last = n.
# Seznam bude vypadat nasledovne:
# a -> d -> f -> i -> k -> n

def link_leaves(tree):
    if tree.root is None:
        return None

    linked_leaves = []
    final_linked_leaves = link_leaves_recursive(tree.root, linked_leaves)

    for i in range(0, len(final_linked_leaves) - 1):
        final_linked_leaves[i].next = final_linked_leaves[i + 1]

    tree.first = final_linked_leaves[0]
    tree.last = final_linked_leaves[len(final_linked_leaves) - 1]


def is_leaf(node):
    return node.left is None and node.right is None


def link_leaves_recursive(current_node, linked_leaves):
    if current_node is not None:
        link_leaves_recursive(current_node.left, linked_leaves)
        if is_leaf(current_node):
            linked_leaves.append(current_node)
        link_leaves_recursive(current_node.right, linked_leaves)
    return linked_leaves



########################################################################
###                 Nasleduje kod testu, neupravujte                 ###
########################################################################

# Vlozi novy uzel s klicem 'key' do stromu 'tree'   
def insert(tree, key):
    if tree == None: return
    node = Node()
    node.key = key
    parent = None
    subroot = tree.root
    
    while (subroot!= None):
        parent = subroot
        subroot = subroot.left if node.key < subroot.key else subroot.right
    node.parent = parent
    if parent == None:
        tree.root = node
    else:
        if node.key < parent.key:
            parent.left = node
        else:
            parent.right = node


def test_small_trees():
    print("Test 1. prazdny strom:"),
    empty_tree = Tree()
    link_leaves(empty_tree)
    if empty_tree.first is None and empty_tree.last is None:
        print("OK")
    else:
        print("NOK, prazdny strom ma mit prazdny prvni i posledni uzel seznamu")

    print("\nTest 2. strom s jednim uzlem:"),
    one_key_tree = Tree()
    insert(one_key_tree, 1)
    root = one_key_tree.root
    link_leaves(one_key_tree)
    if root is one_key_tree.first and root is one_key_tree.last and root.next is None:
        print("OK")
    else:
        print("NOK, nektery z odkazu je spatne")

    print("\nTest 3. strom s 2 uzly, list vlevo:"),
    two_keys_tree = Tree()
    insert(two_keys_tree, 2)
    insert(two_keys_tree, 1)
    root = two_keys_tree.root
    link_leaves(two_keys_tree)
    if root.left is two_keys_tree.first and root.left is two_keys_tree.last and root.left.next is None:
        print("OK")
    else:
        print("NOK, nektery z odkazu je spatne")
        if root.key != 2:
            print("root je " + str(root.key) + " a ma byt 2")
        if two_keys_tree.first is None:
            print("tree.first neni nastaven, ale ma byt nastaven na uzel 1")
        else:
            print("tree.first je " + str(two_keys_tree.first.key) + " a ma byt 1")
        if two_keys_tree.last is None:
            print("tree.last neni nastaven, ale ma byt nastaven na uzel 1")
        else:
            print("tree.last je " + str(two_keys_tree.last.key) + " a ma byt 1")

    print("\nTest 4. strom s 2 uzly, list vpravo:"),
    two_keys_tree_b = Tree()
    insert(two_keys_tree_b, 1)
    insert(two_keys_tree_b, 2)
    root = two_keys_tree_b.root
    link_leaves(two_keys_tree_b)
    if root.right is two_keys_tree_b.first and root.right is two_keys_tree_b.last and root.right.next is None:
        print("OK")
    else:
        print("NOK, nektery z odkazu je spatne")
        if root.key != 1:
            print("root je " + str(root.key) + " a ma byt 1")
        if two_keys_tree_b.first is None:
            print("tree.first neni nastaven, ale ma byt nastaven na uzel 2")
        else:
            print("tree.first je " + str(two_keys_tree_b.first.key) + " a ma byt 2")
        if two_keys_tree_b.last is None:
            print("tree.last neni nastaven, ale ma byt nastaven na uzel 2")
        else:
            print("tree.last je " + str(two_keys_tree_b.last.key) + " a ma byt 2")

    print("\nTest 5. strom se 3 uzly, vyvazeny:"),
    three_keys_tree = Tree()
    insert(three_keys_tree, 2)
    insert(three_keys_tree, 1)
    insert(three_keys_tree, 3)
    root = three_keys_tree.root
    link_leaves(three_keys_tree)
    if root.left is three_keys_tree.first and root.right is three_keys_tree.last and root.left.next is root.right and root.right.next is None:
        print("OK")
    else:
        print("NOK, nektery z odkazu je spatne")
        if root.key != 2:
            print("root je " + str(root.key) + " a ma byt 2")
        if three_keys_tree.first is None:
            print("tree.first neni nastaven, ale ma byt nastaven na uzel 1")
        else:
            print("tree.first je " + str(three_keys_tree.first.key) + " a ma byt 1")
        if three_keys_tree.last is None:
            print("tree.last neni nastaven, ale ma byt nastaven na uzel 3")
        else:
            print("tree.last je " + str(three_keys_tree.last.key) + " a ma byt 3")

    print("\nTest 6. strom se 3 uzly, klikata cesta:"),
    three_keys_tree_b = Tree()
    insert(three_keys_tree_b, 3)
    insert(three_keys_tree_b, 1)
    insert(three_keys_tree_b, 2)
    root = three_keys_tree_b.root
    link_leaves(three_keys_tree_b)
    if root.left.right is three_keys_tree_b.first and root.left.right is three_keys_tree_b.last and three_keys_tree_b.first.next is None:
        print("OK")
    else:
        print("NOK, nektery z odkazu je spatne")


def test_big_trees():
    print("\nTest 7. velky strom rostouci posloupnosti, tedy cesta:"),
    tree_a = Tree()
    for i in range(100):
        insert(tree_a, i)

    link_leaves(tree_a)
    if tree_a.first is None or tree_a.last is None:
        print("NOK, neni nastaven nektery z odkazu tree.first nebo tree.last")
    elif tree_a.first is tree_a.last and tree_a.first.next is None:
        print("OK")
    else:
        print("NOK, nektery z odkazu je spatne")

    print("\nTest 8. velky strom nahodnych hodnot:"),
    tree_b = Tree()
    for i in range(100):
        insert(tree_b, random.randint(1, 1000))

    link_leaves(tree_b)

    if tree_a.first is None or tree_a.last is None:
        print("NOK, neni nastaven nektery z odkazu tree.first nebo tree.last")
    else:
        is_ok = check_tree(tree_b.root)
        is_ok = is_ok and check_list(tree_b)
        if is_ok:
            print("OK")
        else:
            print("NOK, prirazujete next nekteremu z vnitrnich uzlu, nebo mate spatne poradi ve vyslednem seznamu")


def check_tree(node):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return True
    else:
        if node.next is not None:
            return False
        else:
            return check_tree(node.left) and check_tree(node.right)


def check_list(tree):
    actual_node = tree.first
    while actual_node is not tree.last:
        if actual_node.key > actual_node.next.key:
            return False
        if actual_node.left is not None or actual_node.right is not None:
            return False
        actual_node = actual_node.next
    if actual_node.next is not None:
        return False
    return True


if __name__ == '__main__':
    test_small_trees()
    test_big_trees()
