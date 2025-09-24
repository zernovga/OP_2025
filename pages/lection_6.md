---
transition: slide-left
theme: sirius-college
exportFilename: pdf/op_lection_6
layout: cover
---

# Основы программирования<br>Лекция 6. 

Отладка кода. Логирование. Тестирование. Pytest

---

# Отладка кода

Этап разработки компьютерной программы, на котором обнаруживают, локализуют и устраняют ошибки.

Для обнаружения ошибок пошагово выясняют путь, по которому выполнялась программа, а также значения используемых переменных на каждом из этих шагов.

---

# Простейшие способы отладки

- Самый простой и быстрый способ отладки программ мы
  использовали ранее - это встроенная функция `print()`.

---

# Отладка с помощью `print()`

```python {*|6-12|14-17|19-22|23-28}{maxHeight:'420px'}
from math import sqrt
from random import randint
from typing import Tuple


def quadratic_equation(a: int, b: int, c: int) -> Tuple[float]:
    d = b**2 - 4 * a * c
    sq = sqrt(d)
    x1 = -b + sq / (2 * a)
    x2 = -b - sq / (2 * a)

    return x1, x2

def rnd(a: int = -10, b: int = 10) -> int:
    return randint(a, b)

equations = [(rnd(), rnd(), rnd()) for _ in range(10)]

if __name__ == "__main__":
    for values in equations:
        print('Values\t a: {0}, b: {1}, c: {2}'.format(*values))
        print('Result\t x1: {0}, x2: {1}'.format(*quadratic_equation(*values)))
# Traceback (most recent call last):
#   File "/home/gleb/documents/lection_8.py", line 22, in <module>
#     print('Result\t x1: {0}, x2: {1}'.format(*quadratic_equation(*values)))
#   File "/home/gleb/documents/lection_8.py", line 8, in quadratic_equation
#     sq = sqrt(d)
# ValueError: math domain error
```

---

# Отладка с помощью `print()`

```python {*|7,9,11|17-}{maxHeight:'420px', startLine:6}
def quadratic_equation(a: int, b: int, c: int) -> Tuple[float]:
    print('quadric equation: Values\t a: {0}, b: {1}, c: {2}'.format(a, b, c))
    d = b**2 - 4 * a * c
    print('quadric equation: Discriminant: {0}'.format(d))
    sq = sqrt(d)
    print('quadric equation: Disc sqrt: {0}'.format(sq))
    x1 = -b + sq / (2 * a)
    x2 = -b - sq / (2 * a)

    return x1, x2

# Values    a: 8, b: 2, c: 1
# quadric equation: Discriminant: -28
# Traceback (most recent call last):
#   File "/home/gleb/documents/lection_8.py", line 25, in <module>
#     print('Result\t x1: {0}, x2: {1}'.format(*quadratic_equation(*values)))
#   File "/home/gleb/documents/lection_8.py", line 9, in quadratic_equation
#     sq = sqrt(d)
# ValueError: math domain error
```

---

# Отладка с помощью точек останова (breakpoints)

По умолчанию в VSCode поддерживается три вида точек останова:

- **Expression (выражение):** Break when expression evaluates to true. Остановить, когда выражение станет истинным.
- **Hit count (количество срабатываний):** Break when hit count condition is met. Остановить, когда условие количества срабатываний будет выполнено.
- **Log message (лог-сообщение):** Message to log when breakpoint is hit. Expressions within {} are interpolated. Сообщить в лог, когда сработает точка останова. Выражения внутри {} интерполируются.

---

# Отладка с помощью точек останова (breakpoints)

::center

![alt text](/img/lection_6/image.png){width=90%}

::

---

# Отладка с помощью точек останова (breakpoints)

::center

![alt text](/img/lection_6/image-1.png){width=70%}

::

---

# Модули `pdb` и `ipdb`

**Pdb (Python DeBug)** - модуль для ручного дебаггинга вашего кода.
Начать дебаггинг вашего кода можно, запустив в вашем коде:

```python
import pdb
pdb.set_trace()
```

> Когда вы запустите ваш код, запустится интерактивный режим дебаггинга. Вы сможете переходить выполнять ваш код пошагово с помощью определенных команд.

---

# Модули `pdb` и `ipdb`

- `list()`
  Эта команда покажет часть кода, на выполнении которой сейчас находится
  интерпретатор.
