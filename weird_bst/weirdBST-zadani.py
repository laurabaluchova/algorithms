# -*- coding: utf-8 -*-

'''
Vasou ulohou je implementovat specificku variantu binarneho vyhladavacieho
stromu nazvanu Weird Binary Search Tree, podporujucu operacie insert, search
a deactivate (zodpoveda operacii delete). Tato datova struktura sa okrem
specifikacie jednotlivych operacii lisi premennou 'active', ktora sa pouziva
namiesto mazania uzlov. V kazdom okamihu je v takomto strome najviac jeden
uzol s akymkolvek danym klucom. Vasou ulohou je implementovat operacie
search a deactivate.

Operacia insert funguje podobne ako u bezneho binarneho vyhladavacieho
stromu (BST) a mate k dispozicii jej uplnu a spravnu implementaciu. Mozete
predpokladat, ze vysledkom akejkolvek postupnosti operacii insert je
korektny BST, t.j. ak 'node' je uzol s klucom 'key', tak vsetky kluce v
podstrome s korenom node->left maju kluce ostro mensie ako 'key' a obdobne
pre pravy podstrom.

Operacia search ma vratit uzol s danym klucom 'key', ak sa taky uzol
nachadza v strome, rovnako ako u bezneho BST. Pritom nezalezi na tom, ci je
dany uzol aktivny, alebo nie. Ak vsak uzol s danym klucom 'key' neexistuje,
search vrati uzol s klucom 'k', kde 'k' je najvacsi kluc ostro mensi ako
'key' nachadzajuci sa v strome, taktiez bez ohladu na to ci je uzol s klucom
'k' aktivny, alebo nie.

Operacia deactivate ma najst uzol s danym klucom 'key'. Ak taky uzol
existuje, treba nastavit jeho premennu 'active' na hodnotu false bez ohladu
na to, ci bola jej predchadzajuca hodnota true alebo false. Ak uzol s klucom
'key' neexistuje, treba najst uzol s klucom 'k', kde 'k' je najmensi kluc
ostro vacsi ako 'key' nachadzajuci sa v strome a nastavit premennu 'active'
tohto uzla na false bez ohladu na to, ci predtym bola true alebo false.

Poznamka 1: Takato specifikacia operacie deactivate znamena, ze nemusite
presuvat casti stromu pod 'zmazanym' uzlom.

Poznamka 2: Pozor, operacie search a deactivate za urcitych okolnosti mozu
vratit None.

Poznamka 3: Vase riesenie musi byt zalozene na prechadzani stromu a nemoze
skusat hladat vacsie, resp. mensie prvky ako dany kluc.
'''


class Node:
    def __init__(self): 
        self.key = 0
        self.active = True   
        self.parent = None
        self.left = None
        self.right = None


class WeirdBST:
    def __init__(self): 
        self.root = None

'''
Funkcia vklada kluc do WeirdBST podla specifikacie; funkcia je korektna a nesmiete ju menit.
    
Vstup:
@param tree: 	WeirdBST strom
@param key: 	kluc ktory sa ma do stromu vlozit
'''
def insert(tree, key):
    tmp = None
    tmpRoot = tree.root
    while (tmpRoot != None):
        if (key == tmpRoot.key):
            tmpRoot.active = True
            return
        tmp = tmpRoot
        if (key < tmpRoot.key):
            tmpRoot = tmpRoot.left
        else:
            tmpRoot = tmpRoot.right

    node = Node()
    node.key = key
    node.parent = tmp
    if (tmp == None): # tree.root == None
        tree.root = node
    else:
        if (node.key < tmp.key):
            tmp.left = node
        else:
            tmp.right = node


'''
Funkcia vyhlada uzol s danym klucom. Ak sa taky kluc v strome nevyskytuje,
vyhlada uzol s klucom 'k', kde 'k' je najvacsi z klucov mensich nez 'key'
nachadzajucich sa v strome.
    
Vstup:  
@param tree: 	WeirdBST strom, v ktorom ma prebehnut vyhladavanie
@param key: 	kluc ktory sa ma vyhladat
    
Vystup:  
@return najdeny uzol zodpovedajuci specifikacii WeirdBST
'''

def search(tree, key):
    return search_recursive(key, tree.root, None)


def search_recursive(key, node, predecessor):
    if node is None:
        return predecessor

    if node.key == key:
        return node

    if node.key > key:
        return search_recursive(key, node.left, predecessor)

    predecessor = node
    return search_recursive(key, node.right, predecessor)


'''
Funkcia vyhlada uzol s danym klucom a deaktivuje ho.
Ak sa taky kluc v strome nevyskytuje, vyhlada uzol s klucom 'k', kde 'k' je najmensi
z klucov vacsich nez 'key' nachadzajucich sa v strome a deaktivuje tento uzol.
 
Vstup:  
@param tree: 	WeirdBST v ktorom ma prebehnut deaktivacia
@param key: 	kluc ktory sa ma deaktivovat
 
Vystup:  
@return deaktivovany uzol zodpovedajuci specifikacii WeirdBST
'''


