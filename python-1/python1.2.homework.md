# Domácí úkoly ke srazu Python 1.2

**Úkoly řeš postupně**

Poznámky:
- rozměry obrázků jsou libovolné (jde o tvar, ne měřítko)

## kreslení, funkce
1. napiš funkci `draw_square`, která pomocí `range` vykreslí čtverec
1. nakresli rovnostranný trojúhelník
   
   ![](https://projekty.pyladies.cz/static/tasks/handout3a_images/03_trojuhelnik.png)
1. nakresli domeček "jedním tahem"

   ![](https://projekty.pyladies.cz/static/tasks/handout3a_images/04_domecek.png)

1. nakresli vesnici

   ![](https://projekty.pyladies.cz/static/tasks/handout3a_images/05_vesnice.png)
1. nakresli tento ornament
   - nevíš-li si rady, vezmi pravítko a změř délky jednotlivých čar. Doporučuju začít od středu.
   
   ![](https://projekty.pyladies.cz/static/tasks/handout3a_images/10_ornament.png)
1. nakresli tento další ornament
   
   ![](https://projekty.pyladies.cz/static/tasks/handout3a_images/11_ornament.png)

1. nakresli spirálu

   ![](https://projekty.pyladies.cz/static/tasks/handout3a_images/12_spirala.png)

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

1. Pomocí cyklů `for` a parametru `end` pro `print` napiš program, který postupně z jednotlivých `X` vypíše:

   ```
    X X X X X
    X X X X X
    X X X X X
    X X X X X
    X X X X X
    ```
   > „Z jednotlivých `X`“ znamená, že každý print vypíše maximálně jedno `X`. Nepoužiješ tedy např. `print('X X X X X')` ani `print('X ' * 5)`.

   Jak pojmenuješ proměnnou cyklu? A tu druhou?

1. Pomocí cyklů `for` a příkazu `if` napiš program, který z jednotlivých `X` vypíše:
    ```
    X X X X X X
    X         X
    X         X
    X         X
    X         X
    X X X X X X
    ```

    > „Z jednotlivých `X`“ opět znamená, že každý `print` vypíše maximálně jedno `X`.
