# IB002 Extra domaci ukol 6.
#
# Minimova halda je v kanonickem tvaru, pokud pro kazdy jeji prvek se dvema
# potomky plati, ze jeho levy potomek je mensi nez ten pravy.
#
# Je v kanonickem tvaru | Neni v kanonickem tvaru
#                       |
#       (1)             |           (1)
#      /   \            |          /   \
#    (2)   (3)          |        (3)   (2)


# Trida representujici minimovou haldu. Pro praci s ni muzete s vyhodou pouzit
# funkce, ktere jste implementovali v zakladnim domacim ukolu.

class MinHeap:
    def __init__(self):
        self.size = 0
        self.array = None


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

    return heap.array[left_index(i)]


def right(heap, i):
    """Vrati praveho potomka prvku na pozici 'i' v halde 'heap'.
    Pokud neexistuje, vrati None.
    """
    if right_index(i) >= len(heap.array):
        return None

    return heap.array[right_index(i)]


def swap(heap, i, j):
    """Prohodi prvky na pozicich 'i' a 'j' v halde 'heap'."""
    heap.array[i], heap.array[j] = heap.array[j], heap.array[i]

def heapify(heap, i):
    """Opravi haldu 'heap' tak aby splnovala vlastnost minimove haldy.
    Kontrola zacina u prvku na pozici 'i'."""


    if left_index(i) < heap.size and left(heap, i) < heap.array[i]:
        swap(heap, i, left_index(i))
        heapify(heap, left_index(i))

    if right_index(i) < heap.size and right(heap, i) < heap.array[i]:
        swap(heap, i, right_index(i))
        heapify(heap, right_index(i))


def build_heap(array):
    """Vytvori korektni minimovou haldu z pole 'array'."""
    heap = Min_heap()
    heap.array = array
    heap.size = len(array)

    for i in reversed(range(0, len(heap.array))):
        heapify(heap, i)
    return heap


# Ukol 1.
# Vasim prvnim ukolem je implementovat funkci isCanonicalHeap(heap), ktera
# overi, zda je zadana halda 'heap' v kanonickem tvaru. Pokud ano, vrati True,
# v opacnem pripade vrati False.
#
# Prazdna nebo jednoprvkova halda je v kanonickem tvaru implicitne. Mejte na
# pameti, ze halda v kanonickem tvaru musi splnovat take pozadavky kladene na
# minimovou haldu.

def does_node_fit_min_heap(heap, i):
    does_left_son_fit = (left(heap, i) is None or left(heap, i) >= heap.array[i])
    does_right_son_fit = (right(heap, i) is None or right(heap, i) >= heap.array[i])

    return does_left_son_fit and does_right_son_fit


def does_node_fit_canonical_heap(heap, i):
    if left(heap, i) is None or right(heap, i) is None:
        return True

    return left(heap, i) <= right(heap, i)


def isCanonicalHeap(heap):
    if heap.size == 0 or heap.size == 1:
        return True

    last_index_to_control = parent_index(heap.size - 1)

    for i in range(0, last_index_to_control + 1):
        if not does_node_fit_min_heap(heap, i) or not does_node_fit_canonical_heap(heap, i):
            return False
    return True

'''
def isCanonicalHeapRecursive(heap, current_node_index):
    if is_leaf(heap, current_node_index):
        return True

    does_fit = does_node_fit_canonical_heap(heap, current_node_index)\
               and does_node_fit_min_heap(heap, current_node_index)

    left_son_index = left_index(current_node_index)
    right_son_index = right_index(current_node_index)
    return does_fit and isCanonicalHeapRecursive(heap, left_son_index) and isCanonicalHeapRecursive(heap, right_son_index)

def is_leaf(heap, current_node_index):
    return left(heap, current_node_index) is None and right(heap, current_node_index) is None
'''

# Ukol 2.
# Druhym ukolem je implementovat funkci canoniseHeap(heap), ktera zadanou
# minimovou haldu 'heap' prevede na kanonicky tvar. Funkce bude menit primo
# haldu zadanou v argumentu, proto nebude vracet zadnou navratovou hodnotu.
#
# Snazte se neprovadet zbytecne operace a nezapomente, ze kanonicka halda je
# stale minimovou haldou. Pripady, kdy zadana halda neni minimova,
# osetrovat nemusite.

def is_leaf(heap, current_node_index):
    return left(heap, current_node_index) is None and right(heap, current_node_index) is None


def canonise_heap_recursive(heap, current_node_index):
    if is_leaf(heap, current_node_index):
        return heap

    if not does_node_fit_canonical_heap(heap, current_node_index):
        swap(heap, left_index(current_node_index), right_index(current_node_index))
        heapify(heap, right_index(current_node_index))

    canonise_heap_recursive(heap, left_index(current_node_index))
    canonise_heap_recursive(heap, right_index(current_node_index))


