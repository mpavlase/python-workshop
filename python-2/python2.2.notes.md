# nedodělky z minula
* venv
  * nelze přesounout
  * mazání venvu
  * vytvoření venvu skrze nový projekt v PyCharmu
  * rozdíly mezi: venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv
    * viz link v materiálech na StackOverflow
    * TLDR: pochop a používej základní venv, pak teprve zkoušej tooly výše.

# příprava
* poslat den před kurzem:
  * založit `venv`
  * aktivovat `venv`
  * `pip install ipython notebook` (`numpy` a `matplotlib` ještě ne!)

# ipython
klávesnice
- `znak<ArrowUp>` doplňování
- `<Ctrl> + R` reverse search (`<Enter>` i pro editaci)
- `<Ctrl> + O` - newline v promptu
- `<Ctrl> + K` - remove content current line (preserve `\n`)

nápověda:
- `<tab>` completion
- `obj?`, `obj??`
- middle search
  ```
  >>> import typing
  >>> typing.Mu*?  # case sensitive!
  >>> typing.*table*?
  ```

- `os?`
- "magic commands" (možno psát i bez `%`, ale jen pokud nekoliduje s jiným symbolem)
  - `%cmd`
  - `%pip`
  - `%ls`, `%pwd`
  - `%run file.py`
  - `%notebook file.ipynb` - export current IPython session as Jupyter Notebook (requires `notebook`)
  - `%timeit?`
  - `%timeit 'a'.upper()` (inline) vs. `%%timeit` (cell mode)
  - `%load <file_or_url>` - load file/URL as prompt content (editable), i z URL (JSON placeholder URL)
  - `%quickref`
  - `%rerun 5-7` - čísla promptů z historie
- `!ping`, `!notepad`, `msg = !ping 8.8.8.8`
- profily = samostatné konfigurace ipythonu


# Jupyter Notebook
- podobně jako VIM, `insert` vs `command` mode 
- commands:
  - insert **A**bove,
  - insert **B**elow,
  - **C**opy cell,
  - **V**ložit (paste) cell
  - **dd** delete cell
- numpy viz **separated notebook**
- `pip install RISE` (rich presentation with live execution)
  - 

### matplotlib
- `pip install matplotlib`


- matplotlib.inline
  - v základě bez lupy
- sympy
  - převod rovnic do LaTeXu