- `up(p)` и `down(d)`
  Эти команды используются для передвижения по стеку вызовов. С их
  помощью можно отследить, откуда была вызвана текущая функция.
- `step()` и `next()`
  С помощью этих команд можно выполнять код построчно. Единственное
  различие между ними в том, что `next()` перейдёт к следующей строке вне
  зависимости от вызываемых функций, а `step()` перейдёт в вызванную
  функцию, если это возможно.
- `break()`
  Эта команда позволяет создавать брейкпоинты без внесений изменений в
  код.

---

# Модули `pdb` и `ipdb`

::center

![alt text](/img/lection_6/image-2.png){width=90%}

::

---

# Логирование

<<< @/code/log1.py python {*|8-9|12|15-16|17-21|32-40}{maxHeight: '420px'}

---

# Логирование

<<< @/code/log.txt log

---

# Логирование. Модуль `logging`

- Позволяет вести лог выполнения программы как в консоли, так и в файле.
- Имеет уровни дебаггинга, например:

| Level      | Numeric value |
| ---------- | ------------- |
| `CRITICAL` | 50            |
| `ERROR`    | 40            |
| `WARNING`  | 30            |
| `INFO`     | 20            |
| `DEBUG`    | 10            |
| `NOTSET`   | 0             |

---

# Логирование. Модуль `logging`

<<< @/code/log2.py python {*|1|12,16,18,21|33}{maxHeight:'420px'}

---

# Логирование. Модуль `logging`

::center

![alt text](/img/lection_6/image-3.png){width=90%}

::

---

# Логирование. Модуль `logging`

<<< @/code/log3.py python {\*|33-35}{maxHeight:'420px'}

---

# Логирование. Модуль `logging`

<<< @/code/logging.txt log

---

---

# Тестирование

Тестирование программного обеспечения — процесс исследования, испытания программного продукта, имеющий своей целью проверку соответствия между реальным поведением программы и её ожидаемым поведением на конечном наборе тестов, выбранных определённым образом.

В Python тестирование осуществляется с помощью встроенной библиотеки `unittest` или `pytest`.

Большинство функциональных тестов используют модель **Arrange-Act-Assert**:

- **Arrange** - подготовка условий для теста;
- **Act** - вызов необходимых функций;
- **Assert** - проверка результатов.

---

# Виды тестирования

- **Модульный тест (Unit test)**: тест, который проверяет небольшой фрагмент кода, например функцию или класс, в изоляции от остальной системы.
- **Интеграционный тест (Integration Testing)**: тест, который проверяет больший фрагмент кода, может включать несколько классов или подсистемы. Главным образом ярлык используемый для некоторого испытания побольше чем модульный тест, но меньше системного теста.
- **Системный тест (end-to-end)**: тест, который проверяет всю тестируемую систему в среде, максимально приближенной к среде конечного пользователя.
- **Функциональный тест (Functional testing)**: Тест, который проверяет один фрагмент функциональности системы.
- **Subcutaneous test**: Тест, который выполняется не для конечного пользовательского интерфейса, а для интерфейса, расположенного чуть ниже поверхности.

---

# `unittest`. Формат кода

- тесты должны быть написаны в классе;
- класс должен быть унаследован от базового класса `unittest.TestCase`;
- имена всех функций, являющихся тестами, должны начинаться с ключевого слова `test_`;
- внутри функций должны быть вызовы операторов сравнения (`assertX`).

---

# `unittest` vs `pytest`. Пример теста

````md magic-move
```python
from unittest import TestCase

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)
```

```python
def test_always_passes():
    assert True

def test_always_fails():
    assert False
```
````

---

# `pytest`. Пример вывода

```shell {*|1|3-5|7-8|11-17|27-31}{maxHeight: '420px'}
(venv) $ pytest
============================ test session starts ===========================
platform win32 -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0
rootdir: ...\testing-with-pytest
collected 4 items

test_with_pytest.py .F                                                [ 50%]
test_with_unittest.py F.                                              [100%]

================================= FAILURES =================================
_____________________________ test_always_fails ____________________________

    def test_always_fails():
>       assert False
E       assert False

test_with_pytest.py:7: AssertionError
_______________________ TryTesting.test_always_fails _______________________

self = <test_with_unittest.TryTesting testMethod=test_always_fails>

    def test_always_fails(self):
>       self.assertTrue(False)
E       AssertionError: False is not true

test_with_unittest.py:10: AssertionError
========================== short test summary info =========================
FAILED test_with_pytest.py::test_always_fails - assert False
FAILED test_with_unittest.py::TryTesting::test_always_fails - AssertionError:...

======================== 2 failed, 2 passed in 0.20s =======================
```

