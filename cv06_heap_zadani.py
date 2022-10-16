import random
import sys


class Min_heap:
    """Trida Heap slouzi k reprezentaci haldy.

    Atributy:
        size    pocet prvku v halde
        array   pole prvku haldy
    """
    def __init__(self):
        self.size = 0
        self.array = None


# Naimplementujte nasledujici funkce pro ziskani prvku v halde:
# POZOR: Nezapomente, ze indexujeme pole od 0.

def parent_index(i):
    """Vrati index rodice prvku na pozici 'i'.
    Pokud neexistuje, vrati None.
    """
    my_parent_index = (i - 1) // 2

    if my_parent_index < 0:
        return None
    return my_parent_index


def left_index(i):
    """Vrati index leveho potomka prvku na pozici 'i'."""
    my_left_index = (i * 2) + 1
    return my_left_index


def right_index(i):
    """Vrati index praveho potomka prvku na pozici 'i'."""
    my_right_index = (i * 2) + 2
    return my_right_index


def parent(heap, i):
    """Vrati rodice prvku na pozici 'i' v halde 'heap'.
    Pokud neexistuje, vrati None.
    """
    if parent_index(i) is None:
        return None
    return heap.array[parent_index(i)]


def left(heap, i):
    """Vrati leveho potomka prvku na pozici 'i' v halde 'heap'.
    Pokud neexistuje, vrati None.
    """
    if left_index(i) >= len(heap.array):
        return None
    else:
        return heap.array[left_index(i)]


def right(heap, i):
    """Vrati praveho potomka prvku na pozici 'i' v halde 'heap'.
    Pokud neexistuje, vrati None.
    """
    if right_index(i) >= len(heap.array):
        return None
    else:
        return heap.array[right_index(i)]


def swap(heap, i, j):
    """Prohodi prvky na pozicich 'i' a 'j' v halde 'heap'."""
    heap.array[i], heap.array[j] = heap.array[j], heap.array[i]


def heapify(heap, i):
    """Opravi haldu 'heap' tak aby splnovala vlastnost minimove haldy.
    Kontrola zacina u prvku na pozici 'i'.
    """
    index_to_control = i

    if index_to_control > len(heap.array):
        return heap

    if parent_index(index_to_control) is not None and \
            heap.array[index_to_control] < parent(heap, index_to_control):
        swap(heap, index_to_control, parent_index(i))
        heapify(heap, parent_index(index_to_control))

    index_to_control += 1


def build_heap(array):
    """Vytvori korektni minimovou haldu z pole 'array'."""
    heap = Min_heap()
    heap.array = array
    heap.size = len(array)

    heapify(heap, len(array) - 1)
    return heap


def decrease_key(heap, i, value):
    """Snizi hodnotu prvku haldy 'heap' na pozici 'i' na hodnotu 'value'
    a opravi vlastnost haldy 'heap'.
    """
    if heap.array[i] > value:
        heap.array[i] = value
        heapify(heap, i)
    else:
        return heap


def insert(heap, value):
    """Vlozi hodnotu 'value' do haldy 'heap'."""

    heap.array.append(value)
    heap.size += 1
    heapify(heap, heap.size - 1)



def extract_min(heap):
    """Odstrani minimalni prvek haldy 'heap'. Vraci hodnotu odstraneneho
    prvku. Pokud je halda prazdna, vraci None.
    """
    if heap.size == 0:
        return None

    smallest_number = heap.array[0]
    heap.array.pop(0)
    heap.size -= 1
    heapify(heap, heap.size - 1)
    return smallest_number


def heap_sort(array):
    """Seradi pole 'array' pomoci haldy od nejvetsiho prvku po nejmensi.
    Vraci serazene pole.
    """
    heap = build_heap(array)
    print(heap.array)
    return heap.array
    pass


# Graphviz funkce.
# Vytvori haldu jako graf ve formatu ".dot"."""
#
# Dodatek k graphvizu:
# Graphviz je nastroj, ktery vam umozni vizualizaci datovych struktur,
# coz se hodi predevsim pro ladeni. Tento program generuje nekolik
# souboru neco.dot v mainu. Vygenerovane soubory nahrajte do online
# nastroje pro zobrazeni graphvizu:
# http://sandbox.kidstrythisathome.com/erdos/
# nebo http://www.webgraphviz.com/ - zvlada i vetsi grafy.
#
# Alternativne si muzete nainstalovat prekladac z jazyka dot do obrazku
# na svuj pocitac.
def make_graphviz(heap, i, f):
    f.write("\"%i\"\n" % (heap.array[i]))
    if (left_index(i) < heap.size):
        f.write("\"%i\" -> \"%i\"\n" % (heap.array[i], left(heap, i)))
        make_graphviz(heap, left_index(i), f)
    if (right_index(i) < heap.size):
        f.write("\"%i\" -> \"%i\"\n" % (heap.array[i], right(heap, i)))
        make_graphviz(heap, right_index(i), f)


def make_graph(heap, fileName):
    f = open(fileName, 'w')
    f.write("digraph Heap {\n")
    f.write("node [color=lightblue2, style=filled];\n")
    if heap.size > 0:
        make_graphviz(heap, 0, f)
    f.write("}\n")
    f.close()


