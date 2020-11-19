# Domácí úkoly ke srazu Python 1.1

**Úkoly řeště postupně.**

1. Jakým příkazem se ukončuje příkazová řádka ve Windows (`cmd`)?
1. Jakým příkazem se ukončuje interpret pythonu (`python`)?
1. Jaká chyba nastane, když zkusíš podělit řetězec řetězcem?
1. Jaká chyba nastane, když zkusíš použít proměnnou předtím, než do ní něco přiřadíš?
1. Ne všechno se dá použít jako jméno proměnné. Fungují pro proměnné následující jména? (Vyzkoušej si to!) Pokud ne, proč asi?
    ```
    x
    button4
    34
    3e4
    krůta
    $i
    square-root
    readme.txt
    smallerSide
    NUMBER_OF_POINTS
    _ (podtržítko)
    π (pí)
    True
    _cache
    __name__
    while
    ```
1. Pomocí příkazové řádky (`cmd`) vytvoř novou složku `homework` ve složce `Dokumenty/python1/1`
1. Vytvořit následující dva programy ve složce `Dokumenty/python1/1/homework`:
    1. Vytvoř program `drink.py`, který se uživatele zeptá na věk a podle toho mu nabídne (=vypíše text) s vhodným nápojem. Pokud je věk menší než 18, vypíše `juice`, jinak vypíše `juice with "addition"`
    > Volání `input()` vrací vždy řetězec. Pro převod na celé číslo použij konstrukci `int(input())`. Toto jsme na srazu nestihli probrat.
    
    > Volání `print('prvni', promenna, 'treti')`, kde `promenna = 'druha', 
    1. Vytvoř program `repeat_name.py` postupně se zeptá uživatele na jméno, poté se zeptá na celé číslo a vypíše jeho jmé:
    ```
   Enter name:
   Lojza
   Enter number:
   4
   Hi Lojza from Python :-)
   Lojza! Lojza! Lojza! Lojza!
    ```
1. Založ si v PyCharmu dva různé spouštěče pro oba programy výše.
    1. Jeden pomocí pravého tlačítka myši,
    1. druhý pomocí šablony konfigurace `Python`
1. Použít tlačítko "Run" a "Debug" pro oba programy. Co se změnilo?
1. Nastavit zarážku (breakpoint) na řádek s podmínkou u programu `drink.py`
1. Znova si vyzkoušet krok 9. Co je jinak? Vyzkoušej si v debuggeru akce `Step over` (i několikrát `Step over` po sobě), `Resume program`, `Stop`
1. Odstraň všechny breakpointy ze souboru `drink.py` a vlož komentář na libovolný řádek. Spusť tento soubor pomocí debuggeru. Co se stane?
1. Napiš program `spend-day.py`, který se uživatele se zeptá, jaký je den v týdnu a podle toho doporučí aktivitu.
    > Pokud znáte z jiných jazyků konstrukci typu `switch`, kterou byste zde využili, tak Python ji přímo nemá. O ekvivalentní konstrukci vás odkážu na [tento článek](https://naucse.python.cz/course/pyladies/beginners/and-or/)
    - Je li `Monday`, nebo `Tuesday`, nebo `Wednesday`, nebo `Thursday`, nebo `Friday`, napíše `Get up and go work`.
    - Je li `Saturday`, zeptá se ho počasí.
      - Je-li počasí `sunny`, napíše `Go outdoors`.
      - Je-li počasí `rainy`, napíše `Practise Python`.
      - Jinak napíše `I have no preference for you today`.
    - Je-li `Sunday`, napíše `Just rest`.
    - Jinak napíše `I don't know (...) day`, kde za `(...)` doplňte uživatelem zadaný název dne.