---

# `pytest -v` / `pytest --verbose`

Подробный вывод

````md magic-move
```py {*|*}
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)
```

```py {*|*}
def test_failing():
    assert (1, 2, 3) == (3, 2, 1)
```
````

<br>

````md magic-move {at:1}
```shell
$ pytest test_one.py
===================== test session starts ======================
collected 1 items
test_one.py .
=================== 1 passed in 0.01 seconds ===================
```

```shell
$ pytest -v test_one.py
===================== test session starts ======================
collected 1 items
test_one.py::test_passing PASSED
=================== 1 passed in 0.01 seconds ===================
```

```shell {*|9-11}
$ pytest test_two.py
===================== test session starts ======================
collected 1 items
test_two.py F
=========================== FAILURES ===========================
_________________________ test_failing _________________________
def test_failing():
>    assert (1, 2, 3) == (3, 2, 1)
E     assert (1, 2, 3) == (3, 2, 1)
E         At index 0 diff: 1 != 3
E         Use -v to get the full diff

test_two.py:2: AssertionError
=================== 1 failed in 0.04 seconds ===================
```

```shell {*}{maxHeight: '220px'}
$ pytest -v test_two.py
...
def test_failing():
>    assert (1, 2, 3) == (3, 2, 1)
E    assert (1, 2, 3) == (3, 2, 1)
E      At index 0 diff: 1 != 3
E      Full diff:
E      - (1, 2, 3)
E      ?   ^     ^
E      + (3, 2, 1)
E      ?   ^     ^

test_two.py:2: AssertionError
=================== 1 failed in 0.04 seconds ===================
```
````

---

# `pytest --collect-only`

Параметр `--collect-only` показывает, какие тесты будут выполняться с заданными параметрами и конфигурацией. Этот параметр удобно сначала показать, чтобы выходные данные можно было использовать в качестве ссылки для остальных примеров.

```shell {*}{maxHeight: '310px'}
$ pytest --collect-only

=================== test session starts ===================
collected 6 items
<Module 'test_one.py'>
  <Function 'test_passing'>
<Module 'test_two.py'>
  <Function 'test_failing'>
<Module 'tasks/test_four.py'>
  <Function 'test_asdict'>
  <Function 'test_replace'>
<Module 'tasks/test_three.py'>
  <Function 'test_defaults'>
  <Function 'test_member_access'>

============== no tests ran in 0.03 seconds ===============
```

---

# `pytest -k EXPRESSION`

Параметр `-k` позволяет использовать выражение для определения функций тестирования. Её можно использовать как ярлык для запуска отдельного теста, если имя уникально, или запустить набора тестов, которые имеют общий префикс или суффикс в их именах.

```shell
$ pytest -k "asdict or defaults" --collect-only

=================== test session starts ===================
collected 6 items
<Module 'tasks/test_four.py'>
  <Function 'test_asdict'>
<Module 'tasks/test_three.py'>
  <Function 'test_defaults'>

=================== 4 tests deselected ====================
============== 4 deselected in 0.03 seconds ===============
```

---

# `pytest -m MARKER`

```py
import pytest
...
@pytest.mark.run_these_please
def test_member_access():
    ...
```

```shell
pytest -v -m run_these_please

================== test session starts ===================
collected 4 items
test_four.py::test_replace PASSED
test_three.py::test_member_access PASSED

=================== 2 tests deselected ===================
========= 2 passed, 2 deselected in 0.02 seconds =========
```

---

# `pytest -s` / `pytest --capture=method`

Флаг `-s`, сокращенный вариант для `--capture=no`, позволяет печатать операторы — или любой другой вывод, который обычно печатается в `stdout`, чтобы фактически быть напечатаным в стандартном выводе во время выполнения тестов.

---

# `pytest`. Выбор тестов

