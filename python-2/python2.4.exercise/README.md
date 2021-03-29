# Python2.4 - exercise
> This code acts here only for learning purpose and shouldn't be ever used in real application!

You were given a task to refactor code that moves stage on the microscope from coordinates `(X1, Y1)` to `(X2, Y2)`.
You found the code responsible for stage controlling and unfortunately it is a very old and ugly, developed by external company.

Keep in your mind *scout boy* rule and *"leave the code cleaner than you found it."*

**Your task is to improve the code quality.**


## Tasks
1. **execute `run_demo.py`** and then **read the code**. The try to understand what it does.
   This will be the most difficult part.
1. **prepare to refactor code**
    - open [clean code](https://github.com/zedr/clean-code-python) and [PEP8 recommendations](https://realpython.com/python-pep8/) as reference for your further steps
    - open all 4 files in PyCharm (they will be opened as tabs)
    - can be useful to arrange them by splitting to have better overview on whole project (Window - Editor tabs - Split Right/Down). You can do that also by dragging and dropping tab with filename and move to side.
1. **refactor code**
    - do by small steps, don't be in rush. Concentrate on a single thing 
      and improve it in whole file/project
    - pick better names for variables/files/classes/methods
    - replace magic numbers by named constants
    - use enums instead of raw strings representing choice value
    - reduce unnecessary complexity of whole project and simplify if it's possible
    - try to discover repetitive blocks of code and if *it's suitable* 
      move them into functions/methods
    - use idiomatic for-loops instead of while loops
