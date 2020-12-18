## Python 1

Domácí příprava
- instalace aplikací Python a PyCharm

> Obsah níže je spíš rámcový, může se ještě v čase lehce měnit.

### (Sraz 1.0) - Úvod, aneb proč by mě to mělo všechno vlastně zajímat
- [celý obsah najdete zde](python1.0-intro.md)


### Sraz 1.1
- cmd, PyCharm (úvod)
- přiřazení, int, float, str (bez indexace)
- bool, if, logické operátory
- switch
- 📚 materiály: 
  * https://naucse.python.cz/course/pyladies/beginners/first-steps/
  * https://naucse.python.cz/course/pyladies/beginners/cmdline/
  * [PyCharm intro](../topics/pycharm-intro/README.md) (setup project, run configuration)
  * https://naucse.python.cz/course/pyladies/beginners/print/
  * https://naucse.python.cz/course/pyladies/beginners/variables/
  * https://naucse.python.cz/course/pyladies/beginners/comparisons/
  * https://naucse.python.cz/course/pyladies/beginners/str/
  * https://naucse.python.cz/lessons/beginners/expressions/

### Sraz 1.2
- for
- range
- while, break, continue
- def (vlastní funkce)
- 📚 materiály:
  - loops
      * https://naucse.python.cz/course/pyladies/intro/turtle/ (+ `for`)
      * https://naucse.python.cz/course/pyladies/beginners/while/
  - functions
      * https://naucse.python.cz/course/pyladies/beginners/functions/
      * https://raw.githubusercontent.com/pyvec/cheatsheets/master/basic-functions/basic-functions-cs.pdf
      * https://naucse.python.cz/course/pyladies/beginners/def/
      * https://naucse.python.cz/course/pyladies/beginners/nested-traceback/
      * https://github.com/mpavlase/python-workshop/tree/master/topics/functions#rozsah-platnosti-prom%C4%9Bnn%C3%BDch-variable-scope

### Sraz 1.3
- str (všechny operace pro str - tahák, f'', .format, %)
- try/except
- list
- 📚 materiály:
  - `str`
      * https://naucse.python.cz/lessons/beginners/str-index-slice/
      * https://naucse.python.cz/course/pyladies/beginners/str-methods/
      * https://naucse.python.cz/course/pyladies/beginners/fstring/
      * https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python
  - `str` taháky
      * **https://pyformat.info/**
      * https://pyvec.github.io/cheatsheets/strings/strings-cs.pdf
      * http://xahlee.info/comp/unicode_plants_flowers.html
  - výjimky
      * https://docs.python.org/3/library/exceptions.html#exception-hierarchy
  - `list`
      * https://naucse.python.cz/2020/brno-podzim-pondeli/beginners/list/


### Sraz 1.4
- dokončení z dřívějška: předávání argumentů funkcím
- tuple
- dict
- mutable vs. immutable types (+ poznámka k předávaným arg ve funkci)
- 📚 materiály:
  - předávání arg. funkcím https://github.com/mpavlase/python-workshop/tree/master/topics/functions#funkce
  - tuple
    * https://naucse.python.cz/course/pyladies/beginners/tuple/
  - dict
    * https://naucse.python.cz/course/pyladies/beginners/dict/
    * tahák https://pyvec.github.io/cheatsheets/dicts/dicts-cs.pdf


### Sraz 1.5
- práce se soubory (`open`, `fd.close()`)
- užití context manageru (`with open`)
- moduly - psaní vlastních modulů
- `__init__.py`, ukázat jak funguje import cache
- `__main__.py`, `if name == '__main__'`
- JSON, `python -m json.tool` (ukázat zdrojáky)
   - stáhněte si [ukázkový soubor](example.json)
- jen pokud zbyte čas:
  - set
  - enum
- 📚 materiály:
  - https://naucse.python.cz/2020/brno-podzim-pondeli/beginners/files/
  - https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects
  - https://naucse.python.cz/2020/brno-podzim-pondeli/beginners/modules/
  - `from package import *` https://docs.python.org/3/tutorial/modules.html#importing-from-a-package
  - https://docs.python.org/3/library/__main__.html
- poznámky:
  - env var:
    - Win: `%PYTHONPATH%` = `/path1;/path2`
    - Linux: `$PYTHONPATH` = `/path1:/path2`
