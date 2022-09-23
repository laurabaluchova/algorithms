import threading
import time
import sys
import math


sys.setrecursionlimit(6000)  # nastavi maximalni hloubku rekurze na 6000
threading.stack_size(200000000)

# Vasim ukolem bude naimplementovat ruzne verze algoritmu pro vypocet
# mocniny a pro vypocet fibonacciho cisel. Testy obsahuji mereni
# rychlosti, takze si pro ruzne casove tridy muzete udelat predstavu,
# jak dlouho bezi.
#
# Doba behu neni deterministicka - jednou muze vypocet probehnout
# rychle, podruhe pomalu. Proto jsou testy rychlosti nekolikrat
# opakovany a namereny cas neni dobou behu jednoho vypoctu.
# I tak je cas pouze orientacni.


def power_iterative(base, exp):
    """Funkce vypocita hodnotu base^exp pomoci iterativniho algoritmu
    v O(exp). Staci se omezit na prirozene hodnoty exp.
    """
    result = base

    for i in range(exp - 1):
        result = result * base
    return result

# TODO: dopsat implementaci
def power_bin_iterative(base, exp):
    """Funkce vypocita hodnotu base^exp pomoci iterativniho algoritmu
    v O(log(exp)). Staci se omezit na prirozene hodnoty exp.

    Vyuziva predpokladu, ze n lze rozlozit na soucet mocnin dvojky,
    takze a^n lze rozlozit na soucin ruznych a na mocninu 2,
    tedy a^(2^k). a^(2^k) = ((((a^2)^2)^2)...^2), kde je k pocet dvojek.
    """
    # TODO
    return -1


# TODO: dopsat implementaci
def power_recursive(base, exp):
    """Funkce vypocita hodnotu base^exp pomoci rekurzivniho algoritmu
    v O(exp). Staci se omezit na prirozene hodnoty exp.
    """
    if exp == 0:
        return 1
    return base * power_recursive(base, exp - 1)


# TODO: dopsat implementaci
def power_bin_recursive(base, exp):
    """Funkce vypocita hodnotu base^exp pomoci rekurzivniho algoritmu
    v O(log(exp)). Staci se omezit na prirozene hodnoty exp.
    """
    # TODO
    return -1


# TODO: dopsat implementaci
def power_real_numbers(base, exp):
    """Funkce vypocita hodnotu base^exp pomoci libovolneho algoritmu.
    Funkce musi fungovat na realne hodnoty exp. Muzete si dopsat pomocne
    funkce. Na interval exponentu (0, 1) muzete pouzit operator **,
    pokud vsak zkusite resit i tento interval, verte, ze se hodne
    priucite, je to narocne.
    """
    # TODO
    return -1


# TODO: dopsat implementaci
def fib_recursive(number):
    """Funkce vypocita number-te finonacciho cislo pomoci
    exponencialniho rekurzivniho algoritmu.
    0. fibonacciho cislo je 0, 1. je 1
    """
    if number < 2:
        return number
    return fib_recursive(number - 1) + fib_recursive(number - 2)


def fib_iter(number):
    """Funkce vypocita number-te finonacciho cislo pomoci linearniho
    iterativniho algoritmu.
    0. fibonacciho cislo je 0, 1. je 1
    """
    # TODO
    return -1


