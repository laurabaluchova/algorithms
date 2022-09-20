# IB002 Extra domaci ukol 2.
#
# Jednostranne spojovany seznam znate z prednasky - jde o zretezeny seznam
# uzlu (Node), kde kazdy uzel ukazuje na sveho naslednika. V tomto prikladu
# nemame first a last, seznam je zadany "prvnim" ze svych uzlu.
#
# Tato uloha pracuje se dvema typy jednostranne spojovanych seznamu:
# Linearni seznam - kde posledni prvek seznamu ukazuje na None.
# Kruhovy seznam - kde posledni prvek seznamu ukazuje zpet na prvni prvek.
#
# Zjednoduseni:
# Pro vsechny funkce muzete predpokladat, ze seznam na vstupu obsahuje
# vzajemne ruzne klice a ze je linearni nebo kruhovy, tj. nemusite napriklad
# osetrovat situaci, kdy naslednikem "posledniho" v seznamu je "druhy".


# Trida Node reprezentujici prvek ve spojovanem seznamu
class Node:
    def __init__(self):
        self.key = 0  # klic
        self.next = None  # dalsi prvek seznamu
        self.opposite = None  # protejsi prvek seznamu


# Ukol 1.
# Implementujte funkci is_circular, ktera dostane prvni uzel seznamu
# a otestuje, zda je zadany zretezeny seznam kruhovy.
# Prazdny seznam neni kruhovy.

def is_circular(node):
    if node is None:
        return False
    actual_node = node.next
    while actual_node is not None:
        actual_node = actual_node.next
        if actual_node == node:
            return True
    return False


# Ukol 2.
# Implementujte funkci get_length, ktera vrati delku (tj. pocet ruznych uzlu)
# (linearniho nebo kruhoveho) zretezeneho seznamu zacinajiciho v zadanem uzlu.
# Pokud je seznam prazdny (None), vrati 0.

def get_length(node):
    if node is None:
        return 0

    length = 1
    actual_node = node.next
    while actual_node is not None:
        if actual_node == node:
            return length
        actual_node = actual_node.next
        length += 1
    return length



# Ukol 3.
# Implementujte funkci calculate_opposites, ktera korektne naplni polozky
# "opposite" v uzlech kruhoveho seznamu sude delky. Tj. pro kruhove seznamy
# delky 2n naplni u kazdeho uzlu polozku opposite uzlem, ktery je o n kroku
# dale (tedy v kruhu je to uzel "naproti").
#
# Napriklad v kruhovem seznamu 1 -> 2 -> 3 -> 4 (-> 1) je opposite
# uzlu 1 uzel 3, uzlu 2 uzel 4, uzlu 3 uzel 1 a uzlu 4 uzel 2.
#
# Pokud vstupni seznam neni kruhovy nebo ma lichou delku, tak funkce
# calculate_opposites seznam neupravuje.
#
# Pozor na casovou a prostorovou slozitost vaseho algoritmu!

def calculate_opposites(node):
    length = get_length(node)

    if not is_circular(node) or length % 2 != 0:
        return node

    nodes_from_current = length // 2
    actual_node = node
    opposite_node = get_first_opposite(node, nodes_from_current)

    for i in range(nodes_from_current):
        actual_node.opposite = opposite_node
        opposite_node.opposite = actual_node
        actual_node = actual_node.next
        opposite_node = opposite_node.next
    return node


def get_first_opposite(node, nodes_from_current):
    opposite_node = node
    for i in range(nodes_from_current):
        opposite_node = opposite_node.next
    return opposite_node


def test_calculate_opposites_circular_single_node():
    print("Test calculate_opposites with single Node - circular:", end=" ")

    node = Node()
    node.key = 1
    node.next = node

    result = calculate_opposites(node)

    if result == node:
        print("OK")
    else:
        print("FALSE")


def test_calculate_opposites_linear_multiple_nodes_odd():
    print("Test calculate_opposites with multiple Nodes - linear, odd:", end=" ")

    node = Node()
    node.key = 1

    node2 = Node()
    node2.key = 2
    node.next = node2

    node3 = Node()
    node3.key = 3
    node2.next = node3

    result = calculate_opposites(node)

    if result == node:
        print("OK")
    else:
        print("FALSE")


