# Funkce

### Předávání parametrů


Mějme funkci, která vypíše větu podle zadaných slov:
```python
def say_something(name, animal, activity):
    print(f'{name} ma rad {animal} a {activity}.')
```

Funkci mohou předat argumenty více způsoby:
1. pořadím

    ```python
    >>> say_something('Jarek', 'zizaly', 'sekani travy')
    Jarek ma rad zizaly a sekani travy.
    ```

1. pojmenováním

    ```python
    say_something(name='Jarek', animal='zizaly', activity='sekaní travy')
    ```

    Když předáváme argumenty jmenně, můžeme si dovolit změnit pořadí,
    proto následující volání jsou zcela stejná.

    ```python
    say_something(name='Jarek', activity='sekani travy', animal='zizaly')
    say_something(activity='sekani travy', name='Jarek', animal='zizaly')
    say_something(activity='sekani travy', animal='zizaly', name='Jarek')
    ```

1. oboje dohromady

    Toto bude fungovat:
    ```python
    say_something('Jarek', 'zizaly', activity='sekani travy')
    ```

    následující příklad už ale ne.
    ```python
    >>> say_something('Jarek', activity='sekani travy', 'zizaly')
      File "<stdin>", line 1
    SyntaxError: positional argument follows keyword argument
    ```

    Není možné za pojmenované argumenty předávat poziční - nebylo by jasné,
    kolikátý by měl být v pořadí.


### Variabilní počet argumentů

Někdy ale dopředu nevíme, kolik parametrů nám chceme od uživatele převzít.
Typickým zástupcem je funkce `print`.

```python
>>> print('duck')
duck
>>> print(1, 2, 3.0, 'duck')
1 2 3.0 duck
```

Zkusíme si napsat svoji vlastní. Syntaxe vypadá následovně.

```python
def print_params(name, animal, activity, *args, **kwargs):
    print(f'name = {name}')
    print(f'animal = {animal}')
    print(f'activity = {activity}')
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')
```

Funkce přijímá 3 a více argumentů

* povinné argumenty: `name`, `animal` a `activity`
* skrze `*args` dostaneme (jako *n-tici*) `tuple` s dalšími argumenty,
  které byly předané pozičně
* v `**kwargs` dostaneme jako `dict` argumenty, které byly předané 
  jako pojmenované


Variabilní argumenty nemusíme předávat vůbec:
```python
>>> print_params('Josef', 'vrabec', 'utirani prachu')
name = Josef
animal = vrabec
activity = utirani prachu
args = ()
kwargs = {}
```

Ukázka předání parametrů navíc:
```python
>>> print_params('Josef', 'vrabec', 'utirani prachu', 'zahrada', 123, city='Brno', place='Prygl')
name = Josef
animal = vrabec
activity = utirani prachu
args = ('zahrada', 123)
kwargs = {'city': 'Brno', 'place': 'Prygl'}
```

Všimni si, že jednou napasovaný parametr již v `args` a `kwargs` nikdy neobjeví.

Jména `args` a `kwargs` (pochází z *keyword arguments*) jsou ustálenými jmény,
které ale nejsou pevně stanoveny a i následující zápis je zcela v pořádku.
```python
def my_fn(*positional_arguments, **keyword_arguments):
    ...
```

### Rozsah platnosti proměnných (variable scope)

Proměnné uvnitř funkcí mají svůj rozsah platnosti. Proto jsou proměnné definované
mimo funkci unitř přístupné. Naopak to ale nefunguje. Proměnné definované unitř
funkce nejsou mimo ni vidět (s jednou výjimkou popsanou dále).

#### Proměnné mimo tělo funkce
Globální proměnná `name` uvnitř funkce k dispozici je:

```python
name = 'Tonda'

def get_name():
    print(f'{name} (inside)')

print(f'{name} (before call)')
get_name()
print(f'{name} (after call)')
```

Výstup:
```python
Tonda (before call)
Tonda (inside)
Tonda (after call)
```


#### Proměnná pouze v nitru funkce

Proměnná definovaná pouze uvnitř funkce je vidět pouze uvnitř, ne však ven mimo ni.


```python
def get_name():
    name = 'Tonda'
    print(f'{name} (inside)')

print(f'{name} (before call)')
get_name()
print(f'{name} (after call)')
```

Provádění selže, protože v globálním *scope* (tj. mimo tělo funkce) žádná
proměnná `name` neexistuje.
```
Traceback (most recent call last):
  File "variable-scope.py", line 5, in <module>
    print(f'{name} (before call)')
NameError: name 'name' is not defined
```

Zkusme si zakomentovat 5. řádek (`# print(f'{name} (before call)')`). Jaký výstup
dostaneme? Je to trochu lepší, funkce se vykoná (`Tonda (inside)`), ale další chyba 
je na světě - ten samý problém.

```
Tonda (inside)
Traceback (most recent call last):
  File "variable-scope.py", line 7, in <module>
    print(f'{name} (after call)')
NameError: name 'name' is not defined
```

Jak je to možné? Vždyť jsme do `name` přiřadili hodnotu... Jakmile funkce skončí,
všechny proměnné, které byly definované v jejím těle jsou zahozeny.

#### Globální proměnné jsou uvnitř jen pro čtení
Jak to ale skutečně funguje s proměnnými definovanými mimo funkci? To záleží...

* Pokud proměnnou v scope (v tomto případě tělo funkce) jen čteme,
  hodnotu normálně získáme.
* Pokud do ní chceme v tomto scope něco uložit, Python na nás zakřičí
  výjimkou `UnboundLocalError`. Nezáleží přitom ve které části scope se pokusíme
  do proměnné zapsat.

```python
name = 'Tonda'

def get_name():
    print(f'{name} (inside)')
    name = 'Jolana'

print(f'{name} (before call)')
get_name()
print(f'{name} (after call)')
```

Výstup:
```
Tonda (before call)
Traceback (most recent call last):
  File "variable-scope.py", line 8, in <module>
    get_name()
  File "variable-scope.py", line 4, in get_name
    print(f'{name} (inside)')
UnboundLocalError: local variable 'name' referenced before assignment
```

Pro toto chování je ale dobrý úmysl, protože pokud by globální proměnná byla
editovatelná i v lokálním scope, jednalo by se o tzv. *side-effect*, což znamená,
že funkce dělá i něco navíc, než by se od ní očekávalo.

Pokud potřebujeme změnit globální proměnnou, můžeme použít klíčové slovo `global`
([dokumentace](https://docs.python.org/3/reference/simple_stmts.html#global)),
nebo bychom to měli udělat v globálním scope.

Pokud takový případ vůbec nastane, je dobré se nejdříve zamyslet, jestli na to
jedeme ze správného konce.