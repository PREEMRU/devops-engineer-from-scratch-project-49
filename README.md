# Игры разума

[![hexlet-check](https://github.com/PREEMRU/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/PREEMRU/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml)

Учебный проект Хекслета: пять консольных математических игр на Python.

В каждой игре необходимо правильно ответить на три вопроса подряд. После неправильного ответа игра завершается и показывает правильный ответ.

## Минимальные требования

* Python 3.12 или выше.
* Менеджер пакетов [uv](https://docs.astral.sh/uv/getting-started/installation/).
* Git для клонирования репозитория.
* Make — для использования сокращённых команд разработки (необязательно).

## Установка

Клонируйте репозиторий и перейдите в директорию проекта:

```bash
git clone https://github.com/PREEMRU/devops-engineer-from-scratch-project-49.git
cd devops-engineer-from-scratch-project-49
```

Установите зависимости и соберите пакет:

```bash
uv sync
uv build
```

Установите приложение:

```bash
uv tool install dist/*.whl
```

Если команды приложения не найдены, обновите настройки PATH:

```bash
uv tool update-shell
```

После этого перезапустите терминал.

## Запуск

После установки команды доступны из любой директории без `uv run`.

| Команда             | Описание                               |
| ------------------- | -------------------------------------- |
| `brain-games`       | Приветствие и знакомство с игроком     |
| `brain-even`        | Проверка числа на чётность             |
| `brain-calc`        | Вычисление значения выражения          |
| `brain-gcd`         | Нахождение наибольшего общего делителя |
| `brain-progression` | Поиск пропущенного числа в прогрессии  |
| `brain-prime`       | Проверка числа на простоту             |

Например, для запуска калькулятора:

```bash
brain-calc
```

Введите своё имя, затем отвечайте на вопросы игры.

## Правила игр и демонстрации

### Проверка на чётность

Ответьте `yes`, если показанное число чётное, и `no`, если нечётное.

```bash
brain-even
```

[![Демонстрация Brain Even](https://asciinema.org/a/u3qGV38LYREkBLMo.svg)](https://asciinema.org/a/u3qGV38LYREkBLMo)

### Калькулятор

Вычислите значение выражения и введите ответ. В игре используются сложение, вычитание и умножение.

```bash
brain-calc
```

[![Демонстрация Brain Calc](https://asciinema.org/a/Colx6AROnNtYBKil.svg)](https://asciinema.org/a/Colx6AROnNtYBKil)

### Наибольший общий делитель

Найдите наибольший общий делитель двух показанных чисел.

```bash
brain-gcd
```

[![Демонстрация Brain GCD](https://asciinema.org/a/rLOLPqosBfYm3wWj.svg)](https://asciinema.org/a/rLOLPqosBfYm3wWj)

### Арифметическая прогрессия

Найдите число, заменённое двумя точками `..`, и введите его.

```bash
brain-progression
```

[![Демонстрация Brain Progression](https://asciinema.org/a/CKOBVNDpNiCCQ7cz.svg)](https://asciinema.org/a/CKOBVNDpNiCCQ7cz)

### Простые числа

Ответьте `yes`, если число простое, и `no` в остальных случаях. Простое число — целое число больше единицы, имеющее ровно два положительных делителя: единицу и само себя.

```bash
brain-prime
```

[![Демонстрация Brain Prime](https://asciinema.org/a/j6l2AgRQ2xEquQ1w.svg)](https://asciinema.org/a/j6l2AgRQ2xEquQ1w)

## Разработка

Установка зависимостей:

```bash
make install
```

Проверка кода линтером Ruff:

```bash
make lint
```

Сборка пакета:

```bash
make build
```

Установка собранного пакета:

```bash
make package-install
```

Для запуска игры из исходного кода без установки через `uv tool install`:

```bash
uv run brain-calc
```

После изменения исходного кода для обновления установленного приложения:

```bash
uv build
uv tool install --force dist/*.whl
```

## Автоматическая проверка

При отправке изменений в GitHub запускается workflow `hexlet-check`.

Статус и результаты проверки доступны на вкладке [Actions](https://github.com/PREEMRU/devops-engineer-from-scratch-project-49/actions).
