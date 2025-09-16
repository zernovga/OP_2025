---
transition: slide-left
theme: sirius-college
exportFilename: pdf/op_lection_5
layout: cover
---

# Основы программирования<br>Лекция 5. 

Обработка ошибок. Работа с файлами. Контекстные менеджеры. Структурированные текстовые файлы.

---

# Обработка ошибок

- Ошибки отображаются с помощью специальных возвращаемых значений. В Python для отслеживания и корректной обработки ошибок используются исключения.
- **Исключение** - это такой код, который выполняется, когда происходит связанная с ним ошибка.
- Когда вы выполняете код, в котором при некоторых обстоятельствах могут возникнуть ошибки, вам понадобятся **обработчики исключений**.
- Если не предоставить Python код обработчика ошибок, выведется сообщение об ошибке, а программа завершится.

---

# Обработка ошибок

````md magic-move
```python
short_list = [1, 2, 3]

position = 3

short_list[position]
# IndexError: list index out of range
```

```python
short_list = [1, 2, 3]

position = 3

try:
    short_list[position]
except:
    print(f"Need position between 0 and {len(short_list) - 1}")
# Need position between 0 and 2
```

```python
short_list = [1, 2, 3]

while True:
    value = input("Position? [q to quit] ")
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print(f"Bad index: {err}")
    except Exception as other:
        print(f"Something else broke: {other}")
```

```python
print("You can get 3 squares if you'd like")
for i in range(3):
    try:
        number = int(input())
    except ValueError:
        print("That's not a number")
    except KeyboardInterrupt:
        print("How rude of you")
    else:
        print(f"{number} squared is {number**2}")
```

```python
print("You can get 3 squares if you'd like")
for i in range(3):
    try:
        number = int(input())
    except ValueError:
        print("That's not a number")
    except KeyboardInterrupt:
        print("How rude of you")
    else:
        print(f"{number} squared is {number**2}")
    finally:
        print("This always runs")
```
````

---

# Путь к файлам

- Путь к файлам представляет собой строковый тип данных.
- Путь к файлам может быть представлен как относительный путь или абсолютный путь.

Необходимо использовать корректный формат пути:

::block-component{v-click="1"}

Для Windows:

````md magic-move {at:2}
```python
path = 'C:\Users\User\Python\letters.txt'
```

```python
path = 'C:\Users\User\Python\letters.txt'
# File "<python-input-0>", line 1
#     path = 'C:\Users\User\Python\letters.txt'
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
```

```python
path = r'C:\Users\User\Python\letters.txt'
# или
path = 'C:\\Users\\User\\Python\\letters.txt'
```
````

::

::block-component{v-click="4"}

Для Linux:

```python
path = '/home/user/Python/letters.txt'
```

::

---

# Работа с файлами. Открытие и закрытие файлов

````md magic-move
```python
fp = open('filename', mode='w')
```

```python
with open('filename') as fp:
    read_data = fp.read()
```

```python
fp = open('filename')
try:
   # Дальнейшая обработка файлов идет здесь
   read_data = fp.read()
finally:
   fp.close()
```
````

---

# Режимы чтения и записи

- `r` - открывает файл только для чтения
- `w` - открыт для записи (перед записью файл будет очищен)
- `x` - эксклюзивное создание, бросается исключение FileExistsError
- `a` - открыт для добавления в конец файла
- `+` - символ обновления (чтение + запись)
- `t` - символ текстового режима
- `b` - символ двоичного режима

Символы можно (и нужно) использовать сразу в нескольких режимах:

````md magic-move
```python
fp = open('filename', mode='w')
```

```python
fp = open('filename', mode='wb')
```

```python
fp = open('filename', mode='r+t')
```
````

---

# Способы чтения файлов

Метод `fp.read(size=-1)` считывает из файла не более `size` символов
```python
with open('filename') as fp:
    read_data = fp.read()
```

