# Konvence pojmenování

Jména v Pythonu nejsou vyžadována jazykem, ale je důležité se jich držet.
Při čtení cizích zdrojových kódů se pak nemusí člověk učit další _cizí jazyk_.

### Proměnné
se píší v snake_case.

```python
sum_of_items = len(items)
username = 'Tonda'
```

```python
for item in input_devices:
    ...
```

Pokud nás získaná hodnota nezajímá, typicky se používá `_` pro název.

```python
for _ in range(5):
    ping()
```


### Konstanty

**Konstanty** všemi velkými písmeny:
```python
MAX_ITERATIONS = 15
LIMIT = 1e3
```

### Funkce
se píší, stejně jako proměnné, v snake_case.

```python
def get_date():
    ...

def exit():
    ...
```

Název funkce musí vyjadřovat akci, jinak se pravděpodobně jedná o špatný návrh
(např. funkce nedělá jen jednu věc). Pokud funkce zjišťuje, zda fakt platí,
je vhodné používat prefix `is_`.

```python
# 
def processing():
    ...

def resize_event():
    ...

def busy():
    ...
```

Funkce `processing()` spouští zpracování dat, nebo vrací `True`, `False` podle
toho, zda zpracování právě probíhá? `resize_event()` způsobí vyvolání události,
nebo naopak funkce obsahuje kód, který se má provést, pokud událost nastane?

vs.

```python
def process_values():
    ...

def handle_resize_event():
    ...
```

`busy()` z prvního příkladu nastaví na zařízení příznak "busy", nebo tento 
příznak vrací?

```python
def is_busy():
    ...

def set_busy_flag():
    ...
```


### Objekty, třídy, metody
**Názvy tříd** se píší CamelCase, v jednotném čísle, protože třída představuje
_jednu šablonu_, podle které se vyrábí samotné objekty (=instance).

**Názvy metod** ve třídě se drží stejného pravidla, jako obyčejná funkce,
která není součástí objektu. O podtržítcích více v části s objekty.

```python
class Coil:
    ...

class SetupManager:
    ...

class TSCConnector:
    def connect(self):
        ...

    def _get_hw_address(self):
        ...

    def __send_raw_data(self, data):
        ...
```
