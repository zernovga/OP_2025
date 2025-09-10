---
transition: slide-left
theme: sirius-college
exportFilename: pdf/op_lection_4
layout: cover
---

# Основы программирования<br>Лекция 4. 

Функции. Пространства имён и области видимости. Замыкания.  Генераторы. Декораторы. Обработка ошибок.

---

# Функции

Функции в Python определяются с помощью инструкции def, которое вводит определение функции. За ним должно следовать имя функции и заключенный в скобки список формальных параметров/аргументов. Операторы, которые формируют тело функции, начинаются со следующей строки и должны иметь отступ.cd

```python
def func_name(param):
    pass
```

- `func_name` - идентификатор, то есть переменная, которая при выполнении инструкции def связывается со значением в виде объекта функции.
- `param` - это необязательный список формальных параметров/аргументов, которые связываются со значениями, предоставляемыми при вызове функции.

---

# Функции

> Функция - объект, такой же как и прочие объекты в Python.

````md magic-move
```python
def hello(name):
    return f'Hello {name}.'

say = hello
```

```python
def hello(name):
    return f'Hello {name}.'

say = hello
say('World')
# Hello World.
```

```python
def hello(name):
    return f'Hello {name}.'

say = hello
del hello
hello('World')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'hello' is not defined
```

```python
def hello(name):
    return f'Hello {name}.'

say = hello
del hello
hello('World')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'hello' is not defined
say('World')
# 'Hello World.'
```

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a, b = 4, 5
(subtract if a > b else add)(a, b)
# 9

```
````

---

# Атрибуты функций

У объектов функций есть специальный атрибут `__dict__`. Это словарь атрибутов функции. В него можно устанавливать и получать какие-то значения с помощью точечной нотации.

````md magic-move
```python
def func():
    func.a = 10

func.__dict__
# {}
```

```python
def func():
    func.a = 10

func()
func.__dict__
# {'a': 10}
func.a
# 10
```

```python
def func():
    func.a = 10

func.a = 25
func.a
# 25
```

```python
def func():
    func.a = 10

func.x = 6
func.x
# 6
```

```python
def func():
    func.a = 10

func.list = []
func.list.append(10)
func.list.append(1)
func.list.append(5)
func.list
# [10, 1, 5]
func.__dict__
# {'a': 25, 'x': 6, 'list': [10, 1, 5]}
```
````

---

# Атрибуты функций

Словарь атрибутов может быть использован для кеширования промежуточных значений декоратора или для кэширования уже вычисленных значений функции. Например это может быть атрибут функции `func.cash`, который будет хранить словарь, у которого в качестве ключа будет кортеж входных параметров функции, а значение словаря - возвращаемый результат функции.

Атрибуты иногда используются как статические переменные для функции.

---

# Вложенные функции

```python
def parent():
    print('=> parent')
    def child():
        print("=> I'm child function")
    child()

parent()
# => parent
# => I'm child function
```

> **Важно:** внутренние функции не определены до тех пор, пока не будет вызвана родительская функция. Они локально ограничены родительской функцией `parent()`. Они существуют только внутри функции `parent()` как локальные переменные.

---

# Вложенные функции

```python
def talk(n):
    def hello(name):
        return f'Привет {name}.'
    def goodbye(name):
        return f'Пока {name}.'
    if n > 0:
        return hello
    else:
        return goodbye
```

> Функции могут не только принимать поведение через аргументы, но и могут возвращать поведение!

---

# Пространства имен, области видимости

- **Пространство имён** - это раздел, внутри которого имя уникально и не связано с такими же именами в других пространствах имён.
- Каждая функция определяет собственное пространство имён.
- Если вы определили переменную x в основной программе, а в функции также определили переменную x, они будут ссылаться на разные значения.
- В основной программе определяется **глобальное пространство имён**, поэтому переменные, находящиеся в нём, являются глобальными.

---

# Области видимости

```python {1|25-32|3-10|12-20|34-36}{maxHeight:'400px'}
from math import ceil # область встроенных имен

def sum_func():
    # локальная область видимости функции sum_func()
    b = a * 10 # 'b'
    # 'b' - локальная переменная функции sum_func()
    # НЕ доступна для ЧТЕНИЯ в глобальной области
    # Доступна для ЧТЕНИЯ в области видимости вложенной функции nested()
    # НЕ доступна для ИЗМЕНЕНИЯ в области видимости вложенной функции nested()
    # Здесь 'a' называется свободной переменной

    def nested():
        # локальная область видимости вложенной функции nested()
        z = b / 5 * a
        # 'z' - локальная переменная вложенной функции nested()
        # НЕ доступна для ЧТЕНИЯ в глобальной области
        # НЕ доступна для ЧТЕНИЯ в области видимости функции sum_func()
        # Здесь 'a' называется свободной переменной
        # Здесь 'b' называется нелокальной переменной
        return z

    return nested()


