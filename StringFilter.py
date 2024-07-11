def filter_short_strings(strings):
    result = []
    for string in strings:
        if len(string) <= 3:
            result.append(string)
    return result

def main():
    # Пример массива строк
    input_strings = ["Hello", "2", "world", ":-)"]
    
    # Фильтрация строк
    filtered_strings = filter_short_strings(input_strings)
    
    # Вывод результата
    print("Исходный массив:", input_strings)
    print("Отфильтрованный массив:", filtered_strings)

if __name__ == "__main__":
    main()
