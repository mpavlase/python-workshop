# Domácí úkoly ke srazu Python 1.3

**Úkoly řeš postupně**

Poznámky:
- rozměry obrázků jsou libovolné (jde o tvar, ne měřítko)

## řetězce
1. napiš funkci `crop_first_last`, která vrátí vstupní řetězec bez prvního a posledního znaku.
Dej si pozor na případy, kdy je vstup příliš krátký (např. `'a'`). V takovém případě musí vracet prázdný řetězec.

   Ukázka vstupů a výstupů:
   ```python
   >>> crop_first_last('tonda')
   'ond'
   >>> crop_first_last(' tonda ')
   'tonda'
   >>> crop_first_last('')
   ''
   ```

1. napiš funkci `make_first_big`, která vrátí (sama nic nevypisuje) řetězec s prvním znakem převedeným do velké abecedy.

   Ukázka vstupů a výstupů:
   ```python
   >>> make_first_big('tonda')
   'Tonda'
   >>> make_first_big('TONDA')
   'Tonda'
   >>> make_first_big(' tonda')
   ' tonda'
   >>> make_first_big('24. prosince')
   '24. prosince'
   ```

1. napiš funkci `align_examples(input_str, width)`, která vypíše různé zarovnání textu (vlevo, doprostřed, vpravo) a každý řádek obalí mezi znaky `_`.
   
   Ukázka vstupů a výstupů:
   ```python
   >>> align_examples('pes', 7)
   _pes    _
   _  pes  _
   _    pes_
   ```

1. napiš funkci `replace_char_list(input_str, position, replacement)`, která nahradí znak určený pozicí za jiný a vrátí ho jako nový řetězec
   
   > Použij k tomu operace nad datovým typem `list`
   
   Ukázka vstupů a výstupů:
   ```python
   >>> replaced = replace_char_list('chlup', 3, 'a')
   >>> print(replaced)
   'chlap'
   ```

1. napiš funkci `replace_char_str(input_str, position, replacement)`, která nahradí znak určený pozicí za jiný a vrátí ho jako nový řetězec
   
   > Použij k tomu operace nad datovým typem `str`
   
   Ukázka vstupů a výstupů:
   ```python
   >>> replaced = replace_char_str('chlup', 3, 'a')
   >>> print(replaced)
   'chlap'
   ```