# Глобальная область видимости

a = 10
# 'a' - глобальная переменная
# Доступна для ЧТЕНИЯ в области видимости функции sum_func()
# Доступна для ЧТЕНИЯ в области видимости вложенной функции nested()
# НЕ доступна для ИЗМЕНЕНИЯ в области видимости функции sum_func()
# НЕ доступна для ИЗМЕНЕНИЯ в области видимости вложенной функции nested()

print(sum_func())
#  напечатает
200.0
```

---

# Области видимости. Оператор `global`

````md magic-move
```python
animal = 'cat'

def print_global():
    print('global variable animal: ', animal)

print_global()
# global variable animal: cat
```

```python
animal = 'cat'

def change_and_print_global():
    print('global variable animal: ', animal)

    animal = 'dog'

    print('after change: ', animal)

change_and_print_global()
# UnboundLocalError: cannot access local variable 'animal' where it is not
# associated with a value
```

```python
animal = 'cat'

def change_and_print_global():
    animal = 'dog'

    print('after change: ', animal)

change_and_print_global()
print('global variable animal: ', animal)
# after change: dog
# global variable animal: cat
```

```python
animal = 'cat'

def change_and_print_global():
    global animal
    animal = 'dog'

    print('after change: ', animal)

change_and_print_global()
print('global variable animal: ', animal)
# after change: dog
# global variable animal: dog
```
````

---

# Замыкания

**Замыкание (closure)** — это функция, которая запоминает значения из своей внешней области видимости, даже если эта область уже недоступна. Она создается, когда функция объявляется, и продолжает запоминать значения переменных даже после того, как вызывающая функция завершит свою работу.

Замыкания — это инструмент, который позволяет сохранять значения и состояние между вызовами функций, создавать функции на лету и возвращать их из других функций.

---

# Замыкания

````md magic-move
```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure(5))
# 15
```

```python
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

```python
def add_number(n):
    def inner(x):
        return x + n
    return inner

add_five = add_number(5)
add_ten = add_number(10)

print(add_five(3))  # 8
print(add_ten(3))   # 13
```

```py
def password_protected(password):
    def inner():
        if password == 'secret':
            print("Access granted")
        else:
            print("Access denied")
    return inner

login = password_protected('secret')
login()  # Access granted
```

```python
config = {
    'language': 'ru',
    'timezone': 'UTC'
}

def get_config(key):
    def inner():
        return config.get(key, None)
    return inner

get_language = get_config('language')
get_timezone = get_config('timezone')

print(get_language())  # ru
print(get_timezone())  # UTC
```
````
---

# Генераторы

Функция считается генератором, если:

- Содержит одно или несколько выражений `yield`.
- При вызове возвращает объект типа generator, но не начнет выполнение.
- Методы `__iter__()` и `__next__()` реализуются автоматически.
- После каждого вызова функция приостанавливается, а управление передается вызывающей стороне.
- Локальные переменные и их состояния запоминаются между последовательными вызовами.
- Когда вычисления заканчиваются по какому то условию, автоматически вызывается `StopIteration`.

---

# Генераторы

````md magic-move
```python {*|4|*}
def range_1(first=0, last=5, step=1):
    number = first
    while number < last:
        yield number
        number += step
```

```python
def range_1(first=0, last=5, step=1):
    number = first
    while number < last:
        yield number
        number += step


print(type(range_1))
# <class 'function'>
```

```python
def range_1(first=0, last=5, step=1):
    number = first
    while number < last:
        yield number
        number += step


print(type(range_1))
# <class 'function'>
ranger = range_1()
print(type(ranger))
# <class 'generator'>
```

```python
def range_1(first=0, last=5, step=1):
    number = first
    while number < last:
        yield number
        number += step


print(type(range_1))
# <class 'function'>
ranger = range_1()
print(type(ranger))
# <class 'generator'>
for i in ranger:
    print(i)
```
````

---

# Генераторы

````md magic-move
```python
def range_1(first=0, last=2, step=1):
    number = first
    while number < last:
        yield number
        number += step
```

```python
def range_1(first=0, last=2, step=1):
    number = first
    while number < last:
        yield number
        number += step

ranger = range_1()
print(next(ranger))
# 0
```

```python
def range_1(first=0, last=2, step=1):
    number = first
    while number < last:
        yield number
        number += step

ranger = range_1()
print(next(ranger))
print(next(ranger))
# 1
```

```python
def range_1(first=0, last=2, step=1):
    number = first
    while number < last:
        yield number
        number += step

ranger = range_1()
print(next(ranger))
print(next(ranger))
print(next(ranger))
# Traceback (most recent call last):
#   File "<stdin>", line 10, in <module>
#     print(next(ranger))
# StopIteration
```
````

---

