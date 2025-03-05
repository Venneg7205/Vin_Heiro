def count_words_starting_with(filename, letter):
    """
    Подсчитывает количество слов в файле, начинающихся с заданной буквы.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            target_letter = letter.lower()
            count = 0
            for word in words:
                if len(word) > 0 and word[0].lower() == target_letter:
                    count += 1
            return count
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return 0