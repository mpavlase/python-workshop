# Domácí úkoly ke srazu Python 1.4

1. Napiš funkci `power_of_two`, která pro argumentem zadané číslo `n` 
vytvoří a vrátí slovník, kde jako klíče budou čísla od jedné do `n` 
a jako hodnoty k nim jejich druhé mocniny.

    Například: `power_of_two(4)` vrátí `{1: 1, 2: 4, 3: 9, 4: 16}`

1. Napiš funkci `swap`, která vrátí slovník, který má hodnoty na místě klíčů a naopak.

    Například:
    ```python
    >>> input_dict = {'name': 'Karel', 'pet': 'guinea pig', 'age': 99}
    >>> output_dict = swap(input_dict)
    >>> print(output_dict)
    {'karel': 'name', 'guinea pig': 'pet', 99: 'age'}
    ```

1. Napiš funkci `freq_analysis`, která jako argument dostane řetězec 
a vrátí slovník, ve kterém budou jako klíče jednotlivé znaky ze 
zadaného řetězce a jako hodnoty počty výskytů těchto znaků v řetězci. 

    Například: `freq_analysis("hello world")` vrátí
    `{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}`



https://projekty.pyladies.cz/session?course=pyladies-2020-brno-podzim-pondeli&session=file
