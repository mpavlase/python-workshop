# python 1.5 - domácí úkoly

**Poznámka**: Pokud ti nebude fungovat spuštění pythonu pomocí příkazu `python`, zkus použít `py`.

1. Napiš program `show_args.py`, který zobrazí argumenty z příkazové řádky.
   Je proto třeba to spouštět skutečně z příkazové řádky (typicky v `cmd`,
   či PowerShellu), v interaktivním pythonu toho tentokráte moc nezjistíš.

   Příklad:
   ```commandline
   > python show_args.py first second "so long text" 'single quoted text'
   - "first"
   - "second"
   - "so long text"
   - "single quoted text"
   ```

   Argumenty z příkazové řádky v pythonu dostaneš z `argv`,
   který si naimportuješ z modulu `sys` (např. `from sys import argv`).

   Začni jednoduše, jen se podívej, co ti vrátí `argv` a od toho pak
   pokračuj dál. Při seznamování si vyzkoušej přejmenovat celý soubor,
   například z `show_args.py` na `display_args.py` a sleduj, co se změnilo.

1. Napiš program `show_file.py`, který pouze zobrazí obsah souboru zadaný
   z příkazové řádky.
   Příklad užití:
   ```commandline
   > python show_file.py myfile.txt
   This is content
   of myfile.txt
   ```

1. Napiš funkci `add_padding`, kterou ulož do souboru `add_padding.py`,
   která přečte celý soubor daný prvním argumentem a zapíše do souboru 
   daný druhým argumentem (vytvoří nový, pokud je potřeba), původní obsah 
   s tím, že bude odsazen o řetězec `>`.

   Pro práci se soubory použij *context manager* (`with ...`).
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

1. Z předchozího souboru udělej spustitelný modul.
  
   Nachystej si následující adresářovou strukturu, kterout rozšiř tak, 
   aby se dal modul spustit (tečka označuje 
   aktuální adresář, ten se nevytváří):
   ```commandline
   .
   ├── padding
   │   └── add_padding.py
   └── zen.txt
   ```

   Příklad spouštění:
   ```commandline
   python -m padding zen.txt zen-padded.txt
   ```
