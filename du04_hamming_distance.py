# IB002 Extra domaci ukol 4.
#
# Hammingovu vzdalenost dvou stejne dlouhych binarnich retezcu
# definujeme jako pocet bitu, ve kterych se retezce lisi.
#
# Vasim ukolem je implementovat metodu hamming_distance,
# ktera pro binarni retezec b a nezaporne cislo k vrati vsechny
# binarni retezce, jejichz Hammingova vzdalenost od b bude prave k.
#
# Priklady chovani:
# hamming_distance('100', 0) vrati vystup: ['100']
# hamming_distance('0001', 2) vrati vystup:
#         ['1101', '1011', '1000', '0111', '0100', '0010']

def hamming_distance(binary_string, distance):
    adjusted_strings = []
    return hamming_distance_recursive(binary_string, 0, 0, distance, adjusted_strings)


def hamming_distance_recursive(binary_string, left, changes, distance, results):
    if changes == distance:
        results.append(binary_string)

    else:
        for i in range(left, len(binary_string)):
            binary_string[i] = flip_binary_value(binary_string[i])
            hamming_distance_recursive(binary_string, i + 1, changes + 1, distance, results)
            binary_string[i] = flip_binary_value(binary_string[i])

    return results


def flip_binary_value(value):
    if value == "1":
        return "0"
    return "1"


tmp = '0001'.split()
result = hamming_distance(["0", "0", "0", "1"], 2)
print(result)