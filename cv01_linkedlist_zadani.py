class Node:
    """Trida Node slouzi pro reprezentaci objektu v oboustranne
    spojovanem seznamu.

    Atributy:
        value   reprezentuje ulozenou hodnotu/objekt
        next    reference na nasledujici prvek v seznamu
        prev    reference na predchazejici prvek v seznamu
    """
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None


class LinkedList:
    """Trida LinkedList reprezentuje spojovany seznam.

    Atributy:
        first   reference na prvni prvek seznamu
        last    reference na posledni prvek seznamu
    """
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first is None and self.last is None


def insert(linkedList, value):
    """Metoda insert() vlozi na konec seznamu linkedList (za prvek last)
    novy uzel s hodnotou value. Vraci nove vlozeny objekt.
    """

    new_node = Node()
    new_node.value = value
    new_node.prev = linkedList.last

    if linkedList.is_empty():
        linkedList.first = new_node
    else:
        linkedList.last.next = new_node

    linkedList.last = new_node
    return new_node


def print_list(linkedList):
    """Metoda print_list() vypise seznam linkedList."""
    actual_node = linkedList.first
    while actual_node is not None:
        print(actual_node.value, end=" ")
        if actual_node.next is not None:
            print("<->", end=" ")
        actual_node = actual_node.next


def search(linkedList, value):
    """Metoda search() vraci referenci na prvni vyskyt uzlu s hodnotou
    value v seznamu linkedList. Pokud se hodnota v seznamu nenachazi,
    vraci None.
    """
    actual_node = linkedList.first
    while actual_node is not None:
        if value == actual_node.value:
            return actual_node
        actual_node = actual_node.next
    return None



def delete(linkedList, node):
    """Metoda delete() smaze uzel node v seznamu linkedList."""
    if node is None:
        return

    if node.prev is None:
        linkedList.first = node.next
    else:
        node.prev.next = node.next

    if node.next is None:
        linkedList.last = node.prev
    else:
        node.next.prev = node.prev


# Testy implmentace
def test_insert_empty():
    print("Test 1. Vkladani do prazdneho seznamu: ", end="")

    l = LinkedList()
    insert(l, 1)

    if l.first is None or l.last is None:
        print("FAIL")
        return

    if (l.first.value == 1 and l.last.value == 1 and
            l.first.next is None and l.first.prev is None):
        print("OK")
    else:
        print("FAIL")


def test_insert_nonempty():
    print("Test 2. Vkladani do neprazdneho seznamu: ", end="")

    l = LinkedList()
    n = Node()
    n.value = 1
    n.next = None
    l.first = n
    l.last = n

    insert(l, 2)

    if l.last is None:
        print("FAIL")
        return

    if (l.last.value == 2 and l.last.prev is not None and
            l.last.prev == l.first and l.first.value == 1):
        print("OK")
    else:
        print("FAIL")


def test_search_exist():
    print("Test 3. Hledani existujiciho prvku v seznamu: ", end="")

    l = LinkedList()
    n1 = Node()
    n2 = Node()
    n1.value = 1
    n1.next = n2
    n1.prev = None
    n2.value = 2
    n2.next = None
    n2.prev = n1
    l.first = n1
    l.last = n2

    i = search(l, 2)


    if i is n2:
        print("OK")
    else:
        print("FAIL")


def test_search_not_exist():
    print("Test 4. Hledani neexistujiciho prvku v seznamu: ", end="")

    l = LinkedList()
    n1 = Node()
    n2 = Node()
    n1.value = 1
    n1.next = n2
    n1.prev = None
    n2.value = 2
    n2.next = None
    n2.prev = n1
    l.first = n1
    l.last = n2

    i = search(l, 3)

    if i is None:
        print("OK")
    else:
        print("FAIL")


def test_delete_first():
    print("Test 5. Odstraneni prvniho prvku v seznamu: ", end="")

    l = LinkedList()
    n1 = Node()
    n2 = Node()
    n1.value = 1
    n1.next = n2
    n1.prev = None
    n2.value = 2
    n2.next = None
    n2.prev = n1
    l.first = n1
    l.last = n2

    delete(l, n1)

    if l.first is n2 and n2.prev is None:
        print("OK")
    else:
        print("FAIL")


def test_delete_mid():
    print("Test 6. Odstraneni prostredniho prvku v seznamu: ", end="")

    l = LinkedList()
    n1 = Node()
    n2 = Node()
    n3 = Node()
    n1.value = 1
    n1.next = n2
    n1.prev = None
    n2.value = 2
    n2.next = n3
    n2.prev = n1
    n3.value = 3
    n3.next = None
    n3.prev = n2
    l.first = n1
    l.last = n3

    delete(l, n2)

    if (l.last is not n3 or l.last.prev is not n1 or
            l.first.next is not n3):
        print("FAIL")
    else:
        print("OK")


def test_delete_last():
    print("Test 7. Odstraneni posledniho prvku v seznamu: ", end="")

    l = LinkedList()
    n1 = Node()
    n2 = Node()
    n3 = Node()
    n1.value = 1
    n1.next = n2
    n1.prev = None
    n2.value = 2
    n2.next = n3
    n2.prev = n1
    n3.value = 3
    n3.next = None
    n3.prev = n2
    l.first = n1
    l.last = n3

    delete(l, n3)

    if (l.last is not n2 or l.last.prev is not n1 or
            l.first.next is not n2):
        print("FAIL")
    else:
        print("OK")


def test_delete_solo():
    print("Test 8. Odstraneni jedineho prvku v seznamu: ", end="")

    l = LinkedList()
    n1 = Node()
    n1.value = 1
    n1.next = None
    n1.prev = None
    l.first = n1
    l.last = n1

    delete(l, n1)

    if l.last is not None or l.first is not None:
        print("FAIL")
    else:
        print("OK")


def test_insert_return():
    print("Test 9. Vraceni vlozeneho prvku: ", end="")

    l = LinkedList()
    n = insert(l, 1)

    if n is None or n.value != 1:
        print("FAIL")
    else:
        print("OK")


if __name__ == '__main__':
    test_insert_empty()
    test_insert_nonempty()
    test_search_exist()
    test_search_not_exist()
    test_delete_first()
    test_delete_mid()
    test_delete_last()
    test_delete_solo()
    test_insert_return()
