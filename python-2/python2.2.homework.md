# Domácí úkoly ke srazu Python 2.2

Pro následující úlohy bude nutné si v dokumentaci dohledat i další funkce, než byly zmíněné na srazu.

- řešení si vyzkoušej pomcí Jupyter Notebooku
- záměrně místy neuvádím přesné kroky k řešení, ale spíš popis cíle kroku :-)
- úkoly řeš postupně, navazují na sebe.

1. Vyřeš následující soustavu lineárních rovnici pomocí `numpy`.
   ```
   2x + y = 7
   y - 3z = -9
   5z -x = 18
   ```

1. Načtení CSV pomocí numpy. Data pochází z CHMI (Český hydrometeorologický ústav) a popisují stav toku jedné řeky.
   1. Ulož si datový soubor [python2.2.homework.data.csv](python2.2.homework.data.csv) do stejného adresáře, odkud spouštíš Notebook
   1. Pomocí `np.loadtxt` načti obsah souboru z předchozího kroku. Soubor používá znak `;` jako **oddělovač** sloupců.
   1. Ověř si, že načtená sada obsahuje 182 řádků a 3 sloupce:
      - stav (výška hladiny) [cm]
      - průtok [m3s-1]
      - teplota [°C]
   1. Ulož si do do samostatných proměnných jednotlivé sloupce: `height`, `flow`, `temp`
   
1. Vykresli si samostatně jednotlivé datové řady
   1. Jako samostatné figure (1 graf na 1 buňku v notebooku)
   1. Zkus si je umístit do jednoho figure pomocí `plt.subplot` / `plt.subplots` - viz dokumentace

1. "proložení přímkou" (linear regression)
   1. Doinstaluj si balíček `scipy`
   1. V dokumentaci knihovny `scipy` si vyhledej funkci, která vypočítá koeficienty lineární regrese metodou nejmenších čtverců
   1. Jako zdroj dat použij datovou řadu `temp`
   1. Vykresli do jednoho grafu oba průběhy: `temp` a proloženou přímku. Výsledný obrázek pro srovnání je [zde](python2.2.homework.linreg.png).