# Domácí úlohy pro `str`

1. Napiš program, který v zadaném textu vymění všechny samohlásky za znak `_`.
    Použij k tomu vestavěné funkce v Pythonu.

    Vstup: `stromy stroj strycek straka`

    Výstup: `str_m_ str_j str_c_k str_k_`

2. Zkus si to samé zadání, ale tentokrát naprogramovat svépomoci.
   Projdi si vstupní text znak po znaku a postupně skládej výsledek.
   Obejdeš se k tomu bez funkce pro nahrazování znaků, kterou jsi použil/a v
   předchozí úloze.

   Vstup i výstup viz předchozí úloha

   [for, if in, .append]

1. Napiš funkci `get_csv_names`, která vrátí . CSV je textový formát, pro zápis dat, uspořádaných do tabulky.
    Používá znak čárky jako oddělovač sloupců.

    Například:

    ```
    jmeno,doprava,den-noc,patro
    Jiri,auto,sova,1
    Petr,kolo,ptace,4
    ```

    se dá vizualizovat takto:
    ```
    +-------+---------+---------+-------+
    | jmeno | doprava | den-noc | patro |
    +-------+---------+---------+-------+
    | Jiri  | auto    | sova    | 1     |
    +-------+---------+---------+-------+
    | Petr  | kolo    | ptace   | 4     |
    +-------+---------+---------+-------+
    ```

    Vstupní data pro domácí úlohu:
    ```python
    csv = """jmeno,doprava,den-noc
    Vlasta,auto,sova
    Petr,kolo,ptace
    Honza,mhd,ptace
    Jana,auto,ptace
    Vit,mhd,sova"""
    ```

    Výstup:
    ```
    Vlasta, Petr, Honza, Jana
    ```

1. Napiš funkci `get_histogram`, která ze vstupního textu z předchozího příkladu
    zjistěte histogram pro sloupec `doprava`.

    Výstup:

    ```
    doprava
    auto = 2
    kolo = 1
    mhd = 2
    ```

