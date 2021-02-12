# Domácí úkoly ke srazu Python 2.1

Všechny úkoly si zkoušej z příkazové řádky Windows (`cmd`)

1. Vyzkoušej si instalaci a odinstalování balíčku.
   1. vytvoř si nové virtuální prostředí z příkazové řádky
   1. aktivuj ho
   1. podívej se (vypiš), které balíčky máš nainstalované, např. pomocí příkazu `list` (od příkazu `pip`)
   1. nainstaluj si balíček `requests`
   1. znovu si vypiš nainstalované balíčky
   1. odinstaluj balíček `requests`
   1. ještě jednou si vypiš nainstalované balíčky.

   Jak vypadá poslední výstup? Ve kterém místě tohoto úkolu jsi už podobný viděl/a dříve? Nakonec terminál uzavři (nebo deaktivuj virtuální prostředí).

1. Vyzkoušej si přejmenovat virtuální prostředí
   1. vytvoř si nové virtuální prostředí z příkazové řádky, pojmenuj ho třeba `venv-2`
   1. aktivuj ho
   1. nainstaluj si balíček `requests`
   1. ověř si, že ho používáš z virtuálního prostředí. Spusť si `python` a naimportuj si jej:
      ```python
      >>> import requests
      >>> requests
      <module 'requests' from '...\venv-2\lib\site-packages\requests\__init__.py'>
      ```
   1. ukonči interpret python (třeba pomocí `exit()`), deaktivuj si virtuální prostředí (`deactivate`)
   1. přejmenuj složku `venv-2` na `venv-2-renamed`
   1. aktivuj si toto (přejmenované) virtuální prostředí znova
   1. vyzkoušej si znova krok **iv.**. Bude fungovat? Pokud ano, dostaneš stejný výstup (cestu k naimportovanému modulu)?
   