def test_calculate_opposites_circular_multiple_nodes_even():
    print("Test calculate opposites with multiple Nodes - circular, even:", end=" ")

    node = Node()
    node.key = 1

    node2 = Node()
    node2.key = 2
    node.next = node2

    node3 = Node()
    node3.key = 3
    node2.next = node3

    node4 = Node()
    node4.key = 4
    node3.next = node4
    node4.next = node

    result = calculate_opposites(node)

    if node.opposite == node3 and node3.opposite == node and node2.opposite == node4 and node4.opposite == node2:
        print("OK")
    else:
        print("FALSE")


test_calculate_opposites_circular_single_node()
test_calculate_opposites_linear_multiple_nodes_odd()
test_calculate_opposites_circular_multiple_nodes_even()

"""def test_is_circular_none():
    print("Test is_circular with None:", end=" ")
    result = is_circular(None)

    if not result:
        print("OK")
    else:
        print("FALSE")


def test_is_circular_linear_single_node():
    print("Test is_circular with single Node - linear:", end=" ")

    node = Node()
    node.key = 1

    result = is_circular(node)

    if not result:
        print("OK")
    else:
        print("FALSE")


def test_is_circular_circular_single_node():
    print("Test is_circular with single Node - circular:", end=" ")

    node = Node()
    node.key = 1
    node.next = node

    result = is_circular(node)

    if result:
        print("OK")
    else:
        print("FALSE")


def test_is_circular_linear_multiple_nodes():
    print("Test is_circular with multiple Nodes - linear:", end=" ")

    node = Node()
    node.key = 1

    node2 = Node()
    node2.key = 2
    node.next = node2

    node3 = Node()
    node3.key = 3
    node2.next = node3

    result = is_circular(node)

    if not result:
        print("OK")
    else:
        print("FALSE")


def test_is_circular_circular_multiple_nodes():
    print("Test is_circular with multiple Nodes - circular:", end=" ")

    node = Node()
    node.key = 1

    node2 = Node()
    node2.key = 2
    node.next = node2

    node3 = Node()
    node3.key = 3
    node2.next = node3
    node3.next = node

    result = is_circular(node)

    if result:
        print("OK")
    else:
        print("FALSE")
        

test_is_circular_none()
test_is_circular_linear_single_node()
test_is_circular_circular_single_node()
test_is_circular_linear_multiple_nodes()
test_is_circular_circular_multiple_nodes() """


def test_get_length_none():
    print("Test get_length with None:", end=" ")
    length = get_length(None)

    if length == 0:
        print("OK")
    else:
        print("FALSE, got: %i, expected: 0" % length)


def test_get_length_linear_single_node():
    print("Test get_length with linear single Node:", end=" ")
    node = Node()
    node.key = 1

    length = get_length(node)

    if length == 1:
        print("OK")
    else:
        print("FALSE, got: %i, expected: 1" % length)


def test_get_length_circular_single_node():
    print("Test get_length with circular single Node:", end=" ")
    node = Node()
    node.key = 1
    node.next = node

    length = get_length(node)

    if length == 1:
        print("OK")
    else:
        print("FALSE, got: %i, expected: 1" % length)


def test_get_length_circular_multiple_nodes():
    print("Test get_length with circular multiple Nodes:", end=" ")
    node = Node()
    node.key = 1

    node2 = Node()
    node2.key = 2
    node.next = node2

    node3 = Node()
    node3.key = 3
    node2.next = node3
    node3.next = node

    length = get_length(node)

    if length == 3:
        print("OK")
    else:
        print("FALSE, got: %i, expected: 3" % length)


def test_get_length_linear_multiple_nodes():
    print("Test get_length with linear multiple Nodes:", end=" ")
    node = Node()
    node.key = 1

    node2 = Node()
    node2.key = 2
    node.next = node2

    node3 = Node()
    node3.key = 3
    node2.next = node3

    length = get_length(node)

    if length == 3:
        print("OK")
    else:
        print("FALSE, got: %i, expected: 3" % length)


"""test_get_length_none()
test_get_length_linear_single_node()
test_get_length_circular_single_node()
test_get_length_circular_multiple_nodes()
test_get_length_linear_multiple_nodes()"""