import ast
import random
from collections import deque
import copy

# Specialni domaci ukol IB002 2017
# ** Ukol je lehci nez zadani implementacnich testu na zaverecne zkousce. **
#
# Ukol 1.
# Vstupem algoritmu je binarni strom, jehoz zpusob reprezentace naleznete
# nize (trida Tree). Uzly stromu obsahuji jako klice cela cisla.
# Vasim ukolem je rozhodnout, jestli je strom PRETTY, pricemz:
#
# Prazdny strom neni PRETTY.
# Strom s jednim uzlem je PRETTY prave tehdy, kdyz obsahuje sude cislo.
#
# Vetsi strom je PRETTY prave tehdy, kdyz:
# - levy podstrom je PRETTY a pravy podstrom neni PRETTY
# A SOUCASNE
# - pocet sudych cisel v jeho levem podstrome je vetsi nebo roven poctu sudych
#   cisel v jeho pravem podstrome.
#
# Implementujte funkci `is_PRETTY_tree`, ktera urci jestli je zadany strom
# PRETTY. Funkce vraci True, pokud je strom PRETTY, jinak vraci False.
# Funkci lze implementovat s linearni casovou slozitosti vzhledem
# k poctu vrcholu zadaneho stromu.


class Node:

    """Trida Node slouzi k reprezentaci uzlu ve strome.

    Atributy:
        key     klic daneho uzlu (cele cislo)
        left    reference na leveho potomka (None, pokud neexistuje)
        right   reference na praveho potomka (None, pokud neexistuje)
    """

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


class Tree:

    """Trida Tree slouzi k reprezentaci stromu.

    Atributy:
        root    reference na korenovy uzel typu Node
    """

    def __init__(self):
        self.root = None


def is_PRETTY_tree(tree):
    """Overi, zdali je strom 'tree' PRETTY.
    Pokud ano, vraci True, jinak False.
    """
    if tree is None or tree.root is None:
        return False

    is_pretty, number_of_even_keys = is_pretty_recursive(tree.root)
    return is_pretty


def is_pretty_recursive(node):
    if node is None:
        return False, 0

    if is_leaf(node):
        even_keys_count = 0
        if is_even(node):
            even_keys_count += 1
        return is_even(node), even_keys_count

    is_right_pretty, amount_of_even_keys_right = is_pretty_recursive(node.right)
    is_left_pretty, amount_of_even_keys_left = is_pretty_recursive(node.left)

    is_prettiness_satisfied = is_left_pretty and not is_right_pretty
    does_left_have_more_even_keys = amount_of_even_keys_left >= amount_of_even_keys_right
    number_of_even_keys = amount_of_even_keys_left + amount_of_even_keys_right

    if is_even(node):
        number_of_even_keys += 1

    return is_prettiness_satisfied and does_left_have_more_even_keys, number_of_even_keys


def is_leaf(node):
    return node.left is None and node.right is None


def is_even(node):
    return node.key % 2 == 0

# Ukol 2.
# Funkce `is_PRETTY_sequence` pracuje podobne jako `is_PRETTY_tree` v prvnim
# ukolu, jen je definovana na posloupnostech celych cisel.
# Vstupem algoritmu je neprazdna posloupnost ve forme standardniho Python
# seznamu (list). Pamatujte na to, ze pohodlne operace jako napriklad slice
# p[0:3] vytvori novou kopii seznamu, coz znamena jistou casovou a prostorovou
# slozitost.
#
# Vasim ukolem je rozhodnout, jestli je zadana posloupnost PRETTY, pricemz:
#
# Posloupnost delky 1 je PRETTY prave tehdy, kdyz obsahuje sude cislo.
#
# Delsi posloupnost je PRETTY prave tehdy, kdyz:
# - prvni polovina posloupnosti je PRETTY a druha polovina neni PRETTY
# A SOUCASNE
# - pocet sudych cisel v prvni polovine posloupnosti je vetsi nebo
#   roven poctu sudych cisel ve druhe polovine.
#
# V pripade liche delky je prvni "polovina" ta vetsi.
#
# Implementujte funkci `is_PRETTY_sequence`, ktera urci, jestli je posloupnost
# zadana na vstupu PRETTY. Funkce vraci True pro PRETTY posloupnost, jinak
# vraci False. Funkci lze implementovat s linearni casovou slozitosti vzhledem
# k delce vstupni posloupnosti.


def is_PRETTY_sequence(seq):
    """Overi, zdali je posloupnost 'seq' PRETTY.
    Pokud ano, vraci True, jinak False.
    """
    is_pretty, number_of_even_values = is_pretty_sequence_recursive(seq, 0, len(seq) - 1)
    return is_pretty


def is_pretty_sequence_recursive(seq, actual_index, last_index):
    if actual_index > last_index:
        return False, 0

    if actual_index == last_index:
        even_values_count = 0
        if is_value_even(seq, actual_index):
            even_values_count += 1
        return is_value_even(seq, actual_index), even_values_count

    is_right_pretty, amount_of_even_values_right = is_pretty_sequence_recursive(seq, (len(seq) // 2) + 1, last_index)
    is_left_pretty, amount_of_even_values_left = is_pretty_sequence_recursive(seq, actual_index + 1, first_index, len(seq) // 2)

    is_prettiness_satisfied = is_left_pretty and not is_right_pretty
    does_left_have_more_even_values = amount_of_even_values_left >= amount_of_even_values_right
    number_of_even_values = amount_of_even_values_left + amount_of_even_values_right

    if is_value_even(seq, actual_index):
        number_of_even_values += 1

    return is_prettiness_satisfied and does_left_have_more_even_values, number_of_even_values

def is_value_even(seq, index):
    return seq[index] % 2 == 0

# Ukol 3.
# Jedna se o rozsireni Ukolu 1.
# Zde je vasim ukolem vlozit do stromu, ktery je PRETTY, dane cislo tak,
# aby zustala PRETTY vlastnost zachovana. Vstupem je tedy PRETTY binarni strom
# a cele cislo.
#
# Implementujte funkci `insert`, ktera do zadaneho PRETTY stromu `tree` vlozi
# cislo `number` tak, aby vysledny strom byl PRETTY. Vystupem je strom, ktery
# vznikne po vlozeni cisla `number`. Muzete modifikovat a vratit strom zadany
# na vstupu. Pro kontrolu se vyuziva vase funkce `is_PRETTY_tree`, proto
# neuspesny test muze take znamenat, ze tuto funkci nemate implementovanou
# spravne.


def insert(tree, number):
    """Vlozi do PRETTY stromu 'tree' cislo 'number' tak, aby byl
    vysledny strom PRETTY. Vraci tento strom.
    """
    pass


"""
Soubory .dot z testu vykreslite napr. na http://www.webgraphviz.com/.
"""

#########################################################
# Nasleduje kod testu, NEMODIFIKUJTE JEJ               ##
#########################################################


def bool_(s):
    return s == "True"


def pretty(is_pretty):
    return "ma byt PRETTY" if is_pretty else "nema byt PRETTY"


def test_seq():
    error_count = 0
    print("\n**Sequence testing")
    for line in seq_data.split("\n"):
        if error_count > 4:
            print("Zobrazuje se pouze prvnich 5 chyb.")
            break
        seq, res = line.rstrip().split('; ')
        seq = ast.literal_eval(seq)
        res = bool_(res)
        seq = list(map(lambda x: random.randint(-13230, 2056) * 2 + x, seq))
        if is_PRETTY_sequence(seq) != res:
            print("FAIL, {} {}".format(seq, pretty(res)))
            error_count += 1
    if error_count == 0:
        print("SEQUENCE OK")


# **** TREE TESTS **** #
"""
Dodatek k graphvizu:
Graphviz je nastroj, ktery vam umozni vizualizaci datovych struktur,
coz se hodi predevsim pro ladeni.
Zde mate k dispozici funkci `makeGraph`, ktera vam z `tree` na vstupu
vygeneruje do souboru `fileName` reprezentaci stromu pro graphviz.
Pro zobrazeni graphvizu muzete vyuzit:
http://www.webgraphviz.com/
"""


def makeGraph(tree, fileName):

    def makeNode(id, label):
        f.write("{} [label=\"{}\"]\n".format(id, label))

    def makeEdge(n1, n2):
        f.write("{} -> {}\n".format(n1, n2))

    def checkChild(node, child, label):
        if child is None:
            makeNode("{}{}".format(label, id(node)), "Nil\", color=\"white")
            makeEdge(id(node), "{}{}".format(label, id(node)))
        else:
            makeEdge(id(node), id(child))
            makeGraphviz(child, f)

    def makeGraphviz(node, f):
        if node is None:
            return
        makeNode(id(node), node.key)
        checkChild(node, node.left, 'L')
        checkChild(node, node.right, 'R')

    with open(fileName, 'w') as f:
        f.write("digraph Tree {\n")
        f.write("node [color=lightblue2, style=filled, ordering=\"out\"];\n")
        if (tree is not None) and (tree.root is not None):
            makeGraphviz(tree.root, f)
        f.write("}\n")


def load_tree(seq):
    q = deque()
    index = 1
    tree = Tree()
    if not seq or seq[0] is None:
        return tree
    tree.root = Node(seq[0])
    q.append(tree.root)

    while len(q):
        node = q.popleft()
        if len(seq) > index:
            node.left = None if seq[index] is None else Node(seq[index])
            if node.left:
                q.append(node.left)
            index += 1
        if len(seq) > index:
            node.right = None if seq[index] is None else Node(seq[index])
            if node.right:
                q.append(node.right)
            index += 1
    return tree


def test_tree():
    error_count = 0
    print("\n**Tree testing")
    for line in tree_data.split("\n"):
        if error_count > 4:
            print("Zobrazuje se pouze prvnich 5 chyb.")
            break
        seq, res = line.rstrip().split('; ')
        seq = list(map(lambda x: None if x is None else
                   random.randint(-13230, 2056) * 2 + x,
                   ast.literal_eval(seq)))
        tree = load_tree(seq)
        res = bool_(res)
        if is_PRETTY_tree(tree) != res:
            error_count += 1
            filename = "Er_test_" + str(error_count) + ".dot"
            makeGraph(tree, filename)
            print("FAIL, strom v souboru {} {}".format(filename,
                  pretty(res)))
    if error_count == 0:
        print("TREE OK")


def contains(root, num):
    if root is None:
        return False

    return (root.key == num or contains(root.left, num) or
            contains(root.right, num))


def test_insert():
    error_count = 0
    print("\n**Insert testing")
    print("Pouziva vas vlastni is_PRETTY_tree!\n")
    for line in tree_data.split("\n"):
        if error_count > 4:
            break
        seq, res = line.rstrip().split('; ')
        seq = list(map(lambda x: None if x is None else
                   random.randint(-13230, 2056) * 2 + x,
                   ast.literal_eval(seq)))
        tree = load_tree(seq)
        res = bool_(res)
        if res:
            for num in [2, 3]:
                tree_res = insert(copy.deepcopy(tree), num)
                if tree_res and not contains(tree_res.root, num):
                    error_count += 1
                    filename_in = "Er_insert_" + \
                        str(error_count) + "_in.dot"
                    makeGraph(tree, filename_in)
                    filename_out = "Er_insert_" + \
                        str(error_count) + "_out.dot"
                    makeGraph(tree_res, filename_out)
                    print("FAIL, cislo {} vkladane do {} "
                          "neni ve vyslednem "
                          "{}".format(num, filename_in, filename_out))
                    if error_count > 4:
                        break
                elif not is_PRETTY_tree(tree_res):
                    error_count += 1
                    filename_in = "Er_insert_" + \
                        str(error_count) + "_in.dot"
                    makeGraph(tree, filename_in)
                    filename_out = "Er_insert_" + \
                        str(error_count) + "_out.dot"
                    makeGraph(tree_res, filename_out)
                    print("FAIL, pri vkladani {} do {} vracite {}, "
                          "ktery neni "
                          "PRETTY".format(num, filename_in, filename_out))
                    if error_count > 4:
                        break
    if error_count > 4:
        print("Zobrazuje se pouze prvnich 5 chyb.")
    elif error_count == 0:
        print("INSERT OK")


seq_data = """[0]; True
[1]; False
[0, 0]; False
[0, 1]; True
[1, 0]; False
[1, 1]; False
[0, 0, 0]; False
[0, 0, 1]; False
[0, 1, 0]; False
[0, 1, 1]; True
[1, 0, 0]; False
[1, 0, 1]; False
[1, 1, 0]; False
[1, 1, 1]; False
[0, 0, 0, 0]; False
[0, 0, 0, 1]; False
[0, 0, 1, 0]; False
[0, 0, 1, 1]; False
[0, 1, 0, 0]; False
[0, 1, 0, 1]; False
[0, 1, 1, 0]; True
[0, 1, 1, 1]; True
[1, 0, 0, 0]; False
[1, 0, 0, 1]; False
[1, 0, 1, 0]; False
[1, 0, 1, 1]; False
[1, 1, 0, 0]; False
[1, 1, 0, 1]; False
[1, 1, 1, 0]; False
[1, 1, 1, 1]; False
[0, 0, 0, 0, 0]; False
[0, 0, 0, 0, 1]; False
[0, 0, 0, 1, 0]; False
[0, 0, 0, 1, 1]; False
[0, 0, 1, 0, 0]; False
[0, 0, 1, 0, 1]; False
[0, 0, 1, 1, 0]; False
[0, 0, 1, 1, 1]; False
[0, 1, 0, 0, 0]; False
[0, 1, 0, 0, 1]; False
[0, 1, 0, 1, 0]; False
[0, 1, 0, 1, 1]; False
[0, 1, 1, 0, 0]; False
[0, 1, 1, 0, 1]; False
[0, 1, 1, 1, 0]; True
[0, 1, 1, 1, 1]; True
[1, 0, 0, 0, 0]; False
[1, 0, 0, 0, 1]; False
[1, 0, 0, 1, 0]; False
[1, 0, 0, 1, 1]; False
[1, 0, 1, 0, 0]; False
[1, 0, 1, 0, 1]; False
[1, 0, 1, 1, 0]; False
[1, 0, 1, 1, 1]; False
[1, 1, 0, 0, 0]; False
[1, 1, 0, 0, 1]; False
[1, 1, 0, 1, 0]; False
[1, 1, 0, 1, 1]; False
[1, 1, 1, 0, 0]; False
[1, 1, 1, 0, 1]; False
[1, 1, 1, 1, 0]; False
[1, 1, 1, 1, 1]; False
[0, 0, 0, 0, 0, 0]; False
[0, 0, 0, 0, 0, 1]; False
[0, 0, 0, 0, 1, 0]; False
[0, 0, 0, 0, 1, 1]; False
[0, 0, 0, 1, 0, 0]; False
[0, 0, 0, 1, 0, 1]; False
[0, 0, 0, 1, 1, 0]; False
[0, 0, 0, 1, 1, 1]; False
[0, 0, 1, 0, 0, 0]; False
[0, 0, 1, 0, 0, 1]; False
[0, 0, 1, 0, 1, 0]; False
[0, 0, 1, 0, 1, 1]; False
[0, 0, 1, 1, 0, 0]; False
[0, 0, 1, 1, 0, 1]; False
[0, 0, 1, 1, 1, 0]; False
[0, 0, 1, 1, 1, 1]; False
[0, 1, 0, 0, 0, 0]; False
[0, 1, 0, 0, 0, 1]; False
[0, 1, 0, 0, 1, 0]; False
[0, 1, 0, 0, 1, 1]; False
[0, 1, 0, 1, 0, 0]; False
[0, 1, 0, 1, 0, 1]; False
[0, 1, 0, 1, 1, 0]; False
[0, 1, 0, 1, 1, 1]; False
[0, 1, 1, 0, 0, 0]; False
[0, 1, 1, 0, 0, 1]; False
[0, 1, 1, 0, 1, 0]; False
[0, 1, 1, 0, 1, 1]; False
[0, 1, 1, 1, 0, 0]; False
[0, 1, 1, 1, 0, 1]; True
[0, 1, 1, 1, 1, 0]; True
[0, 1, 1, 1, 1, 1]; True
[1, 0, 0, 0, 0, 0]; False
[1, 0, 0, 0, 0, 1]; False
[1, 0, 0, 0, 1, 0]; False
[1, 0, 0, 0, 1, 1]; False
[1, 0, 0, 1, 0, 0]; False
[1, 0, 0, 1, 0, 1]; False
[1, 0, 0, 1, 1, 0]; False
[1, 0, 0, 1, 1, 1]; False
[1, 0, 1, 0, 0, 0]; False
[1, 0, 1, 0, 0, 1]; False
[1, 0, 1, 0, 1, 0]; False
[1, 0, 1, 0, 1, 1]; False
[1, 0, 1, 1, 0, 0]; False
[1, 0, 1, 1, 0, 1]; False
[1, 0, 1, 1, 1, 0]; False
[1, 0, 1, 1, 1, 1]; False
[1, 1, 0, 0, 0, 0]; False
[1, 1, 0, 0, 0, 1]; False
[1, 1, 0, 0, 1, 0]; False
[1, 1, 0, 0, 1, 1]; False
[1, 1, 0, 1, 0, 0]; False
[1, 1, 0, 1, 0, 1]; False
[1, 1, 0, 1, 1, 0]; False
[1, 1, 0, 1, 1, 1]; False
[1, 1, 1, 0, 0, 0]; False
[1, 1, 1, 0, 0, 1]; False
[1, 1, 1, 0, 1, 0]; False
[1, 1, 1, 0, 1, 1]; False
[1, 1, 1, 1, 0, 0]; False
[1, 1, 1, 1, 0, 1]; False
[1, 1, 1, 1, 1, 0]; False
[1, 1, 1, 1, 1, 1]; False
[0, 0, 0, 0, 0, 0, 0]; False
[0, 0, 0, 0, 0, 0, 1]; False
[0, 0, 0, 0, 0, 1, 0]; False
[0, 0, 0, 0, 0, 1, 1]; False
[0, 0, 0, 0, 1, 0, 0]; False
[0, 0, 0, 0, 1, 0, 1]; False
[0, 0, 0, 0, 1, 1, 0]; False
[0, 0, 0, 0, 1, 1, 1]; False
[0, 0, 0, 1, 0, 0, 0]; False
[0, 0, 0, 1, 0, 0, 1]; False
[0, 0, 0, 1, 0, 1, 0]; False
[0, 0, 0, 1, 0, 1, 1]; False
[0, 0, 0, 1, 1, 0, 0]; False
[0, 0, 0, 1, 1, 0, 1]; False
[0, 0, 0, 1, 1, 1, 0]; False
[0, 0, 0, 1, 1, 1, 1]; False
[0, 0, 1, 0, 0, 0, 0]; False
[0, 0, 1, 0, 0, 0, 1]; False
[0, 0, 1, 0, 0, 1, 0]; False
[0, 0, 1, 0, 0, 1, 1]; False
[0, 0, 1, 0, 1, 0, 0]; False
[0, 0, 1, 0, 1, 0, 1]; False
[0, 0, 1, 0, 1, 1, 0]; False
[0, 0, 1, 0, 1, 1, 1]; False
[0, 0, 1, 1, 0, 0, 0]; False
[0, 0, 1, 1, 0, 0, 1]; False
[0, 0, 1, 1, 0, 1, 0]; False
[0, 0, 1, 1, 0, 1, 1]; False
[0, 0, 1, 1, 1, 0, 0]; False
[0, 0, 1, 1, 1, 0, 1]; False
[0, 0, 1, 1, 1, 1, 0]; False
[0, 0, 1, 1, 1, 1, 1]; False
[0, 1, 0, 0, 0, 0, 0]; False
[0, 1, 0, 0, 0, 0, 1]; False
[0, 1, 0, 0, 0, 1, 0]; False
[0, 1, 0, 0, 0, 1, 1]; False
[0, 1, 0, 0, 1, 0, 0]; False
[0, 1, 0, 0, 1, 0, 1]; False
[0, 1, 0, 0, 1, 1, 0]; False
[0, 1, 0, 0, 1, 1, 1]; False
[0, 1, 0, 1, 0, 0, 0]; False
[0, 1, 0, 1, 0, 0, 1]; False
[0, 1, 0, 1, 0, 1, 0]; False
[0, 1, 0, 1, 0, 1, 1]; False
[0, 1, 0, 1, 1, 0, 0]; False
[0, 1, 0, 1, 1, 0, 1]; False
[0, 1, 0, 1, 1, 1, 0]; False
[0, 1, 0, 1, 1, 1, 1]; False
[0, 1, 1, 0, 0, 0, 0]; False
[0, 1, 1, 0, 0, 0, 1]; True
[0, 1, 1, 0, 0, 1, 0]; True
[0, 1, 1, 0, 0, 1, 1]; False
[0, 1, 1, 0, 1, 0, 0]; True
[0, 1, 1, 0, 1, 0, 1]; True
[0, 1, 1, 0, 1, 1, 0]; True
[0, 1, 1, 0, 1, 1, 1]; True
[0, 1, 1, 1, 0, 0, 0]; False
[0, 1, 1, 1, 0, 0, 1]; False
[0, 1, 1, 1, 0, 1, 0]; False
[0, 1, 1, 1, 0, 1, 1]; False
[0, 1, 1, 1, 1, 0, 0]; False
[0, 1, 1, 1, 1, 0, 1]; True
[0, 1, 1, 1, 1, 1, 0]; True
[0, 1, 1, 1, 1, 1, 1]; True
[1, 0, 0, 0, 0, 0, 0]; False
[1, 0, 0, 0, 0, 0, 1]; False
[1, 0, 0, 0, 0, 1, 0]; False
[1, 0, 0, 0, 0, 1, 1]; False
[1, 0, 0, 0, 1, 0, 0]; False
[1, 0, 0, 0, 1, 0, 1]; False
[1, 0, 0, 0, 1, 1, 0]; False
[1, 0, 0, 0, 1, 1, 1]; False
[1, 0, 0, 1, 0, 0, 0]; False
[1, 0, 0, 1, 0, 0, 1]; False
[1, 0, 0, 1, 0, 1, 0]; False
[1, 0, 0, 1, 0, 1, 1]; False
[1, 0, 0, 1, 1, 0, 0]; False
[1, 0, 0, 1, 1, 0, 1]; False
[1, 0, 0, 1, 1, 1, 0]; False
[1, 0, 0, 1, 1, 1, 1]; False
[1, 0, 1, 0, 0, 0, 0]; False
[1, 0, 1, 0, 0, 0, 1]; False
[1, 0, 1, 0, 0, 1, 0]; False
[1, 0, 1, 0, 0, 1, 1]; False
[1, 0, 1, 0, 1, 0, 0]; False
[1, 0, 1, 0, 1, 0, 1]; False
[1, 0, 1, 0, 1, 1, 0]; False
[1, 0, 1, 0, 1, 1, 1]; False
[1, 0, 1, 1, 0, 0, 0]; False
[1, 0, 1, 1, 0, 0, 1]; False
[1, 0, 1, 1, 0, 1, 0]; False
[1, 0, 1, 1, 0, 1, 1]; False
[1, 0, 1, 1, 1, 0, 0]; False
[1, 0, 1, 1, 1, 0, 1]; False
[1, 0, 1, 1, 1, 1, 0]; False
[1, 0, 1, 1, 1, 1, 1]; False
[1, 1, 0, 0, 0, 0, 0]; False
[1, 1, 0, 0, 0, 0, 1]; False
[1, 1, 0, 0, 0, 1, 0]; False
[1, 1, 0, 0, 0, 1, 1]; False
[1, 1, 0, 0, 1, 0, 0]; False
[1, 1, 0, 0, 1, 0, 1]; False
[1, 1, 0, 0, 1, 1, 0]; False
[1, 1, 0, 0, 1, 1, 1]; False
[1, 1, 0, 1, 0, 0, 0]; False
[1, 1, 0, 1, 0, 0, 1]; False
[1, 1, 0, 1, 0, 1, 0]; False
[1, 1, 0, 1, 0, 1, 1]; False
[1, 1, 0, 1, 1, 0, 0]; False
[1, 1, 0, 1, 1, 0, 1]; False
[1, 1, 0, 1, 1, 1, 0]; False
[1, 1, 0, 1, 1, 1, 1]; False
[1, 1, 1, 0, 0, 0, 0]; False
[1, 1, 1, 0, 0, 0, 1]; False
[1, 1, 1, 0, 0, 1, 0]; False
[1, 1, 1, 0, 0, 1, 1]; False
[1, 1, 1, 0, 1, 0, 0]; False
[1, 1, 1, 0, 1, 0, 1]; False
[1, 1, 1, 0, 1, 1, 0]; False
[1, 1, 1, 0, 1, 1, 1]; False
[1, 1, 1, 1, 0, 0, 0]; False
[1, 1, 1, 1, 0, 0, 1]; False
[1, 1, 1, 1, 0, 1, 0]; False
[1, 1, 1, 1, 0, 1, 1]; False
[1, 1, 1, 1, 1, 0, 0]; False
[1, 1, 1, 1, 1, 0, 1]; False
[1, 1, 1, 1, 1, 1, 0]; False
[1, 1, 1, 1, 1, 1, 1]; False
[0, 0, 0, 0, 0, 0, 0, 0]; False
[0, 0, 0, 0, 0, 0, 0, 1]; False
[0, 0, 0, 0, 0, 0, 1, 0]; False
[0, 0, 0, 0, 0, 0, 1, 1]; False
[0, 0, 0, 0, 0, 1, 0, 0]; False
[0, 0, 0, 0, 0, 1, 0, 1]; False
[0, 0, 0, 0, 0, 1, 1, 0]; False
[0, 0, 0, 0, 0, 1, 1, 1]; False
[0, 0, 0, 0, 1, 0, 0, 0]; False
[0, 0, 0, 0, 1, 0, 0, 1]; False
[0, 0, 0, 0, 1, 0, 1, 0]; False
[0, 0, 0, 0, 1, 0, 1, 1]; False
[0, 0, 0, 0, 1, 1, 0, 0]; False
[0, 0, 0, 0, 1, 1, 0, 1]; False
[0, 0, 0, 0, 1, 1, 1, 0]; False
[0, 0, 0, 0, 1, 1, 1, 1]; False
[0, 0, 0, 1, 0, 0, 0, 0]; False
[0, 0, 0, 1, 0, 0, 0, 1]; False
[0, 0, 0, 1, 0, 0, 1, 0]; False
[0, 0, 0, 1, 0, 0, 1, 1]; False
[0, 0, 0, 1, 0, 1, 0, 0]; False
[0, 0, 0, 1, 0, 1, 0, 1]; False
[0, 0, 0, 1, 0, 1, 1, 0]; False
[0, 0, 0, 1, 0, 1, 1, 1]; False
[0, 0, 0, 1, 1, 0, 0, 0]; False
[0, 0, 0, 1, 1, 0, 0, 1]; False
[0, 0, 0, 1, 1, 0, 1, 0]; False
[0, 0, 0, 1, 1, 0, 1, 1]; False
[0, 0, 0, 1, 1, 1, 0, 0]; False
[0, 0, 0, 1, 1, 1, 0, 1]; False
[0, 0, 0, 1, 1, 1, 1, 0]; False
[0, 0, 0, 1, 1, 1, 1, 1]; False
[0, 0, 1, 0, 0, 0, 0, 0]; False
[0, 0, 1, 0, 0, 0, 0, 1]; False
[0, 0, 1, 0, 0, 0, 1, 0]; False
[0, 0, 1, 0, 0, 0, 1, 1]; False
[0, 0, 1, 0, 0, 1, 0, 0]; False
[0, 0, 1, 0, 0, 1, 0, 1]; False
[0, 0, 1, 0, 0, 1, 1, 0]; False
[0, 0, 1, 0, 0, 1, 1, 1]; False
[0, 0, 1, 0, 1, 0, 0, 0]; False
[0, 0, 1, 0, 1, 0, 0, 1]; False
[0, 0, 1, 0, 1, 0, 1, 0]; False
[0, 0, 1, 0, 1, 0, 1, 1]; False
[0, 0, 1, 0, 1, 1, 0, 0]; False
[0, 0, 1, 0, 1, 1, 0, 1]; False
[0, 0, 1, 0, 1, 1, 1, 0]; False
[0, 0, 1, 0, 1, 1, 1, 1]; False
[0, 0, 1, 1, 0, 0, 0, 0]; False
[0, 0, 1, 1, 0, 0, 0, 1]; False
[0, 0, 1, 1, 0, 0, 1, 0]; False
[0, 0, 1, 1, 0, 0, 1, 1]; False
[0, 0, 1, 1, 0, 1, 0, 0]; False
[0, 0, 1, 1, 0, 1, 0, 1]; False
[0, 0, 1, 1, 0, 1, 1, 0]; False
[0, 0, 1, 1, 0, 1, 1, 1]; False
[0, 0, 1, 1, 1, 0, 0, 0]; False
[0, 0, 1, 1, 1, 0, 0, 1]; False
[0, 0, 1, 1, 1, 0, 1, 0]; False
[0, 0, 1, 1, 1, 0, 1, 1]; False
[0, 0, 1, 1, 1, 1, 0, 0]; False
[0, 0, 1, 1, 1, 1, 0, 1]; False
[0, 0, 1, 1, 1, 1, 1, 0]; False
[0, 0, 1, 1, 1, 1, 1, 1]; False
[0, 1, 0, 0, 0, 0, 0, 0]; False
[0, 1, 0, 0, 0, 0, 0, 1]; False
[0, 1, 0, 0, 0, 0, 1, 0]; False
[0, 1, 0, 0, 0, 0, 1, 1]; False
[0, 1, 0, 0, 0, 1, 0, 0]; False
[0, 1, 0, 0, 0, 1, 0, 1]; False
[0, 1, 0, 0, 0, 1, 1, 0]; False
[0, 1, 0, 0, 0, 1, 1, 1]; False
[0, 1, 0, 0, 1, 0, 0, 0]; False
[0, 1, 0, 0, 1, 0, 0, 1]; False
[0, 1, 0, 0, 1, 0, 1, 0]; False
[0, 1, 0, 0, 1, 0, 1, 1]; False
[0, 1, 0, 0, 1, 1, 0, 0]; False
[0, 1, 0, 0, 1, 1, 0, 1]; False
[0, 1, 0, 0, 1, 1, 1, 0]; False
[0, 1, 0, 0, 1, 1, 1, 1]; False
[0, 1, 0, 1, 0, 0, 0, 0]; False
[0, 1, 0, 1, 0, 0, 0, 1]; False
[0, 1, 0, 1, 0, 0, 1, 0]; False
[0, 1, 0, 1, 0, 0, 1, 1]; False
[0, 1, 0, 1, 0, 1, 0, 0]; False
[0, 1, 0, 1, 0, 1, 0, 1]; False
[0, 1, 0, 1, 0, 1, 1, 0]; False
[0, 1, 0, 1, 0, 1, 1, 1]; False
[0, 1, 0, 1, 1, 0, 0, 0]; False
[0, 1, 0, 1, 1, 0, 0, 1]; False
[0, 1, 0, 1, 1, 0, 1, 0]; False
[0, 1, 0, 1, 1, 0, 1, 1]; False
[0, 1, 0, 1, 1, 1, 0, 0]; False
[0, 1, 0, 1, 1, 1, 0, 1]; False
[0, 1, 0, 1, 1, 1, 1, 0]; False
[0, 1, 0, 1, 1, 1, 1, 1]; False
[0, 1, 1, 0, 0, 0, 0, 0]; False
[0, 1, 1, 0, 0, 0, 0, 1]; False
[0, 1, 1, 0, 0, 0, 1, 0]; False
[0, 1, 1, 0, 0, 0, 1, 1]; True
[0, 1, 1, 0, 0, 1, 0, 0]; False
[0, 1, 1, 0, 0, 1, 0, 1]; True
[0, 1, 1, 0, 0, 1, 1, 0]; False
[0, 1, 1, 0, 0, 1, 1, 1]; False
[0, 1, 1, 0, 1, 0, 0, 0]; False
[0, 1, 1, 0, 1, 0, 0, 1]; True
[0, 1, 1, 0, 1, 0, 1, 0]; True
[0, 1, 1, 0, 1, 0, 1, 1]; True
[0, 1, 1, 0, 1, 1, 0, 0]; True
[0, 1, 1, 0, 1, 1, 0, 1]; True
[0, 1, 1, 0, 1, 1, 1, 0]; True
[0, 1, 1, 0, 1, 1, 1, 1]; True
[0, 1, 1, 1, 0, 0, 0, 0]; False
[0, 1, 1, 1, 0, 0, 0, 1]; False
[0, 1, 1, 1, 0, 0, 1, 0]; False
[0, 1, 1, 1, 0, 0, 1, 1]; False
[0, 1, 1, 1, 0, 1, 0, 0]; False
[0, 1, 1, 1, 0, 1, 0, 1]; False
[0, 1, 1, 1, 0, 1, 1, 0]; False
[0, 1, 1, 1, 0, 1, 1, 1]; False
[0, 1, 1, 1, 1, 0, 0, 0]; False
[0, 1, 1, 1, 1, 0, 0, 1]; False
[0, 1, 1, 1, 1, 0, 1, 0]; False
[0, 1, 1, 1, 1, 0, 1, 1]; True
[0, 1, 1, 1, 1, 1, 0, 0]; False
[0, 1, 1, 1, 1, 1, 0, 1]; True
[0, 1, 1, 1, 1, 1, 1, 0]; True
[0, 1, 1, 1, 1, 1, 1, 1]; True
[1, 0, 0, 0, 0, 0, 0, 0]; False
[1, 0, 0, 0, 0, 0, 0, 1]; False
[1, 0, 0, 0, 0, 0, 1, 0]; False
[1, 0, 0, 0, 0, 0, 1, 1]; False
[1, 0, 0, 0, 0, 1, 0, 0]; False
[1, 0, 0, 0, 0, 1, 0, 1]; False
[1, 0, 0, 0, 0, 1, 1, 0]; False
[1, 0, 0, 0, 0, 1, 1, 1]; False
[1, 0, 0, 0, 1, 0, 0, 0]; False
[1, 0, 0, 0, 1, 0, 0, 1]; False
[1, 0, 0, 0, 1, 0, 1, 0]; False
[1, 0, 0, 0, 1, 0, 1, 1]; False
[1, 0, 0, 0, 1, 1, 0, 0]; False
[1, 0, 0, 0, 1, 1, 0, 1]; False
[1, 0, 0, 0, 1, 1, 1, 0]; False
[1, 0, 0, 0, 1, 1, 1, 1]; False
[1, 0, 0, 1, 0, 0, 0, 0]; False
[1, 0, 0, 1, 0, 0, 0, 1]; False
[1, 0, 0, 1, 0, 0, 1, 0]; False
[1, 0, 0, 1, 0, 0, 1, 1]; False
[1, 0, 0, 1, 0, 1, 0, 0]; False
[1, 0, 0, 1, 0, 1, 0, 1]; False
[1, 0, 0, 1, 0, 1, 1, 0]; False
[1, 0, 0, 1, 0, 1, 1, 1]; False
[1, 0, 0, 1, 1, 0, 0, 0]; False
[1, 0, 0, 1, 1, 0, 0, 1]; False
[1, 0, 0, 1, 1, 0, 1, 0]; False
[1, 0, 0, 1, 1, 0, 1, 1]; False
[1, 0, 0, 1, 1, 1, 0, 0]; False
[1, 0, 0, 1, 1, 1, 0, 1]; False
[1, 0, 0, 1, 1, 1, 1, 0]; False
[1, 0, 0, 1, 1, 1, 1, 1]; False
[1, 0, 1, 0, 0, 0, 0, 0]; False
[1, 0, 1, 0, 0, 0, 0, 1]; False
[1, 0, 1, 0, 0, 0, 1, 0]; False
[1, 0, 1, 0, 0, 0, 1, 1]; False
[1, 0, 1, 0, 0, 1, 0, 0]; False
[1, 0, 1, 0, 0, 1, 0, 1]; False
[1, 0, 1, 0, 0, 1, 1, 0]; False
[1, 0, 1, 0, 0, 1, 1, 1]; False
[1, 0, 1, 0, 1, 0, 0, 0]; False
[1, 0, 1, 0, 1, 0, 0, 1]; False
[1, 0, 1, 0, 1, 0, 1, 0]; False
[1, 0, 1, 0, 1, 0, 1, 1]; False
[1, 0, 1, 0, 1, 1, 0, 0]; False
[1, 0, 1, 0, 1, 1, 0, 1]; False
[1, 0, 1, 0, 1, 1, 1, 0]; False
[1, 0, 1, 0, 1, 1, 1, 1]; False
[1, 0, 1, 1, 0, 0, 0, 0]; False
[1, 0, 1, 1, 0, 0, 0, 1]; False
[1, 0, 1, 1, 0, 0, 1, 0]; False
[1, 0, 1, 1, 0, 0, 1, 1]; False
[1, 0, 1, 1, 0, 1, 0, 0]; False
[1, 0, 1, 1, 0, 1, 0, 1]; False
[1, 0, 1, 1, 0, 1, 1, 0]; False
[1, 0, 1, 1, 0, 1, 1, 1]; False
[1, 0, 1, 1, 1, 0, 0, 0]; False
[1, 0, 1, 1, 1, 0, 0, 1]; False
[1, 0, 1, 1, 1, 0, 1, 0]; False
[1, 0, 1, 1, 1, 0, 1, 1]; False
[1, 0, 1, 1, 1, 1, 0, 0]; False
[1, 0, 1, 1, 1, 1, 0, 1]; False
[1, 0, 1, 1, 1, 1, 1, 0]; False
[1, 0, 1, 1, 1, 1, 1, 1]; False
[1, 1, 0, 0, 0, 0, 0, 0]; False
[1, 1, 0, 0, 0, 0, 0, 1]; False
[1, 1, 0, 0, 0, 0, 1, 0]; False
[1, 1, 0, 0, 0, 0, 1, 1]; False
[1, 1, 0, 0, 0, 1, 0, 0]; False
[1, 1, 0, 0, 0, 1, 0, 1]; False
[1, 1, 0, 0, 0, 1, 1, 0]; False
[1, 1, 0, 0, 0, 1, 1, 1]; False
[1, 1, 0, 0, 1, 0, 0, 0]; False
[1, 1, 0, 0, 1, 0, 0, 1]; False
[1, 1, 0, 0, 1, 0, 1, 0]; False
[1, 1, 0, 0, 1, 0, 1, 1]; False
[1, 1, 0, 0, 1, 1, 0, 0]; False
[1, 1, 0, 0, 1, 1, 0, 1]; False
[1, 1, 0, 0, 1, 1, 1, 0]; False
[1, 1, 0, 0, 1, 1, 1, 1]; False
[1, 1, 0, 1, 0, 0, 0, 0]; False
[1, 1, 0, 1, 0, 0, 0, 1]; False
[1, 1, 0, 1, 0, 0, 1, 0]; False
[1, 1, 0, 1, 0, 0, 1, 1]; False
[1, 1, 0, 1, 0, 1, 0, 0]; False
[1, 1, 0, 1, 0, 1, 0, 1]; False
[1, 1, 0, 1, 0, 1, 1, 0]; False
[1, 1, 0, 1, 0, 1, 1, 1]; False
[1, 1, 0, 1, 1, 0, 0, 0]; False
[1, 1, 0, 1, 1, 0, 0, 1]; False
[1, 1, 0, 1, 1, 0, 1, 0]; False
[1, 1, 0, 1, 1, 0, 1, 1]; False
[1, 1, 0, 1, 1, 1, 0, 0]; False
[1, 1, 0, 1, 1, 1, 0, 1]; False
[1, 1, 0, 1, 1, 1, 1, 0]; False
[1, 1, 0, 1, 1, 1, 1, 1]; False
[1, 1, 1, 0, 0, 0, 0, 0]; False
[1, 1, 1, 0, 0, 0, 0, 1]; False
[1, 1, 1, 0, 0, 0, 1, 0]; False
[1, 1, 1, 0, 0, 0, 1, 1]; False
[1, 1, 1, 0, 0, 1, 0, 0]; False
[1, 1, 1, 0, 0, 1, 0, 1]; False
[1, 1, 1, 0, 0, 1, 1, 0]; False
[1, 1, 1, 0, 0, 1, 1, 1]; False
[1, 1, 1, 0, 1, 0, 0, 0]; False
[1, 1, 1, 0, 1, 0, 0, 1]; False
[1, 1, 1, 0, 1, 0, 1, 0]; False
[1, 1, 1, 0, 1, 0, 1, 1]; False
[1, 1, 1, 0, 1, 1, 0, 0]; False
[1, 1, 1, 0, 1, 1, 0, 1]; False
[1, 1, 1, 0, 1, 1, 1, 0]; False
[1, 1, 1, 0, 1, 1, 1, 1]; False
[1, 1, 1, 1, 0, 0, 0, 0]; False
[1, 1, 1, 1, 0, 0, 0, 1]; False
[1, 1, 1, 1, 0, 0, 1, 0]; False
[1, 1, 1, 1, 0, 0, 1, 1]; False
[1, 1, 1, 1, 0, 1, 0, 0]; False
[1, 1, 1, 1, 0, 1, 0, 1]; False
[1, 1, 1, 1, 0, 1, 1, 0]; False
[1, 1, 1, 1, 0, 1, 1, 1]; False
[1, 1, 1, 1, 1, 0, 0, 0]; False
[1, 1, 1, 1, 1, 0, 0, 1]; False
[1, 1, 1, 1, 1, 0, 1, 0]; False
[1, 1, 1, 1, 1, 0, 1, 1]; False
[1, 1, 1, 1, 1, 1, 0, 0]; False
[1, 1, 1, 1, 1, 1, 0, 1]; False
[1, 1, 1, 1, 1, 1, 1, 0]; False
[1, 1, 1, 1, 1, 1, 1, 1]; False
[0, 0, 0, 0, 0, 0, 0, 0, 0]; False
[0, 0, 0, 0, 0, 0, 0, 0, 1]; False
[0, 0, 0, 0, 0, 0, 0, 1, 0]; False
[0, 0, 0, 0, 0, 0, 0, 1, 1]; False
[0, 0, 0, 0, 0, 0, 1, 0, 0]; False
[0, 0, 0, 0, 0, 0, 1, 0, 1]; False
[0, 0, 0, 0, 0, 0, 1, 1, 0]; False
[0, 0, 0, 0, 0, 0, 1, 1, 1]; False
[0, 0, 0, 0, 0, 1, 0, 0, 0]; False
[0, 0, 0, 0, 0, 1, 0, 0, 1]; False
[0, 0, 0, 0, 0, 1, 0, 1, 0]; False
[0, 0, 0, 0, 0, 1, 0, 1, 1]; False
[0, 0, 0, 0, 0, 1, 1, 0, 0]; False
[0, 0, 0, 0, 0, 1, 1, 0, 1]; False
[0, 0, 0, 0, 0, 1, 1, 1, 0]; False
[0, 0, 0, 0, 0, 1, 1, 1, 1]; False
[0, 0, 0, 0, 1, 0, 0, 0, 0]; False
[0, 0, 0, 0, 1, 0, 0, 0, 1]; False
[0, 0, 0, 0, 1, 0, 0, 1, 0]; False
[0, 0, 0, 0, 1, 0, 0, 1, 1]; False
[0, 0, 0, 0, 1, 0, 1, 0, 0]; False
[0, 0, 0, 0, 1, 0, 1, 0, 1]; False
[0, 0, 0, 0, 1, 0, 1, 1, 0]; False
[0, 0, 0, 0, 1, 0, 1, 1, 1]; False
[0, 0, 0, 0, 1, 1, 0, 0, 0]; False
[0, 0, 0, 0, 1, 1, 0, 0, 1]; False
[0, 0, 0, 0, 1, 1, 0, 1, 0]; False
[0, 0, 0, 0, 1, 1, 0, 1, 1]; False
[0, 0, 0, 0, 1, 1, 1, 0, 0]; False
[0, 0, 0, 0, 1, 1, 1, 0, 1]; False
[0, 0, 0, 0, 1, 1, 1, 1, 0]; False
[0, 0, 0, 0, 1, 1, 1, 1, 1]; False
[0, 0, 0, 1, 0, 0, 0, 0, 0]; False
[0, 0, 0, 1, 0, 0, 0, 0, 1]; False
[0, 0, 0, 1, 0, 0, 0, 1, 0]; False
[0, 0, 0, 1, 0, 0, 0, 1, 1]; False
[0, 0, 0, 1, 0, 0, 1, 0, 0]; False
[0, 0, 0, 1, 0, 0, 1, 0, 1]; False
[0, 0, 0, 1, 0, 0, 1, 1, 0]; False
[0, 0, 0, 1, 0, 0, 1, 1, 1]; False
[0, 0, 0, 1, 0, 1, 0, 0, 0]; False
[0, 0, 0, 1, 0, 1, 0, 0, 1]; False
[0, 0, 0, 1, 0, 1, 0, 1, 0]; False
[0, 0, 0, 1, 0, 1, 0, 1, 1]; False
[0, 0, 0, 1, 0, 1, 1, 0, 0]; False
[0, 0, 0, 1, 0, 1, 1, 0, 1]; False
[0, 0, 0, 1, 0, 1, 1, 1, 0]; False
[0, 0, 0, 1, 0, 1, 1, 1, 1]; False
[0, 0, 0, 1, 1, 0, 0, 0, 0]; False
[0, 0, 0, 1, 1, 0, 0, 0, 1]; False
[0, 0, 0, 1, 1, 0, 0, 1, 0]; False
[0, 0, 0, 1, 1, 0, 0, 1, 1]; False
[0, 0, 0, 1, 1, 0, 1, 0, 0]; False
[0, 0, 0, 1, 1, 0, 1, 0, 1]; False
[0, 0, 0, 1, 1, 0, 1, 1, 0]; False
[0, 0, 0, 1, 1, 0, 1, 1, 1]; False
[0, 0, 0, 1, 1, 1, 0, 0, 0]; False
[0, 0, 0, 1, 1, 1, 0, 0, 1]; False
[0, 0, 0, 1, 1, 1, 0, 1, 0]; False
[0, 0, 0, 1, 1, 1, 0, 1, 1]; False
[0, 0, 0, 1, 1, 1, 1, 0, 0]; False
[0, 0, 0, 1, 1, 1, 1, 0, 1]; False
[0, 0, 0, 1, 1, 1, 1, 1, 0]; False
[0, 0, 0, 1, 1, 1, 1, 1, 1]; False
[0, 0, 1, 0, 0, 0, 0, 0, 0]; False
[0, 0, 1, 0, 0, 0, 0, 0, 1]; False
[0, 0, 1, 0, 0, 0, 0, 1, 0]; False
[0, 0, 1, 0, 0, 0, 0, 1, 1]; False
[0, 0, 1, 0, 0, 0, 1, 0, 0]; False
[0, 0, 1, 0, 0, 0, 1, 0, 1]; False
[0, 0, 1, 0, 0, 0, 1, 1, 0]; False
[0, 0, 1, 0, 0, 0, 1, 1, 1]; False
[0, 0, 1, 0, 0, 1, 0, 0, 0]; False
[0, 0, 1, 0, 0, 1, 0, 0, 1]; False
[0, 0, 1, 0, 0, 1, 0, 1, 0]; False
[0, 0, 1, 0, 0, 1, 0, 1, 1]; False
[0, 0, 1, 0, 0, 1, 1, 0, 0]; False
[0, 0, 1, 0, 0, 1, 1, 0, 1]; False
[0, 0, 1, 0, 0, 1, 1, 1, 0]; False
[0, 0, 1, 0, 0, 1, 1, 1, 1]; False
[0, 0, 1, 0, 1, 0, 0, 0, 0]; False
[0, 0, 1, 0, 1, 0, 0, 0, 1]; False
[0, 0, 1, 0, 1, 0, 0, 1, 0]; False
[0, 0, 1, 0, 1, 0, 0, 1, 1]; False
[0, 0, 1, 0, 1, 0, 1, 0, 0]; False
[0, 0, 1, 0, 1, 0, 1, 0, 1]; False
[0, 0, 1, 0, 1, 0, 1, 1, 0]; False
[0, 0, 1, 0, 1, 0, 1, 1, 1]; False
[0, 0, 1, 0, 1, 1, 0, 0, 0]; False
[0, 0, 1, 0, 1, 1, 0, 0, 1]; False
[0, 0, 1, 0, 1, 1, 0, 1, 0]; False
[0, 0, 1, 0, 1, 1, 0, 1, 1]; False
[0, 0, 1, 0, 1, 1, 1, 0, 0]; False
[0, 0, 1, 0, 1, 1, 1, 0, 1]; False
[0, 0, 1, 0, 1, 1, 1, 1, 0]; False
[0, 0, 1, 0, 1, 1, 1, 1, 1]; False
[0, 0, 1, 1, 0, 0, 0, 0, 0]; False
[0, 0, 1, 1, 0, 0, 0, 0, 1]; False
[0, 0, 1, 1, 0, 0, 0, 1, 0]; False
[0, 0, 1, 1, 0, 0, 0, 1, 1]; False
[0, 0, 1, 1, 0, 0, 1, 0, 0]; False
[0, 0, 1, 1, 0, 0, 1, 0, 1]; False
[0, 0, 1, 1, 0, 0, 1, 1, 0]; False
[0, 0, 1, 1, 0, 0, 1, 1, 1]; False
[0, 0, 1, 1, 0, 1, 0, 0, 0]; False
[0, 0, 1, 1, 0, 1, 0, 0, 1]; False
[0, 0, 1, 1, 0, 1, 0, 1, 0]; False
[0, 0, 1, 1, 0, 1, 0, 1, 1]; False
[0, 0, 1, 1, 0, 1, 1, 0, 0]; False
[0, 0, 1, 1, 0, 1, 1, 0, 1]; False
[0, 0, 1, 1, 0, 1, 1, 1, 0]; False
[0, 0, 1, 1, 0, 1, 1, 1, 1]; False
[0, 0, 1, 1, 1, 0, 0, 0, 0]; False
[0, 0, 1, 1, 1, 0, 0, 0, 1]; False
[0, 0, 1, 1, 1, 0, 0, 1, 0]; False
[0, 0, 1, 1, 1, 0, 0, 1, 1]; False
[0, 0, 1, 1, 1, 0, 1, 0, 0]; False
[0, 0, 1, 1, 1, 0, 1, 0, 1]; False
[0, 0, 1, 1, 1, 0, 1, 1, 0]; False
[0, 0, 1, 1, 1, 0, 1, 1, 1]; False
[0, 0, 1, 1, 1, 1, 0, 0, 0]; False
[0, 0, 1, 1, 1, 1, 0, 0, 1]; False
[0, 0, 1, 1, 1, 1, 0, 1, 0]; False
[0, 0, 1, 1, 1, 1, 0, 1, 1]; False
[0, 0, 1, 1, 1, 1, 1, 0, 0]; False
[0, 0, 1, 1, 1, 1, 1, 0, 1]; False
[0, 0, 1, 1, 1, 1, 1, 1, 0]; False
[0, 0, 1, 1, 1, 1, 1, 1, 1]; False
[0, 1, 0, 0, 0, 0, 0, 0, 0]; False
[0, 1, 0, 0, 0, 0, 0, 0, 1]; False
[0, 1, 0, 0, 0, 0, 0, 1, 0]; False
[0, 1, 0, 0, 0, 0, 0, 1, 1]; False
[0, 1, 0, 0, 0, 0, 1, 0, 0]; False
[0, 1, 0, 0, 0, 0, 1, 0, 1]; False
[0, 1, 0, 0, 0, 0, 1, 1, 0]; False
[0, 1, 0, 0, 0, 0, 1, 1, 1]; False
[0, 1, 0, 0, 0, 1, 0, 0, 0]; False
[0, 1, 0, 0, 0, 1, 0, 0, 1]; False
[0, 1, 0, 0, 0, 1, 0, 1, 0]; False
[0, 1, 0, 0, 0, 1, 0, 1, 1]; False
[0, 1, 0, 0, 0, 1, 1, 0, 0]; False
[0, 1, 0, 0, 0, 1, 1, 0, 1]; False
[0, 1, 0, 0, 0, 1, 1, 1, 0]; False
[0, 1, 0, 0, 0, 1, 1, 1, 1]; False
[0, 1, 0, 0, 1, 0, 0, 0, 0]; False
[0, 1, 0, 0, 1, 0, 0, 0, 1]; False
[0, 1, 0, 0, 1, 0, 0, 1, 0]; False
[0, 1, 0, 0, 1, 0, 0, 1, 1]; False
[0, 1, 0, 0, 1, 0, 1, 0, 0]; False
[0, 1, 0, 0, 1, 0, 1, 0, 1]; False
[0, 1, 0, 0, 1, 0, 1, 1, 0]; False
[0, 1, 0, 0, 1, 0, 1, 1, 1]; False
[0, 1, 0, 0, 1, 1, 0, 0, 0]; False
[0, 1, 0, 0, 1, 1, 0, 0, 1]; False
[0, 1, 0, 0, 1, 1, 0, 1, 0]; False
[0, 1, 0, 0, 1, 1, 0, 1, 1]; False
[0, 1, 0, 0, 1, 1, 1, 0, 0]; False
[0, 1, 0, 0, 1, 1, 1, 0, 1]; False
[0, 1, 0, 0, 1, 1, 1, 1, 0]; False
[0, 1, 0, 0, 1, 1, 1, 1, 1]; False
[0, 1, 0, 1, 0, 0, 0, 0, 0]; False
[0, 1, 0, 1, 0, 0, 0, 0, 1]; False
[0, 1, 0, 1, 0, 0, 0, 1, 0]; False
[0, 1, 0, 1, 0, 0, 0, 1, 1]; False
[0, 1, 0, 1, 0, 0, 1, 0, 0]; False
[0, 1, 0, 1, 0, 0, 1, 0, 1]; False
[0, 1, 0, 1, 0, 0, 1, 1, 0]; False
[0, 1, 0, 1, 0, 0, 1, 1, 1]; False
[0, 1, 0, 1, 0, 1, 0, 0, 0]; False
[0, 1, 0, 1, 0, 1, 0, 0, 1]; False
[0, 1, 0, 1, 0, 1, 0, 1, 0]; False
[0, 1, 0, 1, 0, 1, 0, 1, 1]; False
[0, 1, 0, 1, 0, 1, 1, 0, 0]; False
[0, 1, 0, 1, 0, 1, 1, 0, 1]; False
[0, 1, 0, 1, 0, 1, 1, 1, 0]; False
[0, 1, 0, 1, 0, 1, 1, 1, 1]; False
[0, 1, 0, 1, 1, 0, 0, 0, 0]; False
[0, 1, 0, 1, 1, 0, 0, 0, 1]; False
[0, 1, 0, 1, 1, 0, 0, 1, 0]; False
[0, 1, 0, 1, 1, 0, 0, 1, 1]; False
[0, 1, 0, 1, 1, 0, 1, 0, 0]; False
[0, 1, 0, 1, 1, 0, 1, 0, 1]; False
[0, 1, 0, 1, 1, 0, 1, 1, 0]; False
[0, 1, 0, 1, 1, 0, 1, 1, 1]; False
[0, 1, 0, 1, 1, 1, 0, 0, 0]; False
[0, 1, 0, 1, 1, 1, 0, 0, 1]; False
[0, 1, 0, 1, 1, 1, 0, 1, 0]; False
[0, 1, 0, 1, 1, 1, 0, 1, 1]; False
[0, 1, 0, 1, 1, 1, 1, 0, 0]; False
[0, 1, 0, 1, 1, 1, 1, 0, 1]; False
[0, 1, 0, 1, 1, 1, 1, 1, 0]; False
[0, 1, 0, 1, 1, 1, 1, 1, 1]; False
[0, 1, 1, 0, 0, 0, 0, 0, 0]; False
[0, 1, 1, 0, 0, 0, 0, 0, 1]; False
[0, 1, 1, 0, 0, 0, 0, 1, 0]; False
[0, 1, 1, 0, 0, 0, 0, 1, 1]; False
[0, 1, 1, 0, 0, 0, 1, 0, 0]; False
[0, 1, 1, 0, 0, 0, 1, 0, 1]; False
[0, 1, 1, 0, 0, 0, 1, 1, 0]; False
[0, 1, 1, 0, 0, 0, 1, 1, 1]; False
[0, 1, 1, 0, 0, 1, 0, 0, 0]; False
[0, 1, 1, 0, 0, 1, 0, 0, 1]; False
[0, 1, 1, 0, 0, 1, 0, 1, 0]; False
[0, 1, 1, 0, 0, 1, 0, 1, 1]; False
[0, 1, 1, 0, 0, 1, 1, 0, 0]; False
[0, 1, 1, 0, 0, 1, 1, 0, 1]; False
[0, 1, 1, 0, 0, 1, 1, 1, 0]; False
[0, 1, 1, 0, 0, 1, 1, 1, 1]; False
[0, 1, 1, 0, 1, 0, 0, 0, 0]; False
[0, 1, 1, 0, 1, 0, 0, 0, 1]; False
[0, 1, 1, 0, 1, 0, 0, 1, 0]; False
[0, 1, 1, 0, 1, 0, 0, 1, 1]; False
[0, 1, 1, 0, 1, 0, 1, 0, 0]; False
[0, 1, 1, 0, 1, 0, 1, 0, 1]; False
[0, 1, 1, 0, 1, 0, 1, 1, 0]; False
[0, 1, 1, 0, 1, 0, 1, 1, 1]; False
[0, 1, 1, 0, 1, 1, 0, 0, 0]; False
[0, 1, 1, 0, 1, 1, 0, 0, 1]; False
[0, 1, 1, 0, 1, 1, 0, 1, 0]; False
[0, 1, 1, 0, 1, 1, 0, 1, 1]; False
[0, 1, 1, 0, 1, 1, 1, 0, 0]; False
[0, 1, 1, 0, 1, 1, 1, 0, 1]; False
[0, 1, 1, 0, 1, 1, 1, 1, 0]; False
[0, 1, 1, 0, 1, 1, 1, 1, 1]; False
[0, 1, 1, 1, 0, 0, 0, 0, 0]; False
[0, 1, 1, 1, 0, 0, 0, 0, 1]; False
[0, 1, 1, 1, 0, 0, 0, 1, 0]; False
[0, 1, 1, 1, 0, 0, 0, 1, 1]; True
[0, 1, 1, 1, 0, 0, 1, 0, 0]; False
[0, 1, 1, 1, 0, 0, 1, 0, 1]; True
[0, 1, 1, 1, 0, 0, 1, 1, 0]; False
[0, 1, 1, 1, 0, 0, 1, 1, 1]; False
[0, 1, 1, 1, 0, 1, 0, 0, 0]; False
[0, 1, 1, 1, 0, 1, 0, 0, 1]; True
[0, 1, 1, 1, 0, 1, 0, 1, 0]; True
[0, 1, 1, 1, 0, 1, 0, 1, 1]; True
[0, 1, 1, 1, 0, 1, 1, 0, 0]; True
[0, 1, 1, 1, 0, 1, 1, 0, 1]; True
[0, 1, 1, 1, 0, 1, 1, 1, 0]; True
[0, 1, 1, 1, 0, 1, 1, 1, 1]; True
[0, 1, 1, 1, 1, 0, 0, 0, 0]; False
[0, 1, 1, 1, 1, 0, 0, 0, 1]; False
[0, 1, 1, 1, 1, 0, 0, 1, 0]; False
[0, 1, 1, 1, 1, 0, 0, 1, 1]; False
[0, 1, 1, 1, 1, 0, 1, 0, 0]; False
[0, 1, 1, 1, 1, 0, 1, 0, 1]; False
[0, 1, 1, 1, 1, 0, 1, 1, 0]; False
[0, 1, 1, 1, 1, 0, 1, 1, 1]; False
[0, 1, 1, 1, 1, 1, 0, 0, 0]; False
[0, 1, 1, 1, 1, 1, 0, 0, 1]; False
[0, 1, 1, 1, 1, 1, 0, 1, 0]; False
[0, 1, 1, 1, 1, 1, 0, 1, 1]; True
[0, 1, 1, 1, 1, 1, 1, 0, 0]; False
[0, 1, 1, 1, 1, 1, 1, 0, 1]; True
[0, 1, 1, 1, 1, 1, 1, 1, 0]; True
[0, 1, 1, 1, 1, 1, 1, 1, 1]; True
[1, 0, 0, 0, 0, 0, 0, 0, 0]; False
[1, 0, 0, 0, 0, 0, 0, 0, 1]; False
[1, 0, 0, 0, 0, 0, 0, 1, 0]; False
[1, 0, 0, 0, 0, 0, 0, 1, 1]; False
[1, 0, 0, 0, 0, 0, 1, 0, 0]; False
[1, 0, 0, 0, 0, 0, 1, 0, 1]; False
[1, 0, 0, 0, 0, 0, 1, 1, 0]; False
[1, 0, 0, 0, 0, 0, 1, 1, 1]; False
[1, 0, 0, 0, 0, 1, 0, 0, 0]; False
[1, 0, 0, 0, 0, 1, 0, 0, 1]; False
[1, 0, 0, 0, 0, 1, 0, 1, 0]; False
[1, 0, 0, 0, 0, 1, 0, 1, 1]; False
[1, 0, 0, 0, 0, 1, 1, 0, 0]; False
[1, 0, 0, 0, 0, 1, 1, 0, 1]; False
[1, 0, 0, 0, 0, 1, 1, 1, 0]; False
[1, 0, 0, 0, 0, 1, 1, 1, 1]; False
[1, 0, 0, 0, 1, 0, 0, 0, 0]; False
[1, 0, 0, 0, 1, 0, 0, 0, 1]; False
[1, 0, 0, 0, 1, 0, 0, 1, 0]; False
[1, 0, 0, 0, 1, 0, 0, 1, 1]; False
[1, 0, 0, 0, 1, 0, 1, 0, 0]; False
[1, 0, 0, 0, 1, 0, 1, 0, 1]; False
[1, 0, 0, 0, 1, 0, 1, 1, 0]; False
[1, 0, 0, 0, 1, 0, 1, 1, 1]; False
[1, 0, 0, 0, 1, 1, 0, 0, 0]; False
[1, 0, 0, 0, 1, 1, 0, 0, 1]; False
[1, 0, 0, 0, 1, 1, 0, 1, 0]; False
[1, 0, 0, 0, 1, 1, 0, 1, 1]; False
[1, 0, 0, 0, 1, 1, 1, 0, 0]; False
[1, 0, 0, 0, 1, 1, 1, 0, 1]; False
[1, 0, 0, 0, 1, 1, 1, 1, 0]; False
[1, 0, 0, 0, 1, 1, 1, 1, 1]; False
[1, 0, 0, 1, 0, 0, 0, 0, 0]; False
[1, 0, 0, 1, 0, 0, 0, 0, 1]; False
[1, 0, 0, 1, 0, 0, 0, 1, 0]; False
[1, 0, 0, 1, 0, 0, 0, 1, 1]; False
[1, 0, 0, 1, 0, 0, 1, 0, 0]; False
[1, 0, 0, 1, 0, 0, 1, 0, 1]; False
[1, 0, 0, 1, 0, 0, 1, 1, 0]; False
[1, 0, 0, 1, 0, 0, 1, 1, 1]; False
[1, 0, 0, 1, 0, 1, 0, 0, 0]; False
[1, 0, 0, 1, 0, 1, 0, 0, 1]; False
[1, 0, 0, 1, 0, 1, 0, 1, 0]; False
[1, 0, 0, 1, 0, 1, 0, 1, 1]; False
[1, 0, 0, 1, 0, 1, 1, 0, 0]; False
[1, 0, 0, 1, 0, 1, 1, 0, 1]; False
[1, 0, 0, 1, 0, 1, 1, 1, 0]; False
[1, 0, 0, 1, 0, 1, 1, 1, 1]; False
[1, 0, 0, 1, 1, 0, 0, 0, 0]; False
[1, 0, 0, 1, 1, 0, 0, 0, 1]; False
[1, 0, 0, 1, 1, 0, 0, 1, 0]; False
[1, 0, 0, 1, 1, 0, 0, 1, 1]; False
[1, 0, 0, 1, 1, 0, 1, 0, 0]; False
[1, 0, 0, 1, 1, 0, 1, 0, 1]; False
[1, 0, 0, 1, 1, 0, 1, 1, 0]; False
[1, 0, 0, 1, 1, 0, 1, 1, 1]; False
[1, 0, 0, 1, 1, 1, 0, 0, 0]; False
[1, 0, 0, 1, 1, 1, 0, 0, 1]; False
[1, 0, 0, 1, 1, 1, 0, 1, 0]; False
[1, 0, 0, 1, 1, 1, 0, 1, 1]; False
[1, 0, 0, 1, 1, 1, 1, 0, 0]; False
[1, 0, 0, 1, 1, 1, 1, 0, 1]; False
[1, 0, 0, 1, 1, 1, 1, 1, 0]; False
[1, 0, 0, 1, 1, 1, 1, 1, 1]; False
[1, 0, 1, 0, 0, 0, 0, 0, 0]; False
[1, 0, 1, 0, 0, 0, 0, 0, 1]; False
[1, 0, 1, 0, 0, 0, 0, 1, 0]; False
[1, 0, 1, 0, 0, 0, 0, 1, 1]; False
[1, 0, 1, 0, 0, 0, 1, 0, 0]; False
[1, 0, 1, 0, 0, 0, 1, 0, 1]; False
[1, 0, 1, 0, 0, 0, 1, 1, 0]; False
[1, 0, 1, 0, 0, 0, 1, 1, 1]; False
[1, 0, 1, 0, 0, 1, 0, 0, 0]; False
[1, 0, 1, 0, 0, 1, 0, 0, 1]; False
[1, 0, 1, 0, 0, 1, 0, 1, 0]; False
[1, 0, 1, 0, 0, 1, 0, 1, 1]; False
[1, 0, 1, 0, 0, 1, 1, 0, 0]; False
[1, 0, 1, 0, 0, 1, 1, 0, 1]; False
[1, 0, 1, 0, 0, 1, 1, 1, 0]; False
[1, 0, 1, 0, 0, 1, 1, 1, 1]; False
[1, 0, 1, 0, 1, 0, 0, 0, 0]; False
[1, 0, 1, 0, 1, 0, 0, 0, 1]; False
[1, 0, 1, 0, 1, 0, 0, 1, 0]; False
[1, 0, 1, 0, 1, 0, 0, 1, 1]; False
[1, 0, 1, 0, 1, 0, 1, 0, 0]; False
[1, 0, 1, 0, 1, 0, 1, 0, 1]; False
[1, 0, 1, 0, 1, 0, 1, 1, 0]; False
[1, 0, 1, 0, 1, 0, 1, 1, 1]; False
[1, 0, 1, 0, 1, 1, 0, 0, 0]; False
[1, 0, 1, 0, 1, 1, 0, 0, 1]; False
[1, 0, 1, 0, 1, 1, 0, 1, 0]; False
[1, 0, 1, 0, 1, 1, 0, 1, 1]; False
[1, 0, 1, 0, 1, 1, 1, 0, 0]; False
[1, 0, 1, 0, 1, 1, 1, 0, 1]; False
[1, 0, 1, 0, 1, 1, 1, 1, 0]; False
[1, 0, 1, 0, 1, 1, 1, 1, 1]; False
[1, 0, 1, 1, 0, 0, 0, 0, 0]; False
[1, 0, 1, 1, 0, 0, 0, 0, 1]; False
[1, 0, 1, 1, 0, 0, 0, 1, 0]; False
[1, 0, 1, 1, 0, 0, 0, 1, 1]; False
[1, 0, 1, 1, 0, 0, 1, 0, 0]; False
[1, 0, 1, 1, 0, 0, 1, 0, 1]; False
[1, 0, 1, 1, 0, 0, 1, 1, 0]; False
[1, 0, 1, 1, 0, 0, 1, 1, 1]; False
[1, 0, 1, 1, 0, 1, 0, 0, 0]; False
[1, 0, 1, 1, 0, 1, 0, 0, 1]; False
[1, 0, 1, 1, 0, 1, 0, 1, 0]; False
[1, 0, 1, 1, 0, 1, 0, 1, 1]; False
[1, 0, 1, 1, 0, 1, 1, 0, 0]; False
[1, 0, 1, 1, 0, 1, 1, 0, 1]; False
[1, 0, 1, 1, 0, 1, 1, 1, 0]; False
[1, 0, 1, 1, 0, 1, 1, 1, 1]; False
[1, 0, 1, 1, 1, 0, 0, 0, 0]; False
[1, 0, 1, 1, 1, 0, 0, 0, 1]; False
[1, 0, 1, 1, 1, 0, 0, 1, 0]; False
[1, 0, 1, 1, 1, 0, 0, 1, 1]; False
[1, 0, 1, 1, 1, 0, 1, 0, 0]; False
[1, 0, 1, 1, 1, 0, 1, 0, 1]; False
[1, 0, 1, 1, 1, 0, 1, 1, 0]; False
[1, 0, 1, 1, 1, 0, 1, 1, 1]; False
[1, 0, 1, 1, 1, 1, 0, 0, 0]; False
[1, 0, 1, 1, 1, 1, 0, 0, 1]; False
[1, 0, 1, 1, 1, 1, 0, 1, 0]; False
[1, 0, 1, 1, 1, 1, 0, 1, 1]; False
[1, 0, 1, 1, 1, 1, 1, 0, 0]; False
[1, 0, 1, 1, 1, 1, 1, 0, 1]; False
[1, 0, 1, 1, 1, 1, 1, 1, 0]; False
[1, 0, 1, 1, 1, 1, 1, 1, 1]; False
[1, 1, 0, 0, 0, 0, 0, 0, 0]; False
[1, 1, 0, 0, 0, 0, 0, 0, 1]; False
[1, 1, 0, 0, 0, 0, 0, 1, 0]; False
[1, 1, 0, 0, 0, 0, 0, 1, 1]; False
[1, 1, 0, 0, 0, 0, 1, 0, 0]; False
[1, 1, 0, 0, 0, 0, 1, 0, 1]; False
[1, 1, 0, 0, 0, 0, 1, 1, 0]; False
[1, 1, 0, 0, 0, 0, 1, 1, 1]; False
[1, 1, 0, 0, 0, 1, 0, 0, 0]; False
[1, 1, 0, 0, 0, 1, 0, 0, 1]; False
[1, 1, 0, 0, 0, 1, 0, 1, 0]; False
[1, 1, 0, 0, 0, 1, 0, 1, 1]; False
[1, 1, 0, 0, 0, 1, 1, 0, 0]; False
[1, 1, 0, 0, 0, 1, 1, 0, 1]; False
[1, 1, 0, 0, 0, 1, 1, 1, 0]; False
[1, 1, 0, 0, 0, 1, 1, 1, 1]; False
[1, 1, 0, 0, 1, 0, 0, 0, 0]; False
[1, 1, 0, 0, 1, 0, 0, 0, 1]; False
[1, 1, 0, 0, 1, 0, 0, 1, 0]; False
[1, 1, 0, 0, 1, 0, 0, 1, 1]; False
[1, 1, 0, 0, 1, 0, 1, 0, 0]; False
[1, 1, 0, 0, 1, 0, 1, 0, 1]; False
[1, 1, 0, 0, 1, 0, 1, 1, 0]; False
[1, 1, 0, 0, 1, 0, 1, 1, 1]; False
[1, 1, 0, 0, 1, 1, 0, 0, 0]; False
[1, 1, 0, 0, 1, 1, 0, 0, 1]; False
[1, 1, 0, 0, 1, 1, 0, 1, 0]; False
[1, 1, 0, 0, 1, 1, 0, 1, 1]; False
[1, 1, 0, 0, 1, 1, 1, 0, 0]; False
[1, 1, 0, 0, 1, 1, 1, 0, 1]; False
[1, 1, 0, 0, 1, 1, 1, 1, 0]; False
[1, 1, 0, 0, 1, 1, 1, 1, 1]; False
[1, 1, 0, 1, 0, 0, 0, 0, 0]; False
[1, 1, 0, 1, 0, 0, 0, 0, 1]; False
[1, 1, 0, 1, 0, 0, 0, 1, 0]; False
[1, 1, 0, 1, 0, 0, 0, 1, 1]; False
[1, 1, 0, 1, 0, 0, 1, 0, 0]; False
[1, 1, 0, 1, 0, 0, 1, 0, 1]; False
[1, 1, 0, 1, 0, 0, 1, 1, 0]; False
[1, 1, 0, 1, 0, 0, 1, 1, 1]; False
[1, 1, 0, 1, 0, 1, 0, 0, 0]; False
[1, 1, 0, 1, 0, 1, 0, 0, 1]; False
[1, 1, 0, 1, 0, 1, 0, 1, 0]; False
[1, 1, 0, 1, 0, 1, 0, 1, 1]; False
[1, 1, 0, 1, 0, 1, 1, 0, 0]; False
[1, 1, 0, 1, 0, 1, 1, 0, 1]; False
[1, 1, 0, 1, 0, 1, 1, 1, 0]; False
[1, 1, 0, 1, 0, 1, 1, 1, 1]; False
[1, 1, 0, 1, 1, 0, 0, 0, 0]; False
[1, 1, 0, 1, 1, 0, 0, 0, 1]; False
[1, 1, 0, 1, 1, 0, 0, 1, 0]; False
[1, 1, 0, 1, 1, 0, 0, 1, 1]; False
[1, 1, 0, 1, 1, 0, 1, 0, 0]; False
[1, 1, 0, 1, 1, 0, 1, 0, 1]; False
[1, 1, 0, 1, 1, 0, 1, 1, 0]; False
[1, 1, 0, 1, 1, 0, 1, 1, 1]; False
[1, 1, 0, 1, 1, 1, 0, 0, 0]; False
[1, 1, 0, 1, 1, 1, 0, 0, 1]; False
[1, 1, 0, 1, 1, 1, 0, 1, 0]; False
[1, 1, 0, 1, 1, 1, 0, 1, 1]; False
[1, 1, 0, 1, 1, 1, 1, 0, 0]; False
[1, 1, 0, 1, 1, 1, 1, 0, 1]; False
[1, 1, 0, 1, 1, 1, 1, 1, 0]; False
[1, 1, 0, 1, 1, 1, 1, 1, 1]; False
[1, 1, 1, 0, 0, 0, 0, 0, 0]; False
[1, 1, 1, 0, 0, 0, 0, 0, 1]; False
[1, 1, 1, 0, 0, 0, 0, 1, 0]; False
[1, 1, 1, 0, 0, 0, 0, 1, 1]; False
[1, 1, 1, 0, 0, 0, 1, 0, 0]; False
[1, 1, 1, 0, 0, 0, 1, 0, 1]; False
[1, 1, 1, 0, 0, 0, 1, 1, 0]; False
[1, 1, 1, 0, 0, 0, 1, 1, 1]; False
[1, 1, 1, 0, 0, 1, 0, 0, 0]; False
[1, 1, 1, 0, 0, 1, 0, 0, 1]; False
[1, 1, 1, 0, 0, 1, 0, 1, 0]; False
[1, 1, 1, 0, 0, 1, 0, 1, 1]; False
[1, 1, 1, 0, 0, 1, 1, 0, 0]; False
[1, 1, 1, 0, 0, 1, 1, 0, 1]; False
[1, 1, 1, 0, 0, 1, 1, 1, 0]; False
[1, 1, 1, 0, 0, 1, 1, 1, 1]; False
[1, 1, 1, 0, 1, 0, 0, 0, 0]; False
[1, 1, 1, 0, 1, 0, 0, 0, 1]; False
[1, 1, 1, 0, 1, 0, 0, 1, 0]; False
[1, 1, 1, 0, 1, 0, 0, 1, 1]; False
[1, 1, 1, 0, 1, 0, 1, 0, 0]; False
[1, 1, 1, 0, 1, 0, 1, 0, 1]; False
[1, 1, 1, 0, 1, 0, 1, 1, 0]; False
[1, 1, 1, 0, 1, 0, 1, 1, 1]; False
[1, 1, 1, 0, 1, 1, 0, 0, 0]; False
[1, 1, 1, 0, 1, 1, 0, 0, 1]; False
[1, 1, 1, 0, 1, 1, 0, 1, 0]; False
[1, 1, 1, 0, 1, 1, 0, 1, 1]; False
[1, 1, 1, 0, 1, 1, 1, 0, 0]; False
[1, 1, 1, 0, 1, 1, 1, 0, 1]; False
[1, 1, 1, 0, 1, 1, 1, 1, 0]; False
[1, 1, 1, 0, 1, 1, 1, 1, 1]; False
[1, 1, 1, 1, 0, 0, 0, 0, 0]; False
[1, 1, 1, 1, 0, 0, 0, 0, 1]; False
[1, 1, 1, 1, 0, 0, 0, 1, 0]; False
[1, 1, 1, 1, 0, 0, 0, 1, 1]; False
[1, 1, 1, 1, 0, 0, 1, 0, 0]; False
[1, 1, 1, 1, 0, 0, 1, 0, 1]; False
[1, 1, 1, 1, 0, 0, 1, 1, 0]; False
[1, 1, 1, 1, 0, 0, 1, 1, 1]; False
[1, 1, 1, 1, 0, 1, 0, 0, 0]; False
[1, 1, 1, 1, 0, 1, 0, 0, 1]; False
[1, 1, 1, 1, 0, 1, 0, 1, 0]; False
[1, 1, 1, 1, 0, 1, 0, 1, 1]; False
[1, 1, 1, 1, 0, 1, 1, 0, 0]; False
[1, 1, 1, 1, 0, 1, 1, 0, 1]; False
[1, 1, 1, 1, 0, 1, 1, 1, 0]; False
[1, 1, 1, 1, 0, 1, 1, 1, 1]; False
[1, 1, 1, 1, 1, 0, 0, 0, 0]; False
[1, 1, 1, 1, 1, 0, 0, 0, 1]; False
[1, 1, 1, 1, 1, 0, 0, 1, 0]; False
[1, 1, 1, 1, 1, 0, 0, 1, 1]; False
[1, 1, 1, 1, 1, 0, 1, 0, 0]; False
[1, 1, 1, 1, 1, 0, 1, 0, 1]; False
[1, 1, 1, 1, 1, 0, 1, 1, 0]; False
[1, 1, 1, 1, 1, 0, 1, 1, 1]; False
[1, 1, 1, 1, 1, 1, 0, 0, 0]; False
[1, 1, 1, 1, 1, 1, 0, 0, 1]; False
[1, 1, 1, 1, 1, 1, 0, 1, 0]; False
[1, 1, 1, 1, 1, 1, 0, 1, 1]; False
[1, 1, 1, 1, 1, 1, 1, 0, 0]; False
[1, 1, 1, 1, 1, 1, 1, 0, 1]; False
[1, 1, 1, 1, 1, 1, 1, 1, 0]; False
[1, 1, 1, 1, 1, 1, 1, 1, 1]; False
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; False
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]; False
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0]; False
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1]; False
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0]; False
[0, 0, 0, 0, 0, 0, 0, 1, 0, 1]; False
[0, 0, 0, 0, 0, 0, 0, 1, 1, 0]; False
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1]; False
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0]; False
[0, 0, 0, 0, 0, 0, 1, 0, 0, 1]; False
[0, 0, 0, 0, 0, 0, 1, 0, 1, 0]; False
[0, 0, 0, 0, 0, 0, 1, 0, 1, 1]; False
[0, 0, 0, 0, 0, 0, 1, 1, 0, 0]; False
[0, 0, 0, 0, 0, 0, 1, 1, 0, 1]; False
[0, 0, 0, 0, 0, 0, 1, 1, 1, 0]; False
[0, 0, 0, 0, 0, 0, 1, 1, 1, 1]; False
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]; False
[0, 0, 0, 0, 0, 1, 0, 0, 0, 1]; False
[0, 0, 0, 0, 0, 1, 0, 0, 1, 0]; False
[0, 0, 0, 0, 0, 1, 0, 0, 1, 1]; False
[0, 0, 0, 0, 0, 1, 0, 1, 0, 0]; False
[0, 0, 0, 0, 0, 1, 0, 1, 0, 1]; False
[0, 0, 0, 0, 0, 1, 0, 1, 1, 0]; False
[0, 0, 0, 0, 0, 1, 0, 1, 1, 1]; False
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0]; False
[0, 0, 0, 0, 0, 1, 1, 0, 0, 1]; False
[0, 0, 0, 0, 0, 1, 1, 0, 1, 0]; False
[0, 0, 0, 0, 0, 1, 1, 0, 1, 1]; False
[0, 0, 0, 0, 0, 1, 1, 1, 0, 0]; False
[0, 0, 0, 0, 0, 1, 1, 1, 0, 1]; False
[0, 0, 0, 0, 0, 1, 1, 1, 1, 0]; False
[0, 0, 0, 0, 0, 1, 1, 1, 1, 1]; False
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]; False
[0, 0, 0, 0, 1, 0, 0, 0, 0, 1]; False
[0, 0, 0, 0, 1, 0, 0, 0, 1, 0]; False
[0, 0, 0, 0, 1, 0, 0, 0, 1, 1]; False
[0, 0, 0, 0, 1, 0, 0, 1, 0, 0]; False
[0, 0, 0, 0, 1, 0, 0, 1, 0, 1]; False
[0, 0, 0, 0, 1, 0, 0, 1, 1, 0]; False
[0, 0, 0, 0, 1, 0, 0, 1, 1, 1]; False
[0, 0, 0, 0, 1, 0, 1, 0, 0, 0]; False
[0, 0, 0, 0, 1, 0, 1, 0, 0, 1]; False
[0, 0, 0, 0, 1, 0, 1, 0, 1, 0]; False
[0, 0, 0, 0, 1, 0, 1, 0, 1, 1]; False
[0, 0, 0, 0, 1, 0, 1, 1, 0, 0]; False
[0, 0, 0, 0, 1, 0, 1, 1, 0, 1]; False
[0, 0, 0, 0, 1, 0, 1, 1, 1, 0]; False
[0, 0, 0, 0, 1, 0, 1, 1, 1, 1]; False
[0, 0, 0, 0, 1, 1, 0, 0, 0, 0]; False
[0, 0, 0, 0, 1, 1, 0, 0, 0, 1]; False
[0, 0, 0, 0, 1, 1, 0, 0, 1, 0]; False
[0, 0, 0, 0, 1, 1, 0, 0, 1, 1]; False
[0, 0, 0, 0, 1, 1, 0, 1, 0, 0]; False
[0, 0, 0, 0, 1, 1, 0, 1, 0, 1]; False
[0, 0, 0, 0, 1, 1, 0, 1, 1, 0]; False
[0, 0, 0, 0, 1, 1, 0, 1, 1, 1]; False
[0, 0, 0, 0, 1, 1, 1, 0, 0, 0]; False
[0, 0, 0, 0, 1, 1, 1, 0, 0, 1]; False
[0, 0, 0, 0, 1, 1, 1, 0, 1, 0]; False
[0, 0, 0, 0, 1, 1, 1, 0, 1, 1]; False
[0, 0, 0, 0, 1, 1, 1, 1, 0, 0]; False
[0, 0, 0, 0, 1, 1, 1, 1, 0, 1]; False
[0, 0, 0, 0, 1, 1, 1, 1, 1, 0]; False
[0, 0, 0, 0, 1, 1, 1, 1, 1, 1]; False
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0]; False
[0, 0, 0, 1, 0, 0, 0, 0, 0, 1]; False
[0, 0, 0, 1, 0, 0, 0, 0, 1, 0]; False
[0, 0, 0, 1, 0, 0, 0, 0, 1, 1]; False
[0, 0, 0, 1, 0, 0, 0, 1, 0, 0]; False
[0, 0, 0, 1, 0, 0, 0, 1, 0, 1]; False
[0, 0, 0, 1, 0, 0, 0, 1, 1, 0]; False
[0, 0, 0, 1, 0, 0, 0, 1, 1, 1]; False
[0, 0, 0, 1, 0, 0, 1, 0, 0, 0]; False
[0, 0, 0, 1, 0, 0, 1, 0, 0, 1]; False
[0, 0, 0, 1, 0, 0, 1, 0, 1, 0]; False
[0, 0, 0, 1, 0, 0, 1, 0, 1, 1]; False
[0, 0, 0, 1, 0, 0, 1, 1, 0, 0]; False
[0, 0, 0, 1, 0, 0, 1, 1, 0, 1]; False
[0, 0, 0, 1, 0, 0, 1, 1, 1, 0]; False
[0, 0, 0, 1, 0, 0, 1, 1, 1, 1]; False
[0, 0, 0, 1, 0, 1, 0, 0, 0, 0]; False
[0, 0, 0, 1, 0, 1, 0, 0, 0, 1]; False
[0, 0, 0, 1, 0, 1, 0, 0, 1, 0]; False
[0, 0, 0, 1, 0, 1, 0, 0, 1, 1]; False
[0, 0, 0, 1, 0, 1, 0, 1, 0, 0]; False
[0, 0, 0, 1, 0, 1, 0, 1, 0, 1]; False
[0, 0, 0, 1, 0, 1, 0, 1, 1, 0]; False
[0, 0, 0, 1, 0, 1, 0, 1, 1, 1]; False
[0, 0, 0, 1, 0, 1, 1, 0, 0, 0]; False
[0, 0, 0, 1, 0, 1, 1, 0, 0, 1]; False
[0, 0, 0, 1, 0, 1, 1, 0, 1, 0]; False
[0, 0, 0, 1, 0, 1, 1, 0, 1, 1]; False
[0, 0, 0, 1, 0, 1, 1, 1, 0, 0]; False
[0, 0, 0, 1, 0, 1, 1, 1, 0, 1]; False
[0, 0, 0, 1, 0, 1, 1, 1, 1, 0]; False
[0, 0, 0, 1, 0, 1, 1, 1, 1, 1]; False
[0, 0, 0, 1, 1, 0, 0, 0, 0, 0]; False
[0, 0, 0, 1, 1, 0, 0, 0, 0, 1]; False
[0, 0, 0, 1, 1, 0, 0, 0, 1, 0]; False
[0, 0, 0, 1, 1, 0, 0, 0, 1, 1]; False
[0, 0, 0, 1, 1, 0, 0, 1, 0, 0]; False
[0, 0, 0, 1, 1, 0, 0, 1, 0, 1]; False
[0, 0, 0, 1, 1, 0, 0, 1, 1, 0]; False
[0, 0, 0, 1, 1, 0, 0, 1, 1, 1]; False
[0, 0, 0, 1, 1, 0, 1, 0, 0, 0]; False
[0, 0, 0, 1, 1, 0, 1, 0, 0, 1]; False
[0, 0, 0, 1, 1, 0, 1, 0, 1, 0]; False
[0, 0, 0, 1, 1, 0, 1, 0, 1, 1]; False
[0, 0, 0, 1, 1, 0, 1, 1, 0, 0]; False
[0, 0, 0, 1, 1, 0, 1, 1, 0, 1]; False
[0, 0, 0, 1, 1, 0, 1, 1, 1, 0]; False
[0, 0, 0, 1, 1, 0, 1, 1, 1, 1]; False
[0, 0, 0, 1, 1, 1, 0, 0, 0, 0]; False
[0, 0, 0, 1, 1, 1, 0, 0, 0, 1]; False
[0, 0, 0, 1, 1, 1, 0, 0, 1, 0]; False
[0, 0, 0, 1, 1, 1, 0, 0, 1, 1]; False
[0, 0, 0, 1, 1, 1, 0, 1, 0, 0]; False
[0, 0, 0, 1, 1, 1, 0, 1, 0, 1]; False
[0, 0, 0, 1, 1, 1, 0, 1, 1, 0]; False
[0, 0, 0, 1, 1, 1, 0, 1, 1, 1]; False
[0, 0, 0, 1, 1, 1, 1, 0, 0, 0]; False
[0, 0, 0, 1, 1, 1, 1, 0, 0, 1]; False
[0, 0, 0, 1, 1, 1, 1, 0, 1, 0]; False
[0, 0, 0, 1, 1, 1, 1, 0, 1, 1]; False
[0, 0, 0, 1, 1, 1, 1, 1, 0, 0]; False
[0, 0, 0, 1, 1, 1, 1, 1, 0, 1]; False
[0, 0, 0, 1, 1, 1, 1, 1, 1, 0]; False
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1]; False
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]; False
[0, 0, 1, 0, 0, 0, 0, 0, 0, 1]; False
[0, 0, 1, 0, 0, 0, 0, 0, 1, 0]; False
[0, 0, 1, 0, 0, 0, 0, 0, 1, 1]; False
[0, 0, 1, 0, 0, 0, 0, 1, 0, 0]; False
[0, 0, 1, 0, 0, 0, 0, 1, 0, 1]; False
[0, 0, 1, 0, 0, 0, 0, 1, 1, 0]; False
[0, 0, 1, 0, 0, 0, 0, 1, 1, 1]; False
[0, 0, 1, 0, 0, 0, 1, 0, 0, 0]; False
[0, 0, 1, 0, 0, 0, 1, 0, 0, 1]; False
[0, 0, 1, 0, 0, 0, 1, 0, 1, 0]; False
[0, 0, 1, 0, 0, 0, 1, 0, 1, 1]; False
[0, 0, 1, 0, 0, 0, 1, 1, 0, 0]; False
[0, 0, 1, 0, 0, 0, 1, 1, 0, 1]; False
[0, 0, 1, 0, 0, 0, 1, 1, 1, 0]; False
[0, 0, 1, 0, 0, 0, 1, 1, 1, 1]; False
[0, 0, 1, 0, 0, 1, 0, 0, 0, 0]; False
[0, 0, 1, 0, 0, 1, 0, 0, 0, 1]; False
[0, 0, 1, 0, 0, 1, 0, 0, 1, 0]; False
[0, 0, 1, 0, 0, 1, 0, 0, 1, 1]; False
[0, 0, 1, 0, 0, 1, 0, 1, 0, 0]; False
[0, 0, 1, 0, 0, 1, 0, 1, 0, 1]; False
[0, 0, 1, 0, 0, 1, 0, 1, 1, 0]; False
[0, 0, 1, 0, 0, 1, 0, 1, 1, 1]; False
[0, 0, 1, 0, 0, 1, 1, 0, 0, 0]; False
[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]; False
[0, 0, 1, 0, 0, 1, 1, 0, 1, 0]; False
[0, 0, 1, 0, 0, 1, 1, 0, 1, 1]; False
[0, 0, 1, 0, 0, 1, 1, 1, 0, 0]; False
[0, 0, 1, 0, 0, 1, 1, 1, 0, 1]; False
[0, 0, 1, 0, 0, 1, 1, 1, 1, 0]; False
[0, 0, 1, 0, 0, 1, 1, 1, 1, 1]; False
[0, 0, 1, 0, 1, 0, 0, 0, 0, 0]; False
[0, 0, 1, 0, 1, 0, 0, 0, 0, 1]; False
[0, 0, 1, 0, 1, 0, 0, 0, 1, 0]; False
[0, 0, 1, 0, 1, 0, 0, 0, 1, 1]; False
[0, 0, 1, 0, 1, 0, 0, 1, 0, 0]; False
[0, 0, 1, 0, 1, 0, 0, 1, 0, 1]; False
[0, 0, 1, 0, 1, 0, 0, 1, 1, 0]; False
[0, 0, 1, 0, 1, 0, 0, 1, 1, 1]; False
[0, 0, 1, 0, 1, 0, 1, 0, 0, 0]; False
[0, 0, 1, 0, 1, 0, 1, 0, 0, 1]; False
[0, 0, 1, 0, 1, 0, 1, 0, 1, 0]; False
[0, 0, 1, 0, 1, 0, 1, 0, 1, 1]; False
[0, 0, 1, 0, 1, 0, 1, 1, 0, 0]; False
[0, 0, 1, 0, 1, 0, 1, 1, 0, 1]; False
[0, 0, 1, 0, 1, 0, 1, 1, 1, 0]; False
[0, 0, 1, 0, 1, 0, 1, 1, 1, 1]; False
[0, 0, 1, 0, 1, 1, 0, 0, 0, 0]; False
[0, 0, 1, 0, 1, 1, 0, 0, 0, 1]; False
[0, 0, 1, 0, 1, 1, 0, 0, 1, 0]; False
[0, 0, 1, 0, 1, 1, 0, 0, 1, 1]; False
[0, 0, 1, 0, 1, 1, 0, 1, 0, 0]; False
[0, 0, 1, 0, 1, 1, 0, 1, 0, 1]; False
[0, 0, 1, 0, 1, 1, 0, 1, 1, 0]; False
[0, 0, 1, 0, 1, 1, 0, 1, 1, 1]; False
[0, 0, 1, 0, 1, 1, 1, 0, 0, 0]; False
[0, 0, 1, 0, 1, 1, 1, 0, 0, 1]; False
[0, 0, 1, 0, 1, 1, 1, 0, 1, 0]; False
[0, 0, 1, 0, 1, 1, 1, 0, 1, 1]; False
[0, 0, 1, 0, 1, 1, 1, 1, 0, 0]; False
[0, 0, 1, 0, 1, 1, 1, 1, 0, 1]; False
[0, 0, 1, 0, 1, 1, 1, 1, 1, 0]; False
[0, 0, 1, 0, 1, 1, 1, 1, 1, 1]; False
[0, 0, 1, 1, 0, 0, 0, 0, 0, 0]; False
[0, 0, 1, 1, 0, 0, 0, 0, 0, 1]; False
[0, 0, 1, 1, 0, 0, 0, 0, 1, 0]; False
[0, 0, 1, 1, 0, 0, 0, 0, 1, 1]; False
[0, 0, 1, 1, 0, 0, 0, 1, 0, 0]; False
[0, 0, 1, 1, 0, 0, 0, 1, 0, 1]; False
[0, 0, 1, 1, 0, 0, 0, 1, 1, 0]; False
[0, 0, 1, 1, 0, 0, 0, 1, 1, 1]; False
[0, 0, 1, 1, 0, 0, 1, 0, 0, 0]; False
[0, 0, 1, 1, 0, 0, 1, 0, 0, 1]; False
[0, 0, 1, 1, 0, 0, 1, 0, 1, 0]; False
[0, 0, 1, 1, 0, 0, 1, 0, 1, 1]; False
[0, 0, 1, 1, 0, 0, 1, 1, 0, 0]; False
[0, 0, 1, 1, 0, 0, 1, 1, 0, 1]; False
[0, 0, 1, 1, 0, 0, 1, 1, 1, 0]; False
[0, 0, 1, 1, 0, 0, 1, 1, 1, 1]; False
[0, 0, 1, 1, 0, 1, 0, 0, 0, 0]; False
[0, 0, 1, 1, 0, 1, 0, 0, 0, 1]; False
[0, 0, 1, 1, 0, 1, 0, 0, 1, 0]; False
[0, 0, 1, 1, 0, 1, 0, 0, 1, 1]; False
[0, 0, 1, 1, 0, 1, 0, 1, 0, 0]; False
[0, 0, 1, 1, 0, 1, 0, 1, 0, 1]; False
[0, 0, 1, 1, 0, 1, 0, 1, 1, 0]; False
[0, 0, 1, 1, 0, 1, 0, 1, 1, 1]; False
[0, 0, 1, 1, 0, 1, 1, 0, 0, 0]; False
[0, 0, 1, 1, 0, 1, 1, 0, 0, 1]; False
[0, 0, 1, 1, 0, 1, 1, 0, 1, 0]; False
[0, 0, 1, 1, 0, 1, 1, 0, 1, 1]; False
[0, 0, 1, 1, 0, 1, 1, 1, 0, 0]; False
[0, 0, 1, 1, 0, 1, 1, 1, 0, 1]; False
[0, 0, 1, 1, 0, 1, 1, 1, 1, 0]; False
[0, 0, 1, 1, 0, 1, 1, 1, 1, 1]; False
[0, 0, 1, 1, 1, 0, 0, 0, 0, 0]; False
[0, 0, 1, 1, 1, 0, 0, 0, 0, 1]; False
[0, 0, 1, 1, 1, 0, 0, 0, 1, 0]; False
[0, 0, 1, 1, 1, 0, 0, 0, 1, 1]; False
[0, 0, 1, 1, 1, 0, 0, 1, 0, 0]; False
[0, 0, 1, 1, 1, 0, 0, 1, 0, 1]; False
[0, 0, 1, 1, 1, 0, 0, 1, 1, 0]; False
[0, 0, 1, 1, 1, 0, 0, 1, 1, 1]; False
[0, 0, 1, 1, 1, 0, 1, 0, 0, 0]; False
[0, 0, 1, 1, 1, 0, 1, 0, 0, 1]; False
[0, 0, 1, 1, 1, 0, 1, 0, 1, 0]; False
[0, 0, 1, 1, 1, 0, 1, 0, 1, 1]; False
[0, 0, 1, 1, 1, 0, 1, 1, 0, 0]; False
[0, 0, 1, 1, 1, 0, 1, 1, 0, 1]; False
[0, 0, 1, 1, 1, 0, 1, 1, 1, 0]; False
[0, 0, 1, 1, 1, 0, 1, 1, 1, 1]; False
[0, 0, 1, 1, 1, 1, 0, 0, 0, 0]; False
[0, 0, 1, 1, 1, 1, 0, 0, 0, 1]; False
[0, 0, 1, 1, 1, 1, 0, 0, 1, 0]; False
[0, 0, 1, 1, 1, 1, 0, 0, 1, 1]; False
[0, 0, 1, 1, 1, 1, 0, 1, 0, 0]; False
[0, 0, 1, 1, 1, 1, 0, 1, 0, 1]; False
[0, 0, 1, 1, 1, 1, 0, 1, 1, 0]; False
[0, 0, 1, 1, 1, 1, 0, 1, 1, 1]; False
[0, 0, 1, 1, 1, 1, 1, 0, 0, 0]; False
[0, 0, 1, 1, 1, 1, 1, 0, 0, 1]; False
[0, 0, 1, 1, 1, 1, 1, 0, 1, 0]; False
[0, 0, 1, 1, 1, 1, 1, 0, 1, 1]; False
[0, 0, 1, 1, 1, 1, 1, 1, 0, 0]; False
[0, 0, 1, 1, 1, 1, 1, 1, 0, 1]; False
[0, 0, 1, 1, 1, 1, 1, 1, 1, 0]; False
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1]; False
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0]; False
[0, 1, 0, 0, 0, 0, 0, 0, 0, 1]; False
[0, 1, 0, 0, 0, 0, 0, 0, 1, 0]; False
[0, 1, 0, 0, 0, 0, 0, 0, 1, 1]; False
[0, 1, 0, 0, 0, 0, 0, 1, 0, 0]; False
[0, 1, 0, 0, 0, 0, 0, 1, 0, 1]; False
[0, 1, 0, 0, 0, 0, 0, 1, 1, 0]; False
[0, 1, 0, 0, 0, 0, 0, 1, 1, 1]; False
[0, 1, 0, 0, 0, 0, 1, 0, 0, 0]; False
[0, 1, 0, 0, 0, 0, 1, 0, 0, 1]; False
[0, 1, 0, 0, 0, 0, 1, 0, 1, 0]; False
[0, 1, 0, 0, 0, 0, 1, 0, 1, 1]; False
[0, 1, 0, 0, 0, 0, 1, 1, 0, 0]; False
[0, 1, 0, 0, 0, 0, 1, 1, 0, 1]; False
[0, 1, 0, 0, 0, 0, 1, 1, 1, 0]; False
[0, 1, 0, 0, 0, 0, 1, 1, 1, 1]; False
[0, 1, 0, 0, 0, 1, 0, 0, 0, 0]; False
[0, 1, 0, 0, 0, 1, 0, 0, 0, 1]; False
[0, 1, 0, 0, 0, 1, 0, 0, 1, 0]; False
[0, 1, 0, 0, 0, 1, 0, 0, 1, 1]; False
[0, 1, 0, 0, 0, 1, 0, 1, 0, 0]; False
[0, 1, 0, 0, 0, 1, 0, 1, 0, 1]; False
[0, 1, 0, 0, 0, 1, 0, 1, 1, 0]; False
[0, 1, 0, 0, 0, 1, 0, 1, 1, 1]; False
[0, 1, 0, 0, 0, 1, 1, 0, 0, 0]; False
[0, 1, 0, 0, 0, 1, 1, 0, 0, 1]; False
[0, 1, 0, 0, 0, 1, 1, 0, 1, 0]; False
[0, 1, 0, 0, 0, 1, 1, 0, 1, 1]; False
[0, 1, 0, 0, 0, 1, 1, 1, 0, 0]; False
[0, 1, 0, 0, 0, 1, 1, 1, 0, 1]; False
[0, 1, 0, 0, 0, 1, 1, 1, 1, 0]; False
[0, 1, 0, 0, 0, 1, 1, 1, 1, 1]; False
[0, 1, 0, 0, 1, 0, 0, 0, 0, 0]; False
[0, 1, 0, 0, 1, 0, 0, 0, 0, 1]; False
[0, 1, 0, 0, 1, 0, 0, 0, 1, 0]; False
[0, 1, 0, 0, 1, 0, 0, 0, 1, 1]; False
[0, 1, 0, 0, 1, 0, 0, 1, 0, 0]; False
[0, 1, 0, 0, 1, 0, 0, 1, 0, 1]; False
[0, 1, 0, 0, 1, 0, 0, 1, 1, 0]; False
[0, 1, 0, 0, 1, 0, 0, 1, 1, 1]; False
[0, 1, 0, 0, 1, 0, 1, 0, 0, 0]; False
[0, 1, 0, 0, 1, 0, 1, 0, 0, 1]; False
[0, 1, 0, 0, 1, 0, 1, 0, 1, 0]; False
[0, 1, 0, 0, 1, 0, 1, 0, 1, 1]; False
[0, 1, 0, 0, 1, 0, 1, 1, 0, 0]; False
[0, 1, 0, 0, 1, 0, 1, 1, 0, 1]; False
[0, 1, 0, 0, 1, 0, 1, 1, 1, 0]; False
[0, 1, 0, 0, 1, 0, 1, 1, 1, 1]; False
[0, 1, 0, 0, 1, 1, 0, 0, 0, 0]; False
[0, 1, 0, 0, 1, 1, 0, 0, 0, 1]; False
[0, 1, 0, 0, 1, 1, 0, 0, 1, 0]; False
[0, 1, 0, 0, 1, 1, 0, 0, 1, 1]; False
[0, 1, 0, 0, 1, 1, 0, 1, 0, 0]; False
[0, 1, 0, 0, 1, 1, 0, 1, 0, 1]; False
[0, 1, 0, 0, 1, 1, 0, 1, 1, 0]; False
[0, 1, 0, 0, 1, 1, 0, 1, 1, 1]; False
[0, 1, 0, 0, 1, 1, 1, 0, 0, 0]; False
[0, 1, 0, 0, 1, 1, 1, 0, 0, 1]; False
[0, 1, 0, 0, 1, 1, 1, 0, 1, 0]; False
[0, 1, 0, 0, 1, 1, 1, 0, 1, 1]; False
[0, 1, 0, 0, 1, 1, 1, 1, 0, 0]; False
[0, 1, 0, 0, 1, 1, 1, 1, 0, 1]; False
[0, 1, 0, 0, 1, 1, 1, 1, 1, 0]; False
[0, 1, 0, 0, 1, 1, 1, 1, 1, 1]; False
[0, 1, 0, 1, 0, 0, 0, 0, 0, 0]; False
[0, 1, 0, 1, 0, 0, 0, 0, 0, 1]; False
[0, 1, 0, 1, 0, 0, 0, 0, 1, 0]; False
[0, 1, 0, 1, 0, 0, 0, 0, 1, 1]; False
[0, 1, 0, 1, 0, 0, 0, 1, 0, 0]; False
[0, 1, 0, 1, 0, 0, 0, 1, 0, 1]; False
[0, 1, 0, 1, 0, 0, 0, 1, 1, 0]; False
[0, 1, 0, 1, 0, 0, 0, 1, 1, 1]; False
[0, 1, 0, 1, 0, 0, 1, 0, 0, 0]; False
[0, 1, 0, 1, 0, 0, 1, 0, 0, 1]; False
[0, 1, 0, 1, 0, 0, 1, 0, 1, 0]; False
[0, 1, 0, 1, 0, 0, 1, 0, 1, 1]; False
[0, 1, 0, 1, 0, 0, 1, 1, 0, 0]; False
[0, 1, 0, 1, 0, 0, 1, 1, 0, 1]; False
[0, 1, 0, 1, 0, 0, 1, 1, 1, 0]; False
[0, 1, 0, 1, 0, 0, 1, 1, 1, 1]; False
[0, 1, 0, 1, 0, 1, 0, 0, 0, 0]; False
[0, 1, 0, 1, 0, 1, 0, 0, 0, 1]; False
[0, 1, 0, 1, 0, 1, 0, 0, 1, 0]; False
[0, 1, 0, 1, 0, 1, 0, 0, 1, 1]; False
[0, 1, 0, 1, 0, 1, 0, 1, 0, 0]; False
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]; False
[0, 1, 0, 1, 0, 1, 0, 1, 1, 0]; False
[0, 1, 0, 1, 0, 1, 0, 1, 1, 1]; False
[0, 1, 0, 1, 0, 1, 1, 0, 0, 0]; False
[0, 1, 0, 1, 0, 1, 1, 0, 0, 1]; False
[0, 1, 0, 1, 0, 1, 1, 0, 1, 0]; False
[0, 1, 0, 1, 0, 1, 1, 0, 1, 1]; False
[0, 1, 0, 1, 0, 1, 1, 1, 0, 0]; False
[0, 1, 0, 1, 0, 1, 1, 1, 0, 1]; False
[0, 1, 0, 1, 0, 1, 1, 1, 1, 0]; False
[0, 1, 0, 1, 0, 1, 1, 1, 1, 1]; False
[0, 1, 0, 1, 1, 0, 0, 0, 0, 0]; False
[0, 1, 0, 1, 1, 0, 0, 0, 0, 1]; False
[0, 1, 0, 1, 1, 0, 0, 0, 1, 0]; False
[0, 1, 0, 1, 1, 0, 0, 0, 1, 1]; False
[0, 1, 0, 1, 1, 0, 0, 1, 0, 0]; False
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1]; False
[0, 1, 0, 1, 1, 0, 0, 1, 1, 0]; False
[0, 1, 0, 1, 1, 0, 0, 1, 1, 1]; False
[0, 1, 0, 1, 1, 0, 1, 0, 0, 0]; False
[0, 1, 0, 1, 1, 0, 1, 0, 0, 1]; False
[0, 1, 0, 1, 1, 0, 1, 0, 1, 0]; False
[0, 1, 0, 1, 1, 0, 1, 0, 1, 1]; False
[0, 1, 0, 1, 1, 0, 1, 1, 0, 0]; False
[0, 1, 0, 1, 1, 0, 1, 1, 0, 1]; False
[0, 1, 0, 1, 1, 0, 1, 1, 1, 0]; False
[0, 1, 0, 1, 1, 0, 1, 1, 1, 1]; False
[0, 1, 0, 1, 1, 1, 0, 0, 0, 0]; False
[0, 1, 0, 1, 1, 1, 0, 0, 0, 1]; False
[0, 1, 0, 1, 1, 1, 0, 0, 1, 0]; False
[0, 1, 0, 1, 1, 1, 0, 0, 1, 1]; False
[0, 1, 0, 1, 1, 1, 0, 1, 0, 0]; False
[0, 1, 0, 1, 1, 1, 0, 1, 0, 1]; False
[0, 1, 0, 1, 1, 1, 0, 1, 1, 0]; False
[0, 1, 0, 1, 1, 1, 0, 1, 1, 1]; False
[0, 1, 0, 1, 1, 1, 1, 0, 0, 0]; False
[0, 1, 0, 1, 1, 1, 1, 0, 0, 1]; False
[0, 1, 0, 1, 1, 1, 1, 0, 1, 0]; False
[0, 1, 0, 1, 1, 1, 1, 0, 1, 1]; False
[0, 1, 0, 1, 1, 1, 1, 1, 0, 0]; False
[0, 1, 0, 1, 1, 1, 1, 1, 0, 1]; False
[0, 1, 0, 1, 1, 1, 1, 1, 1, 0]; False
[0, 1, 0, 1, 1, 1, 1, 1, 1, 1]; False
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0]; False
[0, 1, 1, 0, 0, 0, 0, 0, 0, 1]; False
[0, 1, 1, 0, 0, 0, 0, 0, 1, 0]; False
[0, 1, 1, 0, 0, 0, 0, 0, 1, 1]; False
[0, 1, 1, 0, 0, 0, 0, 1, 0, 0]; False
[0, 1, 1, 0, 0, 0, 0, 1, 0, 1]; False
[0, 1, 1, 0, 0, 0, 0, 1, 1, 0]; False
[0, 1, 1, 0, 0, 0, 0, 1, 1, 1]; False
[0, 1, 1, 0, 0, 0, 1, 0, 0, 0]; False
[0, 1, 1, 0, 0, 0, 1, 0, 0, 1]; False
[0, 1, 1, 0, 0, 0, 1, 0, 1, 0]; False
[0, 1, 1, 0, 0, 0, 1, 0, 1, 1]; False
[0, 1, 1, 0, 0, 0, 1, 1, 0, 0]; False
[0, 1, 1, 0, 0, 0, 1, 1, 0, 1]; False
[0, 1, 1, 0, 0, 0, 1, 1, 1, 0]; False
[0, 1, 1, 0, 0, 0, 1, 1, 1, 1]; False
[0, 1, 1, 0, 0, 1, 0, 0, 0, 0]; False
[0, 1, 1, 0, 0, 1, 0, 0, 0, 1]; False
[0, 1, 1, 0, 0, 1, 0, 0, 1, 0]; False
[0, 1, 1, 0, 0, 1, 0, 0, 1, 1]; False
[0, 1, 1, 0, 0, 1, 0, 1, 0, 0]; False
[0, 1, 1, 0, 0, 1, 0, 1, 0, 1]; False
[0, 1, 1, 0, 0, 1, 0, 1, 1, 0]; False
[0, 1, 1, 0, 0, 1, 0, 1, 1, 1]; False
[0, 1, 1, 0, 0, 1, 1, 0, 0, 0]; False
[0, 1, 1, 0, 0, 1, 1, 0, 0, 1]; False
[0, 1, 1, 0, 0, 1, 1, 0, 1, 0]; False
[0, 1, 1, 0, 0, 1, 1, 0, 1, 1]; False
[0, 1, 1, 0, 0, 1, 1, 1, 0, 0]; False
[0, 1, 1, 0, 0, 1, 1, 1, 0, 1]; False
[0, 1, 1, 0, 0, 1, 1, 1, 1, 0]; False
[0, 1, 1, 0, 0, 1, 1, 1, 1, 1]; False
[0, 1, 1, 0, 1, 0, 0, 0, 0, 0]; False
[0, 1, 1, 0, 1, 0, 0, 0, 0, 1]; False
[0, 1, 1, 0, 1, 0, 0, 0, 1, 0]; False
[0, 1, 1, 0, 1, 0, 0, 0, 1, 1]; False
[0, 1, 1, 0, 1, 0, 0, 1, 0, 0]; False
[0, 1, 1, 0, 1, 0, 0, 1, 0, 1]; False
[0, 1, 1, 0, 1, 0, 0, 1, 1, 0]; False
[0, 1, 1, 0, 1, 0, 0, 1, 1, 1]; False
[0, 1, 1, 0, 1, 0, 1, 0, 0, 0]; False
[0, 1, 1, 0, 1, 0, 1, 0, 0, 1]; False
[0, 1, 1, 0, 1, 0, 1, 0, 1, 0]; False
[0, 1, 1, 0, 1, 0, 1, 0, 1, 1]; False
[0, 1, 1, 0, 1, 0, 1, 1, 0, 0]; False
[0, 1, 1, 0, 1, 0, 1, 1, 0, 1]; False
[0, 1, 1, 0, 1, 0, 1, 1, 1, 0]; False
[0, 1, 1, 0, 1, 0, 1, 1, 1, 1]; False
[0, 1, 1, 0, 1, 1, 0, 0, 0, 0]; False
[0, 1, 1, 0, 1, 1, 0, 0, 0, 1]; False
[0, 1, 1, 0, 1, 1, 0, 0, 1, 0]; False
[0, 1, 1, 0, 1, 1, 0, 0, 1, 1]; False
[0, 1, 1, 0, 1, 1, 0, 1, 0, 0]; False
[0, 1, 1, 0, 1, 1, 0, 1, 0, 1]; False
[0, 1, 1, 0, 1, 1, 0, 1, 1, 0]; False
[0, 1, 1, 0, 1, 1, 0, 1, 1, 1]; False
[0, 1, 1, 0, 1, 1, 1, 0, 0, 0]; False
[0, 1, 1, 0, 1, 1, 1, 0, 0, 1]; False
[0, 1, 1, 0, 1, 1, 1, 0, 1, 0]; False
[0, 1, 1, 0, 1, 1, 1, 0, 1, 1]; False
[0, 1, 1, 0, 1, 1, 1, 1, 0, 0]; False
[0, 1, 1, 0, 1, 1, 1, 1, 0, 1]; False
[0, 1, 1, 0, 1, 1, 1, 1, 1, 0]; False
[0, 1, 1, 0, 1, 1, 1, 1, 1, 1]; False
[0, 1, 1, 1, 0, 0, 0, 0, 0, 0]; False
[0, 1, 1, 1, 0, 0, 0, 0, 0, 1]; False
[0, 1, 1, 1, 0, 0, 0, 0, 1, 0]; False
[0, 1, 1, 1, 0, 0, 0, 0, 1, 1]; False
[0, 1, 1, 1, 0, 0, 0, 1, 0, 0]; False
[0, 1, 1, 1, 0, 0, 0, 1, 0, 1]; False
[0, 1, 1, 1, 0, 0, 0, 1, 1, 0]; False
[0, 1, 1, 1, 0, 0, 0, 1, 1, 1]; True
[0, 1, 1, 1, 0, 0, 1, 0, 0, 0]; False
[0, 1, 1, 1, 0, 0, 1, 0, 0, 1]; False
[0, 1, 1, 1, 0, 0, 1, 0, 1, 0]; False
[0, 1, 1, 1, 0, 0, 1, 0, 1, 1]; True
[0, 1, 1, 1, 0, 0, 1, 1, 0, 0]; False
[0, 1, 1, 1, 0, 0, 1, 1, 0, 1]; True
[0, 1, 1, 1, 0, 0, 1, 1, 1, 0]; False
[0, 1, 1, 1, 0, 0, 1, 1, 1, 1]; False
[0, 1, 1, 1, 0, 1, 0, 0, 0, 0]; False
[0, 1, 1, 1, 0, 1, 0, 0, 0, 1]; False
[0, 1, 1, 1, 0, 1, 0, 0, 1, 0]; False
[0, 1, 1, 1, 0, 1, 0, 0, 1, 1]; True
[0, 1, 1, 1, 0, 1, 0, 1, 0, 0]; False
[0, 1, 1, 1, 0, 1, 0, 1, 0, 1]; True
[0, 1, 1, 1, 0, 1, 0, 1, 1, 0]; True
[0, 1, 1, 1, 0, 1, 0, 1, 1, 1]; True
[0, 1, 1, 1, 0, 1, 1, 0, 0, 0]; False
[0, 1, 1, 1, 0, 1, 1, 0, 0, 1]; True
[0, 1, 1, 1, 0, 1, 1, 0, 1, 0]; True
[0, 1, 1, 1, 0, 1, 1, 0, 1, 1]; True
[0, 1, 1, 1, 0, 1, 1, 1, 0, 0]; True
[0, 1, 1, 1, 0, 1, 1, 1, 0, 1]; True
[0, 1, 1, 1, 0, 1, 1, 1, 1, 0]; True
[0, 1, 1, 1, 0, 1, 1, 1, 1, 1]; True
[0, 1, 1, 1, 1, 0, 0, 0, 0, 0]; False
[0, 1, 1, 1, 1, 0, 0, 0, 0, 1]; False
[0, 1, 1, 1, 1, 0, 0, 0, 1, 0]; False
[0, 1, 1, 1, 1, 0, 0, 0, 1, 1]; False
[0, 1, 1, 1, 1, 0, 0, 1, 0, 0]; False
[0, 1, 1, 1, 1, 0, 0, 1, 0, 1]; False
[0, 1, 1, 1, 1, 0, 0, 1, 1, 0]; False
[0, 1, 1, 1, 1, 0, 0, 1, 1, 1]; False
[0, 1, 1, 1, 1, 0, 1, 0, 0, 0]; False
[0, 1, 1, 1, 1, 0, 1, 0, 0, 1]; False
[0, 1, 1, 1, 1, 0, 1, 0, 1, 0]; False
[0, 1, 1, 1, 1, 0, 1, 0, 1, 1]; False
[0, 1, 1, 1, 1, 0, 1, 1, 0, 0]; False
[0, 1, 1, 1, 1, 0, 1, 1, 0, 1]; False
[0, 1, 1, 1, 1, 0, 1, 1, 1, 0]; False
[0, 1, 1, 1, 1, 0, 1, 1, 1, 1]; False
[0, 1, 1, 1, 1, 1, 0, 0, 0, 0]; False
[0, 1, 1, 1, 1, 1, 0, 0, 0, 1]; False
[0, 1, 1, 1, 1, 1, 0, 0, 1, 0]; False
[0, 1, 1, 1, 1, 1, 0, 0, 1, 1]; False
[0, 1, 1, 1, 1, 1, 0, 1, 0, 0]; False
[0, 1, 1, 1, 1, 1, 0, 1, 0, 1]; False
[0, 1, 1, 1, 1, 1, 0, 1, 1, 0]; False
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1]; True
[0, 1, 1, 1, 1, 1, 1, 0, 0, 0]; False
[0, 1, 1, 1, 1, 1, 1, 0, 0, 1]; False
[0, 1, 1, 1, 1, 1, 1, 0, 1, 0]; False
[0, 1, 1, 1, 1, 1, 1, 0, 1, 1]; True
[0, 1, 1, 1, 1, 1, 1, 1, 0, 0]; False
[0, 1, 1, 1, 1, 1, 1, 1, 0, 1]; True
[0, 1, 1, 1, 1, 1, 1, 1, 1, 0]; True
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]; True
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]; False
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1]; False
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0]; False
[1, 0, 0, 0, 0, 0, 0, 0, 1, 1]; False
[1, 0, 0, 0, 0, 0, 0, 1, 0, 0]; False
[1, 0, 0, 0, 0, 0, 0, 1, 0, 1]; False
[1, 0, 0, 0, 0, 0, 0, 1, 1, 0]; False
[1, 0, 0, 0, 0, 0, 0, 1, 1, 1]; False
[1, 0, 0, 0, 0, 0, 1, 0, 0, 0]; False
[1, 0, 0, 0, 0, 0, 1, 0, 0, 1]; False
[1, 0, 0, 0, 0, 0, 1, 0, 1, 0]; False
[1, 0, 0, 0, 0, 0, 1, 0, 1, 1]; False
[1, 0, 0, 0, 0, 0, 1, 1, 0, 0]; False
[1, 0, 0, 0, 0, 0, 1, 1, 0, 1]; False
[1, 0, 0, 0, 0, 0, 1, 1, 1, 0]; False
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1]; False
[1, 0, 0, 0, 0, 1, 0, 0, 0, 0]; False
[1, 0, 0, 0, 0, 1, 0, 0, 0, 1]; False
[1, 0, 0, 0, 0, 1, 0, 0, 1, 0]; False
[1, 0, 0, 0, 0, 1, 0, 0, 1, 1]; False
[1, 0, 0, 0, 0, 1, 0, 1, 0, 0]; False
[1, 0, 0, 0, 0, 1, 0, 1, 0, 1]; False
[1, 0, 0, 0, 0, 1, 0, 1, 1, 0]; False
[1, 0, 0, 0, 0, 1, 0, 1, 1, 1]; False
[1, 0, 0, 0, 0, 1, 1, 0, 0, 0]; False
[1, 0, 0, 0, 0, 1, 1, 0, 0, 1]; False
[1, 0, 0, 0, 0, 1, 1, 0, 1, 0]; False
[1, 0, 0, 0, 0, 1, 1, 0, 1, 1]; False
[1, 0, 0, 0, 0, 1, 1, 1, 0, 0]; False
[1, 0, 0, 0, 0, 1, 1, 1, 0, 1]; False
[1, 0, 0, 0, 0, 1, 1, 1, 1, 0]; False
[1, 0, 0, 0, 0, 1, 1, 1, 1, 1]; False
[1, 0, 0, 0, 1, 0, 0, 0, 0, 0]; False
[1, 0, 0, 0, 1, 0, 0, 0, 0, 1]; False
[1, 0, 0, 0, 1, 0, 0, 0, 1, 0]; False
[1, 0, 0, 0, 1, 0, 0, 0, 1, 1]; False
[1, 0, 0, 0, 1, 0, 0, 1, 0, 0]; False
[1, 0, 0, 0, 1, 0, 0, 1, 0, 1]; False
[1, 0, 0, 0, 1, 0, 0, 1, 1, 0]; False
[1, 0, 0, 0, 1, 0, 0, 1, 1, 1]; False
[1, 0, 0, 0, 1, 0, 1, 0, 0, 0]; False
[1, 0, 0, 0, 1, 0, 1, 0, 0, 1]; False
[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]; False
[1, 0, 0, 0, 1, 0, 1, 0, 1, 1]; False
[1, 0, 0, 0, 1, 0, 1, 1, 0, 0]; False
[1, 0, 0, 0, 1, 0, 1, 1, 0, 1]; False
[1, 0, 0, 0, 1, 0, 1, 1, 1, 0]; False
[1, 0, 0, 0, 1, 0, 1, 1, 1, 1]; False
[1, 0, 0, 0, 1, 1, 0, 0, 0, 0]; False
[1, 0, 0, 0, 1, 1, 0, 0, 0, 1]; False
[1, 0, 0, 0, 1, 1, 0, 0, 1, 0]; False
[1, 0, 0, 0, 1, 1, 0, 0, 1, 1]; False
[1, 0, 0, 0, 1, 1, 0, 1, 0, 0]; False
[1, 0, 0, 0, 1, 1, 0, 1, 0, 1]; False
[1, 0, 0, 0, 1, 1, 0, 1, 1, 0]; False
[1, 0, 0, 0, 1, 1, 0, 1, 1, 1]; False
[1, 0, 0, 0, 1, 1, 1, 0, 0, 0]; False
[1, 0, 0, 0, 1, 1, 1, 0, 0, 1]; False
[1, 0, 0, 0, 1, 1, 1, 0, 1, 0]; False
[1, 0, 0, 0, 1, 1, 1, 0, 1, 1]; False
[1, 0, 0, 0, 1, 1, 1, 1, 0, 0]; False
[1, 0, 0, 0, 1, 1, 1, 1, 0, 1]; False
[1, 0, 0, 0, 1, 1, 1, 1, 1, 0]; False
[1, 0, 0, 0, 1, 1, 1, 1, 1, 1]; False
[1, 0, 0, 1, 0, 0, 0, 0, 0, 0]; False
[1, 0, 0, 1, 0, 0, 0, 0, 0, 1]; False
[1, 0, 0, 1, 0, 0, 0, 0, 1, 0]; False
[1, 0, 0, 1, 0, 0, 0, 0, 1, 1]; False
[1, 0, 0, 1, 0, 0, 0, 1, 0, 0]; False
[1, 0, 0, 1, 0, 0, 0, 1, 0, 1]; False
[1, 0, 0, 1, 0, 0, 0, 1, 1, 0]; False
[1, 0, 0, 1, 0, 0, 0, 1, 1, 1]; False
[1, 0, 0, 1, 0, 0, 1, 0, 0, 0]; False
[1, 0, 0, 1, 0, 0, 1, 0, 0, 1]; False
[1, 0, 0, 1, 0, 0, 1, 0, 1, 0]; False
[1, 0, 0, 1, 0, 0, 1, 0, 1, 1]; False
[1, 0, 0, 1, 0, 0, 1, 1, 0, 0]; False
[1, 0, 0, 1, 0, 0, 1, 1, 0, 1]; False
[1, 0, 0, 1, 0, 0, 1, 1, 1, 0]; False
[1, 0, 0, 1, 0, 0, 1, 1, 1, 1]; False
[1, 0, 0, 1, 0, 1, 0, 0, 0, 0]; False
[1, 0, 0, 1, 0, 1, 0, 0, 0, 1]; False
[1, 0, 0, 1, 0, 1, 0, 0, 1, 0]; False
[1, 0, 0, 1, 0, 1, 0, 0, 1, 1]; False
[1, 0, 0, 1, 0, 1, 0, 1, 0, 0]; False
[1, 0, 0, 1, 0, 1, 0, 1, 0, 1]; False
[1, 0, 0, 1, 0, 1, 0, 1, 1, 0]; False
[1, 0, 0, 1, 0, 1, 0, 1, 1, 1]; False
[1, 0, 0, 1, 0, 1, 1, 0, 0, 0]; False
[1, 0, 0, 1, 0, 1, 1, 0, 0, 1]; False
[1, 0, 0, 1, 0, 1, 1, 0, 1, 0]; False
[1, 0, 0, 1, 0, 1, 1, 0, 1, 1]; False
[1, 0, 0, 1, 0, 1, 1, 1, 0, 0]; False
[1, 0, 0, 1, 0, 1, 1, 1, 0, 1]; False
[1, 0, 0, 1, 0, 1, 1, 1, 1, 0]; False
[1, 0, 0, 1, 0, 1, 1, 1, 1, 1]; False
[1, 0, 0, 1, 1, 0, 0, 0, 0, 0]; False
[1, 0, 0, 1, 1, 0, 0, 0, 0, 1]; False
[1, 0, 0, 1, 1, 0, 0, 0, 1, 0]; False
[1, 0, 0, 1, 1, 0, 0, 0, 1, 1]; False
[1, 0, 0, 1, 1, 0, 0, 1, 0, 0]; False
[1, 0, 0, 1, 1, 0, 0, 1, 0, 1]; False
[1, 0, 0, 1, 1, 0, 0, 1, 1, 0]; False
[1, 0, 0, 1, 1, 0, 0, 1, 1, 1]; False
[1, 0, 0, 1, 1, 0, 1, 0, 0, 0]; False
[1, 0, 0, 1, 1, 0, 1, 0, 0, 1]; False
[1, 0, 0, 1, 1, 0, 1, 0, 1, 0]; False
[1, 0, 0, 1, 1, 0, 1, 0, 1, 1]; False
[1, 0, 0, 1, 1, 0, 1, 1, 0, 0]; False
[1, 0, 0, 1, 1, 0, 1, 1, 0, 1]; False
[1, 0, 0, 1, 1, 0, 1, 1, 1, 0]; False
[1, 0, 0, 1, 1, 0, 1, 1, 1, 1]; False
[1, 0, 0, 1, 1, 1, 0, 0, 0, 0]; False
[1, 0, 0, 1, 1, 1, 0, 0, 0, 1]; False
[1, 0, 0, 1, 1, 1, 0, 0, 1, 0]; False
[1, 0, 0, 1, 1, 1, 0, 0, 1, 1]; False
[1, 0, 0, 1, 1, 1, 0, 1, 0, 0]; False
[1, 0, 0, 1, 1, 1, 0, 1, 0, 1]; False
[1, 0, 0, 1, 1, 1, 0, 1, 1, 0]; False
[1, 0, 0, 1, 1, 1, 0, 1, 1, 1]; False
[1, 0, 0, 1, 1, 1, 1, 0, 0, 0]; False
[1, 0, 0, 1, 1, 1, 1, 0, 0, 1]; False
[1, 0, 0, 1, 1, 1, 1, 0, 1, 0]; False
[1, 0, 0, 1, 1, 1, 1, 0, 1, 1]; False
[1, 0, 0, 1, 1, 1, 1, 1, 0, 0]; False
[1, 0, 0, 1, 1, 1, 1, 1, 0, 1]; False
[1, 0, 0, 1, 1, 1, 1, 1, 1, 0]; False
[1, 0, 0, 1, 1, 1, 1, 1, 1, 1]; False
[1, 0, 1, 0, 0, 0, 0, 0, 0, 0]; False
[1, 0, 1, 0, 0, 0, 0, 0, 0, 1]; False
[1, 0, 1, 0, 0, 0, 0, 0, 1, 0]; False
[1, 0, 1, 0, 0, 0, 0, 0, 1, 1]; False
[1, 0, 1, 0, 0, 0, 0, 1, 0, 0]; False
[1, 0, 1, 0, 0, 0, 0, 1, 0, 1]; False
[1, 0, 1, 0, 0, 0, 0, 1, 1, 0]; False
[1, 0, 1, 0, 0, 0, 0, 1, 1, 1]; False
[1, 0, 1, 0, 0, 0, 1, 0, 0, 0]; False
[1, 0, 1, 0, 0, 0, 1, 0, 0, 1]; False
[1, 0, 1, 0, 0, 0, 1, 0, 1, 0]; False
[1, 0, 1, 0, 0, 0, 1, 0, 1, 1]; False
[1, 0, 1, 0, 0, 0, 1, 1, 0, 0]; False
[1, 0, 1, 0, 0, 0, 1, 1, 0, 1]; False
[1, 0, 1, 0, 0, 0, 1, 1, 1, 0]; False
[1, 0, 1, 0, 0, 0, 1, 1, 1, 1]; False
[1, 0, 1, 0, 0, 1, 0, 0, 0, 0]; False
[1, 0, 1, 0, 0, 1, 0, 0, 0, 1]; False
[1, 0, 1, 0, 0, 1, 0, 0, 1, 0]; False
[1, 0, 1, 0, 0, 1, 0, 0, 1, 1]; False
[1, 0, 1, 0, 0, 1, 0, 1, 0, 0]; False
[1, 0, 1, 0, 0, 1, 0, 1, 0, 1]; False
[1, 0, 1, 0, 0, 1, 0, 1, 1, 0]; False
[1, 0, 1, 0, 0, 1, 0, 1, 1, 1]; False
[1, 0, 1, 0, 0, 1, 1, 0, 0, 0]; False
[1, 0, 1, 0, 0, 1, 1, 0, 0, 1]; False
[1, 0, 1, 0, 0, 1, 1, 0, 1, 0]; False
[1, 0, 1, 0, 0, 1, 1, 0, 1, 1]; False
[1, 0, 1, 0, 0, 1, 1, 1, 0, 0]; False
[1, 0, 1, 0, 0, 1, 1, 1, 0, 1]; False
[1, 0, 1, 0, 0, 1, 1, 1, 1, 0]; False
[1, 0, 1, 0, 0, 1, 1, 1, 1, 1]; False
[1, 0, 1, 0, 1, 0, 0, 0, 0, 0]; False
[1, 0, 1, 0, 1, 0, 0, 0, 0, 1]; False
[1, 0, 1, 0, 1, 0, 0, 0, 1, 0]; False
[1, 0, 1, 0, 1, 0, 0, 0, 1, 1]; False
[1, 0, 1, 0, 1, 0, 0, 1, 0, 0]; False
[1, 0, 1, 0, 1, 0, 0, 1, 0, 1]; False
[1, 0, 1, 0, 1, 0, 0, 1, 1, 0]; False
[1, 0, 1, 0, 1, 0, 0, 1, 1, 1]; False
[1, 0, 1, 0, 1, 0, 1, 0, 0, 0]; False
[1, 0, 1, 0, 1, 0, 1, 0, 0, 1]; False
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]; False
[1, 0, 1, 0, 1, 0, 1, 0, 1, 1]; False
[1, 0, 1, 0, 1, 0, 1, 1, 0, 0]; False
[1, 0, 1, 0, 1, 0, 1, 1, 0, 1]; False
[1, 0, 1, 0, 1, 0, 1, 1, 1, 0]; False
[1, 0, 1, 0, 1, 0, 1, 1, 1, 1]; False
[1, 0, 1, 0, 1, 1, 0, 0, 0, 0]; False
[1, 0, 1, 0, 1, 1, 0, 0, 0, 1]; False
[1, 0, 1, 0, 1, 1, 0, 0, 1, 0]; False
[1, 0, 1, 0, 1, 1, 0, 0, 1, 1]; False
[1, 0, 1, 0, 1, 1, 0, 1, 0, 0]; False
[1, 0, 1, 0, 1, 1, 0, 1, 0, 1]; False
[1, 0, 1, 0, 1, 1, 0, 1, 1, 0]; False
[1, 0, 1, 0, 1, 1, 0, 1, 1, 1]; False
[1, 0, 1, 0, 1, 1, 1, 0, 0, 0]; False
[1, 0, 1, 0, 1, 1, 1, 0, 0, 1]; False
[1, 0, 1, 0, 1, 1, 1, 0, 1, 0]; False
[1, 0, 1, 0, 1, 1, 1, 0, 1, 1]; False
[1, 0, 1, 0, 1, 1, 1, 1, 0, 0]; False
[1, 0, 1, 0, 1, 1, 1, 1, 0, 1]; False
[1, 0, 1, 0, 1, 1, 1, 1, 1, 0]; False
[1, 0, 1, 0, 1, 1, 1, 1, 1, 1]; False
[1, 0, 1, 1, 0, 0, 0, 0, 0, 0]; False
[1, 0, 1, 1, 0, 0, 0, 0, 0, 1]; False
[1, 0, 1, 1, 0, 0, 0, 0, 1, 0]; False
[1, 0, 1, 1, 0, 0, 0, 0, 1, 1]; False
[1, 0, 1, 1, 0, 0, 0, 1, 0, 0]; False
[1, 0, 1, 1, 0, 0, 0, 1, 0, 1]; False
[1, 0, 1, 1, 0, 0, 0, 1, 1, 0]; False
[1, 0, 1, 1, 0, 0, 0, 1, 1, 1]; False
[1, 0, 1, 1, 0, 0, 1, 0, 0, 0]; False
[1, 0, 1, 1, 0, 0, 1, 0, 0, 1]; False
[1, 0, 1, 1, 0, 0, 1, 0, 1, 0]; False
[1, 0, 1, 1, 0, 0, 1, 0, 1, 1]; False
[1, 0, 1, 1, 0, 0, 1, 1, 0, 0]; False
[1, 0, 1, 1, 0, 0, 1, 1, 0, 1]; False
[1, 0, 1, 1, 0, 0, 1, 1, 1, 0]; False
[1, 0, 1, 1, 0, 0, 1, 1, 1, 1]; False
[1, 0, 1, 1, 0, 1, 0, 0, 0, 0]; False
[1, 0, 1, 1, 0, 1, 0, 0, 0, 1]; False
[1, 0, 1, 1, 0, 1, 0, 0, 1, 0]; False
[1, 0, 1, 1, 0, 1, 0, 0, 1, 1]; False
[1, 0, 1, 1, 0, 1, 0, 1, 0, 0]; False
[1, 0, 1, 1, 0, 1, 0, 1, 0, 1]; False
[1, 0, 1, 1, 0, 1, 0, 1, 1, 0]; False
[1, 0, 1, 1, 0, 1, 0, 1, 1, 1]; False
[1, 0, 1, 1, 0, 1, 1, 0, 0, 0]; False
[1, 0, 1, 1, 0, 1, 1, 0, 0, 1]; False
[1, 0, 1, 1, 0, 1, 1, 0, 1, 0]; False
[1, 0, 1, 1, 0, 1, 1, 0, 1, 1]; False
[1, 0, 1, 1, 0, 1, 1, 1, 0, 0]; False
[1, 0, 1, 1, 0, 1, 1, 1, 0, 1]; False
[1, 0, 1, 1, 0, 1, 1, 1, 1, 0]; False
[1, 0, 1, 1, 0, 1, 1, 1, 1, 1]; False
[1, 0, 1, 1, 1, 0, 0, 0, 0, 0]; False
[1, 0, 1, 1, 1, 0, 0, 0, 0, 1]; False
[1, 0, 1, 1, 1, 0, 0, 0, 1, 0]; False
[1, 0, 1, 1, 1, 0, 0, 0, 1, 1]; False
[1, 0, 1, 1, 1, 0, 0, 1, 0, 0]; False
[1, 0, 1, 1, 1, 0, 0, 1, 0, 1]; False
[1, 0, 1, 1, 1, 0, 0, 1, 1, 0]; False
[1, 0, 1, 1, 1, 0, 0, 1, 1, 1]; False
[1, 0, 1, 1, 1, 0, 1, 0, 0, 0]; False
[1, 0, 1, 1, 1, 0, 1, 0, 0, 1]; False
[1, 0, 1, 1, 1, 0, 1, 0, 1, 0]; False
[1, 0, 1, 1, 1, 0, 1, 0, 1, 1]; False
[1, 0, 1, 1, 1, 0, 1, 1, 0, 0]; False
[1, 0, 1, 1, 1, 0, 1, 1, 0, 1]; False
[1, 0, 1, 1, 1, 0, 1, 1, 1, 0]; False
[1, 0, 1, 1, 1, 0, 1, 1, 1, 1]; False
[1, 0, 1, 1, 1, 1, 0, 0, 0, 0]; False
[1, 0, 1, 1, 1, 1, 0, 0, 0, 1]; False
[1, 0, 1, 1, 1, 1, 0, 0, 1, 0]; False
[1, 0, 1, 1, 1, 1, 0, 0, 1, 1]; False
[1, 0, 1, 1, 1, 1, 0, 1, 0, 0]; False
[1, 0, 1, 1, 1, 1, 0, 1, 0, 1]; False
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0]; False
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1]; False
[1, 0, 1, 1, 1, 1, 1, 0, 0, 0]; False
[1, 0, 1, 1, 1, 1, 1, 0, 0, 1]; False
[1, 0, 1, 1, 1, 1, 1, 0, 1, 0]; False
[1, 0, 1, 1, 1, 1, 1, 0, 1, 1]; False
[1, 0, 1, 1, 1, 1, 1, 1, 0, 0]; False
[1, 0, 1, 1, 1, 1, 1, 1, 0, 1]; False
[1, 0, 1, 1, 1, 1, 1, 1, 1, 0]; False
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1]; False
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0]; False
[1, 1, 0, 0, 0, 0, 0, 0, 0, 1]; False
[1, 1, 0, 0, 0, 0, 0, 0, 1, 0]; False
[1, 1, 0, 0, 0, 0, 0, 0, 1, 1]; False
[1, 1, 0, 0, 0, 0, 0, 1, 0, 0]; False
[1, 1, 0, 0, 0, 0, 0, 1, 0, 1]; False
[1, 1, 0, 0, 0, 0, 0, 1, 1, 0]; False
[1, 1, 0, 0, 0, 0, 0, 1, 1, 1]; False
[1, 1, 0, 0, 0, 0, 1, 0, 0, 0]; False
[1, 1, 0, 0, 0, 0, 1, 0, 0, 1]; False
[1, 1, 0, 0, 0, 0, 1, 0, 1, 0]; False
[1, 1, 0, 0, 0, 0, 1, 0, 1, 1]; False
[1, 1, 0, 0, 0, 0, 1, 1, 0, 0]; False
[1, 1, 0, 0, 0, 0, 1, 1, 0, 1]; False
[1, 1, 0, 0, 0, 0, 1, 1, 1, 0]; False
[1, 1, 0, 0, 0, 0, 1, 1, 1, 1]; False
[1, 1, 0, 0, 0, 1, 0, 0, 0, 0]; False
[1, 1, 0, 0, 0, 1, 0, 0, 0, 1]; False
[1, 1, 0, 0, 0, 1, 0, 0, 1, 0]; False
[1, 1, 0, 0, 0, 1, 0, 0, 1, 1]; False
[1, 1, 0, 0, 0, 1, 0, 1, 0, 0]; False
[1, 1, 0, 0, 0, 1, 0, 1, 0, 1]; False
[1, 1, 0, 0, 0, 1, 0, 1, 1, 0]; False
[1, 1, 0, 0, 0, 1, 0, 1, 1, 1]; False
[1, 1, 0, 0, 0, 1, 1, 0, 0, 0]; False
[1, 1, 0, 0, 0, 1, 1, 0, 0, 1]; False
[1, 1, 0, 0, 0, 1, 1, 0, 1, 0]; False
[1, 1, 0, 0, 0, 1, 1, 0, 1, 1]; False
[1, 1, 0, 0, 0, 1, 1, 1, 0, 0]; False
[1, 1, 0, 0, 0, 1, 1, 1, 0, 1]; False
[1, 1, 0, 0, 0, 1, 1, 1, 1, 0]; False
[1, 1, 0, 0, 0, 1, 1, 1, 1, 1]; False
[1, 1, 0, 0, 1, 0, 0, 0, 0, 0]; False
[1, 1, 0, 0, 1, 0, 0, 0, 0, 1]; False
[1, 1, 0, 0, 1, 0, 0, 0, 1, 0]; False
[1, 1, 0, 0, 1, 0, 0, 0, 1, 1]; False
[1, 1, 0, 0, 1, 0, 0, 1, 0, 0]; False
[1, 1, 0, 0, 1, 0, 0, 1, 0, 1]; False
[1, 1, 0, 0, 1, 0, 0, 1, 1, 0]; False
[1, 1, 0, 0, 1, 0, 0, 1, 1, 1]; False
[1, 1, 0, 0, 1, 0, 1, 0, 0, 0]; False
[1, 1, 0, 0, 1, 0, 1, 0, 0, 1]; False
[1, 1, 0, 0, 1, 0, 1, 0, 1, 0]; False
[1, 1, 0, 0, 1, 0, 1, 0, 1, 1]; False
[1, 1, 0, 0, 1, 0, 1, 1, 0, 0]; False
[1, 1, 0, 0, 1, 0, 1, 1, 0, 1]; False
[1, 1, 0, 0, 1, 0, 1, 1, 1, 0]; False
[1, 1, 0, 0, 1, 0, 1, 1, 1, 1]; False
[1, 1, 0, 0, 1, 1, 0, 0, 0, 0]; False
[1, 1, 0, 0, 1, 1, 0, 0, 0, 1]; False
[1, 1, 0, 0, 1, 1, 0, 0, 1, 0]; False
[1, 1, 0, 0, 1, 1, 0, 0, 1, 1]; False
[1, 1, 0, 0, 1, 1, 0, 1, 0, 0]; False
[1, 1, 0, 0, 1, 1, 0, 1, 0, 1]; False
[1, 1, 0, 0, 1, 1, 0, 1, 1, 0]; False
[1, 1, 0, 0, 1, 1, 0, 1, 1, 1]; False
[1, 1, 0, 0, 1, 1, 1, 0, 0, 0]; False
[1, 1, 0, 0, 1, 1, 1, 0, 0, 1]; False
[1, 1, 0, 0, 1, 1, 1, 0, 1, 0]; False
[1, 1, 0, 0, 1, 1, 1, 0, 1, 1]; False
[1, 1, 0, 0, 1, 1, 1, 1, 0, 0]; False
[1, 1, 0, 0, 1, 1, 1, 1, 0, 1]; False
[1, 1, 0, 0, 1, 1, 1, 1, 1, 0]; False
[1, 1, 0, 0, 1, 1, 1, 1, 1, 1]; False
[1, 1, 0, 1, 0, 0, 0, 0, 0, 0]; False
[1, 1, 0, 1, 0, 0, 0, 0, 0, 1]; False
[1, 1, 0, 1, 0, 0, 0, 0, 1, 0]; False
[1, 1, 0, 1, 0, 0, 0, 0, 1, 1]; False
[1, 1, 0, 1, 0, 0, 0, 1, 0, 0]; False
[1, 1, 0, 1, 0, 0, 0, 1, 0, 1]; False
[1, 1, 0, 1, 0, 0, 0, 1, 1, 0]; False
[1, 1, 0, 1, 0, 0, 0, 1, 1, 1]; False
[1, 1, 0, 1, 0, 0, 1, 0, 0, 0]; False
[1, 1, 0, 1, 0, 0, 1, 0, 0, 1]; False
[1, 1, 0, 1, 0, 0, 1, 0, 1, 0]; False
[1, 1, 0, 1, 0, 0, 1, 0, 1, 1]; False
[1, 1, 0, 1, 0, 0, 1, 1, 0, 0]; False
[1, 1, 0, 1, 0, 0, 1, 1, 0, 1]; False
[1, 1, 0, 1, 0, 0, 1, 1, 1, 0]; False
[1, 1, 0, 1, 0, 0, 1, 1, 1, 1]; False
[1, 1, 0, 1, 0, 1, 0, 0, 0, 0]; False
[1, 1, 0, 1, 0, 1, 0, 0, 0, 1]; False
[1, 1, 0, 1, 0, 1, 0, 0, 1, 0]; False
[1, 1, 0, 1, 0, 1, 0, 0, 1, 1]; False
[1, 1, 0, 1, 0, 1, 0, 1, 0, 0]; False
[1, 1, 0, 1, 0, 1, 0, 1, 0, 1]; False
[1, 1, 0, 1, 0, 1, 0, 1, 1, 0]; False
[1, 1, 0, 1, 0, 1, 0, 1, 1, 1]; False
[1, 1, 0, 1, 0, 1, 1, 0, 0, 0]; False
[1, 1, 0, 1, 0, 1, 1, 0, 0, 1]; False
[1, 1, 0, 1, 0, 1, 1, 0, 1, 0]; False
[1, 1, 0, 1, 0, 1, 1, 0, 1, 1]; False
[1, 1, 0, 1, 0, 1, 1, 1, 0, 0]; False
[1, 1, 0, 1, 0, 1, 1, 1, 0, 1]; False
[1, 1, 0, 1, 0, 1, 1, 1, 1, 0]; False
[1, 1, 0, 1, 0, 1, 1, 1, 1, 1]; False
[1, 1, 0, 1, 1, 0, 0, 0, 0, 0]; False
[1, 1, 0, 1, 1, 0, 0, 0, 0, 1]; False
[1, 1, 0, 1, 1, 0, 0, 0, 1, 0]; False
[1, 1, 0, 1, 1, 0, 0, 0, 1, 1]; False
[1, 1, 0, 1, 1, 0, 0, 1, 0, 0]; False
[1, 1, 0, 1, 1, 0, 0, 1, 0, 1]; False
[1, 1, 0, 1, 1, 0, 0, 1, 1, 0]; False
[1, 1, 0, 1, 1, 0, 0, 1, 1, 1]; False
[1, 1, 0, 1, 1, 0, 1, 0, 0, 0]; False
[1, 1, 0, 1, 1, 0, 1, 0, 0, 1]; False
[1, 1, 0, 1, 1, 0, 1, 0, 1, 0]; False
[1, 1, 0, 1, 1, 0, 1, 0, 1, 1]; False
[1, 1, 0, 1, 1, 0, 1, 1, 0, 0]; False
[1, 1, 0, 1, 1, 0, 1, 1, 0, 1]; False
[1, 1, 0, 1, 1, 0, 1, 1, 1, 0]; False
[1, 1, 0, 1, 1, 0, 1, 1, 1, 1]; False
[1, 1, 0, 1, 1, 1, 0, 0, 0, 0]; False
[1, 1, 0, 1, 1, 1, 0, 0, 0, 1]; False
[1, 1, 0, 1, 1, 1, 0, 0, 1, 0]; False
[1, 1, 0, 1, 1, 1, 0, 0, 1, 1]; False
[1, 1, 0, 1, 1, 1, 0, 1, 0, 0]; False
[1, 1, 0, 1, 1, 1, 0, 1, 0, 1]; False
[1, 1, 0, 1, 1, 1, 0, 1, 1, 0]; False
[1, 1, 0, 1, 1, 1, 0, 1, 1, 1]; False
[1, 1, 0, 1, 1, 1, 1, 0, 0, 0]; False
[1, 1, 0, 1, 1, 1, 1, 0, 0, 1]; False
[1, 1, 0, 1, 1, 1, 1, 0, 1, 0]; False
[1, 1, 0, 1, 1, 1, 1, 0, 1, 1]; False
[1, 1, 0, 1, 1, 1, 1, 1, 0, 0]; False
[1, 1, 0, 1, 1, 1, 1, 1, 0, 1]; False
[1, 1, 0, 1, 1, 1, 1, 1, 1, 0]; False
[1, 1, 0, 1, 1, 1, 1, 1, 1, 1]; False
[1, 1, 1, 0, 0, 0, 0, 0, 0, 0]; False
[1, 1, 1, 0, 0, 0, 0, 0, 0, 1]; False
[1, 1, 1, 0, 0, 0, 0, 0, 1, 0]; False
[1, 1, 1, 0, 0, 0, 0, 0, 1, 1]; False
[1, 1, 1, 0, 0, 0, 0, 1, 0, 0]; False
[1, 1, 1, 0, 0, 0, 0, 1, 0, 1]; False
[1, 1, 1, 0, 0, 0, 0, 1, 1, 0]; False
[1, 1, 1, 0, 0, 0, 0, 1, 1, 1]; False
[1, 1, 1, 0, 0, 0, 1, 0, 0, 0]; False
[1, 1, 1, 0, 0, 0, 1, 0, 0, 1]; False
[1, 1, 1, 0, 0, 0, 1, 0, 1, 0]; False
[1, 1, 1, 0, 0, 0, 1, 0, 1, 1]; False
[1, 1, 1, 0, 0, 0, 1, 1, 0, 0]; False
[1, 1, 1, 0, 0, 0, 1, 1, 0, 1]; False
[1, 1, 1, 0, 0, 0, 1, 1, 1, 0]; False
[1, 1, 1, 0, 0, 0, 1, 1, 1, 1]; False
[1, 1, 1, 0, 0, 1, 0, 0, 0, 0]; False
[1, 1, 1, 0, 0, 1, 0, 0, 0, 1]; False
[1, 1, 1, 0, 0, 1, 0, 0, 1, 0]; False
[1, 1, 1, 0, 0, 1, 0, 0, 1, 1]; False
[1, 1, 1, 0, 0, 1, 0, 1, 0, 0]; False
[1, 1, 1, 0, 0, 1, 0, 1, 0, 1]; False
[1, 1, 1, 0, 0, 1, 0, 1, 1, 0]; False
[1, 1, 1, 0, 0, 1, 0, 1, 1, 1]; False
[1, 1, 1, 0, 0, 1, 1, 0, 0, 0]; False
[1, 1, 1, 0, 0, 1, 1, 0, 0, 1]; False
[1, 1, 1, 0, 0, 1, 1, 0, 1, 0]; False
[1, 1, 1, 0, 0, 1, 1, 0, 1, 1]; False
[1, 1, 1, 0, 0, 1, 1, 1, 0, 0]; False
[1, 1, 1, 0, 0, 1, 1, 1, 0, 1]; False
[1, 1, 1, 0, 0, 1, 1, 1, 1, 0]; False
[1, 1, 1, 0, 0, 1, 1, 1, 1, 1]; False
[1, 1, 1, 0, 1, 0, 0, 0, 0, 0]; False
[1, 1, 1, 0, 1, 0, 0, 0, 0, 1]; False
[1, 1, 1, 0, 1, 0, 0, 0, 1, 0]; False
[1, 1, 1, 0, 1, 0, 0, 0, 1, 1]; False
[1, 1, 1, 0, 1, 0, 0, 1, 0, 0]; False
[1, 1, 1, 0, 1, 0, 0, 1, 0, 1]; False
[1, 1, 1, 0, 1, 0, 0, 1, 1, 0]; False
[1, 1, 1, 0, 1, 0, 0, 1, 1, 1]; False
[1, 1, 1, 0, 1, 0, 1, 0, 0, 0]; False
[1, 1, 1, 0, 1, 0, 1, 0, 0, 1]; False
[1, 1, 1, 0, 1, 0, 1, 0, 1, 0]; False
[1, 1, 1, 0, 1, 0, 1, 0, 1, 1]; False
[1, 1, 1, 0, 1, 0, 1, 1, 0, 0]; False
[1, 1, 1, 0, 1, 0, 1, 1, 0, 1]; False
[1, 1, 1, 0, 1, 0, 1, 1, 1, 0]; False
[1, 1, 1, 0, 1, 0, 1, 1, 1, 1]; False
[1, 1, 1, 0, 1, 1, 0, 0, 0, 0]; False
[1, 1, 1, 0, 1, 1, 0, 0, 0, 1]; False
[1, 1, 1, 0, 1, 1, 0, 0, 1, 0]; False
[1, 1, 1, 0, 1, 1, 0, 0, 1, 1]; False
[1, 1, 1, 0, 1, 1, 0, 1, 0, 0]; False
[1, 1, 1, 0, 1, 1, 0, 1, 0, 1]; False
[1, 1, 1, 0, 1, 1, 0, 1, 1, 0]; False
[1, 1, 1, 0, 1, 1, 0, 1, 1, 1]; False
[1, 1, 1, 0, 1, 1, 1, 0, 0, 0]; False
[1, 1, 1, 0, 1, 1, 1, 0, 0, 1]; False
[1, 1, 1, 0, 1, 1, 1, 0, 1, 0]; False
[1, 1, 1, 0, 1, 1, 1, 0, 1, 1]; False
[1, 1, 1, 0, 1, 1, 1, 1, 0, 0]; False
[1, 1, 1, 0, 1, 1, 1, 1, 0, 1]; False
[1, 1, 1, 0, 1, 1, 1, 1, 1, 0]; False
[1, 1, 1, 0, 1, 1, 1, 1, 1, 1]; False
[1, 1, 1, 1, 0, 0, 0, 0, 0, 0]; False
[1, 1, 1, 1, 0, 0, 0, 0, 0, 1]; False
[1, 1, 1, 1, 0, 0, 0, 0, 1, 0]; False
[1, 1, 1, 1, 0, 0, 0, 0, 1, 1]; False
[1, 1, 1, 1, 0, 0, 0, 1, 0, 0]; False
[1, 1, 1, 1, 0, 0, 0, 1, 0, 1]; False
[1, 1, 1, 1, 0, 0, 0, 1, 1, 0]; False
[1, 1, 1, 1, 0, 0, 0, 1, 1, 1]; False
[1, 1, 1, 1, 0, 0, 1, 0, 0, 0]; False
[1, 1, 1, 1, 0, 0, 1, 0, 0, 1]; False
[1, 1, 1, 1, 0, 0, 1, 0, 1, 0]; False
[1, 1, 1, 1, 0, 0, 1, 0, 1, 1]; False
[1, 1, 1, 1, 0, 0, 1, 1, 0, 0]; False
[1, 1, 1, 1, 0, 0, 1, 1, 0, 1]; False
[1, 1, 1, 1, 0, 0, 1, 1, 1, 0]; False
[1, 1, 1, 1, 0, 0, 1, 1, 1, 1]; False
[1, 1, 1, 1, 0, 1, 0, 0, 0, 0]; False
[1, 1, 1, 1, 0, 1, 0, 0, 0, 1]; False
[1, 1, 1, 1, 0, 1, 0, 0, 1, 0]; False
[1, 1, 1, 1, 0, 1, 0, 0, 1, 1]; False
[1, 1, 1, 1, 0, 1, 0, 1, 0, 0]; False
[1, 1, 1, 1, 0, 1, 0, 1, 0, 1]; False
[1, 1, 1, 1, 0, 1, 0, 1, 1, 0]; False
[1, 1, 1, 1, 0, 1, 0, 1, 1, 1]; False
[1, 1, 1, 1, 0, 1, 1, 0, 0, 0]; False
[1, 1, 1, 1, 0, 1, 1, 0, 0, 1]; False
[1, 1, 1, 1, 0, 1, 1, 0, 1, 0]; False
[1, 1, 1, 1, 0, 1, 1, 0, 1, 1]; False
[1, 1, 1, 1, 0, 1, 1, 1, 0, 0]; False
[1, 1, 1, 1, 0, 1, 1, 1, 0, 1]; False
[1, 1, 1, 1, 0, 1, 1, 1, 1, 0]; False
[1, 1, 1, 1, 0, 1, 1, 1, 1, 1]; False
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0]; False
[1, 1, 1, 1, 1, 0, 0, 0, 0, 1]; False
[1, 1, 1, 1, 1, 0, 0, 0, 1, 0]; False
[1, 1, 1, 1, 1, 0, 0, 0, 1, 1]; False
[1, 1, 1, 1, 1, 0, 0, 1, 0, 0]; False
[1, 1, 1, 1, 1, 0, 0, 1, 0, 1]; False
[1, 1, 1, 1, 1, 0, 0, 1, 1, 0]; False
[1, 1, 1, 1, 1, 0, 0, 1, 1, 1]; False
[1, 1, 1, 1, 1, 0, 1, 0, 0, 0]; False
[1, 1, 1, 1, 1, 0, 1, 0, 0, 1]; False
[1, 1, 1, 1, 1, 0, 1, 0, 1, 0]; False
[1, 1, 1, 1, 1, 0, 1, 0, 1, 1]; False
[1, 1, 1, 1, 1, 0, 1, 1, 0, 0]; False
[1, 1, 1, 1, 1, 0, 1, 1, 0, 1]; False
[1, 1, 1, 1, 1, 0, 1, 1, 1, 0]; False
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1]; False
[1, 1, 1, 1, 1, 1, 0, 0, 0, 0]; False
[1, 1, 1, 1, 1, 1, 0, 0, 0, 1]; False
[1, 1, 1, 1, 1, 1, 0, 0, 1, 0]; False
[1, 1, 1, 1, 1, 1, 0, 0, 1, 1]; False
[1, 1, 1, 1, 1, 1, 0, 1, 0, 0]; False
[1, 1, 1, 1, 1, 1, 0, 1, 0, 1]; False
[1, 1, 1, 1, 1, 1, 0, 1, 1, 0]; False
[1, 1, 1, 1, 1, 1, 0, 1, 1, 1]; False
[1, 1, 1, 1, 1, 1, 1, 0, 0, 0]; False
[1, 1, 1, 1, 1, 1, 1, 0, 0, 1]; False
[1, 1, 1, 1, 1, 1, 1, 0, 1, 0]; False
[1, 1, 1, 1, 1, 1, 1, 0, 1, 1]; False
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0]; False
[1, 1, 1, 1, 1, 1, 1, 1, 0, 1]; False
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0]; False
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; False"""

tree_data = """[0]; True
[1]; False
[None]; False
[0, 0]; True
[0, 1]; False
[1, 0]; True
[1, 1]; False
[0, 0, 0]; False
[0, 0, 1]; True
[0, 1, 0]; False
[0, 1, 1]; False
[0, None, 0]; False
[0, None, 1]; False
[1, 0, 0]; False
[1, 0, 1]; True
[1, 1, 0]; False
[1, 1, 1]; False
[1, None, 0]; False
[1, None, 1]; False
[0, 0, 0, 0]; False
[0, 0, 0, 1]; False
[0, 0, 1, 0]; True
[0, 0, 1, 1]; False
[0, 0, None, 0]; True
[0, 0, None, 1]; False
[0, 1, 0, 0]; False
[0, 1, 0, 1]; False
[0, 1, 1, 0]; True
[0, 1, 1, 1]; False
[0, 1, None, 0]; True
[0, 1, None, 1]; False
[0, None, 0, 0]; False
[0, None, 0, 1]; False
[0, None, 1, 0]; False
[0, None, 1, 1]; False
[1, 0, 0, 0]; False
[1, 0, 0, 1]; False
[1, 0, 1, 0]; True
[1, 0, 1, 1]; False
[1, 0, None, 0]; True
[1, 0, None, 1]; False
[1, 1, 0, 0]; False
[1, 1, 0, 1]; False
[1, 1, 1, 0]; True
[1, 1, 1, 1]; False
[1, 1, None, 0]; True
[1, 1, None, 1]; False
[1, None, 0, 0]; False
[1, None, 0, 1]; False
[1, None, 1, 0]; False
[1, None, 1, 1]; False
[0, 0, 0, 0, 0]; False
[0, 0, 0, 0, 1]; False
[0, 0, 0, 1, 0]; False
[0, 0, 0, 1, 1]; False
[0, 0, 0, None, 0]; False
[0, 0, 0, None, 1]; False
[0, 0, 1, 0, 0]; False
[0, 0, 1, 0, 1]; True
[0, 0, 1, 1, 0]; False
[0, 0, 1, 1, 1]; False
[0, 0, 1, None, 0]; False
[0, 0, 1, None, 1]; False
[0, 0, None, 0, 0]; False
[0, 0, None, 0, 1]; True
[0, 0, None, 1, 0]; False
[0, 0, None, 1, 1]; False
[0, 0, None, None, 0]; False
[0, 0, None, None, 1]; False
[0, 1, 0, 0, 0]; False
[0, 1, 0, 0, 1]; False
[0, 1, 0, 1, 0]; False
[0, 1, 0, 1, 1]; False
[0, 1, 0, None, 0]; False
[0, 1, 0, None, 1]; False
[0, 1, 1, 0, 0]; False
[0, 1, 1, 0, 1]; True
[0, 1, 1, 1, 0]; False
[0, 1, 1, 1, 1]; False
[0, 1, 1, None, 0]; False
[0, 1, 1, None, 1]; False
[0, 1, None, 0, 0]; False
[0, 1, None, 0, 1]; True
[0, 1, None, 1, 0]; False
[0, 1, None, 1, 1]; False
[0, 1, None, None, 0]; False
[0, 1, None, None, 1]; False
[0, None, 0, 0, 0]; False
[0, None, 0, 0, 1]; False
[0, None, 0, 1, 0]; False
[0, None, 0, 1, 1]; False
[0, None, 0, None, 0]; False
[0, None, 0, None, 1]; False
[0, None, 1, 0, 0]; False
[0, None, 1, 0, 1]; False
[0, None, 1, 1, 0]; False
[0, None, 1, 1, 1]; False
[0, None, 1, None, 0]; False
[0, None, 1, None, 1]; False
[1, 0, 0, 0, 0]; False
[1, 0, 0, 0, 1]; False
[1, 0, 0, 1, 0]; False
[1, 0, 0, 1, 1]; False
[1, 0, 0, None, 0]; False
[1, 0, 0, None, 1]; False
[1, 0, 1, 0, 0]; False
[1, 0, 1, 0, 1]; True
[1, 0, 1, 1, 0]; False
[1, 0, 1, 1, 1]; False
[1, 0, 1, None, 0]; False
[1, 0, 1, None, 1]; False
[1, 0, None, 0, 0]; False
[1, 0, None, 0, 1]; True
[1, 0, None, 1, 0]; False
[1, 0, None, 1, 1]; False
[1, 0, None, None, 0]; False
[1, 0, None, None, 1]; False
[1, 1, 0, 0, 0]; False
[1, 1, 0, 0, 1]; False
[1, 1, 0, 1, 0]; False
[1, 1, 0, 1, 1]; False
[1, 1, 0, None, 0]; False
[1, 1, 0, None, 1]; False
[1, 1, 1, 0, 0]; False
[1, 1, 1, 0, 1]; True
[1, 1, 1, 1, 0]; False
[1, 1, 1, 1, 1]; False
[1, 1, 1, None, 0]; False
[1, 1, 1, None, 1]; False
[1, 1, None, 0, 0]; False
[1, 1, None, 0, 1]; True
[1, 1, None, 1, 0]; False
[1, 1, None, 1, 1]; False
[1, 1, None, None, 0]; False
[1, 1, None, None, 1]; False
[1, None, 0, 0, 0]; False
[1, None, 0, 0, 1]; False
[1, None, 0, 1, 0]; False
[1, None, 0, 1, 1]; False
[1, None, 0, None, 0]; False
[1, None, 0, None, 1]; False
[1, None, 1, 0, 0]; False
[1, None, 1, 0, 1]; False
[1, None, 1, 1, 0]; False
[1, None, 1, 1, 1]; False
[1, None, 1, None, 0]; False
[1, None, 1, None, 1]; False
[0, 0, 0, 0, 0, 0]; False
[0, 0, 0, 0, 0, 1]; False
[0, 0, 0, 0, 1, 0]; False
[0, 0, 0, 0, 1, 1]; True
[0, 0, 0, 0, None, 0]; False
[0, 0, 0, 0, None, 1]; True
[0, 0, 0, 1, 0, 0]; False
[0, 0, 0, 1, 0, 1]; False
[0, 0, 0, 1, 1, 0]; False
[0, 0, 0, 1, 1, 1]; False
[0, 0, 0, 1, None, 0]; False
[0, 0, 0, 1, None, 1]; False
[0, 0, 0, None, 0, 0]; False
[0, 0, 0, None, 0, 1]; False
[0, 0, 0, None, 1, 0]; False
[0, 0, 0, None, 1, 1]; False
[0, 0, 0, None, None, 0]; False
[0, 0, 0, None, None, 1]; True
[0, 0, 1, 0, 0, 0]; False
[0, 0, 1, 0, 0, 1]; False
[0, 0, 1, 0, 1, 0]; False
[0, 0, 1, 0, 1, 1]; True
[0, 0, 1, 0, None, 0]; False
[0, 0, 1, 0, None, 1]; True
[0, 0, 1, 1, 0, 0]; False
[0, 0, 1, 1, 0, 1]; False
[0, 0, 1, 1, 1, 0]; False
[0, 0, 1, 1, 1, 1]; False
[0, 0, 1, 1, None, 0]; False
[0, 0, 1, 1, None, 1]; False
[0, 0, 1, None, 0, 0]; False
[0, 0, 1, None, 0, 1]; False
[0, 0, 1, None, 1, 0]; False
[0, 0, 1, None, 1, 1]; False
[0, 0, 1, None, None, 0]; False
[0, 0, 1, None, None, 1]; True
[0, 0, None, 0, 0, 0]; False
[0, 0, None, 0, 0, 1]; False
[0, 0, None, 0, 1, 0]; True
[0, 0, None, 0, 1, 1]; False
[0, 0, None, 0, None, 0]; True
[0, 0, None, 0, None, 1]; False
[0, 0, None, 1, 0, 0]; False
[0, 0, None, 1, 0, 1]; False
[0, 0, None, 1, 1, 0]; True
[0, 0, None, 1, 1, 1]; False
[0, 0, None, 1, None, 0]; True
[0, 0, None, 1, None, 1]; False
[0, 0, None, None, 0, 0]; False
[0, 0, None, None, 0, 1]; False
[0, 0, None, None, 1, 0]; False
[0, 0, None, None, 1, 1]; False
[0, 1, 0, 0, 0, 0]; False
[0, 1, 0, 0, 0, 1]; False
[0, 1, 0, 0, 1, 0]; False
[0, 1, 0, 0, 1, 1]; True
[0, 1, 0, 0, None, 0]; False
[0, 1, 0, 0, None, 1]; True
[0, 1, 0, 1, 0, 0]; False
[0, 1, 0, 1, 0, 1]; False
[0, 1, 0, 1, 1, 0]; False
[0, 1, 0, 1, 1, 1]; False
[0, 1, 0, 1, None, 0]; False
[0, 1, 0, 1, None, 1]; False
[0, 1, 0, None, 0, 0]; False
[0, 1, 0, None, 0, 1]; False
[0, 1, 0, None, 1, 0]; False
[0, 1, 0, None, 1, 1]; False
[0, 1, 0, None, None, 0]; False
[0, 1, 0, None, None, 1]; False
[0, 1, 1, 0, 0, 0]; False
[0, 1, 1, 0, 0, 1]; False
[0, 1, 1, 0, 1, 0]; False
[0, 1, 1, 0, 1, 1]; True
[0, 1, 1, 0, None, 0]; False
[0, 1, 1, 0, None, 1]; True
[0, 1, 1, 1, 0, 0]; False
[0, 1, 1, 1, 0, 1]; False
[0, 1, 1, 1, 1, 0]; False
[0, 1, 1, 1, 1, 1]; False
[0, 1, 1, 1, None, 0]; False
[0, 1, 1, 1, None, 1]; False
[0, 1, 1, None, 0, 0]; False
[0, 1, 1, None, 0, 1]; False
[0, 1, 1, None, 1, 0]; False
[0, 1, 1, None, 1, 1]; False
[0, 1, 1, None, None, 0]; False
[0, 1, 1, None, None, 1]; False
[0, 1, None, 0, 0, 0]; False
[0, 1, None, 0, 0, 1]; False
[0, 1, None, 0, 1, 0]; True
[0, 1, None, 0, 1, 1]; False
[0, 1, None, 0, None, 0]; True
[0, 1, None, 0, None, 1]; False
[0, 1, None, 1, 0, 0]; False
[0, 1, None, 1, 0, 1]; False
[0, 1, None, 1, 1, 0]; True
[0, 1, None, 1, 1, 1]; False
[0, 1, None, 1, None, 0]; True
[0, 1, None, 1, None, 1]; False
[0, 1, None, None, 0, 0]; False
[0, 1, None, None, 0, 1]; False
[0, 1, None, None, 1, 0]; False
[0, 1, None, None, 1, 1]; False
[0, None, 0, 0, 0, 0]; False
[0, None, 0, 0, 0, 1]; False
[0, None, 0, 0, 1, 0]; False
[0, None, 0, 0, 1, 1]; False
[0, None, 0, 0, None, 0]; False
[0, None, 0, 0, None, 1]; False
[0, None, 0, 1, 0, 0]; False
[0, None, 0, 1, 0, 1]; False
[0, None, 0, 1, 1, 0]; False
[0, None, 0, 1, 1, 1]; False
[0, None, 0, 1, None, 0]; False
[0, None, 0, 1, None, 1]; False
[0, None, 0, None, 0, 0]; False
[0, None, 0, None, 0, 1]; False
[0, None, 0, None, 1, 0]; False
[0, None, 0, None, 1, 1]; False
[0, None, 1, 0, 0, 0]; False
[0, None, 1, 0, 0, 1]; False
[0, None, 1, 0, 1, 0]; False
[0, None, 1, 0, 1, 1]; False
[0, None, 1, 0, None, 0]; False
[0, None, 1, 0, None, 1]; False
[0, None, 1, 1, 0, 0]; False
[0, None, 1, 1, 0, 1]; False
[0, None, 1, 1, 1, 0]; False
[0, None, 1, 1, 1, 1]; False
[0, None, 1, 1, None, 0]; False
[0, None, 1, 1, None, 1]; False
[0, None, 1, None, 0, 0]; False
[0, None, 1, None, 0, 1]; False
[0, None, 1, None, 1, 0]; False
[0, None, 1, None, 1, 1]; False
[1, 0, 0, 0, 0, 0]; False
[1, 0, 0, 0, 0, 1]; False
[1, 0, 0, 0, 1, 0]; False
[1, 0, 0, 0, 1, 1]; True
[1, 0, 0, 0, None, 0]; False
[1, 0, 0, 0, None, 1]; True
[1, 0, 0, 1, 0, 0]; False
[1, 0, 0, 1, 0, 1]; False
[1, 0, 0, 1, 1, 0]; False
[1, 0, 0, 1, 1, 1]; False
[1, 0, 0, 1, None, 0]; False
[1, 0, 0, 1, None, 1]; False
[1, 0, 0, None, 0, 0]; False
[1, 0, 0, None, 0, 1]; False
[1, 0, 0, None, 1, 0]; False
[1, 0, 0, None, 1, 1]; False
[1, 0, 0, None, None, 0]; False
[1, 0, 0, None, None, 1]; True
[1, 0, 1, 0, 0, 0]; False
[1, 0, 1, 0, 0, 1]; False
[1, 0, 1, 0, 1, 0]; False
[1, 0, 1, 0, 1, 1]; True
[1, 0, 1, 0, None, 0]; False
[1, 0, 1, 0, None, 1]; True
[1, 0, 1, 1, 0, 0]; False
[1, 0, 1, 1, 0, 1]; False
[1, 0, 1, 1, 1, 0]; False
[1, 0, 1, 1, 1, 1]; False
[1, 0, 1, 1, None, 0]; False
[1, 0, 1, 1, None, 1]; False
[1, 0, 1, None, 0, 0]; False
[1, 0, 1, None, 0, 1]; False
[1, 0, 1, None, 1, 0]; False
[1, 0, 1, None, 1, 1]; False
[1, 0, 1, None, None, 0]; False
[1, 0, 1, None, None, 1]; True
[1, 0, None, 0, 0, 0]; False
[1, 0, None, 0, 0, 1]; False
[1, 0, None, 0, 1, 0]; True
[1, 0, None, 0, 1, 1]; False
[1, 0, None, 0, None, 0]; True
[1, 0, None, 0, None, 1]; False
[1, 0, None, 1, 0, 0]; False
[1, 0, None, 1, 0, 1]; False
[1, 0, None, 1, 1, 0]; True
[1, 0, None, 1, 1, 1]; False
[1, 0, None, 1, None, 0]; True
[1, 0, None, 1, None, 1]; False
[1, 0, None, None, 0, 0]; False
[1, 0, None, None, 0, 1]; False
[1, 0, None, None, 1, 0]; False
[1, 0, None, None, 1, 1]; False
[1, 1, 0, 0, 0, 0]; False
[1, 1, 0, 0, 0, 1]; False
[1, 1, 0, 0, 1, 0]; False
[1, 1, 0, 0, 1, 1]; True
[1, 1, 0, 0, None, 0]; False
[1, 1, 0, 0, None, 1]; True
[1, 1, 0, 1, 0, 0]; False
[1, 1, 0, 1, 0, 1]; False
[1, 1, 0, 1, 1, 0]; False
[1, 1, 0, 1, 1, 1]; False
[1, 1, 0, 1, None, 0]; False
[1, 1, 0, 1, None, 1]; False
[1, 1, 0, None, 0, 0]; False
[1, 1, 0, None, 0, 1]; False
[1, 1, 0, None, 1, 0]; False
[1, 1, 0, None, 1, 1]; False
[1, 1, 0, None, None, 0]; False
[1, 1, 0, None, None, 1]; False
[1, 1, 1, 0, 0, 0]; False
[1, 1, 1, 0, 0, 1]; False
[1, 1, 1, 0, 1, 0]; False
[1, 1, 1, 0, 1, 1]; True
[1, 1, 1, 0, None, 0]; False
[1, 1, 1, 0, None, 1]; True
[1, 1, 1, 1, 0, 0]; False
[1, 1, 1, 1, 0, 1]; False
[1, 1, 1, 1, 1, 0]; False
[1, 1, 1, 1, 1, 1]; False
[1, 1, 1, 1, None, 0]; False
[1, 1, 1, 1, None, 1]; False
[1, 1, 1, None, 0, 0]; False
[1, 1, 1, None, 0, 1]; False
[1, 1, 1, None, 1, 0]; False
[1, 1, 1, None, 1, 1]; False
[1, 1, 1, None, None, 0]; False
[1, 1, 1, None, None, 1]; False
[1, 1, None, 0, 0, 0]; False
[1, 1, None, 0, 0, 1]; False
[1, 1, None, 0, 1, 0]; True
[1, 1, None, 0, 1, 1]; False
[1, 1, None, 0, None, 0]; True
[1, 1, None, 0, None, 1]; False
[1, 1, None, 1, 0, 0]; False
[1, 1, None, 1, 0, 1]; False
[1, 1, None, 1, 1, 0]; True
[1, 1, None, 1, 1, 1]; False
[1, 1, None, 1, None, 0]; True
[1, 1, None, 1, None, 1]; False
[1, 1, None, None, 0, 0]; False
[1, 1, None, None, 0, 1]; False
[1, 1, None, None, 1, 0]; False
[1, 1, None, None, 1, 1]; False
[1, None, 0, 0, 0, 0]; False
[1, None, 0, 0, 0, 1]; False
[1, None, 0, 0, 1, 0]; False
[1, None, 0, 0, 1, 1]; False
[1, None, 0, 0, None, 0]; False
[1, None, 0, 0, None, 1]; False
[1, None, 0, 1, 0, 0]; False
[1, None, 0, 1, 0, 1]; False
[1, None, 0, 1, 1, 0]; False
[1, None, 0, 1, 1, 1]; False
[1, None, 0, 1, None, 0]; False
[1, None, 0, 1, None, 1]; False
[1, None, 0, None, 0, 0]; False
[1, None, 0, None, 0, 1]; False
[1, None, 0, None, 1, 0]; False
[1, None, 0, None, 1, 1]; False
[1, None, 1, 0, 0, 0]; False
[1, None, 1, 0, 0, 1]; False
[1, None, 1, 0, 1, 0]; False
[1, None, 1, 0, 1, 1]; False
[1, None, 1, 0, None, 0]; False
[1, None, 1, 0, None, 1]; False
[1, None, 1, 1, 0, 0]; False
[1, None, 1, 1, 0, 1]; False
[1, None, 1, 1, 1, 0]; False
[1, None, 1, 1, 1, 1]; False
[1, None, 1, 1, None, 0]; False
[1, None, 1, 1, None, 1]; False
[1, None, 1, None, 0, 0]; False
[1, None, 1, None, 0, 1]; False
[1, None, 1, None, 1, 0]; False
[1, None, 1, None, 1, 1]; False
[0, 0, 0, 0, 0, 0, 0]; False
[0, 0, 0, 0, 0, 0, 1]; False
[0, 0, 0, 0, 0, 1, 0]; False
[0, 0, 0, 0, 0, 1, 1]; False
[0, 0, 0, 0, 0, None, 0]; False
[0, 0, 0, 0, 0, None, 1]; False
[0, 0, 0, 0, 1, 0, 0]; False
[0, 0, 0, 0, 1, 0, 1]; False
[0, 0, 0, 0, 1, 1, 0]; True
[0, 0, 0, 0, 1, 1, 1]; True
[0, 0, 0, 0, 1, None, 0]; True
[0, 0, 0, 0, 1, None, 1]; True
[0, 0, 0, 0, None, 0, 0]; False
[0, 0, 0, 0, None, 0, 1]; False
[0, 0, 0, 0, None, 1, 0]; True
[0, 0, 0, 0, None, 1, 1]; True
[0, 0, 0, 0, None, None, 0]; True
[0, 0, 0, 0, None, None, 1]; True
[0, 0, 0, 1, 0, 0, 0]; False
[0, 0, 0, 1, 0, 0, 1]; False
[0, 0, 0, 1, 0, 1, 0]; False
[0, 0, 0, 1, 0, 1, 1]; False
[0, 0, 0, 1, 0, None, 0]; False
[0, 0, 0, 1, 0, None, 1]; False
[0, 0, 0, 1, 1, 0, 0]; False
[0, 0, 0, 1, 1, 0, 1]; False
[0, 0, 0, 1, 1, 1, 0]; False
[0, 0, 0, 1, 1, 1, 1]; False
[0, 0, 0, 1, 1, None, 0]; False
[0, 0, 0, 1, 1, None, 1]; False
[0, 0, 0, 1, None, 0, 0]; False
[0, 0, 0, 1, None, 0, 1]; False
[0, 0, 0, 1, None, 1, 0]; False
[0, 0, 0, 1, None, 1, 1]; False
[0, 0, 0, 1, None, None, 0]; False
[0, 0, 0, 1, None, None, 1]; False
[0, 0, 0, None, 0, 0, 0]; False
[0, 0, 0, None, 0, 0, 1]; False
[0, 0, 0, None, 0, 1, 0]; False
[0, 0, 0, None, 0, 1, 1]; False
[0, 0, 0, None, 0, None, 0]; False
[0, 0, 0, None, 0, None, 1]; False
[0, 0, 0, None, 1, 0, 0]; False
[0, 0, 0, None, 1, 0, 1]; False
[0, 0, 0, None, 1, 1, 0]; False
[0, 0, 0, None, 1, 1, 1]; False
[0, 0, 0, None, 1, None, 0]; False
[0, 0, 0, None, 1, None, 1]; False
[0, 0, 0, None, None, 0, 0]; False
[0, 0, 0, None, None, 0, 1]; False
[0, 0, 0, None, None, 1, 0]; False
[0, 0, 0, None, None, 1, 1]; True
[0, 0, 0, None, None, None, 0]; False
[0, 0, 0, None, None, None, 1]; True
[0, 0, 1, 0, 0, 0, 0]; False
[0, 0, 1, 0, 0, 0, 1]; False
[0, 0, 1, 0, 0, 1, 0]; False
[0, 0, 1, 0, 0, 1, 1]; False
[0, 0, 1, 0, 0, None, 0]; False
[0, 0, 1, 0, 0, None, 1]; False
[0, 0, 1, 0, 1, 0, 0]; True
[0, 0, 1, 0, 1, 0, 1]; False
[0, 0, 1, 0, 1, 1, 0]; True
[0, 0, 1, 0, 1, 1, 1]; True
[0, 0, 1, 0, 1, None, 0]; True
[0, 0, 1, 0, 1, None, 1]; True
[0, 0, 1, 0, None, 0, 0]; True
[0, 0, 1, 0, None, 0, 1]; False
[0, 0, 1, 0, None, 1, 0]; True
[0, 0, 1, 0, None, 1, 1]; True
[0, 0, 1, 0, None, None, 0]; True
[0, 0, 1, 0, None, None, 1]; True
[0, 0, 1, 1, 0, 0, 0]; False
[0, 0, 1, 1, 0, 0, 1]; False
[0, 0, 1, 1, 0, 1, 0]; False
[0, 0, 1, 1, 0, 1, 1]; False
[0, 0, 1, 1, 0, None, 0]; False
[0, 0, 1, 1, 0, None, 1]; False
[0, 0, 1, 1, 1, 0, 0]; False
[0, 0, 1, 1, 1, 0, 1]; False
[0, 0, 1, 1, 1, 1, 0]; False
[0, 0, 1, 1, 1, 1, 1]; False
[0, 0, 1, 1, 1, None, 0]; False
[0, 0, 1, 1, 1, None, 1]; False
[0, 0, 1, 1, None, 0, 0]; False
[0, 0, 1, 1, None, 0, 1]; False
[0, 0, 1, 1, None, 1, 0]; False
[0, 0, 1, 1, None, 1, 1]; False
[0, 0, 1, 1, None, None, 0]; False
[0, 0, 1, 1, None, None, 1]; False
[0, 0, 1, None, 0, 0, 0]; False
[0, 0, 1, None, 0, 0, 1]; False
[0, 0, 1, None, 0, 1, 0]; False
[0, 0, 1, None, 0, 1, 1]; False
[0, 0, 1, None, 0, None, 0]; False
[0, 0, 1, None, 0, None, 1]; False
[0, 0, 1, None, 1, 0, 0]; False
[0, 0, 1, None, 1, 0, 1]; False
[0, 0, 1, None, 1, 1, 0]; False
[0, 0, 1, None, 1, 1, 1]; False
[0, 0, 1, None, 1, None, 0]; False
[0, 0, 1, None, 1, None, 1]; False
[0, 0, 1, None, None, 0, 0]; False
[0, 0, 1, None, None, 0, 1]; False
[0, 0, 1, None, None, 1, 0]; True
[0, 0, 1, None, None, 1, 1]; True
[0, 0, 1, None, None, None, 0]; True
[0, 0, 1, None, None, None, 1]; True
[0, 0, None, 0, 0, 0, 0]; False
[0, 0, None, 0, 0, 0, 1]; False
[0, 0, None, 0, 0, 1, 0]; False
[0, 0, None, 0, 0, 1, 1]; False
[0, 0, None, 0, 0, None, 0]; False
[0, 0, None, 0, 0, None, 1]; False
[0, 0, None, 0, 1, 0, 0]; False
[0, 0, None, 0, 1, 0, 1]; True
[0, 0, None, 0, 1, 1, 0]; False
[0, 0, None, 0, 1, 1, 1]; False
[0, 0, None, 0, 1, None, 0]; False
[0, 0, None, 0, 1, None, 1]; False
[0, 0, None, 0, None, 0, 0]; False
[0, 0, None, 0, None, 0, 1]; True
[0, 0, None, 0, None, 1, 0]; False
[0, 0, None, 0, None, 1, 1]; False
[0, 0, None, 0, None, None, 0]; False
[0, 0, None, 0, None, None, 1]; False
[0, 0, None, 1, 0, 0, 0]; False
[0, 0, None, 1, 0, 0, 1]; False
[0, 0, None, 1, 0, 1, 0]; False
[0, 0, None, 1, 0, 1, 1]; False
[0, 0, None, 1, 0, None, 0]; False
[0, 0, None, 1, 0, None, 1]; False
[0, 0, None, 1, 1, 0, 0]; False
[0, 0, None, 1, 1, 0, 1]; True
[0, 0, None, 1, 1, 1, 0]; False
[0, 0, None, 1, 1, 1, 1]; False
[0, 0, None, 1, 1, None, 0]; False
[0, 0, None, 1, 1, None, 1]; False
[0, 0, None, 1, None, 0, 0]; False
[0, 0, None, 1, None, 0, 1]; True
[0, 0, None, 1, None, 1, 0]; False
[0, 0, None, 1, None, 1, 1]; False
[0, 0, None, 1, None, None, 0]; False
[0, 0, None, 1, None, None, 1]; False
[0, 0, None, None, 0, 0, 0]; False
[0, 0, None, None, 0, 0, 1]; False
[0, 0, None, None, 0, 1, 0]; False
[0, 0, None, None, 0, 1, 1]; False
[0, 0, None, None, 0, None, 0]; False
[0, 0, None, None, 0, None, 1]; False
[0, 0, None, None, 1, 0, 0]; False
[0, 0, None, None, 1, 0, 1]; False
[0, 0, None, None, 1, 1, 0]; False
[0, 0, None, None, 1, 1, 1]; False
[0, 0, None, None, 1, None, 0]; False
[0, 0, None, None, 1, None, 1]; False
[0, 1, 0, 0, 0, 0, 0]; False
[0, 1, 0, 0, 0, 0, 1]; False
[0, 1, 0, 0, 0, 1, 0]; False
[0, 1, 0, 0, 0, 1, 1]; False
[0, 1, 0, 0, 0, None, 0]; False
[0, 1, 0, 0, 0, None, 1]; False
[0, 1, 0, 0, 1, 0, 0]; False
[0, 1, 0, 0, 1, 0, 1]; False
[0, 1, 0, 0, 1, 1, 0]; False
[0, 1, 0, 0, 1, 1, 1]; True
[0, 1, 0, 0, 1, None, 0]; False
[0, 1, 0, 0, 1, None, 1]; True
[0, 1, 0, 0, None, 0, 0]; False
[0, 1, 0, 0, None, 0, 1]; False
[0, 1, 0, 0, None, 1, 0]; False
[0, 1, 0, 0, None, 1, 1]; True
[0, 1, 0, 0, None, None, 0]; False
[0, 1, 0, 0, None, None, 1]; True
[0, 1, 0, 1, 0, 0, 0]; False
[0, 1, 0, 1, 0, 0, 1]; False
[0, 1, 0, 1, 0, 1, 0]; False
[0, 1, 0, 1, 0, 1, 1]; False
[0, 1, 0, 1, 0, None, 0]; False
[0, 1, 0, 1, 0, None, 1]; False
[0, 1, 0, 1, 1, 0, 0]; False
[0, 1, 0, 1, 1, 0, 1]; False
[0, 1, 0, 1, 1, 1, 0]; False
[0, 1, 0, 1, 1, 1, 1]; False
[0, 1, 0, 1, 1, None, 0]; False
[0, 1, 0, 1, 1, None, 1]; False
[0, 1, 0, 1, None, 0, 0]; False
[0, 1, 0, 1, None, 0, 1]; False
[0, 1, 0, 1, None, 1, 0]; False
[0, 1, 0, 1, None, 1, 1]; False
[0, 1, 0, 1, None, None, 0]; False
[0, 1, 0, 1, None, None, 1]; False
[0, 1, 0, None, 0, 0, 0]; False
[0, 1, 0, None, 0, 0, 1]; False
[0, 1, 0, None, 0, 1, 0]; False
[0, 1, 0, None, 0, 1, 1]; False
[0, 1, 0, None, 0, None, 0]; False
[0, 1, 0, None, 0, None, 1]; False
[0, 1, 0, None, 1, 0, 0]; False
[0, 1, 0, None, 1, 0, 1]; False
[0, 1, 0, None, 1, 1, 0]; False
[0, 1, 0, None, 1, 1, 1]; False
[0, 1, 0, None, 1, None, 0]; False
[0, 1, 0, None, 1, None, 1]; False
[0, 1, 0, None, None, 0, 0]; False
[0, 1, 0, None, None, 0, 1]; False
[0, 1, 0, None, None, 1, 0]; False
[0, 1, 0, None, None, 1, 1]; False
[0, 1, 0, None, None, None, 0]; False
[0, 1, 0, None, None, None, 1]; False
[0, 1, 1, 0, 0, 0, 0]; False
[0, 1, 1, 0, 0, 0, 1]; False
[0, 1, 1, 0, 0, 1, 0]; False
[0, 1, 1, 0, 0, 1, 1]; False
[0, 1, 1, 0, 0, None, 0]; False
[0, 1, 1, 0, 0, None, 1]; False
[0, 1, 1, 0, 1, 0, 0]; False
[0, 1, 1, 0, 1, 0, 1]; False
[0, 1, 1, 0, 1, 1, 0]; True
[0, 1, 1, 0, 1, 1, 1]; True
[0, 1, 1, 0, 1, None, 0]; True
[0, 1, 1, 0, 1, None, 1]; True
[0, 1, 1, 0, None, 0, 0]; False
[0, 1, 1, 0, None, 0, 1]; False
[0, 1, 1, 0, None, 1, 0]; True
[0, 1, 1, 0, None, 1, 1]; True
[0, 1, 1, 0, None, None, 0]; True
[0, 1, 1, 0, None, None, 1]; True
[0, 1, 1, 1, 0, 0, 0]; False
[0, 1, 1, 1, 0, 0, 1]; False
[0, 1, 1, 1, 0, 1, 0]; False
[0, 1, 1, 1, 0, 1, 1]; False
[0, 1, 1, 1, 0, None, 0]; False
[0, 1, 1, 1, 0, None, 1]; False
[0, 1, 1, 1, 1, 0, 0]; False
[0, 1, 1, 1, 1, 0, 1]; False
[0, 1, 1, 1, 1, 1, 0]; False
[0, 1, 1, 1, 1, 1, 1]; False
[0, 1, 1, 1, 1, None, 0]; False
[0, 1, 1, 1, 1, None, 1]; False
[0, 1, 1, 1, None, 0, 0]; False
[0, 1, 1, 1, None, 0, 1]; False
[0, 1, 1, 1, None, 1, 0]; False
[0, 1, 1, 1, None, 1, 1]; False
[0, 1, 1, 1, None, None, 0]; False
[0, 1, 1, 1, None, None, 1]; False
[0, 1, 1, None, 0, 0, 0]; False
[0, 1, 1, None, 0, 0, 1]; False
[0, 1, 1, None, 0, 1, 0]; False
[0, 1, 1, None, 0, 1, 1]; False
[0, 1, 1, None, 0, None, 0]; False
[0, 1, 1, None, 0, None, 1]; False
[0, 1, 1, None, 1, 0, 0]; False
[0, 1, 1, None, 1, 0, 1]; False
[0, 1, 1, None, 1, 1, 0]; False
[0, 1, 1, None, 1, 1, 1]; False
[0, 1, 1, None, 1, None, 0]; False
[0, 1, 1, None, 1, None, 1]; False
[0, 1, 1, None, None, 0, 0]; False
[0, 1, 1, None, None, 0, 1]; False
[0, 1, 1, None, None, 1, 0]; False
[0, 1, 1, None, None, 1, 1]; False
[0, 1, 1, None, None, None, 0]; False
[0, 1, 1, None, None, None, 1]; False
[0, 1, None, 0, 0, 0, 0]; False
[0, 1, None, 0, 0, 0, 1]; False
[0, 1, None, 0, 0, 1, 0]; False
[0, 1, None, 0, 0, 1, 1]; False
[0, 1, None, 0, 0, None, 0]; False
[0, 1, None, 0, 0, None, 1]; False
[0, 1, None, 0, 1, 0, 0]; False
[0, 1, None, 0, 1, 0, 1]; True
[0, 1, None, 0, 1, 1, 0]; False
[0, 1, None, 0, 1, 1, 1]; False
[0, 1, None, 0, 1, None, 0]; False
[0, 1, None, 0, 1, None, 1]; False
[0, 1, None, 0, None, 0, 0]; False
[0, 1, None, 0, None, 0, 1]; True
[0, 1, None, 0, None, 1, 0]; False
[0, 1, None, 0, None, 1, 1]; False
[0, 1, None, 0, None, None, 0]; False
[0, 1, None, 0, None, None, 1]; False
[0, 1, None, 1, 0, 0, 0]; False
[0, 1, None, 1, 0, 0, 1]; False
[0, 1, None, 1, 0, 1, 0]; False
[0, 1, None, 1, 0, 1, 1]; False
[0, 1, None, 1, 0, None, 0]; False
[0, 1, None, 1, 0, None, 1]; False
[0, 1, None, 1, 1, 0, 0]; False
[0, 1, None, 1, 1, 0, 1]; True
[0, 1, None, 1, 1, 1, 0]; False
[0, 1, None, 1, 1, 1, 1]; False
[0, 1, None, 1, 1, None, 0]; False
[0, 1, None, 1, 1, None, 1]; False
[0, 1, None, 1, None, 0, 0]; False
[0, 1, None, 1, None, 0, 1]; True
[0, 1, None, 1, None, 1, 0]; False
[0, 1, None, 1, None, 1, 1]; False
[0, 1, None, 1, None, None, 0]; False
[0, 1, None, 1, None, None, 1]; False
[0, 1, None, None, 0, 0, 0]; False
[0, 1, None, None, 0, 0, 1]; False
[0, 1, None, None, 0, 1, 0]; False
[0, 1, None, None, 0, 1, 1]; False
[0, 1, None, None, 0, None, 0]; False
[0, 1, None, None, 0, None, 1]; False
[0, 1, None, None, 1, 0, 0]; False
[0, 1, None, None, 1, 0, 1]; False
[0, 1, None, None, 1, 1, 0]; False
[0, 1, None, None, 1, 1, 1]; False
[0, 1, None, None, 1, None, 0]; False
[0, 1, None, None, 1, None, 1]; False
[0, None, 0, 0, 0, 0, 0]; False
[0, None, 0, 0, 0, 0, 1]; False
[0, None, 0, 0, 0, 1, 0]; False
[0, None, 0, 0, 0, 1, 1]; False
[0, None, 0, 0, 0, None, 0]; False
[0, None, 0, 0, 0, None, 1]; False
[0, None, 0, 0, 1, 0, 0]; False
[0, None, 0, 0, 1, 0, 1]; False
[0, None, 0, 0, 1, 1, 0]; False
[0, None, 0, 0, 1, 1, 1]; False
[0, None, 0, 0, 1, None, 0]; False
[0, None, 0, 0, 1, None, 1]; False
[0, None, 0, 0, None, 0, 0]; False
[0, None, 0, 0, None, 0, 1]; False
[0, None, 0, 0, None, 1, 0]; False
[0, None, 0, 0, None, 1, 1]; False
[0, None, 0, 0, None, None, 0]; False
[0, None, 0, 0, None, None, 1]; False
[0, None, 0, 1, 0, 0, 0]; False
[0, None, 0, 1, 0, 0, 1]; False
[0, None, 0, 1, 0, 1, 0]; False
[0, None, 0, 1, 0, 1, 1]; False
[0, None, 0, 1, 0, None, 0]; False
[0, None, 0, 1, 0, None, 1]; False
[0, None, 0, 1, 1, 0, 0]; False
[0, None, 0, 1, 1, 0, 1]; False
[0, None, 0, 1, 1, 1, 0]; False
[0, None, 0, 1, 1, 1, 1]; False
[0, None, 0, 1, 1, None, 0]; False
[0, None, 0, 1, 1, None, 1]; False
[0, None, 0, 1, None, 0, 0]; False
[0, None, 0, 1, None, 0, 1]; False
[0, None, 0, 1, None, 1, 0]; False
[0, None, 0, 1, None, 1, 1]; False
[0, None, 0, 1, None, None, 0]; False
[0, None, 0, 1, None, None, 1]; False
[0, None, 0, None, 0, 0, 0]; False
[0, None, 0, None, 0, 0, 1]; False
[0, None, 0, None, 0, 1, 0]; False
[0, None, 0, None, 0, 1, 1]; False
[0, None, 0, None, 0, None, 0]; False
[0, None, 0, None, 0, None, 1]; False
[0, None, 0, None, 1, 0, 0]; False
[0, None, 0, None, 1, 0, 1]; False
[0, None, 0, None, 1, 1, 0]; False
[0, None, 0, None, 1, 1, 1]; False
[0, None, 0, None, 1, None, 0]; False
[0, None, 0, None, 1, None, 1]; False
[0, None, 1, 0, 0, 0, 0]; False
[0, None, 1, 0, 0, 0, 1]; False
[0, None, 1, 0, 0, 1, 0]; False
[0, None, 1, 0, 0, 1, 1]; False
[0, None, 1, 0, 0, None, 0]; False
[0, None, 1, 0, 0, None, 1]; False
[0, None, 1, 0, 1, 0, 0]; False
[0, None, 1, 0, 1, 0, 1]; False
[0, None, 1, 0, 1, 1, 0]; False
[0, None, 1, 0, 1, 1, 1]; False
[0, None, 1, 0, 1, None, 0]; False
[0, None, 1, 0, 1, None, 1]; False
[0, None, 1, 0, None, 0, 0]; False
[0, None, 1, 0, None, 0, 1]; False
[0, None, 1, 0, None, 1, 0]; False
[0, None, 1, 0, None, 1, 1]; False
[0, None, 1, 0, None, None, 0]; False
[0, None, 1, 0, None, None, 1]; False
[0, None, 1, 1, 0, 0, 0]; False
[0, None, 1, 1, 0, 0, 1]; False
[0, None, 1, 1, 0, 1, 0]; False
[0, None, 1, 1, 0, 1, 1]; False
[0, None, 1, 1, 0, None, 0]; False
[0, None, 1, 1, 0, None, 1]; False
[0, None, 1, 1, 1, 0, 0]; False
[0, None, 1, 1, 1, 0, 1]; False
[0, None, 1, 1, 1, 1, 0]; False
[0, None, 1, 1, 1, 1, 1]; False
[0, None, 1, 1, 1, None, 0]; False
[0, None, 1, 1, 1, None, 1]; False
[0, None, 1, 1, None, 0, 0]; False
[0, None, 1, 1, None, 0, 1]; False
[0, None, 1, 1, None, 1, 0]; False
[0, None, 1, 1, None, 1, 1]; False
[0, None, 1, 1, None, None, 0]; False
[0, None, 1, 1, None, None, 1]; False
[0, None, 1, None, 0, 0, 0]; False
[0, None, 1, None, 0, 0, 1]; False
[0, None, 1, None, 0, 1, 0]; False
[0, None, 1, None, 0, 1, 1]; False
[0, None, 1, None, 0, None, 0]; False
[0, None, 1, None, 0, None, 1]; False
[0, None, 1, None, 1, 0, 0]; False
[0, None, 1, None, 1, 0, 1]; False
[0, None, 1, None, 1, 1, 0]; False
[0, None, 1, None, 1, 1, 1]; False
[0, None, 1, None, 1, None, 0]; False
[0, None, 1, None, 1, None, 1]; False
[1, 0, 0, 0, 0, 0, 0]; False
[1, 0, 0, 0, 0, 0, 1]; False
[1, 0, 0, 0, 0, 1, 0]; False
[1, 0, 0, 0, 0, 1, 1]; False
[1, 0, 0, 0, 0, None, 0]; False
[1, 0, 0, 0, 0, None, 1]; False
[1, 0, 0, 0, 1, 0, 0]; False
[1, 0, 0, 0, 1, 0, 1]; False
[1, 0, 0, 0, 1, 1, 0]; True
[1, 0, 0, 0, 1, 1, 1]; True
[1, 0, 0, 0, 1, None, 0]; True
[1, 0, 0, 0, 1, None, 1]; True
[1, 0, 0, 0, None, 0, 0]; False
[1, 0, 0, 0, None, 0, 1]; False
[1, 0, 0, 0, None, 1, 0]; True
[1, 0, 0, 0, None, 1, 1]; True
[1, 0, 0, 0, None, None, 0]; True
[1, 0, 0, 0, None, None, 1]; True
[1, 0, 0, 1, 0, 0, 0]; False
[1, 0, 0, 1, 0, 0, 1]; False
[1, 0, 0, 1, 0, 1, 0]; False
[1, 0, 0, 1, 0, 1, 1]; False
[1, 0, 0, 1, 0, None, 0]; False
[1, 0, 0, 1, 0, None, 1]; False
[1, 0, 0, 1, 1, 0, 0]; False
[1, 0, 0, 1, 1, 0, 1]; False
[1, 0, 0, 1, 1, 1, 0]; False
[1, 0, 0, 1, 1, 1, 1]; False
[1, 0, 0, 1, 1, None, 0]; False
[1, 0, 0, 1, 1, None, 1]; False
[1, 0, 0, 1, None, 0, 0]; False
[1, 0, 0, 1, None, 0, 1]; False
[1, 0, 0, 1, None, 1, 0]; False
[1, 0, 0, 1, None, 1, 1]; False
[1, 0, 0, 1, None, None, 0]; False
[1, 0, 0, 1, None, None, 1]; False
[1, 0, 0, None, 0, 0, 0]; False
[1, 0, 0, None, 0, 0, 1]; False
[1, 0, 0, None, 0, 1, 0]; False
[1, 0, 0, None, 0, 1, 1]; False
[1, 0, 0, None, 0, None, 0]; False
[1, 0, 0, None, 0, None, 1]; False
[1, 0, 0, None, 1, 0, 0]; False
[1, 0, 0, None, 1, 0, 1]; False
[1, 0, 0, None, 1, 1, 0]; False
[1, 0, 0, None, 1, 1, 1]; False
[1, 0, 0, None, 1, None, 0]; False
[1, 0, 0, None, 1, None, 1]; False
[1, 0, 0, None, None, 0, 0]; False
[1, 0, 0, None, None, 0, 1]; False
[1, 0, 0, None, None, 1, 0]; False
[1, 0, 0, None, None, 1, 1]; True
[1, 0, 0, None, None, None, 0]; False
[1, 0, 0, None, None, None, 1]; True
[1, 0, 1, 0, 0, 0, 0]; False
[1, 0, 1, 0, 0, 0, 1]; False
[1, 0, 1, 0, 0, 1, 0]; False
[1, 0, 1, 0, 0, 1, 1]; False
[1, 0, 1, 0, 0, None, 0]; False
[1, 0, 1, 0, 0, None, 1]; False
[1, 0, 1, 0, 1, 0, 0]; True
[1, 0, 1, 0, 1, 0, 1]; False
[1, 0, 1, 0, 1, 1, 0]; True
[1, 0, 1, 0, 1, 1, 1]; True
[1, 0, 1, 0, 1, None, 0]; True
[1, 0, 1, 0, 1, None, 1]; True
[1, 0, 1, 0, None, 0, 0]; True
[1, 0, 1, 0, None, 0, 1]; False
[1, 0, 1, 0, None, 1, 0]; True
[1, 0, 1, 0, None, 1, 1]; True
[1, 0, 1, 0, None, None, 0]; True
[1, 0, 1, 0, None, None, 1]; True
[1, 0, 1, 1, 0, 0, 0]; False
[1, 0, 1, 1, 0, 0, 1]; False
[1, 0, 1, 1, 0, 1, 0]; False
[1, 0, 1, 1, 0, 1, 1]; False
[1, 0, 1, 1, 0, None, 0]; False
[1, 0, 1, 1, 0, None, 1]; False
[1, 0, 1, 1, 1, 0, 0]; False
[1, 0, 1, 1, 1, 0, 1]; False
[1, 0, 1, 1, 1, 1, 0]; False
[1, 0, 1, 1, 1, 1, 1]; False
[1, 0, 1, 1, 1, None, 0]; False
[1, 0, 1, 1, 1, None, 1]; False
[1, 0, 1, 1, None, 0, 0]; False
[1, 0, 1, 1, None, 0, 1]; False
[1, 0, 1, 1, None, 1, 0]; False
[1, 0, 1, 1, None, 1, 1]; False
[1, 0, 1, 1, None, None, 0]; False
[1, 0, 1, 1, None, None, 1]; False
[1, 0, 1, None, 0, 0, 0]; False
[1, 0, 1, None, 0, 0, 1]; False
[1, 0, 1, None, 0, 1, 0]; False
[1, 0, 1, None, 0, 1, 1]; False
[1, 0, 1, None, 0, None, 0]; False
[1, 0, 1, None, 0, None, 1]; False
[1, 0, 1, None, 1, 0, 0]; False
[1, 0, 1, None, 1, 0, 1]; False
[1, 0, 1, None, 1, 1, 0]; False
[1, 0, 1, None, 1, 1, 1]; False
[1, 0, 1, None, 1, None, 0]; False
[1, 0, 1, None, 1, None, 1]; False
[1, 0, 1, None, None, 0, 0]; False
[1, 0, 1, None, None, 0, 1]; False
[1, 0, 1, None, None, 1, 0]; True
[1, 0, 1, None, None, 1, 1]; True
[1, 0, 1, None, None, None, 0]; True
[1, 0, 1, None, None, None, 1]; True
[1, 0, None, 0, 0, 0, 0]; False
[1, 0, None, 0, 0, 0, 1]; False
[1, 0, None, 0, 0, 1, 0]; False
[1, 0, None, 0, 0, 1, 1]; False
[1, 0, None, 0, 0, None, 0]; False
[1, 0, None, 0, 0, None, 1]; False
[1, 0, None, 0, 1, 0, 0]; False
[1, 0, None, 0, 1, 0, 1]; True
[1, 0, None, 0, 1, 1, 0]; False
[1, 0, None, 0, 1, 1, 1]; False
[1, 0, None, 0, 1, None, 0]; False
[1, 0, None, 0, 1, None, 1]; False
[1, 0, None, 0, None, 0, 0]; False
[1, 0, None, 0, None, 0, 1]; True
[1, 0, None, 0, None, 1, 0]; False
[1, 0, None, 0, None, 1, 1]; False
[1, 0, None, 0, None, None, 0]; False
[1, 0, None, 0, None, None, 1]; False
[1, 0, None, 1, 0, 0, 0]; False
[1, 0, None, 1, 0, 0, 1]; False
[1, 0, None, 1, 0, 1, 0]; False
[1, 0, None, 1, 0, 1, 1]; False
[1, 0, None, 1, 0, None, 0]; False
[1, 0, None, 1, 0, None, 1]; False
[1, 0, None, 1, 1, 0, 0]; False
[1, 0, None, 1, 1, 0, 1]; True
[1, 0, None, 1, 1, 1, 0]; False
[1, 0, None, 1, 1, 1, 1]; False
[1, 0, None, 1, 1, None, 0]; False
[1, 0, None, 1, 1, None, 1]; False
[1, 0, None, 1, None, 0, 0]; False
[1, 0, None, 1, None, 0, 1]; True
[1, 0, None, 1, None, 1, 0]; False
[1, 0, None, 1, None, 1, 1]; False
[1, 0, None, 1, None, None, 0]; False
[1, 0, None, 1, None, None, 1]; False
[1, 0, None, None, 0, 0, 0]; False
[1, 0, None, None, 0, 0, 1]; False
[1, 0, None, None, 0, 1, 0]; False
[1, 0, None, None, 0, 1, 1]; False
[1, 0, None, None, 0, None, 0]; False
[1, 0, None, None, 0, None, 1]; False
[1, 0, None, None, 1, 0, 0]; False
[1, 0, None, None, 1, 0, 1]; False
[1, 0, None, None, 1, 1, 0]; False
[1, 0, None, None, 1, 1, 1]; False
[1, 0, None, None, 1, None, 0]; False
[1, 0, None, None, 1, None, 1]; False
[1, 1, 0, 0, 0, 0, 0]; False
[1, 1, 0, 0, 0, 0, 1]; False
[1, 1, 0, 0, 0, 1, 0]; False
[1, 1, 0, 0, 0, 1, 1]; False
[1, 1, 0, 0, 0, None, 0]; False
[1, 1, 0, 0, 0, None, 1]; False
[1, 1, 0, 0, 1, 0, 0]; False
[1, 1, 0, 0, 1, 0, 1]; False
[1, 1, 0, 0, 1, 1, 0]; False
[1, 1, 0, 0, 1, 1, 1]; True
[1, 1, 0, 0, 1, None, 0]; False
[1, 1, 0, 0, 1, None, 1]; True
[1, 1, 0, 0, None, 0, 0]; False
[1, 1, 0, 0, None, 0, 1]; False
[1, 1, 0, 0, None, 1, 0]; False
[1, 1, 0, 0, None, 1, 1]; True
[1, 1, 0, 0, None, None, 0]; False
[1, 1, 0, 0, None, None, 1]; True
[1, 1, 0, 1, 0, 0, 0]; False
[1, 1, 0, 1, 0, 0, 1]; False
[1, 1, 0, 1, 0, 1, 0]; False
[1, 1, 0, 1, 0, 1, 1]; False
[1, 1, 0, 1, 0, None, 0]; False
[1, 1, 0, 1, 0, None, 1]; False
[1, 1, 0, 1, 1, 0, 0]; False
[1, 1, 0, 1, 1, 0, 1]; False
[1, 1, 0, 1, 1, 1, 0]; False
[1, 1, 0, 1, 1, 1, 1]; False
[1, 1, 0, 1, 1, None, 0]; False
[1, 1, 0, 1, 1, None, 1]; False
[1, 1, 0, 1, None, 0, 0]; False
[1, 1, 0, 1, None, 0, 1]; False
[1, 1, 0, 1, None, 1, 0]; False
[1, 1, 0, 1, None, 1, 1]; False
[1, 1, 0, 1, None, None, 0]; False
[1, 1, 0, 1, None, None, 1]; False
[1, 1, 0, None, 0, 0, 0]; False
[1, 1, 0, None, 0, 0, 1]; False
[1, 1, 0, None, 0, 1, 0]; False
[1, 1, 0, None, 0, 1, 1]; False
[1, 1, 0, None, 0, None, 0]; False
[1, 1, 0, None, 0, None, 1]; False
[1, 1, 0, None, 1, 0, 0]; False
[1, 1, 0, None, 1, 0, 1]; False
[1, 1, 0, None, 1, 1, 0]; False
[1, 1, 0, None, 1, 1, 1]; False
[1, 1, 0, None, 1, None, 0]; False
[1, 1, 0, None, 1, None, 1]; False
[1, 1, 0, None, None, 0, 0]; False
[1, 1, 0, None, None, 0, 1]; False
[1, 1, 0, None, None, 1, 0]; False
[1, 1, 0, None, None, 1, 1]; False
[1, 1, 0, None, None, None, 0]; False
[1, 1, 0, None, None, None, 1]; False
[1, 1, 1, 0, 0, 0, 0]; False
[1, 1, 1, 0, 0, 0, 1]; False
[1, 1, 1, 0, 0, 1, 0]; False
[1, 1, 1, 0, 0, 1, 1]; False
[1, 1, 1, 0, 0, None, 0]; False
[1, 1, 1, 0, 0, None, 1]; False
[1, 1, 1, 0, 1, 0, 0]; False
[1, 1, 1, 0, 1, 0, 1]; False
[1, 1, 1, 0, 1, 1, 0]; True
[1, 1, 1, 0, 1, 1, 1]; True
[1, 1, 1, 0, 1, None, 0]; True
[1, 1, 1, 0, 1, None, 1]; True
[1, 1, 1, 0, None, 0, 0]; False
[1, 1, 1, 0, None, 0, 1]; False
[1, 1, 1, 0, None, 1, 0]; True
[1, 1, 1, 0, None, 1, 1]; True
[1, 1, 1, 0, None, None, 0]; True
[1, 1, 1, 0, None, None, 1]; True
[1, 1, 1, 1, 0, 0, 0]; False
[1, 1, 1, 1, 0, 0, 1]; False
[1, 1, 1, 1, 0, 1, 0]; False
[1, 1, 1, 1, 0, 1, 1]; False
[1, 1, 1, 1, 0, None, 0]; False
[1, 1, 1, 1, 0, None, 1]; False
[1, 1, 1, 1, 1, 0, 0]; False
[1, 1, 1, 1, 1, 0, 1]; False
[1, 1, 1, 1, 1, 1, 0]; False
[1, 1, 1, 1, 1, 1, 1]; False
[1, 1, 1, 1, 1, None, 0]; False
[1, 1, 1, 1, 1, None, 1]; False
[1, 1, 1, 1, None, 0, 0]; False
[1, 1, 1, 1, None, 0, 1]; False
[1, 1, 1, 1, None, 1, 0]; False
[1, 1, 1, 1, None, 1, 1]; False
[1, 1, 1, 1, None, None, 0]; False
[1, 1, 1, 1, None, None, 1]; False
[1, 1, 1, None, 0, 0, 0]; False
[1, 1, 1, None, 0, 0, 1]; False
[1, 1, 1, None, 0, 1, 0]; False
[1, 1, 1, None, 0, 1, 1]; False
[1, 1, 1, None, 0, None, 0]; False
[1, 1, 1, None, 0, None, 1]; False
[1, 1, 1, None, 1, 0, 0]; False
[1, 1, 1, None, 1, 0, 1]; False
[1, 1, 1, None, 1, 1, 0]; False
[1, 1, 1, None, 1, 1, 1]; False
[1, 1, 1, None, 1, None, 0]; False
[1, 1, 1, None, 1, None, 1]; False
[1, 1, 1, None, None, 0, 0]; False
[1, 1, 1, None, None, 0, 1]; False
[1, 1, 1, None, None, 1, 0]; False
[1, 1, 1, None, None, 1, 1]; False
[1, 1, 1, None, None, None, 0]; False
[1, 1, 1, None, None, None, 1]; False
[1, 1, None, 0, 0, 0, 0]; False
[1, 1, None, 0, 0, 0, 1]; False
[1, 1, None, 0, 0, 1, 0]; False
[1, 1, None, 0, 0, 1, 1]; False
[1, 1, None, 0, 0, None, 0]; False
[1, 1, None, 0, 0, None, 1]; False
[1, 1, None, 0, 1, 0, 0]; False
[1, 1, None, 0, 1, 0, 1]; True
[1, 1, None, 0, 1, 1, 0]; False
[1, 1, None, 0, 1, 1, 1]; False
[1, 1, None, 0, 1, None, 0]; False
[1, 1, None, 0, 1, None, 1]; False
[1, 1, None, 0, None, 0, 0]; False
[1, 1, None, 0, None, 0, 1]; True
[1, 1, None, 0, None, 1, 0]; False
[1, 1, None, 0, None, 1, 1]; False
[1, 1, None, 0, None, None, 0]; False
[1, 1, None, 0, None, None, 1]; False
[1, 1, None, 1, 0, 0, 0]; False
[1, 1, None, 1, 0, 0, 1]; False
[1, 1, None, 1, 0, 1, 0]; False
[1, 1, None, 1, 0, 1, 1]; False
[1, 1, None, 1, 0, None, 0]; False
[1, 1, None, 1, 0, None, 1]; False
[1, 1, None, 1, 1, 0, 0]; False
[1, 1, None, 1, 1, 0, 1]; True
[1, 1, None, 1, 1, 1, 0]; False
[1, 1, None, 1, 1, 1, 1]; False
[1, 1, None, 1, 1, None, 0]; False
[1, 1, None, 1, 1, None, 1]; False
[1, 1, None, 1, None, 0, 0]; False
[1, 1, None, 1, None, 0, 1]; True
[1, 1, None, 1, None, 1, 0]; False
[1, 1, None, 1, None, 1, 1]; False
[1, 1, None, 1, None, None, 0]; False
[1, 1, None, 1, None, None, 1]; False
[1, 1, None, None, 0, 0, 0]; False
[1, 1, None, None, 0, 0, 1]; False
[1, 1, None, None, 0, 1, 0]; False
[1, 1, None, None, 0, 1, 1]; False
[1, 1, None, None, 0, None, 0]; False
[1, 1, None, None, 0, None, 1]; False
[1, 1, None, None, 1, 0, 0]; False
[1, 1, None, None, 1, 0, 1]; False
[1, 1, None, None, 1, 1, 0]; False
[1, 1, None, None, 1, 1, 1]; False
[1, 1, None, None, 1, None, 0]; False
[1, 1, None, None, 1, None, 1]; False
[1, None, 0, 0, 0, 0, 0]; False
[1, None, 0, 0, 0, 0, 1]; False
[1, None, 0, 0, 0, 1, 0]; False
[1, None, 0, 0, 0, 1, 1]; False
[1, None, 0, 0, 0, None, 0]; False
[1, None, 0, 0, 0, None, 1]; False
[1, None, 0, 0, 1, 0, 0]; False
[1, None, 0, 0, 1, 0, 1]; False
[1, None, 0, 0, 1, 1, 0]; False
[1, None, 0, 0, 1, 1, 1]; False
[1, None, 0, 0, 1, None, 0]; False
[1, None, 0, 0, 1, None, 1]; False
[1, None, 0, 0, None, 0, 0]; False
[1, None, 0, 0, None, 0, 1]; False
[1, None, 0, 0, None, 1, 0]; False
[1, None, 0, 0, None, 1, 1]; False
[1, None, 0, 0, None, None, 0]; False
[1, None, 0, 0, None, None, 1]; False
[1, None, 0, 1, 0, 0, 0]; False
[1, None, 0, 1, 0, 0, 1]; False
[1, None, 0, 1, 0, 1, 0]; False
[1, None, 0, 1, 0, 1, 1]; False
[1, None, 0, 1, 0, None, 0]; False
[1, None, 0, 1, 0, None, 1]; False
[1, None, 0, 1, 1, 0, 0]; False
[1, None, 0, 1, 1, 0, 1]; False
[1, None, 0, 1, 1, 1, 0]; False
[1, None, 0, 1, 1, 1, 1]; False
[1, None, 0, 1, 1, None, 0]; False
[1, None, 0, 1, 1, None, 1]; False
[1, None, 0, 1, None, 0, 0]; False
[1, None, 0, 1, None, 0, 1]; False
[1, None, 0, 1, None, 1, 0]; False
[1, None, 0, 1, None, 1, 1]; False
[1, None, 0, 1, None, None, 0]; False
[1, None, 0, 1, None, None, 1]; False
[1, None, 0, None, 0, 0, 0]; False
[1, None, 0, None, 0, 0, 1]; False
[1, None, 0, None, 0, 1, 0]; False
[1, None, 0, None, 0, 1, 1]; False
[1, None, 0, None, 0, None, 0]; False
[1, None, 0, None, 0, None, 1]; False
[1, None, 0, None, 1, 0, 0]; False
[1, None, 0, None, 1, 0, 1]; False
[1, None, 0, None, 1, 1, 0]; False
[1, None, 0, None, 1, 1, 1]; False
[1, None, 0, None, 1, None, 0]; False
[1, None, 0, None, 1, None, 1]; False
[1, None, 1, 0, 0, 0, 0]; False
[1, None, 1, 0, 0, 0, 1]; False
[1, None, 1, 0, 0, 1, 0]; False
[1, None, 1, 0, 0, 1, 1]; False
[1, None, 1, 0, 0, None, 0]; False
[1, None, 1, 0, 0, None, 1]; False
[1, None, 1, 0, 1, 0, 0]; False
[1, None, 1, 0, 1, 0, 1]; False
[1, None, 1, 0, 1, 1, 0]; False
[1, None, 1, 0, 1, 1, 1]; False
[1, None, 1, 0, 1, None, 0]; False
[1, None, 1, 0, 1, None, 1]; False
[1, None, 1, 0, None, 0, 0]; False
[1, None, 1, 0, None, 0, 1]; False
[1, None, 1, 0, None, 1, 0]; False
[1, None, 1, 0, None, 1, 1]; False
[1, None, 1, 0, None, None, 0]; False
[1, None, 1, 0, None, None, 1]; False
[1, None, 1, 1, 0, 0, 0]; False
[1, None, 1, 1, 0, 0, 1]; False
[1, None, 1, 1, 0, 1, 0]; False
[1, None, 1, 1, 0, 1, 1]; False
[1, None, 1, 1, 0, None, 0]; False
[1, None, 1, 1, 0, None, 1]; False
[1, None, 1, 1, 1, 0, 0]; False
[1, None, 1, 1, 1, 0, 1]; False
[1, None, 1, 1, 1, 1, 0]; False
[1, None, 1, 1, 1, 1, 1]; False
[1, None, 1, 1, 1, None, 0]; False
[1, None, 1, 1, 1, None, 1]; False
[1, None, 1, 1, None, 0, 0]; False
[1, None, 1, 1, None, 0, 1]; False
[1, None, 1, 1, None, 1, 0]; False
[1, None, 1, 1, None, 1, 1]; False
[1, None, 1, 1, None, None, 0]; False
[1, None, 1, 1, None, None, 1]; False
[1, None, 1, None, 0, 0, 0]; False
[1, None, 1, None, 0, 0, 1]; False
[1, None, 1, None, 0, 1, 0]; False
[1, None, 1, None, 0, 1, 1]; False
[1, None, 1, None, 0, None, 0]; False
[1, None, 1, None, 0, None, 1]; False
[1, None, 1, None, 1, 0, 0]; False
[1, None, 1, None, 1, 0, 1]; False
[1, None, 1, None, 1, 1, 0]; False
[1, None, 1, None, 1, 1, 1]; False
[1, None, 1, None, 1, None, 0]; False
[1, None, 1, None, 1, None, 1]; False
[0, 0, 0, 0, 0, 0, 0, 0]; False
[0, 0, 0, 0, 0, 0, 0, 1]; False
[0, 0, 0, 0, 0, 0, 1, 0]; False
[0, 0, 0, 0, 0, 0, 1, 1]; False
[0, 0, 0, 0, 0, 0, None, 0]; False
[0, 0, 0, 0, 0, 0, None, 1]; False
[0, 0, 0, 0, 0, 1, 0, 0]; False
[0, 0, 0, 0, 0, 1, 0, 1]; False
[0, 0, 0, 0, 0, 1, 1, 0]; False
[0, 0, 0, 0, 0, 1, 1, 1]; False
[0, 0, 0, 0, 0, 1, None, 0]; False
[0, 0, 0, 0, 0, 1, None, 1]; False
[0, 0, 0, 0, 0, None, 0, 0]; False
[0, 0, 0, 0, 0, None, 0, 1]; False
[0, 0, 0, 0, 0, None, 1, 0]; False
[0, 0, 0, 0, 0, None, 1, 1]; False
[0, 0, 0, 0, 0, None, None, 0]; False
[0, 0, 0, 0, 0, None, None, 1]; False
[0, 0, 0, 0, 1, 0, 0, 0]; True
[0, 0, 0, 0, 1, 0, 0, 1]; False
[0, 0, 0, 0, 1, 0, 1, 0]; False
[0, 0, 0, 0, 1, 0, 1, 1]; False
[0, 0, 0, 0, 1, 0, None, 0]; False
[0, 0, 0, 0, 1, 0, None, 1]; False
[0, 0, 0, 0, 1, 1, 0, 0]; True
[0, 0, 0, 0, 1, 1, 0, 1]; False
[0, 0, 0, 0, 1, 1, 1, 0]; True
[0, 0, 0, 0, 1, 1, 1, 1]; False
[0, 0, 0, 0, 1, 1, None, 0]; True
[0, 0, 0, 0, 1, 1, None, 1]; False
[0, 0, 0, 0, 1, None, 0, 0]; True
[0, 0, 0, 0, 1, None, 0, 1]; False
[0, 0, 0, 0, 1, None, 1, 0]; True
[0, 0, 0, 0, 1, None, 1, 1]; False
[0, 0, 0, 0, 1, None, None, 0]; False
[0, 0, 0, 0, 1, None, None, 1]; False
[0, 0, 0, 0, None, 0, 0, 0]; True
[0, 0, 0, 0, None, 0, 0, 1]; False
[0, 0, 0, 0, None, 0, 1, 0]; False
[0, 0, 0, 0, None, 0, 1, 1]; False
[0, 0, 0, 0, None, 0, None, 0]; False
[0, 0, 0, 0, None, 0, None, 1]; False
[0, 0, 0, 0, None, 1, 0, 0]; True
[0, 0, 0, 0, None, 1, 0, 1]; False
[0, 0, 0, 0, None, 1, 1, 0]; True
[0, 0, 0, 0, None, 1, 1, 1]; False
[0, 0, 0, 0, None, 1, None, 0]; True
[0, 0, 0, 0, None, 1, None, 1]; False
[0, 0, 0, 0, None, None, 0, 0]; True
[0, 0, 0, 0, None, None, 0, 1]; False
[0, 0, 0, 0, None, None, 1, 0]; True
[0, 0, 0, 0, None, None, 1, 1]; False
[0, 0, 0, 0, None, None, None, 0]; False
[0, 0, 0, 0, None, None, None, 1]; False
[0, 0, 0, 1, 0, 0, 0, 0]; False
[0, 0, 0, 1, 0, 0, 0, 1]; False
[0, 0, 0, 1, 0, 0, 1, 0]; False
[0, 0, 0, 1, 0, 0, 1, 1]; False
[0, 0, 0, 1, 0, 0, None, 0]; False
[0, 0, 0, 1, 0, 0, None, 1]; False
[0, 0, 0, 1, 0, 1, 0, 0]; False
[0, 0, 0, 1, 0, 1, 0, 1]; False
[0, 0, 0, 1, 0, 1, 1, 0]; False
[0, 0, 0, 1, 0, 1, 1, 1]; False
[0, 0, 0, 1, 0, 1, None, 0]; False
[0, 0, 0, 1, 0, 1, None, 1]; False
[0, 0, 0, 1, 0, None, 0, 0]; False
[0, 0, 0, 1, 0, None, 0, 1]; False
[0, 0, 0, 1, 0, None, 1, 0]; False
[0, 0, 0, 1, 0, None, 1, 1]; False
[0, 0, 0, 1, 0, None, None, 0]; False
[0, 0, 0, 1, 0, None, None, 1]; False
[0, 0, 0, 1, 1, 0, 0, 0]; False
[0, 0, 0, 1, 1, 0, 0, 1]; False
[0, 0, 0, 1, 1, 0, 1, 0]; False
[0, 0, 0, 1, 1, 0, 1, 1]; False
[0, 0, 0, 1, 1, 0, None, 0]; False
[0, 0, 0, 1, 1, 0, None, 1]; False
[0, 0, 0, 1, 1, 1, 0, 0]; True
[0, 0, 0, 1, 1, 1, 0, 1]; False
[0, 0, 0, 1, 1, 1, 1, 0]; True
[0, 0, 0, 1, 1, 1, 1, 1]; False
[0, 0, 0, 1, 1, 1, None, 0]; True
[0, 0, 0, 1, 1, 1, None, 1]; False
[0, 0, 0, 1, 1, None, 0, 0]; True
[0, 0, 0, 1, 1, None, 0, 1]; False
[0, 0, 0, 1, 1, None, 1, 0]; True
[0, 0, 0, 1, 1, None, 1, 1]; False
[0, 0, 0, 1, 1, None, None, 0]; False
[0, 0, 0, 1, 1, None, None, 1]; False
[0, 0, 0, 1, None, 0, 0, 0]; False
[0, 0, 0, 1, None, 0, 0, 1]; False
[0, 0, 0, 1, None, 0, 1, 0]; False
[0, 0, 0, 1, None, 0, 1, 1]; False
[0, 0, 0, 1, None, 0, None, 0]; False
[0, 0, 0, 1, None, 0, None, 1]; False
[0, 0, 0, 1, None, 1, 0, 0]; True
[0, 0, 0, 1, None, 1, 0, 1]; False
[0, 0, 0, 1, None, 1, 1, 0]; True
[0, 0, 0, 1, None, 1, 1, 1]; False
[0, 0, 0, 1, None, 1, None, 0]; True
[0, 0, 0, 1, None, 1, None, 1]; False
[0, 0, 0, 1, None, None, 0, 0]; True
[0, 0, 0, 1, None, None, 0, 1]; False
[0, 0, 0, 1, None, None, 1, 0]; True
[0, 0, 0, 1, None, None, 1, 1]; False
[0, 0, 0, 1, None, None, None, 0]; False
[0, 0, 0, 1, None, None, None, 1]; False
[0, 0, 0, None, 0, 0, 0, 0]; False
[0, 0, 0, None, 0, 0, 0, 1]; False
[0, 0, 0, None, 0, 0, 1, 0]; False
[0, 0, 0, None, 0, 0, 1, 1]; False
[0, 0, 0, None, 0, 0, None, 0]; False
[0, 0, 0, None, 0, 0, None, 1]; False
[0, 0, 0, None, 0, 1, 0, 0]; False
[0, 0, 0, None, 0, 1, 0, 1]; False
[0, 0, 0, None, 0, 1, 1, 0]; False
[0, 0, 0, None, 0, 1, 1, 1]; False
[0, 0, 0, None, 0, 1, None, 0]; False
[0, 0, 0, None, 0, 1, None, 1]; False
[0, 0, 0, None, 0, None, 0, 0]; False
[0, 0, 0, None, 0, None, 0, 1]; False
[0, 0, 0, None, 0, None, 1, 0]; False
[0, 0, 0, None, 0, None, 1, 1]; False
[0, 0, 0, None, 0, None, None, 0]; False
[0, 0, 0, None, 0, None, None, 1]; False
[0, 0, 0, None, 1, 0, 0, 0]; False
[0, 0, 0, None, 1, 0, 0, 1]; False
[0, 0, 0, None, 1, 0, 1, 0]; False
[0, 0, 0, None, 1, 0, 1, 1]; False
[0, 0, 0, None, 1, 0, None, 0]; False
[0, 0, 0, None, 1, 0, None, 1]; False
[0, 0, 0, None, 1, 1, 0, 0]; False
[0, 0, 0, None, 1, 1, 0, 1]; False
[0, 0, 0, None, 1, 1, 1, 0]; False
[0, 0, 0, None, 1, 1, 1, 1]; False
[0, 0, 0, None, 1, 1, None, 0]; False
[0, 0, 0, None, 1, 1, None, 1]; False
[0, 0, 0, None, 1, None, 0, 0]; False
[0, 0, 0, None, 1, None, 0, 1]; False
[0, 0, 0, None, 1, None, 1, 0]; False
[0, 0, 0, None, 1, None, 1, 1]; False
[0, 0, 0, None, 1, None, None, 0]; False
[0, 0, 0, None, 1, None, None, 1]; False
[0, 0, 0, None, None, 0, 0, 0]; False
[0, 0, 0, None, None, 0, 0, 1]; False
[0, 0, 0, None, None, 0, 1, 0]; False
[0, 0, 0, None, None, 0, 1, 1]; False
[0, 0, 0, None, None, 0, None, 0]; False
[0, 0, 0, None, None, 0, None, 1]; False
[0, 0, 0, None, None, 1, 0, 0]; False
[0, 0, 0, None, None, 1, 0, 1]; False
[0, 0, 0, None, None, 1, 1, 0]; False
[0, 0, 0, None, None, 1, 1, 1]; True
[0, 0, 0, None, None, 1, None, 0]; False
[0, 0, 0, None, None, 1, None, 1]; True
[0, 0, 0, None, None, None, 0, 0]; False
[0, 0, 0, None, None, None, 0, 1]; False
[0, 0, 0, None, None, None, 1, 0]; False
[0, 0, 0, None, None, None, 1, 1]; True
[0, 0, 1, 0, 0, 0, 0, 0]; False
[0, 0, 1, 0, 0, 0, 0, 1]; False
[0, 0, 1, 0, 0, 0, 1, 0]; False
[0, 0, 1, 0, 0, 0, 1, 1]; False
[0, 0, 1, 0, 0, 0, None, 0]; False
[0, 0, 1, 0, 0, 0, None, 1]; False
[0, 0, 1, 0, 0, 1, 0, 0]; False
[0, 0, 1, 0, 0, 1, 0, 1]; False
[0, 0, 1, 0, 0, 1, 1, 0]; False
[0, 0, 1, 0, 0, 1, 1, 1]; False
[0, 0, 1, 0, 0, 1, None, 0]; False
[0, 0, 1, 0, 0, 1, None, 1]; False
[0, 0, 1, 0, 0, None, 0, 0]; False
[0, 0, 1, 0, 0, None, 0, 1]; False
[0, 0, 1, 0, 0, None, 1, 0]; False
[0, 0, 1, 0, 0, None, 1, 1]; False
[0, 0, 1, 0, 0, None, None, 0]; False
[0, 0, 1, 0, 0, None, None, 1]; False
[0, 0, 1, 0, 1, 0, 0, 0]; True
[0, 0, 1, 0, 1, 0, 0, 1]; False
[0, 0, 1, 0, 1, 0, 1, 0]; False
[0, 0, 1, 0, 1, 0, 1, 1]; False
[0, 0, 1, 0, 1, 0, None, 0]; False
[0, 0, 1, 0, 1, 0, None, 1]; False
[0, 0, 1, 0, 1, 1, 0, 0]; True
[0, 0, 1, 0, 1, 1, 0, 1]; False
[0, 0, 1, 0, 1, 1, 1, 0]; True
[0, 0, 1, 0, 1, 1, 1, 1]; False
[0, 0, 1, 0, 1, 1, None, 0]; True
[0, 0, 1, 0, 1, 1, None, 1]; False
[0, 0, 1, 0, 1, None, 0, 0]; True
[0, 0, 1, 0, 1, None, 0, 1]; False
[0, 0, 1, 0, 1, None, 1, 0]; True
[0, 0, 1, 0, 1, None, 1, 1]; False
[0, 0, 1, 0, 1, None, None, 0]; True
[0, 0, 1, 0, 1, None, None, 1]; False
[0, 0, 1, 0, None, 0, 0, 0]; True
[0, 0, 1, 0, None, 0, 0, 1]; False
[0, 0, 1, 0, None, 0, 1, 0]; False
[0, 0, 1, 0, None, 0, 1, 1]; False
[0, 0, 1, 0, None, 0, None, 0]; False
[0, 0, 1, 0, None, 0, None, 1]; False
[0, 0, 1, 0, None, 1, 0, 0]; True
[0, 0, 1, 0, None, 1, 0, 1]; False
[0, 0, 1, 0, None, 1, 1, 0]; True
[0, 0, 1, 0, None, 1, 1, 1]; False
[0, 0, 1, 0, None, 1, None, 0]; True
[0, 0, 1, 0, None, 1, None, 1]; False
[0, 0, 1, 0, None, None, 0, 0]; True
[0, 0, 1, 0, None, None, 0, 1]; False
[0, 0, 1, 0, None, None, 1, 0]; True
[0, 0, 1, 0, None, None, 1, 1]; False
[0, 0, 1, 0, None, None, None, 0]; True
[0, 0, 1, 0, None, None, None, 1]; False
[0, 0, 1, 1, 0, 0, 0, 0]; False
[0, 0, 1, 1, 0, 0, 0, 1]; False
[0, 0, 1, 1, 0, 0, 1, 0]; False
[0, 0, 1, 1, 0, 0, 1, 1]; False
[0, 0, 1, 1, 0, 0, None, 0]; False
[0, 0, 1, 1, 0, 0, None, 1]; False
[0, 0, 1, 1, 0, 1, 0, 0]; False
[0, 0, 1, 1, 0, 1, 0, 1]; False
[0, 0, 1, 1, 0, 1, 1, 0]; False
[0, 0, 1, 1, 0, 1, 1, 1]; False
[0, 0, 1, 1, 0, 1, None, 0]; False
[0, 0, 1, 1, 0, 1, None, 1]; False
[0, 0, 1, 1, 0, None, 0, 0]; False
[0, 0, 1, 1, 0, None, 0, 1]; False
[0, 0, 1, 1, 0, None, 1, 0]; False
[0, 0, 1, 1, 0, None, 1, 1]; False
[0, 0, 1, 1, 0, None, None, 0]; False
[0, 0, 1, 1, 0, None, None, 1]; False
[0, 0, 1, 1, 1, 0, 0, 0]; True
[0, 0, 1, 1, 1, 0, 0, 1]; False
[0, 0, 1, 1, 1, 0, 1, 0]; False
[0, 0, 1, 1, 1, 0, 1, 1]; False
[0, 0, 1, 1, 1, 0, None, 0]; False
[0, 0, 1, 1, 1, 0, None, 1]; False
[0, 0, 1, 1, 1, 1, 0, 0]; True
[0, 0, 1, 1, 1, 1, 0, 1]; False
[0, 0, 1, 1, 1, 1, 1, 0]; True
[0, 0, 1, 1, 1, 1, 1, 1]; False
[0, 0, 1, 1, 1, 1, None, 0]; True
[0, 0, 1, 1, 1, 1, None, 1]; False
[0, 0, 1, 1, 1, None, 0, 0]; True
[0, 0, 1, 1, 1, None, 0, 1]; False
[0, 0, 1, 1, 1, None, 1, 0]; True
[0, 0, 1, 1, 1, None, 1, 1]; False
[0, 0, 1, 1, 1, None, None, 0]; True
[0, 0, 1, 1, 1, None, None, 1]; False
[0, 0, 1, 1, None, 0, 0, 0]; True
[0, 0, 1, 1, None, 0, 0, 1]; False
[0, 0, 1, 1, None, 0, 1, 0]; False
[0, 0, 1, 1, None, 0, 1, 1]; False
[0, 0, 1, 1, None, 0, None, 0]; False
[0, 0, 1, 1, None, 0, None, 1]; False
[0, 0, 1, 1, None, 1, 0, 0]; True
[0, 0, 1, 1, None, 1, 0, 1]; False
[0, 0, 1, 1, None, 1, 1, 0]; True
[0, 0, 1, 1, None, 1, 1, 1]; False
[0, 0, 1, 1, None, 1, None, 0]; True
[0, 0, 1, 1, None, 1, None, 1]; False
[0, 0, 1, 1, None, None, 0, 0]; True
[0, 0, 1, 1, None, None, 0, 1]; False
[0, 0, 1, 1, None, None, 1, 0]; True
[0, 0, 1, 1, None, None, 1, 1]; False
[0, 0, 1, 1, None, None, None, 0]; True
[0, 0, 1, 1, None, None, None, 1]; False
[0, 0, 1, None, 0, 0, 0, 0]; False
[0, 0, 1, None, 0, 0, 0, 1]; False
[0, 0, 1, None, 0, 0, 1, 0]; False
[0, 0, 1, None, 0, 0, 1, 1]; False
[0, 0, 1, None, 0, 0, None, 0]; False
[0, 0, 1, None, 0, 0, None, 1]; False
[0, 0, 1, None, 0, 1, 0, 0]; False
[0, 0, 1, None, 0, 1, 0, 1]; False
[0, 0, 1, None, 0, 1, 1, 0]; False
[0, 0, 1, None, 0, 1, 1, 1]; False
[0, 0, 1, None, 0, 1, None, 0]; False
[0, 0, 1, None, 0, 1, None, 1]; False
[0, 0, 1, None, 0, None, 0, 0]; False
[0, 0, 1, None, 0, None, 0, 1]; False
[0, 0, 1, None, 0, None, 1, 0]; False
[0, 0, 1, None, 0, None, 1, 1]; False
[0, 0, 1, None, 0, None, None, 0]; False
[0, 0, 1, None, 0, None, None, 1]; False
[0, 0, 1, None, 1, 0, 0, 0]; False
[0, 0, 1, None, 1, 0, 0, 1]; False
[0, 0, 1, None, 1, 0, 1, 0]; False
[0, 0, 1, None, 1, 0, 1, 1]; False
[0, 0, 1, None, 1, 0, None, 0]; False
[0, 0, 1, None, 1, 0, None, 1]; False
[0, 0, 1, None, 1, 1, 0, 0]; False
[0, 0, 1, None, 1, 1, 0, 1]; False
[0, 0, 1, None, 1, 1, 1, 0]; False
[0, 0, 1, None, 1, 1, 1, 1]; False
[0, 0, 1, None, 1, 1, None, 0]; False
[0, 0, 1, None, 1, 1, None, 1]; False
[0, 0, 1, None, 1, None, 0, 0]; False
[0, 0, 1, None, 1, None, 0, 1]; False
[0, 0, 1, None, 1, None, 1, 0]; False
[0, 0, 1, None, 1, None, 1, 1]; False
[0, 0, 1, None, 1, None, None, 0]; False
[0, 0, 1, None, 1, None, None, 1]; False
[0, 0, 1, None, None, 0, 0, 0]; False
[0, 0, 1, None, None, 0, 0, 1]; False
[0, 0, 1, None, None, 0, 1, 0]; False
[0, 0, 1, None, None, 0, 1, 1]; True
[0, 0, 1, None, None, 0, None, 0]; False
[0, 0, 1, None, None, 0, None, 1]; True
[0, 0, 1, None, None, 1, 0, 0]; False
[0, 0, 1, None, None, 1, 0, 1]; True
[0, 0, 1, None, None, 1, 1, 0]; False
[0, 0, 1, None, None, 1, 1, 1]; True
[0, 0, 1, None, None, 1, None, 0]; False
[0, 0, 1, None, None, 1, None, 1]; True
[0, 0, 1, None, None, None, 0, 0]; False
[0, 0, 1, None, None, None, 0, 1]; True
[0, 0, 1, None, None, None, 1, 0]; True
[0, 0, 1, None, None, None, 1, 1]; True
[0, 0, None, 0, 0, 0, 0, 0]; False
[0, 0, None, 0, 0, 0, 0, 1]; False
[0, 0, None, 0, 0, 0, 1, 0]; False
[0, 0, None, 0, 0, 0, 1, 1]; True
[0, 0, None, 0, 0, 0, None, 0]; False
[0, 0, None, 0, 0, 0, None, 1]; True
[0, 0, None, 0, 0, 1, 0, 0]; False
[0, 0, None, 0, 0, 1, 0, 1]; False
[0, 0, None, 0, 0, 1, 1, 0]; False
[0, 0, None, 0, 0, 1, 1, 1]; False
[0, 0, None, 0, 0, 1, None, 0]; False
[0, 0, None, 0, 0, 1, None, 1]; False
[0, 0, None, 0, 0, None, 0, 0]; False
[0, 0, None, 0, 0, None, 0, 1]; False
[0, 0, None, 0, 0, None, 1, 0]; False
[0, 0, None, 0, 0, None, 1, 1]; False
[0, 0, None, 0, 0, None, None, 0]; False
[0, 0, None, 0, 0, None, None, 1]; True
[0, 0, None, 0, 1, 0, 0, 0]; False
[0, 0, None, 0, 1, 0, 0, 1]; False
[0, 0, None, 0, 1, 0, 1, 0]; False
[0, 0, None, 0, 1, 0, 1, 1]; True
[0, 0, None, 0, 1, 0, None, 0]; False
[0, 0, None, 0, 1, 0, None, 1]; True
[0, 0, None, 0, 1, 1, 0, 0]; False
[0, 0, None, 0, 1, 1, 0, 1]; False
[0, 0, None, 0, 1, 1, 1, 0]; False
[0, 0, None, 0, 1, 1, 1, 1]; False
[0, 0, None, 0, 1, 1, None, 0]; False
[0, 0, None, 0, 1, 1, None, 1]; False
[0, 0, None, 0, 1, None, 0, 0]; False
[0, 0, None, 0, 1, None, 0, 1]; False
[0, 0, None, 0, 1, None, 1, 0]; False
[0, 0, None, 0, 1, None, 1, 1]; False
[0, 0, None, 0, 1, None, None, 0]; False
[0, 0, None, 0, 1, None, None, 1]; True
[0, 0, None, 0, None, 0, 0, 0]; False
[0, 0, None, 0, None, 0, 0, 1]; False
[0, 0, None, 0, None, 0, 1, 0]; True
[0, 0, None, 0, None, 0, 1, 1]; False
[0, 0, None, 0, None, 0, None, 0]; True
[0, 0, None, 0, None, 0, None, 1]; False
[0, 0, None, 0, None, 1, 0, 0]; False
[0, 0, None, 0, None, 1, 0, 1]; False
[0, 0, None, 0, None, 1, 1, 0]; True
[0, 0, None, 0, None, 1, 1, 1]; False
[0, 0, None, 0, None, 1, None, 0]; True
[0, 0, None, 0, None, 1, None, 1]; False
[0, 0, None, 0, None, None, 0, 0]; False
[0, 0, None, 0, None, None, 0, 1]; False
[0, 0, None, 0, None, None, 1, 0]; False
[0, 0, None, 0, None, None, 1, 1]; False
[0, 0, None, 1, 0, 0, 0, 0]; False
[0, 0, None, 1, 0, 0, 0, 1]; False
[0, 0, None, 1, 0, 0, 1, 0]; False
[0, 0, None, 1, 0, 0, 1, 1]; True
[0, 0, None, 1, 0, 0, None, 0]; False
[0, 0, None, 1, 0, 0, None, 1]; True
[0, 0, None, 1, 0, 1, 0, 0]; False
[0, 0, None, 1, 0, 1, 0, 1]; False
[0, 0, None, 1, 0, 1, 1, 0]; False
[0, 0, None, 1, 0, 1, 1, 1]; False
[0, 0, None, 1, 0, 1, None, 0]; False
[0, 0, None, 1, 0, 1, None, 1]; False
[0, 0, None, 1, 0, None, 0, 0]; False
[0, 0, None, 1, 0, None, 0, 1]; False
[0, 0, None, 1, 0, None, 1, 0]; False
[0, 0, None, 1, 0, None, 1, 1]; False
[0, 0, None, 1, 0, None, None, 0]; False
[0, 0, None, 1, 0, None, None, 1]; False
[0, 0, None, 1, 1, 0, 0, 0]; False
[0, 0, None, 1, 1, 0, 0, 1]; False
[0, 0, None, 1, 1, 0, 1, 0]; False
[0, 0, None, 1, 1, 0, 1, 1]; True
[0, 0, None, 1, 1, 0, None, 0]; False
[0, 0, None, 1, 1, 0, None, 1]; True
[0, 0, None, 1, 1, 1, 0, 0]; False
[0, 0, None, 1, 1, 1, 0, 1]; False
[0, 0, None, 1, 1, 1, 1, 0]; False
[0, 0, None, 1, 1, 1, 1, 1]; False
[0, 0, None, 1, 1, 1, None, 0]; False
[0, 0, None, 1, 1, 1, None, 1]; False
[0, 0, None, 1, 1, None, 0, 0]; False
[0, 0, None, 1, 1, None, 0, 1]; False
[0, 0, None, 1, 1, None, 1, 0]; False
[0, 0, None, 1, 1, None, 1, 1]; False
[0, 0, None, 1, 1, None, None, 0]; False
[0, 0, None, 1, 1, None, None, 1]; False
[0, 0, None, 1, None, 0, 0, 0]; False
[0, 0, None, 1, None, 0, 0, 1]; False
[0, 0, None, 1, None, 0, 1, 0]; True
[0, 0, None, 1, None, 0, 1, 1]; False
[0, 0, None, 1, None, 0, None, 0]; True
[0, 0, None, 1, None, 0, None, 1]; False
[0, 0, None, 1, None, 1, 0, 0]; False
[0, 0, None, 1, None, 1, 0, 1]; False
[0, 0, None, 1, None, 1, 1, 0]; True
[0, 0, None, 1, None, 1, 1, 1]; False
[0, 0, None, 1, None, 1, None, 0]; True
[0, 0, None, 1, None, 1, None, 1]; False
[0, 0, None, 1, None, None, 0, 0]; False
[0, 0, None, 1, None, None, 0, 1]; False
[0, 0, None, 1, None, None, 1, 0]; False
[0, 0, None, 1, None, None, 1, 1]; False
[0, 0, None, None, 0, 0, 0, 0]; False
[0, 0, None, None, 0, 0, 0, 1]; False
[0, 0, None, None, 0, 0, 1, 0]; False
[0, 0, None, None, 0, 0, 1, 1]; False
[0, 0, None, None, 0, 0, None, 0]; False
[0, 0, None, None, 0, 0, None, 1]; False
[0, 0, None, None, 0, 1, 0, 0]; False
[0, 0, None, None, 0, 1, 0, 1]; False
[0, 0, None, None, 0, 1, 1, 0]; False
[0, 0, None, None, 0, 1, 1, 1]; False
[0, 0, None, None, 0, 1, None, 0]; False
[0, 0, None, None, 0, 1, None, 1]; False
[0, 0, None, None, 0, None, 0, 0]; False
[0, 0, None, None, 0, None, 0, 1]; False
[0, 0, None, None, 0, None, 1, 0]; False
[0, 0, None, None, 0, None, 1, 1]; False
[0, 0, None, None, 1, 0, 0, 0]; False
[0, 0, None, None, 1, 0, 0, 1]; False
[0, 0, None, None, 1, 0, 1, 0]; False
[0, 0, None, None, 1, 0, 1, 1]; False
[0, 0, None, None, 1, 0, None, 0]; False
[0, 0, None, None, 1, 0, None, 1]; False
[0, 0, None, None, 1, 1, 0, 0]; False
[0, 0, None, None, 1, 1, 0, 1]; False
[0, 0, None, None, 1, 1, 1, 0]; False
[0, 0, None, None, 1, 1, 1, 1]; False
[0, 0, None, None, 1, 1, None, 0]; False
[0, 0, None, None, 1, 1, None, 1]; False
[0, 0, None, None, 1, None, 0, 0]; False
[0, 0, None, None, 1, None, 0, 1]; False
[0, 0, None, None, 1, None, 1, 0]; False
[0, 0, None, None, 1, None, 1, 1]; False
[0, 1, 0, 0, 0, 0, 0, 0]; False
[0, 1, 0, 0, 0, 0, 0, 1]; False
[0, 1, 0, 0, 0, 0, 1, 0]; False
[0, 1, 0, 0, 0, 0, 1, 1]; False
[0, 1, 0, 0, 0, 0, None, 0]; False
[0, 1, 0, 0, 0, 0, None, 1]; False
[0, 1, 0, 0, 0, 1, 0, 0]; False
[0, 1, 0, 0, 0, 1, 0, 1]; False
[0, 1, 0, 0, 0, 1, 1, 0]; False
[0, 1, 0, 0, 0, 1, 1, 1]; False
[0, 1, 0, 0, 0, 1, None, 0]; False
[0, 1, 0, 0, 0, 1, None, 1]; False
[0, 1, 0, 0, 0, None, 0, 0]; False
[0, 1, 0, 0, 0, None, 0, 1]; False
[0, 1, 0, 0, 0, None, 1, 0]; False
[0, 1, 0, 0, 0, None, 1, 1]; False
[0, 1, 0, 0, 0, None, None, 0]; False
[0, 1, 0, 0, 0, None, None, 1]; False
[0, 1, 0, 0, 1, 0, 0, 0]; False
[0, 1, 0, 0, 1, 0, 0, 1]; False
[0, 1, 0, 0, 1, 0, 1, 0]; False
[0, 1, 0, 0, 1, 0, 1, 1]; False
[0, 1, 0, 0, 1, 0, None, 0]; False
[0, 1, 0, 0, 1, 0, None, 1]; False
[0, 1, 0, 0, 1, 1, 0, 0]; True
[0, 1, 0, 0, 1, 1, 0, 1]; False
[0, 1, 0, 0, 1, 1, 1, 0]; True
[0, 1, 0, 0, 1, 1, 1, 1]; False
[0, 1, 0, 0, 1, 1, None, 0]; True
[0, 1, 0, 0, 1, 1, None, 1]; False
[0, 1, 0, 0, 1, None, 0, 0]; True
[0, 1, 0, 0, 1, None, 0, 1]; False
[0, 1, 0, 0, 1, None, 1, 0]; True
[0, 1, 0, 0, 1, None, 1, 1]; False
[0, 1, 0, 0, 1, None, None, 0]; False
[0, 1, 0, 0, 1, None, None, 1]; False
[0, 1, 0, 0, None, 0, 0, 0]; False
[0, 1, 0, 0, None, 0, 0, 1]; False
[0, 1, 0, 0, None, 0, 1, 0]; False
[0, 1, 0, 0, None, 0, 1, 1]; False
[0, 1, 0, 0, None, 0, None, 0]; False
[0, 1, 0, 0, None, 0, None, 1]; False
[0, 1, 0, 0, None, 1, 0, 0]; True
[0, 1, 0, 0, None, 1, 0, 1]; False
[0, 1, 0, 0, None, 1, 1, 0]; True
[0, 1, 0, 0, None, 1, 1, 1]; False
[0, 1, 0, 0, None, 1, None, 0]; True
[0, 1, 0, 0, None, 1, None, 1]; False
[0, 1, 0, 0, None, None, 0, 0]; True
[0, 1, 0, 0, None, None, 0, 1]; False
[0, 1, 0, 0, None, None, 1, 0]; True
[0, 1, 0, 0, None, None, 1, 1]; False
[0, 1, 0, 0, None, None, None, 0]; False
[0, 1, 0, 0, None, None, None, 1]; False
[0, 1, 0, 1, 0, 0, 0, 0]; False
[0, 1, 0, 1, 0, 0, 0, 1]; False
[0, 1, 0, 1, 0, 0, 1, 0]; False
[0, 1, 0, 1, 0, 0, 1, 1]; False
[0, 1, 0, 1, 0, 0, None, 0]; False
[0, 1, 0, 1, 0, 0, None, 1]; False
[0, 1, 0, 1, 0, 1, 0, 0]; False
[0, 1, 0, 1, 0, 1, 0, 1]; False
[0, 1, 0, 1, 0, 1, 1, 0]; False
[0, 1, 0, 1, 0, 1, 1, 1]; False
[0, 1, 0, 1, 0, 1, None, 0]; False
[0, 1, 0, 1, 0, 1, None, 1]; False
[0, 1, 0, 1, 0, None, 0, 0]; False
[0, 1, 0, 1, 0, None, 0, 1]; False
[0, 1, 0, 1, 0, None, 1, 0]; False
[0, 1, 0, 1, 0, None, 1, 1]; False
[0, 1, 0, 1, 0, None, None, 0]; False
[0, 1, 0, 1, 0, None, None, 1]; False
[0, 1, 0, 1, 1, 0, 0, 0]; False
[0, 1, 0, 1, 1, 0, 0, 1]; False
[0, 1, 0, 1, 1, 0, 1, 0]; False
[0, 1, 0, 1, 1, 0, 1, 1]; False
[0, 1, 0, 1, 1, 0, None, 0]; False
[0, 1, 0, 1, 1, 0, None, 1]; False
[0, 1, 0, 1, 1, 1, 0, 0]; False
[0, 1, 0, 1, 1, 1, 0, 1]; False
[0, 1, 0, 1, 1, 1, 1, 0]; True
[0, 1, 0, 1, 1, 1, 1, 1]; False
[0, 1, 0, 1, 1, 1, None, 0]; True
[0, 1, 0, 1, 1, 1, None, 1]; False
[0, 1, 0, 1, 1, None, 0, 0]; False
[0, 1, 0, 1, 1, None, 0, 1]; False
[0, 1, 0, 1, 1, None, 1, 0]; True
[0, 1, 0, 1, 1, None, 1, 1]; False
[0, 1, 0, 1, 1, None, None, 0]; False
[0, 1, 0, 1, 1, None, None, 1]; False
[0, 1, 0, 1, None, 0, 0, 0]; False
[0, 1, 0, 1, None, 0, 0, 1]; False
[0, 1, 0, 1, None, 0, 1, 0]; False
[0, 1, 0, 1, None, 0, 1, 1]; False
[0, 1, 0, 1, None, 0, None, 0]; False
[0, 1, 0, 1, None, 0, None, 1]; False
[0, 1, 0, 1, None, 1, 0, 0]; False
[0, 1, 0, 1, None, 1, 0, 1]; False
[0, 1, 0, 1, None, 1, 1, 0]; True
[0, 1, 0, 1, None, 1, 1, 1]; False
[0, 1, 0, 1, None, 1, None, 0]; True
[0, 1, 0, 1, None, 1, None, 1]; False
[0, 1, 0, 1, None, None, 0, 0]; False
[0, 1, 0, 1, None, None, 0, 1]; False
[0, 1, 0, 1, None, None, 1, 0]; True
[0, 1, 0, 1, None, None, 1, 1]; False
[0, 1, 0, 1, None, None, None, 0]; False
[0, 1, 0, 1, None, None, None, 1]; False
[0, 1, 0, None, 0, 0, 0, 0]; False
[0, 1, 0, None, 0, 0, 0, 1]; False
[0, 1, 0, None, 0, 0, 1, 0]; False
[0, 1, 0, None, 0, 0, 1, 1]; False
[0, 1, 0, None, 0, 0, None, 0]; False
[0, 1, 0, None, 0, 0, None, 1]; False
[0, 1, 0, None, 0, 1, 0, 0]; False
[0, 1, 0, None, 0, 1, 0, 1]; False
[0, 1, 0, None, 0, 1, 1, 0]; False
[0, 1, 0, None, 0, 1, 1, 1]; False
[0, 1, 0, None, 0, 1, None, 0]; False
[0, 1, 0, None, 0, 1, None, 1]; False
[0, 1, 0, None, 0, None, 0, 0]; False
[0, 1, 0, None, 0, None, 0, 1]; False
[0, 1, 0, None, 0, None, 1, 0]; False
[0, 1, 0, None, 0, None, 1, 1]; False
[0, 1, 0, None, 0, None, None, 0]; False
[0, 1, 0, None, 0, None, None, 1]; False
[0, 1, 0, None, 1, 0, 0, 0]; False
[0, 1, 0, None, 1, 0, 0, 1]; False
[0, 1, 0, None, 1, 0, 1, 0]; False
[0, 1, 0, None, 1, 0, 1, 1]; False
[0, 1, 0, None, 1, 0, None, 0]; False
[0, 1, 0, None, 1, 0, None, 1]; False
[0, 1, 0, None, 1, 1, 0, 0]; False
[0, 1, 0, None, 1, 1, 0, 1]; False
[0, 1, 0, None, 1, 1, 1, 0]; False
[0, 1, 0, None, 1, 1, 1, 1]; False
[0, 1, 0, None, 1, 1, None, 0]; False
[0, 1, 0, None, 1, 1, None, 1]; False
[0, 1, 0, None, 1, None, 0, 0]; False
[0, 1, 0, None, 1, None, 0, 1]; False
[0, 1, 0, None, 1, None, 1, 0]; False
[0, 1, 0, None, 1, None, 1, 1]; False
[0, 1, 0, None, 1, None, None, 0]; False
[0, 1, 0, None, 1, None, None, 1]; False
[0, 1, 0, None, None, 0, 0, 0]; False
[0, 1, 0, None, None, 0, 0, 1]; False
[0, 1, 0, None, None, 0, 1, 0]; False
[0, 1, 0, None, None, 0, 1, 1]; False
[0, 1, 0, None, None, 0, None, 0]; False
[0, 1, 0, None, None, 0, None, 1]; False
[0, 1, 0, None, None, 1, 0, 0]; False
[0, 1, 0, None, None, 1, 0, 1]; False
[0, 1, 0, None, None, 1, 1, 0]; False
[0, 1, 0, None, None, 1, 1, 1]; False
[0, 1, 0, None, None, 1, None, 0]; False
[0, 1, 0, None, None, 1, None, 1]; False
[0, 1, 0, None, None, None, 0, 0]; False
[0, 1, 0, None, None, None, 0, 1]; False
[0, 1, 0, None, None, None, 1, 0]; False
[0, 1, 0, None, None, None, 1, 1]; False
[0, 1, 1, 0, 0, 0, 0, 0]; False
[0, 1, 1, 0, 0, 0, 0, 1]; False
[0, 1, 1, 0, 0, 0, 1, 0]; False
[0, 1, 1, 0, 0, 0, 1, 1]; False
[0, 1, 1, 0, 0, 0, None, 0]; False
[0, 1, 1, 0, 0, 0, None, 1]; False
[0, 1, 1, 0, 0, 1, 0, 0]; False
[0, 1, 1, 0, 0, 1, 0, 1]; False
[0, 1, 1, 0, 0, 1, 1, 0]; False
[0, 1, 1, 0, 0, 1, 1, 1]; False
[0, 1, 1, 0, 0, 1, None, 0]; False
[0, 1, 1, 0, 0, 1, None, 1]; False
[0, 1, 1, 0, 0, None, 0, 0]; False
[0, 1, 1, 0, 0, None, 0, 1]; False
[0, 1, 1, 0, 0, None, 1, 0]; False
[0, 1, 1, 0, 0, None, 1, 1]; False
[0, 1, 1, 0, 0, None, None, 0]; False
[0, 1, 1, 0, 0, None, None, 1]; False
[0, 1, 1, 0, 1, 0, 0, 0]; True
[0, 1, 1, 0, 1, 0, 0, 1]; False
[0, 1, 1, 0, 1, 0, 1, 0]; False
[0, 1, 1, 0, 1, 0, 1, 1]; False
[0, 1, 1, 0, 1, 0, None, 0]; False
[0, 1, 1, 0, 1, 0, None, 1]; False
[0, 1, 1, 0, 1, 1, 0, 0]; True
[0, 1, 1, 0, 1, 1, 0, 1]; False
[0, 1, 1, 0, 1, 1, 1, 0]; True
[0, 1, 1, 0, 1, 1, 1, 1]; False
[0, 1, 1, 0, 1, 1, None, 0]; True
[0, 1, 1, 0, 1, 1, None, 1]; False
[0, 1, 1, 0, 1, None, 0, 0]; True
[0, 1, 1, 0, 1, None, 0, 1]; False
[0, 1, 1, 0, 1, None, 1, 0]; True
[0, 1, 1, 0, 1, None, 1, 1]; False
[0, 1, 1, 0, 1, None, None, 0]; True
[0, 1, 1, 0, 1, None, None, 1]; False
[0, 1, 1, 0, None, 0, 0, 0]; True
[0, 1, 1, 0, None, 0, 0, 1]; False
[0, 1, 1, 0, None, 0, 1, 0]; False
[0, 1, 1, 0, None, 0, 1, 1]; False
[0, 1, 1, 0, None, 0, None, 0]; False
[0, 1, 1, 0, None, 0, None, 1]; False
[0, 1, 1, 0, None, 1, 0, 0]; True
[0, 1, 1, 0, None, 1, 0, 1]; False
[0, 1, 1, 0, None, 1, 1, 0]; True
[0, 1, 1, 0, None, 1, 1, 1]; False
[0, 1, 1, 0, None, 1, None, 0]; True
[0, 1, 1, 0, None, 1, None, 1]; False
[0, 1, 1, 0, None, None, 0, 0]; True
[0, 1, 1, 0, None, None, 0, 1]; False
[0, 1, 1, 0, None, None, 1, 0]; True
[0, 1, 1, 0, None, None, 1, 1]; False
[0, 1, 1, 0, None, None, None, 0]; True
[0, 1, 1, 0, None, None, None, 1]; False
[0, 1, 1, 1, 0, 0, 0, 0]; False
[0, 1, 1, 1, 0, 0, 0, 1]; False
[0, 1, 1, 1, 0, 0, 1, 0]; False
[0, 1, 1, 1, 0, 0, 1, 1]; False
[0, 1, 1, 1, 0, 0, None, 0]; False
[0, 1, 1, 1, 0, 0, None, 1]; False
[0, 1, 1, 1, 0, 1, 0, 0]; False
[0, 1, 1, 1, 0, 1, 0, 1]; False
[0, 1, 1, 1, 0, 1, 1, 0]; False
[0, 1, 1, 1, 0, 1, 1, 1]; False
[0, 1, 1, 1, 0, 1, None, 0]; False
[0, 1, 1, 1, 0, 1, None, 1]; False
[0, 1, 1, 1, 0, None, 0, 0]; False
[0, 1, 1, 1, 0, None, 0, 1]; False
[0, 1, 1, 1, 0, None, 1, 0]; False
[0, 1, 1, 1, 0, None, 1, 1]; False
[0, 1, 1, 1, 0, None, None, 0]; False
[0, 1, 1, 1, 0, None, None, 1]; False
[0, 1, 1, 1, 1, 0, 0, 0]; False
[0, 1, 1, 1, 1, 0, 0, 1]; False
[0, 1, 1, 1, 1, 0, 1, 0]; False
[0, 1, 1, 1, 1, 0, 1, 1]; False
[0, 1, 1, 1, 1, 0, None, 0]; False
[0, 1, 1, 1, 1, 0, None, 1]; False
[0, 1, 1, 1, 1, 1, 0, 0]; True
[0, 1, 1, 1, 1, 1, 0, 1]; False
[0, 1, 1, 1, 1, 1, 1, 0]; True
[0, 1, 1, 1, 1, 1, 1, 1]; False
[0, 1, 1, 1, 1, 1, None, 0]; True
[0, 1, 1, 1, 1, 1, None, 1]; False
[0, 1, 1, 1, 1, None, 0, 0]; True
[0, 1, 1, 1, 1, None, 0, 1]; False
[0, 1, 1, 1, 1, None, 1, 0]; True
[0, 1, 1, 1, 1, None, 1, 1]; False
[0, 1, 1, 1, 1, None, None, 0]; True
[0, 1, 1, 1, 1, None, None, 1]; False
[0, 1, 1, 1, None, 0, 0, 0]; False
[0, 1, 1, 1, None, 0, 0, 1]; False
[0, 1, 1, 1, None, 0, 1, 0]; False
[0, 1, 1, 1, None, 0, 1, 1]; False
[0, 1, 1, 1, None, 0, None, 0]; False
[0, 1, 1, 1, None, 0, None, 1]; False
[0, 1, 1, 1, None, 1, 0, 0]; True
[0, 1, 1, 1, None, 1, 0, 1]; False
[0, 1, 1, 1, None, 1, 1, 0]; True
[0, 1, 1, 1, None, 1, 1, 1]; False
[0, 1, 1, 1, None, 1, None, 0]; True
[0, 1, 1, 1, None, 1, None, 1]; False
[0, 1, 1, 1, None, None, 0, 0]; True
[0, 1, 1, 1, None, None, 0, 1]; False
[0, 1, 1, 1, None, None, 1, 0]; True
[0, 1, 1, 1, None, None, 1, 1]; False
[0, 1, 1, 1, None, None, None, 0]; True
[0, 1, 1, 1, None, None, None, 1]; False
[0, 1, 1, None, 0, 0, 0, 0]; False
[0, 1, 1, None, 0, 0, 0, 1]; False
[0, 1, 1, None, 0, 0, 1, 0]; False
[0, 1, 1, None, 0, 0, 1, 1]; False
[0, 1, 1, None, 0, 0, None, 0]; False
[0, 1, 1, None, 0, 0, None, 1]; False
[0, 1, 1, None, 0, 1, 0, 0]; False
[0, 1, 1, None, 0, 1, 0, 1]; False
[0, 1, 1, None, 0, 1, 1, 0]; False
[0, 1, 1, None, 0, 1, 1, 1]; False
[0, 1, 1, None, 0, 1, None, 0]; False
[0, 1, 1, None, 0, 1, None, 1]; False
[0, 1, 1, None, 0, None, 0, 0]; False
[0, 1, 1, None, 0, None, 0, 1]; False
[0, 1, 1, None, 0, None, 1, 0]; False
[0, 1, 1, None, 0, None, 1, 1]; False
[0, 1, 1, None, 0, None, None, 0]; False
[0, 1, 1, None, 0, None, None, 1]; False
[0, 1, 1, None, 1, 0, 0, 0]; False
[0, 1, 1, None, 1, 0, 0, 1]; False
[0, 1, 1, None, 1, 0, 1, 0]; False
[0, 1, 1, None, 1, 0, 1, 1]; False
[0, 1, 1, None, 1, 0, None, 0]; False
[0, 1, 1, None, 1, 0, None, 1]; False
[0, 1, 1, None, 1, 1, 0, 0]; False
[0, 1, 1, None, 1, 1, 0, 1]; False
[0, 1, 1, None, 1, 1, 1, 0]; False
[0, 1, 1, None, 1, 1, 1, 1]; False
[0, 1, 1, None, 1, 1, None, 0]; False
[0, 1, 1, None, 1, 1, None, 1]; False
[0, 1, 1, None, 1, None, 0, 0]; False
[0, 1, 1, None, 1, None, 0, 1]; False
[0, 1, 1, None, 1, None, 1, 0]; False
[0, 1, 1, None, 1, None, 1, 1]; False
[0, 1, 1, None, 1, None, None, 0]; False
[0, 1, 1, None, 1, None, None, 1]; False
[0, 1, 1, None, None, 0, 0, 0]; False
[0, 1, 1, None, None, 0, 0, 1]; False
[0, 1, 1, None, None, 0, 1, 0]; False
[0, 1, 1, None, None, 0, 1, 1]; False
[0, 1, 1, None, None, 0, None, 0]; False
[0, 1, 1, None, None, 0, None, 1]; False
[0, 1, 1, None, None, 1, 0, 0]; False
[0, 1, 1, None, None, 1, 0, 1]; False
[0, 1, 1, None, None, 1, 1, 0]; False
[0, 1, 1, None, None, 1, 1, 1]; False
[0, 1, 1, None, None, 1, None, 0]; False
[0, 1, 1, None, None, 1, None, 1]; False
[0, 1, 1, None, None, None, 0, 0]; False
[0, 1, 1, None, None, None, 0, 1]; False
[0, 1, 1, None, None, None, 1, 0]; False
[0, 1, 1, None, None, None, 1, 1]; False
[0, 1, None, 0, 0, 0, 0, 0]; False
[0, 1, None, 0, 0, 0, 0, 1]; False
[0, 1, None, 0, 0, 0, 1, 0]; False
[0, 1, None, 0, 0, 0, 1, 1]; True
[0, 1, None, 0, 0, 0, None, 0]; False
[0, 1, None, 0, 0, 0, None, 1]; True
[0, 1, None, 0, 0, 1, 0, 0]; False
[0, 1, None, 0, 0, 1, 0, 1]; False
[0, 1, None, 0, 0, 1, 1, 0]; False
[0, 1, None, 0, 0, 1, 1, 1]; False
[0, 1, None, 0, 0, 1, None, 0]; False
[0, 1, None, 0, 0, 1, None, 1]; False
[0, 1, None, 0, 0, None, 0, 0]; False
[0, 1, None, 0, 0, None, 0, 1]; False
[0, 1, None, 0, 0, None, 1, 0]; False
[0, 1, None, 0, 0, None, 1, 1]; False
[0, 1, None, 0, 0, None, None, 0]; False
[0, 1, None, 0, 0, None, None, 1]; True
[0, 1, None, 0, 1, 0, 0, 0]; False
[0, 1, None, 0, 1, 0, 0, 1]; False
[0, 1, None, 0, 1, 0, 1, 0]; False
[0, 1, None, 0, 1, 0, 1, 1]; True
[0, 1, None, 0, 1, 0, None, 0]; False
[0, 1, None, 0, 1, 0, None, 1]; True
[0, 1, None, 0, 1, 1, 0, 0]; False
[0, 1, None, 0, 1, 1, 0, 1]; False
[0, 1, None, 0, 1, 1, 1, 0]; False
[0, 1, None, 0, 1, 1, 1, 1]; False
[0, 1, None, 0, 1, 1, None, 0]; False
[0, 1, None, 0, 1, 1, None, 1]; False
[0, 1, None, 0, 1, None, 0, 0]; False
[0, 1, None, 0, 1, None, 0, 1]; False
[0, 1, None, 0, 1, None, 1, 0]; False
[0, 1, None, 0, 1, None, 1, 1]; False
[0, 1, None, 0, 1, None, None, 0]; False
[0, 1, None, 0, 1, None, None, 1]; True
[0, 1, None, 0, None, 0, 0, 0]; False
[0, 1, None, 0, None, 0, 0, 1]; False
[0, 1, None, 0, None, 0, 1, 0]; True
[0, 1, None, 0, None, 0, 1, 1]; False
[0, 1, None, 0, None, 0, None, 0]; True
[0, 1, None, 0, None, 0, None, 1]; False
[0, 1, None, 0, None, 1, 0, 0]; False
[0, 1, None, 0, None, 1, 0, 1]; False
[0, 1, None, 0, None, 1, 1, 0]; True
[0, 1, None, 0, None, 1, 1, 1]; False
[0, 1, None, 0, None, 1, None, 0]; True
[0, 1, None, 0, None, 1, None, 1]; False
[0, 1, None, 0, None, None, 0, 0]; False
[0, 1, None, 0, None, None, 0, 1]; False
[0, 1, None, 0, None, None, 1, 0]; False
[0, 1, None, 0, None, None, 1, 1]; False
[0, 1, None, 1, 0, 0, 0, 0]; False
[0, 1, None, 1, 0, 0, 0, 1]; False
[0, 1, None, 1, 0, 0, 1, 0]; False
[0, 1, None, 1, 0, 0, 1, 1]; True
[0, 1, None, 1, 0, 0, None, 0]; False
[0, 1, None, 1, 0, 0, None, 1]; True
[0, 1, None, 1, 0, 1, 0, 0]; False
[0, 1, None, 1, 0, 1, 0, 1]; False
[0, 1, None, 1, 0, 1, 1, 0]; False
[0, 1, None, 1, 0, 1, 1, 1]; False
[0, 1, None, 1, 0, 1, None, 0]; False
[0, 1, None, 1, 0, 1, None, 1]; False
[0, 1, None, 1, 0, None, 0, 0]; False
[0, 1, None, 1, 0, None, 0, 1]; False
[0, 1, None, 1, 0, None, 1, 0]; False
[0, 1, None, 1, 0, None, 1, 1]; False
[0, 1, None, 1, 0, None, None, 0]; False
[0, 1, None, 1, 0, None, None, 1]; False
[0, 1, None, 1, 1, 0, 0, 0]; False
[0, 1, None, 1, 1, 0, 0, 1]; False
[0, 1, None, 1, 1, 0, 1, 0]; False
[0, 1, None, 1, 1, 0, 1, 1]; True
[0, 1, None, 1, 1, 0, None, 0]; False
[0, 1, None, 1, 1, 0, None, 1]; True
[0, 1, None, 1, 1, 1, 0, 0]; False
[0, 1, None, 1, 1, 1, 0, 1]; False
[0, 1, None, 1, 1, 1, 1, 0]; False
[0, 1, None, 1, 1, 1, 1, 1]; False
[0, 1, None, 1, 1, 1, None, 0]; False
[0, 1, None, 1, 1, 1, None, 1]; False
[0, 1, None, 1, 1, None, 0, 0]; False
[0, 1, None, 1, 1, None, 0, 1]; False
[0, 1, None, 1, 1, None, 1, 0]; False
[0, 1, None, 1, 1, None, 1, 1]; False
[0, 1, None, 1, 1, None, None, 0]; False
[0, 1, None, 1, 1, None, None, 1]; False
[0, 1, None, 1, None, 0, 0, 0]; False
[0, 1, None, 1, None, 0, 0, 1]; False
[0, 1, None, 1, None, 0, 1, 0]; True
[0, 1, None, 1, None, 0, 1, 1]; False
[0, 1, None, 1, None, 0, None, 0]; True
[0, 1, None, 1, None, 0, None, 1]; False
[0, 1, None, 1, None, 1, 0, 0]; False
[0, 1, None, 1, None, 1, 0, 1]; False
[0, 1, None, 1, None, 1, 1, 0]; True
[0, 1, None, 1, None, 1, 1, 1]; False
[0, 1, None, 1, None, 1, None, 0]; True
[0, 1, None, 1, None, 1, None, 1]; False
[0, 1, None, 1, None, None, 0, 0]; False
[0, 1, None, 1, None, None, 0, 1]; False
[0, 1, None, 1, None, None, 1, 0]; False
[0, 1, None, 1, None, None, 1, 1]; False
[0, 1, None, None, 0, 0, 0, 0]; False
[0, 1, None, None, 0, 0, 0, 1]; False
[0, 1, None, None, 0, 0, 1, 0]; False
[0, 1, None, None, 0, 0, 1, 1]; False
[0, 1, None, None, 0, 0, None, 0]; False
[0, 1, None, None, 0, 0, None, 1]; False
[0, 1, None, None, 0, 1, 0, 0]; False
[0, 1, None, None, 0, 1, 0, 1]; False
[0, 1, None, None, 0, 1, 1, 0]; False
[0, 1, None, None, 0, 1, 1, 1]; False
[0, 1, None, None, 0, 1, None, 0]; False
[0, 1, None, None, 0, 1, None, 1]; False
[0, 1, None, None, 0, None, 0, 0]; False
[0, 1, None, None, 0, None, 0, 1]; False
[0, 1, None, None, 0, None, 1, 0]; False
[0, 1, None, None, 0, None, 1, 1]; False
[0, 1, None, None, 1, 0, 0, 0]; False
[0, 1, None, None, 1, 0, 0, 1]; False
[0, 1, None, None, 1, 0, 1, 0]; False
[0, 1, None, None, 1, 0, 1, 1]; False
[0, 1, None, None, 1, 0, None, 0]; False
[0, 1, None, None, 1, 0, None, 1]; False
[0, 1, None, None, 1, 1, 0, 0]; False
[0, 1, None, None, 1, 1, 0, 1]; False
[0, 1, None, None, 1, 1, 1, 0]; False
[0, 1, None, None, 1, 1, 1, 1]; False
[0, 1, None, None, 1, 1, None, 0]; False
[0, 1, None, None, 1, 1, None, 1]; False
[0, 1, None, None, 1, None, 0, 0]; False
[0, 1, None, None, 1, None, 0, 1]; False
[0, 1, None, None, 1, None, 1, 0]; False
[0, 1, None, None, 1, None, 1, 1]; False
[0, None, 0, 0, 0, 0, 0, 0]; False
[0, None, 0, 0, 0, 0, 0, 1]; False
[0, None, 0, 0, 0, 0, 1, 0]; False
[0, None, 0, 0, 0, 0, 1, 1]; False
[0, None, 0, 0, 0, 0, None, 0]; False
[0, None, 0, 0, 0, 0, None, 1]; False
[0, None, 0, 0, 0, 1, 0, 0]; False
[0, None, 0, 0, 0, 1, 0, 1]; False
[0, None, 0, 0, 0, 1, 1, 0]; False
[0, None, 0, 0, 0, 1, 1, 1]; False
[0, None, 0, 0, 0, 1, None, 0]; False
[0, None, 0, 0, 0, 1, None, 1]; False
[0, None, 0, 0, 0, None, 0, 0]; False
[0, None, 0, 0, 0, None, 0, 1]; False
[0, None, 0, 0, 0, None, 1, 0]; False
[0, None, 0, 0, 0, None, 1, 1]; False
[0, None, 0, 0, 0, None, None, 0]; False
[0, None, 0, 0, 0, None, None, 1]; False
[0, None, 0, 0, 1, 0, 0, 0]; False
[0, None, 0, 0, 1, 0, 0, 1]; False
[0, None, 0, 0, 1, 0, 1, 0]; False
[0, None, 0, 0, 1, 0, 1, 1]; False
[0, None, 0, 0, 1, 0, None, 0]; False
[0, None, 0, 0, 1, 0, None, 1]; False
[0, None, 0, 0, 1, 1, 0, 0]; False
[0, None, 0, 0, 1, 1, 0, 1]; False
[0, None, 0, 0, 1, 1, 1, 0]; False
[0, None, 0, 0, 1, 1, 1, 1]; False
[0, None, 0, 0, 1, 1, None, 0]; False
[0, None, 0, 0, 1, 1, None, 1]; False
[0, None, 0, 0, 1, None, 0, 0]; False
[0, None, 0, 0, 1, None, 0, 1]; False
[0, None, 0, 0, 1, None, 1, 0]; False
[0, None, 0, 0, 1, None, 1, 1]; False
[0, None, 0, 0, 1, None, None, 0]; False
[0, None, 0, 0, 1, None, None, 1]; False
[0, None, 0, 0, None, 0, 0, 0]; False
[0, None, 0, 0, None, 0, 0, 1]; False
[0, None, 0, 0, None, 0, 1, 0]; False
[0, None, 0, 0, None, 0, 1, 1]; False
[0, None, 0, 0, None, 0, None, 0]; False
[0, None, 0, 0, None, 0, None, 1]; False
[0, None, 0, 0, None, 1, 0, 0]; False
[0, None, 0, 0, None, 1, 0, 1]; False
[0, None, 0, 0, None, 1, 1, 0]; False
[0, None, 0, 0, None, 1, 1, 1]; False
[0, None, 0, 0, None, 1, None, 0]; False
[0, None, 0, 0, None, 1, None, 1]; False
[0, None, 0, 0, None, None, 0, 0]; False
[0, None, 0, 0, None, None, 0, 1]; False
[0, None, 0, 0, None, None, 1, 0]; False
[0, None, 0, 0, None, None, 1, 1]; False
[0, None, 0, 1, 0, 0, 0, 0]; False
[0, None, 0, 1, 0, 0, 0, 1]; False
[0, None, 0, 1, 0, 0, 1, 0]; False
[0, None, 0, 1, 0, 0, 1, 1]; False
[0, None, 0, 1, 0, 0, None, 0]; False
[0, None, 0, 1, 0, 0, None, 1]; False
[0, None, 0, 1, 0, 1, 0, 0]; False
[0, None, 0, 1, 0, 1, 0, 1]; False
[0, None, 0, 1, 0, 1, 1, 0]; False
[0, None, 0, 1, 0, 1, 1, 1]; False
[0, None, 0, 1, 0, 1, None, 0]; False
[0, None, 0, 1, 0, 1, None, 1]; False
[0, None, 0, 1, 0, None, 0, 0]; False
[0, None, 0, 1, 0, None, 0, 1]; False
[0, None, 0, 1, 0, None, 1, 0]; False
[0, None, 0, 1, 0, None, 1, 1]; False
[0, None, 0, 1, 0, None, None, 0]; False
[0, None, 0, 1, 0, None, None, 1]; False
[0, None, 0, 1, 1, 0, 0, 0]; False
[0, None, 0, 1, 1, 0, 0, 1]; False
[0, None, 0, 1, 1, 0, 1, 0]; False
[0, None, 0, 1, 1, 0, 1, 1]; False
[0, None, 0, 1, 1, 0, None, 0]; False
[0, None, 0, 1, 1, 0, None, 1]; False
[0, None, 0, 1, 1, 1, 0, 0]; False
[0, None, 0, 1, 1, 1, 0, 1]; False
[0, None, 0, 1, 1, 1, 1, 0]; False
[0, None, 0, 1, 1, 1, 1, 1]; False
[0, None, 0, 1, 1, 1, None, 0]; False
[0, None, 0, 1, 1, 1, None, 1]; False
[0, None, 0, 1, 1, None, 0, 0]; False
[0, None, 0, 1, 1, None, 0, 1]; False
[0, None, 0, 1, 1, None, 1, 0]; False
[0, None, 0, 1, 1, None, 1, 1]; False
[0, None, 0, 1, 1, None, None, 0]; False
[0, None, 0, 1, 1, None, None, 1]; False
[0, None, 0, 1, None, 0, 0, 0]; False
[0, None, 0, 1, None, 0, 0, 1]; False
[0, None, 0, 1, None, 0, 1, 0]; False
[0, None, 0, 1, None, 0, 1, 1]; False
[0, None, 0, 1, None, 0, None, 0]; False
[0, None, 0, 1, None, 0, None, 1]; False
[0, None, 0, 1, None, 1, 0, 0]; False
[0, None, 0, 1, None, 1, 0, 1]; False
[0, None, 0, 1, None, 1, 1, 0]; False
[0, None, 0, 1, None, 1, 1, 1]; False
[0, None, 0, 1, None, 1, None, 0]; False
[0, None, 0, 1, None, 1, None, 1]; False
[0, None, 0, 1, None, None, 0, 0]; False
[0, None, 0, 1, None, None, 0, 1]; False
[0, None, 0, 1, None, None, 1, 0]; False
[0, None, 0, 1, None, None, 1, 1]; False
[0, None, 0, None, 0, 0, 0, 0]; False
[0, None, 0, None, 0, 0, 0, 1]; False
[0, None, 0, None, 0, 0, 1, 0]; False
[0, None, 0, None, 0, 0, 1, 1]; False
[0, None, 0, None, 0, 0, None, 0]; False
[0, None, 0, None, 0, 0, None, 1]; False
[0, None, 0, None, 0, 1, 0, 0]; False
[0, None, 0, None, 0, 1, 0, 1]; False
[0, None, 0, None, 0, 1, 1, 0]; False
[0, None, 0, None, 0, 1, 1, 1]; False
[0, None, 0, None, 0, 1, None, 0]; False
[0, None, 0, None, 0, 1, None, 1]; False
[0, None, 0, None, 0, None, 0, 0]; False
[0, None, 0, None, 0, None, 0, 1]; False
[0, None, 0, None, 0, None, 1, 0]; False
[0, None, 0, None, 0, None, 1, 1]; False
[0, None, 0, None, 1, 0, 0, 0]; False
[0, None, 0, None, 1, 0, 0, 1]; False
[0, None, 0, None, 1, 0, 1, 0]; False
[0, None, 0, None, 1, 0, 1, 1]; False
[0, None, 0, None, 1, 0, None, 0]; False
[0, None, 0, None, 1, 0, None, 1]; False
[0, None, 0, None, 1, 1, 0, 0]; False
[0, None, 0, None, 1, 1, 0, 1]; False
[0, None, 0, None, 1, 1, 1, 0]; False
[0, None, 0, None, 1, 1, 1, 1]; False
[0, None, 0, None, 1, 1, None, 0]; False
[0, None, 0, None, 1, 1, None, 1]; False
[0, None, 0, None, 1, None, 0, 0]; False
[0, None, 0, None, 1, None, 0, 1]; False
[0, None, 0, None, 1, None, 1, 0]; False
[0, None, 0, None, 1, None, 1, 1]; False
[0, None, 1, 0, 0, 0, 0, 0]; False
[0, None, 1, 0, 0, 0, 0, 1]; False
[0, None, 1, 0, 0, 0, 1, 0]; False
[0, None, 1, 0, 0, 0, 1, 1]; False
[0, None, 1, 0, 0, 0, None, 0]; False
[0, None, 1, 0, 0, 0, None, 1]; False
[0, None, 1, 0, 0, 1, 0, 0]; False
[0, None, 1, 0, 0, 1, 0, 1]; False
[0, None, 1, 0, 0, 1, 1, 0]; False
[0, None, 1, 0, 0, 1, 1, 1]; False
[0, None, 1, 0, 0, 1, None, 0]; False
[0, None, 1, 0, 0, 1, None, 1]; False
[0, None, 1, 0, 0, None, 0, 0]; False
[0, None, 1, 0, 0, None, 0, 1]; False
[0, None, 1, 0, 0, None, 1, 0]; False
[0, None, 1, 0, 0, None, 1, 1]; False
[0, None, 1, 0, 0, None, None, 0]; False
[0, None, 1, 0, 0, None, None, 1]; False
[0, None, 1, 0, 1, 0, 0, 0]; False
[0, None, 1, 0, 1, 0, 0, 1]; False
[0, None, 1, 0, 1, 0, 1, 0]; False
[0, None, 1, 0, 1, 0, 1, 1]; False
[0, None, 1, 0, 1, 0, None, 0]; False
[0, None, 1, 0, 1, 0, None, 1]; False
[0, None, 1, 0, 1, 1, 0, 0]; False
[0, None, 1, 0, 1, 1, 0, 1]; False
[0, None, 1, 0, 1, 1, 1, 0]; False
[0, None, 1, 0, 1, 1, 1, 1]; False
[0, None, 1, 0, 1, 1, None, 0]; False
[0, None, 1, 0, 1, 1, None, 1]; False
[0, None, 1, 0, 1, None, 0, 0]; False
[0, None, 1, 0, 1, None, 0, 1]; False
[0, None, 1, 0, 1, None, 1, 0]; False
[0, None, 1, 0, 1, None, 1, 1]; False
[0, None, 1, 0, 1, None, None, 0]; False
[0, None, 1, 0, 1, None, None, 1]; False
[0, None, 1, 0, None, 0, 0, 0]; False
[0, None, 1, 0, None, 0, 0, 1]; False
[0, None, 1, 0, None, 0, 1, 0]; False
[0, None, 1, 0, None, 0, 1, 1]; False
[0, None, 1, 0, None, 0, None, 0]; False
[0, None, 1, 0, None, 0, None, 1]; False
[0, None, 1, 0, None, 1, 0, 0]; False
[0, None, 1, 0, None, 1, 0, 1]; False
[0, None, 1, 0, None, 1, 1, 0]; False
[0, None, 1, 0, None, 1, 1, 1]; False
[0, None, 1, 0, None, 1, None, 0]; False
[0, None, 1, 0, None, 1, None, 1]; False
[0, None, 1, 0, None, None, 0, 0]; False
[0, None, 1, 0, None, None, 0, 1]; False
[0, None, 1, 0, None, None, 1, 0]; False
[0, None, 1, 0, None, None, 1, 1]; False
[0, None, 1, 1, 0, 0, 0, 0]; False
[0, None, 1, 1, 0, 0, 0, 1]; False
[0, None, 1, 1, 0, 0, 1, 0]; False
[0, None, 1, 1, 0, 0, 1, 1]; False
[0, None, 1, 1, 0, 0, None, 0]; False
[0, None, 1, 1, 0, 0, None, 1]; False
[0, None, 1, 1, 0, 1, 0, 0]; False
[0, None, 1, 1, 0, 1, 0, 1]; False
[0, None, 1, 1, 0, 1, 1, 0]; False
[0, None, 1, 1, 0, 1, 1, 1]; False
[0, None, 1, 1, 0, 1, None, 0]; False
[0, None, 1, 1, 0, 1, None, 1]; False
[0, None, 1, 1, 0, None, 0, 0]; False
[0, None, 1, 1, 0, None, 0, 1]; False
[0, None, 1, 1, 0, None, 1, 0]; False
[0, None, 1, 1, 0, None, 1, 1]; False
[0, None, 1, 1, 0, None, None, 0]; False
[0, None, 1, 1, 0, None, None, 1]; False
[0, None, 1, 1, 1, 0, 0, 0]; False
[0, None, 1, 1, 1, 0, 0, 1]; False
[0, None, 1, 1, 1, 0, 1, 0]; False
[0, None, 1, 1, 1, 0, 1, 1]; False
[0, None, 1, 1, 1, 0, None, 0]; False
[0, None, 1, 1, 1, 0, None, 1]; False
[0, None, 1, 1, 1, 1, 0, 0]; False
[0, None, 1, 1, 1, 1, 0, 1]; False
[0, None, 1, 1, 1, 1, 1, 0]; False
[0, None, 1, 1, 1, 1, 1, 1]; False
[0, None, 1, 1, 1, 1, None, 0]; False
[0, None, 1, 1, 1, 1, None, 1]; False
[0, None, 1, 1, 1, None, 0, 0]; False
[0, None, 1, 1, 1, None, 0, 1]; False
[0, None, 1, 1, 1, None, 1, 0]; False
[0, None, 1, 1, 1, None, 1, 1]; False
[0, None, 1, 1, 1, None, None, 0]; False
[0, None, 1, 1, 1, None, None, 1]; False
[0, None, 1, 1, None, 0, 0, 0]; False
[0, None, 1, 1, None, 0, 0, 1]; False
[0, None, 1, 1, None, 0, 1, 0]; False
[0, None, 1, 1, None, 0, 1, 1]; False
[0, None, 1, 1, None, 0, None, 0]; False
[0, None, 1, 1, None, 0, None, 1]; False
[0, None, 1, 1, None, 1, 0, 0]; False
[0, None, 1, 1, None, 1, 0, 1]; False
[0, None, 1, 1, None, 1, 1, 0]; False
[0, None, 1, 1, None, 1, 1, 1]; False
[0, None, 1, 1, None, 1, None, 0]; False
[0, None, 1, 1, None, 1, None, 1]; False
[0, None, 1, 1, None, None, 0, 0]; False
[0, None, 1, 1, None, None, 0, 1]; False
[0, None, 1, 1, None, None, 1, 0]; False
[0, None, 1, 1, None, None, 1, 1]; False
[0, None, 1, None, 0, 0, 0, 0]; False
[0, None, 1, None, 0, 0, 0, 1]; False
[0, None, 1, None, 0, 0, 1, 0]; False
[0, None, 1, None, 0, 0, 1, 1]; False
[0, None, 1, None, 0, 0, None, 0]; False
[0, None, 1, None, 0, 0, None, 1]; False
[0, None, 1, None, 0, 1, 0, 0]; False
[0, None, 1, None, 0, 1, 0, 1]; False
[0, None, 1, None, 0, 1, 1, 0]; False
[0, None, 1, None, 0, 1, 1, 1]; False
[0, None, 1, None, 0, 1, None, 0]; False
[0, None, 1, None, 0, 1, None, 1]; False
[0, None, 1, None, 0, None, 0, 0]; False
[0, None, 1, None, 0, None, 0, 1]; False
[0, None, 1, None, 0, None, 1, 0]; False
[0, None, 1, None, 0, None, 1, 1]; False
[0, None, 1, None, 1, 0, 0, 0]; False
[0, None, 1, None, 1, 0, 0, 1]; False
[0, None, 1, None, 1, 0, 1, 0]; False
[0, None, 1, None, 1, 0, 1, 1]; False
[0, None, 1, None, 1, 0, None, 0]; False
[0, None, 1, None, 1, 0, None, 1]; False
[0, None, 1, None, 1, 1, 0, 0]; False
[0, None, 1, None, 1, 1, 0, 1]; False
[0, None, 1, None, 1, 1, 1, 0]; False
[0, None, 1, None, 1, 1, 1, 1]; False
[0, None, 1, None, 1, 1, None, 0]; False
[0, None, 1, None, 1, 1, None, 1]; False
[0, None, 1, None, 1, None, 0, 0]; False
[0, None, 1, None, 1, None, 0, 1]; False
[0, None, 1, None, 1, None, 1, 0]; False
[0, None, 1, None, 1, None, 1, 1]; False
[1, 0, 0, 0, 0, 0, 0, 0]; False
[1, 0, 0, 0, 0, 0, 0, 1]; False
[1, 0, 0, 0, 0, 0, 1, 0]; False
[1, 0, 0, 0, 0, 0, 1, 1]; False
[1, 0, 0, 0, 0, 0, None, 0]; False
[1, 0, 0, 0, 0, 0, None, 1]; False
[1, 0, 0, 0, 0, 1, 0, 0]; False
[1, 0, 0, 0, 0, 1, 0, 1]; False
[1, 0, 0, 0, 0, 1, 1, 0]; False
[1, 0, 0, 0, 0, 1, 1, 1]; False
[1, 0, 0, 0, 0, 1, None, 0]; False
[1, 0, 0, 0, 0, 1, None, 1]; False
[1, 0, 0, 0, 0, None, 0, 0]; False
[1, 0, 0, 0, 0, None, 0, 1]; False
[1, 0, 0, 0, 0, None, 1, 0]; False
[1, 0, 0, 0, 0, None, 1, 1]; False
[1, 0, 0, 0, 0, None, None, 0]; False
[1, 0, 0, 0, 0, None, None, 1]; False
[1, 0, 0, 0, 1, 0, 0, 0]; True
[1, 0, 0, 0, 1, 0, 0, 1]; False
[1, 0, 0, 0, 1, 0, 1, 0]; False
[1, 0, 0, 0, 1, 0, 1, 1]; False
[1, 0, 0, 0, 1, 0, None, 0]; False
[1, 0, 0, 0, 1, 0, None, 1]; False
[1, 0, 0, 0, 1, 1, 0, 0]; True
[1, 0, 0, 0, 1, 1, 0, 1]; False
[1, 0, 0, 0, 1, 1, 1, 0]; True
[1, 0, 0, 0, 1, 1, 1, 1]; False
[1, 0, 0, 0, 1, 1, None, 0]; True
[1, 0, 0, 0, 1, 1, None, 1]; False
[1, 0, 0, 0, 1, None, 0, 0]; True
[1, 0, 0, 0, 1, None, 0, 1]; False
[1, 0, 0, 0, 1, None, 1, 0]; True
[1, 0, 0, 0, 1, None, 1, 1]; False
[1, 0, 0, 0, 1, None, None, 0]; False
[1, 0, 0, 0, 1, None, None, 1]; False
[1, 0, 0, 0, None, 0, 0, 0]; True
[1, 0, 0, 0, None, 0, 0, 1]; False
[1, 0, 0, 0, None, 0, 1, 0]; False
[1, 0, 0, 0, None, 0, 1, 1]; False
[1, 0, 0, 0, None, 0, None, 0]; False
[1, 0, 0, 0, None, 0, None, 1]; False
[1, 0, 0, 0, None, 1, 0, 0]; True
[1, 0, 0, 0, None, 1, 0, 1]; False
[1, 0, 0, 0, None, 1, 1, 0]; True
[1, 0, 0, 0, None, 1, 1, 1]; False
[1, 0, 0, 0, None, 1, None, 0]; True
[1, 0, 0, 0, None, 1, None, 1]; False
[1, 0, 0, 0, None, None, 0, 0]; True
[1, 0, 0, 0, None, None, 0, 1]; False
[1, 0, 0, 0, None, None, 1, 0]; True
[1, 0, 0, 0, None, None, 1, 1]; False
[1, 0, 0, 0, None, None, None, 0]; False
[1, 0, 0, 0, None, None, None, 1]; False
[1, 0, 0, 1, 0, 0, 0, 0]; False
[1, 0, 0, 1, 0, 0, 0, 1]; False
[1, 0, 0, 1, 0, 0, 1, 0]; False
[1, 0, 0, 1, 0, 0, 1, 1]; False
[1, 0, 0, 1, 0, 0, None, 0]; False
[1, 0, 0, 1, 0, 0, None, 1]; False
[1, 0, 0, 1, 0, 1, 0, 0]; False
[1, 0, 0, 1, 0, 1, 0, 1]; False
[1, 0, 0, 1, 0, 1, 1, 0]; False
[1, 0, 0, 1, 0, 1, 1, 1]; False
[1, 0, 0, 1, 0, 1, None, 0]; False
[1, 0, 0, 1, 0, 1, None, 1]; False
[1, 0, 0, 1, 0, None, 0, 0]; False
[1, 0, 0, 1, 0, None, 0, 1]; False
[1, 0, 0, 1, 0, None, 1, 0]; False
[1, 0, 0, 1, 0, None, 1, 1]; False
[1, 0, 0, 1, 0, None, None, 0]; False
[1, 0, 0, 1, 0, None, None, 1]; False
[1, 0, 0, 1, 1, 0, 0, 0]; False
[1, 0, 0, 1, 1, 0, 0, 1]; False
[1, 0, 0, 1, 1, 0, 1, 0]; False
[1, 0, 0, 1, 1, 0, 1, 1]; False
[1, 0, 0, 1, 1, 0, None, 0]; False
[1, 0, 0, 1, 1, 0, None, 1]; False
[1, 0, 0, 1, 1, 1, 0, 0]; True
[1, 0, 0, 1, 1, 1, 0, 1]; False
[1, 0, 0, 1, 1, 1, 1, 0]; True
[1, 0, 0, 1, 1, 1, 1, 1]; False
[1, 0, 0, 1, 1, 1, None, 0]; True
[1, 0, 0, 1, 1, 1, None, 1]; False
[1, 0, 0, 1, 1, None, 0, 0]; True
[1, 0, 0, 1, 1, None, 0, 1]; False
[1, 0, 0, 1, 1, None, 1, 0]; True
[1, 0, 0, 1, 1, None, 1, 1]; False
[1, 0, 0, 1, 1, None, None, 0]; False
[1, 0, 0, 1, 1, None, None, 1]; False
[1, 0, 0, 1, None, 0, 0, 0]; False
[1, 0, 0, 1, None, 0, 0, 1]; False
[1, 0, 0, 1, None, 0, 1, 0]; False
[1, 0, 0, 1, None, 0, 1, 1]; False
[1, 0, 0, 1, None, 0, None, 0]; False
[1, 0, 0, 1, None, 0, None, 1]; False
[1, 0, 0, 1, None, 1, 0, 0]; True
[1, 0, 0, 1, None, 1, 0, 1]; False
[1, 0, 0, 1, None, 1, 1, 0]; True
[1, 0, 0, 1, None, 1, 1, 1]; False
[1, 0, 0, 1, None, 1, None, 0]; True
[1, 0, 0, 1, None, 1, None, 1]; False
[1, 0, 0, 1, None, None, 0, 0]; True
[1, 0, 0, 1, None, None, 0, 1]; False
[1, 0, 0, 1, None, None, 1, 0]; True
[1, 0, 0, 1, None, None, 1, 1]; False
[1, 0, 0, 1, None, None, None, 0]; False
[1, 0, 0, 1, None, None, None, 1]; False
[1, 0, 0, None, 0, 0, 0, 0]; False
[1, 0, 0, None, 0, 0, 0, 1]; False
[1, 0, 0, None, 0, 0, 1, 0]; False
[1, 0, 0, None, 0, 0, 1, 1]; False
[1, 0, 0, None, 0, 0, None, 0]; False
[1, 0, 0, None, 0, 0, None, 1]; False
[1, 0, 0, None, 0, 1, 0, 0]; False
[1, 0, 0, None, 0, 1, 0, 1]; False
[1, 0, 0, None, 0, 1, 1, 0]; False
[1, 0, 0, None, 0, 1, 1, 1]; False
[1, 0, 0, None, 0, 1, None, 0]; False
[1, 0, 0, None, 0, 1, None, 1]; False
[1, 0, 0, None, 0, None, 0, 0]; False
[1, 0, 0, None, 0, None, 0, 1]; False
[1, 0, 0, None, 0, None, 1, 0]; False
[1, 0, 0, None, 0, None, 1, 1]; False
[1, 0, 0, None, 0, None, None, 0]; False
[1, 0, 0, None, 0, None, None, 1]; False
[1, 0, 0, None, 1, 0, 0, 0]; False
[1, 0, 0, None, 1, 0, 0, 1]; False
[1, 0, 0, None, 1, 0, 1, 0]; False
[1, 0, 0, None, 1, 0, 1, 1]; False
[1, 0, 0, None, 1, 0, None, 0]; False
[1, 0, 0, None, 1, 0, None, 1]; False
[1, 0, 0, None, 1, 1, 0, 0]; False
[1, 0, 0, None, 1, 1, 0, 1]; False
[1, 0, 0, None, 1, 1, 1, 0]; False
[1, 0, 0, None, 1, 1, 1, 1]; False
[1, 0, 0, None, 1, 1, None, 0]; False
[1, 0, 0, None, 1, 1, None, 1]; False
[1, 0, 0, None, 1, None, 0, 0]; False
[1, 0, 0, None, 1, None, 0, 1]; False
[1, 0, 0, None, 1, None, 1, 0]; False
[1, 0, 0, None, 1, None, 1, 1]; False
[1, 0, 0, None, 1, None, None, 0]; False
[1, 0, 0, None, 1, None, None, 1]; False
[1, 0, 0, None, None, 0, 0, 0]; False
[1, 0, 0, None, None, 0, 0, 1]; False
[1, 0, 0, None, None, 0, 1, 0]; False
[1, 0, 0, None, None, 0, 1, 1]; False
[1, 0, 0, None, None, 0, None, 0]; False
[1, 0, 0, None, None, 0, None, 1]; False
[1, 0, 0, None, None, 1, 0, 0]; False
[1, 0, 0, None, None, 1, 0, 1]; False
[1, 0, 0, None, None, 1, 1, 0]; False
[1, 0, 0, None, None, 1, 1, 1]; True
[1, 0, 0, None, None, 1, None, 0]; False
[1, 0, 0, None, None, 1, None, 1]; True
[1, 0, 0, None, None, None, 0, 0]; False
[1, 0, 0, None, None, None, 0, 1]; False
[1, 0, 0, None, None, None, 1, 0]; False
[1, 0, 0, None, None, None, 1, 1]; True
[1, 0, 1, 0, 0, 0, 0, 0]; False
[1, 0, 1, 0, 0, 0, 0, 1]; False
[1, 0, 1, 0, 0, 0, 1, 0]; False
[1, 0, 1, 0, 0, 0, 1, 1]; False
[1, 0, 1, 0, 0, 0, None, 0]; False
[1, 0, 1, 0, 0, 0, None, 1]; False
[1, 0, 1, 0, 0, 1, 0, 0]; False
[1, 0, 1, 0, 0, 1, 0, 1]; False
[1, 0, 1, 0, 0, 1, 1, 0]; False
[1, 0, 1, 0, 0, 1, 1, 1]; False
[1, 0, 1, 0, 0, 1, None, 0]; False
[1, 0, 1, 0, 0, 1, None, 1]; False
[1, 0, 1, 0, 0, None, 0, 0]; False
[1, 0, 1, 0, 0, None, 0, 1]; False
[1, 0, 1, 0, 0, None, 1, 0]; False
[1, 0, 1, 0, 0, None, 1, 1]; False
[1, 0, 1, 0, 0, None, None, 0]; False
[1, 0, 1, 0, 0, None, None, 1]; False
[1, 0, 1, 0, 1, 0, 0, 0]; True
[1, 0, 1, 0, 1, 0, 0, 1]; False
[1, 0, 1, 0, 1, 0, 1, 0]; False
[1, 0, 1, 0, 1, 0, 1, 1]; False
[1, 0, 1, 0, 1, 0, None, 0]; False
[1, 0, 1, 0, 1, 0, None, 1]; False
[1, 0, 1, 0, 1, 1, 0, 0]; True
[1, 0, 1, 0, 1, 1, 0, 1]; False
[1, 0, 1, 0, 1, 1, 1, 0]; True
[1, 0, 1, 0, 1, 1, 1, 1]; False
[1, 0, 1, 0, 1, 1, None, 0]; True
[1, 0, 1, 0, 1, 1, None, 1]; False
[1, 0, 1, 0, 1, None, 0, 0]; True
[1, 0, 1, 0, 1, None, 0, 1]; False
[1, 0, 1, 0, 1, None, 1, 0]; True
[1, 0, 1, 0, 1, None, 1, 1]; False
[1, 0, 1, 0, 1, None, None, 0]; True
[1, 0, 1, 0, 1, None, None, 1]; False
[1, 0, 1, 0, None, 0, 0, 0]; True
[1, 0, 1, 0, None, 0, 0, 1]; False
[1, 0, 1, 0, None, 0, 1, 0]; False
[1, 0, 1, 0, None, 0, 1, 1]; False
[1, 0, 1, 0, None, 0, None, 0]; False
[1, 0, 1, 0, None, 0, None, 1]; False
[1, 0, 1, 0, None, 1, 0, 0]; True
[1, 0, 1, 0, None, 1, 0, 1]; False
[1, 0, 1, 0, None, 1, 1, 0]; True
[1, 0, 1, 0, None, 1, 1, 1]; False
[1, 0, 1, 0, None, 1, None, 0]; True
[1, 0, 1, 0, None, 1, None, 1]; False
[1, 0, 1, 0, None, None, 0, 0]; True
[1, 0, 1, 0, None, None, 0, 1]; False
[1, 0, 1, 0, None, None, 1, 0]; True
[1, 0, 1, 0, None, None, 1, 1]; False
[1, 0, 1, 0, None, None, None, 0]; True
[1, 0, 1, 0, None, None, None, 1]; False
[1, 0, 1, 1, 0, 0, 0, 0]; False
[1, 0, 1, 1, 0, 0, 0, 1]; False
[1, 0, 1, 1, 0, 0, 1, 0]; False
[1, 0, 1, 1, 0, 0, 1, 1]; False
[1, 0, 1, 1, 0, 0, None, 0]; False
[1, 0, 1, 1, 0, 0, None, 1]; False
[1, 0, 1, 1, 0, 1, 0, 0]; False
[1, 0, 1, 1, 0, 1, 0, 1]; False
[1, 0, 1, 1, 0, 1, 1, 0]; False
[1, 0, 1, 1, 0, 1, 1, 1]; False
[1, 0, 1, 1, 0, 1, None, 0]; False
[1, 0, 1, 1, 0, 1, None, 1]; False
[1, 0, 1, 1, 0, None, 0, 0]; False
[1, 0, 1, 1, 0, None, 0, 1]; False
[1, 0, 1, 1, 0, None, 1, 0]; False
[1, 0, 1, 1, 0, None, 1, 1]; False
[1, 0, 1, 1, 0, None, None, 0]; False
[1, 0, 1, 1, 0, None, None, 1]; False
[1, 0, 1, 1, 1, 0, 0, 0]; True
[1, 0, 1, 1, 1, 0, 0, 1]; False
[1, 0, 1, 1, 1, 0, 1, 0]; False
[1, 0, 1, 1, 1, 0, 1, 1]; False
[1, 0, 1, 1, 1, 0, None, 0]; False
[1, 0, 1, 1, 1, 0, None, 1]; False
[1, 0, 1, 1, 1, 1, 0, 0]; True
[1, 0, 1, 1, 1, 1, 0, 1]; False
[1, 0, 1, 1, 1, 1, 1, 0]; True
[1, 0, 1, 1, 1, 1, 1, 1]; False
[1, 0, 1, 1, 1, 1, None, 0]; True
[1, 0, 1, 1, 1, 1, None, 1]; False
[1, 0, 1, 1, 1, None, 0, 0]; True
[1, 0, 1, 1, 1, None, 0, 1]; False
[1, 0, 1, 1, 1, None, 1, 0]; True
[1, 0, 1, 1, 1, None, 1, 1]; False
[1, 0, 1, 1, 1, None, None, 0]; True
[1, 0, 1, 1, 1, None, None, 1]; False
[1, 0, 1, 1, None, 0, 0, 0]; True
[1, 0, 1, 1, None, 0, 0, 1]; False
[1, 0, 1, 1, None, 0, 1, 0]; False
[1, 0, 1, 1, None, 0, 1, 1]; False
[1, 0, 1, 1, None, 0, None, 0]; False
[1, 0, 1, 1, None, 0, None, 1]; False
[1, 0, 1, 1, None, 1, 0, 0]; True
[1, 0, 1, 1, None, 1, 0, 1]; False
[1, 0, 1, 1, None, 1, 1, 0]; True
[1, 0, 1, 1, None, 1, 1, 1]; False
[1, 0, 1, 1, None, 1, None, 0]; True
[1, 0, 1, 1, None, 1, None, 1]; False
[1, 0, 1, 1, None, None, 0, 0]; True
[1, 0, 1, 1, None, None, 0, 1]; False
[1, 0, 1, 1, None, None, 1, 0]; True
[1, 0, 1, 1, None, None, 1, 1]; False
[1, 0, 1, 1, None, None, None, 0]; True
[1, 0, 1, 1, None, None, None, 1]; False
[1, 0, 1, None, 0, 0, 0, 0]; False
[1, 0, 1, None, 0, 0, 0, 1]; False
[1, 0, 1, None, 0, 0, 1, 0]; False
[1, 0, 1, None, 0, 0, 1, 1]; False
[1, 0, 1, None, 0, 0, None, 0]; False
[1, 0, 1, None, 0, 0, None, 1]; False
[1, 0, 1, None, 0, 1, 0, 0]; False
[1, 0, 1, None, 0, 1, 0, 1]; False
[1, 0, 1, None, 0, 1, 1, 0]; False
[1, 0, 1, None, 0, 1, 1, 1]; False
[1, 0, 1, None, 0, 1, None, 0]; False
[1, 0, 1, None, 0, 1, None, 1]; False
[1, 0, 1, None, 0, None, 0, 0]; False
[1, 0, 1, None, 0, None, 0, 1]; False
[1, 0, 1, None, 0, None, 1, 0]; False
[1, 0, 1, None, 0, None, 1, 1]; False
[1, 0, 1, None, 0, None, None, 0]; False
[1, 0, 1, None, 0, None, None, 1]; False
[1, 0, 1, None, 1, 0, 0, 0]; False
[1, 0, 1, None, 1, 0, 0, 1]; False
[1, 0, 1, None, 1, 0, 1, 0]; False
[1, 0, 1, None, 1, 0, 1, 1]; False
[1, 0, 1, None, 1, 0, None, 0]; False
[1, 0, 1, None, 1, 0, None, 1]; False
[1, 0, 1, None, 1, 1, 0, 0]; False
[1, 0, 1, None, 1, 1, 0, 1]; False
[1, 0, 1, None, 1, 1, 1, 0]; False
[1, 0, 1, None, 1, 1, 1, 1]; False
[1, 0, 1, None, 1, 1, None, 0]; False
[1, 0, 1, None, 1, 1, None, 1]; False
[1, 0, 1, None, 1, None, 0, 0]; False
[1, 0, 1, None, 1, None, 0, 1]; False
[1, 0, 1, None, 1, None, 1, 0]; False
[1, 0, 1, None, 1, None, 1, 1]; False
[1, 0, 1, None, 1, None, None, 0]; False
[1, 0, 1, None, 1, None, None, 1]; False
[1, 0, 1, None, None, 0, 0, 0]; False
[1, 0, 1, None, None, 0, 0, 1]; False
[1, 0, 1, None, None, 0, 1, 0]; False
[1, 0, 1, None, None, 0, 1, 1]; True
[1, 0, 1, None, None, 0, None, 0]; False
[1, 0, 1, None, None, 0, None, 1]; True
[1, 0, 1, None, None, 1, 0, 0]; False
[1, 0, 1, None, None, 1, 0, 1]; True
[1, 0, 1, None, None, 1, 1, 0]; False
[1, 0, 1, None, None, 1, 1, 1]; True
[1, 0, 1, None, None, 1, None, 0]; False
[1, 0, 1, None, None, 1, None, 1]; True
[1, 0, 1, None, None, None, 0, 0]; False
[1, 0, 1, None, None, None, 0, 1]; True
[1, 0, 1, None, None, None, 1, 0]; True
[1, 0, 1, None, None, None, 1, 1]; True
[1, 0, None, 0, 0, 0, 0, 0]; False
[1, 0, None, 0, 0, 0, 0, 1]; False
[1, 0, None, 0, 0, 0, 1, 0]; False
[1, 0, None, 0, 0, 0, 1, 1]; True
[1, 0, None, 0, 0, 0, None, 0]; False
[1, 0, None, 0, 0, 0, None, 1]; True
[1, 0, None, 0, 0, 1, 0, 0]; False
[1, 0, None, 0, 0, 1, 0, 1]; False
[1, 0, None, 0, 0, 1, 1, 0]; False
[1, 0, None, 0, 0, 1, 1, 1]; False
[1, 0, None, 0, 0, 1, None, 0]; False
[1, 0, None, 0, 0, 1, None, 1]; False
[1, 0, None, 0, 0, None, 0, 0]; False
[1, 0, None, 0, 0, None, 0, 1]; False
[1, 0, None, 0, 0, None, 1, 0]; False
[1, 0, None, 0, 0, None, 1, 1]; False
[1, 0, None, 0, 0, None, None, 0]; False
[1, 0, None, 0, 0, None, None, 1]; True
[1, 0, None, 0, 1, 0, 0, 0]; False
[1, 0, None, 0, 1, 0, 0, 1]; False
[1, 0, None, 0, 1, 0, 1, 0]; False
[1, 0, None, 0, 1, 0, 1, 1]; True
[1, 0, None, 0, 1, 0, None, 0]; False
[1, 0, None, 0, 1, 0, None, 1]; True
[1, 0, None, 0, 1, 1, 0, 0]; False
[1, 0, None, 0, 1, 1, 0, 1]; False
[1, 0, None, 0, 1, 1, 1, 0]; False
[1, 0, None, 0, 1, 1, 1, 1]; False
[1, 0, None, 0, 1, 1, None, 0]; False
[1, 0, None, 0, 1, 1, None, 1]; False
[1, 0, None, 0, 1, None, 0, 0]; False
[1, 0, None, 0, 1, None, 0, 1]; False
[1, 0, None, 0, 1, None, 1, 0]; False
[1, 0, None, 0, 1, None, 1, 1]; False
[1, 0, None, 0, 1, None, None, 0]; False
[1, 0, None, 0, 1, None, None, 1]; True
[1, 0, None, 0, None, 0, 0, 0]; False
[1, 0, None, 0, None, 0, 0, 1]; False
[1, 0, None, 0, None, 0, 1, 0]; True
[1, 0, None, 0, None, 0, 1, 1]; False
[1, 0, None, 0, None, 0, None, 0]; True
[1, 0, None, 0, None, 0, None, 1]; False
[1, 0, None, 0, None, 1, 0, 0]; False
[1, 0, None, 0, None, 1, 0, 1]; False
[1, 0, None, 0, None, 1, 1, 0]; True
[1, 0, None, 0, None, 1, 1, 1]; False
[1, 0, None, 0, None, 1, None, 0]; True
[1, 0, None, 0, None, 1, None, 1]; False
[1, 0, None, 0, None, None, 0, 0]; False
[1, 0, None, 0, None, None, 0, 1]; False
[1, 0, None, 0, None, None, 1, 0]; False
[1, 0, None, 0, None, None, 1, 1]; False
[1, 0, None, 1, 0, 0, 0, 0]; False
[1, 0, None, 1, 0, 0, 0, 1]; False
[1, 0, None, 1, 0, 0, 1, 0]; False
[1, 0, None, 1, 0, 0, 1, 1]; True
[1, 0, None, 1, 0, 0, None, 0]; False
[1, 0, None, 1, 0, 0, None, 1]; True
[1, 0, None, 1, 0, 1, 0, 0]; False
[1, 0, None, 1, 0, 1, 0, 1]; False
[1, 0, None, 1, 0, 1, 1, 0]; False
[1, 0, None, 1, 0, 1, 1, 1]; False
[1, 0, None, 1, 0, 1, None, 0]; False
[1, 0, None, 1, 0, 1, None, 1]; False
[1, 0, None, 1, 0, None, 0, 0]; False
[1, 0, None, 1, 0, None, 0, 1]; False
[1, 0, None, 1, 0, None, 1, 0]; False
[1, 0, None, 1, 0, None, 1, 1]; False
[1, 0, None, 1, 0, None, None, 0]; False
[1, 0, None, 1, 0, None, None, 1]; False
[1, 0, None, 1, 1, 0, 0, 0]; False
[1, 0, None, 1, 1, 0, 0, 1]; False
[1, 0, None, 1, 1, 0, 1, 0]; False
[1, 0, None, 1, 1, 0, 1, 1]; True
[1, 0, None, 1, 1, 0, None, 0]; False
[1, 0, None, 1, 1, 0, None, 1]; True
[1, 0, None, 1, 1, 1, 0, 0]; False
[1, 0, None, 1, 1, 1, 0, 1]; False
[1, 0, None, 1, 1, 1, 1, 0]; False
[1, 0, None, 1, 1, 1, 1, 1]; False
[1, 0, None, 1, 1, 1, None, 0]; False
[1, 0, None, 1, 1, 1, None, 1]; False
[1, 0, None, 1, 1, None, 0, 0]; False
[1, 0, None, 1, 1, None, 0, 1]; False
[1, 0, None, 1, 1, None, 1, 0]; False
[1, 0, None, 1, 1, None, 1, 1]; False
[1, 0, None, 1, 1, None, None, 0]; False
[1, 0, None, 1, 1, None, None, 1]; False
[1, 0, None, 1, None, 0, 0, 0]; False
[1, 0, None, 1, None, 0, 0, 1]; False
[1, 0, None, 1, None, 0, 1, 0]; True
[1, 0, None, 1, None, 0, 1, 1]; False
[1, 0, None, 1, None, 0, None, 0]; True
[1, 0, None, 1, None, 0, None, 1]; False
[1, 0, None, 1, None, 1, 0, 0]; False
[1, 0, None, 1, None, 1, 0, 1]; False
[1, 0, None, 1, None, 1, 1, 0]; True
[1, 0, None, 1, None, 1, 1, 1]; False
[1, 0, None, 1, None, 1, None, 0]; True
[1, 0, None, 1, None, 1, None, 1]; False
[1, 0, None, 1, None, None, 0, 0]; False
[1, 0, None, 1, None, None, 0, 1]; False
[1, 0, None, 1, None, None, 1, 0]; False
[1, 0, None, 1, None, None, 1, 1]; False
[1, 0, None, None, 0, 0, 0, 0]; False
[1, 0, None, None, 0, 0, 0, 1]; False
[1, 0, None, None, 0, 0, 1, 0]; False
[1, 0, None, None, 0, 0, 1, 1]; False
[1, 0, None, None, 0, 0, None, 0]; False
[1, 0, None, None, 0, 0, None, 1]; False
[1, 0, None, None, 0, 1, 0, 0]; False
[1, 0, None, None, 0, 1, 0, 1]; False
[1, 0, None, None, 0, 1, 1, 0]; False
[1, 0, None, None, 0, 1, 1, 1]; False
[1, 0, None, None, 0, 1, None, 0]; False
[1, 0, None, None, 0, 1, None, 1]; False
[1, 0, None, None, 0, None, 0, 0]; False
[1, 0, None, None, 0, None, 0, 1]; False
[1, 0, None, None, 0, None, 1, 0]; False
[1, 0, None, None, 0, None, 1, 1]; False
[1, 0, None, None, 1, 0, 0, 0]; False
[1, 0, None, None, 1, 0, 0, 1]; False
[1, 0, None, None, 1, 0, 1, 0]; False
[1, 0, None, None, 1, 0, 1, 1]; False
[1, 0, None, None, 1, 0, None, 0]; False
[1, 0, None, None, 1, 0, None, 1]; False
[1, 0, None, None, 1, 1, 0, 0]; False
[1, 0, None, None, 1, 1, 0, 1]; False
[1, 0, None, None, 1, 1, 1, 0]; False
[1, 0, None, None, 1, 1, 1, 1]; False
[1, 0, None, None, 1, 1, None, 0]; False
[1, 0, None, None, 1, 1, None, 1]; False
[1, 0, None, None, 1, None, 0, 0]; False
[1, 0, None, None, 1, None, 0, 1]; False
[1, 0, None, None, 1, None, 1, 0]; False
[1, 0, None, None, 1, None, 1, 1]; False
[1, 1, 0, 0, 0, 0, 0, 0]; False
[1, 1, 0, 0, 0, 0, 0, 1]; False
[1, 1, 0, 0, 0, 0, 1, 0]; False
[1, 1, 0, 0, 0, 0, 1, 1]; False
[1, 1, 0, 0, 0, 0, None, 0]; False
[1, 1, 0, 0, 0, 0, None, 1]; False
[1, 1, 0, 0, 0, 1, 0, 0]; False
[1, 1, 0, 0, 0, 1, 0, 1]; False
[1, 1, 0, 0, 0, 1, 1, 0]; False
[1, 1, 0, 0, 0, 1, 1, 1]; False
[1, 1, 0, 0, 0, 1, None, 0]; False
[1, 1, 0, 0, 0, 1, None, 1]; False
[1, 1, 0, 0, 0, None, 0, 0]; False
[1, 1, 0, 0, 0, None, 0, 1]; False
[1, 1, 0, 0, 0, None, 1, 0]; False
[1, 1, 0, 0, 0, None, 1, 1]; False
[1, 1, 0, 0, 0, None, None, 0]; False
[1, 1, 0, 0, 0, None, None, 1]; False
[1, 1, 0, 0, 1, 0, 0, 0]; False
[1, 1, 0, 0, 1, 0, 0, 1]; False
[1, 1, 0, 0, 1, 0, 1, 0]; False
[1, 1, 0, 0, 1, 0, 1, 1]; False
[1, 1, 0, 0, 1, 0, None, 0]; False
[1, 1, 0, 0, 1, 0, None, 1]; False
[1, 1, 0, 0, 1, 1, 0, 0]; True
[1, 1, 0, 0, 1, 1, 0, 1]; False
[1, 1, 0, 0, 1, 1, 1, 0]; True
[1, 1, 0, 0, 1, 1, 1, 1]; False
[1, 1, 0, 0, 1, 1, None, 0]; True
[1, 1, 0, 0, 1, 1, None, 1]; False
[1, 1, 0, 0, 1, None, 0, 0]; True
[1, 1, 0, 0, 1, None, 0, 1]; False
[1, 1, 0, 0, 1, None, 1, 0]; True
[1, 1, 0, 0, 1, None, 1, 1]; False
[1, 1, 0, 0, 1, None, None, 0]; False
[1, 1, 0, 0, 1, None, None, 1]; False
[1, 1, 0, 0, None, 0, 0, 0]; False
[1, 1, 0, 0, None, 0, 0, 1]; False
[1, 1, 0, 0, None, 0, 1, 0]; False
[1, 1, 0, 0, None, 0, 1, 1]; False
[1, 1, 0, 0, None, 0, None, 0]; False
[1, 1, 0, 0, None, 0, None, 1]; False
[1, 1, 0, 0, None, 1, 0, 0]; True
[1, 1, 0, 0, None, 1, 0, 1]; False
[1, 1, 0, 0, None, 1, 1, 0]; True
[1, 1, 0, 0, None, 1, 1, 1]; False
[1, 1, 0, 0, None, 1, None, 0]; True
[1, 1, 0, 0, None, 1, None, 1]; False
[1, 1, 0, 0, None, None, 0, 0]; True
[1, 1, 0, 0, None, None, 0, 1]; False
[1, 1, 0, 0, None, None, 1, 0]; True
[1, 1, 0, 0, None, None, 1, 1]; False
[1, 1, 0, 0, None, None, None, 0]; False
[1, 1, 0, 0, None, None, None, 1]; False
[1, 1, 0, 1, 0, 0, 0, 0]; False
[1, 1, 0, 1, 0, 0, 0, 1]; False
[1, 1, 0, 1, 0, 0, 1, 0]; False
[1, 1, 0, 1, 0, 0, 1, 1]; False
[1, 1, 0, 1, 0, 0, None, 0]; False
[1, 1, 0, 1, 0, 0, None, 1]; False
[1, 1, 0, 1, 0, 1, 0, 0]; False
[1, 1, 0, 1, 0, 1, 0, 1]; False
[1, 1, 0, 1, 0, 1, 1, 0]; False
[1, 1, 0, 1, 0, 1, 1, 1]; False
[1, 1, 0, 1, 0, 1, None, 0]; False
[1, 1, 0, 1, 0, 1, None, 1]; False
[1, 1, 0, 1, 0, None, 0, 0]; False
[1, 1, 0, 1, 0, None, 0, 1]; False
[1, 1, 0, 1, 0, None, 1, 0]; False
[1, 1, 0, 1, 0, None, 1, 1]; False
[1, 1, 0, 1, 0, None, None, 0]; False
[1, 1, 0, 1, 0, None, None, 1]; False
[1, 1, 0, 1, 1, 0, 0, 0]; False
[1, 1, 0, 1, 1, 0, 0, 1]; False
[1, 1, 0, 1, 1, 0, 1, 0]; False
[1, 1, 0, 1, 1, 0, 1, 1]; False
[1, 1, 0, 1, 1, 0, None, 0]; False
[1, 1, 0, 1, 1, 0, None, 1]; False
[1, 1, 0, 1, 1, 1, 0, 0]; False
[1, 1, 0, 1, 1, 1, 0, 1]; False
[1, 1, 0, 1, 1, 1, 1, 0]; True
[1, 1, 0, 1, 1, 1, 1, 1]; False
[1, 1, 0, 1, 1, 1, None, 0]; True
[1, 1, 0, 1, 1, 1, None, 1]; False
[1, 1, 0, 1, 1, None, 0, 0]; False
[1, 1, 0, 1, 1, None, 0, 1]; False
[1, 1, 0, 1, 1, None, 1, 0]; True
[1, 1, 0, 1, 1, None, 1, 1]; False
[1, 1, 0, 1, 1, None, None, 0]; False
[1, 1, 0, 1, 1, None, None, 1]; False
[1, 1, 0, 1, None, 0, 0, 0]; False
[1, 1, 0, 1, None, 0, 0, 1]; False
[1, 1, 0, 1, None, 0, 1, 0]; False
[1, 1, 0, 1, None, 0, 1, 1]; False
[1, 1, 0, 1, None, 0, None, 0]; False
[1, 1, 0, 1, None, 0, None, 1]; False
[1, 1, 0, 1, None, 1, 0, 0]; False
[1, 1, 0, 1, None, 1, 0, 1]; False
[1, 1, 0, 1, None, 1, 1, 0]; True
[1, 1, 0, 1, None, 1, 1, 1]; False
[1, 1, 0, 1, None, 1, None, 0]; True
[1, 1, 0, 1, None, 1, None, 1]; False
[1, 1, 0, 1, None, None, 0, 0]; False
[1, 1, 0, 1, None, None, 0, 1]; False
[1, 1, 0, 1, None, None, 1, 0]; True
[1, 1, 0, 1, None, None, 1, 1]; False
[1, 1, 0, 1, None, None, None, 0]; False
[1, 1, 0, 1, None, None, None, 1]; False
[1, 1, 0, None, 0, 0, 0, 0]; False
[1, 1, 0, None, 0, 0, 0, 1]; False
[1, 1, 0, None, 0, 0, 1, 0]; False
[1, 1, 0, None, 0, 0, 1, 1]; False
[1, 1, 0, None, 0, 0, None, 0]; False
[1, 1, 0, None, 0, 0, None, 1]; False
[1, 1, 0, None, 0, 1, 0, 0]; False
[1, 1, 0, None, 0, 1, 0, 1]; False
[1, 1, 0, None, 0, 1, 1, 0]; False
[1, 1, 0, None, 0, 1, 1, 1]; False
[1, 1, 0, None, 0, 1, None, 0]; False
[1, 1, 0, None, 0, 1, None, 1]; False
[1, 1, 0, None, 0, None, 0, 0]; False
[1, 1, 0, None, 0, None, 0, 1]; False
[1, 1, 0, None, 0, None, 1, 0]; False
[1, 1, 0, None, 0, None, 1, 1]; False
[1, 1, 0, None, 0, None, None, 0]; False
[1, 1, 0, None, 0, None, None, 1]; False
[1, 1, 0, None, 1, 0, 0, 0]; False
[1, 1, 0, None, 1, 0, 0, 1]; False
[1, 1, 0, None, 1, 0, 1, 0]; False
[1, 1, 0, None, 1, 0, 1, 1]; False
[1, 1, 0, None, 1, 0, None, 0]; False
[1, 1, 0, None, 1, 0, None, 1]; False
[1, 1, 0, None, 1, 1, 0, 0]; False
[1, 1, 0, None, 1, 1, 0, 1]; False
[1, 1, 0, None, 1, 1, 1, 0]; False
[1, 1, 0, None, 1, 1, 1, 1]; False
[1, 1, 0, None, 1, 1, None, 0]; False
[1, 1, 0, None, 1, 1, None, 1]; False
[1, 1, 0, None, 1, None, 0, 0]; False
[1, 1, 0, None, 1, None, 0, 1]; False
[1, 1, 0, None, 1, None, 1, 0]; False
[1, 1, 0, None, 1, None, 1, 1]; False
[1, 1, 0, None, 1, None, None, 0]; False
[1, 1, 0, None, 1, None, None, 1]; False
[1, 1, 0, None, None, 0, 0, 0]; False
[1, 1, 0, None, None, 0, 0, 1]; False
[1, 1, 0, None, None, 0, 1, 0]; False
[1, 1, 0, None, None, 0, 1, 1]; False
[1, 1, 0, None, None, 0, None, 0]; False
[1, 1, 0, None, None, 0, None, 1]; False
[1, 1, 0, None, None, 1, 0, 0]; False
[1, 1, 0, None, None, 1, 0, 1]; False
[1, 1, 0, None, None, 1, 1, 0]; False
[1, 1, 0, None, None, 1, 1, 1]; False
[1, 1, 0, None, None, 1, None, 0]; False
[1, 1, 0, None, None, 1, None, 1]; False
[1, 1, 0, None, None, None, 0, 0]; False
[1, 1, 0, None, None, None, 0, 1]; False
[1, 1, 0, None, None, None, 1, 0]; False
[1, 1, 0, None, None, None, 1, 1]; False
[1, 1, 1, 0, 0, 0, 0, 0]; False
[1, 1, 1, 0, 0, 0, 0, 1]; False
[1, 1, 1, 0, 0, 0, 1, 0]; False
[1, 1, 1, 0, 0, 0, 1, 1]; False
[1, 1, 1, 0, 0, 0, None, 0]; False
[1, 1, 1, 0, 0, 0, None, 1]; False
[1, 1, 1, 0, 0, 1, 0, 0]; False
[1, 1, 1, 0, 0, 1, 0, 1]; False
[1, 1, 1, 0, 0, 1, 1, 0]; False
[1, 1, 1, 0, 0, 1, 1, 1]; False
[1, 1, 1, 0, 0, 1, None, 0]; False
[1, 1, 1, 0, 0, 1, None, 1]; False
[1, 1, 1, 0, 0, None, 0, 0]; False
[1, 1, 1, 0, 0, None, 0, 1]; False
[1, 1, 1, 0, 0, None, 1, 0]; False
[1, 1, 1, 0, 0, None, 1, 1]; False
[1, 1, 1, 0, 0, None, None, 0]; False
[1, 1, 1, 0, 0, None, None, 1]; False
[1, 1, 1, 0, 1, 0, 0, 0]; True
[1, 1, 1, 0, 1, 0, 0, 1]; False
[1, 1, 1, 0, 1, 0, 1, 0]; False
[1, 1, 1, 0, 1, 0, 1, 1]; False
[1, 1, 1, 0, 1, 0, None, 0]; False
[1, 1, 1, 0, 1, 0, None, 1]; False
[1, 1, 1, 0, 1, 1, 0, 0]; True
[1, 1, 1, 0, 1, 1, 0, 1]; False
[1, 1, 1, 0, 1, 1, 1, 0]; True
[1, 1, 1, 0, 1, 1, 1, 1]; False
[1, 1, 1, 0, 1, 1, None, 0]; True
[1, 1, 1, 0, 1, 1, None, 1]; False
[1, 1, 1, 0, 1, None, 0, 0]; True
[1, 1, 1, 0, 1, None, 0, 1]; False
[1, 1, 1, 0, 1, None, 1, 0]; True
[1, 1, 1, 0, 1, None, 1, 1]; False
[1, 1, 1, 0, 1, None, None, 0]; True
[1, 1, 1, 0, 1, None, None, 1]; False
[1, 1, 1, 0, None, 0, 0, 0]; True
[1, 1, 1, 0, None, 0, 0, 1]; False
[1, 1, 1, 0, None, 0, 1, 0]; False
[1, 1, 1, 0, None, 0, 1, 1]; False
[1, 1, 1, 0, None, 0, None, 0]; False
[1, 1, 1, 0, None, 0, None, 1]; False
[1, 1, 1, 0, None, 1, 0, 0]; True
[1, 1, 1, 0, None, 1, 0, 1]; False
[1, 1, 1, 0, None, 1, 1, 0]; True
[1, 1, 1, 0, None, 1, 1, 1]; False
[1, 1, 1, 0, None, 1, None, 0]; True
[1, 1, 1, 0, None, 1, None, 1]; False
[1, 1, 1, 0, None, None, 0, 0]; True
[1, 1, 1, 0, None, None, 0, 1]; False
[1, 1, 1, 0, None, None, 1, 0]; True
[1, 1, 1, 0, None, None, 1, 1]; False
[1, 1, 1, 0, None, None, None, 0]; True
[1, 1, 1, 0, None, None, None, 1]; False
[1, 1, 1, 1, 0, 0, 0, 0]; False
[1, 1, 1, 1, 0, 0, 0, 1]; False
[1, 1, 1, 1, 0, 0, 1, 0]; False
[1, 1, 1, 1, 0, 0, 1, 1]; False
[1, 1, 1, 1, 0, 0, None, 0]; False
[1, 1, 1, 1, 0, 0, None, 1]; False
[1, 1, 1, 1, 0, 1, 0, 0]; False
[1, 1, 1, 1, 0, 1, 0, 1]; False
[1, 1, 1, 1, 0, 1, 1, 0]; False
[1, 1, 1, 1, 0, 1, 1, 1]; False
[1, 1, 1, 1, 0, 1, None, 0]; False
[1, 1, 1, 1, 0, 1, None, 1]; False
[1, 1, 1, 1, 0, None, 0, 0]; False
[1, 1, 1, 1, 0, None, 0, 1]; False
[1, 1, 1, 1, 0, None, 1, 0]; False
[1, 1, 1, 1, 0, None, 1, 1]; False
[1, 1, 1, 1, 0, None, None, 0]; False
[1, 1, 1, 1, 0, None, None, 1]; False
[1, 1, 1, 1, 1, 0, 0, 0]; False
[1, 1, 1, 1, 1, 0, 0, 1]; False
[1, 1, 1, 1, 1, 0, 1, 0]; False
[1, 1, 1, 1, 1, 0, 1, 1]; False
[1, 1, 1, 1, 1, 0, None, 0]; False
[1, 1, 1, 1, 1, 0, None, 1]; False
[1, 1, 1, 1, 1, 1, 0, 0]; True
[1, 1, 1, 1, 1, 1, 0, 1]; False
[1, 1, 1, 1, 1, 1, 1, 0]; True
[1, 1, 1, 1, 1, 1, 1, 1]; False
[1, 1, 1, 1, 1, 1, None, 0]; True
[1, 1, 1, 1, 1, 1, None, 1]; False
[1, 1, 1, 1, 1, None, 0, 0]; True
[1, 1, 1, 1, 1, None, 0, 1]; False
[1, 1, 1, 1, 1, None, 1, 0]; True
[1, 1, 1, 1, 1, None, 1, 1]; False
[1, 1, 1, 1, 1, None, None, 0]; True
[1, 1, 1, 1, 1, None, None, 1]; False
[1, 1, 1, 1, None, 0, 0, 0]; False
[1, 1, 1, 1, None, 0, 0, 1]; False
[1, 1, 1, 1, None, 0, 1, 0]; False
[1, 1, 1, 1, None, 0, 1, 1]; False
[1, 1, 1, 1, None, 0, None, 0]; False
[1, 1, 1, 1, None, 0, None, 1]; False
[1, 1, 1, 1, None, 1, 0, 0]; True
[1, 1, 1, 1, None, 1, 0, 1]; False
[1, 1, 1, 1, None, 1, 1, 0]; True
[1, 1, 1, 1, None, 1, 1, 1]; False
[1, 1, 1, 1, None, 1, None, 0]; True
[1, 1, 1, 1, None, 1, None, 1]; False
[1, 1, 1, 1, None, None, 0, 0]; True
[1, 1, 1, 1, None, None, 0, 1]; False
[1, 1, 1, 1, None, None, 1, 0]; True
[1, 1, 1, 1, None, None, 1, 1]; False
[1, 1, 1, 1, None, None, None, 0]; True
[1, 1, 1, 1, None, None, None, 1]; False
[1, 1, 1, None, 0, 0, 0, 0]; False
[1, 1, 1, None, 0, 0, 0, 1]; False
[1, 1, 1, None, 0, 0, 1, 0]; False
[1, 1, 1, None, 0, 0, 1, 1]; False
[1, 1, 1, None, 0, 0, None, 0]; False
[1, 1, 1, None, 0, 0, None, 1]; False
[1, 1, 1, None, 0, 1, 0, 0]; False
[1, 1, 1, None, 0, 1, 0, 1]; False
[1, 1, 1, None, 0, 1, 1, 0]; False
[1, 1, 1, None, 0, 1, 1, 1]; False
[1, 1, 1, None, 0, 1, None, 0]; False
[1, 1, 1, None, 0, 1, None, 1]; False
[1, 1, 1, None, 0, None, 0, 0]; False
[1, 1, 1, None, 0, None, 0, 1]; False
[1, 1, 1, None, 0, None, 1, 0]; False
[1, 1, 1, None, 0, None, 1, 1]; False
[1, 1, 1, None, 0, None, None, 0]; False
[1, 1, 1, None, 0, None, None, 1]; False
[1, 1, 1, None, 1, 0, 0, 0]; False
[1, 1, 1, None, 1, 0, 0, 1]; False
[1, 1, 1, None, 1, 0, 1, 0]; False
[1, 1, 1, None, 1, 0, 1, 1]; False
[1, 1, 1, None, 1, 0, None, 0]; False
[1, 1, 1, None, 1, 0, None, 1]; False
[1, 1, 1, None, 1, 1, 0, 0]; False
[1, 1, 1, None, 1, 1, 0, 1]; False
[1, 1, 1, None, 1, 1, 1, 0]; False
[1, 1, 1, None, 1, 1, 1, 1]; False
[1, 1, 1, None, 1, 1, None, 0]; False
[1, 1, 1, None, 1, 1, None, 1]; False
[1, 1, 1, None, 1, None, 0, 0]; False
[1, 1, 1, None, 1, None, 0, 1]; False
[1, 1, 1, None, 1, None, 1, 0]; False
[1, 1, 1, None, 1, None, 1, 1]; False
[1, 1, 1, None, 1, None, None, 0]; False
[1, 1, 1, None, 1, None, None, 1]; False
[1, 1, 1, None, None, 0, 0, 0]; False
[1, 1, 1, None, None, 0, 0, 1]; False
[1, 1, 1, None, None, 0, 1, 0]; False
[1, 1, 1, None, None, 0, 1, 1]; False
[1, 1, 1, None, None, 0, None, 0]; False
[1, 1, 1, None, None, 0, None, 1]; False
[1, 1, 1, None, None, 1, 0, 0]; False
[1, 1, 1, None, None, 1, 0, 1]; False
[1, 1, 1, None, None, 1, 1, 0]; False
[1, 1, 1, None, None, 1, 1, 1]; False
[1, 1, 1, None, None, 1, None, 0]; False
[1, 1, 1, None, None, 1, None, 1]; False
[1, 1, 1, None, None, None, 0, 0]; False
[1, 1, 1, None, None, None, 0, 1]; False
[1, 1, 1, None, None, None, 1, 0]; False
[1, 1, 1, None, None, None, 1, 1]; False
[1, 1, None, 0, 0, 0, 0, 0]; False
[1, 1, None, 0, 0, 0, 0, 1]; False
[1, 1, None, 0, 0, 0, 1, 0]; False
[1, 1, None, 0, 0, 0, 1, 1]; True
[1, 1, None, 0, 0, 0, None, 0]; False
[1, 1, None, 0, 0, 0, None, 1]; True
[1, 1, None, 0, 0, 1, 0, 0]; False
[1, 1, None, 0, 0, 1, 0, 1]; False
[1, 1, None, 0, 0, 1, 1, 0]; False
[1, 1, None, 0, 0, 1, 1, 1]; False
[1, 1, None, 0, 0, 1, None, 0]; False
[1, 1, None, 0, 0, 1, None, 1]; False
[1, 1, None, 0, 0, None, 0, 0]; False
[1, 1, None, 0, 0, None, 0, 1]; False
[1, 1, None, 0, 0, None, 1, 0]; False
[1, 1, None, 0, 0, None, 1, 1]; False
[1, 1, None, 0, 0, None, None, 0]; False
[1, 1, None, 0, 0, None, None, 1]; True
[1, 1, None, 0, 1, 0, 0, 0]; False
[1, 1, None, 0, 1, 0, 0, 1]; False
[1, 1, None, 0, 1, 0, 1, 0]; False
[1, 1, None, 0, 1, 0, 1, 1]; True
[1, 1, None, 0, 1, 0, None, 0]; False
[1, 1, None, 0, 1, 0, None, 1]; True
[1, 1, None, 0, 1, 1, 0, 0]; False
[1, 1, None, 0, 1, 1, 0, 1]; False
[1, 1, None, 0, 1, 1, 1, 0]; False
[1, 1, None, 0, 1, 1, 1, 1]; False
[1, 1, None, 0, 1, 1, None, 0]; False
[1, 1, None, 0, 1, 1, None, 1]; False
[1, 1, None, 0, 1, None, 0, 0]; False
[1, 1, None, 0, 1, None, 0, 1]; False
[1, 1, None, 0, 1, None, 1, 0]; False
[1, 1, None, 0, 1, None, 1, 1]; False
[1, 1, None, 0, 1, None, None, 0]; False
[1, 1, None, 0, 1, None, None, 1]; True
[1, 1, None, 0, None, 0, 0, 0]; False
[1, 1, None, 0, None, 0, 0, 1]; False
[1, 1, None, 0, None, 0, 1, 0]; True
[1, 1, None, 0, None, 0, 1, 1]; False
[1, 1, None, 0, None, 0, None, 0]; True
[1, 1, None, 0, None, 0, None, 1]; False
[1, 1, None, 0, None, 1, 0, 0]; False
[1, 1, None, 0, None, 1, 0, 1]; False
[1, 1, None, 0, None, 1, 1, 0]; True
[1, 1, None, 0, None, 1, 1, 1]; False
[1, 1, None, 0, None, 1, None, 0]; True
[1, 1, None, 0, None, 1, None, 1]; False
[1, 1, None, 0, None, None, 0, 0]; False
[1, 1, None, 0, None, None, 0, 1]; False
[1, 1, None, 0, None, None, 1, 0]; False
[1, 1, None, 0, None, None, 1, 1]; False
[1, 1, None, 1, 0, 0, 0, 0]; False
[1, 1, None, 1, 0, 0, 0, 1]; False
[1, 1, None, 1, 0, 0, 1, 0]; False
[1, 1, None, 1, 0, 0, 1, 1]; True
[1, 1, None, 1, 0, 0, None, 0]; False
[1, 1, None, 1, 0, 0, None, 1]; True
[1, 1, None, 1, 0, 1, 0, 0]; False
[1, 1, None, 1, 0, 1, 0, 1]; False
[1, 1, None, 1, 0, 1, 1, 0]; False
[1, 1, None, 1, 0, 1, 1, 1]; False
[1, 1, None, 1, 0, 1, None, 0]; False
[1, 1, None, 1, 0, 1, None, 1]; False
[1, 1, None, 1, 0, None, 0, 0]; False
[1, 1, None, 1, 0, None, 0, 1]; False
[1, 1, None, 1, 0, None, 1, 0]; False
[1, 1, None, 1, 0, None, 1, 1]; False
[1, 1, None, 1, 0, None, None, 0]; False
[1, 1, None, 1, 0, None, None, 1]; False
[1, 1, None, 1, 1, 0, 0, 0]; False
[1, 1, None, 1, 1, 0, 0, 1]; False
[1, 1, None, 1, 1, 0, 1, 0]; False
[1, 1, None, 1, 1, 0, 1, 1]; True
[1, 1, None, 1, 1, 0, None, 0]; False
[1, 1, None, 1, 1, 0, None, 1]; True
[1, 1, None, 1, 1, 1, 0, 0]; False
[1, 1, None, 1, 1, 1, 0, 1]; False
[1, 1, None, 1, 1, 1, 1, 0]; False
[1, 1, None, 1, 1, 1, 1, 1]; False
[1, 1, None, 1, 1, 1, None, 0]; False
[1, 1, None, 1, 1, 1, None, 1]; False
[1, 1, None, 1, 1, None, 0, 0]; False
[1, 1, None, 1, 1, None, 0, 1]; False
[1, 1, None, 1, 1, None, 1, 0]; False
[1, 1, None, 1, 1, None, 1, 1]; False
[1, 1, None, 1, 1, None, None, 0]; False
[1, 1, None, 1, 1, None, None, 1]; False
[1, 1, None, 1, None, 0, 0, 0]; False
[1, 1, None, 1, None, 0, 0, 1]; False
[1, 1, None, 1, None, 0, 1, 0]; True
[1, 1, None, 1, None, 0, 1, 1]; False
[1, 1, None, 1, None, 0, None, 0]; True
[1, 1, None, 1, None, 0, None, 1]; False
[1, 1, None, 1, None, 1, 0, 0]; False
[1, 1, None, 1, None, 1, 0, 1]; False
[1, 1, None, 1, None, 1, 1, 0]; True
[1, 1, None, 1, None, 1, 1, 1]; False
[1, 1, None, 1, None, 1, None, 0]; True
[1, 1, None, 1, None, 1, None, 1]; False
[1, 1, None, 1, None, None, 0, 0]; False
[1, 1, None, 1, None, None, 0, 1]; False
[1, 1, None, 1, None, None, 1, 0]; False
[1, 1, None, 1, None, None, 1, 1]; False
[1, 1, None, None, 0, 0, 0, 0]; False
[1, 1, None, None, 0, 0, 0, 1]; False
[1, 1, None, None, 0, 0, 1, 0]; False
[1, 1, None, None, 0, 0, 1, 1]; False
[1, 1, None, None, 0, 0, None, 0]; False
[1, 1, None, None, 0, 0, None, 1]; False
[1, 1, None, None, 0, 1, 0, 0]; False
[1, 1, None, None, 0, 1, 0, 1]; False
[1, 1, None, None, 0, 1, 1, 0]; False
[1, 1, None, None, 0, 1, 1, 1]; False
[1, 1, None, None, 0, 1, None, 0]; False
[1, 1, None, None, 0, 1, None, 1]; False
[1, 1, None, None, 0, None, 0, 0]; False
[1, 1, None, None, 0, None, 0, 1]; False
[1, 1, None, None, 0, None, 1, 0]; False
[1, 1, None, None, 0, None, 1, 1]; False
[1, 1, None, None, 1, 0, 0, 0]; False
[1, 1, None, None, 1, 0, 0, 1]; False
[1, 1, None, None, 1, 0, 1, 0]; False
[1, 1, None, None, 1, 0, 1, 1]; False
[1, 1, None, None, 1, 0, None, 0]; False
[1, 1, None, None, 1, 0, None, 1]; False
[1, 1, None, None, 1, 1, 0, 0]; False
[1, 1, None, None, 1, 1, 0, 1]; False
[1, 1, None, None, 1, 1, 1, 0]; False
[1, 1, None, None, 1, 1, 1, 1]; False
[1, 1, None, None, 1, 1, None, 0]; False
[1, 1, None, None, 1, 1, None, 1]; False
[1, 1, None, None, 1, None, 0, 0]; False
[1, 1, None, None, 1, None, 0, 1]; False
[1, 1, None, None, 1, None, 1, 0]; False
[1, 1, None, None, 1, None, 1, 1]; False
[1, None, 0, 0, 0, 0, 0, 0]; False
[1, None, 0, 0, 0, 0, 0, 1]; False
[1, None, 0, 0, 0, 0, 1, 0]; False
[1, None, 0, 0, 0, 0, 1, 1]; False
[1, None, 0, 0, 0, 0, None, 0]; False
[1, None, 0, 0, 0, 0, None, 1]; False
[1, None, 0, 0, 0, 1, 0, 0]; False
[1, None, 0, 0, 0, 1, 0, 1]; False
[1, None, 0, 0, 0, 1, 1, 0]; False
[1, None, 0, 0, 0, 1, 1, 1]; False
[1, None, 0, 0, 0, 1, None, 0]; False
[1, None, 0, 0, 0, 1, None, 1]; False
[1, None, 0, 0, 0, None, 0, 0]; False
[1, None, 0, 0, 0, None, 0, 1]; False
[1, None, 0, 0, 0, None, 1, 0]; False
[1, None, 0, 0, 0, None, 1, 1]; False
[1, None, 0, 0, 0, None, None, 0]; False
[1, None, 0, 0, 0, None, None, 1]; False
[1, None, 0, 0, 1, 0, 0, 0]; False
[1, None, 0, 0, 1, 0, 0, 1]; False
[1, None, 0, 0, 1, 0, 1, 0]; False
[1, None, 0, 0, 1, 0, 1, 1]; False
[1, None, 0, 0, 1, 0, None, 0]; False
[1, None, 0, 0, 1, 0, None, 1]; False
[1, None, 0, 0, 1, 1, 0, 0]; False
[1, None, 0, 0, 1, 1, 0, 1]; False
[1, None, 0, 0, 1, 1, 1, 0]; False
[1, None, 0, 0, 1, 1, 1, 1]; False
[1, None, 0, 0, 1, 1, None, 0]; False
[1, None, 0, 0, 1, 1, None, 1]; False
[1, None, 0, 0, 1, None, 0, 0]; False
[1, None, 0, 0, 1, None, 0, 1]; False
[1, None, 0, 0, 1, None, 1, 0]; False
[1, None, 0, 0, 1, None, 1, 1]; False
[1, None, 0, 0, 1, None, None, 0]; False
[1, None, 0, 0, 1, None, None, 1]; False
[1, None, 0, 0, None, 0, 0, 0]; False
[1, None, 0, 0, None, 0, 0, 1]; False
[1, None, 0, 0, None, 0, 1, 0]; False
[1, None, 0, 0, None, 0, 1, 1]; False
[1, None, 0, 0, None, 0, None, 0]; False
[1, None, 0, 0, None, 0, None, 1]; False
[1, None, 0, 0, None, 1, 0, 0]; False
[1, None, 0, 0, None, 1, 0, 1]; False
[1, None, 0, 0, None, 1, 1, 0]; False
[1, None, 0, 0, None, 1, 1, 1]; False
[1, None, 0, 0, None, 1, None, 0]; False
[1, None, 0, 0, None, 1, None, 1]; False
[1, None, 0, 0, None, None, 0, 0]; False
[1, None, 0, 0, None, None, 0, 1]; False
[1, None, 0, 0, None, None, 1, 0]; False
[1, None, 0, 0, None, None, 1, 1]; False
[1, None, 0, 1, 0, 0, 0, 0]; False
[1, None, 0, 1, 0, 0, 0, 1]; False
[1, None, 0, 1, 0, 0, 1, 0]; False
[1, None, 0, 1, 0, 0, 1, 1]; False
[1, None, 0, 1, 0, 0, None, 0]; False
[1, None, 0, 1, 0, 0, None, 1]; False
[1, None, 0, 1, 0, 1, 0, 0]; False
[1, None, 0, 1, 0, 1, 0, 1]; False
[1, None, 0, 1, 0, 1, 1, 0]; False
[1, None, 0, 1, 0, 1, 1, 1]; False
[1, None, 0, 1, 0, 1, None, 0]; False
[1, None, 0, 1, 0, 1, None, 1]; False
[1, None, 0, 1, 0, None, 0, 0]; False
[1, None, 0, 1, 0, None, 0, 1]; False
[1, None, 0, 1, 0, None, 1, 0]; False
[1, None, 0, 1, 0, None, 1, 1]; False
[1, None, 0, 1, 0, None, None, 0]; False
[1, None, 0, 1, 0, None, None, 1]; False
[1, None, 0, 1, 1, 0, 0, 0]; False
[1, None, 0, 1, 1, 0, 0, 1]; False
[1, None, 0, 1, 1, 0, 1, 0]; False
[1, None, 0, 1, 1, 0, 1, 1]; False
[1, None, 0, 1, 1, 0, None, 0]; False
[1, None, 0, 1, 1, 0, None, 1]; False
[1, None, 0, 1, 1, 1, 0, 0]; False
[1, None, 0, 1, 1, 1, 0, 1]; False
[1, None, 0, 1, 1, 1, 1, 0]; False
[1, None, 0, 1, 1, 1, 1, 1]; False
[1, None, 0, 1, 1, 1, None, 0]; False
[1, None, 0, 1, 1, 1, None, 1]; False
[1, None, 0, 1, 1, None, 0, 0]; False
[1, None, 0, 1, 1, None, 0, 1]; False
[1, None, 0, 1, 1, None, 1, 0]; False
[1, None, 0, 1, 1, None, 1, 1]; False
[1, None, 0, 1, 1, None, None, 0]; False
[1, None, 0, 1, 1, None, None, 1]; False
[1, None, 0, 1, None, 0, 0, 0]; False
[1, None, 0, 1, None, 0, 0, 1]; False
[1, None, 0, 1, None, 0, 1, 0]; False
[1, None, 0, 1, None, 0, 1, 1]; False
[1, None, 0, 1, None, 0, None, 0]; False
[1, None, 0, 1, None, 0, None, 1]; False
[1, None, 0, 1, None, 1, 0, 0]; False
[1, None, 0, 1, None, 1, 0, 1]; False
[1, None, 0, 1, None, 1, 1, 0]; False
[1, None, 0, 1, None, 1, 1, 1]; False
[1, None, 0, 1, None, 1, None, 0]; False
[1, None, 0, 1, None, 1, None, 1]; False
[1, None, 0, 1, None, None, 0, 0]; False
[1, None, 0, 1, None, None, 0, 1]; False
[1, None, 0, 1, None, None, 1, 0]; False
[1, None, 0, 1, None, None, 1, 1]; False
[1, None, 0, None, 0, 0, 0, 0]; False
[1, None, 0, None, 0, 0, 0, 1]; False
[1, None, 0, None, 0, 0, 1, 0]; False
[1, None, 0, None, 0, 0, 1, 1]; False
[1, None, 0, None, 0, 0, None, 0]; False
[1, None, 0, None, 0, 0, None, 1]; False
[1, None, 0, None, 0, 1, 0, 0]; False
[1, None, 0, None, 0, 1, 0, 1]; False
[1, None, 0, None, 0, 1, 1, 0]; False
[1, None, 0, None, 0, 1, 1, 1]; False
[1, None, 0, None, 0, 1, None, 0]; False
[1, None, 0, None, 0, 1, None, 1]; False
[1, None, 0, None, 0, None, 0, 0]; False
[1, None, 0, None, 0, None, 0, 1]; False
[1, None, 0, None, 0, None, 1, 0]; False
[1, None, 0, None, 0, None, 1, 1]; False
[1, None, 0, None, 1, 0, 0, 0]; False
[1, None, 0, None, 1, 0, 0, 1]; False
[1, None, 0, None, 1, 0, 1, 0]; False
[1, None, 0, None, 1, 0, 1, 1]; False
[1, None, 0, None, 1, 0, None, 0]; False
[1, None, 0, None, 1, 0, None, 1]; False
[1, None, 0, None, 1, 1, 0, 0]; False
[1, None, 0, None, 1, 1, 0, 1]; False
[1, None, 0, None, 1, 1, 1, 0]; False
[1, None, 0, None, 1, 1, 1, 1]; False
[1, None, 0, None, 1, 1, None, 0]; False
[1, None, 0, None, 1, 1, None, 1]; False
[1, None, 0, None, 1, None, 0, 0]; False
[1, None, 0, None, 1, None, 0, 1]; False
[1, None, 0, None, 1, None, 1, 0]; False
[1, None, 0, None, 1, None, 1, 1]; False
[1, None, 1, 0, 0, 0, 0, 0]; False
[1, None, 1, 0, 0, 0, 0, 1]; False
[1, None, 1, 0, 0, 0, 1, 0]; False
[1, None, 1, 0, 0, 0, 1, 1]; False
[1, None, 1, 0, 0, 0, None, 0]; False
[1, None, 1, 0, 0, 0, None, 1]; False
[1, None, 1, 0, 0, 1, 0, 0]; False
[1, None, 1, 0, 0, 1, 0, 1]; False
[1, None, 1, 0, 0, 1, 1, 0]; False
[1, None, 1, 0, 0, 1, 1, 1]; False
[1, None, 1, 0, 0, 1, None, 0]; False
[1, None, 1, 0, 0, 1, None, 1]; False
[1, None, 1, 0, 0, None, 0, 0]; False
[1, None, 1, 0, 0, None, 0, 1]; False
[1, None, 1, 0, 0, None, 1, 0]; False
[1, None, 1, 0, 0, None, 1, 1]; False
[1, None, 1, 0, 0, None, None, 0]; False
[1, None, 1, 0, 0, None, None, 1]; False
[1, None, 1, 0, 1, 0, 0, 0]; False
[1, None, 1, 0, 1, 0, 0, 1]; False
[1, None, 1, 0, 1, 0, 1, 0]; False
[1, None, 1, 0, 1, 0, 1, 1]; False
[1, None, 1, 0, 1, 0, None, 0]; False
[1, None, 1, 0, 1, 0, None, 1]; False
[1, None, 1, 0, 1, 1, 0, 0]; False
[1, None, 1, 0, 1, 1, 0, 1]; False
[1, None, 1, 0, 1, 1, 1, 0]; False
[1, None, 1, 0, 1, 1, 1, 1]; False
[1, None, 1, 0, 1, 1, None, 0]; False
[1, None, 1, 0, 1, 1, None, 1]; False
[1, None, 1, 0, 1, None, 0, 0]; False
[1, None, 1, 0, 1, None, 0, 1]; False
[1, None, 1, 0, 1, None, 1, 0]; False
[1, None, 1, 0, 1, None, 1, 1]; False
[1, None, 1, 0, 1, None, None, 0]; False
[1, None, 1, 0, 1, None, None, 1]; False
[1, None, 1, 0, None, 0, 0, 0]; False
[1, None, 1, 0, None, 0, 0, 1]; False
[1, None, 1, 0, None, 0, 1, 0]; False
[1, None, 1, 0, None, 0, 1, 1]; False
[1, None, 1, 0, None, 0, None, 0]; False
[1, None, 1, 0, None, 0, None, 1]; False
[1, None, 1, 0, None, 1, 0, 0]; False
[1, None, 1, 0, None, 1, 0, 1]; False
[1, None, 1, 0, None, 1, 1, 0]; False
[1, None, 1, 0, None, 1, 1, 1]; False
[1, None, 1, 0, None, 1, None, 0]; False
[1, None, 1, 0, None, 1, None, 1]; False
[1, None, 1, 0, None, None, 0, 0]; False
[1, None, 1, 0, None, None, 0, 1]; False
[1, None, 1, 0, None, None, 1, 0]; False
[1, None, 1, 0, None, None, 1, 1]; False
[1, None, 1, 1, 0, 0, 0, 0]; False
[1, None, 1, 1, 0, 0, 0, 1]; False
[1, None, 1, 1, 0, 0, 1, 0]; False
[1, None, 1, 1, 0, 0, 1, 1]; False
[1, None, 1, 1, 0, 0, None, 0]; False
[1, None, 1, 1, 0, 0, None, 1]; False
[1, None, 1, 1, 0, 1, 0, 0]; False
[1, None, 1, 1, 0, 1, 0, 1]; False
[1, None, 1, 1, 0, 1, 1, 0]; False
[1, None, 1, 1, 0, 1, 1, 1]; False
[1, None, 1, 1, 0, 1, None, 0]; False
[1, None, 1, 1, 0, 1, None, 1]; False
[1, None, 1, 1, 0, None, 0, 0]; False
[1, None, 1, 1, 0, None, 0, 1]; False
[1, None, 1, 1, 0, None, 1, 0]; False
[1, None, 1, 1, 0, None, 1, 1]; False
[1, None, 1, 1, 0, None, None, 0]; False
[1, None, 1, 1, 0, None, None, 1]; False
[1, None, 1, 1, 1, 0, 0, 0]; False
[1, None, 1, 1, 1, 0, 0, 1]; False
[1, None, 1, 1, 1, 0, 1, 0]; False
[1, None, 1, 1, 1, 0, 1, 1]; False
[1, None, 1, 1, 1, 0, None, 0]; False
[1, None, 1, 1, 1, 0, None, 1]; False
[1, None, 1, 1, 1, 1, 0, 0]; False
[1, None, 1, 1, 1, 1, 0, 1]; False
[1, None, 1, 1, 1, 1, 1, 0]; False
[1, None, 1, 1, 1, 1, 1, 1]; False
[1, None, 1, 1, 1, 1, None, 0]; False
[1, None, 1, 1, 1, 1, None, 1]; False
[1, None, 1, 1, 1, None, 0, 0]; False
[1, None, 1, 1, 1, None, 0, 1]; False
[1, None, 1, 1, 1, None, 1, 0]; False
[1, None, 1, 1, 1, None, 1, 1]; False
[1, None, 1, 1, 1, None, None, 0]; False
[1, None, 1, 1, 1, None, None, 1]; False
[1, None, 1, 1, None, 0, 0, 0]; False
[1, None, 1, 1, None, 0, 0, 1]; False
[1, None, 1, 1, None, 0, 1, 0]; False
[1, None, 1, 1, None, 0, 1, 1]; False
[1, None, 1, 1, None, 0, None, 0]; False
[1, None, 1, 1, None, 0, None, 1]; False
[1, None, 1, 1, None, 1, 0, 0]; False
[1, None, 1, 1, None, 1, 0, 1]; False
[1, None, 1, 1, None, 1, 1, 0]; False
[1, None, 1, 1, None, 1, 1, 1]; False
[1, None, 1, 1, None, 1, None, 0]; False
[1, None, 1, 1, None, 1, None, 1]; False
[1, None, 1, 1, None, None, 0, 0]; False
[1, None, 1, 1, None, None, 0, 1]; False
[1, None, 1, 1, None, None, 1, 0]; False
[1, None, 1, 1, None, None, 1, 1]; False
[1, None, 1, None, 0, 0, 0, 0]; False
[1, None, 1, None, 0, 0, 0, 1]; False
[1, None, 1, None, 0, 0, 1, 0]; False
[1, None, 1, None, 0, 0, 1, 1]; False
[1, None, 1, None, 0, 0, None, 0]; False
[1, None, 1, None, 0, 0, None, 1]; False
[1, None, 1, None, 0, 1, 0, 0]; False
[1, None, 1, None, 0, 1, 0, 1]; False
[1, None, 1, None, 0, 1, 1, 0]; False
[1, None, 1, None, 0, 1, 1, 1]; False
[1, None, 1, None, 0, 1, None, 0]; False
[1, None, 1, None, 0, 1, None, 1]; False
[1, None, 1, None, 0, None, 0, 0]; False
[1, None, 1, None, 0, None, 0, 1]; False
[1, None, 1, None, 0, None, 1, 0]; False
[1, None, 1, None, 0, None, 1, 1]; False
[1, None, 1, None, 1, 0, 0, 0]; False
[1, None, 1, None, 1, 0, 0, 1]; False
[1, None, 1, None, 1, 0, 1, 0]; False
[1, None, 1, None, 1, 0, 1, 1]; False
[1, None, 1, None, 1, 0, None, 0]; False
[1, None, 1, None, 1, 0, None, 1]; False
[1, None, 1, None, 1, 1, 0, 0]; False
[1, None, 1, None, 1, 1, 0, 1]; False
[1, None, 1, None, 1, 1, 1, 0]; False
[1, None, 1, None, 1, 1, 1, 1]; False
[1, None, 1, None, 1, 1, None, 0]; False
[1, None, 1, None, 1, 1, None, 1]; False
[1, None, 1, None, 1, None, 0, 0]; False
[1, None, 1, None, 1, None, 0, 1]; False
[1, None, 1, None, 1, None, 1, 0]; False
[1, None, 1, None, 1, None, 1, 1]; False
[0, 0, 0, 0, 0, 0, 0, 0, 0]; False
[0, 0, 0, 0, 0, 0, 0, 0, 1]; False
[0, 0, 0, 0, 0, 0, 0, 1, 0]; False
[0, 0, 0, 0, 0, 0, 0, 1, 1]; False
[0, 0, 0, 0, 0, 0, 0, None, 0]; False
[0, 0, 0, 0, 0, 0, 0, None, 1]; False
[0, 0, 0, 0, 0, 0, 1, 0, 0]; False
[0, 0, 0, 0, 0, 0, 1, 0, 1]; False
[0, 0, 0, 0, 0, 0, 1, 1, 0]; False
[0, 0, 0, 0, 0, 0, 1, 1, 1]; False
[0, 0, 0, 0, 0, 0, 1, None, 0]; False
[0, 0, 0, 0, 0, 0, 1, None, 1]; False
[0, 0, 0, 0, 0, 0, None, 0, 0]; False
[0, 0, 0, 0, 0, 0, None, 0, 1]; False
[0, 0, 0, 0, 0, 0, None, 1, 0]; False
[0, 0, 0, 0, 0, 0, None, 1, 1]; False
[0, 0, 0, 0, 0, 0, None, None, 0]; False
[0, 0, 0, 0, 0, 0, None, None, 1]; False
[0, 0, 0, 0, 0, 1, 0, 0, 0]; False
[0, 0, 0, 0, 0, 1, 0, 0, 1]; False
[0, 0, 0, 0, 0, 1, 0, 1, 0]; False
[0, 0, 0, 0, 0, 1, 0, 1, 1]; False
[0, 0, 0, 0, 0, 1, 0, None, 0]; False
[0, 0, 0, 0, 0, 1, 0, None, 1]; False
[0, 0, 0, 0, 0, 1, 1, 0, 0]; False
[0, 0, 0, 0, 0, 1, 1, 0, 1]; False
[0, 0, 0, 0, 0, 1, 1, 1, 0]; False
[0, 0, 0, 0, 0, 1, 1, 1, 1]; False
[0, 0, 0, 0, 0, 1, 1, None, 0]; False
[0, 0, 0, 0, 0, 1, 1, None, 1]; False
[0, 0, 0, 0, 0, 1, None, 0, 0]; False
[0, 0, 0, 0, 0, 1, None, 0, 1]; False
[0, 0, 0, 0, 0, 1, None, 1, 0]; False
[0, 0, 0, 0, 0, 1, None, 1, 1]; False
[0, 0, 0, 0, 0, 1, None, None, 0]; False
[0, 0, 0, 0, 0, 1, None, None, 1]; False
[0, 0, 0, 0, 0, None, 0, 0, 0]; False
[0, 0, 0, 0, 0, None, 0, 0, 1]; False
[0, 0, 0, 0, 0, None, 0, 1, 0]; False
[0, 0, 0, 0, 0, None, 0, 1, 1]; False
[0, 0, 0, 0, 0, None, 0, None, 0]; False
[0, 0, 0, 0, 0, None, 0, None, 1]; False
[0, 0, 0, 0, 0, None, 1, 0, 0]; False
[0, 0, 0, 0, 0, None, 1, 0, 1]; False
[0, 0, 0, 0, 0, None, 1, 1, 0]; False
[0, 0, 0, 0, 0, None, 1, 1, 1]; False
[0, 0, 0, 0, 0, None, 1, None, 0]; False
[0, 0, 0, 0, 0, None, 1, None, 1]; False
[0, 0, 0, 0, 0, None, None, 0, 0]; False
[0, 0, 0, 0, 0, None, None, 0, 1]; False
[0, 0, 0, 0, 0, None, None, 1, 0]; False
[0, 0, 0, 0, 0, None, None, 1, 1]; False
[0, 0, 0, 0, 0, None, None, None, 0]; False
[0, 0, 0, 0, 0, None, None, None, 1]; False
[0, 0, 0, 0, 1, 0, 0, 0, 0]; False
[0, 0, 0, 0, 1, 0, 0, 0, 1]; True
[0, 0, 0, 0, 1, 0, 0, 1, 0]; False
[0, 0, 0, 0, 1, 0, 0, 1, 1]; False
[0, 0, 0, 0, 1, 0, 0, None, 0]; False
[0, 0, 0, 0, 1, 0, 0, None, 1]; False
[0, 0, 0, 0, 1, 0, 1, 0, 0]; False
[0, 0, 0, 0, 1, 0, 1, 0, 1]; False
[0, 0, 0, 0, 1, 0, 1, 1, 0]; False
[0, 0, 0, 0, 1, 0, 1, 1, 1]; False
[0, 0, 0, 0, 1, 0, 1, None, 0]; False
[0, 0, 0, 0, 1, 0, 1, None, 1]; False
[0, 0, 0, 0, 1, 0, None, 0, 0]; False
[0, 0, 0, 0, 1, 0, None, 0, 1]; False
[0, 0, 0, 0, 1, 0, None, 1, 0]; False
[0, 0, 0, 0, 1, 0, None, 1, 1]; False
[0, 0, 0, 0, 1, 0, None, None, 0]; False
[0, 0, 0, 0, 1, 0, None, None, 1]; False
[0, 0, 0, 0, 1, 1, 0, 0, 0]; False
[0, 0, 0, 0, 1, 1, 0, 0, 1]; True
[0, 0, 0, 0, 1, 1, 0, 1, 0]; False
[0, 0, 0, 0, 1, 1, 0, 1, 1]; False
[0, 0, 0, 0, 1, 1, 0, None, 0]; False
[0, 0, 0, 0, 1, 1, 0, None, 1]; False
[0, 0, 0, 0, 1, 1, 1, 0, 0]; False
[0, 0, 0, 0, 1, 1, 1, 0, 1]; True
[0, 0, 0, 0, 1, 1, 1, 1, 0]; False
[0, 0, 0, 0, 1, 1, 1, 1, 1]; False
[0, 0, 0, 0, 1, 1, 1, None, 0]; False
[0, 0, 0, 0, 1, 1, 1, None, 1]; False
[0, 0, 0, 0, 1, 1, None, 0, 0]; False
[0, 0, 0, 0, 1, 1, None, 0, 1]; True
[0, 0, 0, 0, 1, 1, None, 1, 0]; False
[0, 0, 0, 0, 1, 1, None, 1, 1]; False
[0, 0, 0, 0, 1, 1, None, None, 0]; False
[0, 0, 0, 0, 1, 1, None, None, 1]; False
[0, 0, 0, 0, 1, None, 0, 0, 0]; False
[0, 0, 0, 0, 1, None, 0, 0, 1]; True
[0, 0, 0, 0, 1, None, 0, 1, 0]; False
[0, 0, 0, 0, 1, None, 0, 1, 1]; False
[0, 0, 0, 0, 1, None, 0, None, 0]; False
[0, 0, 0, 0, 1, None, 0, None, 1]; False
[0, 0, 0, 0, 1, None, 1, 0, 0]; False
[0, 0, 0, 0, 1, None, 1, 0, 1]; True
[0, 0, 0, 0, 1, None, 1, 1, 0]; False
[0, 0, 0, 0, 1, None, 1, 1, 1]; False
[0, 0, 0, 0, 1, None, 1, None, 0]; False
[0, 0, 0, 0, 1, None, 1, None, 1]; False
[0, 0, 0, 0, 1, None, None, 0, 0]; False
[0, 0, 0, 0, 1, None, None, 0, 1]; False
[0, 0, 0, 0, 1, None, None, 1, 0]; False
[0, 0, 0, 0, 1, None, None, 1, 1]; False
[0, 0, 0, 0, 1, None, None, None, 0]; False
[0, 0, 0, 0, 1, None, None, None, 1]; False
[0, 0, 0, 0, None, 0, 0, 0, 0]; False
[0, 0, 0, 0, None, 0, 0, 0, 1]; True
[0, 0, 0, 0, None, 0, 0, 1, 0]; False
[0, 0, 0, 0, None, 0, 0, 1, 1]; False
[0, 0, 0, 0, None, 0, 0, None, 0]; False
[0, 0, 0, 0, None, 0, 0, None, 1]; False
[0, 0, 0, 0, None, 0, 1, 0, 0]; False
[0, 0, 0, 0, None, 0, 1, 0, 1]; False
[0, 0, 0, 0, None, 0, 1, 1, 0]; False
[0, 0, 0, 0, None, 0, 1, 1, 1]; False
[0, 0, 0, 0, None, 0, 1, None, 0]; False
[0, 0, 0, 0, None, 0, 1, None, 1]; False
[0, 0, 0, 0, None, 0, None, 0, 0]; False
[0, 0, 0, 0, None, 0, None, 0, 1]; False
[0, 0, 0, 0, None, 0, None, 1, 0]; False
[0, 0, 0, 0, None, 0, None, 1, 1]; False
[0, 0, 0, 0, None, 0, None, None, 0]; False
[0, 0, 0, 0, None, 0, None, None, 1]; False
[0, 0, 0, 0, None, 1, 0, 0, 0]; False
[0, 0, 0, 0, None, 1, 0, 0, 1]; True
[0, 0, 0, 0, None, 1, 0, 1, 0]; False
[0, 0, 0, 0, None, 1, 0, 1, 1]; False
[0, 0, 0, 0, None, 1, 0, None, 0]; False
[0, 0, 0, 0, None, 1, 0, None, 1]; False
[0, 0, 0, 0, None, 1, 1, 0, 0]; False
[0, 0, 0, 0, None, 1, 1, 0, 1]; True
[0, 0, 0, 0, None, 1, 1, 1, 0]; False
[0, 0, 0, 0, None, 1, 1, 1, 1]; False
[0, 0, 0, 0, None, 1, 1, None, 0]; False
[0, 0, 0, 0, None, 1, 1, None, 1]; False
[0, 0, 0, 0, None, 1, None, 0, 0]; False
[0, 0, 0, 0, None, 1, None, 0, 1]; True
[0, 0, 0, 0, None, 1, None, 1, 0]; False
[0, 0, 0, 0, None, 1, None, 1, 1]; False
[0, 0, 0, 0, None, 1, None, None, 0]; False
[0, 0, 0, 0, None, 1, None, None, 1]; False
[0, 0, 0, 0, None, None, 0, 0, 0]; False
[0, 0, 0, 0, None, None, 0, 0, 1]; True
[0, 0, 0, 0, None, None, 0, 1, 0]; False
[0, 0, 0, 0, None, None, 0, 1, 1]; False
[0, 0, 0, 0, None, None, 0, None, 0]; False
[0, 0, 0, 0, None, None, 0, None, 1]; False
[0, 0, 0, 0, None, None, 1, 0, 0]; False
[0, 0, 0, 0, None, None, 1, 0, 1]; True
[0, 0, 0, 0, None, None, 1, 1, 0]; False
[0, 0, 0, 0, None, None, 1, 1, 1]; False
[0, 0, 0, 0, None, None, 1, None, 0]; False
[0, 0, 0, 0, None, None, 1, None, 1]; False
[0, 0, 0, 0, None, None, None, 0, 0]; False
[0, 0, 0, 0, None, None, None, 0, 1]; False
[0, 0, 0, 0, None, None, None, 1, 0]; False
[0, 0, 0, 0, None, None, None, 1, 1]; False
[0, 0, 0, 0, None, None, None, None, 0]; False
[0, 0, 0, 0, None, None, None, None, 1]; False
[0, 0, 0, 1, 0, 0, 0, 0, 0]; False
[0, 0, 0, 1, 0, 0, 0, 0, 1]; False
[0, 0, 0, 1, 0, 0, 0, 1, 0]; False
[0, 0, 0, 1, 0, 0, 0, 1, 1]; False
[0, 0, 0, 1, 0, 0, 0, None, 0]; False
[0, 0, 0, 1, 0, 0, 0, None, 1]; False
[0, 0, 0, 1, 0, 0, 1, 0, 0]; False
[0, 0, 0, 1, 0, 0, 1, 0, 1]; False
[0, 0, 0, 1, 0, 0, 1, 1, 0]; False
[0, 0, 0, 1, 0, 0, 1, 1, 1]; False
[0, 0, 0, 1, 0, 0, 1, None, 0]; False
[0, 0, 0, 1, 0, 0, 1, None, 1]; False
[0, 0, 0, 1, 0, 0, None, 0, 0]; False
[0, 0, 0, 1, 0, 0, None, 0, 1]; False
[0, 0, 0, 1, 0, 0, None, 1, 0]; False
[0, 0, 0, 1, 0, 0, None, 1, 1]; False
[0, 0, 0, 1, 0, 0, None, None, 0]; False
[0, 0, 0, 1, 0, 0, None, None, 1]; False
[0, 0, 0, 1, 0, 1, 0, 0, 0]; False
[0, 0, 0, 1, 0, 1, 0, 0, 1]; False
[0, 0, 0, 1, 0, 1, 0, 1, 0]; False
[0, 0, 0, 1, 0, 1, 0, 1, 1]; False
[0, 0, 0, 1, 0, 1, 0, None, 0]; False
[0, 0, 0, 1, 0, 1, 0, None, 1]; False
[0, 0, 0, 1, 0, 1, 1, 0, 0]; False
[0, 0, 0, 1, 0, 1, 1, 0, 1]; False
[0, 0, 0, 1, 0, 1, 1, 1, 0]; False
[0, 0, 0, 1, 0, 1, 1, 1, 1]; False
[0, 0, 0, 1, 0, 1, 1, None, 0]; False
[0, 0, 0, 1, 0, 1, 1, None, 1]; False
[0, 0, 0, 1, 0, 1, None, 0, 0]; False
[0, 0, 0, 1, 0, 1, None, 0, 1]; False
[0, 0, 0, 1, 0, 1, None, 1, 0]; False
[0, 0, 0, 1, 0, 1, None, 1, 1]; False
[0, 0, 0, 1, 0, 1, None, None, 0]; False
[0, 0, 0, 1, 0, 1, None, None, 1]; False
[0, 0, 0, 1, 0, None, 0, 0, 0]; False
[0, 0, 0, 1, 0, None, 0, 0, 1]; False
[0, 0, 0, 1, 0, None, 0, 1, 0]; False
[0, 0, 0, 1, 0, None, 0, 1, 1]; False
[0, 0, 0, 1, 0, None, 0, None, 0]; False
[0, 0, 0, 1, 0, None, 0, None, 1]; False
[0, 0, 0, 1, 0, None, 1, 0, 0]; False
[0, 0, 0, 1, 0, None, 1, 0, 1]; False
[0, 0, 0, 1, 0, None, 1, 1, 0]; False
[0, 0, 0, 1, 0, None, 1, 1, 1]; False
[0, 0, 0, 1, 0, None, 1, None, 0]; False
[0, 0, 0, 1, 0, None, 1, None, 1]; False
[0, 0, 0, 1, 0, None, None, 0, 0]; False
[0, 0, 0, 1, 0, None, None, 0, 1]; False
[0, 0, 0, 1, 0, None, None, 1, 0]; False
[0, 0, 0, 1, 0, None, None, 1, 1]; False
[0, 0, 0, 1, 0, None, None, None, 0]; False
[0, 0, 0, 1, 0, None, None, None, 1]; False
[0, 0, 0, 1, 1, 0, 0, 0, 0]; False
[0, 0, 0, 1, 1, 0, 0, 0, 1]; False
[0, 0, 0, 1, 1, 0, 0, 1, 0]; False
[0, 0, 0, 1, 1, 0, 0, 1, 1]; False
[0, 0, 0, 1, 1, 0, 0, None, 0]; False
[0, 0, 0, 1, 1, 0, 0, None, 1]; False
[0, 0, 0, 1, 1, 0, 1, 0, 0]; False
[0, 0, 0, 1, 1, 0, 1, 0, 1]; False
[0, 0, 0, 1, 1, 0, 1, 1, 0]; False
[0, 0, 0, 1, 1, 0, 1, 1, 1]; False
[0, 0, 0, 1, 1, 0, 1, None, 0]; False
[0, 0, 0, 1, 1, 0, 1, None, 1]; False
[0, 0, 0, 1, 1, 0, None, 0, 0]; False
[0, 0, 0, 1, 1, 0, None, 0, 1]; False
[0, 0, 0, 1, 1, 0, None, 1, 0]; False
[0, 0, 0, 1, 1, 0, None, 1, 1]; False
[0, 0, 0, 1, 1, 0, None, None, 0]; False
[0, 0, 0, 1, 1, 0, None, None, 1]; False
[0, 0, 0, 1, 1, 1, 0, 0, 0]; False
[0, 0, 0, 1, 1, 1, 0, 0, 1]; True
[0, 0, 0, 1, 1, 1, 0, 1, 0]; False
[0, 0, 0, 1, 1, 1, 0, 1, 1]; False
[0, 0, 0, 1, 1, 1, 0, None, 0]; False
[0, 0, 0, 1, 1, 1, 0, None, 1]; False
[0, 0, 0, 1, 1, 1, 1, 0, 0]; False
[0, 0, 0, 1, 1, 1, 1, 0, 1]; True
[0, 0, 0, 1, 1, 1, 1, 1, 0]; False
[0, 0, 0, 1, 1, 1, 1, 1, 1]; False
[0, 0, 0, 1, 1, 1, 1, None, 0]; False
[0, 0, 0, 1, 1, 1, 1, None, 1]; False
[0, 0, 0, 1, 1, 1, None, 0, 0]; False
[0, 0, 0, 1, 1, 1, None, 0, 1]; True
[0, 0, 0, 1, 1, 1, None, 1, 0]; False
[0, 0, 0, 1, 1, 1, None, 1, 1]; False
[0, 0, 0, 1, 1, 1, None, None, 0]; False
[0, 0, 0, 1, 1, 1, None, None, 1]; False
[0, 0, 0, 1, 1, None, 0, 0, 0]; False
[0, 0, 0, 1, 1, None, 0, 0, 1]; True
[0, 0, 0, 1, 1, None, 0, 1, 0]; False
[0, 0, 0, 1, 1, None, 0, 1, 1]; False
[0, 0, 0, 1, 1, None, 0, None, 0]; False
[0, 0, 0, 1, 1, None, 0, None, 1]; False
[0, 0, 0, 1, 1, None, 1, 0, 0]; False
[0, 0, 0, 1, 1, None, 1, 0, 1]; True
[0, 0, 0, 1, 1, None, 1, 1, 0]; False
[0, 0, 0, 1, 1, None, 1, 1, 1]; False
[0, 0, 0, 1, 1, None, 1, None, 0]; False
[0, 0, 0, 1, 1, None, 1, None, 1]; False
[0, 0, 0, 1, 1, None, None, 0, 0]; False
[0, 0, 0, 1, 1, None, None, 0, 1]; False
[0, 0, 0, 1, 1, None, None, 1, 0]; False
[0, 0, 0, 1, 1, None, None, 1, 1]; False
[0, 0, 0, 1, 1, None, None, None, 0]; False
[0, 0, 0, 1, 1, None, None, None, 1]; False
[0, 0, 0, 1, None, 0, 0, 0, 0]; False
[0, 0, 0, 1, None, 0, 0, 0, 1]; False
[0, 0, 0, 1, None, 0, 0, 1, 0]; False
[0, 0, 0, 1, None, 0, 0, 1, 1]; False
[0, 0, 0, 1, None, 0, 0, None, 0]; False
[0, 0, 0, 1, None, 0, 0, None, 1]; False
[0, 0, 0, 1, None, 0, 1, 0, 0]; False
[0, 0, 0, 1, None, 0, 1, 0, 1]; False
[0, 0, 0, 1, None, 0, 1, 1, 0]; False
[0, 0, 0, 1, None, 0, 1, 1, 1]; False
[0, 0, 0, 1, None, 0, 1, None, 0]; False
[0, 0, 0, 1, None, 0, 1, None, 1]; False
[0, 0, 0, 1, None, 0, None, 0, 0]; False
[0, 0, 0, 1, None, 0, None, 0, 1]; False
[0, 0, 0, 1, None, 0, None, 1, 0]; False
[0, 0, 0, 1, None, 0, None, 1, 1]; False
[0, 0, 0, 1, None, 0, None, None, 0]; False
[0, 0, 0, 1, None, 0, None, None, 1]; False
[0, 0, 0, 1, None, 1, 0, 0, 0]; False
[0, 0, 0, 1, None, 1, 0, 0, 1]; True
[0, 0, 0, 1, None, 1, 0, 1, 0]; False
[0, 0, 0, 1, None, 1, 0, 1, 1]; False
[0, 0, 0, 1, None, 1, 0, None, 0]; False
[0, 0, 0, 1, None, 1, 0, None, 1]; False
[0, 0, 0, 1, None, 1, 1, 0, 0]; False
[0, 0, 0, 1, None, 1, 1, 0, 1]; True
[0, 0, 0, 1, None, 1, 1, 1, 0]; False
[0, 0, 0, 1, None, 1, 1, 1, 1]; False
[0, 0, 0, 1, None, 1, 1, None, 0]; False
[0, 0, 0, 1, None, 1, 1, None, 1]; False
[0, 0, 0, 1, None, 1, None, 0, 0]; False
[0, 0, 0, 1, None, 1, None, 0, 1]; True
[0, 0, 0, 1, None, 1, None, 1, 0]; False
[0, 0, 0, 1, None, 1, None, 1, 1]; False
[0, 0, 0, 1, None, 1, None, None, 0]; False
[0, 0, 0, 1, None, 1, None, None, 1]; False
[0, 0, 0, 1, None, None, 0, 0, 0]; False
[0, 0, 0, 1, None, None, 0, 0, 1]; True
[0, 0, 0, 1, None, None, 0, 1, 0]; False
[0, 0, 0, 1, None, None, 0, 1, 1]; False
[0, 0, 0, 1, None, None, 0, None, 0]; False
[0, 0, 0, 1, None, None, 0, None, 1]; False
[0, 0, 0, 1, None, None, 1, 0, 0]; False
[0, 0, 0, 1, None, None, 1, 0, 1]; True
[0, 0, 0, 1, None, None, 1, 1, 0]; False
[0, 0, 0, 1, None, None, 1, 1, 1]; False
[0, 0, 0, 1, None, None, 1, None, 0]; False
[0, 0, 0, 1, None, None, 1, None, 1]; False
[0, 0, 0, 1, None, None, None, 0, 0]; False
[0, 0, 0, 1, None, None, None, 0, 1]; False
[0, 0, 0, 1, None, None, None, 1, 0]; False
[0, 0, 0, 1, None, None, None, 1, 1]; False
[0, 0, 0, 1, None, None, None, None, 0]; False
[0, 0, 0, 1, None, None, None, None, 1]; False
[0, 0, 0, None, 0, 0, 0, 0, 0]; False
[0, 0, 0, None, 0, 0, 0, 0, 1]; False
[0, 0, 0, None, 0, 0, 0, 1, 0]; False
[0, 0, 0, None, 0, 0, 0, 1, 1]; False
[0, 0, 0, None, 0, 0, 0, None, 0]; False
[0, 0, 0, None, 0, 0, 0, None, 1]; False
[0, 0, 0, None, 0, 0, 1, 0, 0]; False
[0, 0, 0, None, 0, 0, 1, 0, 1]; False
[0, 0, 0, None, 0, 0, 1, 1, 0]; False
[0, 0, 0, None, 0, 0, 1, 1, 1]; False
[0, 0, 0, None, 0, 0, 1, None, 0]; False
[0, 0, 0, None, 0, 0, 1, None, 1]; False
[0, 0, 0, None, 0, 0, None, 0, 0]; False
[0, 0, 0, None, 0, 0, None, 0, 1]; False
[0, 0, 0, None, 0, 0, None, 1, 0]; False
[0, 0, 0, None, 0, 0, None, 1, 1]; False
[0, 0, 0, None, 0, 0, None, None, 0]; False
[0, 0, 0, None, 0, 0, None, None, 1]; False
[0, 0, 0, None, 0, 1, 0, 0, 0]; False
[0, 0, 0, None, 0, 1, 0, 0, 1]; False
[0, 0, 0, None, 0, 1, 0, 1, 0]; False
[0, 0, 0, None, 0, 1, 0, 1, 1]; False
[0, 0, 0, None, 0, 1, 0, None, 0]; False
[0, 0, 0, None, 0, 1, 0, None, 1]; False
[0, 0, 0, None, 0, 1, 1, 0, 0]; False
[0, 0, 0, None, 0, 1, 1, 0, 1]; False
[0, 0, 0, None, 0, 1, 1, 1, 0]; False
[0, 0, 0, None, 0, 1, 1, 1, 1]; False
[0, 0, 0, None, 0, 1, 1, None, 0]; False
[0, 0, 0, None, 0, 1, 1, None, 1]; False
[0, 0, 0, None, 0, 1, None, 0, 0]; False
[0, 0, 0, None, 0, 1, None, 0, 1]; False
[0, 0, 0, None, 0, 1, None, 1, 0]; False
[0, 0, 0, None, 0, 1, None, 1, 1]; False
[0, 0, 0, None, 0, 1, None, None, 0]; False
[0, 0, 0, None, 0, 1, None, None, 1]; False
[0, 0, 0, None, 0, None, 0, 0, 0]; False
[0, 0, 0, None, 0, None, 0, 0, 1]; False
[0, 0, 0, None, 0, None, 0, 1, 0]; False
[0, 0, 0, None, 0, None, 0, 1, 1]; False
[0, 0, 0, None, 0, None, 0, None, 0]; False
[0, 0, 0, None, 0, None, 0, None, 1]; False
[0, 0, 0, None, 0, None, 1, 0, 0]; False
[0, 0, 0, None, 0, None, 1, 0, 1]; False
[0, 0, 0, None, 0, None, 1, 1, 0]; False
[0, 0, 0, None, 0, None, 1, 1, 1]; False
[0, 0, 0, None, 0, None, 1, None, 0]; False
[0, 0, 0, None, 0, None, 1, None, 1]; False
[0, 0, 0, None, 0, None, None, 0, 0]; False
[0, 0, 0, None, 0, None, None, 0, 1]; False
[0, 0, 0, None, 0, None, None, 1, 0]; False
[0, 0, 0, None, 0, None, None, 1, 1]; False
[0, 0, 0, None, 0, None, None, None, 0]; False
[0, 0, 0, None, 0, None, None, None, 1]; False
[0, 0, 0, None, 1, 0, 0, 0, 0]; False
[0, 0, 0, None, 1, 0, 0, 0, 1]; False
[0, 0, 0, None, 1, 0, 0, 1, 0]; False
[0, 0, 0, None, 1, 0, 0, 1, 1]; False
[0, 0, 0, None, 1, 0, 0, None, 0]; False
[0, 0, 0, None, 1, 0, 0, None, 1]; False
[0, 0, 0, None, 1, 0, 1, 0, 0]; False
[0, 0, 0, None, 1, 0, 1, 0, 1]; False
[0, 0, 0, None, 1, 0, 1, 1, 0]; False
[0, 0, 0, None, 1, 0, 1, 1, 1]; False
[0, 0, 0, None, 1, 0, 1, None, 0]; False
[0, 0, 0, None, 1, 0, 1, None, 1]; False
[0, 0, 0, None, 1, 0, None, 0, 0]; False
[0, 0, 0, None, 1, 0, None, 0, 1]; False
[0, 0, 0, None, 1, 0, None, 1, 0]; False
[0, 0, 0, None, 1, 0, None, 1, 1]; False
[0, 0, 0, None, 1, 0, None, None, 0]; False
[0, 0, 0, None, 1, 0, None, None, 1]; False
[0, 0, 0, None, 1, 1, 0, 0, 0]; False
[0, 0, 0, None, 1, 1, 0, 0, 1]; False
[0, 0, 0, None, 1, 1, 0, 1, 0]; False
[0, 0, 0, None, 1, 1, 0, 1, 1]; False
[0, 0, 0, None, 1, 1, 0, None, 0]; False
[0, 0, 0, None, 1, 1, 0, None, 1]; False
[0, 0, 0, None, 1, 1, 1, 0, 0]; False
[0, 0, 0, None, 1, 1, 1, 0, 1]; False
[0, 0, 0, None, 1, 1, 1, 1, 0]; False
[0, 0, 0, None, 1, 1, 1, 1, 1]; False
[0, 0, 0, None, 1, 1, 1, None, 0]; False
[0, 0, 0, None, 1, 1, 1, None, 1]; False
[0, 0, 0, None, 1, 1, None, 0, 0]; False
[0, 0, 0, None, 1, 1, None, 0, 1]; False
[0, 0, 0, None, 1, 1, None, 1, 0]; False
[0, 0, 0, None, 1, 1, None, 1, 1]; False
[0, 0, 0, None, 1, 1, None, None, 0]; False
[0, 0, 0, None, 1, 1, None, None, 1]; False
[0, 0, 0, None, 1, None, 0, 0, 0]; False
[0, 0, 0, None, 1, None, 0, 0, 1]; False
[0, 0, 0, None, 1, None, 0, 1, 0]; False
[0, 0, 0, None, 1, None, 0, 1, 1]; False
[0, 0, 0, None, 1, None, 0, None, 0]; False
[0, 0, 0, None, 1, None, 0, None, 1]; False
[0, 0, 0, None, 1, None, 1, 0, 0]; False
[0, 0, 0, None, 1, None, 1, 0, 1]; False
[0, 0, 0, None, 1, None, 1, 1, 0]; False
[0, 0, 0, None, 1, None, 1, 1, 1]; False
[0, 0, 0, None, 1, None, 1, None, 0]; False
[0, 0, 0, None, 1, None, 1, None, 1]; False
[0, 0, 0, None, 1, None, None, 0, 0]; False
[0, 0, 0, None, 1, None, None, 0, 1]; False
[0, 0, 0, None, 1, None, None, 1, 0]; False
[0, 0, 0, None, 1, None, None, 1, 1]; False
[0, 0, 0, None, 1, None, None, None, 0]; False
[0, 0, 0, None, 1, None, None, None, 1]; False
[0, 0, 0, None, None, 0, 0, 0, 0]; False
[0, 0, 0, None, None, 0, 0, 0, 1]; False
[0, 0, 0, None, None, 0, 0, 1, 0]; False
[0, 0, 0, None, None, 0, 0, 1, 1]; False
[0, 0, 0, None, None, 0, 0, None, 0]; False
[0, 0, 0, None, None, 0, 0, None, 1]; False
[0, 0, 0, None, None, 0, 1, 0, 0]; False
[0, 0, 0, None, None, 0, 1, 0, 1]; False
[0, 0, 0, None, None, 0, 1, 1, 0]; False
[0, 0, 0, None, None, 0, 1, 1, 1]; False
[0, 0, 0, None, None, 0, 1, None, 0]; False
[0, 0, 0, None, None, 0, 1, None, 1]; False
[0, 0, 0, None, None, 0, None, 0, 0]; False
[0, 0, 0, None, None, 0, None, 0, 1]; False
[0, 0, 0, None, None, 0, None, 1, 0]; False
[0, 0, 0, None, None, 0, None, 1, 1]; False
[0, 0, 0, None, None, 0, None, None, 0]; False
[0, 0, 0, None, None, 0, None, None, 1]; False
[0, 0, 0, None, None, 1, 0, 0, 0]; False
[0, 0, 0, None, None, 1, 0, 0, 1]; False
[0, 0, 0, None, None, 1, 0, 1, 0]; False
[0, 0, 0, None, None, 1, 0, 1, 1]; False
[0, 0, 0, None, None, 1, 0, None, 0]; False
[0, 0, 0, None, None, 1, 0, None, 1]; False
[0, 0, 0, None, None, 1, 1, 0, 0]; False
[0, 0, 0, None, None, 1, 1, 0, 1]; False
[0, 0, 0, None, None, 1, 1, 1, 0]; False
[0, 0, 0, None, None, 1, 1, 1, 1]; True
[0, 0, 0, None, None, 1, 1, None, 0]; False
[0, 0, 0, None, None, 1, 1, None, 1]; True
[0, 0, 0, None, None, 1, None, 0, 0]; False
[0, 0, 0, None, None, 1, None, 0, 1]; False
[0, 0, 0, None, None, 1, None, 1, 0]; False
[0, 0, 0, None, None, 1, None, 1, 1]; True
[0, 0, 0, None, None, 1, None, None, 0]; False
[0, 0, 0, None, None, 1, None, None, 1]; True
[0, 0, 0, None, None, None, 0, 0, 0]; False
[0, 0, 0, None, None, None, 0, 0, 1]; False
[0, 0, 0, None, None, None, 0, 1, 0]; False
[0, 0, 0, None, None, None, 0, 1, 1]; False
[0, 0, 0, None, None, None, 0, None, 0]; False
[0, 0, 0, None, None, None, 0, None, 1]; False
[0, 0, 0, None, None, None, 1, 0, 0]; False
[0, 0, 0, None, None, None, 1, 0, 1]; False
[0, 0, 0, None, None, None, 1, 1, 0]; False
[0, 0, 0, None, None, None, 1, 1, 1]; True
[0, 0, 0, None, None, None, 1, None, 0]; False
[0, 0, 0, None, None, None, 1, None, 1]; True
[0, 0, 1, 0, 0, 0, 0, 0, 0]; False
[0, 0, 1, 0, 0, 0, 0, 0, 1]; False
[0, 0, 1, 0, 0, 0, 0, 1, 0]; False
[0, 0, 1, 0, 0, 0, 0, 1, 1]; False
[0, 0, 1, 0, 0, 0, 0, None, 0]; False
[0, 0, 1, 0, 0, 0, 0, None, 1]; False
[0, 0, 1, 0, 0, 0, 1, 0, 0]; False
[0, 0, 1, 0, 0, 0, 1, 0, 1]; False
[0, 0, 1, 0, 0, 0, 1, 1, 0]; False
[0, 0, 1, 0, 0, 0, 1, 1, 1]; False
[0, 0, 1, 0, 0, 0, 1, None, 0]; False
[0, 0, 1, 0, 0, 0, 1, None, 1]; False
[0, 0, 1, 0, 0, 0, None, 0, 0]; False
[0, 0, 1, 0, 0, 0, None, 0, 1]; False
[0, 0, 1, 0, 0, 0, None, 1, 0]; False
[0, 0, 1, 0, 0, 0, None, 1, 1]; False
[0, 0, 1, 0, 0, 0, None, None, 0]; False
[0, 0, 1, 0, 0, 0, None, None, 1]; False
[0, 0, 1, 0, 0, 1, 0, 0, 0]; False
[0, 0, 1, 0, 0, 1, 0, 0, 1]; False
[0, 0, 1, 0, 0, 1, 0, 1, 0]; False
[0, 0, 1, 0, 0, 1, 0, 1, 1]; False
[0, 0, 1, 0, 0, 1, 0, None, 0]; False
[0, 0, 1, 0, 0, 1, 0, None, 1]; False
[0, 0, 1, 0, 0, 1, 1, 0, 0]; False
[0, 0, 1, 0, 0, 1, 1, 0, 1]; False
[0, 0, 1, 0, 0, 1, 1, 1, 0]; False
[0, 0, 1, 0, 0, 1, 1, 1, 1]; False
[0, 0, 1, 0, 0, 1, 1, None, 0]; False
[0, 0, 1, 0, 0, 1, 1, None, 1]; False
[0, 0, 1, 0, 0, 1, None, 0, 0]; False
[0, 0, 1, 0, 0, 1, None, 0, 1]; False
[0, 0, 1, 0, 0, 1, None, 1, 0]; False
[0, 0, 1, 0, 0, 1, None, 1, 1]; False
[0, 0, 1, 0, 0, 1, None, None, 0]; False
[0, 0, 1, 0, 0, 1, None, None, 1]; False
[0, 0, 1, 0, 0, None, 0, 0, 0]; False
[0, 0, 1, 0, 0, None, 0, 0, 1]; False
[0, 0, 1, 0, 0, None, 0, 1, 0]; False
[0, 0, 1, 0, 0, None, 0, 1, 1]; False
[0, 0, 1, 0, 0, None, 0, None, 0]; False
[0, 0, 1, 0, 0, None, 0, None, 1]; False
[0, 0, 1, 0, 0, None, 1, 0, 0]; False
[0, 0, 1, 0, 0, None, 1, 0, 1]; False
[0, 0, 1, 0, 0, None, 1, 1, 0]; False
[0, 0, 1, 0, 0, None, 1, 1, 1]; False
[0, 0, 1, 0, 0, None, 1, None, 0]; False
[0, 0, 1, 0, 0, None, 1, None, 1]; False
[0, 0, 1, 0, 0, None, None, 0, 0]; False
[0, 0, 1, 0, 0, None, None, 0, 1]; False
[0, 0, 1, 0, 0, None, None, 1, 0]; False
[0, 0, 1, 0, 0, None, None, 1, 1]; False
[0, 0, 1, 0, 0, None, None, None, 0]; False
[0, 0, 1, 0, 0, None, None, None, 1]; False
[0, 0, 1, 0, 1, 0, 0, 0, 0]; False
[0, 0, 1, 0, 1, 0, 0, 0, 1]; True
[0, 0, 1, 0, 1, 0, 0, 1, 0]; False
[0, 0, 1, 0, 1, 0, 0, 1, 1]; False
[0, 0, 1, 0, 1, 0, 0, None, 0]; False
[0, 0, 1, 0, 1, 0, 0, None, 1]; False
[0, 0, 1, 0, 1, 0, 1, 0, 0]; False
[0, 0, 1, 0, 1, 0, 1, 0, 1]; False
[0, 0, 1, 0, 1, 0, 1, 1, 0]; False
[0, 0, 1, 0, 1, 0, 1, 1, 1]; False
[0, 0, 1, 0, 1, 0, 1, None, 0]; False
[0, 0, 1, 0, 1, 0, 1, None, 1]; False
[0, 0, 1, 0, 1, 0, None, 0, 0]; False
[0, 0, 1, 0, 1, 0, None, 0, 1]; False
[0, 0, 1, 0, 1, 0, None, 1, 0]; False
[0, 0, 1, 0, 1, 0, None, 1, 1]; False
[0, 0, 1, 0, 1, 0, None, None, 0]; False
[0, 0, 1, 0, 1, 0, None, None, 1]; False
[0, 0, 1, 0, 1, 1, 0, 0, 0]; False
[0, 0, 1, 0, 1, 1, 0, 0, 1]; True
[0, 0, 1, 0, 1, 1, 0, 1, 0]; False
[0, 0, 1, 0, 1, 1, 0, 1, 1]; False
[0, 0, 1, 0, 1, 1, 0, None, 0]; False
[0, 0, 1, 0, 1, 1, 0, None, 1]; False
[0, 0, 1, 0, 1, 1, 1, 0, 0]; False
[0, 0, 1, 0, 1, 1, 1, 0, 1]; True
[0, 0, 1, 0, 1, 1, 1, 1, 0]; False
[0, 0, 1, 0, 1, 1, 1, 1, 1]; False
[0, 0, 1, 0, 1, 1, 1, None, 0]; False
[0, 0, 1, 0, 1, 1, 1, None, 1]; False
[0, 0, 1, 0, 1, 1, None, 0, 0]; False
[0, 0, 1, 0, 1, 1, None, 0, 1]; True
[0, 0, 1, 0, 1, 1, None, 1, 0]; False
[0, 0, 1, 0, 1, 1, None, 1, 1]; False
[0, 0, 1, 0, 1, 1, None, None, 0]; False
[0, 0, 1, 0, 1, 1, None, None, 1]; False
[0, 0, 1, 0, 1, None, 0, 0, 0]; False
[0, 0, 1, 0, 1, None, 0, 0, 1]; True
[0, 0, 1, 0, 1, None, 0, 1, 0]; False
[0, 0, 1, 0, 1, None, 0, 1, 1]; False
[0, 0, 1, 0, 1, None, 0, None, 0]; False
[0, 0, 1, 0, 1, None, 0, None, 1]; False
[0, 0, 1, 0, 1, None, 1, 0, 0]; False
[0, 0, 1, 0, 1, None, 1, 0, 1]; True
[0, 0, 1, 0, 1, None, 1, 1, 0]; False
[0, 0, 1, 0, 1, None, 1, 1, 1]; False
[0, 0, 1, 0, 1, None, 1, None, 0]; False
[0, 0, 1, 0, 1, None, 1, None, 1]; False
[0, 0, 1, 0, 1, None, None, 0, 0]; False
[0, 0, 1, 0, 1, None, None, 0, 1]; True
[0, 0, 1, 0, 1, None, None, 1, 0]; False
[0, 0, 1, 0, 1, None, None, 1, 1]; False
[0, 0, 1, 0, 1, None, None, None, 0]; False
[0, 0, 1, 0, 1, None, None, None, 1]; False
[0, 0, 1, 0, None, 0, 0, 0, 0]; False
[0, 0, 1, 0, None, 0, 0, 0, 1]; True
[0, 0, 1, 0, None, 0, 0, 1, 0]; False
[0, 0, 1, 0, None, 0, 0, 1, 1]; False
[0, 0, 1, 0, None, 0, 0, None, 0]; False
[0, 0, 1, 0, None, 0, 0, None, 1]; False
[0, 0, 1, 0, None, 0, 1, 0, 0]; False
[0, 0, 1, 0, None, 0, 1, 0, 1]; False
[0, 0, 1, 0, None, 0, 1, 1, 0]; False
[0, 0, 1, 0, None, 0, 1, 1, 1]; False
[0, 0, 1, 0, None, 0, 1, None, 0]; False
[0, 0, 1, 0, None, 0, 1, None, 1]; False
[0, 0, 1, 0, None, 0, None, 0, 0]; False
[0, 0, 1, 0, None, 0, None, 0, 1]; False
[0, 0, 1, 0, None, 0, None, 1, 0]; False
[0, 0, 1, 0, None, 0, None, 1, 1]; False
[0, 0, 1, 0, None, 0, None, None, 0]; False
[0, 0, 1, 0, None, 0, None, None, 1]; False
[0, 0, 1, 0, None, 1, 0, 0, 0]; False
[0, 0, 1, 0, None, 1, 0, 0, 1]; True
[0, 0, 1, 0, None, 1, 0, 1, 0]; False
[0, 0, 1, 0, None, 1, 0, 1, 1]; False
[0, 0, 1, 0, None, 1, 0, None, 0]; False
[0, 0, 1, 0, None, 1, 0, None, 1]; False
[0, 0, 1, 0, None, 1, 1, 0, 0]; False
[0, 0, 1, 0, None, 1, 1, 0, 1]; True
[0, 0, 1, 0, None, 1, 1, 1, 0]; False
[0, 0, 1, 0, None, 1, 1, 1, 1]; False
[0, 0, 1, 0, None, 1, 1, None, 0]; False
[0, 0, 1, 0, None, 1, 1, None, 1]; False
[0, 0, 1, 0, None, 1, None, 0, 0]; False
[0, 0, 1, 0, None, 1, None, 0, 1]; True
[0, 0, 1, 0, None, 1, None, 1, 0]; False
[0, 0, 1, 0, None, 1, None, 1, 1]; False
[0, 0, 1, 0, None, 1, None, None, 0]; False
[0, 0, 1, 0, None, 1, None, None, 1]; False
[0, 0, 1, 0, None, None, 0, 0, 0]; False
[0, 0, 1, 0, None, None, 0, 0, 1]; True
[0, 0, 1, 0, None, None, 0, 1, 0]; False
[0, 0, 1, 0, None, None, 0, 1, 1]; False
[0, 0, 1, 0, None, None, 0, None, 0]; False
[0, 0, 1, 0, None, None, 0, None, 1]; False
[0, 0, 1, 0, None, None, 1, 0, 0]; False
[0, 0, 1, 0, None, None, 1, 0, 1]; True
[0, 0, 1, 0, None, None, 1, 1, 0]; False
[0, 0, 1, 0, None, None, 1, 1, 1]; False
[0, 0, 1, 0, None, None, 1, None, 0]; False
[0, 0, 1, 0, None, None, 1, None, 1]; False
[0, 0, 1, 0, None, None, None, 0, 0]; False
[0, 0, 1, 0, None, None, None, 0, 1]; True
[0, 0, 1, 0, None, None, None, 1, 0]; False
[0, 0, 1, 0, None, None, None, 1, 1]; False
[0, 0, 1, 0, None, None, None, None, 0]; False
[0, 0, 1, 0, None, None, None, None, 1]; False
[0, 0, 1, 1, 0, 0, 0, 0, 0]; False
[0, 0, 1, 1, 0, 0, 0, 0, 1]; False
[0, 0, 1, 1, 0, 0, 0, 1, 0]; False
[0, 0, 1, 1, 0, 0, 0, 1, 1]; False
[0, 0, 1, 1, 0, 0, 0, None, 0]; False
[0, 0, 1, 1, 0, 0, 0, None, 1]; False
[0, 0, 1, 1, 0, 0, 1, 0, 0]; False
[0, 0, 1, 1, 0, 0, 1, 0, 1]; False
[0, 0, 1, 1, 0, 0, 1, 1, 0]; False
[0, 0, 1, 1, 0, 0, 1, 1, 1]; False
[0, 0, 1, 1, 0, 0, 1, None, 0]; False
[0, 0, 1, 1, 0, 0, 1, None, 1]; False
[0, 0, 1, 1, 0, 0, None, 0, 0]; False
[0, 0, 1, 1, 0, 0, None, 0, 1]; False
[0, 0, 1, 1, 0, 0, None, 1, 0]; False
[0, 0, 1, 1, 0, 0, None, 1, 1]; False
[0, 0, 1, 1, 0, 0, None, None, 0]; False
[0, 0, 1, 1, 0, 0, None, None, 1]; False
[0, 0, 1, 1, 0, 1, 0, 0, 0]; False
[0, 0, 1, 1, 0, 1, 0, 0, 1]; False
[0, 0, 1, 1, 0, 1, 0, 1, 0]; False
[0, 0, 1, 1, 0, 1, 0, 1, 1]; False
[0, 0, 1, 1, 0, 1, 0, None, 0]; False
[0, 0, 1, 1, 0, 1, 0, None, 1]; False
[0, 0, 1, 1, 0, 1, 1, 0, 0]; False
[0, 0, 1, 1, 0, 1, 1, 0, 1]; False
[0, 0, 1, 1, 0, 1, 1, 1, 0]; False
[0, 0, 1, 1, 0, 1, 1, 1, 1]; False
[0, 0, 1, 1, 0, 1, 1, None, 0]; False
[0, 0, 1, 1, 0, 1, 1, None, 1]; False
[0, 0, 1, 1, 0, 1, None, 0, 0]; False
[0, 0, 1, 1, 0, 1, None, 0, 1]; False
[0, 0, 1, 1, 0, 1, None, 1, 0]; False
[0, 0, 1, 1, 0, 1, None, 1, 1]; False
[0, 0, 1, 1, 0, 1, None, None, 0]; False
[0, 0, 1, 1, 0, 1, None, None, 1]; False
[0, 0, 1, 1, 0, None, 0, 0, 0]; False
[0, 0, 1, 1, 0, None, 0, 0, 1]; False
[0, 0, 1, 1, 0, None, 0, 1, 0]; False
[0, 0, 1, 1, 0, None, 0, 1, 1]; False
[0, 0, 1, 1, 0, None, 0, None, 0]; False
[0, 0, 1, 1, 0, None, 0, None, 1]; False
[0, 0, 1, 1, 0, None, 1, 0, 0]; False
[0, 0, 1, 1, 0, None, 1, 0, 1]; False
[0, 0, 1, 1, 0, None, 1, 1, 0]; False
[0, 0, 1, 1, 0, None, 1, 1, 1]; False
[0, 0, 1, 1, 0, None, 1, None, 0]; False
[0, 0, 1, 1, 0, None, 1, None, 1]; False
[0, 0, 1, 1, 0, None, None, 0, 0]; False
[0, 0, 1, 1, 0, None, None, 0, 1]; False
[0, 0, 1, 1, 0, None, None, 1, 0]; False
[0, 0, 1, 1, 0, None, None, 1, 1]; False
[0, 0, 1, 1, 0, None, None, None, 0]; False
[0, 0, 1, 1, 0, None, None, None, 1]; False
[0, 0, 1, 1, 1, 0, 0, 0, 0]; False
[0, 0, 1, 1, 1, 0, 0, 0, 1]; True
[0, 0, 1, 1, 1, 0, 0, 1, 0]; False
[0, 0, 1, 1, 1, 0, 0, 1, 1]; False
[0, 0, 1, 1, 1, 0, 0, None, 0]; False
[0, 0, 1, 1, 1, 0, 0, None, 1]; False
[0, 0, 1, 1, 1, 0, 1, 0, 0]; False
[0, 0, 1, 1, 1, 0, 1, 0, 1]; False
[0, 0, 1, 1, 1, 0, 1, 1, 0]; False
[0, 0, 1, 1, 1, 0, 1, 1, 1]; False
[0, 0, 1, 1, 1, 0, 1, None, 0]; False
[0, 0, 1, 1, 1, 0, 1, None, 1]; False
[0, 0, 1, 1, 1, 0, None, 0, 0]; False
[0, 0, 1, 1, 1, 0, None, 0, 1]; False
[0, 0, 1, 1, 1, 0, None, 1, 0]; False
[0, 0, 1, 1, 1, 0, None, 1, 1]; False
[0, 0, 1, 1, 1, 0, None, None, 0]; False
[0, 0, 1, 1, 1, 0, None, None, 1]; False
[0, 0, 1, 1, 1, 1, 0, 0, 0]; False
[0, 0, 1, 1, 1, 1, 0, 0, 1]; True
[0, 0, 1, 1, 1, 1, 0, 1, 0]; False
[0, 0, 1, 1, 1, 1, 0, 1, 1]; False
[0, 0, 1, 1, 1, 1, 0, None, 0]; False
[0, 0, 1, 1, 1, 1, 0, None, 1]; False
[0, 0, 1, 1, 1, 1, 1, 0, 0]; False
[0, 0, 1, 1, 1, 1, 1, 0, 1]; True
[0, 0, 1, 1, 1, 1, 1, 1, 0]; False
[0, 0, 1, 1, 1, 1, 1, 1, 1]; False
[0, 0, 1, 1, 1, 1, 1, None, 0]; False
[0, 0, 1, 1, 1, 1, 1, None, 1]; False
[0, 0, 1, 1, 1, 1, None, 0, 0]; False
[0, 0, 1, 1, 1, 1, None, 0, 1]; True
[0, 0, 1, 1, 1, 1, None, 1, 0]; False
[0, 0, 1, 1, 1, 1, None, 1, 1]; False
[0, 0, 1, 1, 1, 1, None, None, 0]; False
[0, 0, 1, 1, 1, 1, None, None, 1]; False
[0, 0, 1, 1, 1, None, 0, 0, 0]; False
[0, 0, 1, 1, 1, None, 0, 0, 1]; True
[0, 0, 1, 1, 1, None, 0, 1, 0]; False
[0, 0, 1, 1, 1, None, 0, 1, 1]; False
[0, 0, 1, 1, 1, None, 0, None, 0]; False
[0, 0, 1, 1, 1, None, 0, None, 1]; False
[0, 0, 1, 1, 1, None, 1, 0, 0]; False
[0, 0, 1, 1, 1, None, 1, 0, 1]; True
[0, 0, 1, 1, 1, None, 1, 1, 0]; False
[0, 0, 1, 1, 1, None, 1, 1, 1]; False
[0, 0, 1, 1, 1, None, 1, None, 0]; False
[0, 0, 1, 1, 1, None, 1, None, 1]; False
[0, 0, 1, 1, 1, None, None, 0, 0]; False
[0, 0, 1, 1, 1, None, None, 0, 1]; True
[0, 0, 1, 1, 1, None, None, 1, 0]; False
[0, 0, 1, 1, 1, None, None, 1, 1]; False
[0, 0, 1, 1, 1, None, None, None, 0]; False
[0, 0, 1, 1, 1, None, None, None, 1]; False
[0, 0, 1, 1, None, 0, 0, 0, 0]; False
[0, 0, 1, 1, None, 0, 0, 0, 1]; True
[0, 0, 1, 1, None, 0, 0, 1, 0]; False
[0, 0, 1, 1, None, 0, 0, 1, 1]; False
[0, 0, 1, 1, None, 0, 0, None, 0]; False
[0, 0, 1, 1, None, 0, 0, None, 1]; False
[0, 0, 1, 1, None, 0, 1, 0, 0]; False
[0, 0, 1, 1, None, 0, 1, 0, 1]; False
[0, 0, 1, 1, None, 0, 1, 1, 0]; False
[0, 0, 1, 1, None, 0, 1, 1, 1]; False
[0, 0, 1, 1, None, 0, 1, None, 0]; False
[0, 0, 1, 1, None, 0, 1, None, 1]; False
[0, 0, 1, 1, None, 0, None, 0, 0]; False
[0, 0, 1, 1, None, 0, None, 0, 1]; False
[0, 0, 1, 1, None, 0, None, 1, 0]; False
[0, 0, 1, 1, None, 0, None, 1, 1]; False
[0, 0, 1, 1, None, 0, None, None, 0]; False
[0, 0, 1, 1, None, 0, None, None, 1]; False
[0, 0, 1, 1, None, 1, 0, 0, 0]; False
[0, 0, 1, 1, None, 1, 0, 0, 1]; True
[0, 0, 1, 1, None, 1, 0, 1, 0]; False
[0, 0, 1, 1, None, 1, 0, 1, 1]; False
[0, 0, 1, 1, None, 1, 0, None, 0]; False
[0, 0, 1, 1, None, 1, 0, None, 1]; False
[0, 0, 1, 1, None, 1, 1, 0, 0]; False
[0, 0, 1, 1, None, 1, 1, 0, 1]; True
[0, 0, 1, 1, None, 1, 1, 1, 0]; False
[0, 0, 1, 1, None, 1, 1, 1, 1]; False
[0, 0, 1, 1, None, 1, 1, None, 0]; False
[0, 0, 1, 1, None, 1, 1, None, 1]; False
[0, 0, 1, 1, None, 1, None, 0, 0]; False
[0, 0, 1, 1, None, 1, None, 0, 1]; True
[0, 0, 1, 1, None, 1, None, 1, 0]; False
[0, 0, 1, 1, None, 1, None, 1, 1]; False
[0, 0, 1, 1, None, 1, None, None, 0]; False
[0, 0, 1, 1, None, 1, None, None, 1]; False
[0, 0, 1, 1, None, None, 0, 0, 0]; False
[0, 0, 1, 1, None, None, 0, 0, 1]; True
[0, 0, 1, 1, None, None, 0, 1, 0]; False
[0, 0, 1, 1, None, None, 0, 1, 1]; False
[0, 0, 1, 1, None, None, 0, None, 0]; False
[0, 0, 1, 1, None, None, 0, None, 1]; False
[0, 0, 1, 1, None, None, 1, 0, 0]; False
[0, 0, 1, 1, None, None, 1, 0, 1]; True
[0, 0, 1, 1, None, None, 1, 1, 0]; False
[0, 0, 1, 1, None, None, 1, 1, 1]; False
[0, 0, 1, 1, None, None, 1, None, 0]; False
[0, 0, 1, 1, None, None, 1, None, 1]; False
[0, 0, 1, 1, None, None, None, 0, 0]; False
[0, 0, 1, 1, None, None, None, 0, 1]; True
[0, 0, 1, 1, None, None, None, 1, 0]; False
[0, 0, 1, 1, None, None, None, 1, 1]; False
[0, 0, 1, 1, None, None, None, None, 0]; False
[0, 0, 1, 1, None, None, None, None, 1]; False
[0, 0, 1, None, 0, 0, 0, 0, 0]; False
[0, 0, 1, None, 0, 0, 0, 0, 1]; False
[0, 0, 1, None, 0, 0, 0, 1, 0]; False
[0, 0, 1, None, 0, 0, 0, 1, 1]; False
[0, 0, 1, None, 0, 0, 0, None, 0]; False
[0, 0, 1, None, 0, 0, 0, None, 1]; False
[0, 0, 1, None, 0, 0, 1, 0, 0]; False
[0, 0, 1, None, 0, 0, 1, 0, 1]; False
[0, 0, 1, None, 0, 0, 1, 1, 0]; False
[0, 0, 1, None, 0, 0, 1, 1, 1]; False
[0, 0, 1, None, 0, 0, 1, None, 0]; False
[0, 0, 1, None, 0, 0, 1, None, 1]; False
[0, 0, 1, None, 0, 0, None, 0, 0]; False
[0, 0, 1, None, 0, 0, None, 0, 1]; False
[0, 0, 1, None, 0, 0, None, 1, 0]; False
[0, 0, 1, None, 0, 0, None, 1, 1]; False
[0, 0, 1, None, 0, 0, None, None, 0]; False
[0, 0, 1, None, 0, 0, None, None, 1]; False
[0, 0, 1, None, 0, 1, 0, 0, 0]; False
[0, 0, 1, None, 0, 1, 0, 0, 1]; False
[0, 0, 1, None, 0, 1, 0, 1, 0]; False
[0, 0, 1, None, 0, 1, 0, 1, 1]; False
[0, 0, 1, None, 0, 1, 0, None, 0]; False
[0, 0, 1, None, 0, 1, 0, None, 1]; False
[0, 0, 1, None, 0, 1, 1, 0, 0]; False
[0, 0, 1, None, 0, 1, 1, 0, 1]; False
[0, 0, 1, None, 0, 1, 1, 1, 0]; False
[0, 0, 1, None, 0, 1, 1, 1, 1]; False
[0, 0, 1, None, 0, 1, 1, None, 0]; False
[0, 0, 1, None, 0, 1, 1, None, 1]; False
[0, 0, 1, None, 0, 1, None, 0, 0]; False
[0, 0, 1, None, 0, 1, None, 0, 1]; False
[0, 0, 1, None, 0, 1, None, 1, 0]; False
[0, 0, 1, None, 0, 1, None, 1, 1]; False
[0, 0, 1, None, 0, 1, None, None, 0]; False
[0, 0, 1, None, 0, 1, None, None, 1]; False
[0, 0, 1, None, 0, None, 0, 0, 0]; False
[0, 0, 1, None, 0, None, 0, 0, 1]; False
[0, 0, 1, None, 0, None, 0, 1, 0]; False
[0, 0, 1, None, 0, None, 0, 1, 1]; False
[0, 0, 1, None, 0, None, 0, None, 0]; False
[0, 0, 1, None, 0, None, 0, None, 1]; False
[0, 0, 1, None, 0, None, 1, 0, 0]; False
[0, 0, 1, None, 0, None, 1, 0, 1]; False
[0, 0, 1, None, 0, None, 1, 1, 0]; False
[0, 0, 1, None, 0, None, 1, 1, 1]; False
[0, 0, 1, None, 0, None, 1, None, 0]; False
[0, 0, 1, None, 0, None, 1, None, 1]; False
[0, 0, 1, None, 0, None, None, 0, 0]; False
[0, 0, 1, None, 0, None, None, 0, 1]; False
[0, 0, 1, None, 0, None, None, 1, 0]; False
[0, 0, 1, None, 0, None, None, 1, 1]; False
[0, 0, 1, None, 0, None, None, None, 0]; False
[0, 0, 1, None, 0, None, None, None, 1]; False
[0, 0, 1, None, 1, 0, 0, 0, 0]; False
[0, 0, 1, None, 1, 0, 0, 0, 1]; False
[0, 0, 1, None, 1, 0, 0, 1, 0]; False
[0, 0, 1, None, 1, 0, 0, 1, 1]; False
[0, 0, 1, None, 1, 0, 0, None, 0]; False
[0, 0, 1, None, 1, 0, 0, None, 1]; False
[0, 0, 1, None, 1, 0, 1, 0, 0]; False
[0, 0, 1, None, 1, 0, 1, 0, 1]; False
[0, 0, 1, None, 1, 0, 1, 1, 0]; False
[0, 0, 1, None, 1, 0, 1, 1, 1]; False
[0, 0, 1, None, 1, 0, 1, None, 0]; False
[0, 0, 1, None, 1, 0, 1, None, 1]; False
[0, 0, 1, None, 1, 0, None, 0, 0]; False
[0, 0, 1, None, 1, 0, None, 0, 1]; False
[0, 0, 1, None, 1, 0, None, 1, 0]; False
[0, 0, 1, None, 1, 0, None, 1, 1]; False
[0, 0, 1, None, 1, 0, None, None, 0]; False
[0, 0, 1, None, 1, 0, None, None, 1]; False
[0, 0, 1, None, 1, 1, 0, 0, 0]; False
[0, 0, 1, None, 1, 1, 0, 0, 1]; False
[0, 0, 1, None, 1, 1, 0, 1, 0]; False
[0, 0, 1, None, 1, 1, 0, 1, 1]; False
[0, 0, 1, None, 1, 1, 0, None, 0]; False
[0, 0, 1, None, 1, 1, 0, None, 1]; False
[0, 0, 1, None, 1, 1, 1, 0, 0]; False
[0, 0, 1, None, 1, 1, 1, 0, 1]; False
[0, 0, 1, None, 1, 1, 1, 1, 0]; False
[0, 0, 1, None, 1, 1, 1, 1, 1]; False
[0, 0, 1, None, 1, 1, 1, None, 0]; False
[0, 0, 1, None, 1, 1, 1, None, 1]; False
[0, 0, 1, None, 1, 1, None, 0, 0]; False
[0, 0, 1, None, 1, 1, None, 0, 1]; False
[0, 0, 1, None, 1, 1, None, 1, 0]; False
[0, 0, 1, None, 1, 1, None, 1, 1]; False
[0, 0, 1, None, 1, 1, None, None, 0]; False
[0, 0, 1, None, 1, 1, None, None, 1]; False
[0, 0, 1, None, 1, None, 0, 0, 0]; False
[0, 0, 1, None, 1, None, 0, 0, 1]; False
[0, 0, 1, None, 1, None, 0, 1, 0]; False
[0, 0, 1, None, 1, None, 0, 1, 1]; False
[0, 0, 1, None, 1, None, 0, None, 0]; False
[0, 0, 1, None, 1, None, 0, None, 1]; False
[0, 0, 1, None, 1, None, 1, 0, 0]; False
[0, 0, 1, None, 1, None, 1, 0, 1]; False
[0, 0, 1, None, 1, None, 1, 1, 0]; False
[0, 0, 1, None, 1, None, 1, 1, 1]; False
[0, 0, 1, None, 1, None, 1, None, 0]; False
[0, 0, 1, None, 1, None, 1, None, 1]; False
[0, 0, 1, None, 1, None, None, 0, 0]; False
[0, 0, 1, None, 1, None, None, 0, 1]; False
[0, 0, 1, None, 1, None, None, 1, 0]; False
[0, 0, 1, None, 1, None, None, 1, 1]; False
[0, 0, 1, None, 1, None, None, None, 0]; False
[0, 0, 1, None, 1, None, None, None, 1]; False
[0, 0, 1, None, None, 0, 0, 0, 0]; False
[0, 0, 1, None, None, 0, 0, 0, 1]; False
[0, 0, 1, None, None, 0, 0, 1, 0]; False
[0, 0, 1, None, None, 0, 0, 1, 1]; False
[0, 0, 1, None, None, 0, 0, None, 0]; False
[0, 0, 1, None, None, 0, 0, None, 1]; False
[0, 0, 1, None, None, 0, 1, 0, 0]; False
[0, 0, 1, None, None, 0, 1, 0, 1]; False
[0, 0, 1, None, None, 0, 1, 1, 0]; False
[0, 0, 1, None, None, 0, 1, 1, 1]; True
[0, 0, 1, None, None, 0, 1, None, 0]; False
[0, 0, 1, None, None, 0, 1, None, 1]; True
[0, 0, 1, None, None, 0, None, 0, 0]; False
[0, 0, 1, None, None, 0, None, 0, 1]; False
[0, 0, 1, None, None, 0, None, 1, 0]; False
[0, 0, 1, None, None, 0, None, 1, 1]; True
[0, 0, 1, None, None, 0, None, None, 0]; False
[0, 0, 1, None, None, 0, None, None, 1]; True
[0, 0, 1, None, None, 1, 0, 0, 0]; False
[0, 0, 1, None, None, 1, 0, 0, 1]; False
[0, 0, 1, None, None, 1, 0, 1, 0]; False
[0, 0, 1, None, None, 1, 0, 1, 1]; True
[0, 0, 1, None, None, 1, 0, None, 0]; False
[0, 0, 1, None, None, 1, 0, None, 1]; True
[0, 0, 1, None, None, 1, 1, 0, 0]; False
[0, 0, 1, None, None, 1, 1, 0, 1]; False
[0, 0, 1, None, None, 1, 1, 1, 0]; True
[0, 0, 1, None, None, 1, 1, 1, 1]; True
[0, 0, 1, None, None, 1, 1, None, 0]; True
[0, 0, 1, None, None, 1, 1, None, 1]; True
[0, 0, 1, None, None, 1, None, 0, 0]; False
[0, 0, 1, None, None, 1, None, 0, 1]; False
[0, 0, 1, None, None, 1, None, 1, 0]; True
[0, 0, 1, None, None, 1, None, 1, 1]; True
[0, 0, 1, None, None, 1, None, None, 0]; True
[0, 0, 1, None, None, 1, None, None, 1]; True
[0, 0, 1, None, None, None, 0, 0, 0]; False
[0, 0, 1, None, None, None, 0, 0, 1]; False
[0, 0, 1, None, None, None, 0, 1, 0]; False
[0, 0, 1, None, None, None, 0, 1, 1]; True
[0, 0, 1, None, None, None, 0, None, 0]; False
[0, 0, 1, None, None, None, 0, None, 1]; True
[0, 0, 1, None, None, None, 1, 0, 0]; False
[0, 0, 1, None, None, None, 1, 0, 1]; True
[0, 0, 1, None, None, None, 1, 1, 0]; True
[0, 0, 1, None, None, None, 1, 1, 1]; True
[0, 0, 1, None, None, None, 1, None, 0]; True
[0, 0, 1, None, None, None, 1, None, 1]; True
[0, 0, None, 0, 0, 0, 0, 0, 0]; False
[0, 0, None, 0, 0, 0, 0, 0, 1]; False
[0, 0, None, 0, 0, 0, 0, 1, 0]; False
[0, 0, None, 0, 0, 0, 0, 1, 1]; False
[0, 0, None, 0, 0, 0, 0, None, 0]; False
[0, 0, None, 0, 0, 0, 0, None, 1]; False
[0, 0, None, 0, 0, 0, 1, 0, 0]; False
[0, 0, None, 0, 0, 0, 1, 0, 1]; False
[0, 0, None, 0, 0, 0, 1, 1, 0]; True
[0, 0, None, 0, 0, 0, 1, 1, 1]; True
[0, 0, None, 0, 0, 0, 1, None, 0]; True
[0, 0, None, 0, 0, 0, 1, None, 1]; True
[0, 0, None, 0, 0, 0, None, 0, 0]; False
[0, 0, None, 0, 0, 0, None, 0, 1]; False
[0, 0, None, 0, 0, 0, None, 1, 0]; True
[0, 0, None, 0, 0, 0, None, 1, 1]; True
[0, 0, None, 0, 0, 0, None, None, 0]; True
[0, 0, None, 0, 0, 0, None, None, 1]; True
[0, 0, None, 0, 0, 1, 0, 0, 0]; False
[0, 0, None, 0, 0, 1, 0, 0, 1]; False
[0, 0, None, 0, 0, 1, 0, 1, 0]; False
[0, 0, None, 0, 0, 1, 0, 1, 1]; False
[0, 0, None, 0, 0, 1, 0, None, 0]; False
[0, 0, None, 0, 0, 1, 0, None, 1]; False
[0, 0, None, 0, 0, 1, 1, 0, 0]; False
[0, 0, None, 0, 0, 1, 1, 0, 1]; False
[0, 0, None, 0, 0, 1, 1, 1, 0]; False
[0, 0, None, 0, 0, 1, 1, 1, 1]; False
[0, 0, None, 0, 0, 1, 1, None, 0]; False
[0, 0, None, 0, 0, 1, 1, None, 1]; False
[0, 0, None, 0, 0, 1, None, 0, 0]; False
[0, 0, None, 0, 0, 1, None, 0, 1]; False
[0, 0, None, 0, 0, 1, None, 1, 0]; False
[0, 0, None, 0, 0, 1, None, 1, 1]; False
[0, 0, None, 0, 0, 1, None, None, 0]; False
[0, 0, None, 0, 0, 1, None, None, 1]; False
[0, 0, None, 0, 0, None, 0, 0, 0]; False
[0, 0, None, 0, 0, None, 0, 0, 1]; False
[0, 0, None, 0, 0, None, 0, 1, 0]; False
[0, 0, None, 0, 0, None, 0, 1, 1]; False
[0, 0, None, 0, 0, None, 0, None, 0]; False
[0, 0, None, 0, 0, None, 0, None, 1]; False
[0, 0, None, 0, 0, None, 1, 0, 0]; False
[0, 0, None, 0, 0, None, 1, 0, 1]; False
[0, 0, None, 0, 0, None, 1, 1, 0]; False
[0, 0, None, 0, 0, None, 1, 1, 1]; False
[0, 0, None, 0, 0, None, 1, None, 0]; False
[0, 0, None, 0, 0, None, 1, None, 1]; False
[0, 0, None, 0, 0, None, None, 0, 0]; False
[0, 0, None, 0, 0, None, None, 0, 1]; False
[0, 0, None, 0, 0, None, None, 1, 0]; False
[0, 0, None, 0, 0, None, None, 1, 1]; True
[0, 0, None, 0, 0, None, None, None, 0]; False
[0, 0, None, 0, 0, None, None, None, 1]; True
[0, 0, None, 0, 1, 0, 0, 0, 0]; False
[0, 0, None, 0, 1, 0, 0, 0, 1]; False
[0, 0, None, 0, 1, 0, 0, 1, 0]; False
[0, 0, None, 0, 1, 0, 0, 1, 1]; False
[0, 0, None, 0, 1, 0, 0, None, 0]; False
[0, 0, None, 0, 1, 0, 0, None, 1]; False
[0, 0, None, 0, 1, 0, 1, 0, 0]; True
[0, 0, None, 0, 1, 0, 1, 0, 1]; False
[0, 0, None, 0, 1, 0, 1, 1, 0]; True
[0, 0, None, 0, 1, 0, 1, 1, 1]; True
[0, 0, None, 0, 1, 0, 1, None, 0]; True
[0, 0, None, 0, 1, 0, 1, None, 1]; True
[0, 0, None, 0, 1, 0, None, 0, 0]; True
[0, 0, None, 0, 1, 0, None, 0, 1]; False
[0, 0, None, 0, 1, 0, None, 1, 0]; True
[0, 0, None, 0, 1, 0, None, 1, 1]; True
[0, 0, None, 0, 1, 0, None, None, 0]; True
[0, 0, None, 0, 1, 0, None, None, 1]; True
[0, 0, None, 0, 1, 1, 0, 0, 0]; False
[0, 0, None, 0, 1, 1, 0, 0, 1]; False
[0, 0, None, 0, 1, 1, 0, 1, 0]; False
[0, 0, None, 0, 1, 1, 0, 1, 1]; False
[0, 0, None, 0, 1, 1, 0, None, 0]; False
[0, 0, None, 0, 1, 1, 0, None, 1]; False
[0, 0, None, 0, 1, 1, 1, 0, 0]; False
[0, 0, None, 0, 1, 1, 1, 0, 1]; False
[0, 0, None, 0, 1, 1, 1, 1, 0]; False
[0, 0, None, 0, 1, 1, 1, 1, 1]; False
[0, 0, None, 0, 1, 1, 1, None, 0]; False
[0, 0, None, 0, 1, 1, 1, None, 1]; False
[0, 0, None, 0, 1, 1, None, 0, 0]; False
[0, 0, None, 0, 1, 1, None, 0, 1]; False
[0, 0, None, 0, 1, 1, None, 1, 0]; False
[0, 0, None, 0, 1, 1, None, 1, 1]; False
[0, 0, None, 0, 1, 1, None, None, 0]; False
[0, 0, None, 0, 1, 1, None, None, 1]; False
[0, 0, None, 0, 1, None, 0, 0, 0]; False
[0, 0, None, 0, 1, None, 0, 0, 1]; False
[0, 0, None, 0, 1, None, 0, 1, 0]; False
[0, 0, None, 0, 1, None, 0, 1, 1]; False
[0, 0, None, 0, 1, None, 0, None, 0]; False
[0, 0, None, 0, 1, None, 0, None, 1]; False
[0, 0, None, 0, 1, None, 1, 0, 0]; False
[0, 0, None, 0, 1, None, 1, 0, 1]; False
[0, 0, None, 0, 1, None, 1, 1, 0]; False
[0, 0, None, 0, 1, None, 1, 1, 1]; False
[0, 0, None, 0, 1, None, 1, None, 0]; False
[0, 0, None, 0, 1, None, 1, None, 1]; False
[0, 0, None, 0, 1, None, None, 0, 0]; False
[0, 0, None, 0, 1, None, None, 0, 1]; False
[0, 0, None, 0, 1, None, None, 1, 0]; True
[0, 0, None, 0, 1, None, None, 1, 1]; True
[0, 0, None, 0, 1, None, None, None, 0]; True
[0, 0, None, 0, 1, None, None, None, 1]; True
[0, 0, None, 0, None, 0, 0, 0, 0]; False
[0, 0, None, 0, None, 0, 0, 0, 1]; False
[0, 0, None, 0, None, 0, 0, 1, 0]; False
[0, 0, None, 0, None, 0, 0, 1, 1]; False
[0, 0, None, 0, None, 0, 0, None, 0]; False
[0, 0, None, 0, None, 0, 0, None, 1]; False
[0, 0, None, 0, None, 0, 1, 0, 0]; False
[0, 0, None, 0, None, 0, 1, 0, 1]; True
[0, 0, None, 0, None, 0, 1, 1, 0]; False
[0, 0, None, 0, None, 0, 1, 1, 1]; False
[0, 0, None, 0, None, 0, 1, None, 0]; False
[0, 0, None, 0, None, 0, 1, None, 1]; False
[0, 0, None, 0, None, 0, None, 0, 0]; False
[0, 0, None, 0, None, 0, None, 0, 1]; True
[0, 0, None, 0, None, 0, None, 1, 0]; False
[0, 0, None, 0, None, 0, None, 1, 1]; False
[0, 0, None, 0, None, 0, None, None, 0]; False
[0, 0, None, 0, None, 0, None, None, 1]; False
[0, 0, None, 0, None, 1, 0, 0, 0]; False
[0, 0, None, 0, None, 1, 0, 0, 1]; False
[0, 0, None, 0, None, 1, 0, 1, 0]; False
[0, 0, None, 0, None, 1, 0, 1, 1]; False
[0, 0, None, 0, None, 1, 0, None, 0]; False
[0, 0, None, 0, None, 1, 0, None, 1]; False
[0, 0, None, 0, None, 1, 1, 0, 0]; False
[0, 0, None, 0, None, 1, 1, 0, 1]; True
[0, 0, None, 0, None, 1, 1, 1, 0]; False
[0, 0, None, 0, None, 1, 1, 1, 1]; False
[0, 0, None, 0, None, 1, 1, None, 0]; False
[0, 0, None, 0, None, 1, 1, None, 1]; False
[0, 0, None, 0, None, 1, None, 0, 0]; False
[0, 0, None, 0, None, 1, None, 0, 1]; True
[0, 0, None, 0, None, 1, None, 1, 0]; False
[0, 0, None, 0, None, 1, None, 1, 1]; False
[0, 0, None, 0, None, 1, None, None, 0]; False
[0, 0, None, 0, None, 1, None, None, 1]; False
[0, 0, None, 0, None, None, 0, 0, 0]; False
[0, 0, None, 0, None, None, 0, 0, 1]; False
[0, 0, None, 0, None, None, 0, 1, 0]; False
[0, 0, None, 0, None, None, 0, 1, 1]; False
[0, 0, None, 0, None, None, 0, None, 0]; False
[0, 0, None, 0, None, None, 0, None, 1]; False
[0, 0, None, 0, None, None, 1, 0, 0]; False
[0, 0, None, 0, None, None, 1, 0, 1]; False
[0, 0, None, 0, None, None, 1, 1, 0]; False
[0, 0, None, 0, None, None, 1, 1, 1]; False
[0, 0, None, 0, None, None, 1, None, 0]; False
[0, 0, None, 0, None, None, 1, None, 1]; False
[0, 0, None, 1, 0, 0, 0, 0, 0]; False
[0, 0, None, 1, 0, 0, 0, 0, 1]; False
[0, 0, None, 1, 0, 0, 0, 1, 0]; False
[0, 0, None, 1, 0, 0, 0, 1, 1]; False
[0, 0, None, 1, 0, 0, 0, None, 0]; False
[0, 0, None, 1, 0, 0, 0, None, 1]; False
[0, 0, None, 1, 0, 0, 1, 0, 0]; False
[0, 0, None, 1, 0, 0, 1, 0, 1]; False
[0, 0, None, 1, 0, 0, 1, 1, 0]; False
[0, 0, None, 1, 0, 0, 1, 1, 1]; True
[0, 0, None, 1, 0, 0, 1, None, 0]; False
[0, 0, None, 1, 0, 0, 1, None, 1]; True
[0, 0, None, 1, 0, 0, None, 0, 0]; False
[0, 0, None, 1, 0, 0, None, 0, 1]; False
[0, 0, None, 1, 0, 0, None, 1, 0]; False
[0, 0, None, 1, 0, 0, None, 1, 1]; True
[0, 0, None, 1, 0, 0, None, None, 0]; False
[0, 0, None, 1, 0, 0, None, None, 1]; True
[0, 0, None, 1, 0, 1, 0, 0, 0]; False
[0, 0, None, 1, 0, 1, 0, 0, 1]; False
[0, 0, None, 1, 0, 1, 0, 1, 0]; False
[0, 0, None, 1, 0, 1, 0, 1, 1]; False
[0, 0, None, 1, 0, 1, 0, None, 0]; False
[0, 0, None, 1, 0, 1, 0, None, 1]; False
[0, 0, None, 1, 0, 1, 1, 0, 0]; False
[0, 0, None, 1, 0, 1, 1, 0, 1]; False
[0, 0, None, 1, 0, 1, 1, 1, 0]; False
[0, 0, None, 1, 0, 1, 1, 1, 1]; False
[0, 0, None, 1, 0, 1, 1, None, 0]; False
[0, 0, None, 1, 0, 1, 1, None, 1]; False
[0, 0, None, 1, 0, 1, None, 0, 0]; False
[0, 0, None, 1, 0, 1, None, 0, 1]; False
[0, 0, None, 1, 0, 1, None, 1, 0]; False
[0, 0, None, 1, 0, 1, None, 1, 1]; False
[0, 0, None, 1, 0, 1, None, None, 0]; False
[0, 0, None, 1, 0, 1, None, None, 1]; False
[0, 0, None, 1, 0, None, 0, 0, 0]; False
[0, 0, None, 1, 0, None, 0, 0, 1]; False
[0, 0, None, 1, 0, None, 0, 1, 0]; False
[0, 0, None, 1, 0, None, 0, 1, 1]; False
[0, 0, None, 1, 0, None, 0, None, 0]; False
[0, 0, None, 1, 0, None, 0, None, 1]; False
[0, 0, None, 1, 0, None, 1, 0, 0]; False
[0, 0, None, 1, 0, None, 1, 0, 1]; False
[0, 0, None, 1, 0, None, 1, 1, 0]; False
[0, 0, None, 1, 0, None, 1, 1, 1]; False
[0, 0, None, 1, 0, None, 1, None, 0]; False
[0, 0, None, 1, 0, None, 1, None, 1]; False
[0, 0, None, 1, 0, None, None, 0, 0]; False
[0, 0, None, 1, 0, None, None, 0, 1]; False
[0, 0, None, 1, 0, None, None, 1, 0]; False
[0, 0, None, 1, 0, None, None, 1, 1]; False
[0, 0, None, 1, 0, None, None, None, 0]; False
[0, 0, None, 1, 0, None, None, None, 1]; False
[0, 0, None, 1, 1, 0, 0, 0, 0]; False
[0, 0, None, 1, 1, 0, 0, 0, 1]; False
[0, 0, None, 1, 1, 0, 0, 1, 0]; False
[0, 0, None, 1, 1, 0, 0, 1, 1]; False
[0, 0, None, 1, 1, 0, 0, None, 0]; False
[0, 0, None, 1, 1, 0, 0, None, 1]; False
[0, 0, None, 1, 1, 0, 1, 0, 0]; False
[0, 0, None, 1, 1, 0, 1, 0, 1]; False
[0, 0, None, 1, 1, 0, 1, 1, 0]; True
[0, 0, None, 1, 1, 0, 1, 1, 1]; True
[0, 0, None, 1, 1, 0, 1, None, 0]; True
[0, 0, None, 1, 1, 0, 1, None, 1]; True
[0, 0, None, 1, 1, 0, None, 0, 0]; False
[0, 0, None, 1, 1, 0, None, 0, 1]; False
[0, 0, None, 1, 1, 0, None, 1, 0]; True
[0, 0, None, 1, 1, 0, None, 1, 1]; True
[0, 0, None, 1, 1, 0, None, None, 0]; True
[0, 0, None, 1, 1, 0, None, None, 1]; True
[0, 0, None, 1, 1, 1, 0, 0, 0]; False
[0, 0, None, 1, 1, 1, 0, 0, 1]; False
[0, 0, None, 1, 1, 1, 0, 1, 0]; False
[0, 0, None, 1, 1, 1, 0, 1, 1]; False
[0, 0, None, 1, 1, 1, 0, None, 0]; False
[0, 0, None, 1, 1, 1, 0, None, 1]; False
[0, 0, None, 1, 1, 1, 1, 0, 0]; False
[0, 0, None, 1, 1, 1, 1, 0, 1]; False
[0, 0, None, 1, 1, 1, 1, 1, 0]; False
[0, 0, None, 1, 1, 1, 1, 1, 1]; False
[0, 0, None, 1, 1, 1, 1, None, 0]; False
[0, 0, None, 1, 1, 1, 1, None, 1]; False
[0, 0, None, 1, 1, 1, None, 0, 0]; False
[0, 0, None, 1, 1, 1, None, 0, 1]; False
[0, 0, None, 1, 1, 1, None, 1, 0]; False
[0, 0, None, 1, 1, 1, None, 1, 1]; False
[0, 0, None, 1, 1, 1, None, None, 0]; False
[0, 0, None, 1, 1, 1, None, None, 1]; False
[0, 0, None, 1, 1, None, 0, 0, 0]; False
[0, 0, None, 1, 1, None, 0, 0, 1]; False
[0, 0, None, 1, 1, None, 0, 1, 0]; False
[0, 0, None, 1, 1, None, 0, 1, 1]; False
[0, 0, None, 1, 1, None, 0, None, 0]; False
[0, 0, None, 1, 1, None, 0, None, 1]; False
[0, 0, None, 1, 1, None, 1, 0, 0]; False
[0, 0, None, 1, 1, None, 1, 0, 1]; False
[0, 0, None, 1, 1, None, 1, 1, 0]; False
[0, 0, None, 1, 1, None, 1, 1, 1]; False
[0, 0, None, 1, 1, None, 1, None, 0]; False
[0, 0, None, 1, 1, None, 1, None, 1]; False
[0, 0, None, 1, 1, None, None, 0, 0]; False
[0, 0, None, 1, 1, None, None, 0, 1]; False
[0, 0, None, 1, 1, None, None, 1, 0]; False
[0, 0, None, 1, 1, None, None, 1, 1]; False
[0, 0, None, 1, 1, None, None, None, 0]; False
[0, 0, None, 1, 1, None, None, None, 1]; False
[0, 0, None, 1, None, 0, 0, 0, 0]; False
[0, 0, None, 1, None, 0, 0, 0, 1]; False
[0, 0, None, 1, None, 0, 0, 1, 0]; False
[0, 0, None, 1, None, 0, 0, 1, 1]; False
[0, 0, None, 1, None, 0, 0, None, 0]; False
[0, 0, None, 1, None, 0, 0, None, 1]; False
[0, 0, None, 1, None, 0, 1, 0, 0]; False
[0, 0, None, 1, None, 0, 1, 0, 1]; True
[0, 0, None, 1, None, 0, 1, 1, 0]; False
[0, 0, None, 1, None, 0, 1, 1, 1]; False
[0, 0, None, 1, None, 0, 1, None, 0]; False
[0, 0, None, 1, None, 0, 1, None, 1]; False
[0, 0, None, 1, None, 0, None, 0, 0]; False
[0, 0, None, 1, None, 0, None, 0, 1]; True
[0, 0, None, 1, None, 0, None, 1, 0]; False
[0, 0, None, 1, None, 0, None, 1, 1]; False
[0, 0, None, 1, None, 0, None, None, 0]; False
[0, 0, None, 1, None, 0, None, None, 1]; False
[0, 0, None, 1, None, 1, 0, 0, 0]; False
[0, 0, None, 1, None, 1, 0, 0, 1]; False
[0, 0, None, 1, None, 1, 0, 1, 0]; False
[0, 0, None, 1, None, 1, 0, 1, 1]; False
[0, 0, None, 1, None, 1, 0, None, 0]; False
[0, 0, None, 1, None, 1, 0, None, 1]; False
[0, 0, None, 1, None, 1, 1, 0, 0]; False
[0, 0, None, 1, None, 1, 1, 0, 1]; True
[0, 0, None, 1, None, 1, 1, 1, 0]; False
[0, 0, None, 1, None, 1, 1, 1, 1]; False
[0, 0, None, 1, None, 1, 1, None, 0]; False
[0, 0, None, 1, None, 1, 1, None, 1]; False
[0, 0, None, 1, None, 1, None, 0, 0]; False
[0, 0, None, 1, None, 1, None, 0, 1]; True
[0, 0, None, 1, None, 1, None, 1, 0]; False
[0, 0, None, 1, None, 1, None, 1, 1]; False
[0, 0, None, 1, None, 1, None, None, 0]; False
[0, 0, None, 1, None, 1, None, None, 1]; False
[0, 0, None, 1, None, None, 0, 0, 0]; False
[0, 0, None, 1, None, None, 0, 0, 1]; False
[0, 0, None, 1, None, None, 0, 1, 0]; False
[0, 0, None, 1, None, None, 0, 1, 1]; False
[0, 0, None, 1, None, None, 0, None, 0]; False
[0, 0, None, 1, None, None, 0, None, 1]; False
[0, 0, None, 1, None, None, 1, 0, 0]; False
[0, 0, None, 1, None, None, 1, 0, 1]; False
[0, 0, None, 1, None, None, 1, 1, 0]; False
[0, 0, None, 1, None, None, 1, 1, 1]; False
[0, 0, None, 1, None, None, 1, None, 0]; False
[0, 0, None, 1, None, None, 1, None, 1]; False
[0, 0, None, None, 0, 0, 0, 0, 0]; False
[0, 0, None, None, 0, 0, 0, 0, 1]; False
[0, 0, None, None, 0, 0, 0, 1, 0]; False
[0, 0, None, None, 0, 0, 0, 1, 1]; False
[0, 0, None, None, 0, 0, 0, None, 0]; False
[0, 0, None, None, 0, 0, 0, None, 1]; False
[0, 0, None, None, 0, 0, 1, 0, 0]; False
[0, 0, None, None, 0, 0, 1, 0, 1]; False
[0, 0, None, None, 0, 0, 1, 1, 0]; False
[0, 0, None, None, 0, 0, 1, 1, 1]; False
[0, 0, None, None, 0, 0, 1, None, 0]; False
[0, 0, None, None, 0, 0, 1, None, 1]; False
[0, 0, None, None, 0, 0, None, 0, 0]; False
[0, 0, None, None, 0, 0, None, 0, 1]; False
[0, 0, None, None, 0, 0, None, 1, 0]; False
[0, 0, None, None, 0, 0, None, 1, 1]; False
[0, 0, None, None, 0, 0, None, None, 0]; False
[0, 0, None, None, 0, 0, None, None, 1]; False
[0, 0, None, None, 0, 1, 0, 0, 0]; False
[0, 0, None, None, 0, 1, 0, 0, 1]; False
[0, 0, None, None, 0, 1, 0, 1, 0]; False
[0, 0, None, None, 0, 1, 0, 1, 1]; False
[0, 0, None, None, 0, 1, 0, None, 0]; False
[0, 0, None, None, 0, 1, 0, None, 1]; False
[0, 0, None, None, 0, 1, 1, 0, 0]; False
[0, 0, None, None, 0, 1, 1, 0, 1]; False
[0, 0, None, None, 0, 1, 1, 1, 0]; False
[0, 0, None, None, 0, 1, 1, 1, 1]; False
[0, 0, None, None, 0, 1, 1, None, 0]; False
[0, 0, None, None, 0, 1, 1, None, 1]; False
[0, 0, None, None, 0, 1, None, 0, 0]; False
[0, 0, None, None, 0, 1, None, 0, 1]; False
[0, 0, None, None, 0, 1, None, 1, 0]; False
[0, 0, None, None, 0, 1, None, 1, 1]; False
[0, 0, None, None, 0, 1, None, None, 0]; False
[0, 0, None, None, 0, 1, None, None, 1]; False
[0, 0, None, None, 0, None, 0, 0, 0]; False
[0, 0, None, None, 0, None, 0, 0, 1]; False
[0, 0, None, None, 0, None, 0, 1, 0]; False
[0, 0, None, None, 0, None, 0, 1, 1]; False
[0, 0, None, None, 0, None, 0, None, 0]; False
[0, 0, None, None, 0, None, 0, None, 1]; False
[0, 0, None, None, 0, None, 1, 0, 0]; False
[0, 0, None, None, 0, None, 1, 0, 1]; False
[0, 0, None, None, 0, None, 1, 1, 0]; False
[0, 0, None, None, 0, None, 1, 1, 1]; False
[0, 0, None, None, 0, None, 1, None, 0]; False
[0, 0, None, None, 0, None, 1, None, 1]; False
[0, 0, None, None, 1, 0, 0, 0, 0]; False
[0, 0, None, None, 1, 0, 0, 0, 1]; False
[0, 0, None, None, 1, 0, 0, 1, 0]; False
[0, 0, None, None, 1, 0, 0, 1, 1]; False
[0, 0, None, None, 1, 0, 0, None, 0]; False
[0, 0, None, None, 1, 0, 0, None, 1]; False
[0, 0, None, None, 1, 0, 1, 0, 0]; False
[0, 0, None, None, 1, 0, 1, 0, 1]; False
[0, 0, None, None, 1, 0, 1, 1, 0]; False
[0, 0, None, None, 1, 0, 1, 1, 1]; False
[0, 0, None, None, 1, 0, 1, None, 0]; False
[0, 0, None, None, 1, 0, 1, None, 1]; False
[0, 0, None, None, 1, 0, None, 0, 0]; False
[0, 0, None, None, 1, 0, None, 0, 1]; False
[0, 0, None, None, 1, 0, None, 1, 0]; False
[0, 0, None, None, 1, 0, None, 1, 1]; False
[0, 0, None, None, 1, 0, None, None, 0]; False
[0, 0, None, None, 1, 0, None, None, 1]; False
[0, 0, None, None, 1, 1, 0, 0, 0]; False
[0, 0, None, None, 1, 1, 0, 0, 1]; False
[0, 0, None, None, 1, 1, 0, 1, 0]; False
[0, 0, None, None, 1, 1, 0, 1, 1]; False
[0, 0, None, None, 1, 1, 0, None, 0]; False
[0, 0, None, None, 1, 1, 0, None, 1]; False
[0, 0, None, None, 1, 1, 1, 0, 0]; False
[0, 0, None, None, 1, 1, 1, 0, 1]; False
[0, 0, None, None, 1, 1, 1, 1, 0]; False
[0, 0, None, None, 1, 1, 1, 1, 1]; False
[0, 0, None, None, 1, 1, 1, None, 0]; False
[0, 0, None, None, 1, 1, 1, None, 1]; False
[0, 0, None, None, 1, 1, None, 0, 0]; False
[0, 0, None, None, 1, 1, None, 0, 1]; False
[0, 0, None, None, 1, 1, None, 1, 0]; False
[0, 0, None, None, 1, 1, None, 1, 1]; False
[0, 0, None, None, 1, 1, None, None, 0]; False
[0, 0, None, None, 1, 1, None, None, 1]; False
[0, 0, None, None, 1, None, 0, 0, 0]; False
[0, 0, None, None, 1, None, 0, 0, 1]; False
[0, 0, None, None, 1, None, 0, 1, 0]; False
[0, 0, None, None, 1, None, 0, 1, 1]; False
[0, 0, None, None, 1, None, 0, None, 0]; False
[0, 0, None, None, 1, None, 0, None, 1]; False
[0, 0, None, None, 1, None, 1, 0, 0]; False
[0, 0, None, None, 1, None, 1, 0, 1]; False
[0, 0, None, None, 1, None, 1, 1, 0]; False
[0, 0, None, None, 1, None, 1, 1, 1]; False
[0, 0, None, None, 1, None, 1, None, 0]; False
[0, 0, None, None, 1, None, 1, None, 1]; False
[0, 1, 0, 0, 0, 0, 0, 0, 0]; False
[0, 1, 0, 0, 0, 0, 0, 0, 1]; False
[0, 1, 0, 0, 0, 0, 0, 1, 0]; False
[0, 1, 0, 0, 0, 0, 0, 1, 1]; False
[0, 1, 0, 0, 0, 0, 0, None, 0]; False
[0, 1, 0, 0, 0, 0, 0, None, 1]; False
[0, 1, 0, 0, 0, 0, 1, 0, 0]; False
[0, 1, 0, 0, 0, 0, 1, 0, 1]; False
[0, 1, 0, 0, 0, 0, 1, 1, 0]; False
[0, 1, 0, 0, 0, 0, 1, 1, 1]; False
[0, 1, 0, 0, 0, 0, 1, None, 0]; False
[0, 1, 0, 0, 0, 0, 1, None, 1]; False
[0, 1, 0, 0, 0, 0, None, 0, 0]; False
[0, 1, 0, 0, 0, 0, None, 0, 1]; False
[0, 1, 0, 0, 0, 0, None, 1, 0]; False
[0, 1, 0, 0, 0, 0, None, 1, 1]; False
[0, 1, 0, 0, 0, 0, None, None, 0]; False
[0, 1, 0, 0, 0, 0, None, None, 1]; False
[0, 1, 0, 0, 0, 1, 0, 0, 0]; False
[0, 1, 0, 0, 0, 1, 0, 0, 1]; False
[0, 1, 0, 0, 0, 1, 0, 1, 0]; False
[0, 1, 0, 0, 0, 1, 0, 1, 1]; False
[0, 1, 0, 0, 0, 1, 0, None, 0]; False
[0, 1, 0, 0, 0, 1, 0, None, 1]; False
[0, 1, 0, 0, 0, 1, 1, 0, 0]; False
[0, 1, 0, 0, 0, 1, 1, 0, 1]; False
[0, 1, 0, 0, 0, 1, 1, 1, 0]; False
[0, 1, 0, 0, 0, 1, 1, 1, 1]; False
[0, 1, 0, 0, 0, 1, 1, None, 0]; False
[0, 1, 0, 0, 0, 1, 1, None, 1]; False
[0, 1, 0, 0, 0, 1, None, 0, 0]; False
[0, 1, 0, 0, 0, 1, None, 0, 1]; False
[0, 1, 0, 0, 0, 1, None, 1, 0]; False
[0, 1, 0, 0, 0, 1, None, 1, 1]; False
[0, 1, 0, 0, 0, 1, None, None, 0]; False
[0, 1, 0, 0, 0, 1, None, None, 1]; False
[0, 1, 0, 0, 0, None, 0, 0, 0]; False
[0, 1, 0, 0, 0, None, 0, 0, 1]; False
[0, 1, 0, 0, 0, None, 0, 1, 0]; False
[0, 1, 0, 0, 0, None, 0, 1, 1]; False
[0, 1, 0, 0, 0, None, 0, None, 0]; False
[0, 1, 0, 0, 0, None, 0, None, 1]; False
[0, 1, 0, 0, 0, None, 1, 0, 0]; False
[0, 1, 0, 0, 0, None, 1, 0, 1]; False
[0, 1, 0, 0, 0, None, 1, 1, 0]; False
[0, 1, 0, 0, 0, None, 1, 1, 1]; False
[0, 1, 0, 0, 0, None, 1, None, 0]; False
[0, 1, 0, 0, 0, None, 1, None, 1]; False
[0, 1, 0, 0, 0, None, None, 0, 0]; False
[0, 1, 0, 0, 0, None, None, 0, 1]; False
[0, 1, 0, 0, 0, None, None, 1, 0]; False
[0, 1, 0, 0, 0, None, None, 1, 1]; False
[0, 1, 0, 0, 0, None, None, None, 0]; False
[0, 1, 0, 0, 0, None, None, None, 1]; False
[0, 1, 0, 0, 1, 0, 0, 0, 0]; False
[0, 1, 0, 0, 1, 0, 0, 0, 1]; False
[0, 1, 0, 0, 1, 0, 0, 1, 0]; False
[0, 1, 0, 0, 1, 0, 0, 1, 1]; False
[0, 1, 0, 0, 1, 0, 0, None, 0]; False
[0, 1, 0, 0, 1, 0, 0, None, 1]; False
[0, 1, 0, 0, 1, 0, 1, 0, 0]; False
[0, 1, 0, 0, 1, 0, 1, 0, 1]; False
[0, 1, 0, 0, 1, 0, 1, 1, 0]; False
[0, 1, 0, 0, 1, 0, 1, 1, 1]; False
[0, 1, 0, 0, 1, 0, 1, None, 0]; False
[0, 1, 0, 0, 1, 0, 1, None, 1]; False
[0, 1, 0, 0, 1, 0, None, 0, 0]; False
[0, 1, 0, 0, 1, 0, None, 0, 1]; False
[0, 1, 0, 0, 1, 0, None, 1, 0]; False
[0, 1, 0, 0, 1, 0, None, 1, 1]; False
[0, 1, 0, 0, 1, 0, None, None, 0]; False
[0, 1, 0, 0, 1, 0, None, None, 1]; False
[0, 1, 0, 0, 1, 1, 0, 0, 0]; False
[0, 1, 0, 0, 1, 1, 0, 0, 1]; True
[0, 1, 0, 0, 1, 1, 0, 1, 0]; False
[0, 1, 0, 0, 1, 1, 0, 1, 1]; False
[0, 1, 0, 0, 1, 1, 0, None, 0]; False
[0, 1, 0, 0, 1, 1, 0, None, 1]; False
[0, 1, 0, 0, 1, 1, 1, 0, 0]; False
[0, 1, 0, 0, 1, 1, 1, 0, 1]; True
[0, 1, 0, 0, 1, 1, 1, 1, 0]; False
[0, 1, 0, 0, 1, 1, 1, 1, 1]; False
[0, 1, 0, 0, 1, 1, 1, None, 0]; False
[0, 1, 0, 0, 1, 1, 1, None, 1]; False
[0, 1, 0, 0, 1, 1, None, 0, 0]; False
[0, 1, 0, 0, 1, 1, None, 0, 1]; True
[0, 1, 0, 0, 1, 1, None, 1, 0]; False
[0, 1, 0, 0, 1, 1, None, 1, 1]; False
[0, 1, 0, 0, 1, 1, None, None, 0]; False
[0, 1, 0, 0, 1, 1, None, None, 1]; False
[0, 1, 0, 0, 1, None, 0, 0, 0]; False
[0, 1, 0, 0, 1, None, 0, 0, 1]; True
[0, 1, 0, 0, 1, None, 0, 1, 0]; False
[0, 1, 0, 0, 1, None, 0, 1, 1]; False
[0, 1, 0, 0, 1, None, 0, None, 0]; False
[0, 1, 0, 0, 1, None, 0, None, 1]; False
[0, 1, 0, 0, 1, None, 1, 0, 0]; False
[0, 1, 0, 0, 1, None, 1, 0, 1]; True
[0, 1, 0, 0, 1, None, 1, 1, 0]; False
[0, 1, 0, 0, 1, None, 1, 1, 1]; False
[0, 1, 0, 0, 1, None, 1, None, 0]; False
[0, 1, 0, 0, 1, None, 1, None, 1]; False
[0, 1, 0, 0, 1, None, None, 0, 0]; False
[0, 1, 0, 0, 1, None, None, 0, 1]; False
[0, 1, 0, 0, 1, None, None, 1, 0]; False
[0, 1, 0, 0, 1, None, None, 1, 1]; False
[0, 1, 0, 0, 1, None, None, None, 0]; False
[0, 1, 0, 0, 1, None, None, None, 1]; False
[0, 1, 0, 0, None, 0, 0, 0, 0]; False
[0, 1, 0, 0, None, 0, 0, 0, 1]; False
[0, 1, 0, 0, None, 0, 0, 1, 0]; False
[0, 1, 0, 0, None, 0, 0, 1, 1]; False
[0, 1, 0, 0, None, 0, 0, None, 0]; False
[0, 1, 0, 0, None, 0, 0, None, 1]; False
[0, 1, 0, 0, None, 0, 1, 0, 0]; False
[0, 1, 0, 0, None, 0, 1, 0, 1]; False
[0, 1, 0, 0, None, 0, 1, 1, 0]; False
[0, 1, 0, 0, None, 0, 1, 1, 1]; False
[0, 1, 0, 0, None, 0, 1, None, 0]; False
[0, 1, 0, 0, None, 0, 1, None, 1]; False
[0, 1, 0, 0, None, 0, None, 0, 0]; False
[0, 1, 0, 0, None, 0, None, 0, 1]; False
[0, 1, 0, 0, None, 0, None, 1, 0]; False
[0, 1, 0, 0, None, 0, None, 1, 1]; False
[0, 1, 0, 0, None, 0, None, None, 0]; False
[0, 1, 0, 0, None, 0, None, None, 1]; False
[0, 1, 0, 0, None, 1, 0, 0, 0]; False
[0, 1, 0, 0, None, 1, 0, 0, 1]; True
[0, 1, 0, 0, None, 1, 0, 1, 0]; False
[0, 1, 0, 0, None, 1, 0, 1, 1]; False
[0, 1, 0, 0, None, 1, 0, None, 0]; False
[0, 1, 0, 0, None, 1, 0, None, 1]; False
[0, 1, 0, 0, None, 1, 1, 0, 0]; False
[0, 1, 0, 0, None, 1, 1, 0, 1]; True
[0, 1, 0, 0, None, 1, 1, 1, 0]; False
[0, 1, 0, 0, None, 1, 1, 1, 1]; False
[0, 1, 0, 0, None, 1, 1, None, 0]; False
[0, 1, 0, 0, None, 1, 1, None, 1]; False
[0, 1, 0, 0, None, 1, None, 0, 0]; False
[0, 1, 0, 0, None, 1, None, 0, 1]; True
[0, 1, 0, 0, None, 1, None, 1, 0]; False
[0, 1, 0, 0, None, 1, None, 1, 1]; False
[0, 1, 0, 0, None, 1, None, None, 0]; False
[0, 1, 0, 0, None, 1, None, None, 1]; False
[0, 1, 0, 0, None, None, 0, 0, 0]; False
[0, 1, 0, 0, None, None, 0, 0, 1]; True
[0, 1, 0, 0, None, None, 0, 1, 0]; False
[0, 1, 0, 0, None, None, 0, 1, 1]; False
[0, 1, 0, 0, None, None, 0, None, 0]; False
[0, 1, 0, 0, None, None, 0, None, 1]; False
[0, 1, 0, 0, None, None, 1, 0, 0]; False
[0, 1, 0, 0, None, None, 1, 0, 1]; True
[0, 1, 0, 0, None, None, 1, 1, 0]; False
[0, 1, 0, 0, None, None, 1, 1, 1]; False
[0, 1, 0, 0, None, None, 1, None, 0]; False
[0, 1, 0, 0, None, None, 1, None, 1]; False
[0, 1, 0, 0, None, None, None, 0, 0]; False
[0, 1, 0, 0, None, None, None, 0, 1]; False
[0, 1, 0, 0, None, None, None, 1, 0]; False
[0, 1, 0, 0, None, None, None, 1, 1]; False
[0, 1, 0, 0, None, None, None, None, 0]; False
[0, 1, 0, 0, None, None, None, None, 1]; False
[0, 1, 0, 1, 0, 0, 0, 0, 0]; False
[0, 1, 0, 1, 0, 0, 0, 0, 1]; False
[0, 1, 0, 1, 0, 0, 0, 1, 0]; False
[0, 1, 0, 1, 0, 0, 0, 1, 1]; False
[0, 1, 0, 1, 0, 0, 0, None, 0]; False
[0, 1, 0, 1, 0, 0, 0, None, 1]; False
[0, 1, 0, 1, 0, 0, 1, 0, 0]; False
[0, 1, 0, 1, 0, 0, 1, 0, 1]; False
[0, 1, 0, 1, 0, 0, 1, 1, 0]; False
[0, 1, 0, 1, 0, 0, 1, 1, 1]; False
[0, 1, 0, 1, 0, 0, 1, None, 0]; False
[0, 1, 0, 1, 0, 0, 1, None, 1]; False
[0, 1, 0, 1, 0, 0, None, 0, 0]; False
[0, 1, 0, 1, 0, 0, None, 0, 1]; False
[0, 1, 0, 1, 0, 0, None, 1, 0]; False
[0, 1, 0, 1, 0, 0, None, 1, 1]; False
[0, 1, 0, 1, 0, 0, None, None, 0]; False
[0, 1, 0, 1, 0, 0, None, None, 1]; False
[0, 1, 0, 1, 0, 1, 0, 0, 0]; False
[0, 1, 0, 1, 0, 1, 0, 0, 1]; False
[0, 1, 0, 1, 0, 1, 0, 1, 0]; False
[0, 1, 0, 1, 0, 1, 0, 1, 1]; False
[0, 1, 0, 1, 0, 1, 0, None, 0]; False
[0, 1, 0, 1, 0, 1, 0, None, 1]; False
[0, 1, 0, 1, 0, 1, 1, 0, 0]; False
[0, 1, 0, 1, 0, 1, 1, 0, 1]; False
[0, 1, 0, 1, 0, 1, 1, 1, 0]; False
[0, 1, 0, 1, 0, 1, 1, 1, 1]; False
[0, 1, 0, 1, 0, 1, 1, None, 0]; False
[0, 1, 0, 1, 0, 1, 1, None, 1]; False
[0, 1, 0, 1, 0, 1, None, 0, 0]; False
[0, 1, 0, 1, 0, 1, None, 0, 1]; False
[0, 1, 0, 1, 0, 1, None, 1, 0]; False
[0, 1, 0, 1, 0, 1, None, 1, 1]; False
[0, 1, 0, 1, 0, 1, None, None, 0]; False
[0, 1, 0, 1, 0, 1, None, None, 1]; False
[0, 1, 0, 1, 0, None, 0, 0, 0]; False
[0, 1, 0, 1, 0, None, 0, 0, 1]; False
[0, 1, 0, 1, 0, None, 0, 1, 0]; False
[0, 1, 0, 1, 0, None, 0, 1, 1]; False
[0, 1, 0, 1, 0, None, 0, None, 0]; False
[0, 1, 0, 1, 0, None, 0, None, 1]; False
[0, 1, 0, 1, 0, None, 1, 0, 0]; False
[0, 1, 0, 1, 0, None, 1, 0, 1]; False
[0, 1, 0, 1, 0, None, 1, 1, 0]; False
[0, 1, 0, 1, 0, None, 1, 1, 1]; False
[0, 1, 0, 1, 0, None, 1, None, 0]; False
[0, 1, 0, 1, 0, None, 1, None, 1]; False
[0, 1, 0, 1, 0, None, None, 0, 0]; False
[0, 1, 0, 1, 0, None, None, 0, 1]; False
[0, 1, 0, 1, 0, None, None, 1, 0]; False
[0, 1, 0, 1, 0, None, None, 1, 1]; False
[0, 1, 0, 1, 0, None, None, None, 0]; False
[0, 1, 0, 1, 0, None, None, None, 1]; False
[0, 1, 0, 1, 1, 0, 0, 0, 0]; False
[0, 1, 0, 1, 1, 0, 0, 0, 1]; False
[0, 1, 0, 1, 1, 0, 0, 1, 0]; False
[0, 1, 0, 1, 1, 0, 0, 1, 1]; False
[0, 1, 0, 1, 1, 0, 0, None, 0]; False
[0, 1, 0, 1, 1, 0, 0, None, 1]; False
[0, 1, 0, 1, 1, 0, 1, 0, 0]; False
[0, 1, 0, 1, 1, 0, 1, 0, 1]; False
[0, 1, 0, 1, 1, 0, 1, 1, 0]; False
[0, 1, 0, 1, 1, 0, 1, 1, 1]; False
[0, 1, 0, 1, 1, 0, 1, None, 0]; False
[0, 1, 0, 1, 1, 0, 1, None, 1]; False
[0, 1, 0, 1, 1, 0, None, 0, 0]; False
[0, 1, 0, 1, 1, 0, None, 0, 1]; False
[0, 1, 0, 1, 1, 0, None, 1, 0]; False
[0, 1, 0, 1, 1, 0, None, 1, 1]; False
[0, 1, 0, 1, 1, 0, None, None, 0]; False
[0, 1, 0, 1, 1, 0, None, None, 1]; False
[0, 1, 0, 1, 1, 1, 0, 0, 0]; False
[0, 1, 0, 1, 1, 1, 0, 0, 1]; False
[0, 1, 0, 1, 1, 1, 0, 1, 0]; False
[0, 1, 0, 1, 1, 1, 0, 1, 1]; False
[0, 1, 0, 1, 1, 1, 0, None, 0]; False
[0, 1, 0, 1, 1, 1, 0, None, 1]; False
[0, 1, 0, 1, 1, 1, 1, 0, 0]; False
[0, 1, 0, 1, 1, 1, 1, 0, 1]; True
[0, 1, 0, 1, 1, 1, 1, 1, 0]; False
[0, 1, 0, 1, 1, 1, 1, 1, 1]; False
[0, 1, 0, 1, 1, 1, 1, None, 0]; False
[0, 1, 0, 1, 1, 1, 1, None, 1]; False
[0, 1, 0, 1, 1, 1, None, 0, 0]; False
[0, 1, 0, 1, 1, 1, None, 0, 1]; True
[0, 1, 0, 1, 1, 1, None, 1, 0]; False
[0, 1, 0, 1, 1, 1, None, 1, 1]; False
[0, 1, 0, 1, 1, 1, None, None, 0]; False
[0, 1, 0, 1, 1, 1, None, None, 1]; False
[0, 1, 0, 1, 1, None, 0, 0, 0]; False
[0, 1, 0, 1, 1, None, 0, 0, 1]; False
[0, 1, 0, 1, 1, None, 0, 1, 0]; False
[0, 1, 0, 1, 1, None, 0, 1, 1]; False
[0, 1, 0, 1, 1, None, 0, None, 0]; False
[0, 1, 0, 1, 1, None, 0, None, 1]; False
[0, 1, 0, 1, 1, None, 1, 0, 0]; False
[0, 1, 0, 1, 1, None, 1, 0, 1]; True
[0, 1, 0, 1, 1, None, 1, 1, 0]; False
[0, 1, 0, 1, 1, None, 1, 1, 1]; False
[0, 1, 0, 1, 1, None, 1, None, 0]; False
[0, 1, 0, 1, 1, None, 1, None, 1]; False
[0, 1, 0, 1, 1, None, None, 0, 0]; False
[0, 1, 0, 1, 1, None, None, 0, 1]; False
[0, 1, 0, 1, 1, None, None, 1, 0]; False
[0, 1, 0, 1, 1, None, None, 1, 1]; False
[0, 1, 0, 1, 1, None, None, None, 0]; False
[0, 1, 0, 1, 1, None, None, None, 1]; False
[0, 1, 0, 1, None, 0, 0, 0, 0]; False
[0, 1, 0, 1, None, 0, 0, 0, 1]; False
[0, 1, 0, 1, None, 0, 0, 1, 0]; False
[0, 1, 0, 1, None, 0, 0, 1, 1]; False
[0, 1, 0, 1, None, 0, 0, None, 0]; False
[0, 1, 0, 1, None, 0, 0, None, 1]; False
[0, 1, 0, 1, None, 0, 1, 0, 0]; False
[0, 1, 0, 1, None, 0, 1, 0, 1]; False
[0, 1, 0, 1, None, 0, 1, 1, 0]; False
[0, 1, 0, 1, None, 0, 1, 1, 1]; False
[0, 1, 0, 1, None, 0, 1, None, 0]; False
[0, 1, 0, 1, None, 0, 1, None, 1]; False
[0, 1, 0, 1, None, 0, None, 0, 0]; False
[0, 1, 0, 1, None, 0, None, 0, 1]; False
[0, 1, 0, 1, None, 0, None, 1, 0]; False
[0, 1, 0, 1, None, 0, None, 1, 1]; False
[0, 1, 0, 1, None, 0, None, None, 0]; False
[0, 1, 0, 1, None, 0, None, None, 1]; False
[0, 1, 0, 1, None, 1, 0, 0, 0]; False
[0, 1, 0, 1, None, 1, 0, 0, 1]; False
[0, 1, 0, 1, None, 1, 0, 1, 0]; False
[0, 1, 0, 1, None, 1, 0, 1, 1]; False
[0, 1, 0, 1, None, 1, 0, None, 0]; False
[0, 1, 0, 1, None, 1, 0, None, 1]; False
[0, 1, 0, 1, None, 1, 1, 0, 0]; False
[0, 1, 0, 1, None, 1, 1, 0, 1]; True
[0, 1, 0, 1, None, 1, 1, 1, 0]; False
[0, 1, 0, 1, None, 1, 1, 1, 1]; False
[0, 1, 0, 1, None, 1, 1, None, 0]; False
[0, 1, 0, 1, None, 1, 1, None, 1]; False
[0, 1, 0, 1, None, 1, None, 0, 0]; False
[0, 1, 0, 1, None, 1, None, 0, 1]; True
[0, 1, 0, 1, None, 1, None, 1, 0]; False
[0, 1, 0, 1, None, 1, None, 1, 1]; False
[0, 1, 0, 1, None, 1, None, None, 0]; False
[0, 1, 0, 1, None, 1, None, None, 1]; False
[0, 1, 0, 1, None, None, 0, 0, 0]; False
[0, 1, 0, 1, None, None, 0, 0, 1]; False
[0, 1, 0, 1, None, None, 0, 1, 0]; False
[0, 1, 0, 1, None, None, 0, 1, 1]; False
[0, 1, 0, 1, None, None, 0, None, 0]; False
[0, 1, 0, 1, None, None, 0, None, 1]; False
[0, 1, 0, 1, None, None, 1, 0, 0]; False
[0, 1, 0, 1, None, None, 1, 0, 1]; True
[0, 1, 0, 1, None, None, 1, 1, 0]; False
[0, 1, 0, 1, None, None, 1, 1, 1]; False
[0, 1, 0, 1, None, None, 1, None, 0]; False
[0, 1, 0, 1, None, None, 1, None, 1]; False
[0, 1, 0, 1, None, None, None, 0, 0]; False
[0, 1, 0, 1, None, None, None, 0, 1]; False
[0, 1, 0, 1, None, None, None, 1, 0]; False
[0, 1, 0, 1, None, None, None, 1, 1]; False
[0, 1, 0, 1, None, None, None, None, 0]; False
[0, 1, 0, 1, None, None, None, None, 1]; False
[0, 1, 0, None, 0, 0, 0, 0, 0]; False
[0, 1, 0, None, 0, 0, 0, 0, 1]; False
[0, 1, 0, None, 0, 0, 0, 1, 0]; False
[0, 1, 0, None, 0, 0, 0, 1, 1]; False
[0, 1, 0, None, 0, 0, 0, None, 0]; False
[0, 1, 0, None, 0, 0, 0, None, 1]; False
[0, 1, 0, None, 0, 0, 1, 0, 0]; False
[0, 1, 0, None, 0, 0, 1, 0, 1]; False
[0, 1, 0, None, 0, 0, 1, 1, 0]; False
[0, 1, 0, None, 0, 0, 1, 1, 1]; False
[0, 1, 0, None, 0, 0, 1, None, 0]; False
[0, 1, 0, None, 0, 0, 1, None, 1]; False
[0, 1, 0, None, 0, 0, None, 0, 0]; False
[0, 1, 0, None, 0, 0, None, 0, 1]; False
[0, 1, 0, None, 0, 0, None, 1, 0]; False
[0, 1, 0, None, 0, 0, None, 1, 1]; False
[0, 1, 0, None, 0, 0, None, None, 0]; False
[0, 1, 0, None, 0, 0, None, None, 1]; False
[0, 1, 0, None, 0, 1, 0, 0, 0]; False
[0, 1, 0, None, 0, 1, 0, 0, 1]; False
[0, 1, 0, None, 0, 1, 0, 1, 0]; False
[0, 1, 0, None, 0, 1, 0, 1, 1]; False
[0, 1, 0, None, 0, 1, 0, None, 0]; False
[0, 1, 0, None, 0, 1, 0, None, 1]; False
[0, 1, 0, None, 0, 1, 1, 0, 0]; False
[0, 1, 0, None, 0, 1, 1, 0, 1]; False
[0, 1, 0, None, 0, 1, 1, 1, 0]; False
[0, 1, 0, None, 0, 1, 1, 1, 1]; False
[0, 1, 0, None, 0, 1, 1, None, 0]; False
[0, 1, 0, None, 0, 1, 1, None, 1]; False
[0, 1, 0, None, 0, 1, None, 0, 0]; False
[0, 1, 0, None, 0, 1, None, 0, 1]; False
[0, 1, 0, None, 0, 1, None, 1, 0]; False
[0, 1, 0, None, 0, 1, None, 1, 1]; False
[0, 1, 0, None, 0, 1, None, None, 0]; False
[0, 1, 0, None, 0, 1, None, None, 1]; False
[0, 1, 0, None, 0, None, 0, 0, 0]; False
[0, 1, 0, None, 0, None, 0, 0, 1]; False
[0, 1, 0, None, 0, None, 0, 1, 0]; False
[0, 1, 0, None, 0, None, 0, 1, 1]; False
[0, 1, 0, None, 0, None, 0, None, 0]; False
[0, 1, 0, None, 0, None, 0, None, 1]; False
[0, 1, 0, None, 0, None, 1, 0, 0]; False
[0, 1, 0, None, 0, None, 1, 0, 1]; False
[0, 1, 0, None, 0, None, 1, 1, 0]; False
[0, 1, 0, None, 0, None, 1, 1, 1]; False
[0, 1, 0, None, 0, None, 1, None, 0]; False
[0, 1, 0, None, 0, None, 1, None, 1]; False
[0, 1, 0, None, 0, None, None, 0, 0]; False
[0, 1, 0, None, 0, None, None, 0, 1]; False
[0, 1, 0, None, 0, None, None, 1, 0]; False
[0, 1, 0, None, 0, None, None, 1, 1]; False
[0, 1, 0, None, 0, None, None, None, 0]; False
[0, 1, 0, None, 0, None, None, None, 1]; False
[0, 1, 0, None, 1, 0, 0, 0, 0]; False
[0, 1, 0, None, 1, 0, 0, 0, 1]; False
[0, 1, 0, None, 1, 0, 0, 1, 0]; False
[0, 1, 0, None, 1, 0, 0, 1, 1]; False
[0, 1, 0, None, 1, 0, 0, None, 0]; False
[0, 1, 0, None, 1, 0, 0, None, 1]; False
[0, 1, 0, None, 1, 0, 1, 0, 0]; False
[0, 1, 0, None, 1, 0, 1, 0, 1]; False
[0, 1, 0, None, 1, 0, 1, 1, 0]; False
[0, 1, 0, None, 1, 0, 1, 1, 1]; False
[0, 1, 0, None, 1, 0, 1, None, 0]; False
[0, 1, 0, None, 1, 0, 1, None, 1]; False
[0, 1, 0, None, 1, 0, None, 0, 0]; False
[0, 1, 0, None, 1, 0, None, 0, 1]; False
[0, 1, 0, None, 1, 0, None, 1, 0]; False
[0, 1, 0, None, 1, 0, None, 1, 1]; False
[0, 1, 0, None, 1, 0, None, None, 0]; False
[0, 1, 0, None, 1, 0, None, None, 1]; False
[0, 1, 0, None, 1, 1, 0, 0, 0]; False
[0, 1, 0, None, 1, 1, 0, 0, 1]; False
[0, 1, 0, None, 1, 1, 0, 1, 0]; False
[0, 1, 0, None, 1, 1, 0, 1, 1]; False
[0, 1, 0, None, 1, 1, 0, None, 0]; False
[0, 1, 0, None, 1, 1, 0, None, 1]; False
[0, 1, 0, None, 1, 1, 1, 0, 0]; False
[0, 1, 0, None, 1, 1, 1, 0, 1]; False
[0, 1, 0, None, 1, 1, 1, 1, 0]; False
[0, 1, 0, None, 1, 1, 1, 1, 1]; False
[0, 1, 0, None, 1, 1, 1, None, 0]; False
[0, 1, 0, None, 1, 1, 1, None, 1]; False
[0, 1, 0, None, 1, 1, None, 0, 0]; False
[0, 1, 0, None, 1, 1, None, 0, 1]; False
[0, 1, 0, None, 1, 1, None, 1, 0]; False
[0, 1, 0, None, 1, 1, None, 1, 1]; False
[0, 1, 0, None, 1, 1, None, None, 0]; False
[0, 1, 0, None, 1, 1, None, None, 1]; False
[0, 1, 0, None, 1, None, 0, 0, 0]; False
[0, 1, 0, None, 1, None, 0, 0, 1]; False
[0, 1, 0, None, 1, None, 0, 1, 0]; False
[0, 1, 0, None, 1, None, 0, 1, 1]; False
[0, 1, 0, None, 1, None, 0, None, 0]; False
[0, 1, 0, None, 1, None, 0, None, 1]; False
[0, 1, 0, None, 1, None, 1, 0, 0]; False
[0, 1, 0, None, 1, None, 1, 0, 1]; False
[0, 1, 0, None, 1, None, 1, 1, 0]; False
[0, 1, 0, None, 1, None, 1, 1, 1]; False
[0, 1, 0, None, 1, None, 1, None, 0]; False
[0, 1, 0, None, 1, None, 1, None, 1]; False
[0, 1, 0, None, 1, None, None, 0, 0]; False
[0, 1, 0, None, 1, None, None, 0, 1]; False
[0, 1, 0, None, 1, None, None, 1, 0]; False
[0, 1, 0, None, 1, None, None, 1, 1]; False
[0, 1, 0, None, 1, None, None, None, 0]; False
[0, 1, 0, None, 1, None, None, None, 1]; False
[0, 1, 0, None, None, 0, 0, 0, 0]; False
[0, 1, 0, None, None, 0, 0, 0, 1]; False
[0, 1, 0, None, None, 0, 0, 1, 0]; False
[0, 1, 0, None, None, 0, 0, 1, 1]; False
[0, 1, 0, None, None, 0, 0, None, 0]; False
[0, 1, 0, None, None, 0, 0, None, 1]; False
[0, 1, 0, None, None, 0, 1, 0, 0]; False
[0, 1, 0, None, None, 0, 1, 0, 1]; False
[0, 1, 0, None, None, 0, 1, 1, 0]; False
[0, 1, 0, None, None, 0, 1, 1, 1]; False
[0, 1, 0, None, None, 0, 1, None, 0]; False
[0, 1, 0, None, None, 0, 1, None, 1]; False
[0, 1, 0, None, None, 0, None, 0, 0]; False
[0, 1, 0, None, None, 0, None, 0, 1]; False
[0, 1, 0, None, None, 0, None, 1, 0]; False
[0, 1, 0, None, None, 0, None, 1, 1]; False
[0, 1, 0, None, None, 0, None, None, 0]; False
[0, 1, 0, None, None, 0, None, None, 1]; False
[0, 1, 0, None, None, 1, 0, 0, 0]; False
[0, 1, 0, None, None, 1, 0, 0, 1]; False
[0, 1, 0, None, None, 1, 0, 1, 0]; False
[0, 1, 0, None, None, 1, 0, 1, 1]; False
[0, 1, 0, None, None, 1, 0, None, 0]; False
[0, 1, 0, None, None, 1, 0, None, 1]; False
[0, 1, 0, None, None, 1, 1, 0, 0]; False
[0, 1, 0, None, None, 1, 1, 0, 1]; False
[0, 1, 0, None, None, 1, 1, 1, 0]; False
[0, 1, 0, None, None, 1, 1, 1, 1]; False
[0, 1, 0, None, None, 1, 1, None, 0]; False
[0, 1, 0, None, None, 1, 1, None, 1]; False
[0, 1, 0, None, None, 1, None, 0, 0]; False
[0, 1, 0, None, None, 1, None, 0, 1]; False
[0, 1, 0, None, None, 1, None, 1, 0]; False
[0, 1, 0, None, None, 1, None, 1, 1]; False
[0, 1, 0, None, None, 1, None, None, 0]; False
[0, 1, 0, None, None, 1, None, None, 1]; False
[0, 1, 0, None, None, None, 0, 0, 0]; False
[0, 1, 0, None, None, None, 0, 0, 1]; False
[0, 1, 0, None, None, None, 0, 1, 0]; False
[0, 1, 0, None, None, None, 0, 1, 1]; False
[0, 1, 0, None, None, None, 0, None, 0]; False
[0, 1, 0, None, None, None, 0, None, 1]; False
[0, 1, 0, None, None, None, 1, 0, 0]; False
[0, 1, 0, None, None, None, 1, 0, 1]; False
[0, 1, 0, None, None, None, 1, 1, 0]; False
[0, 1, 0, None, None, None, 1, 1, 1]; False
[0, 1, 0, None, None, None, 1, None, 0]; False
[0, 1, 0, None, None, None, 1, None, 1]; False
[0, 1, 1, 0, 0, 0, 0, 0, 0]; False
[0, 1, 1, 0, 0, 0, 0, 0, 1]; False
[0, 1, 1, 0, 0, 0, 0, 1, 0]; False
[0, 1, 1, 0, 0, 0, 0, 1, 1]; False
[0, 1, 1, 0, 0, 0, 0, None, 0]; False
[0, 1, 1, 0, 0, 0, 0, None, 1]; False
[0, 1, 1, 0, 0, 0, 1, 0, 0]; False
[0, 1, 1, 0, 0, 0, 1, 0, 1]; False
[0, 1, 1, 0, 0, 0, 1, 1, 0]; False
[0, 1, 1, 0, 0, 0, 1, 1, 1]; False
[0, 1, 1, 0, 0, 0, 1, None, 0]; False
[0, 1, 1, 0, 0, 0, 1, None, 1]; False
[0, 1, 1, 0, 0, 0, None, 0, 0]; False
[0, 1, 1, 0, 0, 0, None, 0, 1]; False
[0, 1, 1, 0, 0, 0, None, 1, 0]; False
[0, 1, 1, 0, 0, 0, None, 1, 1]; False
[0, 1, 1, 0, 0, 0, None, None, 0]; False
[0, 1, 1, 0, 0, 0, None, None, 1]; False
[0, 1, 1, 0, 0, 1, 0, 0, 0]; False
[0, 1, 1, 0, 0, 1, 0, 0, 1]; False
[0, 1, 1, 0, 0, 1, 0, 1, 0]; False
[0, 1, 1, 0, 0, 1, 0, 1, 1]; False
[0, 1, 1, 0, 0, 1, 0, None, 0]; False
[0, 1, 1, 0, 0, 1, 0, None, 1]; False
[0, 1, 1, 0, 0, 1, 1, 0, 0]; False
[0, 1, 1, 0, 0, 1, 1, 0, 1]; False
[0, 1, 1, 0, 0, 1, 1, 1, 0]; False
[0, 1, 1, 0, 0, 1, 1, 1, 1]; False
[0, 1, 1, 0, 0, 1, 1, None, 0]; False
[0, 1, 1, 0, 0, 1, 1, None, 1]; False
[0, 1, 1, 0, 0, 1, None, 0, 0]; False
[0, 1, 1, 0, 0, 1, None, 0, 1]; False
[0, 1, 1, 0, 0, 1, None, 1, 0]; False
[0, 1, 1, 0, 0, 1, None, 1, 1]; False
[0, 1, 1, 0, 0, 1, None, None, 0]; False
[0, 1, 1, 0, 0, 1, None, None, 1]; False
[0, 1, 1, 0, 0, None, 0, 0, 0]; False
[0, 1, 1, 0, 0, None, 0, 0, 1]; False
[0, 1, 1, 0, 0, None, 0, 1, 0]; False
[0, 1, 1, 0, 0, None, 0, 1, 1]; False
[0, 1, 1, 0, 0, None, 0, None, 0]; False
[0, 1, 1, 0, 0, None, 0, None, 1]; False
[0, 1, 1, 0, 0, None, 1, 0, 0]; False
[0, 1, 1, 0, 0, None, 1, 0, 1]; False
[0, 1, 1, 0, 0, None, 1, 1, 0]; False
[0, 1, 1, 0, 0, None, 1, 1, 1]; False
[0, 1, 1, 0, 0, None, 1, None, 0]; False
[0, 1, 1, 0, 0, None, 1, None, 1]; False
[0, 1, 1, 0, 0, None, None, 0, 0]; False
[0, 1, 1, 0, 0, None, None, 0, 1]; False
[0, 1, 1, 0, 0, None, None, 1, 0]; False
[0, 1, 1, 0, 0, None, None, 1, 1]; False
[0, 1, 1, 0, 0, None, None, None, 0]; False
[0, 1, 1, 0, 0, None, None, None, 1]; False
[0, 1, 1, 0, 1, 0, 0, 0, 0]; False
[0, 1, 1, 0, 1, 0, 0, 0, 1]; True
[0, 1, 1, 0, 1, 0, 0, 1, 0]; False
[0, 1, 1, 0, 1, 0, 0, 1, 1]; False
[0, 1, 1, 0, 1, 0, 0, None, 0]; False
[0, 1, 1, 0, 1, 0, 0, None, 1]; False
[0, 1, 1, 0, 1, 0, 1, 0, 0]; False
[0, 1, 1, 0, 1, 0, 1, 0, 1]; False
[0, 1, 1, 0, 1, 0, 1, 1, 0]; False
[0, 1, 1, 0, 1, 0, 1, 1, 1]; False
[0, 1, 1, 0, 1, 0, 1, None, 0]; False
[0, 1, 1, 0, 1, 0, 1, None, 1]; False
[0, 1, 1, 0, 1, 0, None, 0, 0]; False
[0, 1, 1, 0, 1, 0, None, 0, 1]; False
[0, 1, 1, 0, 1, 0, None, 1, 0]; False
[0, 1, 1, 0, 1, 0, None, 1, 1]; False
[0, 1, 1, 0, 1, 0, None, None, 0]; False
[0, 1, 1, 0, 1, 0, None, None, 1]; False
[0, 1, 1, 0, 1, 1, 0, 0, 0]; False
[0, 1, 1, 0, 1, 1, 0, 0, 1]; True
[0, 1, 1, 0, 1, 1, 0, 1, 0]; False
[0, 1, 1, 0, 1, 1, 0, 1, 1]; False
[0, 1, 1, 0, 1, 1, 0, None, 0]; False
[0, 1, 1, 0, 1, 1, 0, None, 1]; False
[0, 1, 1, 0, 1, 1, 1, 0, 0]; False
[0, 1, 1, 0, 1, 1, 1, 0, 1]; True
[0, 1, 1, 0, 1, 1, 1, 1, 0]; False
[0, 1, 1, 0, 1, 1, 1, 1, 1]; False
[0, 1, 1, 0, 1, 1, 1, None, 0]; False
[0, 1, 1, 0, 1, 1, 1, None, 1]; False
[0, 1, 1, 0, 1, 1, None, 0, 0]; False
[0, 1, 1, 0, 1, 1, None, 0, 1]; True
[0, 1, 1, 0, 1, 1, None, 1, 0]; False
[0, 1, 1, 0, 1, 1, None, 1, 1]; False
[0, 1, 1, 0, 1, 1, None, None, 0]; False
[0, 1, 1, 0, 1, 1, None, None, 1]; False
[0, 1, 1, 0, 1, None, 0, 0, 0]; False
[0, 1, 1, 0, 1, None, 0, 0, 1]; True
[0, 1, 1, 0, 1, None, 0, 1, 0]; False
[0, 1, 1, 0, 1, None, 0, 1, 1]; False
[0, 1, 1, 0, 1, None, 0, None, 0]; False
[0, 1, 1, 0, 1, None, 0, None, 1]; False
[0, 1, 1, 0, 1, None, 1, 0, 0]; False
[0, 1, 1, 0, 1, None, 1, 0, 1]; True
[0, 1, 1, 0, 1, None, 1, 1, 0]; False
[0, 1, 1, 0, 1, None, 1, 1, 1]; False
[0, 1, 1, 0, 1, None, 1, None, 0]; False
[0, 1, 1, 0, 1, None, 1, None, 1]; False
[0, 1, 1, 0, 1, None, None, 0, 0]; False
[0, 1, 1, 0, 1, None, None, 0, 1]; True
[0, 1, 1, 0, 1, None, None, 1, 0]; False
[0, 1, 1, 0, 1, None, None, 1, 1]; False
[0, 1, 1, 0, 1, None, None, None, 0]; False
[0, 1, 1, 0, 1, None, None, None, 1]; False
[0, 1, 1, 0, None, 0, 0, 0, 0]; False
[0, 1, 1, 0, None, 0, 0, 0, 1]; True
[0, 1, 1, 0, None, 0, 0, 1, 0]; False
[0, 1, 1, 0, None, 0, 0, 1, 1]; False
[0, 1, 1, 0, None, 0, 0, None, 0]; False
[0, 1, 1, 0, None, 0, 0, None, 1]; False
[0, 1, 1, 0, None, 0, 1, 0, 0]; False
[0, 1, 1, 0, None, 0, 1, 0, 1]; False
[0, 1, 1, 0, None, 0, 1, 1, 0]; False
[0, 1, 1, 0, None, 0, 1, 1, 1]; False
[0, 1, 1, 0, None, 0, 1, None, 0]; False
[0, 1, 1, 0, None, 0, 1, None, 1]; False
[0, 1, 1, 0, None, 0, None, 0, 0]; False
[0, 1, 1, 0, None, 0, None, 0, 1]; False
[0, 1, 1, 0, None, 0, None, 1, 0]; False
[0, 1, 1, 0, None, 0, None, 1, 1]; False
[0, 1, 1, 0, None, 0, None, None, 0]; False
[0, 1, 1, 0, None, 0, None, None, 1]; False
[0, 1, 1, 0, None, 1, 0, 0, 0]; False
[0, 1, 1, 0, None, 1, 0, 0, 1]; True
[0, 1, 1, 0, None, 1, 0, 1, 0]; False
[0, 1, 1, 0, None, 1, 0, 1, 1]; False
[0, 1, 1, 0, None, 1, 0, None, 0]; False
[0, 1, 1, 0, None, 1, 0, None, 1]; False
[0, 1, 1, 0, None, 1, 1, 0, 0]; False
[0, 1, 1, 0, None, 1, 1, 0, 1]; True
[0, 1, 1, 0, None, 1, 1, 1, 0]; False
[0, 1, 1, 0, None, 1, 1, 1, 1]; False
[0, 1, 1, 0, None, 1, 1, None, 0]; False
[0, 1, 1, 0, None, 1, 1, None, 1]; False
[0, 1, 1, 0, None, 1, None, 0, 0]; False
[0, 1, 1, 0, None, 1, None, 0, 1]; True
[0, 1, 1, 0, None, 1, None, 1, 0]; False
[0, 1, 1, 0, None, 1, None, 1, 1]; False
[0, 1, 1, 0, None, 1, None, None, 0]; False
[0, 1, 1, 0, None, 1, None, None, 1]; False
[0, 1, 1, 0, None, None, 0, 0, 0]; False
[0, 1, 1, 0, None, None, 0, 0, 1]; True
[0, 1, 1, 0, None, None, 0, 1, 0]; False
[0, 1, 1, 0, None, None, 0, 1, 1]; False
[0, 1, 1, 0, None, None, 0, None, 0]; False
[0, 1, 1, 0, None, None, 0, None, 1]; False
[0, 1, 1, 0, None, None, 1, 0, 0]; False
[0, 1, 1, 0, None, None, 1, 0, 1]; True
[0, 1, 1, 0, None, None, 1, 1, 0]; False
[0, 1, 1, 0, None, None, 1, 1, 1]; False
[0, 1, 1, 0, None, None, 1, None, 0]; False
[0, 1, 1, 0, None, None, 1, None, 1]; False
[0, 1, 1, 0, None, None, None, 0, 0]; False
[0, 1, 1, 0, None, None, None, 0, 1]; True
[0, 1, 1, 0, None, None, None, 1, 0]; False
[0, 1, 1, 0, None, None, None, 1, 1]; False
[0, 1, 1, 0, None, None, None, None, 0]; False
[0, 1, 1, 0, None, None, None, None, 1]; False
[0, 1, 1, 1, 0, 0, 0, 0, 0]; False
[0, 1, 1, 1, 0, 0, 0, 0, 1]; False
[0, 1, 1, 1, 0, 0, 0, 1, 0]; False
[0, 1, 1, 1, 0, 0, 0, 1, 1]; False
[0, 1, 1, 1, 0, 0, 0, None, 0]; False
[0, 1, 1, 1, 0, 0, 0, None, 1]; False
[0, 1, 1, 1, 0, 0, 1, 0, 0]; False
[0, 1, 1, 1, 0, 0, 1, 0, 1]; False
[0, 1, 1, 1, 0, 0, 1, 1, 0]; False
[0, 1, 1, 1, 0, 0, 1, 1, 1]; False
[0, 1, 1, 1, 0, 0, 1, None, 0]; False
[0, 1, 1, 1, 0, 0, 1, None, 1]; False
[0, 1, 1, 1, 0, 0, None, 0, 0]; False
[0, 1, 1, 1, 0, 0, None, 0, 1]; False
[0, 1, 1, 1, 0, 0, None, 1, 0]; False
[0, 1, 1, 1, 0, 0, None, 1, 1]; False
[0, 1, 1, 1, 0, 0, None, None, 0]; False
[0, 1, 1, 1, 0, 0, None, None, 1]; False
[0, 1, 1, 1, 0, 1, 0, 0, 0]; False
[0, 1, 1, 1, 0, 1, 0, 0, 1]; False
[0, 1, 1, 1, 0, 1, 0, 1, 0]; False
[0, 1, 1, 1, 0, 1, 0, 1, 1]; False
[0, 1, 1, 1, 0, 1, 0, None, 0]; False
[0, 1, 1, 1, 0, 1, 0, None, 1]; False
[0, 1, 1, 1, 0, 1, 1, 0, 0]; False
[0, 1, 1, 1, 0, 1, 1, 0, 1]; False
[0, 1, 1, 1, 0, 1, 1, 1, 0]; False
[0, 1, 1, 1, 0, 1, 1, 1, 1]; False
[0, 1, 1, 1, 0, 1, 1, None, 0]; False
[0, 1, 1, 1, 0, 1, 1, None, 1]; False
[0, 1, 1, 1, 0, 1, None, 0, 0]; False
[0, 1, 1, 1, 0, 1, None, 0, 1]; False
[0, 1, 1, 1, 0, 1, None, 1, 0]; False
[0, 1, 1, 1, 0, 1, None, 1, 1]; False
[0, 1, 1, 1, 0, 1, None, None, 0]; False
[0, 1, 1, 1, 0, 1, None, None, 1]; False
[0, 1, 1, 1, 0, None, 0, 0, 0]; False
[0, 1, 1, 1, 0, None, 0, 0, 1]; False
[0, 1, 1, 1, 0, None, 0, 1, 0]; False
[0, 1, 1, 1, 0, None, 0, 1, 1]; False
[0, 1, 1, 1, 0, None, 0, None, 0]; False
[0, 1, 1, 1, 0, None, 0, None, 1]; False
[0, 1, 1, 1, 0, None, 1, 0, 0]; False
[0, 1, 1, 1, 0, None, 1, 0, 1]; False
[0, 1, 1, 1, 0, None, 1, 1, 0]; False
[0, 1, 1, 1, 0, None, 1, 1, 1]; False
[0, 1, 1, 1, 0, None, 1, None, 0]; False
[0, 1, 1, 1, 0, None, 1, None, 1]; False
[0, 1, 1, 1, 0, None, None, 0, 0]; False
[0, 1, 1, 1, 0, None, None, 0, 1]; False
[0, 1, 1, 1, 0, None, None, 1, 0]; False
[0, 1, 1, 1, 0, None, None, 1, 1]; False
[0, 1, 1, 1, 0, None, None, None, 0]; False
[0, 1, 1, 1, 0, None, None, None, 1]; False
[0, 1, 1, 1, 1, 0, 0, 0, 0]; False
[0, 1, 1, 1, 1, 0, 0, 0, 1]; False
[0, 1, 1, 1, 1, 0, 0, 1, 0]; False
[0, 1, 1, 1, 1, 0, 0, 1, 1]; False
[0, 1, 1, 1, 1, 0, 0, None, 0]; False
[0, 1, 1, 1, 1, 0, 0, None, 1]; False
[0, 1, 1, 1, 1, 0, 1, 0, 0]; False
[0, 1, 1, 1, 1, 0, 1, 0, 1]; False
[0, 1, 1, 1, 1, 0, 1, 1, 0]; False
[0, 1, 1, 1, 1, 0, 1, 1, 1]; False
[0, 1, 1, 1, 1, 0, 1, None, 0]; False
[0, 1, 1, 1, 1, 0, 1, None, 1]; False
[0, 1, 1, 1, 1, 0, None, 0, 0]; False
[0, 1, 1, 1, 1, 0, None, 0, 1]; False
[0, 1, 1, 1, 1, 0, None, 1, 0]; False
[0, 1, 1, 1, 1, 0, None, 1, 1]; False
[0, 1, 1, 1, 1, 0, None, None, 0]; False
[0, 1, 1, 1, 1, 0, None, None, 1]; False
[0, 1, 1, 1, 1, 1, 0, 0, 0]; False
[0, 1, 1, 1, 1, 1, 0, 0, 1]; True
[0, 1, 1, 1, 1, 1, 0, 1, 0]; False
[0, 1, 1, 1, 1, 1, 0, 1, 1]; False
[0, 1, 1, 1, 1, 1, 0, None, 0]; False
[0, 1, 1, 1, 1, 1, 0, None, 1]; False
[0, 1, 1, 1, 1, 1, 1, 0, 0]; False
[0, 1, 1, 1, 1, 1, 1, 0, 1]; True
[0, 1, 1, 1, 1, 1, 1, 1, 0]; False
[0, 1, 1, 1, 1, 1, 1, 1, 1]; False
[0, 1, 1, 1, 1, 1, 1, None, 0]; False
[0, 1, 1, 1, 1, 1, 1, None, 1]; False
[0, 1, 1, 1, 1, 1, None, 0, 0]; False
[0, 1, 1, 1, 1, 1, None, 0, 1]; True
[0, 1, 1, 1, 1, 1, None, 1, 0]; False
[0, 1, 1, 1, 1, 1, None, 1, 1]; False
[0, 1, 1, 1, 1, 1, None, None, 0]; False
[0, 1, 1, 1, 1, 1, None, None, 1]; False
[0, 1, 1, 1, 1, None, 0, 0, 0]; False
[0, 1, 1, 1, 1, None, 0, 0, 1]; True
[0, 1, 1, 1, 1, None, 0, 1, 0]; False
[0, 1, 1, 1, 1, None, 0, 1, 1]; False
[0, 1, 1, 1, 1, None, 0, None, 0]; False
[0, 1, 1, 1, 1, None, 0, None, 1]; False
[0, 1, 1, 1, 1, None, 1, 0, 0]; False
[0, 1, 1, 1, 1, None, 1, 0, 1]; True
[0, 1, 1, 1, 1, None, 1, 1, 0]; False
[0, 1, 1, 1, 1, None, 1, 1, 1]; False
[0, 1, 1, 1, 1, None, 1, None, 0]; False
[0, 1, 1, 1, 1, None, 1, None, 1]; False
[0, 1, 1, 1, 1, None, None, 0, 0]; False
[0, 1, 1, 1, 1, None, None, 0, 1]; True
[0, 1, 1, 1, 1, None, None, 1, 0]; False
[0, 1, 1, 1, 1, None, None, 1, 1]; False
[0, 1, 1, 1, 1, None, None, None, 0]; False
[0, 1, 1, 1, 1, None, None, None, 1]; False
[0, 1, 1, 1, None, 0, 0, 0, 0]; False
[0, 1, 1, 1, None, 0, 0, 0, 1]; False
[0, 1, 1, 1, None, 0, 0, 1, 0]; False
[0, 1, 1, 1, None, 0, 0, 1, 1]; False
[0, 1, 1, 1, None, 0, 0, None, 0]; False
[0, 1, 1, 1, None, 0, 0, None, 1]; False
[0, 1, 1, 1, None, 0, 1, 0, 0]; False
[0, 1, 1, 1, None, 0, 1, 0, 1]; False
[0, 1, 1, 1, None, 0, 1, 1, 0]; False
[0, 1, 1, 1, None, 0, 1, 1, 1]; False
[0, 1, 1, 1, None, 0, 1, None, 0]; False
[0, 1, 1, 1, None, 0, 1, None, 1]; False
[0, 1, 1, 1, None, 0, None, 0, 0]; False
[0, 1, 1, 1, None, 0, None, 0, 1]; False
[0, 1, 1, 1, None, 0, None, 1, 0]; False
[0, 1, 1, 1, None, 0, None, 1, 1]; False
[0, 1, 1, 1, None, 0, None, None, 0]; False
[0, 1, 1, 1, None, 0, None, None, 1]; False
[0, 1, 1, 1, None, 1, 0, 0, 0]; False
[0, 1, 1, 1, None, 1, 0, 0, 1]; True
[0, 1, 1, 1, None, 1, 0, 1, 0]; False
[0, 1, 1, 1, None, 1, 0, 1, 1]; False
[0, 1, 1, 1, None, 1, 0, None, 0]; False
[0, 1, 1, 1, None, 1, 0, None, 1]; False
[0, 1, 1, 1, None, 1, 1, 0, 0]; False
[0, 1, 1, 1, None, 1, 1, 0, 1]; True
[0, 1, 1, 1, None, 1, 1, 1, 0]; False
[0, 1, 1, 1, None, 1, 1, 1, 1]; False
[0, 1, 1, 1, None, 1, 1, None, 0]; False
[0, 1, 1, 1, None, 1, 1, None, 1]; False
[0, 1, 1, 1, None, 1, None, 0, 0]; False
[0, 1, 1, 1, None, 1, None, 0, 1]; True
[0, 1, 1, 1, None, 1, None, 1, 0]; False
[0, 1, 1, 1, None, 1, None, 1, 1]; False
[0, 1, 1, 1, None, 1, None, None, 0]; False
[0, 1, 1, 1, None, 1, None, None, 1]; False
[0, 1, 1, 1, None, None, 0, 0, 0]; False
[0, 1, 1, 1, None, None, 0, 0, 1]; True
[0, 1, 1, 1, None, None, 0, 1, 0]; False
[0, 1, 1, 1, None, None, 0, 1, 1]; False
[0, 1, 1, 1, None, None, 0, None, 0]; False
[0, 1, 1, 1, None, None, 0, None, 1]; False
[0, 1, 1, 1, None, None, 1, 0, 0]; False
[0, 1, 1, 1, None, None, 1, 0, 1]; True
[0, 1, 1, 1, None, None, 1, 1, 0]; False
[0, 1, 1, 1, None, None, 1, 1, 1]; False
[0, 1, 1, 1, None, None, 1, None, 0]; False
[0, 1, 1, 1, None, None, 1, None, 1]; False
[0, 1, 1, 1, None, None, None, 0, 0]; False
[0, 1, 1, 1, None, None, None, 0, 1]; True
[0, 1, 1, 1, None, None, None, 1, 0]; False
[0, 1, 1, 1, None, None, None, 1, 1]; False
[0, 1, 1, 1, None, None, None, None, 0]; False
[0, 1, 1, 1, None, None, None, None, 1]; False
[0, 1, 1, None, 0, 0, 0, 0, 0]; False
[0, 1, 1, None, 0, 0, 0, 0, 1]; False
[0, 1, 1, None, 0, 0, 0, 1, 0]; False
[0, 1, 1, None, 0, 0, 0, 1, 1]; False
[0, 1, 1, None, 0, 0, 0, None, 0]; False
[0, 1, 1, None, 0, 0, 0, None, 1]; False
[0, 1, 1, None, 0, 0, 1, 0, 0]; False
[0, 1, 1, None, 0, 0, 1, 0, 1]; False
[0, 1, 1, None, 0, 0, 1, 1, 0]; False
[0, 1, 1, None, 0, 0, 1, 1, 1]; False
[0, 1, 1, None, 0, 0, 1, None, 0]; False
[0, 1, 1, None, 0, 0, 1, None, 1]; False
[0, 1, 1, None, 0, 0, None, 0, 0]; False
[0, 1, 1, None, 0, 0, None, 0, 1]; False
[0, 1, 1, None, 0, 0, None, 1, 0]; False
[0, 1, 1, None, 0, 0, None, 1, 1]; False
[0, 1, 1, None, 0, 0, None, None, 0]; False
[0, 1, 1, None, 0, 0, None, None, 1]; False
[0, 1, 1, None, 0, 1, 0, 0, 0]; False
[0, 1, 1, None, 0, 1, 0, 0, 1]; False
[0, 1, 1, None, 0, 1, 0, 1, 0]; False
[0, 1, 1, None, 0, 1, 0, 1, 1]; False
[0, 1, 1, None, 0, 1, 0, None, 0]; False
[0, 1, 1, None, 0, 1, 0, None, 1]; False
[0, 1, 1, None, 0, 1, 1, 0, 0]; False
[0, 1, 1, None, 0, 1, 1, 0, 1]; False
[0, 1, 1, None, 0, 1, 1, 1, 0]; False
[0, 1, 1, None, 0, 1, 1, 1, 1]; False
[0, 1, 1, None, 0, 1, 1, None, 0]; False
[0, 1, 1, None, 0, 1, 1, None, 1]; False
[0, 1, 1, None, 0, 1, None, 0, 0]; False
[0, 1, 1, None, 0, 1, None, 0, 1]; False
[0, 1, 1, None, 0, 1, None, 1, 0]; False
[0, 1, 1, None, 0, 1, None, 1, 1]; False
[0, 1, 1, None, 0, 1, None, None, 0]; False
[0, 1, 1, None, 0, 1, None, None, 1]; False
[0, 1, 1, None, 0, None, 0, 0, 0]; False
[0, 1, 1, None, 0, None, 0, 0, 1]; False
[0, 1, 1, None, 0, None, 0, 1, 0]; False
[0, 1, 1, None, 0, None, 0, 1, 1]; False
[0, 1, 1, None, 0, None, 0, None, 0]; False
[0, 1, 1, None, 0, None, 0, None, 1]; False
[0, 1, 1, None, 0, None, 1, 0, 0]; False
[0, 1, 1, None, 0, None, 1, 0, 1]; False
[0, 1, 1, None, 0, None, 1, 1, 0]; False
[0, 1, 1, None, 0, None, 1, 1, 1]; False
[0, 1, 1, None, 0, None, 1, None, 0]; False
[0, 1, 1, None, 0, None, 1, None, 1]; False
[0, 1, 1, None, 0, None, None, 0, 0]; False
[0, 1, 1, None, 0, None, None, 0, 1]; False
[0, 1, 1, None, 0, None, None, 1, 0]; False
[0, 1, 1, None, 0, None, None, 1, 1]; False
[0, 1, 1, None, 0, None, None, None, 0]; False
[0, 1, 1, None, 0, None, None, None, 1]; False
[0, 1, 1, None, 1, 0, 0, 0, 0]; False
[0, 1, 1, None, 1, 0, 0, 0, 1]; False
[0, 1, 1, None, 1, 0, 0, 1, 0]; False
[0, 1, 1, None, 1, 0, 0, 1, 1]; False
[0, 1, 1, None, 1, 0, 0, None, 0]; False
[0, 1, 1, None, 1, 0, 0, None, 1]; False
[0, 1, 1, None, 1, 0, 1, 0, 0]; False
[0, 1, 1, None, 1, 0, 1, 0, 1]; False
[0, 1, 1, None, 1, 0, 1, 1, 0]; False
[0, 1, 1, None, 1, 0, 1, 1, 1]; False
[0, 1, 1, None, 1, 0, 1, None, 0]; False
[0, 1, 1, None, 1, 0, 1, None, 1]; False
[0, 1, 1, None, 1, 0, None, 0, 0]; False
[0, 1, 1, None, 1, 0, None, 0, 1]; False
[0, 1, 1, None, 1, 0, None, 1, 0]; False
[0, 1, 1, None, 1, 0, None, 1, 1]; False
[0, 1, 1, None, 1, 0, None, None, 0]; False
[0, 1, 1, None, 1, 0, None, None, 1]; False
[0, 1, 1, None, 1, 1, 0, 0, 0]; False
[0, 1, 1, None, 1, 1, 0, 0, 1]; False
[0, 1, 1, None, 1, 1, 0, 1, 0]; False
[0, 1, 1, None, 1, 1, 0, 1, 1]; False
[0, 1, 1, None, 1, 1, 0, None, 0]; False
[0, 1, 1, None, 1, 1, 0, None, 1]; False
[0, 1, 1, None, 1, 1, 1, 0, 0]; False
[0, 1, 1, None, 1, 1, 1, 0, 1]; False
[0, 1, 1, None, 1, 1, 1, 1, 0]; False
[0, 1, 1, None, 1, 1, 1, 1, 1]; False
[0, 1, 1, None, 1, 1, 1, None, 0]; False
[0, 1, 1, None, 1, 1, 1, None, 1]; False
[0, 1, 1, None, 1, 1, None, 0, 0]; False
[0, 1, 1, None, 1, 1, None, 0, 1]; False
[0, 1, 1, None, 1, 1, None, 1, 0]; False
[0, 1, 1, None, 1, 1, None, 1, 1]; False
[0, 1, 1, None, 1, 1, None, None, 0]; False
[0, 1, 1, None, 1, 1, None, None, 1]; False
[0, 1, 1, None, 1, None, 0, 0, 0]; False
[0, 1, 1, None, 1, None, 0, 0, 1]; False
[0, 1, 1, None, 1, None, 0, 1, 0]; False
[0, 1, 1, None, 1, None, 0, 1, 1]; False
[0, 1, 1, None, 1, None, 0, None, 0]; False
[0, 1, 1, None, 1, None, 0, None, 1]; False
[0, 1, 1, None, 1, None, 1, 0, 0]; False
[0, 1, 1, None, 1, None, 1, 0, 1]; False
[0, 1, 1, None, 1, None, 1, 1, 0]; False
[0, 1, 1, None, 1, None, 1, 1, 1]; False
[0, 1, 1, None, 1, None, 1, None, 0]; False
[0, 1, 1, None, 1, None, 1, None, 1]; False
[0, 1, 1, None, 1, None, None, 0, 0]; False
[0, 1, 1, None, 1, None, None, 0, 1]; False
[0, 1, 1, None, 1, None, None, 1, 0]; False
[0, 1, 1, None, 1, None, None, 1, 1]; False
[0, 1, 1, None, 1, None, None, None, 0]; False
[0, 1, 1, None, 1, None, None, None, 1]; False
[0, 1, 1, None, None, 0, 0, 0, 0]; False
[0, 1, 1, None, None, 0, 0, 0, 1]; False
[0, 1, 1, None, None, 0, 0, 1, 0]; False
[0, 1, 1, None, None, 0, 0, 1, 1]; False
[0, 1, 1, None, None, 0, 0, None, 0]; False
[0, 1, 1, None, None, 0, 0, None, 1]; False
[0, 1, 1, None, None, 0, 1, 0, 0]; False
[0, 1, 1, None, None, 0, 1, 0, 1]; False
[0, 1, 1, None, None, 0, 1, 1, 0]; False
[0, 1, 1, None, None, 0, 1, 1, 1]; False
[0, 1, 1, None, None, 0, 1, None, 0]; False
[0, 1, 1, None, None, 0, 1, None, 1]; False
[0, 1, 1, None, None, 0, None, 0, 0]; False
[0, 1, 1, None, None, 0, None, 0, 1]; False
[0, 1, 1, None, None, 0, None, 1, 0]; False
[0, 1, 1, None, None, 0, None, 1, 1]; False
[0, 1, 1, None, None, 0, None, None, 0]; False
[0, 1, 1, None, None, 0, None, None, 1]; False
[0, 1, 1, None, None, 1, 0, 0, 0]; False
[0, 1, 1, None, None, 1, 0, 0, 1]; False
[0, 1, 1, None, None, 1, 0, 1, 0]; False
[0, 1, 1, None, None, 1, 0, 1, 1]; False
[0, 1, 1, None, None, 1, 0, None, 0]; False
[0, 1, 1, None, None, 1, 0, None, 1]; False
[0, 1, 1, None, None, 1, 1, 0, 0]; False
[0, 1, 1, None, None, 1, 1, 0, 1]; False
[0, 1, 1, None, None, 1, 1, 1, 0]; False
[0, 1, 1, None, None, 1, 1, 1, 1]; False
[0, 1, 1, None, None, 1, 1, None, 0]; False
[0, 1, 1, None, None, 1, 1, None, 1]; False
[0, 1, 1, None, None, 1, None, 0, 0]; False
[0, 1, 1, None, None, 1, None, 0, 1]; False
[0, 1, 1, None, None, 1, None, 1, 0]; False
[0, 1, 1, None, None, 1, None, 1, 1]; False
[0, 1, 1, None, None, 1, None, None, 0]; False
[0, 1, 1, None, None, 1, None, None, 1]; False
[0, 1, 1, None, None, None, 0, 0, 0]; False
[0, 1, 1, None, None, None, 0, 0, 1]; False
[0, 1, 1, None, None, None, 0, 1, 0]; False
[0, 1, 1, None, None, None, 0, 1, 1]; False
[0, 1, 1, None, None, None, 0, None, 0]; False
[0, 1, 1, None, None, None, 0, None, 1]; False
[0, 1, 1, None, None, None, 1, 0, 0]; False
[0, 1, 1, None, None, None, 1, 0, 1]; False
[0, 1, 1, None, None, None, 1, 1, 0]; False
[0, 1, 1, None, None, None, 1, 1, 1]; False
[0, 1, 1, None, None, None, 1, None, 0]; False
[0, 1, 1, None, None, None, 1, None, 1]; False
[0, 1, None, 0, 0, 0, 0, 0, 0]; False
[0, 1, None, 0, 0, 0, 0, 0, 1]; False
[0, 1, None, 0, 0, 0, 0, 1, 0]; False
[0, 1, None, 0, 0, 0, 0, 1, 1]; False
[0, 1, None, 0, 0, 0, 0, None, 0]; False
[0, 1, None, 0, 0, 0, 0, None, 1]; False
[0, 1, None, 0, 0, 0, 1, 0, 0]; False
[0, 1, None, 0, 0, 0, 1, 0, 1]; False
[0, 1, None, 0, 0, 0, 1, 1, 0]; True
[0, 1, None, 0, 0, 0, 1, 1, 1]; True
[0, 1, None, 0, 0, 0, 1, None, 0]; True
[0, 1, None, 0, 0, 0, 1, None, 1]; True
[0, 1, None, 0, 0, 0, None, 0, 0]; False
[0, 1, None, 0, 0, 0, None, 0, 1]; False
[0, 1, None, 0, 0, 0, None, 1, 0]; True
[0, 1, None, 0, 0, 0, None, 1, 1]; True
[0, 1, None, 0, 0, 0, None, None, 0]; True
[0, 1, None, 0, 0, 0, None, None, 1]; True
[0, 1, None, 0, 0, 1, 0, 0, 0]; False
[0, 1, None, 0, 0, 1, 0, 0, 1]; False
[0, 1, None, 0, 0, 1, 0, 1, 0]; False
[0, 1, None, 0, 0, 1, 0, 1, 1]; False
[0, 1, None, 0, 0, 1, 0, None, 0]; False
[0, 1, None, 0, 0, 1, 0, None, 1]; False
[0, 1, None, 0, 0, 1, 1, 0, 0]; False
[0, 1, None, 0, 0, 1, 1, 0, 1]; False
[0, 1, None, 0, 0, 1, 1, 1, 0]; False
[0, 1, None, 0, 0, 1, 1, 1, 1]; False
[0, 1, None, 0, 0, 1, 1, None, 0]; False
[0, 1, None, 0, 0, 1, 1, None, 1]; False
[0, 1, None, 0, 0, 1, None, 0, 0]; False
[0, 1, None, 0, 0, 1, None, 0, 1]; False
[0, 1, None, 0, 0, 1, None, 1, 0]; False
[0, 1, None, 0, 0, 1, None, 1, 1]; False
[0, 1, None, 0, 0, 1, None, None, 0]; False
[0, 1, None, 0, 0, 1, None, None, 1]; False
[0, 1, None, 0, 0, None, 0, 0, 0]; False
[0, 1, None, 0, 0, None, 0, 0, 1]; False
[0, 1, None, 0, 0, None, 0, 1, 0]; False
[0, 1, None, 0, 0, None, 0, 1, 1]; False
[0, 1, None, 0, 0, None, 0, None, 0]; False
[0, 1, None, 0, 0, None, 0, None, 1]; False
[0, 1, None, 0, 0, None, 1, 0, 0]; False
[0, 1, None, 0, 0, None, 1, 0, 1]; False
[0, 1, None, 0, 0, None, 1, 1, 0]; False
[0, 1, None, 0, 0, None, 1, 1, 1]; False
[0, 1, None, 0, 0, None, 1, None, 0]; False
[0, 1, None, 0, 0, None, 1, None, 1]; False
[0, 1, None, 0, 0, None, None, 0, 0]; False
[0, 1, None, 0, 0, None, None, 0, 1]; False
[0, 1, None, 0, 0, None, None, 1, 0]; False
[0, 1, None, 0, 0, None, None, 1, 1]; True
[0, 1, None, 0, 0, None, None, None, 0]; False
[0, 1, None, 0, 0, None, None, None, 1]; True
[0, 1, None, 0, 1, 0, 0, 0, 0]; False
[0, 1, None, 0, 1, 0, 0, 0, 1]; False
[0, 1, None, 0, 1, 0, 0, 1, 0]; False
[0, 1, None, 0, 1, 0, 0, 1, 1]; False
[0, 1, None, 0, 1, 0, 0, None, 0]; False
[0, 1, None, 0, 1, 0, 0, None, 1]; False
[0, 1, None, 0, 1, 0, 1, 0, 0]; True
[0, 1, None, 0, 1, 0, 1, 0, 1]; False
[0, 1, None, 0, 1, 0, 1, 1, 0]; True
[0, 1, None, 0, 1, 0, 1, 1, 1]; True
[0, 1, None, 0, 1, 0, 1, None, 0]; True
[0, 1, None, 0, 1, 0, 1, None, 1]; True
[0, 1, None, 0, 1, 0, None, 0, 0]; True
[0, 1, None, 0, 1, 0, None, 0, 1]; False
[0, 1, None, 0, 1, 0, None, 1, 0]; True
[0, 1, None, 0, 1, 0, None, 1, 1]; True
[0, 1, None, 0, 1, 0, None, None, 0]; True
[0, 1, None, 0, 1, 0, None, None, 1]; True
[0, 1, None, 0, 1, 1, 0, 0, 0]; False
[0, 1, None, 0, 1, 1, 0, 0, 1]; False
[0, 1, None, 0, 1, 1, 0, 1, 0]; False
[0, 1, None, 0, 1, 1, 0, 1, 1]; False
[0, 1, None, 0, 1, 1, 0, None, 0]; False
[0, 1, None, 0, 1, 1, 0, None, 1]; False
[0, 1, None, 0, 1, 1, 1, 0, 0]; False
[0, 1, None, 0, 1, 1, 1, 0, 1]; False
[0, 1, None, 0, 1, 1, 1, 1, 0]; False
[0, 1, None, 0, 1, 1, 1, 1, 1]; False
[0, 1, None, 0, 1, 1, 1, None, 0]; False
[0, 1, None, 0, 1, 1, 1, None, 1]; False
[0, 1, None, 0, 1, 1, None, 0, 0]; False
[0, 1, None, 0, 1, 1, None, 0, 1]; False
[0, 1, None, 0, 1, 1, None, 1, 0]; False
[0, 1, None, 0, 1, 1, None, 1, 1]; False
[0, 1, None, 0, 1, 1, None, None, 0]; False
[0, 1, None, 0, 1, 1, None, None, 1]; False
[0, 1, None, 0, 1, None, 0, 0, 0]; False
[0, 1, None, 0, 1, None, 0, 0, 1]; False
[0, 1, None, 0, 1, None, 0, 1, 0]; False
[0, 1, None, 0, 1, None, 0, 1, 1]; False
[0, 1, None, 0, 1, None, 0, None, 0]; False
[0, 1, None, 0, 1, None, 0, None, 1]; False
[0, 1, None, 0, 1, None, 1, 0, 0]; False
[0, 1, None, 0, 1, None, 1, 0, 1]; False
[0, 1, None, 0, 1, None, 1, 1, 0]; False
[0, 1, None, 0, 1, None, 1, 1, 1]; False
[0, 1, None, 0, 1, None, 1, None, 0]; False
[0, 1, None, 0, 1, None, 1, None, 1]; False
[0, 1, None, 0, 1, None, None, 0, 0]; False
[0, 1, None, 0, 1, None, None, 0, 1]; False
[0, 1, None, 0, 1, None, None, 1, 0]; True
[0, 1, None, 0, 1, None, None, 1, 1]; True
[0, 1, None, 0, 1, None, None, None, 0]; True
[0, 1, None, 0, 1, None, None, None, 1]; True
[0, 1, None, 0, None, 0, 0, 0, 0]; False
[0, 1, None, 0, None, 0, 0, 0, 1]; False
[0, 1, None, 0, None, 0, 0, 1, 0]; False
[0, 1, None, 0, None, 0, 0, 1, 1]; False
[0, 1, None, 0, None, 0, 0, None, 0]; False
[0, 1, None, 0, None, 0, 0, None, 1]; False
[0, 1, None, 0, None, 0, 1, 0, 0]; False
[0, 1, None, 0, None, 0, 1, 0, 1]; True
[0, 1, None, 0, None, 0, 1, 1, 0]; False
[0, 1, None, 0, None, 0, 1, 1, 1]; False
[0, 1, None, 0, None, 0, 1, None, 0]; False
[0, 1, None, 0, None, 0, 1, None, 1]; False
[0, 1, None, 0, None, 0, None, 0, 0]; False
[0, 1, None, 0, None, 0, None, 0, 1]; True
[0, 1, None, 0, None, 0, None, 1, 0]; False
[0, 1, None, 0, None, 0, None, 1, 1]; False
[0, 1, None, 0, None, 0, None, None, 0]; False
[0, 1, None, 0, None, 0, None, None, 1]; False
[0, 1, None, 0, None, 1, 0, 0, 0]; False
[0, 1, None, 0, None, 1, 0, 0, 1]; False
[0, 1, None, 0, None, 1, 0, 1, 0]; False
[0, 1, None, 0, None, 1, 0, 1, 1]; False
[0, 1, None, 0, None, 1, 0, None, 0]; False
[0, 1, None, 0, None, 1, 0, None, 1]; False
[0, 1, None, 0, None, 1, 1, 0, 0]; False
[0, 1, None, 0, None, 1, 1, 0, 1]; True
[0, 1, None, 0, None, 1, 1, 1, 0]; False
[0, 1, None, 0, None, 1, 1, 1, 1]; False
[0, 1, None, 0, None, 1, 1, None, 0]; False
[0, 1, None, 0, None, 1, 1, None, 1]; False
[0, 1, None, 0, None, 1, None, 0, 0]; False
[0, 1, None, 0, None, 1, None, 0, 1]; True
[0, 1, None, 0, None, 1, None, 1, 0]; False
[0, 1, None, 0, None, 1, None, 1, 1]; False
[0, 1, None, 0, None, 1, None, None, 0]; False
[0, 1, None, 0, None, 1, None, None, 1]; False
[0, 1, None, 0, None, None, 0, 0, 0]; False
[0, 1, None, 0, None, None, 0, 0, 1]; False
[0, 1, None, 0, None, None, 0, 1, 0]; False
[0, 1, None, 0, None, None, 0, 1, 1]; False
[0, 1, None, 0, None, None, 0, None, 0]; False
[0, 1, None, 0, None, None, 0, None, 1]; False
[0, 1, None, 0, None, None, 1, 0, 0]; False
[0, 1, None, 0, None, None, 1, 0, 1]; False
[0, 1, None, 0, None, None, 1, 1, 0]; False
[0, 1, None, 0, None, None, 1, 1, 1]; False
[0, 1, None, 0, None, None, 1, None, 0]; False
[0, 1, None, 0, None, None, 1, None, 1]; False
[0, 1, None, 1, 0, 0, 0, 0, 0]; False
[0, 1, None, 1, 0, 0, 0, 0, 1]; False
[0, 1, None, 1, 0, 0, 0, 1, 0]; False
[0, 1, None, 1, 0, 0, 0, 1, 1]; False
[0, 1, None, 1, 0, 0, 0, None, 0]; False
[0, 1, None, 1, 0, 0, 0, None, 1]; False
[0, 1, None, 1, 0, 0, 1, 0, 0]; False
[0, 1, None, 1, 0, 0, 1, 0, 1]; False
[0, 1, None, 1, 0, 0, 1, 1, 0]; False
[0, 1, None, 1, 0, 0, 1, 1, 1]; True
[0, 1, None, 1, 0, 0, 1, None, 0]; False
[0, 1, None, 1, 0, 0, 1, None, 1]; True
[0, 1, None, 1, 0, 0, None, 0, 0]; False
[0, 1, None, 1, 0, 0, None, 0, 1]; False
[0, 1, None, 1, 0, 0, None, 1, 0]; False
[0, 1, None, 1, 0, 0, None, 1, 1]; True
[0, 1, None, 1, 0, 0, None, None, 0]; False
[0, 1, None, 1, 0, 0, None, None, 1]; True
[0, 1, None, 1, 0, 1, 0, 0, 0]; False
[0, 1, None, 1, 0, 1, 0, 0, 1]; False
[0, 1, None, 1, 0, 1, 0, 1, 0]; False
[0, 1, None, 1, 0, 1, 0, 1, 1]; False
[0, 1, None, 1, 0, 1, 0, None, 0]; False
[0, 1, None, 1, 0, 1, 0, None, 1]; False
[0, 1, None, 1, 0, 1, 1, 0, 0]; False
[0, 1, None, 1, 0, 1, 1, 0, 1]; False
[0, 1, None, 1, 0, 1, 1, 1, 0]; False
[0, 1, None, 1, 0, 1, 1, 1, 1]; False
[0, 1, None, 1, 0, 1, 1, None, 0]; False
[0, 1, None, 1, 0, 1, 1, None, 1]; False
[0, 1, None, 1, 0, 1, None, 0, 0]; False
[0, 1, None, 1, 0, 1, None, 0, 1]; False
[0, 1, None, 1, 0, 1, None, 1, 0]; False
[0, 1, None, 1, 0, 1, None, 1, 1]; False
[0, 1, None, 1, 0, 1, None, None, 0]; False
[0, 1, None, 1, 0, 1, None, None, 1]; False
[0, 1, None, 1, 0, None, 0, 0, 0]; False
[0, 1, None, 1, 0, None, 0, 0, 1]; False
[0, 1, None, 1, 0, None, 0, 1, 0]; False
[0, 1, None, 1, 0, None, 0, 1, 1]; False
[0, 1, None, 1, 0, None, 0, None, 0]; False
[0, 1, None, 1, 0, None, 0, None, 1]; False
[0, 1, None, 1, 0, None, 1, 0, 0]; False
[0, 1, None, 1, 0, None, 1, 0, 1]; False
[0, 1, None, 1, 0, None, 1, 1, 0]; False
[0, 1, None, 1, 0, None, 1, 1, 1]; False
[0, 1, None, 1, 0, None, 1, None, 0]; False
[0, 1, None, 1, 0, None, 1, None, 1]; False
[0, 1, None, 1, 0, None, None, 0, 0]; False
[0, 1, None, 1, 0, None, None, 0, 1]; False
[0, 1, None, 1, 0, None, None, 1, 0]; False
[0, 1, None, 1, 0, None, None, 1, 1]; False
[0, 1, None, 1, 0, None, None, None, 0]; False
[0, 1, None, 1, 0, None, None, None, 1]; False
[0, 1, None, 1, 1, 0, 0, 0, 0]; False
[0, 1, None, 1, 1, 0, 0, 0, 1]; False
[0, 1, None, 1, 1, 0, 0, 1, 0]; False
[0, 1, None, 1, 1, 0, 0, 1, 1]; False
[0, 1, None, 1, 1, 0, 0, None, 0]; False
[0, 1, None, 1, 1, 0, 0, None, 1]; False
[0, 1, None, 1, 1, 0, 1, 0, 0]; False
[0, 1, None, 1, 1, 0, 1, 0, 1]; False
[0, 1, None, 1, 1, 0, 1, 1, 0]; True
[0, 1, None, 1, 1, 0, 1, 1, 1]; True
[0, 1, None, 1, 1, 0, 1, None, 0]; True
[0, 1, None, 1, 1, 0, 1, None, 1]; True
[0, 1, None, 1, 1, 0, None, 0, 0]; False
[0, 1, None, 1, 1, 0, None, 0, 1]; False
[0, 1, None, 1, 1, 0, None, 1, 0]; True
[0, 1, None, 1, 1, 0, None, 1, 1]; True
[0, 1, None, 1, 1, 0, None, None, 0]; True
[0, 1, None, 1, 1, 0, None, None, 1]; True
[0, 1, None, 1, 1, 1, 0, 0, 0]; False
[0, 1, None, 1, 1, 1, 0, 0, 1]; False
[0, 1, None, 1, 1, 1, 0, 1, 0]; False
[0, 1, None, 1, 1, 1, 0, 1, 1]; False
[0, 1, None, 1, 1, 1, 0, None, 0]; False
[0, 1, None, 1, 1, 1, 0, None, 1]; False
[0, 1, None, 1, 1, 1, 1, 0, 0]; False
[0, 1, None, 1, 1, 1, 1, 0, 1]; False
[0, 1, None, 1, 1, 1, 1, 1, 0]; False
[0, 1, None, 1, 1, 1, 1, 1, 1]; False
[0, 1, None, 1, 1, 1, 1, None, 0]; False
[0, 1, None, 1, 1, 1, 1, None, 1]; False
[0, 1, None, 1, 1, 1, None, 0, 0]; False
[0, 1, None, 1, 1, 1, None, 0, 1]; False
[0, 1, None, 1, 1, 1, None, 1, 0]; False
[0, 1, None, 1, 1, 1, None, 1, 1]; False
[0, 1, None, 1, 1, 1, None, None, 0]; False
[0, 1, None, 1, 1, 1, None, None, 1]; False
[0, 1, None, 1, 1, None, 0, 0, 0]; False
[0, 1, None, 1, 1, None, 0, 0, 1]; False
[0, 1, None, 1, 1, None, 0, 1, 0]; False
[0, 1, None, 1, 1, None, 0, 1, 1]; False
[0, 1, None, 1, 1, None, 0, None, 0]; False
[0, 1, None, 1, 1, None, 0, None, 1]; False
[0, 1, None, 1, 1, None, 1, 0, 0]; False
[0, 1, None, 1, 1, None, 1, 0, 1]; False
[0, 1, None, 1, 1, None, 1, 1, 0]; False
[0, 1, None, 1, 1, None, 1, 1, 1]; False
[0, 1, None, 1, 1, None, 1, None, 0]; False
[0, 1, None, 1, 1, None, 1, None, 1]; False
[0, 1, None, 1, 1, None, None, 0, 0]; False
[0, 1, None, 1, 1, None, None, 0, 1]; False
[0, 1, None, 1, 1, None, None, 1, 0]; False
[0, 1, None, 1, 1, None, None, 1, 1]; False
[0, 1, None, 1, 1, None, None, None, 0]; False
[0, 1, None, 1, 1, None, None, None, 1]; False
[0, 1, None, 1, None, 0, 0, 0, 0]; False
[0, 1, None, 1, None, 0, 0, 0, 1]; False
[0, 1, None, 1, None, 0, 0, 1, 0]; False
[0, 1, None, 1, None, 0, 0, 1, 1]; False
[0, 1, None, 1, None, 0, 0, None, 0]; False
[0, 1, None, 1, None, 0, 0, None, 1]; False
[0, 1, None, 1, None, 0, 1, 0, 0]; False
[0, 1, None, 1, None, 0, 1, 0, 1]; True
[0, 1, None, 1, None, 0, 1, 1, 0]; False
[0, 1, None, 1, None, 0, 1, 1, 1]; False
[0, 1, None, 1, None, 0, 1, None, 0]; False
[0, 1, None, 1, None, 0, 1, None, 1]; False
[0, 1, None, 1, None, 0, None, 0, 0]; False
[0, 1, None, 1, None, 0, None, 0, 1]; True
[0, 1, None, 1, None, 0, None, 1, 0]; False
[0, 1, None, 1, None, 0, None, 1, 1]; False
[0, 1, None, 1, None, 0, None, None, 0]; False
[0, 1, None, 1, None, 0, None, None, 1]; False
[0, 1, None, 1, None, 1, 0, 0, 0]; False
[0, 1, None, 1, None, 1, 0, 0, 1]; False
[0, 1, None, 1, None, 1, 0, 1, 0]; False
[0, 1, None, 1, None, 1, 0, 1, 1]; False
[0, 1, None, 1, None, 1, 0, None, 0]; False
[0, 1, None, 1, None, 1, 0, None, 1]; False
[0, 1, None, 1, None, 1, 1, 0, 0]; False
[0, 1, None, 1, None, 1, 1, 0, 1]; True
[0, 1, None, 1, None, 1, 1, 1, 0]; False
[0, 1, None, 1, None, 1, 1, 1, 1]; False
[0, 1, None, 1, None, 1, 1, None, 0]; False
[0, 1, None, 1, None, 1, 1, None, 1]; False
[0, 1, None, 1, None, 1, None, 0, 0]; False
[0, 1, None, 1, None, 1, None, 0, 1]; True
[0, 1, None, 1, None, 1, None, 1, 0]; False
[0, 1, None, 1, None, 1, None, 1, 1]; False
[0, 1, None, 1, None, 1, None, None, 0]; False
[0, 1, None, 1, None, 1, None, None, 1]; False
[0, 1, None, 1, None, None, 0, 0, 0]; False
[0, 1, None, 1, None, None, 0, 0, 1]; False
[0, 1, None, 1, None, None, 0, 1, 0]; False
[0, 1, None, 1, None, None, 0, 1, 1]; False
[0, 1, None, 1, None, None, 0, None, 0]; False
[0, 1, None, 1, None, None, 0, None, 1]; False
[0, 1, None, 1, None, None, 1, 0, 0]; False
[0, 1, None, 1, None, None, 1, 0, 1]; False
[0, 1, None, 1, None, None, 1, 1, 0]; False
[0, 1, None, 1, None, None, 1, 1, 1]; False
[0, 1, None, 1, None, None, 1, None, 0]; False
[0, 1, None, 1, None, None, 1, None, 1]; False
[0, 1, None, None, 0, 0, 0, 0, 0]; False
[0, 1, None, None, 0, 0, 0, 0, 1]; False
[0, 1, None, None, 0, 0, 0, 1, 0]; False
[0, 1, None, None, 0, 0, 0, 1, 1]; False
[0, 1, None, None, 0, 0, 0, None, 0]; False
[0, 1, None, None, 0, 0, 0, None, 1]; False
[0, 1, None, None, 0, 0, 1, 0, 0]; False
[0, 1, None, None, 0, 0, 1, 0, 1]; False
[0, 1, None, None, 0, 0, 1, 1, 0]; False
[0, 1, None, None, 0, 0, 1, 1, 1]; False
[0, 1, None, None, 0, 0, 1, None, 0]; False
[0, 1, None, None, 0, 0, 1, None, 1]; False
[0, 1, None, None, 0, 0, None, 0, 0]; False
[0, 1, None, None, 0, 0, None, 0, 1]; False
[0, 1, None, None, 0, 0, None, 1, 0]; False
[0, 1, None, None, 0, 0, None, 1, 1]; False
[0, 1, None, None, 0, 0, None, None, 0]; False
[0, 1, None, None, 0, 0, None, None, 1]; False
[0, 1, None, None, 0, 1, 0, 0, 0]; False
[0, 1, None, None, 0, 1, 0, 0, 1]; False
[0, 1, None, None, 0, 1, 0, 1, 0]; False
[0, 1, None, None, 0, 1, 0, 1, 1]; False
[0, 1, None, None, 0, 1, 0, None, 0]; False
[0, 1, None, None, 0, 1, 0, None, 1]; False
[0, 1, None, None, 0, 1, 1, 0, 0]; False
[0, 1, None, None, 0, 1, 1, 0, 1]; False
[0, 1, None, None, 0, 1, 1, 1, 0]; False
[0, 1, None, None, 0, 1, 1, 1, 1]; False
[0, 1, None, None, 0, 1, 1, None, 0]; False
[0, 1, None, None, 0, 1, 1, None, 1]; False
[0, 1, None, None, 0, 1, None, 0, 0]; False
[0, 1, None, None, 0, 1, None, 0, 1]; False
[0, 1, None, None, 0, 1, None, 1, 0]; False
[0, 1, None, None, 0, 1, None, 1, 1]; False
[0, 1, None, None, 0, 1, None, None, 0]; False
[0, 1, None, None, 0, 1, None, None, 1]; False
[0, 1, None, None, 0, None, 0, 0, 0]; False
[0, 1, None, None, 0, None, 0, 0, 1]; False
[0, 1, None, None, 0, None, 0, 1, 0]; False
[0, 1, None, None, 0, None, 0, 1, 1]; False
[0, 1, None, None, 0, None, 0, None, 0]; False
[0, 1, None, None, 0, None, 0, None, 1]; False
[0, 1, None, None, 0, None, 1, 0, 0]; False
[0, 1, None, None, 0, None, 1, 0, 1]; False
[0, 1, None, None, 0, None, 1, 1, 0]; False
[0, 1, None, None, 0, None, 1, 1, 1]; False
[0, 1, None, None, 0, None, 1, None, 0]; False
[0, 1, None, None, 0, None, 1, None, 1]; False
[0, 1, None, None, 1, 0, 0, 0, 0]; False
[0, 1, None, None, 1, 0, 0, 0, 1]; False
[0, 1, None, None, 1, 0, 0, 1, 0]; False
[0, 1, None, None, 1, 0, 0, 1, 1]; False
[0, 1, None, None, 1, 0, 0, None, 0]; False
[0, 1, None, None, 1, 0, 0, None, 1]; False
[0, 1, None, None, 1, 0, 1, 0, 0]; False
[0, 1, None, None, 1, 0, 1, 0, 1]; False
[0, 1, None, None, 1, 0, 1, 1, 0]; False
[0, 1, None, None, 1, 0, 1, 1, 1]; False
[0, 1, None, None, 1, 0, 1, None, 0]; False
[0, 1, None, None, 1, 0, 1, None, 1]; False
[0, 1, None, None, 1, 0, None, 0, 0]; False
[0, 1, None, None, 1, 0, None, 0, 1]; False
[0, 1, None, None, 1, 0, None, 1, 0]; False
[0, 1, None, None, 1, 0, None, 1, 1]; False
[0, 1, None, None, 1, 0, None, None, 0]; False
[0, 1, None, None, 1, 0, None, None, 1]; False
[0, 1, None, None, 1, 1, 0, 0, 0]; False
[0, 1, None, None, 1, 1, 0, 0, 1]; False
[0, 1, None, None, 1, 1, 0, 1, 0]; False
[0, 1, None, None, 1, 1, 0, 1, 1]; False
[0, 1, None, None, 1, 1, 0, None, 0]; False
[0, 1, None, None, 1, 1, 0, None, 1]; False
[0, 1, None, None, 1, 1, 1, 0, 0]; False
[0, 1, None, None, 1, 1, 1, 0, 1]; False
[0, 1, None, None, 1, 1, 1, 1, 0]; False
[0, 1, None, None, 1, 1, 1, 1, 1]; False
[0, 1, None, None, 1, 1, 1, None, 0]; False
[0, 1, None, None, 1, 1, 1, None, 1]; False
[0, 1, None, None, 1, 1, None, 0, 0]; False
[0, 1, None, None, 1, 1, None, 0, 1]; False
[0, 1, None, None, 1, 1, None, 1, 0]; False
[0, 1, None, None, 1, 1, None, 1, 1]; False
[0, 1, None, None, 1, 1, None, None, 0]; False
[0, 1, None, None, 1, 1, None, None, 1]; False
[0, 1, None, None, 1, None, 0, 0, 0]; False
[0, 1, None, None, 1, None, 0, 0, 1]; False
[0, 1, None, None, 1, None, 0, 1, 0]; False
[0, 1, None, None, 1, None, 0, 1, 1]; False
[0, 1, None, None, 1, None, 0, None, 0]; False
[0, 1, None, None, 1, None, 0, None, 1]; False
[0, 1, None, None, 1, None, 1, 0, 0]; False
[0, 1, None, None, 1, None, 1, 0, 1]; False
[0, 1, None, None, 1, None, 1, 1, 0]; False
[0, 1, None, None, 1, None, 1, 1, 1]; False
[0, 1, None, None, 1, None, 1, None, 0]; False
[0, 1, None, None, 1, None, 1, None, 1]; False
[0, None, 0, 0, 0, 0, 0, 0, 0]; False
[0, None, 0, 0, 0, 0, 0, 0, 1]; False
[0, None, 0, 0, 0, 0, 0, 1, 0]; False
[0, None, 0, 0, 0, 0, 0, 1, 1]; False
[0, None, 0, 0, 0, 0, 0, None, 0]; False
[0, None, 0, 0, 0, 0, 0, None, 1]; False
[0, None, 0, 0, 0, 0, 1, 0, 0]; False
[0, None, 0, 0, 0, 0, 1, 0, 1]; False
[0, None, 0, 0, 0, 0, 1, 1, 0]; False
[0, None, 0, 0, 0, 0, 1, 1, 1]; False
[0, None, 0, 0, 0, 0, 1, None, 0]; False
[0, None, 0, 0, 0, 0, 1, None, 1]; False
[0, None, 0, 0, 0, 0, None, 0, 0]; False
[0, None, 0, 0, 0, 0, None, 0, 1]; False
[0, None, 0, 0, 0, 0, None, 1, 0]; False
[0, None, 0, 0, 0, 0, None, 1, 1]; False
[0, None, 0, 0, 0, 0, None, None, 0]; False
[0, None, 0, 0, 0, 0, None, None, 1]; False
[0, None, 0, 0, 0, 1, 0, 0, 0]; False
[0, None, 0, 0, 0, 1, 0, 0, 1]; False
[0, None, 0, 0, 0, 1, 0, 1, 0]; False
[0, None, 0, 0, 0, 1, 0, 1, 1]; False
[0, None, 0, 0, 0, 1, 0, None, 0]; False
[0, None, 0, 0, 0, 1, 0, None, 1]; False
[0, None, 0, 0, 0, 1, 1, 0, 0]; False
[0, None, 0, 0, 0, 1, 1, 0, 1]; False
[0, None, 0, 0, 0, 1, 1, 1, 0]; False
[0, None, 0, 0, 0, 1, 1, 1, 1]; False
[0, None, 0, 0, 0, 1, 1, None, 0]; False
[0, None, 0, 0, 0, 1, 1, None, 1]; False
[0, None, 0, 0, 0, 1, None, 0, 0]; False
[0, None, 0, 0, 0, 1, None, 0, 1]; False
[0, None, 0, 0, 0, 1, None, 1, 0]; False
[0, None, 0, 0, 0, 1, None, 1, 1]; False
[0, None, 0, 0, 0, 1, None, None, 0]; False
[0, None, 0, 0, 0, 1, None, None, 1]; False
[0, None, 0, 0, 0, None, 0, 0, 0]; False
[0, None, 0, 0, 0, None, 0, 0, 1]; False
[0, None, 0, 0, 0, None, 0, 1, 0]; False
[0, None, 0, 0, 0, None, 0, 1, 1]; False
[0, None, 0, 0, 0, None, 0, None, 0]; False
[0, None, 0, 0, 0, None, 0, None, 1]; False
[0, None, 0, 0, 0, None, 1, 0, 0]; False
[0, None, 0, 0, 0, None, 1, 0, 1]; False
[0, None, 0, 0, 0, None, 1, 1, 0]; False
[0, None, 0, 0, 0, None, 1, 1, 1]; False
[0, None, 0, 0, 0, None, 1, None, 0]; False
[0, None, 0, 0, 0, None, 1, None, 1]; False
[0, None, 0, 0, 0, None, None, 0, 0]; False
[0, None, 0, 0, 0, None, None, 0, 1]; False
[0, None, 0, 0, 0, None, None, 1, 0]; False
[0, None, 0, 0, 0, None, None, 1, 1]; False
[0, None, 0, 0, 0, None, None, None, 0]; False
[0, None, 0, 0, 0, None, None, None, 1]; False
[0, None, 0, 0, 1, 0, 0, 0, 0]; False
[0, None, 0, 0, 1, 0, 0, 0, 1]; False
[0, None, 0, 0, 1, 0, 0, 1, 0]; False
[0, None, 0, 0, 1, 0, 0, 1, 1]; False
[0, None, 0, 0, 1, 0, 0, None, 0]; False
[0, None, 0, 0, 1, 0, 0, None, 1]; False
[0, None, 0, 0, 1, 0, 1, 0, 0]; False
[0, None, 0, 0, 1, 0, 1, 0, 1]; False
[0, None, 0, 0, 1, 0, 1, 1, 0]; False
[0, None, 0, 0, 1, 0, 1, 1, 1]; False
[0, None, 0, 0, 1, 0, 1, None, 0]; False
[0, None, 0, 0, 1, 0, 1, None, 1]; False
[0, None, 0, 0, 1, 0, None, 0, 0]; False
[0, None, 0, 0, 1, 0, None, 0, 1]; False
[0, None, 0, 0, 1, 0, None, 1, 0]; False
[0, None, 0, 0, 1, 0, None, 1, 1]; False
[0, None, 0, 0, 1, 0, None, None, 0]; False
[0, None, 0, 0, 1, 0, None, None, 1]; False
[0, None, 0, 0, 1, 1, 0, 0, 0]; False
[0, None, 0, 0, 1, 1, 0, 0, 1]; False
[0, None, 0, 0, 1, 1, 0, 1, 0]; False
[0, None, 0, 0, 1, 1, 0, 1, 1]; False
[0, None, 0, 0, 1, 1, 0, None, 0]; False
[0, None, 0, 0, 1, 1, 0, None, 1]; False
[0, None, 0, 0, 1, 1, 1, 0, 0]; False
[0, None, 0, 0, 1, 1, 1, 0, 1]; False
[0, None, 0, 0, 1, 1, 1, 1, 0]; False
[0, None, 0, 0, 1, 1, 1, 1, 1]; False
[0, None, 0, 0, 1, 1, 1, None, 0]; False
[0, None, 0, 0, 1, 1, 1, None, 1]; False
[0, None, 0, 0, 1, 1, None, 0, 0]; False
[0, None, 0, 0, 1, 1, None, 0, 1]; False
[0, None, 0, 0, 1, 1, None, 1, 0]; False
[0, None, 0, 0, 1, 1, None, 1, 1]; False
[0, None, 0, 0, 1, 1, None, None, 0]; False
[0, None, 0, 0, 1, 1, None, None, 1]; False
[0, None, 0, 0, 1, None, 0, 0, 0]; False
[0, None, 0, 0, 1, None, 0, 0, 1]; False
[0, None, 0, 0, 1, None, 0, 1, 0]; False
[0, None, 0, 0, 1, None, 0, 1, 1]; False
[0, None, 0, 0, 1, None, 0, None, 0]; False
[0, None, 0, 0, 1, None, 0, None, 1]; False
[0, None, 0, 0, 1, None, 1, 0, 0]; False
[0, None, 0, 0, 1, None, 1, 0, 1]; False
[0, None, 0, 0, 1, None, 1, 1, 0]; False
[0, None, 0, 0, 1, None, 1, 1, 1]; False
[0, None, 0, 0, 1, None, 1, None, 0]; False
[0, None, 0, 0, 1, None, 1, None, 1]; False
[0, None, 0, 0, 1, None, None, 0, 0]; False
[0, None, 0, 0, 1, None, None, 0, 1]; False
[0, None, 0, 0, 1, None, None, 1, 0]; False
[0, None, 0, 0, 1, None, None, 1, 1]; False
[0, None, 0, 0, 1, None, None, None, 0]; False
[0, None, 0, 0, 1, None, None, None, 1]; False
[0, None, 0, 0, None, 0, 0, 0, 0]; False
[0, None, 0, 0, None, 0, 0, 0, 1]; False
[0, None, 0, 0, None, 0, 0, 1, 0]; False
[0, None, 0, 0, None, 0, 0, 1, 1]; False
[0, None, 0, 0, None, 0, 0, None, 0]; False
[0, None, 0, 0, None, 0, 0, None, 1]; False
[0, None, 0, 0, None, 0, 1, 0, 0]; False
[0, None, 0, 0, None, 0, 1, 0, 1]; False
[0, None, 0, 0, None, 0, 1, 1, 0]; False
[0, None, 0, 0, None, 0, 1, 1, 1]; False
[0, None, 0, 0, None, 0, 1, None, 0]; False
[0, None, 0, 0, None, 0, 1, None, 1]; False
[0, None, 0, 0, None, 0, None, 0, 0]; False
[0, None, 0, 0, None, 0, None, 0, 1]; False
[0, None, 0, 0, None, 0, None, 1, 0]; False
[0, None, 0, 0, None, 0, None, 1, 1]; False
[0, None, 0, 0, None, 0, None, None, 0]; False
[0, None, 0, 0, None, 0, None, None, 1]; False
[0, None, 0, 0, None, 1, 0, 0, 0]; False
[0, None, 0, 0, None, 1, 0, 0, 1]; False
[0, None, 0, 0, None, 1, 0, 1, 0]; False
[0, None, 0, 0, None, 1, 0, 1, 1]; False
[0, None, 0, 0, None, 1, 0, None, 0]; False
[0, None, 0, 0, None, 1, 0, None, 1]; False
[0, None, 0, 0, None, 1, 1, 0, 0]; False
[0, None, 0, 0, None, 1, 1, 0, 1]; False
[0, None, 0, 0, None, 1, 1, 1, 0]; False
[0, None, 0, 0, None, 1, 1, 1, 1]; False
[0, None, 0, 0, None, 1, 1, None, 0]; False
[0, None, 0, 0, None, 1, 1, None, 1]; False
[0, None, 0, 0, None, 1, None, 0, 0]; False
[0, None, 0, 0, None, 1, None, 0, 1]; False
[0, None, 0, 0, None, 1, None, 1, 0]; False
[0, None, 0, 0, None, 1, None, 1, 1]; False
[0, None, 0, 0, None, 1, None, None, 0]; False
[0, None, 0, 0, None, 1, None, None, 1]; False
[0, None, 0, 0, None, None, 0, 0, 0]; False
[0, None, 0, 0, None, None, 0, 0, 1]; False
[0, None, 0, 0, None, None, 0, 1, 0]; False
[0, None, 0, 0, None, None, 0, 1, 1]; False
[0, None, 0, 0, None, None, 0, None, 0]; False
[0, None, 0, 0, None, None, 0, None, 1]; False
[0, None, 0, 0, None, None, 1, 0, 0]; False
[0, None, 0, 0, None, None, 1, 0, 1]; False
[0, None, 0, 0, None, None, 1, 1, 0]; False
[0, None, 0, 0, None, None, 1, 1, 1]; False
[0, None, 0, 0, None, None, 1, None, 0]; False
[0, None, 0, 0, None, None, 1, None, 1]; False
[0, None, 0, 1, 0, 0, 0, 0, 0]; False
[0, None, 0, 1, 0, 0, 0, 0, 1]; False
[0, None, 0, 1, 0, 0, 0, 1, 0]; False
[0, None, 0, 1, 0, 0, 0, 1, 1]; False
[0, None, 0, 1, 0, 0, 0, None, 0]; False
[0, None, 0, 1, 0, 0, 0, None, 1]; False
[0, None, 0, 1, 0, 0, 1, 0, 0]; False
[0, None, 0, 1, 0, 0, 1, 0, 1]; False
[0, None, 0, 1, 0, 0, 1, 1, 0]; False
[0, None, 0, 1, 0, 0, 1, 1, 1]; False
[0, None, 0, 1, 0, 0, 1, None, 0]; False
[0, None, 0, 1, 0, 0, 1, None, 1]; False
[0, None, 0, 1, 0, 0, None, 0, 0]; False
[0, None, 0, 1, 0, 0, None, 0, 1]; False
[0, None, 0, 1, 0, 0, None, 1, 0]; False
[0, None, 0, 1, 0, 0, None, 1, 1]; False
[0, None, 0, 1, 0, 0, None, None, 0]; False
[0, None, 0, 1, 0, 0, None, None, 1]; False
[0, None, 0, 1, 0, 1, 0, 0, 0]; False
[0, None, 0, 1, 0, 1, 0, 0, 1]; False
[0, None, 0, 1, 0, 1, 0, 1, 0]; False
[0, None, 0, 1, 0, 1, 0, 1, 1]; False
[0, None, 0, 1, 0, 1, 0, None, 0]; False
[0, None, 0, 1, 0, 1, 0, None, 1]; False
[0, None, 0, 1, 0, 1, 1, 0, 0]; False
[0, None, 0, 1, 0, 1, 1, 0, 1]; False
[0, None, 0, 1, 0, 1, 1, 1, 0]; False
[0, None, 0, 1, 0, 1, 1, 1, 1]; False
[0, None, 0, 1, 0, 1, 1, None, 0]; False
[0, None, 0, 1, 0, 1, 1, None, 1]; False
[0, None, 0, 1, 0, 1, None, 0, 0]; False
[0, None, 0, 1, 0, 1, None, 0, 1]; False
[0, None, 0, 1, 0, 1, None, 1, 0]; False
[0, None, 0, 1, 0, 1, None, 1, 1]; False
[0, None, 0, 1, 0, 1, None, None, 0]; False
[0, None, 0, 1, 0, 1, None, None, 1]; False
[0, None, 0, 1, 0, None, 0, 0, 0]; False
[0, None, 0, 1, 0, None, 0, 0, 1]; False
[0, None, 0, 1, 0, None, 0, 1, 0]; False
[0, None, 0, 1, 0, None, 0, 1, 1]; False
[0, None, 0, 1, 0, None, 0, None, 0]; False
[0, None, 0, 1, 0, None, 0, None, 1]; False
[0, None, 0, 1, 0, None, 1, 0, 0]; False
[0, None, 0, 1, 0, None, 1, 0, 1]; False
[0, None, 0, 1, 0, None, 1, 1, 0]; False
[0, None, 0, 1, 0, None, 1, 1, 1]; False
[0, None, 0, 1, 0, None, 1, None, 0]; False
[0, None, 0, 1, 0, None, 1, None, 1]; False
[0, None, 0, 1, 0, None, None, 0, 0]; False
[0, None, 0, 1, 0, None, None, 0, 1]; False
[0, None, 0, 1, 0, None, None, 1, 0]; False
[0, None, 0, 1, 0, None, None, 1, 1]; False
[0, None, 0, 1, 0, None, None, None, 0]; False
[0, None, 0, 1, 0, None, None, None, 1]; False
[0, None, 0, 1, 1, 0, 0, 0, 0]; False
[0, None, 0, 1, 1, 0, 0, 0, 1]; False
[0, None, 0, 1, 1, 0, 0, 1, 0]; False
[0, None, 0, 1, 1, 0, 0, 1, 1]; False
[0, None, 0, 1, 1, 0, 0, None, 0]; False
[0, None, 0, 1, 1, 0, 0, None, 1]; False
[0, None, 0, 1, 1, 0, 1, 0, 0]; False
[0, None, 0, 1, 1, 0, 1, 0, 1]; False
[0, None, 0, 1, 1, 0, 1, 1, 0]; False
[0, None, 0, 1, 1, 0, 1, 1, 1]; False
[0, None, 0, 1, 1, 0, 1, None, 0]; False
[0, None, 0, 1, 1, 0, 1, None, 1]; False
[0, None, 0, 1, 1, 0, None, 0, 0]; False
[0, None, 0, 1, 1, 0, None, 0, 1]; False
[0, None, 0, 1, 1, 0, None, 1, 0]; False
[0, None, 0, 1, 1, 0, None, 1, 1]; False
[0, None, 0, 1, 1, 0, None, None, 0]; False
[0, None, 0, 1, 1, 0, None, None, 1]; False
[0, None, 0, 1, 1, 1, 0, 0, 0]; False
[0, None, 0, 1, 1, 1, 0, 0, 1]; False
[0, None, 0, 1, 1, 1, 0, 1, 0]; False
[0, None, 0, 1, 1, 1, 0, 1, 1]; False
[0, None, 0, 1, 1, 1, 0, None, 0]; False
[0, None, 0, 1, 1, 1, 0, None, 1]; False
[0, None, 0, 1, 1, 1, 1, 0, 0]; False
[0, None, 0, 1, 1, 1, 1, 0, 1]; False
[0, None, 0, 1, 1, 1, 1, 1, 0]; False
[0, None, 0, 1, 1, 1, 1, 1, 1]; False
[0, None, 0, 1, 1, 1, 1, None, 0]; False
[0, None, 0, 1, 1, 1, 1, None, 1]; False
[0, None, 0, 1, 1, 1, None, 0, 0]; False
[0, None, 0, 1, 1, 1, None, 0, 1]; False
[0, None, 0, 1, 1, 1, None, 1, 0]; False
[0, None, 0, 1, 1, 1, None, 1, 1]; False
[0, None, 0, 1, 1, 1, None, None, 0]; False
[0, None, 0, 1, 1, 1, None, None, 1]; False
[0, None, 0, 1, 1, None, 0, 0, 0]; False
[0, None, 0, 1, 1, None, 0, 0, 1]; False
[0, None, 0, 1, 1, None, 0, 1, 0]; False
[0, None, 0, 1, 1, None, 0, 1, 1]; False
[0, None, 0, 1, 1, None, 0, None, 0]; False
[0, None, 0, 1, 1, None, 0, None, 1]; False
[0, None, 0, 1, 1, None, 1, 0, 0]; False
[0, None, 0, 1, 1, None, 1, 0, 1]; False
[0, None, 0, 1, 1, None, 1, 1, 0]; False
[0, None, 0, 1, 1, None, 1, 1, 1]; False
[0, None, 0, 1, 1, None, 1, None, 0]; False
[0, None, 0, 1, 1, None, 1, None, 1]; False
[0, None, 0, 1, 1, None, None, 0, 0]; False
[0, None, 0, 1, 1, None, None, 0, 1]; False
[0, None, 0, 1, 1, None, None, 1, 0]; False
[0, None, 0, 1, 1, None, None, 1, 1]; False
[0, None, 0, 1, 1, None, None, None, 0]; False
[0, None, 0, 1, 1, None, None, None, 1]; False
[0, None, 0, 1, None, 0, 0, 0, 0]; False
[0, None, 0, 1, None, 0, 0, 0, 1]; False
[0, None, 0, 1, None, 0, 0, 1, 0]; False
[0, None, 0, 1, None, 0, 0, 1, 1]; False
[0, None, 0, 1, None, 0, 0, None, 0]; False
[0, None, 0, 1, None, 0, 0, None, 1]; False
[0, None, 0, 1, None, 0, 1, 0, 0]; False
[0, None, 0, 1, None, 0, 1, 0, 1]; False
[0, None, 0, 1, None, 0, 1, 1, 0]; False
[0, None, 0, 1, None, 0, 1, 1, 1]; False
[0, None, 0, 1, None, 0, 1, None, 0]; False
[0, None, 0, 1, None, 0, 1, None, 1]; False
[0, None, 0, 1, None, 0, None, 0, 0]; False
[0, None, 0, 1, None, 0, None, 0, 1]; False
[0, None, 0, 1, None, 0, None, 1, 0]; False
[0, None, 0, 1, None, 0, None, 1, 1]; False
[0, None, 0, 1, None, 0, None, None, 0]; False
[0, None, 0, 1, None, 0, None, None, 1]; False
[0, None, 0, 1, None, 1, 0, 0, 0]; False
[0, None, 0, 1, None, 1, 0, 0, 1]; False
[0, None, 0, 1, None, 1, 0, 1, 0]; False
[0, None, 0, 1, None, 1, 0, 1, 1]; False
[0, None, 0, 1, None, 1, 0, None, 0]; False
[0, None, 0, 1, None, 1, 0, None, 1]; False
[0, None, 0, 1, None, 1, 1, 0, 0]; False
[0, None, 0, 1, None, 1, 1, 0, 1]; False
[0, None, 0, 1, None, 1, 1, 1, 0]; False
[0, None, 0, 1, None, 1, 1, 1, 1]; False
[0, None, 0, 1, None, 1, 1, None, 0]; False
[0, None, 0, 1, None, 1, 1, None, 1]; False
[0, None, 0, 1, None, 1, None, 0, 0]; False
[0, None, 0, 1, None, 1, None, 0, 1]; False
[0, None, 0, 1, None, 1, None, 1, 0]; False
[0, None, 0, 1, None, 1, None, 1, 1]; False
[0, None, 0, 1, None, 1, None, None, 0]; False
[0, None, 0, 1, None, 1, None, None, 1]; False
[0, None, 0, 1, None, None, 0, 0, 0]; False
[0, None, 0, 1, None, None, 0, 0, 1]; False
[0, None, 0, 1, None, None, 0, 1, 0]; False
[0, None, 0, 1, None, None, 0, 1, 1]; False
[0, None, 0, 1, None, None, 0, None, 0]; False
[0, None, 0, 1, None, None, 0, None, 1]; False
[0, None, 0, 1, None, None, 1, 0, 0]; False
[0, None, 0, 1, None, None, 1, 0, 1]; False
[0, None, 0, 1, None, None, 1, 1, 0]; False
[0, None, 0, 1, None, None, 1, 1, 1]; False
[0, None, 0, 1, None, None, 1, None, 0]; False
[0, None, 0, 1, None, None, 1, None, 1]; False
[0, None, 0, None, 0, 0, 0, 0, 0]; False
[0, None, 0, None, 0, 0, 0, 0, 1]; False
[0, None, 0, None, 0, 0, 0, 1, 0]; False
[0, None, 0, None, 0, 0, 0, 1, 1]; False
[0, None, 0, None, 0, 0, 0, None, 0]; False
[0, None, 0, None, 0, 0, 0, None, 1]; False
[0, None, 0, None, 0, 0, 1, 0, 0]; False
[0, None, 0, None, 0, 0, 1, 0, 1]; False
[0, None, 0, None, 0, 0, 1, 1, 0]; False
[0, None, 0, None, 0, 0, 1, 1, 1]; False
[0, None, 0, None, 0, 0, 1, None, 0]; False
[0, None, 0, None, 0, 0, 1, None, 1]; False
[0, None, 0, None, 0, 0, None, 0, 0]; False
[0, None, 0, None, 0, 0, None, 0, 1]; False
[0, None, 0, None, 0, 0, None, 1, 0]; False
[0, None, 0, None, 0, 0, None, 1, 1]; False
[0, None, 0, None, 0, 0, None, None, 0]; False
[0, None, 0, None, 0, 0, None, None, 1]; False
[0, None, 0, None, 0, 1, 0, 0, 0]; False
[0, None, 0, None, 0, 1, 0, 0, 1]; False
[0, None, 0, None, 0, 1, 0, 1, 0]; False
[0, None, 0, None, 0, 1, 0, 1, 1]; False
[0, None, 0, None, 0, 1, 0, None, 0]; False
[0, None, 0, None, 0, 1, 0, None, 1]; False
[0, None, 0, None, 0, 1, 1, 0, 0]; False
[0, None, 0, None, 0, 1, 1, 0, 1]; False
[0, None, 0, None, 0, 1, 1, 1, 0]; False
[0, None, 0, None, 0, 1, 1, 1, 1]; False
[0, None, 0, None, 0, 1, 1, None, 0]; False
[0, None, 0, None, 0, 1, 1, None, 1]; False
[0, None, 0, None, 0, 1, None, 0, 0]; False
[0, None, 0, None, 0, 1, None, 0, 1]; False
[0, None, 0, None, 0, 1, None, 1, 0]; False
[0, None, 0, None, 0, 1, None, 1, 1]; False
[0, None, 0, None, 0, 1, None, None, 0]; False
[0, None, 0, None, 0, 1, None, None, 1]; False
[0, None, 0, None, 0, None, 0, 0, 0]; False
[0, None, 0, None, 0, None, 0, 0, 1]; False
[0, None, 0, None, 0, None, 0, 1, 0]; False
[0, None, 0, None, 0, None, 0, 1, 1]; False
[0, None, 0, None, 0, None, 0, None, 0]; False
[0, None, 0, None, 0, None, 0, None, 1]; False
[0, None, 0, None, 0, None, 1, 0, 0]; False
[0, None, 0, None, 0, None, 1, 0, 1]; False
[0, None, 0, None, 0, None, 1, 1, 0]; False
[0, None, 0, None, 0, None, 1, 1, 1]; False
[0, None, 0, None, 0, None, 1, None, 0]; False
[0, None, 0, None, 0, None, 1, None, 1]; False
[0, None, 0, None, 1, 0, 0, 0, 0]; False
[0, None, 0, None, 1, 0, 0, 0, 1]; False
[0, None, 0, None, 1, 0, 0, 1, 0]; False
[0, None, 0, None, 1, 0, 0, 1, 1]; False
[0, None, 0, None, 1, 0, 0, None, 0]; False
[0, None, 0, None, 1, 0, 0, None, 1]; False
[0, None, 0, None, 1, 0, 1, 0, 0]; False
[0, None, 0, None, 1, 0, 1, 0, 1]; False
[0, None, 0, None, 1, 0, 1, 1, 0]; False
[0, None, 0, None, 1, 0, 1, 1, 1]; False
[0, None, 0, None, 1, 0, 1, None, 0]; False
[0, None, 0, None, 1, 0, 1, None, 1]; False
[0, None, 0, None, 1, 0, None, 0, 0]; False
[0, None, 0, None, 1, 0, None, 0, 1]; False
[0, None, 0, None, 1, 0, None, 1, 0]; False
[0, None, 0, None, 1, 0, None, 1, 1]; False
[0, None, 0, None, 1, 0, None, None, 0]; False
[0, None, 0, None, 1, 0, None, None, 1]; False
[0, None, 0, None, 1, 1, 0, 0, 0]; False
[0, None, 0, None, 1, 1, 0, 0, 1]; False
[0, None, 0, None, 1, 1, 0, 1, 0]; False
[0, None, 0, None, 1, 1, 0, 1, 1]; False
[0, None, 0, None, 1, 1, 0, None, 0]; False
[0, None, 0, None, 1, 1, 0, None, 1]; False
[0, None, 0, None, 1, 1, 1, 0, 0]; False
[0, None, 0, None, 1, 1, 1, 0, 1]; False
[0, None, 0, None, 1, 1, 1, 1, 0]; False
[0, None, 0, None, 1, 1, 1, 1, 1]; False
[0, None, 0, None, 1, 1, 1, None, 0]; False
[0, None, 0, None, 1, 1, 1, None, 1]; False
[0, None, 0, None, 1, 1, None, 0, 0]; False
[0, None, 0, None, 1, 1, None, 0, 1]; False
[0, None, 0, None, 1, 1, None, 1, 0]; False
[0, None, 0, None, 1, 1, None, 1, 1]; False
[0, None, 0, None, 1, 1, None, None, 0]; False
[0, None, 0, None, 1, 1, None, None, 1]; False
[0, None, 0, None, 1, None, 0, 0, 0]; False
[0, None, 0, None, 1, None, 0, 0, 1]; False
[0, None, 0, None, 1, None, 0, 1, 0]; False
[0, None, 0, None, 1, None, 0, 1, 1]; False
[0, None, 0, None, 1, None, 0, None, 0]; False
[0, None, 0, None, 1, None, 0, None, 1]; False
[0, None, 0, None, 1, None, 1, 0, 0]; False
[0, None, 0, None, 1, None, 1, 0, 1]; False
[0, None, 0, None, 1, None, 1, 1, 0]; False
[0, None, 0, None, 1, None, 1, 1, 1]; False
[0, None, 0, None, 1, None, 1, None, 0]; False
[0, None, 0, None, 1, None, 1, None, 1]; False
[0, None, 1, 0, 0, 0, 0, 0, 0]; False
[0, None, 1, 0, 0, 0, 0, 0, 1]; False
[0, None, 1, 0, 0, 0, 0, 1, 0]; False
[0, None, 1, 0, 0, 0, 0, 1, 1]; False
[0, None, 1, 0, 0, 0, 0, None, 0]; False
[0, None, 1, 0, 0, 0, 0, None, 1]; False
[0, None, 1, 0, 0, 0, 1, 0, 0]; False
[0, None, 1, 0, 0, 0, 1, 0, 1]; False
[0, None, 1, 0, 0, 0, 1, 1, 0]; False
[0, None, 1, 0, 0, 0, 1, 1, 1]; False
[0, None, 1, 0, 0, 0, 1, None, 0]; False
[0, None, 1, 0, 0, 0, 1, None, 1]; False
[0, None, 1, 0, 0, 0, None, 0, 0]; False
[0, None, 1, 0, 0, 0, None, 0, 1]; False
[0, None, 1, 0, 0, 0, None, 1, 0]; False
[0, None, 1, 0, 0, 0, None, 1, 1]; False
[0, None, 1, 0, 0, 0, None, None, 0]; False
[0, None, 1, 0, 0, 0, None, None, 1]; False
[0, None, 1, 0, 0, 1, 0, 0, 0]; False
[0, None, 1, 0, 0, 1, 0, 0, 1]; False
[0, None, 1, 0, 0, 1, 0, 1, 0]; False
[0, None, 1, 0, 0, 1, 0, 1, 1]; False
[0, None, 1, 0, 0, 1, 0, None, 0]; False
[0, None, 1, 0, 0, 1, 0, None, 1]; False
[0, None, 1, 0, 0, 1, 1, 0, 0]; False
[0, None, 1, 0, 0, 1, 1, 0, 1]; False
[0, None, 1, 0, 0, 1, 1, 1, 0]; False
[0, None, 1, 0, 0, 1, 1, 1, 1]; False
[0, None, 1, 0, 0, 1, 1, None, 0]; False
[0, None, 1, 0, 0, 1, 1, None, 1]; False
[0, None, 1, 0, 0, 1, None, 0, 0]; False
[0, None, 1, 0, 0, 1, None, 0, 1]; False
[0, None, 1, 0, 0, 1, None, 1, 0]; False
[0, None, 1, 0, 0, 1, None, 1, 1]; False
[0, None, 1, 0, 0, 1, None, None, 0]; False
[0, None, 1, 0, 0, 1, None, None, 1]; False
[0, None, 1, 0, 0, None, 0, 0, 0]; False
[0, None, 1, 0, 0, None, 0, 0, 1]; False
[0, None, 1, 0, 0, None, 0, 1, 0]; False
[0, None, 1, 0, 0, None, 0, 1, 1]; False
[0, None, 1, 0, 0, None, 0, None, 0]; False
[0, None, 1, 0, 0, None, 0, None, 1]; False
[0, None, 1, 0, 0, None, 1, 0, 0]; False
[0, None, 1, 0, 0, None, 1, 0, 1]; False
[0, None, 1, 0, 0, None, 1, 1, 0]; False
[0, None, 1, 0, 0, None, 1, 1, 1]; False
[0, None, 1, 0, 0, None, 1, None, 0]; False
[0, None, 1, 0, 0, None, 1, None, 1]; False
[0, None, 1, 0, 0, None, None, 0, 0]; False
[0, None, 1, 0, 0, None, None, 0, 1]; False
[0, None, 1, 0, 0, None, None, 1, 0]; False
[0, None, 1, 0, 0, None, None, 1, 1]; False
[0, None, 1, 0, 0, None, None, None, 0]; False
[0, None, 1, 0, 0, None, None, None, 1]; False
[0, None, 1, 0, 1, 0, 0, 0, 0]; False
[0, None, 1, 0, 1, 0, 0, 0, 1]; False
[0, None, 1, 0, 1, 0, 0, 1, 0]; False
[0, None, 1, 0, 1, 0, 0, 1, 1]; False
[0, None, 1, 0, 1, 0, 0, None, 0]; False
[0, None, 1, 0, 1, 0, 0, None, 1]; False
[0, None, 1, 0, 1, 0, 1, 0, 0]; False
[0, None, 1, 0, 1, 0, 1, 0, 1]; False
[0, None, 1, 0, 1, 0, 1, 1, 0]; False
[0, None, 1, 0, 1, 0, 1, 1, 1]; False
[0, None, 1, 0, 1, 0, 1, None, 0]; False
[0, None, 1, 0, 1, 0, 1, None, 1]; False
[0, None, 1, 0, 1, 0, None, 0, 0]; False
[0, None, 1, 0, 1, 0, None, 0, 1]; False
[0, None, 1, 0, 1, 0, None, 1, 0]; False
[0, None, 1, 0, 1, 0, None, 1, 1]; False
[0, None, 1, 0, 1, 0, None, None, 0]; False
[0, None, 1, 0, 1, 0, None, None, 1]; False
[0, None, 1, 0, 1, 1, 0, 0, 0]; False
[0, None, 1, 0, 1, 1, 0, 0, 1]; False
[0, None, 1, 0, 1, 1, 0, 1, 0]; False
[0, None, 1, 0, 1, 1, 0, 1, 1]; False
[0, None, 1, 0, 1, 1, 0, None, 0]; False
[0, None, 1, 0, 1, 1, 0, None, 1]; False
[0, None, 1, 0, 1, 1, 1, 0, 0]; False
[0, None, 1, 0, 1, 1, 1, 0, 1]; False
[0, None, 1, 0, 1, 1, 1, 1, 0]; False
[0, None, 1, 0, 1, 1, 1, 1, 1]; False
[0, None, 1, 0, 1, 1, 1, None, 0]; False
[0, None, 1, 0, 1, 1, 1, None, 1]; False
[0, None, 1, 0, 1, 1, None, 0, 0]; False
[0, None, 1, 0, 1, 1, None, 0, 1]; False
[0, None, 1, 0, 1, 1, None, 1, 0]; False
[0, None, 1, 0, 1, 1, None, 1, 1]; False
[0, None, 1, 0, 1, 1, None, None, 0]; False
[0, None, 1, 0, 1, 1, None, None, 1]; False
[0, None, 1, 0, 1, None, 0, 0, 0]; False
[0, None, 1, 0, 1, None, 0, 0, 1]; False
[0, None, 1, 0, 1, None, 0, 1, 0]; False
[0, None, 1, 0, 1, None, 0, 1, 1]; False
[0, None, 1, 0, 1, None, 0, None, 0]; False
[0, None, 1, 0, 1, None, 0, None, 1]; False
[0, None, 1, 0, 1, None, 1, 0, 0]; False
[0, None, 1, 0, 1, None, 1, 0, 1]; False
[0, None, 1, 0, 1, None, 1, 1, 0]; False
[0, None, 1, 0, 1, None, 1, 1, 1]; False
[0, None, 1, 0, 1, None, 1, None, 0]; False
[0, None, 1, 0, 1, None, 1, None, 1]; False
[0, None, 1, 0, 1, None, None, 0, 0]; False
[0, None, 1, 0, 1, None, None, 0, 1]; False
[0, None, 1, 0, 1, None, None, 1, 0]; False
[0, None, 1, 0, 1, None, None, 1, 1]; False
[0, None, 1, 0, 1, None, None, None, 0]; False
[0, None, 1, 0, 1, None, None, None, 1]; False
[0, None, 1, 0, None, 0, 0, 0, 0]; False
[0, None, 1, 0, None, 0, 0, 0, 1]; False
[0, None, 1, 0, None, 0, 0, 1, 0]; False
[0, None, 1, 0, None, 0, 0, 1, 1]; False
[0, None, 1, 0, None, 0, 0, None, 0]; False
[0, None, 1, 0, None, 0, 0, None, 1]; False
[0, None, 1, 0, None, 0, 1, 0, 0]; False
[0, None, 1, 0, None, 0, 1, 0, 1]; False
[0, None, 1, 0, None, 0, 1, 1, 0]; False
[0, None, 1, 0, None, 0, 1, 1, 1]; False
[0, None, 1, 0, None, 0, 1, None, 0]; False
[0, None, 1, 0, None, 0, 1, None, 1]; False
[0, None, 1, 0, None, 0, None, 0, 0]; False
[0, None, 1, 0, None, 0, None, 0, 1]; False
[0, None, 1, 0, None, 0, None, 1, 0]; False
[0, None, 1, 0, None, 0, None, 1, 1]; False
[0, None, 1, 0, None, 0, None, None, 0]; False
[0, None, 1, 0, None, 0, None, None, 1]; False
[0, None, 1, 0, None, 1, 0, 0, 0]; False
[0, None, 1, 0, None, 1, 0, 0, 1]; False
[0, None, 1, 0, None, 1, 0, 1, 0]; False
[0, None, 1, 0, None, 1, 0, 1, 1]; False
[0, None, 1, 0, None, 1, 0, None, 0]; False
[0, None, 1, 0, None, 1, 0, None, 1]; False
[0, None, 1, 0, None, 1, 1, 0, 0]; False
[0, None, 1, 0, None, 1, 1, 0, 1]; False
[0, None, 1, 0, None, 1, 1, 1, 0]; False
[0, None, 1, 0, None, 1, 1, 1, 1]; False
[0, None, 1, 0, None, 1, 1, None, 0]; False
[0, None, 1, 0, None, 1, 1, None, 1]; False
[0, None, 1, 0, None, 1, None, 0, 0]; False
[0, None, 1, 0, None, 1, None, 0, 1]; False
[0, None, 1, 0, None, 1, None, 1, 0]; False
[0, None, 1, 0, None, 1, None, 1, 1]; False
[0, None, 1, 0, None, 1, None, None, 0]; False
[0, None, 1, 0, None, 1, None, None, 1]; False
[0, None, 1, 0, None, None, 0, 0, 0]; False
[0, None, 1, 0, None, None, 0, 0, 1]; False
[0, None, 1, 0, None, None, 0, 1, 0]; False
[0, None, 1, 0, None, None, 0, 1, 1]; False
[0, None, 1, 0, None, None, 0, None, 0]; False
[0, None, 1, 0, None, None, 0, None, 1]; False
[0, None, 1, 0, None, None, 1, 0, 0]; False
[0, None, 1, 0, None, None, 1, 0, 1]; False
[0, None, 1, 0, None, None, 1, 1, 0]; False
[0, None, 1, 0, None, None, 1, 1, 1]; False
[0, None, 1, 0, None, None, 1, None, 0]; False
[0, None, 1, 0, None, None, 1, None, 1]; False
[0, None, 1, 1, 0, 0, 0, 0, 0]; False
[0, None, 1, 1, 0, 0, 0, 0, 1]; False
[0, None, 1, 1, 0, 0, 0, 1, 0]; False
[0, None, 1, 1, 0, 0, 0, 1, 1]; False
[0, None, 1, 1, 0, 0, 0, None, 0]; False
[0, None, 1, 1, 0, 0, 0, None, 1]; False
[0, None, 1, 1, 0, 0, 1, 0, 0]; False
[0, None, 1, 1, 0, 0, 1, 0, 1]; False
[0, None, 1, 1, 0, 0, 1, 1, 0]; False
[0, None, 1, 1, 0, 0, 1, 1, 1]; False
[0, None, 1, 1, 0, 0, 1, None, 0]; False
[0, None, 1, 1, 0, 0, 1, None, 1]; False
[0, None, 1, 1, 0, 0, None, 0, 0]; False
[0, None, 1, 1, 0, 0, None, 0, 1]; False
[0, None, 1, 1, 0, 0, None, 1, 0]; False
[0, None, 1, 1, 0, 0, None, 1, 1]; False
[0, None, 1, 1, 0, 0, None, None, 0]; False
[0, None, 1, 1, 0, 0, None, None, 1]; False
[0, None, 1, 1, 0, 1, 0, 0, 0]; False
[0, None, 1, 1, 0, 1, 0, 0, 1]; False
[0, None, 1, 1, 0, 1, 0, 1, 0]; False
[0, None, 1, 1, 0, 1, 0, 1, 1]; False
[0, None, 1, 1, 0, 1, 0, None, 0]; False
[0, None, 1, 1, 0, 1, 0, None, 1]; False
[0, None, 1, 1, 0, 1, 1, 0, 0]; False
[0, None, 1, 1, 0, 1, 1, 0, 1]; False
[0, None, 1, 1, 0, 1, 1, 1, 0]; False
[0, None, 1, 1, 0, 1, 1, 1, 1]; False
[0, None, 1, 1, 0, 1, 1, None, 0]; False
[0, None, 1, 1, 0, 1, 1, None, 1]; False
[0, None, 1, 1, 0, 1, None, 0, 0]; False
[0, None, 1, 1, 0, 1, None, 0, 1]; False
[0, None, 1, 1, 0, 1, None, 1, 0]; False
[0, None, 1, 1, 0, 1, None, 1, 1]; False
[0, None, 1, 1, 0, 1, None, None, 0]; False
[0, None, 1, 1, 0, 1, None, None, 1]; False
[0, None, 1, 1, 0, None, 0, 0, 0]; False
[0, None, 1, 1, 0, None, 0, 0, 1]; False
[0, None, 1, 1, 0, None, 0, 1, 0]; False
[0, None, 1, 1, 0, None, 0, 1, 1]; False
[0, None, 1, 1, 0, None, 0, None, 0]; False
[0, None, 1, 1, 0, None, 0, None, 1]; False
[0, None, 1, 1, 0, None, 1, 0, 0]; False
[0, None, 1, 1, 0, None, 1, 0, 1]; False
[0, None, 1, 1, 0, None, 1, 1, 0]; False
[0, None, 1, 1, 0, None, 1, 1, 1]; False
[0, None, 1, 1, 0, None, 1, None, 0]; False
[0, None, 1, 1, 0, None, 1, None, 1]; False
[0, None, 1, 1, 0, None, None, 0, 0]; False
[0, None, 1, 1, 0, None, None, 0, 1]; False
[0, None, 1, 1, 0, None, None, 1, 0]; False
[0, None, 1, 1, 0, None, None, 1, 1]; False
[0, None, 1, 1, 0, None, None, None, 0]; False
[0, None, 1, 1, 0, None, None, None, 1]; False
[0, None, 1, 1, 1, 0, 0, 0, 0]; False
[0, None, 1, 1, 1, 0, 0, 0, 1]; False
[0, None, 1, 1, 1, 0, 0, 1, 0]; False
[0, None, 1, 1, 1, 0, 0, 1, 1]; False
[0, None, 1, 1, 1, 0, 0, None, 0]; False
[0, None, 1, 1, 1, 0, 0, None, 1]; False
[0, None, 1, 1, 1, 0, 1, 0, 0]; False
[0, None, 1, 1, 1, 0, 1, 0, 1]; False
[0, None, 1, 1, 1, 0, 1, 1, 0]; False
[0, None, 1, 1, 1, 0, 1, 1, 1]; False
[0, None, 1, 1, 1, 0, 1, None, 0]; False
[0, None, 1, 1, 1, 0, 1, None, 1]; False
[0, None, 1, 1, 1, 0, None, 0, 0]; False
[0, None, 1, 1, 1, 0, None, 0, 1]; False
[0, None, 1, 1, 1, 0, None, 1, 0]; False
[0, None, 1, 1, 1, 0, None, 1, 1]; False
[0, None, 1, 1, 1, 0, None, None, 0]; False
[0, None, 1, 1, 1, 0, None, None, 1]; False
[0, None, 1, 1, 1, 1, 0, 0, 0]; False
[0, None, 1, 1, 1, 1, 0, 0, 1]; False
[0, None, 1, 1, 1, 1, 0, 1, 0]; False
[0, None, 1, 1, 1, 1, 0, 1, 1]; False
[0, None, 1, 1, 1, 1, 0, None, 0]; False
[0, None, 1, 1, 1, 1, 0, None, 1]; False
[0, None, 1, 1, 1, 1, 1, 0, 0]; False
[0, None, 1, 1, 1, 1, 1, 0, 1]; False
[0, None, 1, 1, 1, 1, 1, 1, 0]; False
[0, None, 1, 1, 1, 1, 1, 1, 1]; False
[0, None, 1, 1, 1, 1, 1, None, 0]; False
[0, None, 1, 1, 1, 1, 1, None, 1]; False
[0, None, 1, 1, 1, 1, None, 0, 0]; False
[0, None, 1, 1, 1, 1, None, 0, 1]; False
[0, None, 1, 1, 1, 1, None, 1, 0]; False
[0, None, 1, 1, 1, 1, None, 1, 1]; False
[0, None, 1, 1, 1, 1, None, None, 0]; False
[0, None, 1, 1, 1, 1, None, None, 1]; False
[0, None, 1, 1, 1, None, 0, 0, 0]; False
[0, None, 1, 1, 1, None, 0, 0, 1]; False
[0, None, 1, 1, 1, None, 0, 1, 0]; False
[0, None, 1, 1, 1, None, 0, 1, 1]; False
[0, None, 1, 1, 1, None, 0, None, 0]; False
[0, None, 1, 1, 1, None, 0, None, 1]; False
[0, None, 1, 1, 1, None, 1, 0, 0]; False"""

if __name__ == '__main__':
    test_tree()
    test_seq()
    test_insert()