def canoniseHeap(heap):
    canonise_heap_recursive(heap, 0)



def isCanonicalHeap_emptyHeap():
    # Arrange
    heap = MinHeap()
    heap.array = []

    # Act
    is_canonical = isCanonicalHeap(heap)

    # Assert
    print("isCanonicalHeap with empty heap: ", end="")
    if is_canonical:
        print("OK")
    else:
        print("NOK")


def isCanonicalHeap_oneElementHeap():
    # Arrange
    heap = MinHeap()
    heap.array = [1]
    heap.size = 1

    # Act
    is_canonical = isCanonicalHeap(heap)

    # Assert
    print("isCanonicalHeap with one element heap: ", end="")
    if is_canonical:
        print("OK")
    else:
        print("NOK")

def isCanonicalHeap_three_elements_True():
    # Arrange
    heap = MinHeap()
    heap.array = [1, 2, 3]
    heap.size = 3

    # Act
    is_canonical = isCanonicalHeap(heap)

    # Assert
    print("isCanonicalHeap with three elements heap True: ", end="")
    if is_canonical:
        print("OK")
    else:
        print("NOK")


def isCanonicalHeap_three_elements_False():
    # Arrange
    heap = MinHeap()
    heap.array = [1, 3, 2]
    heap.size = 3

    # Act
    is_canonical = isCanonicalHeap(heap)

    # Assert
    print("isCanonicalHeap with three elements heap False: ", end="")
    if not is_canonical:
        print("OK")
    else:
        print("NOK")


def isCanonicalHeap_complex_heap_true():
    # Arrange
    heap = MinHeap()
    heap.array = [1, 2, 3, 4, 5, 6, 7]
    heap.size = len(heap.array)

    # Act
    is_canonical = isCanonicalHeap(heap)

    # Assert
    print("isCanonicalHeap complex heap True: ", end="")
    if is_canonical:
        print("OK")
    else:
        print("NOK")


def isCanonicalHeap_complex_not_min_heap_false():
    # Arrange
    heap = MinHeap()
    heap.array = [1, 2, 6, 4, 5, 3, 7]
    heap.size = len(heap.array)

    # Act
    is_canonical = isCanonicalHeap(heap)

    # Assert
    print("isCanonicalHeap complex non min heap False: ", end="")
    if not is_canonical:
        print("OK")
    else:
        print("NOK")


def isCanonicalHeap_complex_not_canonical_false():
    # Arrange
    heap = MinHeap()
    heap.array = [1, 2, 3, 4, 5, 7, 6]
    heap.size = len(heap.array)

    # Act
    is_canonical = isCanonicalHeap(heap)

    # Assert
    print("isCanonicalHeap complex non canonical heap False: ", end="")
    if not is_canonical:
        print("OK")
    else:
        print("NOK")


isCanonicalHeap_emptyHeap()
isCanonicalHeap_oneElementHeap()
isCanonicalHeap_three_elements_True()
isCanonicalHeap_three_elements_False()
isCanonicalHeap_complex_heap_true()
isCanonicalHeap_complex_not_min_heap_false()
isCanonicalHeap_complex_not_canonical_false()


def canoniseHeap_oneElementHeap():
    # Arrange
    heap = MinHeap()
    heap.array = [1]
    heap.size = 1

    # Act
    canoniseHeap(heap)

    # Assert
    print("Canonise_Heap with one element heap: ", end="")
    if heap.array == [1]:
        print("OK")
    else:
        print("NOK")


def canoniseHeap_threeElementHeap_canonical():
    # Arrange
    heap = MinHeap()
    heap.array = [1, 2, 3]
    heap.size = 3

    # Act
    canoniseHeap(heap)

    # Assert
    print("Canonise_Heap with three elements heap: ", end="")
    if heap.array == [1, 2, 3]:
        print("OK")
    else:
        print("NOK")


def canoniseHeap_threeElementHeap_non_canonical():
    # Arrange
    heap = MinHeap()
    heap.array = [1, 3, 2]
    heap.size = 3

    # Act
    canoniseHeap(heap)

    # Assert
    print("Canonise_Heap with three elements heap: ", end="")
    if heap.array == [1, 2, 3]:
        print("OK")
    else:
        print("NOK")

def canoniseHeap_complex_heap_non_canonical():
    # Arrange
    heap = MinHeap()
    heap.array = [5, 10, 7, 20, 19, 8, 9]
    heap.size = 7

    # Act
    canoniseHeap(heap)

    # Assert
    print("Canonise_Heap complex heap: ", end="")
    if heap.array == [5, 7, 8, 19, 20, 9, 10]:
        print("OK")
    else:
        print("NOK")



canoniseHeap_oneElementHeap()
canoniseHeap_threeElementHeap_canonical()
canoniseHeap_threeElementHeap_non_canonical()
canoniseHeap_complex_heap_non_canonical()
