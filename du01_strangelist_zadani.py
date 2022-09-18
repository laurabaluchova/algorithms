from cv01_linkedlist_zadani import LinkedList, Node


# IB002 Extra domaci ukol 1.
#
# Vasi ulohou v tomto priklade je modifikovat jiz existujici strukturu
# oboustranne zretezeneho linearniho seznamu.
#
# Oboustranne zretezeny seznam je definovan ukazatelem first, ktery
# ukazuje na zacatek seznamu, a ukazatelem last, ktery ukazuje na konec
# seznamu.
#
# Seznam s uzly a, b, c, d, e, f vypada bezne takto (v nakresu
# vynechavame ukazatele first a last):
#       ___   ___   ___   ___   ___
#      /   \ /   \ /   \ /   \ /   \
#     a <-- b <-- c <-- d <-- e <-- f
#
# kde obloucky nad pismeny reprezentuji dopredne sipky (napr. a --> b),
# tedy ukazatele next.
#
# Nas modifikovany StrangeList pouziva pro reprezentaci stejne promenne,
# pouze ukazatele ukazuji jinam. Ukazatele next budou ukazovat ob jeden
# uzel, ukazatele prev zustanou zachovany. Po prevedeni predchoziho
# seznamu na StrangeList vznikne takovyto seznam (opet vynechavame
# ukazatele first a last):
#       _________   _________
#      /         \ /         \
#     a <-- b <-- c <-- d <-- e <-- f
#            \_________/ \_________/
#
# StrangeList je take definovan ukazatelem first, ktery ukazuje na jeho
# zacatek, a ukazatelem last, ktery ukazuje na jeho konec, v tomto pripade
# first - a, last - f.


# Ukol 1.
# Definujte datovou strukturu StrangeList.
# Muzete se inspirovat definici ze zakladniho domaciho ukolu.


class StrangeList:

    def __init__(self):
        self.first = None
        self.last = None


# Ukol 2.
# Implementujte metodu list_to_strange_list, ktera z oboustranne
# zretezeneho seznamu vytvori nas StrangeList.
# Reprezentaci oboustranne zretezeneho seznamu muzete prevzit ze
# zakladniho domaciho ukolu.

def list_to_strange_list(linked_list):
    strange_list = StrangeList()

    linked_list_node = linked_list.first
    previous_node = None
    while linked_list_node is not None:
        strange_list_node = Node()
        strange_list_node.value = linked_list_node.value
        strange_list.last = strange_list_node

        if linked_list_node.prev is None:
            strange_list.first = strange_list_node

        strange_list_node.prev = previous_node

        if does_pointing_node_exist(strange_list_node) is True:
            pointing_node = strange_list_node.prev.prev
            pointing_node.next = strange_list_node

        previous_node = strange_list_node
        linked_list_node = linked_list_node.next
    return strange_list


def does_pointing_node_exist(node):
    return node.prev is not None and node.prev.prev is not None



# Ukol 3.
# Implementujte metodu check_strange_list, ktera zkontroluje, ze
# ukazatele first a last jsou nastaveny spravne.

def check_strange_list(strange_list):
    if strange_list.first == strange_list.last:
        return True

    if strange_list.first.prev is not None or strange_list.last.next is not None:
        return False

    actual_node = strange_list.first

    while actual_node is not None:
        next_node = actual_node.next
        if next_node is None and strange_list.last.prev == actual_node:
            return True
        if next_node.prev.prev is not actual_node:
            return False
        actual_node = next_node.prev
    return True


def test_list_to_strange_list_nonempty():
    linked_list = LinkedList()

    node1 = Node()
    node1.value = 1

    node2 = Node()
    node2.value = 2
    node1.next = node2
    node2.prev = node1

    node3 = Node()
    node3.value = 3
    node2.next = node3
    node3.prev = node2

    linked_list.first = node1
    linked_list.last = node3

    strange_list = list_to_strange_list(linked_list)
    #TODO: check pointers

def test_check_strange_list_correct_odd():
    strange_list = StrangeList()

    node1 = Node()
    node1.value = 1

    node2 = Node()
    node2.value = 2
    node2.prev = node1

    node3 = Node()
    node3.value = 3
    node1.next = node3
    node3.prev = node2

    strange_list.first = node1
    strange_list.last = node3

    is_correct = check_strange_list(strange_list)

    print("Test correct strange list with odd length: ", end="")
    if is_correct:
        print("OK")
    else:
        print("FAIL")

def test_check_strange_list_correct_even():
    strange_list = StrangeList()

    node1 = Node()
    node1.value = 1

    node2 = Node()
    node2.value = 2
    node2.prev = node1

    node3 = Node()
    node3.value = 3
    node1.next = node3
    node3.prev = node2

    node4 = Node()
    node4.value = 4
    node2.next = node4
    node4.prev = node3

    strange_list.first = node1
    strange_list.last = node4

    is_correct = check_strange_list(strange_list)

    print("Test correct strange list with even length: ", end="")
    if is_correct:
        print("OK")
    else:
        print("FAIL")

def test_check_strange_list_incorrect():
    strange_list = StrangeList()

    node1 = Node()
    node1.value = 1

    node2 = Node()
    node2.value = 2
    node2.prev = node1

    node3 = Node()
    node3.value = 3
    node1.next = node2
    node3.prev = node2

    node4 = Node()
    node4.value = 4
    node2.next = node4
    node4.prev = node3

    strange_list.first = node1
    strange_list.last = node4

    is_correct = check_strange_list(strange_list)

    print("Test incorrect strange list with wrong next pointer: ", end="")
    if not is_correct:
        print("OK")
    else:
        print("FAIL")

def test_check_strange_list_correct_one_node():
    strange_list = StrangeList()

    node1 = Node()
    node1.value = 1

    strange_list.first = node1
    strange_list.last = node1

    is_correct = check_strange_list(strange_list)

    print("Test correct strange list with one node: ", end="")
    if is_correct:
        print("OK")
    else:
        print("FAIL")


def test_check_strange_list_empty():
    strange_list = StrangeList()

    is_correct = check_strange_list(strange_list)

    print("Test correct strange list empty: ", end="")
    if is_correct:
        print("OK")
    else:
        print("FAIL")




#test_list_to_strange_list_nonempty()
test_check_strange_list_correct_odd()
test_check_strange_list_correct_even()
test_check_strange_list_incorrect()
test_check_strange_list_correct_one_node()
test_check_strange_list_empty()