````md magic-move
```shell
$ pytest
===================== test session starts ======================
collected 6 items
test_one.py .
test_two.py F
tasks/test_four.py ..
tasks/test_three.py ..
=========================== FAILURES ===========================
_________________________ test_failing _________________________
def test_failing():
>    assert (1, 2, 3) == (3, 2, 1)
E     assert (1, 2, 3) == (3, 2, 1)
E         At index 0 diff: 1 != 3
E         Use -v to get the full diff

test_two.py:2: AssertionError
============== 1 failed, 5 passed in 0.08 seconds ==============
```

```shell
$ pytest tasks/test_three.py tasks/test_four.py
===================== test session starts ======================
collected 4 items
tasks/test_three.py ..
tasks/test_four.py ..
=================== 4 passed in 0.02 seconds ===================
```

```shell
$ pytest tasks
===================== test session starts ======================
collected 4 items
tasks/test_four.py ..
tasks/test_three.py ..
=================== 4 passed in 0.03 seconds ===================
```

```shell
$ cd /tasks
$ pytest
===================== test session starts ======================
collected 4 items
test_four.py ..
test_three.py ..
=================== 4 passed in 0.02 seconds ===================
```

```shell
$ pytest -v tests/func/test_add.py::test_add_returns_valid_id
=========================== test session starts ===========================
collected 3 items
tests/func/test_add.py::test_add_returns_valid_id PASSED
======================== 1 passed in 0.02 seconds =========================
```

```shell
(venv33) pytest -v tests/func/test_api_exceptions.py::TestUpdate
============================= test session starts =============================

collected 2 items

tests\func\test_api_exceptions.py::TestUpdate::test_bad_id PASSED
tests\func\test_api_exceptions.py::TestUpdate::test_bad_task PASSED

========================== 2 passed in 0.12 seconds ===========================
```

```shell
$ pytest -v tests/func/test_api_exceptions.py::TestUpdate::test_bad_id
===================== test session starts ======================
collected 1 item
tests/func/test_api_exceptions.py::TestUpdate::test_bad_id PASSED
=================== 1 passed in 0.03 seconds ===================
```
````

---

# `pytest`. Имена тестов и файлов

- Тестовые файлы должны быть названы `test_<something>.py` или `<something>_test.py`.
- Методы и функции тестирования должны быть названы `test_<something>`.
- Тестовые классы должны быть названы `Test<Something>`.

---

# Оператор `assert`

```python
assert something
assert a == b
assert a != b
...
```

Если выражение будет вычисляться как `False`, когда оно будет преобразовано в `bool`, тест завершится с ошибкой.

`pytest` включает функцию, называемую _assert rewriting_, которая перехватывает _assert calls_ и заменяет их тем, что может рассказать вам больше о том, почему ваши утверждения не удались.

---

# Примеры тестовых функций

```python
def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }
```

---

# Exceptions

```python
import pytest

def test_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

`pytest.raises(ZeroDivisionError)`: оператор сообщает, что все, что находится в следующем блоке кода, должно вызвать исключение `ZeroDivisionError`. Если исключение не вызывается, тест завершается неудачей. Если тест вызывает другое исключение, он завершается неудачей.

---

```python
import pytest

def test_raises():
    with pytest.raises(ZeroDivisionError) as e:
        1 / 0
    assert str(e.value) == 'division by zero'
```

---

# `pytest.fixture`

`pytest.fixture` (фикстура) — это функции, выполняемые `pytest` до (а иногда и после) фактических тестовых функций. Код в фикстуре может делать все, что вам необходимо. Вы можете использовать `Fixtures`, чтобы получить набор данных для тестирования. Вы можете использовать `Fixtures`, чтобы получить систему в известном состоянии перед запуском теста. `Fixtures` также используются для получения данных для нескольких тестов.

---

# `pytest.fixture`

```python
import pytest

@pytest.fixture()
def some_data():
    """Return answer to ultimate question."""
    return 42

def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42
```

---

# `pytest.fixture`. Пример

````md magic-move
```python
def test_format_data_for_display():
    people = [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

    assert format_data_for_display(people) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]
