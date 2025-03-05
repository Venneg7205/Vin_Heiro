def find_spring_dates(filename):
    """
    Находит все весенние даты (март, апрель, май) в файле.
    Ожидает даты в формате DD.MM.YYYY.
    """
    spring_dates = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    day, month, year = map(int, line.split('.'))
                    if 3 <= month <= 5:
                        spring_dates.append(f"{day:02d}.{month:02d}.{year}")
                except ValueError:
                    print(f"Ошибка формата в строке: {line}")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    return spring_dates