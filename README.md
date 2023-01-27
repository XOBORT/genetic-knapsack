# Evolutionary-genetic algorithm for solving the knapsack problem
This algorithm consists of:
  Encoding method:
    Discrete encoding (binary, integers).
  Methods of formation of the initial population:
    Random;
    Random with limitation control;
    Using greedy heuristics.
  The method of choosing a parent pair:
    Negative associative crossing.
  Crossover Operators:
    Single-point;
    Two-point;
    Multipoint.
  Mutation Operators:
    Gene:
      Point mutation.
    Macromutation:
      Saltation;
      Inversion;
      Translocation.
    Chromosomal:
      Addition.
    Strategy for the formation of the next generation:
      The strategy of overlapping generations.
    Selection Operator:
      β - tournament.
    Stop condition:
      On quantitative grounds. The dynamics of maximum fitness is determined:
        The maximum number of generations without improving the solution is determined.
    The way restrictions are handled:
      Decoder:
        Only items with a higher value are entered into the fitness (solution) (according to greedy methods), if the total weight is not violated, the original encoding (genotype) does not change.
File tt.py creates .xlsx file with the number of iterations of all possible combinations to make it clear that the minimum number of iterations to find the optimal solution depends on the randomness of the formation of the initial population.

# Эволюционно-генетический алгоритм для решения задачи о рюкзаке
Данный алгоритм состоит из:
  Способ кодирования: 
    Дискретное кодирование (бинарные, целые числа).
  Методы формирования начальной популяции:
    Случайный;
    Случайный с контролем ограничений;
    Использование жадных эвристик.
  Способ выбора родительской пары:
    Отрицательное ассоциативное скрещивание.
  Операторы кроссовера:
    Одноточечный;
    Двухточечный;
    Многоточечный.
  Операторы мутации:
    Генная:
      Точечная мутация.
    Макромутация:
      Сальтация;
      Инверсия;
      Транслокация.
    Хромосомная:
      Дополнение.
  Стратегия формирования следующего поколения:
    Стратегия перекрывающихся поколений.
  Оператор селекции:
    β - турнир.
  Условие остановки:
    По количественным признакам. Определяется динамика максимальной приспособленности:
      Определяется максимальное число поколений без улучшения решения.
  Способ обработки ограничений:
    Декодер:
      В приспособленность (решение) заносятся только предметы с большей ценностью (по жадным методам), если суммарный вес не нарушен, исходная кодировка (генотип) не изменяется.
Файл tt.py создает .xlsx файл с количеством итераций всех возможных комбинаций для наглядности того, что минимальное число итераций для поиска оптимального решения зависит от случайности формирования начальной популяции.
