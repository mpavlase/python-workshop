# Domácí úkoly ke srazu Python 1.2

**Úkoly řeš postupně**

Poznámky:
- rozměry obrázků jsou libovolné (jde o tvar, ne měřítko)
- že na obrázcích dole není vidět želva/šipka není podstatné

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

1. Pomocí cyklů `for` a parametru `end` pro `print` napiš program, který postupně z jednotlivých `X` vypíše:

   ```
    X X X X X
    X X X X X
    X X X X X
    X X X X X
    X X X X X
    ```
   > „Z jednotlivých `X`“ znamená, že každý print vypíše maximálně jedno `X`. Nepoužiješ tedy např. `print('X X X X X')` ani `print('X ' * 5)`.

   Pokus se vymyslet smysluplné názvy pro proměnné v rámci konstrukce `for <meaningful name> in ...` i přesto, že bys je nevyužil/a. Jak pojmenuješ proměnnou cyklu? A tu druhou?

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


Reference:
- většina úloh byla převzata z https://projekty.pyladies.cz/session?course=pyladies-2019-brno-jaro-monday&session=cycles
