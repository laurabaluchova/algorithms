class Item:
    """Trida Item slouzi pro reprezentaci objektu ve fronte.

    Atributy:
        value   reprezentuje ulozenou hodnotu/objekt
        left    reference na predchazejici prvek ve fronte
    """
    def __init__(self):
        self.value = None
        self.left = None


class Queue:
    """Trida Queue reprezentuje frontu.

    Atributy:
        atribut first je reference na prvni prvek
        atribut last je reference na posledni prvek
    """
    def __init__(self):
        self.first = None
        self.last = None


def enqueue(queue, value):
    """Metoda enqueue vlozi do fronty (queue) novy prvek s hodnotou
    (value).
    """
    new_item = Item()
    new_item.value = value

    if isEmpty(queue):
        queue.first = new_item
    else:
        queue.last.left = new_item

    queue.last = new_item


def dequeue(queue):
    """Metoda dequeue odebere prvni prvek z fronty (queue).
    Vraci hodnotu (value) odebraneho prvku, pokud je fronta prazdna,
    vraci None
    """
    if isEmpty(queue):
        return None

    deleted_item = queue.first
    if queue.first.left is None:
        queue.first = None
        queue.last = None
        return deleted_item.value
    queue.first = queue.first.left
    return deleted_item.value


def isEmpty(queue):
    """isEmpty() vraci True v pripade prazdne fronty, jinak False."""
    return queue.last is None and queue.first is None


# Testy implmentace
def test_enqueue_empty():
    print("Test 1. Vkladani do prazdne fronty: ", end="")

    q = Queue()
    enqueue(q, 1)

    if q.first is None or q.last is None:
        print("FAIL")
        return

    if (q.first.value == 1 and q.first.left is None and
            q.last.value == 1 and q.last.left is None):
        print("OK")
    else:
        print("FAIL")


def test_enqueue_nonempty():
    print("Test 2. Vkladani do neprazdne fronty: "),

    q = Queue()
    i = Item()
    i.left = None
    i.value = 1
    q.first = i
    q.last = i

    enqueue(q, 2)

    if q.first is None or q.last is None:
        print("FAIL")
        return
    if q.last.value == 2 and q.first is i and q.first.left.value == 2:
        print("OK")
    else:
        print("FAIL")


def test_dequeue_empty():
    print("Test 3. Odebirani z prazdne fronty: "),

    q = Queue()
    v = dequeue(q)

    if v is not None or q.first is not None or q.last is not None:
        print("FAIL")
    else:
        print("OK")


def test_dequeue_nonempty():
    print("Test 4. Odebirani z neprazdne fronty: "),

    q = Queue()
    i = Item()
    i.value = 1
    i.left = None
    q.first = i
    q.last = i

    v = dequeue(q)

    if v != 1 or q.first is not None or q.last is not None:
        print("FAIL")
    else:
        print("OK")


def test_isEmpty_empty():
    print("Test 5. isEmpty na prazdne fronte: "),

    q = Queue()

    if isEmpty(q):
        print("OK")
    else:
        print("FAIL")


def test_isEmpty_nonempty():
    print("Test 6. isEmpty na neprazdne fronte: "),

    q = Queue()
    i = Item()
    i.left = None
    i.value = 1
    q.first = i
    q.last = i

    if isEmpty(q):
        print("FAIL")
    else:
        print("OK")


if __name__ == '__main__':
    test_enqueue_empty()
    test_enqueue_nonempty()
    test_dequeue_empty()
    test_dequeue_nonempty()
    test_isEmpty_empty()
    test_isEmpty_nonempty()