Метод `fp.readline(size=-1)` читает не более `size` символов в строке за раз. Считывание продолжается до конца строки.
  ```py
  with open('text.txt', 'r') as fp:
     # читаем и печатаем первые 5 символов строки
     print(fp.readline(5))
  ```
Метод `fp.readlines()` читает файл целиком и возвращает их в виде списка.

  ```python
  with open('text.txt', 'r') as fp:
     # Возвращает объект списка
     text_list = fp.readlines()

  text_list
  # ['Строка №1', 'Строка №2', 'Строка №3', 'Строка №4', 'Строка №5']
  ```

---

# Способы чтения файлов

````md magic-move
```python
with open('text.txt', 'r') as fp:
   # Считывание и печать всего файла строка за строкой
   line = fp.readline()
   while line != '':
       print(line, end='')
       line = fp.readline()
```

```python
with open('text.txt', 'r') as fp:
   # Считывание и печать всего файла строка за строкой
   for line in fp.readlines():
       print(line, end='')
```

```python
with open('text.txt', 'r') as fp:
   # Считывание и печать всего файла строка за строкой
   for line in fp:
       print(line, end='')
```
````

---

# Способы записи файлов

Метод `fp.write(string)` записывает в файл строку. "Строка" может быть сколь угодно большой и уже заранее разделена на подстроки escape-последовательностью новой строки `'\n'`. То есть этот метод позволяет писать в файл как построчно, так и все сразу.

````md magic-move
```python
text = ['Строка №1', 'Строка №2', 'Строка №3', 'Строка №4', 'Строка №5']

with open('text.txt', 'w') as fp:
   for line in text:
          fp.write(line + '\n')
```

```python
text = ['Строка №1', 'Строка №2', 'Строка №3', 'Строка №4', 'Строка №5']
write_string = '\n'.join(text)

with open('text.txt', 'w') as fp:
   fp.write(write_string)
```
````

---

# Способы записи файлов

Метод `fp.writelines(sequence)` записывает в файл последовательность, которая в качестве элементов содержит строки. Метод не добавляет автоматически разделители строк `'\n'`.

````md magic-move
```python
text = ['Строка №1', 'Строка №2', 'Строка №3', 'Строка №4', 'Строка №5']

with open('text.txt', 'w') as fp, open('text.txt', 'r') as fr:
   fp.writelines(text)
   fp.flush()
   for line in fr:
       print(line, end='')
```
````

---

# Контекстные менеджеры

````md magic-move
```python
f = open("file.txt", "w")
f.write("hello")
f.close()
```

```python
f = open('file.txt', 'w')
try:
    f.write('hello')
except:
    print('Some error!')
finally:
    f.close()
```

```py
with open('file.txt', 'w') as f:
     f.write('hello')
```
````

---

# Контекстные менеджеры

Оператор `with` в Python поддерживает концепцию контекста среды выполнения, определенного контекстным менеджером.

Типичные области применения контекстных менеджеров включают сохранение и восстановление различных типов глобального состояния, блокировку и разблокировку ресурсов, закрытие открытых файлов и т.д.

```python
with EXPRESSION as TARGET:
    SUITE
```

---

# Примеры применения контекстных менеджеров

````md magic-move
```python
# Обход каталогов

import os

with os.scandir('.') as entries:
    for entry in entries:
        print(entry.name, "->", entry.stat().st_size, "bytes")
```

```python
# Выполнение высокоточных вычислений
from decimal import Decimal, localcontext

with localcontext() as ctx:
    ctx.prec = 42
    Decimal("1") / Decimal("42")
# Decimal('0.0238095238095238095238095238095238095238095')

Decimal("1") / Decimal("42")
# Decimal('0.02380952380952380952380952381')
```

```python
# Блокировка в многопоточном режиме

import threading

balance_lock = threading.Lock()

balance_lock.acquire()
try:
    # Выполняем текущую операцию с балансом
finally:
    balance_lock.release()
```

