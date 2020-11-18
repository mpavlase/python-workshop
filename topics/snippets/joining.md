# slepování řetězců, cesty k souborům

## Příklad č.1: lepení řetězců

> Chceme vytvořit CSV soubor

CSV je jednoduchý textový formát pro ukládání tabulkových dat.
```
cislo;jmeno;prijmeni
```

Takto ne:
```python
csv = index + ';' + name + ';' + surname
```

* pracné přidání další položky (rozšířit lze pouze ručním zásahem)
* opakující se vzor oddělovače středníku (co když budu potřebovat oddělovač
  změnit třeba na čárku?)

Takto taky ne:
```python
data = [index, name, surname]
csv = ''
for item in data:
    csv += item
    csv += ';'

# remove extra ; from end
csv = csv[:-1]
```

* musím si ohlídat odstranění oddělovače z posledního kusu


Takto ano:
```python
data = [index, name, surname]
csv = ';'.join(data)
```

V čem to je lepší?
* přidání dalšího sloupce je velmi pohodlné - stačí rozšířit pole `data`
* 



## Příklad č.2: cesta k souborům

> Potřebuju sestavit cestu k souboru...

Takto ne!

```python
base_path = 'C:\\' + dir1 + '\\'
file_path = base_path + filename
```

Co je tady špatně?

* platformí závislost na oddělovači adresářů (Linux/UNIX + Mac používá `/`,
  Windows `\ `)
* když chci skládat cestu, je na konci `base_path` už obsažen oddělovač, nebo ne?
  Musím si to pamatovat, nebo vyčíst z kódu...

Takto ano:
```python
imprt pathlib

base_path = pathlib.Path('C:\\' + dir1)
file_path = base_path / filename
```

Konkrétně to pak vypadá takto:
```python
>>> base_path = pathlib.Path('C:\\repos')
>>> file_path = base_path / 'pystem' / 'data'
```

`file_path` je objekt, který poskytuje další užitečné metody:
```python
>>> file_path
WindowsPath('C:/repos/pystem/data')
>>> file_path.exists()
False
```

Poznámka: funkce `open` očekává řetězec s cestou. Proto je potřeba ji předtím
převést (všimni si změny lomítek):
```python
>>> str(file_path)
'C:\\repos\\pystem\\data'
```