# Testy implmentace
def test_power():
    limit_of_tests = 2900

    print("0. Cas vestaveneho mocneni v Pythonu: ", end="")
    start = time.process_time()
    counter1 = 0
    for i in range(1, limit_of_tests):
        counter1 += 13 ** i
    end = time.process_time()
    print("{} s.".format(end - start))

    print("1. Cas iterativniho mocneni v O(exp): ", end="")
    start = time.process_time()
    counter2 = 0
    for i in range(1, limit_of_tests):
        counter2 += power_iterative(13, i)
    end = time.process_time()
    print("{} s.".format(end - start))
    if counter1 != counter2:
        print("Vase funkce power_iterative nedava stejny vystup jako **.")
        for i in range(10):
            print("7 ^ {} = {},".format(i, 7 ** i))
            print("vas vystup power_iterative je ", end="")
            print(power_iterative(7, i))
    else:
        print("Vysledek je OK.")

    print("\n2. Cas iterativniho mocneni v O(log(exp)): ", end="")
    start = time.process_time()
    counter3 = 0
    for i in range(1, limit_of_tests):
        counter3 += power_bin_iterative(13, i)
    end = time.process_time()
    print("{} s.".format(end - start))
    if counter1 != counter3:
        print("Vase funkce power_bin_iterative nedava stejny vystup jako **.")
        for i in range(10):
            print("7 ^ {} = {},".format(i, 7 ** i))
            print("vas vystup power_bin_iterative je ", end="")
            print(power_bin_iterative(7, i))
    else:
        print("Vysledek je OK.")

    print("\n3. Cas rekurzivniho mocneni v O(exp): ", end="")
    start = time.process_time()
    counter4 = 0
    for i in range(1, limit_of_tests):
        counter4 += power_recursive(13, i)
    end = time.process_time()
    print("{} s.".format(end - start))
    if counter1 != counter4:
        print("Vase funkce power_recursive nedava stejny vystup jako **.")
        for i in range(10):
            print("7 ^ {} = {},".format(i, 7 ** i))
            print("vas vystup power_recursive je ", end="")
            print(power_recursive(7, i))
    else:
        print("Vysledek je OK.")

    print("\n4. Cas rekurzivniho mocneni v O(log(exp)): ", end="")
    start = time.process_time()
    counter5 = 0
    for i in range(1, limit_of_tests):
        counter5 += power_bin_recursive(13, i)
    end = time.process_time()
    print("{} s.".format(end - start))
    if counter1 != counter5:
        print("Vase funkce power_bin_recursive nedava stejny vystup jako **.")
        for i in range(10):
            print("7 ^ {} = {},".format(i, 7 ** i))
            print("vas vystup power_bin_recursive je ", end="")
            print(power_bin_recursive(7, i))
    else:
        print("Vysledek je OK.")


def test_extended_power():
    print("\n5. Test power pro realna cisla zakladu (nemeri se cas).")
    ok = True
    for i in range(-10, 10):
        if abs(7.5 ** i - power_real_numbers(7.5, i)) > 0.1 * (7.5 ** i):
            print("vas vystup z power_real_numbers se lisi ", end="")
            print("od ** o vice nez 10 %")
            print("7.5 ^ {} = {},".format(i, 7.5 ** i))
            print("vas vystup power_real_numbers je ", end="")
            print(power_real_numbers(7.5, i))
            ok = False
    if ok:
        print("Vysledek je OK.")

    print("\n6. Test power pro realna cisla ", end="")
    print("(exponentu i zakladu, nemeri se cas).")
    ok = True
    for i in range(-10, 10):
        if (abs(7.5 ** (i+0.5) - power_real_numbers(7.5, (i+0.5))) >
                0.1 * (7.5 ** (i+0.5))):
            print("vas vystup z power_real_numbers se lisi ", end="")
            print("od ** o vice nez 10 %")
            print("7.5 ^ {} = {},".format(i+0.5, 7.5 ** (i+0.5)))
            print("vas vystup power_real_numbers je ", end="")
            print(power_real_numbers(7.5, (i+0.5)))
            ok = False
    if ok:
        print("Vysledek je OK.")


def test_fib():
    print("\n7. Cas vypoctu fibonacciho cisla 35 v O(2^n): ", end="")
    start = time.process_time()
    result = fib_recursive(35)
    end = time.process_time()
    print("{} s.".format(end - start))
    if result != 9227465:
        print("Vase funkce fib_recursive nepocita spravne.", end="")
        print("Nasleduji vysledky do 35:")
        for i in range(35):
            print("Fib i = {} = {}".format(i, fib_recursive(i)))
    else:
        print("Vysledek je OK.")

    print("\n8. Cas vypoctu fibonacciho cisla 350000 v O(n): ", end="")
    start = time.process_time()
    fib_iter(350000)
    end = time.process_time()
    print("{} s.".format(end - start))
    if fib_iter(35) != 9227465:
        print("Vase funkce fib_iter nepocita spravne.", end="")
        print("Nasleduji vysledky do 35:")
        for i in range(35):
            print("Fib i = {} = {}".format(i, fib_iter(i)))
    else:
        print("Vysledek je OK.")


def fact(number, result):
    if number == 1:
        return result
    final_result = fact(number - 1, result * number)
    return final_result

if __name__ == '__main__':
    # result = fact(3, 1)
    test_power()
    test_extended_power()
    test_fib()
