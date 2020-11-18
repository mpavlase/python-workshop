# Podmínky - domácí úkoly


1. Napiš program `tajemstvi.py`, který po zadání správného hesla vypíše nějakou tajnou informaci.

   > Vhodné tajemství je třeba: *V pátek jsem viděl černého havrana.*

1. Napiš program `rychlost.py`, který ti podle zadané rychlosti řekne, na kterém typu vozovky
   můžeš takto jezdit.

   Limity:

        50 km/h - v obci
        90 km/h - mimo obec
       110 km/h - silnice pro motorová vozidla
       130 km/h - dálnice

   Ukázka:

       Zadej rychlost: 53
       Takto se jezdí mimo obec.

1. Ulož si následující program jako `nahoda.py` a spusť ho několikrát za sebou.
   Co dělá?

       from random import randrange
       cislo = randrange(3)
       print(cislo)

1. Vytvoř program `tvar.py`, který dělá následující:

    Vybere náhodné číslo ze tří možností (0, 1, nebo 2). (Koukni na předchozí úkol!)

    * Je-li číslo 0:
      * do proměnné `tvar` uloží slovo 'trojúhelník';
    * jinak, je-li číslo 1:
      * do proměnné `tvar` uloží slovo 'čtverec';
    * jinak:
      * do proměnné `tvar` uloží slovo 'kolečko'.
    * Vypíše `tvar`.

1. Vytvoř hru *Kámen nůžky papír* (`kamen.py`), která funguje následovně:
   * Do proměnné `tah_pocitace` dá náhodně slovo 'kámen', 'nůžky' nebo 'papír'. (Koukni na předchozí úkol!)
   * Zeptá se uživatele na tah; výsledek uloží do proměnné tah_hrace
   * Je-li tah hráče `kámen`:
     * je-li tah počítače `kámen`:
       * vypíše `Remíza!`;
     * jinak, je-li tah počítače `nůžky`:
       * vypíše `Vyhrál jsi!`;
     * jinak, je-li tah počítače `papír`:
       * vypíše `Prohrál jsi!`.
   * Jinak, je-li tah hráče `nůžky`:
     * je-li tah počítače `kámen`:
       * vypíše `Prohrál jsi!`;
     * jinak, je-li tah počítače `nůžky`:
       * vypíše `Remíza!`;
     * jinak, je-li tah počítače `papír`:
       * vypíše `Vyhrál jsi!`.
   * Jinak, je-li tah hráče `papír`:
     * je-li tah počítače `kámen`:
       * vypíše `Vyhrála jsi!`;
     * jinak, je-li tah počítače `nůžky`:
       * vypíše `Prohrála jsi!`;
     * jinak, je-li tah počítače `papír`:
       * vypíše `Remíza!`.
   * Jinak,
     * Omluví se (*vypíše hlášku*), že zná jen tři slova: kámen, nůžky a papír.