```python
# Блокировка в многопоточном режиме

import threading

balance_lock = threading.Lock()

with balance_lock:
    # Выполняем текущую операцию с балансом
```

```python
import pytest

1 / 0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero

with pytest.raises(ZeroDivisionError):
    1 / 0
```

```python
import pytest

favorites = {"fruit": "apple", "pet": "dog"}
favorites["car"]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'car'

with pytest.raises(KeyError):
    favorites["car"]
```

```python
import pytest

with pytest.raises(ZeroDivisionError):
    4 / 2

# 2.0
# Traceback (most recent call last):
#   ...
# Failed: DID NOT RAISE <class 'ZeroDivisionError'>
```

```python
import pytest

with pytest.raises(ZeroDivisionError) as exc:
    1 / 0

assert str(exc.value) == "division by zero"
```
````

---

# Структурированные текстовые файлы. CSV

- **Comma-Separated Values** — значения, разделённые запятыми. Текстовый формат, предназначенный для представления табличных данных. Строка таблицы соответствует строке текста, которая содержит одно или несколько полей, разделенных запятыми.
- Идея использовать запятые для разделения полей очевидна, но при таком подходе возникают проблемы, если исходные табличные данные содержат запятые или переводы строк.
- Возможным решением проблемы запятых и переносов строк является заключение данных в кавычки, однако исходные данные могут содержать кавычки.

::block-component {style="font-size:20px;"}

|  Team   | Games | Wins | Losses | Draws | Goals For | Goals Against |
| :-----: | :---: | :--: | :----: | :---: | :-------: | :-----------: |
| Arsenal |  38   |  26  |   9    |   3   |    79     |      36       |

::

```csv
Team,Games,Wins,Losses,Draws,Goals For,Goals Against
Arsenal,38,26,9,3,79,36
```

---
layout: two-cols
---

# Структурированные текстовые файлы. CSV

```python
import csv

names = [
  ["Hovard", "Roark"],
  ["Peter", "Keating"],
  ["Dominique", "Francon"],
  ["Gail", "Wynand"],
  ["Ellsworth", "Toohey"]
]

with open("names.csv", "w") as fp:
    writer = csv.writer(fp)
    writer.writerows(names)
```

::right::

Файл `names.csv`
```csv
Hovard,Roark,
Peter,Keating
Dominique,Francon
Gail,Wynand
Ellsworth,Toohey
```

---

# Структурированные текстовые файлы. CSV

```python
import csv

with open("names.csv") as fp:
    reader = csv.reader(fp)
    names = [name for name in reader]
print(names)

# [['Hovard', 'Roark'], ['Peter', 'Keating'], ...]
```

---
layout: two-cols
---

# Структурированные текстовые файлы. CSV

```python
import csv

names = [...]

names2: dict = [
    {'first_name': fst, 'last_name': lst}
    for fst, lst in names
    ]

with open("names_2.csv", "w") as fp:
    writer = csv.DictWriter(fp,
        ['first_name', 'last_name'])
    writer.writeheader()
    writer.writerows(names_2)
```

::right::

Файл `names2.csv`
```csv
first_name,last_name
Hovard,Roark
Peter,Keating
Dominique,Francon
Gail,Wynand
Ellsworth,Toohey
```

---

# Структурированные текстовые файлы. CSV

```python
import csv

with open("names_2.csv") as fp:
    reader = csv.DictReader(fp)
    names = [name for name in reader]
print(names)

# [{'first_name': 'Hovard', 'last_name': 'Roark'}, ...]
```

---

# Структурированные текстовые файлы. XML

- **eXtensible Markup Language** — «расширяемый язык разметки».
- Язык называется расширяемым, поскольку он не фиксирует разметку, используемую в документах: разработчик волен создать разметку в соответствии с потребностями к конкретной области, будучи ограниченным лишь синтаксическими правилами языка.
- Расширение XML — это конкретная грамматика, созданная на базе XML и представленная словарём тегов и их атрибутов, а также набором правил, определяющих, какие атрибуты и элементы могут входить в состав других элементов.

