# python 1.5 - domácí úkoly

1. Napiš funkci `add_padding`, která přečte celý soubor daný prvním argumentem
   a zapíše do souboru daný druhým argumentem (vytvoří nový, pokud je potřeba),
   původní obsah s tím, že bude odsazen o řetězec `>`.
    ```python
    >>> add_padding('zen.txt', 'zen-padded.txt')
    ```

    Soubor `zen.txt`
    ```
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    ```

    Vyvtořený soubor `zen-padded.txt`
    ```
    > Beautiful is better than ugly.
    > Explicit is better than implicit.
    > Simple is better than complex.
    > Complex is better than complicated.
    > Flat is better than nested.
    ```