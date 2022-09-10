class Item:
    """ Trida Item slouzi pro reprezentaci objektu v zasobniku.

    Atributy:
        value   reprezentuje ulozenou hodnotu/objekt
        below   reference na predchazejici prvek v zasobniku
    """
    def __init__(self):
        self.value = None
        self.below = None


class Stack:
    """Trida stack reprezentuje zasobnik.

    Atributy:
        top     reference na vrchni prvek v zasobniku
    """
    def __init__(self):
        self.top = None


def push(stack, value):
    """Metoda push() vlozi na vrchol zasobniku (stack) novy prvek
    s hodnotou (value).
    """
    pass
    # TODO


def pop(stack):
    """Metoda pop() odebere vrchni prvek zasobniku. Vraci hodnotu
    (value) odebraneho prvku, pokud je zasobnik prazdny vraci None.
    """
    pass
    # TODO


def is_empty(stack):
    """Metoda isEmpty() vraci True v pripade prazdneho zasobniku,
    jinak False.
    """
    pass
    # TODO


# Testy implementace
def test_push_empty():
    print("Test 1. Vkladani do prazdneho zasobniku: ", end="")

    s = Stack()
    push(s, 1)

    if s.top is None:
        print("FAIL")
        return

    if s.top.value is 1 and s.top.below is None:
        print("OK")
    else:
        print("FAIL")


def test_push_nonempty():
    print("Test 2. Vkladani do neprazdneho zasobniku: ", end="")

    s = Stack()
    i = Item()
    i.below = None
    i.value = 1
    s.top = i

    push(s, 2)

    if s.top is None:
        print("FAIL")
        return
    if s.top.value == 2 and s.top.below == i:
        print("OK")
    else:
        print("FAIL")


def test_pop_empty():
    print("Test 3. Odebirani z prazdneho zasobniku: ", end="")

    s = Stack()
    v = pop(s)

    if v is not None or s.top is not None:
        print("FAIL")
    else:
        print("OK")


def test_pop_nonempty():
    print("Test 4. Odebirani z neprazdneho zasobniku: ", end="")
    s = Stack()
    i = Item()
    i.value = 1
    i.below = None
    s.top = i

    v = pop(s)

    if v is not 1 or s.top is not None:
        print("FAIL")
    else:
        print("OK")


def test_is_empty_empty():
    print("Test 5. isEmpty na prazdnem zasobniku: ", end="")

    s = Stack()

    if is_empty(s):
        print("OK")
    else:
        print("FAIL")


def test_is_empty_nonempty():
    print("Test 6. isEmpty na neprazdnem zasobniku: ", end="")

    s = Stack()
    i = Item()
    i.below = None
    i.value = 1
    s.top = i

    if is_empty(s):
        print("FAIL")
    else:
        print("OK")


if __name__ == '__main__':
    test_push_empty()
    test_push_nonempty()
    test_pop_empty()
    test_pop_nonempty()
    test_is_empty_empty()
    test_is_empty_nonempty()
