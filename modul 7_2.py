def custom_write(file_name, strings):
    strings_positions = {}
    file_name = 'file_name.txt'
    file = open(file_name, 'w', encoding='utf-8')
    for s in strings:
        position = file.tell()
        file.write(s + '\n')
        # Возвращать словарь strings_positions,
        # где ключом будет кортеж (<номер строки>, <байт начала строки>),
        # а значением - записываемая строка.
        # Для получения номера байта начала строки используйте
        # метод tell() перед записью.
        strings_positions[len(strings_positions) + 1, position] = s
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