def test_indexes():
    print("Test 1. indexovani parent, left, right: "),
    if (parent_index(2) != 0 or
            parent_index(1) != 0 or
            parent_index(0) is not None):
        print("NOK - chybny parent_index")
        return False
    if left_index(0) != 1 or left_index(3) != 7:
        print("NOK - chybny left_index")
        return False
    if right_index(0) != 2 or right_index(3) != 8:
        print("NOK - chybny right_index")
        return False

    heap = Min_heap()
    heap.array = [1, 2, 3]
    heap.size = len(heap.array)
    try:
        if (parent(heap, 0) is not None or
                parent(heap, 1) != 1 or
                parent(heap, 2) != 1):
            print("NOK - chyba ve funkci parent")
            return False
        if left(heap, 0) != 2 or left(heap, 1) is not None:
            print("NOK - chyba ve funkci left")
            return False
        if right(heap, 0) != 3 or right(heap, 1) is not None:
            print("NOK - chyba ve funkci right")
            return False
    except IndexError:
        print("NOK - pristup mimo pole")
        return False
    print("OK")
    return True


def test_build_heap():
    print("Test 2. build_heap: "),
    array = [4, 3, 1]
    heap = build_heap(array)
    if (heap.array == [1, 3, 4] or heap.array == [1, 4, 3]) and heap.size == 3:
        print("OK")
    else:
        print("NOK - chyba ve funkci build_heap")
    try:
        make_graph(heap, "built.dot")
        print("Vykreslenou haldu najdete v souboru build.dot")
    except:
        print("Chyba ve vykreslovani, ", end="")
        print("je potreba mit spravne nastavenou heap.size")


def test_insert_heap():
    print("Test 3. insert_heap: "),
    heap = Min_heap()
    heap.array = []
    heap.size = 0

    insert(heap, 2)
    if heap.array != [2] or heap.size != 1:
        print("NOK - chyba ve funkci insert na prazdne halde")
    else:
        insert(heap, 3)
        insert(heap, 4)
        if heap.array != [2, 3, 4] or heap.size != 3:
            print("NOK - chyba ve funkci insert na neprazdne halde")
        else:
            insert(heap, 5)
            if heap.array != [2, 3, 4, 5] or heap.size != 4:
                print("NOK - chyba ve funkci insert na neprazdne halde")
            else:
                insert(heap, 1)
                if heap.array != [1, 2, 4, 5, 3] or heap.size != 5:
                    print("NOK - chyba ve funkci insert na neprazdne halde")
                else:
                    print("OK")
    try:
        make_graph(heap, "insert.dot")
        print("Vykreslenou haldu najdete v souboru insert.dot")
    except:
        print("Chyba ve vykreslovani, ", end="")
        print("je potreba mit spravne nastavenou heap.size")


def test_decrease_key():
    print("Test 4. decrease_key: "),
    heap = Min_heap()
    heap.array = [2, 3, 4]
    heap.size = 3
    decrease_key(heap, 2, 1)

    if heap.array != [1, 3, 2] or heap.size != 3:
        print("NOK - chyba ve funkci decrease_key")
    else:
        decrease_key(heap, 0, 4)
        if heap.array != [1, 3, 2] or heap.size != 3:
            print("NOK - chyba ve funkci decrease_key")
        else:
            print("OK")
    try:
        make_graph(heap, "decrease.dot")
        print("Vykreslenou haldu najdete v souboru decrease.dot")
    except:
        print("Chyba ve vykreslovani, ", end="")
        print("je potreba mit spravne nastavenou heap.size")


def test_extract_min():
    print("Test 5. extract_min: "),
    heap = Min_heap()
    heap.array = [2, 3, 4, 5]
    heap.size = 4

    tmp = extract_min(heap)

    if heap.array[0:heap.size] != [3, 5, 4] or tmp != 2:
        print("NOK - chyba ve funkci extract_min")
    else:
        tmp = extract_min(heap)
        if heap.array[0:heap.size] != [4, 5] or tmp != 3:
            print("NOK - chyba ve funkci extract_min")
        else:
            tmp = extract_min(heap)
            if heap.array[0:heap.size] != [5] or tmp != 4:
                print("NOK - chyba ve funkci extract_min")
            else:
                tmp = extract_min(heap)
                if heap.array[0:heap.size] != [] or tmp != 5:
                    print("NOK - chyba ve funkci extract_min")
                else:
                    try:
                        if extract_min(heap) is None:
                            print("OK")
                    except:
                        print("NOK - chyba ve funkci ", end="")
                        print("extract_min na prazne halde")
    try:
        make_graph(heap, "extract.dot")
        print("Vykreslenou haldu najdete v souboru extract.dot")
    except:
        print("Chyba ve vykreslovani, ", end="")
        print("je potreba mit spravne nastavenou heap.size")


def test_heap_sort():
    array = [8, 4, 9, 3, 2, 7, 5, 0, 6, 1]
    print("Test 6. heap_sort: "),
    if heap_sort(array) != [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
        print("NOK - chyba ve funkci heap_sort, vraci neserazene pole")
    else:
        print("OK")


if __name__ == '__main__':
    if (test_indexes()):
        test_build_heap()
        test_decrease_key()
        test_insert_heap()
        test_extract_min()
        test_heap_sort()
