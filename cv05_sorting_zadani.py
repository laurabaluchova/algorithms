#!/usr/bin/python3
import random


###########################
# Dotaz studenta:
#
#
###########################

# Chcete-li dostat odpoved, vlozte do nazvu souboru heslo KONTROLA.


# Vasim ukolem v teto implementacni uloze je naprogramovat zakladni
# radici algoritmy. Formulace problemu neni vzdy stejna jako je ve
# sbirce, musite splnit zadani v komentari nad funkci.
#
# Povinne jsou pro vas radici algoritmy InsertSort, MergeSort, QuickSort
# a CountingSort. Zbyle algoritmy presto doporucujeme naimplementovat.


def swap(array, i, j):
    """Pomocna funkce swap pro vas, bere argumenty pole 'array', ve kterem
    prohodi prvky na pozicich indexu 'i' a 'j'.
    """
    array[i], array[j] = array[j], array[i]
    return


# TODO: dopsat tuto funkci
def insert_sort(array):
    """Razeni vkladanim. V kazdem pruchodu se nasledujici prvek posouva
    v poli 'array' tak dlouho, dokud nenarazi na mensi prvek, nebo na zacatek.
    Velikost vstupniho pole ziskate pomoci 'len(array)'.
    """
    # TODO
    pass


# TODO: dopsat tuto funkci
def quick_sort_in_place(array, i, j):
    """Razeni rozdelovanim (QuickSort). Zadane pole 'array' v rozsahu
    indexu 'i' a 'j' rekurzivne seradte bez pouziti pomocneho pole.
    Jako pivot se voli posledni prvek zadaneho rozsahu.
    """
    # TODO
    pass


# TODO: dopsat tuto funkci
def merge(array, aux, left, mid, right):
    """Slevani pro razeni spojovanim (MergeSort). Zadane pole 'array'
    obsahuje 2 usporadane posloupnosti v intervalech od 'left' po 'mid'
    a od 'mid'+1 po 'right'. K spojeni pouzijte pomocne pole 'aux'.
    Vysledek ulozte v poli 'array'.
    """
    # TODO
    pass


# TODO: dopsat tuto funkci
def merge_sort(array, aux, left, right):
    """Razeni spojovanim (MergeSort). Seradte zadane pole 'array'
    v intervalu od indexu 'left' po index 'right'.
    Pouzijte pomocnou funkci 'merge' a pomocne pole 'aux'. Vysledek
    ulozte v poli 'array'.
    """
    # TODO
    pass


# TODO: dopsat tuto funkci
def counting_sort(array, low, high):
    """Razeni pocitanim (CountingSort). Seradte zadane pole 'array'
    pricemz o poli vite, ze se v nem nachazeji pouze hodnoty v intervalu
    od 'low' po 'high' (vcetne okraju intervalu). Vratte serazene pole.
    """
    # TODO
    return array


# Nasledujici radici algoritmy nejsou povinne, presto je doporucujeme
# naimplementovat jako cviceni. Nejsou to nejtezsi radici algoritmy,
# takze je mozna vhodne je v ramci treninku implementovat drive nez
# zbyle optimalni radici algoritmy.


# TODO: dopsat tuto funkci
def minIndex(array, i, j):
    """Pomocna funkce pro razeni vyberem. Vrati index nejmensiho prvku
    v poli 'array' mezi 'i' a 'j'-1.
    """
    # TODO
    pass


# TODO: dopsat tuto funkci
def select_sort(array):
    """Seradte pole 'array' pomoci razeni vyberem."""
    # TODO
    pass


# TODO: dopsat tuto funkci
def bucket_sort(array, maxElement):
    """Prihradkove razeni. Seradte pole 'array', pricemz vite, ze pole
    obsahuje pouze nezaporne hodnoty mensi nebo rovny 'maxElement'. Vstupni
    hodnoty nemusite upravovat do intervalu <0, 1), staci chytre vyuzit
    celociselne deleni hodnotou 'maxElement + 1' pri vkladani do bucketu.
    """
    # TODO
    pass


# Dale nasleduji kody potrebne k testum, needitujte je.

element_count = 10
max_element = 50


def new_random_array(size, maxElement=max_element):
    """Slouzi pro generovani noveho pole delky size."""
    result = []
    for i in range(size):
        result.append(random.randint(1, maxElement))
    return result


def is_sorted(array):
    """Overuje serazenost."""
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True


def run_quick_sort(array):
    quick_sort_in_place(array, 0, len(array)-1)


def run_merge_sort(array):
    aux = [0 for i in range(len(array))]
    merge_sort(array, aux, 0, len(array)-1)


