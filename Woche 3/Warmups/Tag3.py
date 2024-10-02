"""
Schreibe eine Funktion, um den Median einer gegebenen Zahl zu finden. 
Verwenden Sie keine Bibliotheken wie Math oder Numpy. Berücksichtigen Sie, dass das Array nicht-numerische Werte enthalten könnte.

Beispiel:
[23, 34, 15] = 23
[1, 2, 3, 4] = 2.5

"""


def median(arr):
    for i in arr:
        if type(i) != int and type(i) != float:
            raise ValueError("Array contains non-numeric values")

    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        upper_bound = n // 2
        lower_bound = upper_bound - 1
        arr_upper = arr[upper_bound]
        arr_lower = arr[lower_bound]
        return (arr_upper + arr_lower) / 2
    else:
        return arr[n // 2]


print(median([23, 34, 15]) == 23)
print(median([1, 2, 3, 4]) == 2.5)