# Генераторы. Примеры.

````md magic-move
```python
# Чтение большого файла
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
```

```python
# Чтение большого файла
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
```

```python
# Бесконечный генератор
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```
````

---

# Генераторные выражения (generator expressions, generator comprehensions)

````md magic-move
```py
nums_squared_lc = [num**2 for num in range(5)]
print(type(nums_squared_lc))
# <class 'list'>
```

```py
nums_squared_lc = [num**2 for num in range(5)]
print(type(nums_squared_lc))
# <class 'list'>
nums_squared_gc = (num**2 for num in range(5))
print(type(nums_squared_gc))
# <class 'generator'>
```
````

---

# Сравнение генераторов и списков

````md magic-move
```python
import sys


nums_squared_lc = [i ** 2 for i in range(10000)]
```

```python
import sys


nums_squared_lc = [i ** 2 for i in range(10000)]
sys.getsizeof(nums_squared_lc)
# 87624
```

```python
import sys


nums_squared_lc = [i ** 2 for i in range(10000)]
sys.getsizeof(nums_squared_lc)
# 87624
nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))
# 120
```

```python
import cProfile

cProfile.run('sum([i * 2 for i in range(10000)])')
```

```python {*|3-4|*}
import cProfile

cProfile.run('sum([i * 2 for i in range(10000)])')
#         5 function calls in 0.001 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.001    0.001    0.001    0.001 <string>:1(<listcomp>)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

```python {*|3-4,7-8|*}
import cProfile

cProfile.run('sum([i * 2 for i in range(10000)])')
#         5 function calls in 0.001 seconds
# ...

cProfile.run('sum((i * 2 for i in range(10000)))')
#         10005 function calls in 0.003 seconds
# ...
```
````

::block-component{v-click="10"}

> Генераторы хоть и дают существенное преимущество в объеме памяти, могут работать значительно медленнее, чем списки.

::

---

# Генераторы. Методы `.send()`, `.throw()`, `.close()`

````md magic-move
```python
def is_palindrome(num):
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False
```

```python {*|5|5-7}
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1
```

```python
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1

pal_gen = infinite_palindromes()
for i in pal_gen:
    digits = len(str(i))
    pal_gen.send(10 ** (digits))
```

```python
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1
```

```python {*|6}
pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.throw(ValueError("We don't like large palindromes"))
    pal_gen.send(10 ** (digits))
```

```python {*|6}
pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.close()
    pal_gen.send(10 ** (digits))
```
````

<v-switch at="1">

<template #2-4>

`i` принимает значение возвращаемое `yield`. Это позволяет изменять полученное значение. И, что важнее, позволяет отправлять (`.send()`) новое значение в генератор. Когда выполнение продолжается после `yield`, `i` получит отправленное значение.
</template>

<template #5-6>

Генератор `infinite_palindromes` является корутиной.

</template>

<template #7-8>

`.throw()` Создает исключение в точке, где генератор был приостановлен, и возвращает следующее значение, выданное функцией генератора . Если генератор завершает работу, не выдав другого значения, то возникает исключение StopIteration. Если функция генератора не улавливает переданное исключение или создает другое исключение, то это исключение распространяется на вызывающую сторону/программу.

</template>

<template #9-10>

Метод `.close()` прерывает выполнение генератора.

</template>

</v-switch>

---

# Декораторы

Вспомним, как работают функции:

<v-clicks>

- Функции являются объектами первого класса. Это означает, что функции можно передавать и использовать в качестве аргументов.
- Можно определить функции внутри других функций.
- Функции умеют возвращать другие функции в качестве результата.

</v-clicks>

---

# Декораторы

````md magic-move
```python {*|2-5|4|3,5|*}
def sample_decorator(func):
    def wrapper():
        print('Я родился...')
        func()
        print('Меня зовут Лунтик!')
    return wrapper
```

```python {*|11}
def sample_decorator(func):
    def wrapper():
        print('Я родился...')
        func()
        print('Меня зовут Лунтик!')
    return wrapper

def say():
    print('Привет Мир.')

say = sample_decorator(say)
```

```python {*|12-}
def sample_decorator(func):
    def wrapper():
        print('Я родился...')
        func()
        print('Меня зовут Лунтик!')
    return wrapper

def say():
    print('Привет Мир.')

say = sample_decorator(say)
say
# <function sample_decorator.<locals>.wrapper at 0x7f591a0a42f0>
```

```python
def sample_decorator(func):
    def wrapper():
        print('Я родился...')
        func()
        print('Меня зовут Лунтик!')
    return wrapper

def say():
    print('Привет Мир.')

say = sample_decorator(say)
say()
# Я родился...
# Привет Мир.
# Меня зовут Лунтик!
```

```python
def sample_decorator(func):
    def wrapper():
        print('Я родился...')
        func()
        print('Меня зовут Лунтик!')
    return wrapper

