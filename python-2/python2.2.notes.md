# leftovers from last session
* venv
  * can't be moved to different location
  * venv removal
  * show create venv from New project dialog in PyCharm
  * different between: venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, ...
    * viz link v materiálech na StackOverflow
    * TLDR: begin with understanding pure `venv`, then experiment with other wrappers

# preparation
* day before session
  * create `venv`
  * activate `venv`
  * `pip install ipython notebook` (`numpy` a `matplotlib` not yet!)

# numpy, scipy, sympy, OpenCV, pandas...
> There are vast of python specialized libraries. We aren't going to go deep 
> dive - read the docs is essential.

# ipython
keyboard
- `char<ArrowUp>` completion
- `<Ctrl> + R` reverse search (`<Enter>` i pro editaci)
- `<Ctrl> + O` - newline v promptu
- `<Ctrl> + K` - remove content current line (preserve `\n`)

getting help:
- `<tab>` completion
- `obj?`, `obj??`
- middle search
  ```
  >>> import typing
  >>> typing.Mu*?  # case sensitive!
  >>> typing.*table*?
  ```

- `os?`
- "magic commands" (`%` prefix is not needed unless there is other symbol to collide)
  - https://ipython.readthedocs.io/en/stable/interactive/magics.html
  - `%cmd`
  - `%pip`
  - `%ls`, `%pwd`
  - `%run file.py`
  - `%notebook file.ipynb` - export current IPython session as Jupyter Notebook (requires `notebook`)
  - `%timeit?`
  - `%timeit 'a'.upper()` (inline) vs. `%%timeit` (cell mode)
  - `%load <file_or_url>` - load file/URL as prompt content (editable), i z URL (JSON placeholder URL)
  - `%quickref`
  - `%rerun 5-7` - promopt numbers from history
  - `%paste` - ignore `>`, `+`, paste & execute code from clipboard
  ```python
  In [10]: print('>>> a = 6\n>>> print(f"{a=}")')
  >>> a = 6
  >>> print(f"{a=}")
  
  In [11]: %paste
  >>> a = 6
  >>> print(f"{a=}")

  ## -- End pasted text --
  a=6
  ```
- `!ping`, `!notepad`, `msg = !ping 8.8.8.8`
- profily = possibility to use different ipythonu configs


# Jupyter Notebook
- show actions from menu first
- moves like VIM, `insert` vs `command` mode
  - cell types:
    - **M**arkdown
    - **Y** code
- commands:
  - insert new cell **A**bove,
  - insert new cell **B**elow,
  - **C**opy cell,
  - **V**ložit (paste) cell
  - **dd** delete cell

# numpy + sympy
- see **separated notebook** [python2.2.numpy.sympy.ipynb](python2.2.numpy.sympy.ipynb)

# matplotlib, cell magic, RISE, presentation mode
- see **separated notebook** [python2.2.matplotlib.ipynb](python2.2.matplotlib.ipynb)
- `% matplotlib inline` is implicit setup
  - inline doesn't provide zooming 
  - but `%matplotlib qt5` does
