import random


# Vasim ukolem bude naimplementovat rekurzivni a iterativni verze
# algoritmu pro binarni vyhledavani a vyhledavani minima a maxima
# v poli.
#
# Prepsani na iterativni algoritmus muzete v pripade binarniho
# vyhledavani zkusit napsat pomoci zasobniku, tato cast vsak neni
# povinna.
#
# U funkci na hledani dvojice minima a maxima nesmite pouzit pouze
# vestavene funkce min a max (muzete je pouzivat na dvojice, ne na cele
# pole).


def binary_search_recursive(array, left, right, key):
    """
    Funkce rekurzivne ve vzestupne usporadanem poli 'array' vyhleda klic
    'key'. Hleda se pouze v rozsahu od indexu 'left' do indexu 'right'.
    Funkce vraci index nalezeneho prvku, pokud prvek v posloupnosti
    neni, vraci -1.
    """

    current_middle_index = left + ((right - left) // 2)
    current_middle = array[current_middle_index]
    if left > right:
        return -1
    if current_middle == key:
        return current_middle_index

    if current_middle < key:
        return binary_search_recursive(array, current_middle_index + 1, right, key)
    else:
        return binary_search_recursive(array, left, current_middle_index - 1, key)



def binary_search_iterative(array, left, right, key):
    """Iterativni verze predesle funkce.
    Iterativni podobu napiste podle intuice.
    """
    return -1
    # TODO


# Nepovinna funkce (ale vhodna procviceni se)
def binary_search_iterative_stack(array, left, right, key):
    """Iterativni verze funkce 'binary_search_recursive', kde k prevodu
    do iterativni podoby pouzijte zasobnik. Do zasobniku si chcete
    ukladat stav volani.

    Jedna se o bonusovou cast, neni povinne ji delat a i reseni je
    zvlastni. Predchozi algoritmus bude nakonec mnohem intuitivnejsi,
    toto by vam melo jen ukazat, jak se prevod na iterativni verzi dela.

    Nebudte prekvapeni, ze se zasobnik nakonec moc nepouzije. Pokud si
    chcete vyzkouset prevod rekurze na iterativni algoritmus pomoci
    zasobniku poradne, zkuste jej pouzit v min_max_search_iterative.
    """

    # zde je ukazka, jak pouzit list v Pythonu jako zasobnik
    # pro ukladani usporadanych dvojic
    stack = [(left, right)]
    while stack:
        (l, r) = stack.pop()
        # TODO
    return -1


def min_max_search_recursive(array, left, right):
    """Funkce vyhleda hodnoty minima a maxima v poli 'array' pomoci
    rozdeluj a panuj algoritmu.
    V poli se hleda v rozsahu od indexu 'left' do indexu 'right'.
    """
    if left == right:
        minimum = array[left]
        maximum = array[left]
        return minimum, maximum

    middle_index = (right + left) // 2
    right_min, right_max = min_max_search_recursive(array, middle_index + 1, right)
    left_min, left_max = min_max_search_recursive(array, left, middle_index)

    return min(right_min, left_min), max(right_max, left_max)


def min_max_search_iterative(array, left, right):
    """Iterativni verze predesle funkce. Iterativni podobu napiste podle
    intuice.
    Pokud chcete, muzete zkusit prepis do iterativni podoby pomoci
    zasobniku. Je to dobry trenink.
    Navodem by vam mohlo byt:
    http://www.codeproject.com/Articles/418776/How-to-replace-recursive-functions-using-stack-and
    """
    minimum = array[left]
    maximum = array[left]

    for i in range(left, right + 1):
        if array[i] < minimum:
            minimum = array[i]
        if array[i] > maximum:
            maximum = array[i]
    return minimum, maximum

# Nize nasleduji testy, nemodifikujte je prosim.
def test_binary_search_recursive():
    print("Test 1. rekurzivni vyhledavani, prvek v poli neni:")
    array1 = [i for i in range(100)]
    ret = binary_search_recursive(array1, 0, 99, 100)
    if ret == -1:
        print("OK")
    else:
        print("NOK, v [0..99] se 100 nevyskytuje,")
        print("vracite {} != -1".format(ret))

    print("Test 2. rekurzivni vyhledavani, prvek v poli je na konci:")
    array2 = [i for i in range(100)]
    ret = binary_search_recursive(array2, 0, 99, 99)
    if ret == 99:
        print("OK")
    else:
        print("NOK, v [0..99] je 99 na pozici 99")
        print("vracite {} != 99".format(ret))

    print("Test 3. rekurzivni vyhledavani, prvek v poli je na zacatku:")
    array3 = [i for i in range(100)]
    ret = binary_search_recursive(array3, 0, 99, 0)
    if ret == 0:
        print("OK")
    else:
        print("NOK, v [0..99] je 0 na pozici 0")
        print("vracite {} != 0".format(ret))

    print("Test 4. rekurzivni vyhledavani, prvek v poli je kdekoliv:")
    array4 = [i for i in range(100)]
    ret = binary_search_recursive(array4, 0, 99, 33)
    if ret == 33:
        print("OK")
    else:
        print("NOK, v [0..99] je 33 na pozici 33")
        print("vracite {} != 33".format(ret))

    print("Test 5. rekurzivni vyhledavani, nahodne prvky:")
    array5 = []
    for i in range(100):
        array5.append(random.randint(1, 1000000000))
    array5.sort()
    ret = binary_search_recursive(array5, 0, 99, array5[68])
    if ret == 68:
        print("OK")
    else:
        print("NOK, v posloupnosti se hledal klic 68. prvku")
        print("vracite {} != 68".format(ret))


def test_binary_search_iterative():
    print("\nTest 6. iterativni vyhledavani, prvek v poli neni:")
    array1 = [i for i in range(100)]
    ret = binary_search_iterative(array1, 0, 99, 100)
    if ret == -1:
        print("OK")
    else:
        print("NOK, v [0..99] se 100 nevyskytuje,")
        print("vracite {} != -1".format(ret))

    print("Test 7. iterativni vyhledavani, prvek v poli je na konci:")
    array2 = [i for i in range(100)]
    ret = binary_search_iterative(array2, 0, 99, 99)
    if ret == 99:
        print("OK")
    else:
        print("NOK, v [0..99] je 99 na pozici 99")
        print("vracite {} != 99".format(ret))

    print("Test 8. iterativni vyhledavani, prvek v poli je na zacatku:")
    array3 = [i for i in range(100)]
    ret = binary_search_iterative(array3, 0, 99, 0)
    if ret == 0:
        print("OK")
    else:
        print("NOK, v [0..99] je 0 na pozici 0")
        print("vracite {} != 0".format(ret))

    print("Test 9. iterativni vyhledavani, prvek v poli je kdekoliv:")
    array4 = [i for i in range(100)]
    ret = binary_search_iterative(array4, 0, 99, 33)
    if ret == 33:
        print("OK")
    else:
        print("NOK, v [0..99] je 33 na pozici 33")
        print("vracite {} != 33".format(ret))

    print("Test 10. iterativni vyhledavani, nahodne prvky:")
    array5 = []
    for i in range(100):
        array5.append(random.randint(1, 1000000000))
    array5.sort()
    ret = binary_search_iterative(array5, 0, 99, array5[68])
    if ret == 68:
        print("OK")
    else:
        print("NOK, v posloupnosti se hledal klic 68. prvku")
        print("vracite {} != 68".format(ret))


def test_binary_search_iterative_stack():
    print("\nTest 11. iterativni vyhledavani (pomoci zasobniku, ", end="")
    print("nepovinne), prvek v poli neni:")
    array1 = [i for i in range(100)]
    ret = binary_search_iterative_stack(array1, 0, 99, 100)
    if ret == -1:
        print("OK")
    else:
        print("NOK, v [0..99] se 100 nevyskytuje,")
        print("vracite {} != -1".format(ret))

    print("Test 12. iterativni vyhledavani (pomoci zasobniku, ", end="")
    print("nepovinne), prvek v poli je na konci:")
    array2 = [i for i in range(100)]
    ret = binary_search_iterative_stack(array2, 0, 99, 99)
    if ret == 99:
        print("OK")
    else:
        print("NOK, v [0..99] je 99 na pozici 99")
        print("vracite {} != 99".format(ret))

    print("Test 13. iterativni vyhledavani (pomoci zasobniku, ", end="")
    print("nepovinne), prvek v poli je na zacatku:")
    array3 = [i for i in range(100)]
    ret = binary_search_iterative_stack(array3, 0, 99, 0)
    if ret == 0:
        print("OK")
    else:
        print("NOK, v [0..99] je 0 na pozici 0")
        print("vracite {} != 0".format(ret))

    print("Test 14. iterativni vyhledavani (pomoci zasobniku, ", end="")
    print("nepovinne), prvek v poli je kdekoliv:")
    array4 = [i for i in range(100)]
    ret = binary_search_iterative_stack(array4, 0, 99, 33)
    if ret == 33:
        print("OK")
    else:
        print("NOK, v [0..99] je 33 na pozici 33")
        print("vracite {} != 33".format(ret))

    print("Test 15. iterativni vyhledavani (pomoci zasobniku, ", end="")
    print("nepovinne), nahodne prvky:")
    array5 = []
    for i in range(100):
        array5.append(random.randint(1, 1000000000))
    array5.sort()
    ret = binary_search_iterative_stack(array5, 0, 99, array5[68])
    if ret == 68:
        print("OK")
    else:
        print("NOK, v posloupnosti se hledal klic 68. prvku")
        print("vracite {} != 68".format(ret))


def test_min_max_search_recursive():
    print("\nTest 16. rekurzivni vyhledavani minima a maxima v poli [1]:")
    array1 = [1]
    ret = min_max_search_recursive(array1, 0, 0)
    if ret == (1, 1):
        print("OK")
    else:
        print("NOK, v poli [1] je min 1 a max 1,")
        print("vracite {} != (1, 1)".format(ret))

    print("Test 17. rekurzivni vyhledavani minima a maxima v poli [2, 1]:")
    array2 = [2, 1]
    ret = min_max_search_recursive(array2, 0, 1)
    if ret == (1, 2):
        print("OK")
    else:
        print("NOK, v poli [2, 1] je min 1 a max 2,")
        print("vracite {} != (1, 2)".format(ret))

    print("Test 18. rekurzivni vyhledavani minima a maxima v poli [0..99]:")
    array3 = [i for i in range(100)]
    ret = min_max_search_recursive(array3, 0, 99)
    if ret == (0, 99):
        print("OK")
    else:
        print("NOK, v poli [0..99] je min 0 a max 99,")
        print("vracite {} != (0, 99)".format(ret))

    print("Test 19. rekurzivni vyhledavani minima a maxima v poli ", end="")
    print("nahodnych cisel:")
    array4 = [random.randint(1, 1000) for i in range(100)]
    array4[21] = 0
    array4[45] = 1001
    ret = min_max_search_recursive(array4, 0, 99)
    if ret == (0, 1001):
        print("OK")
    else:
        print("NOK, v poli je min 0 a max 1001,")
        print("vracite {} != (0, 1001)".format(ret))

    print("Test 20. rekurzivni vyhledavani minima a maxima v poli ", end="")
    print("nahodnych cisel (opakujici se minimum a maximum):")
    array5 = [random.randint(1, 1000) for i in range(100)]
    array5[21] = 0
    array5[61] = 0
    array5[42] = 1001
    array5[45] = 1001
    ret = min_max_search_recursive(array5, 0, 99)
    if ret == (0, 1001):
        print("OK")
    else:
        print("NOK, v poli je min 0 a max 1001,")
        print("vracite {} != (0, 1001)".format(ret))


def test_min_max_search_iterative():
    print("\nTest 21. iterativni vyhledavani minima a maxima v poli [1]:")
    array1 = [1]
    ret = min_max_search_iterative(array1, 0, 0)
    if ret == (1, 1):
        print("OK")
    else:
        print("NOK, v poli [1] je min 1 a max 1,")
        print("vracite {} != (1, 1)".format(ret))

    print("Test 22. iterativni vyhledavani minima a maxima v poli [2, 1]:")
    array2 = [2, 1]
    ret = min_max_search_iterative(array2, 0, 1)
    if ret == (1, 2):
        print("OK")
    else:
        print("NOK, v poli [2, 1] je min 1 a max 2,")
        print("vracite {} != (1, 2)".format(ret))

    print("Test 23. iterativni vyhledavani minima a maxima v poli [0..99]:")
    array3 = [i for i in range(100)]
    ret = min_max_search_iterative(array3, 0, 99)
    if ret == (0, 99):
        print("OK")
    else:
        print("NOK, v poli [0..99] je min 0 a max 99,")
        print("vracite {} != (0, 99)".format(ret))

    print("Test 24. iterativni vyhledavani minima a maxima ", end="")
    print("v poli nahodnych cisel:")
    array4 = [random.randint(1, 1000) for i in range(100)]
    array4[21] = 0
    array4[45] = 1001
    ret = min_max_search_iterative(array4, 0, 99)
    if ret == (0, 1001):
        print("OK")
    else:
        print("NOK, v poli je min 0 a max 1001,")
        print("vracite {} != (0, 1001)".format(ret))

    print("Test 25. iterativni vyhledavani minima a maxima v poli ", end="")
    print("nahodnych cisel (opakujici se minimum a maximum):")
    array5 = [random.randint(1, 1000) for i in range(100)]
    array5[21] = 0
    array5[61] = 0
    array5[42] = 1001
    array5[45] = 1001
    ret = min_max_search_iterative(array5, 0, 99)
    if ret == (0, 1001):
        print("OK")
    else:
        print("NOK, v poli je min 0 a max 1001,")
        print("vracite {} != (0, 1001)".format(ret))


if __name__ == '__main__':
    test_binary_search_recursive()
    test_binary_search_iterative()
    test_binary_search_iterative_stack()
    test_min_max_search_recursive()
    test_min_max_search_iterative()