---

# Структурированные текстовые файлы. XML

```xml
<?xml version="1.0">
<menu>
  <breakfast hours="7:00-9:00">
    <item price="5.95">Scrambled eggs</item>
    <item price="6.95">Pancakes</item>
  </breakfast>
  <lunch hours="11:00-13:00">
    <item price="7.95">Hamburger</item>
    <item price="8.95">Soup</item>
  </lunch>
</menu>
```

---

# Структурированные текстовые файлы. XML

```python
import xml.etree.ElementTree as et

tree = et.ElementTree(file="menu.xml")
root = tree.getroot()
print(root.tag)
def read(root, level=0):
    for child in root:
        padding = "\t" * level
        print(f"{padding}tag: {child.tag};\
          value: {child.text};attrs: {child.attrib}")
        if child:
            read(child, level + 1)

read(root)
```

---

# Структурированные текстовые файлы. XML

```console
menu
tag: breakfas;value:
        ;attrs: {'hours': '7:00-9:00'}
    tag: item;value: Scrambled eggs;attrs: {'price': '5.95'}
    tag: item;value: Pancakes;attrs: {'price': '6.95'}
tag: lunch;value:
        ;attrs: {'hours': '11:00-13:00'}
    tag: item;value: Hamburger;attrs: {'price': '7.95'}
    tag: item;value: Soup;attrs: {'price': '8.95'}
```

---

# Структурированные текстовые файлы. JSON

- **JavaScript Object Notation** — текстовый формат обмена данными, основанный на JavaScript.
- Как и многие другие текстовые форматы, JSON легко читается людьми.
- Несмотря на происхождение от JavaScript, формат считается независимым от языка и может использоваться практически с любым языком программирования.
- Для многих языков существует готовый код для создания и обработки данных в формате JSON.
- Активно используется в нереляционных БД.

---

# Структурированные текстовые файлы. JSON

```json
{
  "breakfast": {
    "hours": "7:00-9:00",
    "items": {
      "Scrambled eggs": "5.95",
      "Pancakes": "6.95"
    }
  },
  "lunch": {
    "hours": "11:00-13:00",
    "items": {
      "Hamburger": "7.95",
      "Soup": "8.95"
    }
  }
}
```

---

# Структурированные текстовые файлы. JSON

```python
import json
from pprint import pprint

with open("menu.json") as fp:
    menu = json.load(fp)

pprint(menu)

# {'breakfast': {'hours': '7:00-9:00',
#                'items': {'Scrambled eggs': '5.95', 'Pancakes': '6.95'}},
#  'lunch': {'hours': '11:00-13:00',
#            'items': {'Hamburger': '7.95', 'Soup': '8.95'}}}
```

---

# Структурированные текстовые файлы. JSON

```python
menu = {
    "breakfast": {
        "hours": "7:00-9:00",
        "items": {"Scrambled eggs": "5.95", "Pancakes": "6.95"}},
    "lunch": {
        "hours": "11:00-13:00",
        "items": {"Hamburger": "7.95", "Soup": "8.95"}}
}

data = json.dumps(menu)
print(type(data))
# <class 'str'>
print(data)
# {"breakfast": {"hours": "7:00-9:00", "items": {"Scrambled eggs": "5.95", "Pancakes": "6.95"}}, "lunch": {"hours": "11:00-13:00", "items": {"Hamburger": "7.95", "Soup": "8.95"}}}
```

---

# Структурированные текстовые файлы. JSON

```python
import json

data_json = json.dumps(menu)
back_to_data = json.loads(data_json)
print(type(back_to_data))
# <class 'dict'>
pprint(back_to_data)
# {'breakfast': {'hours': '7:00-9:00',
#                'items': {'Scrambled eggs': '5.95', 'Pancakes': '6.95'}},
#  'lunch': {'hours': '11:00-13:00',
#            'items': {'Hamburger': '7.95', 'Soup': '8.95'}}}
```
