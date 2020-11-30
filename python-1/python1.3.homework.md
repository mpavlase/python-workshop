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

1. napiš funkci `make_first_big`, která vrátí řetězec s prvním znakem převedeným do velké abecedy.

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

