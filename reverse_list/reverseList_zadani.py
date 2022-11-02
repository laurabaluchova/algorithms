# Implementacni test IB002 - uloha 2. (12 bodov)
#
# Vasi ulohou v tomto prikladu je obratit poradi prvku v
# jednostranne zretezenem linearnim seznamu
# autor Karel Kubicek


class Element:
    value = None
    next = None
    prev = None


class ReverseList:
    list_beginning = None  # zacatek seznamu


# metoda getEnd vrati konec seznamu
# pomocna metoda pro vkladani do seznamu, pouziti ve vasi uloze je na vas
def getEnd(linked_list):
    if linked_list.list_beginning is None:
        return None
    tmp = linked_list.list_beginning
    while tmp.next is not None:
        tmp = tmp.next
    return tmp


# insert do klasickeho listu
# @param value hodnota, kterou vkladame
def insert(linked_list, value):
    new_one = Element()
    new_one.value = value
    if linked_list.list_beginning is None:
        linked_list.list_beginning = new_one
    else:
        list_end = getEnd(linked_list)
        list_end.next = new_one


# vypisy slouzici ke kontrole
# @param from pocatek vypisu
# @return
def toStringForward(begin):
    tmp = begin
    output = ""
    while tmp is not None:
        output = output + " " + str(tmp.value)
        tmp = tmp.next
    return output


# TODO: naimplementujte metodu revert
# pracujte se seznamem, na ktery mate ukazatele listBegining
# metoda ma za ukol obratit poradi prvku v seznamu
# metoda by nesmi vytvaret novy seznam, musi jen zmenit ukazatele v jiz existujicich objektech


def revert(linked_list):
    if linked_list.list_beginning is None:
        return None

    last_element = getEnd(linked_list)
    element = linked_list.list_beginning

    while element is not None:
        if element == last_element:
            element.next = element.prev
            element.prev = None
            linked_list.list_beginning = element
            return

        if element == linked_list.list_beginning:
            element.prev = element.next
            element.next = None

        else:
            original_next = element.next
            original_previous = element.prev
            element.prev = original_next
            element.next = original_previous

        element = element.prev










# Main
print("Testing:")
print("Test 1.:", end=" ")
r = ReverseList()

revert(r)
if r.list_beginning is None:
    print("OK")
else:
    print("Chyba pri praci s prazdnym listem")

print("Test 2.:", end=" ")
r = ReverseList()

tmpEnd = getEnd(r)

revert(r)
if r.list_beginning == tmpEnd:
    print("OK")
else:
    print("Chyba pri praci s listem s jednim prvkem")

for i in range(3, 11):
    r = ReverseList()

    for j in range(1, i):
        insert(r, j)

    tmpEnd = getEnd(r)

    print("Test " + str(i) + ".:", end=" ")
    revert(r)
    if tmpEnd == r.list_beginning:
        print("OK, ")
    else:
        print("Chyba, byvaly konec neni ted zacatek, vas novy zacatek je " + str(r.list_beginning.value))
        print("spravne to ma byt " + str(tmpEnd.value))

    currentElement = r.list_beginning
    for j in range(i - 1, 0):
        if currentElement.value != j:
            print("Chyba, spatne poradi: \n" + str(toStringForward(currentElement)))
            print("spravne maji byt sestupne cisla po 1 od " + str(j))
            break
        currentElement = currentElement.next
