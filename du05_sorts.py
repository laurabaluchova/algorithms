# Ukol 1.
# Implementujte metodu is_odd, ktera vraci true, pokud je vstup liche cislo,
# jinak vraci false.

def is_odd(value):
    return value % 2 != 0


# Ukol 2.
# Implementujte metodu odd_sort_array, ktera setridi vstupni sekvenci cisel
# tak, ze licha cisla (nikoliv liche pozice v sekvenci) budou tvorit
# neklesajici posloupnost a ze suda cisla zustanou nehnute na svych pozicich.
#
# Pouzijte predpripravene reseni postavene na algoritmu MergeSort. Je hotovo
# deleni vstupu na dve pulky rozkopirovanim (takze algoritmus neni "in situ").
# Vasim ukolem je dopsat chybejici casti kodu. Casova slozitost hotoveho
# algoritmu musi byt v O(n.log(n)) vzhledem k delce vstupu.
#
# Reseni typu vykopirovani lichych cisel stranou, jejich samostatne serazeni
# a nasledne vlozeni zpet do puvodniho pole nevyhovuje predchystanemu reseni,
# proto je pro ucely tohoto ukolu explicitne zapovezeno.
#
# odd_sort_array([5,4,3,2,1,6,8]) pretransformuje pole na: [1,4,3,2,5,6,8]
#

def odd_sort_array(arr):
    if len(arr) < 3:
        if len(arr) > 1 and is_odd(arr[0]) and is_odd(arr[1]):
            if arr[0] > arr[1]:
                arr[0], arr[1] = arr[1], arr[0]

    else:
        # Vstup moc dlouhy, budeme rozdelovat a panovat.
        # Nove zhruba stejne dlouhe podseznamy pro samostatne setrideni.
        A = [0] * (len(arr) // 2)
        B = [0] * (len(arr) - len(A))
        # Rozdeleni: rozkopirovani
        d = 0
        while (d < len(A)):
                    A[d] = arr[d]
                    d += 1
        while (d < len(arr)):
                    B[d-len(A)] = arr[d]
                    d += 1
        # Rekurze
        odd_sort_array(A)
        odd_sort_array(B)
        # Panovani: Mergovani, tj. kopirovani zpet

    def odd_merge(array, left, mid, right):

        left_to_compare = left
        right_to_compare = mid + 1
        array_index = left

        for i in range(left, right + 1):
            aux[i] = array[i]

        for j in range(left, right + 1):

           if left_to_compare > mid:
                array[array_index] = aux[right_to_compare]
                right_to_compare += 1
                array_index += 1

            elif right_to_compare > right:
                array[array_index] = aux[left_to_compare]
                left_to_compare += 1
                array_index += 1

            elif aux[right_to_compare] < aux[left_to_compare]:
                array[array_index] = aux[right_to_compare]
                right_to_compare += 1
                array_index += 1

            else:
                array[array_index] = aux[left_to_compare]
                left_to_compare += 1
                array_index += 1


print(odd_sort_array([5, 4, 3, 2, 1, 6, 8]))

# Ukol 3.
# Implementujte metodu sort_array, ktera setridi vstupni sekvenci cisel tak,
# ze suda cisla budou tvorit nerostouci posloupnost (od nejvetsiho po nejmensi)
# a licha cisla budou tvorit neklesajici posloupnost.
# Zase zachovame pozice sudych a lichych, tj. sude cislo muze byt jen na
# pozici, kde bylo sude, a liche, kde bylo liche.
#
# sort_array([5,4,3,2,1,6,8]) pretransformuje pole na: [1,8,3,6,5,4,2]
# sort_array([1,2,3,4,6,5,8]) pretransformuje pole na: [1,8,3,6,4,5,2]
#
# Hint: Podobne jako druhy ukol, nemyslite?

def sort_array(array):
    pass
    # TODO


# Ukol 4.
# Implementujte metodu sort_list, ktera setridi oboustranne zretezeny
# seznam vzestupne.
# Reprezentaci oboustranne zretezeneho seznamu muzete prevzit ze
# zakladniho domaciho ukolu c. 1.
#
# Poznamka: Je zakazano pretransformovat seznam na pole, ktere pouze seradite
# a opet zmenite na seznam. Tento ukol je zamereny na praci se seznamem,
# ne s polem.


def sort_list(linkedList):
    pass
    # TODO