@sample_decorator
def say():
    print('Привет Мир.')

say
# <function sample_decorator.<locals>.wrapper at 0x789564722f20>
```
````

---
layout: statement
---

## Проще говоря: декораторы обертывают функцию, изменяя ее поведение.

---

# Декорирование функций с аргументами

````md magic-move
```python
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

```

```python
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def say_whee():
    print("Whee!")
```

```python
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def say_whee():
    print("Whee!")

say_whee()
# Whee!
# Whee!
```

```python
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")
```

```python
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")

greet(name="World")
# Traceback (most recent call last):
#   ...
# TypeError: wrapper_do_twice() takes 0 positional arguments but 1 was given
```

```python {*|2-4|*}
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")

greet("World")
# Hello World
# Hello World
```
````

---

# Возвращаемые значения из декорированных функций

````md magic-move
```python
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"
```

```python
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam = return_greeting("Adam")
# Creating greeting
# Creating greeting

print(hi_adam)
# None
```

```python {*|4|*}
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
```

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

return_greeting("Adam")
# Creating greeting
# Creating greeting
# 'Hi Adam'
```
````

---

# `@functools.wraps`

````md magic-move
```python
print
# <built-in function print>
print.__name__
# 'print'
help(print)
# Help on built-in function print in module builtins:
#
# print(...)
#     <full help message>
```

```python
say_whee
# <function do_twice.<locals>.wrapper_do_twice at 0x7f43700e52f0>
say_whee.__name__
# 'wrapper_do_twice'
help(say_whee)
# Help on function wrapper_do_twice in module decorators:
#
# wrapper_do_twice()
```

```python {*|1,4|*}
import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
```

```python
@do_twice
def say_whee():
    print("Whee!")


say_whee
# <function say_whee at 0x7ff79a60f2f0>
say_whee.__name__
# 'say_whee'
help(say_whee)
# Help on function say_whee in module whee:
#
# say_whee()
```
````

---

# Декораторы. Примеры

<v-switch>

<template #0>
Базовый шаблон декоратора:
</template>

<template #1-3>
Измерение времени выполнения:
</template>

<template #3-7>
Отладка:
</template>

<template #7>
Замедление времени выполнения:
</template>

<template #8>
Регистрация функций:
</template>

</v-switch>

````md magic-move {at:1}
```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
```

```python
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer
```

```python
import functools
import time

def timer(func): ...

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([number**2 for number in range(10_000)])

waste_some_time(1)
# Finished waste_some_time() in 0.0010 secs
waste_some_time(999)
# Finished waste_some_time() in 0.3260 secs
```

```python
def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}")
        return value
    return wrapper_debug
```

```python
@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you're growing up!"

make_greeting("Benjamin")
# Calling make_greeting('Benjamin')
# make_greeting() returned 'Howdy Benjamin!'
# 'Howdy Benjamin!'
```

```python
@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you're growing up!"

make_greeting("Juan", age=114)
# Calling make_greeting('Juan', age=114)
# make_greeting() returned 'Whoa Juan! 114 already, you're growing up!'
# 'Whoa Juan! 114 already, you're growing up!'
```

```python
@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you're growing up!"

make_greeting(name="Maria", age=116)
# Calling make_greeting(name='Maria', age=116)
# make_greeting() returned 'Whoa Maria! 116 already, you're growing up!'
# 'Whoa Maria! 116 already, you're growing up!'
```

```python
import functools
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down
```

```python
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func
```

```python
PLUGINS = dict()

def register(func): ...

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"

PLUGINS
# {'say_hello': <function say_hello at 0x7f768eae6730>,
#  'be_awesome': <function be_awesome at 0x7f768eae67b8>}
```
````

---

# Прочие возможности декораторов

````md magic-move
```python
@debug
@do_twice
def greet(name):
    print(f"Hello {name}")
```

```python
@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")


greet("World")
# Hello World
# Hello World
# Hello World
# Hello World
```

```python {*|4-7|2-4,8|1-2,9|*}
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat
```

```python
def name(_func=None, *, key1=value1, key2=value2, ...):
    def decorator_name(func):
        ...  # Create and return a wrapper function.

    if _func is None:
        return decorator_name
    else:
        return decorator_name(_func)
```

```python
def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)
```

```python
def repeat(_func=None, *, num_times=2): ...

@repeat
def say_whee():
    print("Whee!")

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")
```

```python
say_whee()
# Whee!
# Whee!

greet("Penny")
# Hello Penny
# Hello Penny
# Hello Penny
```

```python
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__}()")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls
```

```python
@count_calls
def say_whee():
    print("Whee!")

say_whee()
# Call 1 of say_whee()
# Whee!

say_whee()
# Call 2 of say_whee()
# Whee!

say_whee.num_calls
# 2
```
````

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
