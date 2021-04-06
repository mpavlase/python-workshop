## Python 2


### Sraz 2.1
- orgranizace Py projektů:
  - pip
  - requirements.txt
  - venv
- materiály:
  - repozitář balíčků https://pypi.org
  - virtualenv vs venv vs pyenv... https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe
  - pipenv (officially recommended) https://realpython.com/pipenv-guide/


### Sraz 2.2
- ipython - https://ipython.readthedocs.io/en/stable/overview.html
  - příklad pro `%load`: https://jsonplaceholder.typicode.com/todos/1
- jupyter notebook - https://jupyter.org/documentation
- základy:
  - numpy
  - matplotlib

- examples for live presentation:
  - [python2.2.notes.md](python2.2.notes.md)
  - [python2.2.matplotlib.ipynb](python2.2.matplotlib.ipynb)
  - [python2.2.numpy.sympy.ipynb](python2.2.numpy.sympy.ipynb)

- other related libraries (not part of presentation):
  - **SciPy** - library for mathematics, science, and engineering. https://docs.scipy.org/doc/scipy/reference/tutorial/general.html
  - **Pandas** - library for data analysis. https://pandas.pydata.org/
  - **OpenCV** - image processing (`pip install cv2`). https://docs.opencv.org/master/d6/d00/tutorial_py_root.html

### Sraz 2.3
- úvod do tříd
  - zapouzdření,
  - třída vs. instance,
  - self,
  - class/inst property
- inheritance, super()

- examples for live presentation:
  -  [python2.3.notes.ipynb](python2.3.notes.ipynb)
- homework
  -  [python2.3.homework.ipynb](python2.3.homework.ipynb)
  -  solution: [python2.3.homework.solution.ipynb](python2.3.homework.solution.ipynb)

- materiály:
  - https://naucse.python.cz/2019/brno-podzim-pondeli/beginners/class/
  - https://naucse.python.cz/2019/brno-podzim-pondeli/beginners/inheritance/

### Sraz 2.4
- PEP8
- clean code
- Enum
- examples for live presentation:
  -  [python2.4.notes.ipynb](python2.4.notes.ipynb)
- exercise to practise (=called *homework* before):
  - [python2.4.exercise](python2.4.exercise)
- resources:
    - **pep8** - code style recommendations for Python, https://realpython.com/python-pep8/
        - PEP8 song 😃 https://www.youtube.com/watch?v=wNcobO-TAyY
    - **clean code** by examples - https://github.com/zedr/clean-code-python
    - **Enum** - enumeration data type, https://docs.python.org/3/library/enum.html


### Sraz 2.5
- Enum review
- typehints
- testing, pytest
- own defined exceptions
- examples for live presentation:
  - [python2.5.notes.ipynb](python2.5.notes.ipynb)
  - [python2.5.testing.notes.ipynb](python2.5.testing.notes.ipynb)
- exercise to practise
  - [python2.5.exercise](python2.5.exercise)
- resources
  - **mypy** - static analysis of code, https://mypy.readthedocs.io/
  - testing related:
    - https://docs.python-guide.org/writing/tests/
    - https://www.youtube.com/watch?v=FjwayiHNI1w
    - testing as science https://www.youtube.com/watch?v=FjwayiHNI1w
    - mocks, fakes, stubs, spies... - https://www.youtube.com/watch?v=-nJ-ZW_LP7s
    - test driven development, https://en.wikipedia.org/wiki/Test-driven_development#Test-driven_development_cycle
  - **pytest** - famous test runner, https://docs.pytest.org/en/stable/


### Sraz 2.6
- namedtuple
- pathlib
- dekorátory
- list/dict/set comprehensions
- ternary operator
- lambda, map, filter, sort
- logging module
- jupyter notebook as presentatin
- rady a postřehy k debuggování obecně
- PyCharm podrobně
