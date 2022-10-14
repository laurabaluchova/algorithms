#!/usr/bin/python3


###########################
# Dotaz studenta:
#
#
###########################

# Chcete-li dostat odpoved, vlozte do nazvu souboru heslo KONTROLA.


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


# Ukol 1.
# Vasim prvnim ukolem je implementovat funkci isCanonicalHeap(heap), ktera
# overi, zda je zadana halda 'heap' v kanonickem tvaru. Pokud ano, vrati True,
# v opacnem pripade vrati False.
#
# Prazdna nebo jednoprvkova halda je v kanonickem tvaru implicitne. Mejte na
# pameti, ze halda v kanonickem tvaru musi splnovat take pozadavky kladene na
# minimovou haldu.

def isCanonicalHeap(heap):
    pass
    # TODO


# Ukol 2.
# Druhym ukolem je implementovat funkci canoniseHeap(heap), ktera zadanou
# minimovou haldu 'heap' prevede na kanonicky tvar. Funkce bude menit primo
# haldu zadanou v argumentu, proto nebude vracet zadnou navratovou hodnotu.
#
# Snazte se neprovadet zbytecne operace a nezapomente, ze kanonicka halda je
# stale minimovou haldou. Pripady, kdy zadana halda neni minimova,
# osetrovat nemusite.

def canoniseHeap(heap):
    pass
    # TODO
