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
    if (len(arr) < 3):
        # Kratky vstup, primo setridime.
        pass
        # TODO
    else:
        # Vstup moc dlouhy, budeme rozdelovat a panovat.
        # Nove zhruba stejne dlouhe podseznamy pro samostatne setrideni.
        A = [0] * (len(arr) / 2)
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
        # TODO


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
