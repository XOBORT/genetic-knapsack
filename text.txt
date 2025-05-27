# Эволюционно-генетический алгоритм для задачи о рюкзаке

## Постановка задачи

Рассматривается классическая 0/1 задача о рюкзаке: имеется набор предметов, каждый из которых обладает весом и ценностью. Необходимо выбрать подмножество предметов так, чтобы их суммарная ценность была максимальной, а вес — не превышал заданный предел.

В отличие от точных методов, проект реализует приближённый подход с помощью эволюционно-генетического алгоритма (ЭГА).

## Методология

Алгоритм реализует типовой цикл ЭГА:

1. Генерация начальной популяции
2. Оценка приспособленности
3. Селекция родительских пар
4. Кроссовер
5. Мутация
6. Проверка ограничений
7. Запись результатов по поколениям
8. Сравнение с полным перебором (опционально)

## Реализация

Каждый этап оформлен как отдельный модуль. Код масштабируемый и легко поддерживается.

* `main.py` — управляющий сценарий
* `data.py` — параметры предметов и ограничения
* `data_recording.py` — запись логов поколений
* `complete_bust/` — полный перебор для сравнения
* `crossover/` — выбор и реализация операторов кроссовера
* `initial_population/` — методы генерации стартовых решений
* `mutation/` — выбор и применение мутаций
* `parent_couple/` — отбор родительских пар
* `processing_restrictions/` — обработка ограничений по весу
* `selection/` — механизмы селекции

## Пример параметров задачи

```python
items = [
    {'weight': 4, 'value': 10},
    {'weight': 2, 'value': 7},
    {'weight': 5, 'value': 13},
    # ...
]
MAX_WEIGHT = 15
POPULATION_SIZE = 30
NUM_GENERATIONS = 50
```

Каждое решение — бинарный вектор длины N, где `1` — предмет включён в рюкзак, `0` — нет.

## Результаты и анализ

Результаты сохраняются в Excel (`50_GENERATIONS_N.xlsx`) — можно анализировать прогресс по поколениям:

* средняя и максимальная приспособленность
* сходимость популяции
* поведение оператора мутации и отбора

Для верификации добавлен модуль полного перебора (`complete_bust`).

## Стек технологий

* Python 3
* Pandas, openpyxl (логирование)
* Стандартные библиотеки: `random`, `math`, `os`, `typing`

## Структура проекта

```
EGA_DATA_RECORDING/
├── main.py
├── data.py
├── data_recording.py
├── complete_bust/
│   ├── complete_bust.py
│   └── full_list.py
├── crossover/
│   ├── choosing_crossover.py
│   └── crossover_operators.py
├── initial_population/
│   ├── choosing_init_popul.py
│   └── methods_creating_initial_population.py
├── mutation/
│   ├── choosing_mutation.py
│   └── mutation_operators.py
├── parent_couple/
│   └── methods_pair_selection.py
├── processing_restrictions/
│   └── ways_restrictions_processing.py
├── selection/
│   └── selection_operators.py
├── *.xlsx (результаты по поколениям)
```

## Контакты

* Telegram: \[[https://t.me/Xobortz](https://t.me/Xobortz)]
* Email: \[[genaj.2000@yandex.ru](mailto:genaj.2000@yandex.ru)]
* Профиль: [https://github.com/XOBORT](https://github.com/XOBORT)