def test_sort(sort):
    print("Test 1.: jednoprvkove pole [1]: ")
    array1 = [1]
    sort(array1)

    if array1[0] == 1 and is_sorted(array1):
        print("OK")
    else:
        print("NOK, puvodni pole bylo [1] a bylo serazeno,")
        print("po volani sortu je vystup: {}".format(array1[0]))

    print("Test 2.: dvouprvkove pole [1, 2]: ")
    array2 = [1, 2]
    sort(array2)

    if array2[0] == 1 and array2[1] == 2 and is_sorted(array2):
        print("OK")
    else:
        print("NOK, puvodni pole bylo [1, 2] a bylo serazeno,")
        print("po volani sortu je vystup: {}".format(array2))

    print("Test 3.: dvouprvkove pole [2, 1]: ")
    array3 = [2, 1]
    sort(array3)

    if array3[0] == 1 and array3[1] == 2 and is_sorted(array3):
        print("OK")
    else:
        print("NOK, puvodni pole bylo [2, 1],")
        print("po volani sortu je vystup: {}".format(array3))

    print("Test 4.: serazene pole 10 prvku [1..10]: ")
    array4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sort(array4)

    if is_sorted(array4):
        print("OK")
    else:
        print("NOK, puvodni pole bylo [1, 2..10],")
        print(" po volani sortu je vystup: {}".format(array4))

    print("Test 5.: neserazene pole: ")
    array5 = new_random_array(element_count)
    print("Puvodni pole: {}".format(array5))
    sort(array5)

    if is_sorted(array5):
        print("OK")
    else:
        print("NOK: po volani sortu je vystup: {}".format(array5))


def test_insert_sort():
    print("Testy na InsertSort:")
    test_sort(insert_sort)


def test_quick_sort():
    print("\nTesty na QuickSort:\n")
    test_sort(run_quick_sort)


def test_merge():
    print("\nTesty na Merge z MergeSortu:\n")
    aux = [0 for i in range(element_count)]

    print("Test 1.: Merge 2 jednoprvkovych stejnych poli [1] a [1]:")
    array1 = [1, 1]
    merge(array1, aux, 0, 0, 1)

    if array1[0] == 1 and array1[0] == 1:
        print("OK")
    else:
        print("NOK, puvodni pole bylo [1, 1],")
        print("po volani Merge je vystup: {}".format(array1))

    print("Test 2.: Merge 2 jednoprvkovych stejnych poli [1] a [2]:")
    array2 = [1, 2]
    merge(array2, aux, 0, 0, 1)

    if array2[0] == 1 and array2[1] == 2:
        print("OK")
    else:
        print("NOK, puvodni pole bylo [1, 2],")
        print("po volani Merge je vystup: {}".format(array2))

    print("Test 3.: dvouprvkove pole [2, 1]: ")
    array3 = [2, 1]
    merge(array3, aux, 0, 0, 1)

    if array3[0] == 1 and array3[1] == 2:
        print("OK")
    else:
        print("NOK, puvodni pole bylo [2, 1], vysledek mel byt [1, 2],")
        print("po volani Merge je vystup: {}".format(array3))

    print("Test 4.: desetiprvkove pole [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]:")
    array4 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    merge(array4, aux, 0, 4, 9)

    if is_sorted(array4):
        print("OK")
    else:
        print("NOK, vysledek mel byt [1..10],")
        print("po volani Merge je vystup: {}".format(array4))

    print("Test 5.: desetiprvkove pole [1, 1, 2, 2, 3, 1, 1, 2, 3, 3]:")
    array5 = [1, 1, 2, 2, 3, 1, 1, 2, 3, 3]
    merge(array5, aux, 0, 4, 9)

    if is_sorted(array5):
        print("OK")
    else:
        print("NOK, vysledek mel byt [1, 1, 1, 1, 2, 2, 2, 3, 3, 3],")
        print("po volani Merge je vystup: {}".format(array5))


def test_merge_sort():
    print("\nTesty na MergeSort:")
    test_sort(run_merge_sort)


def run_counting_sort(array):
    array[:] = counting_sort(array, 0, max_element)


def test_counting_sort():
    print("\nTesty na CountingSort:")
    test_sort(run_counting_sort)

    print("Test 6.: neserazene pole malo hodnot:")
    array = new_random_array(element_count, element_count//3)
    print("Puvodni pole: " + str(array))
    array = counting_sort(array, 0, element_count//3)

    if is_sorted(array):
        print("OK")
    else:
        print("NOK: po volani sortu je vystup: " + str(array))

    print("Test 7.: neserazene pole malo hodnot posunute:")
    array = new_random_array(element_count, element_count//3)
    for i in range(element_count):
        array[i] += 20

    print("Puvodni pole: {}".format(array))
    array = counting_sort(array, 20, 20+element_count//3)

    if is_sorted(array):
        print("OK")
    else:
        print("NOK: po volani sortu je vystup: " + str(array))


def test_select_sort():
    print("\nTesty na SelectSort:")
    test_sort(select_sort)


def run_bucket_sort(array):
    bucket_sort(array, max_element)


def test_bucket_sort():
    print("\nTesty na BucketSort:")
    test_sort(run_bucket_sort)

    print("Test 6.: neserazene pole malo hodnot:")
    array = new_random_array(element_count, element_count//3)
    print("Puvodni pole: {}".format(array))
    bucket_sort(array, element_count//3)

    if is_sorted(array):
        print("OK")
    else:
        print("NOK: po volani sortu je vystup: " + str(array))


if __name__ == '__main__':
    test_insert_sort()
    test_quick_sort()
    test_merge()
    test_merge_sort()
    test_counting_sort()
    # BONUS
    test_select_sort()
    test_bucket_sort()
