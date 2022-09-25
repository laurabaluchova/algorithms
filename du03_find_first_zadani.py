# IB002 Extra domaci ukol 3.
#
# Vasi ulohou bude s vyuzitim principu binarniho vyhledavani implementovat
# dve metody, find_first_occurrence a find_first_greater. V obou pripadech
# musi casova slozitost vaseho algoritmu byt nejhure logaritmicka, tedy byt
# v O(log n). (Pozor, iterovani v poli ma linearni slozitost.)
#
# Ukol 1.
# Implementujte metodu find_first_occurrence, ktera vrati index prvniho
# vyskytu prvku key v serazenem poli numbers. Pokud se prvek v poli
# nevyskytuje, vrati -1.
#
# Priklady vstupu a vystupu:
# find_first_occurrence(2, [1, 2, 2, 2, 4]) -->  1
# find_first_occurrence(3, [1, 2, 4, 5])    --> -1

def find_first_occurrence(key, numbers):
    first_index = 0
    last_index = len(numbers) - 1
    first_occurrence_index = -1

    while first_index <= last_index:
        current_number_index = find_current_number_index(first_index, last_index)
        current_number = numbers[current_number_index]
        if current_number == key:
            first_occurrence_index = current_number_index
        if current_number < key:
            first_index = current_number_index + 1
        else:
            last_index = current_number_index - 1
    return first_occurrence_index


def find_current_number_index(first_index, last_index):
    length = (last_index - first_index) // 2
    current_number_index = first_index + length
    return current_number_index



def test_first_occurrence_single_element_existing():
    print("Test existing with single element:", end=" ")

    input_list = [1]
    key = 1

    index = find_first_occurrence(key, input_list)

    if index == 0:
        print("OK")
    else:
        print("FAIL", "Expected index: 0, Returned index: %i" % index)


def test_first_occurrence_single_element_nonexisting():
    print("Test non-existing with single element:", end=" ")

    input_list = [0]
    key = 1

    index = find_first_occurrence(key, input_list)

    if index == -1:
        print("OK")
    else:
        print("FAIL", "Expected index: -1, Returned index: %i" % index)


def test_first_occurrence_multiple_elements_existing():
    print("Test existing with multiple elements:", end=" ")

    input_list = [1, 2, 2, 2, 3, 6]
    key = 3

    index = find_first_occurrence(key, input_list)

    if index == 4:
        print("OK")
    else:
        print("FAIL", "Expected index: 4, Returned index: %i" % index)


def test_first_occurrence_multiple_repeated_elements_existing():
    print("Test existing with multiple repeated elements:", end=" ")

    input_list = [2, 2, 2, 2, 2]
    key = 2

    index = find_first_occurrence(key, input_list)

    if index == 0:
        print("OK")
    else:
        print("FAIL", "Expected index: 0, Returned index: %i" % index)


"""
test_first_occurrence_single_element_existing()
test_first_occurrence_single_element_nonexisting()
test_first_occurrence_multiple_elements_existing()
test_first_occurrence_multiple_repeated_elements_existing()
"""


# Ukol 2.
# Implementujte metodu find_first_greater modifikaci predchozi metody
# find_first_occurrence tak, ze find_first_greater vrati index prvniho prvku
# v poli vetsiho nez key. Neni-li v poli zadny takovy, vrati -1.
#
# Priklady vstupu a vystupu:
# find_first_greater(2, [1, 2, 4, 5]) -->  2
# find_first_greater(3, [1, 2, 4, 5]) -->  2
# find_first_greater(3, [1, 2, 3])    --> -1


def find_first_greater(key, numbers):
    first_index = 0
    last_index = len(numbers) - 1
    first_greater_index = -1

    while first_index <= last_index:
        current_number_index = find_current_number_index(first_index, last_index)
        current_number = numbers[current_number_index]

        if current_number <= key:
            first_index = current_number_index + 1
        else:
            first_greater_index = current_number_index
            last_index = current_number_index - 1
    return first_greater_index


def test_first_greater_single_element():
    print("Test non-existing greater with single element:", end=" ")

    input_list = [0]
    key = 1

    index = find_first_greater(key, input_list)

    if index == -1:
        print("OK")
    else:
        print("FAIL", "Expected index: %i, Returned index: %i" % -1, index)


def test_first_greater_multiple_repeated_elements():
    print("Test first greater with multiple repeated elements:", end=" ")

    input_list = [2, 2, 2, 2, 2]
    key = 2

    index = find_first_greater(key, input_list)

    if index == -1:
        print("OK")
    else:
        print("FAIL", "Expected index: -1, Returned index: %i" % index)

def test_first_greater_existing_left():
    print("Test greater existing left:", end=" ")

    input_list = [1, 2, 2, 2, 3, 6]
    key = 3

    index = find_first_greater(key, input_list)

    if index == 5:
        print("OK")
    else:
        print("FAIL", "Expected index: 5, Returned index: %i" % index)


def test_first_greater_existing_right():
    print("Test greater existing right:", end=" ")

    input_list = [1, 2, 2, 2, 3, 6]
    key = 0

    index = find_first_greater(key, input_list)

    if index == 0:
        print("OK")
    else:
        print("FAIL", "Expected index: 0, Returned index: %i" % index)


def test_first_greater_existing_middle():
    print("Test greater existing middle:", end=" ")

    input_list = [1, 2, 3, 4, 5, 6, 7]
    key = 3

    index = find_first_greater(key, input_list)

    if index == 3:
        print("OK")
    else:
        print("FAIL", "Expected index: 3, Returned index: %i" % index)


test_first_greater_single_element()
test_first_greater_multiple_repeated_elements()
test_first_greater_existing_left()
test_first_greater_existing_right()
test_first_greater_existing_middle()