def deactivate(tree, key):
    node_to_deactivate = search_with_equivalent_successor(key, tree.root, None)
    if node_to_deactivate is not None:
        node_to_deactivate.active = False
    return node_to_deactivate


def search_with_equivalent_successor(key, node, successor):
    if node is None:
        return successor

    if node.key == key:
        return node

    if node.key > key:
        successor = node
        return search_with_equivalent_successor(key, node.left, successor)

    return search_with_equivalent_successor(key, node.right, successor)

        
'''
Testovanie ma tri fazy: najprv su Vase funkcie testovane na prazdnom
strome, potom na strome obsahujucom prave jeden uzol, a nakoniec na
uplnom strome vyobrazenom na v 'graph.jpg' (pozor na to, ze sa jedna o
BST a teda kazdy potomok je bud vlavo, alebo vpravo od rodica v
zavislosti od kluca).
'''

print ("Testing weird binary search tree.")

wbst = WeirdBST()

print ("Testing search and deactivate on an empty tree.")

if (search(wbst, 4) == None):
    print ("Correct search of 4.")
else:
    print ("Search of 4 failed.")

if (deactivate(wbst, 14) == None):
	print ("Correct deactivation of 14.")
else:
	print ("Deactivation of 14 failed.")


print ("")
print ("Testing search and deactivate on a tree with only one node; the key of the root is 12.")

insert(wbst,12)

result = search(wbst, 12)
if (result != None and result.key == 12):
    print ("Correct search of 12.")
else:
    print ("Search of 12 failed.")

result = search(wbst, 11)
if (result == None):
    print ("Correct search of 11.")
else:
    print ("Search of 11 failed.")

result = search(wbst, 13)
if (result != None and result.key == 12):
    print ("Correct search of 13.")
else:
    print ("Search of 13 failed.")


result = deactivate(wbst, 12)
if (result != None and result.key == 12 and result.active == False):
    print ("Correct deactivation of 12.")
else:
    print ("Deactivation of 12 failed.")

insert(wbst,12) #Sets 12.active to True

result = deactivate(wbst, 11)
if (result != None and result.key == 12 and result.active == False):
    print ("Correct deactivation of 11.")
else:
    print ("Deactivation of 11 failed.")

result = deactivate(wbst, 13)
if (result == None):
    print ("Correct deactivation of 13.")
else:
    print ("Deactivation of 13 failed.")

print ("")
print ("Testing search and deactivate on the full tree.")

insert(wbst,12) #Sets 12.active to True
insert(wbst,8)
insert(wbst,19)
insert(wbst,5)
insert(wbst,10)
insert(wbst,14)
insert(wbst,20)
insert(wbst,16)
insert(wbst,9)
insert(wbst,11)

result = search(wbst, 12)
if (result != None and result.key == 12):
    print ("Correct search of 12.")
else:
    print ("Search of 12 failed.")

result = search(wbst, 14)
if (result != None and result.key == 14):
    print ("Correct search of 14.")
else:
    print ("Search of 14 failed.")

result = search(wbst, 16)
if (result != None and result.key == 16):
    print ("Correct search of 16.")
else:
    print ("Search of 16 failed.")

result = search(wbst, 15)
if (result != None and result.key == 14):
    print ("Correct search of 15.")
else:
    print ("Search of 15 failed.")

result = search(wbst, 13)
if (result != None and result.key == 12):
    print ("Correct search of 13.")
else:
    print ("Search of 13 failed.")

result = search(wbst, 4)
if (result == None):
    print ("Correct search of 4.")
else:
    print ("Search of 4 failed.")

result = search(wbst, 7)
if (result != None and result.key == 5):
    print ("Correct search of 7.")
else:
    print ("Search of 7 failed.")


result = deactivate(wbst, 12)
if (result != None and result.key == 12 and result.active == False):
    print ("Correct deactivation of 12.")
else:
    print ("Deactivation of 12 failed.")

result = deactivate(wbst, 19)
if (result != None and result.key == 19 and result.active == False):
    print ("Correct deactivation of 19.")
else:
    print( "Deactivation of 19 failed.")

result = deactivate(wbst, 20)
if (result != None and result.key == 20 and result.active == False):
    print ("Correct deactivation of 20.")
else:
    print ("Deactivation of 20 failed.")

result = deactivate(wbst, 13)
if (result != None and result.key == 14 and result.active == False):
    print ("Correct deactivation of 13.")
else:
    print ("Deactivation of 13 failed.")

result = deactivate(wbst, 15)
if (result != None and result.key == 16 and result.active == False):
    print ("Correct deactivation of 15.")
else:
    print ("Deactivation of 15 failed.")

result = deactivate(wbst, 17)
if (result != None and result.key == 19 and result.active == False):
    print ("Correct deactivation of 17.")
else:
    print ("Deactivation of 17 failed.")

result = deactivate(wbst, 21)
if (result == None):
    print ("Correct deactivation of 21.")
else:
    print ("Deactivation of 21 failed.")