```

```python
def test_format_data_for_excel():
    people = [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

    assert format_data_for_excel(people) == """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""
```

```python
import pytest

@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]
```

```python
import pytest

@pytest.fixture
def example_people_data(): ...

def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]

def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""
```
````

---

# `pytest.fixture`

Фикстуры - модульные, а значит их можно импортировать, они могут импортировать другие модули и они могут импортировать другие фикстуры и зависеть от них.

Фикстуры размещенные в файле `conftest.py` не нужно импортировать, но они будут доступны всем тестам.

---

# `pytest.fixture`. Спецификация областей (`Scope`)

- `scope='function'` - Выполняется один раз для каждой функции теста. Часть `setup` запускается перед каждым тестом с помощью `fixture`. Часть `teardown` запускается после каждого теста с использованием `fixture`. Это область используемая по умолчанию, если параметр `scope` не указан.
- `scope='class'` - Выполняется один раз для каждого тестового класса, независимо от количества тестовых методов в классе.
- `scope='module'` - Выполняется один раз для каждого модуля, независимо от того, сколько тестовых функций или методов или других фикстур при использовании модуля.
- `scope='session'` - Выполняется один раз за сеанс. Все методы и функции тестирования, использующие фикстуру области сеанса, используют один вызов `setup` и `teardown`.

---

# `pytest.fixture`. Спецификация областей (`Scope`)

```shell {*|20,7|8,19|9-14|15-18}{maxHeight: '420px'}
$ pytest --setup-show test_scope.py
============================= test session starts =============================

collected 4 items

test_scope.py
SETUP    S sess_scope
    SETUP    M mod_scope
        SETUP    F func_scope
        test_scope.py::test_1 (fixtures used: func_scope, mod_scope, sess_scope).
        TEARDOWN F func_scope
        SETUP    F func_scope
        test_scope.py::test_2 (fixtures used: func_scope, mod_scope, sess_scope).
        TEARDOWN F func_scope
      SETUP    C class_scope
        test_scope.py::TestSomething::()::test_3 (fixtures used: class_scope).
        test_scope.py::TestSomething::()::test_4 (fixtures used: class_scope).
      TEARDOWN C class_scope
    TEARDOWN M mod_scope
TEARDOWN S sess_scope

========================== 4 passed in 0.11 seconds ===========================
```

---

# `monkeypatch`

`monkeypatch` - встроенная фикстура `pytest`, позволяет изменять существующие объекты в процессе тестирования.

````md magic-move
```python
def calculate_sum(a: int | float, b: int | float) -> str:
    delay()
    return f"Sum of the 2 Numbers is `{a + b}`"


def delay():
    print("5 Sec Delay....")
    time.sleep(5)
```

```python
def calculate_sum(a: int | float, b: int | float) -> str: ...

def delay(): ...

def test_calculate_sum_no_monkeypatch() -> None:
    x = calculate_sum(2, 2)
    assert x == "Sum of the 2 Numbers is `4`"
```

```python
def calculate_sum(a: int | float, b: int | float) -> str: ...

def delay(): ...

def test_calculate_sum_w_monkeypatch(monkeypatch) -> None:
    def mock_return():
        return print("NO 5 Sec Delay!!!")

    monkeypatch.setattr("monkeypatch_examples.calculate_sum.delay", mock_return)

    x = calculate_sum(2, 2)
    assert x == "Sum of the 2 Numbers is `4`"
```
````

---

# `monkeypatch` - пример

````md magic-move
```python
base_url = "https://meowfacts.herokuapp.com/"


def get_cat_fact() -> tuple[int, dict] | str:
    try:
        response = requests.get(base_url)
        if response.status_code in (200, 201):
            return response.status_code, response.json()
        else:
            return json.dumps({"ERROR": "Cat Fact Not Available"})
    except requests.exceptions.HTTPError as errh:
        logging.error(errh)
    except requests.exceptions.ConnectionError as errc:
        logging.error(errc)
    except requests.exceptions.Timeout as errt:
        logging.error(errt)
    except requests.exceptions.RequestException as err:
        logging.error(err)
```

```python
def get_cat_fact() -> tuple[int, dict] | str: ...

def test_cat_fact_no_monkeypatch():
    code, response = get_cat_fact()
    assert code == 200
```


```python
def get_cat_fact() -> tuple[int, dict] | str: ...

def test_cat_fact_w_monkeypatch(monkeypatch):
    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
            self.url = "www.testurl.com"

        def json(self):
            return {'data': ['Mother cats teach their '
                             'kittens to use the litter box.']}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)
    assert get_cat_fact() == (200, {'data': ['Mother cats '
                                             'teach their kittens '
                                             'to use the litter box.']})
```
````
