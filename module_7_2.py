# Задача "Записать и запомнить":

def custom_write(file_name, strings):
    file = open(file_name, "w", encoding='utf-8')
    strings_positions = {}
    for string in strings:
        position = file.tell()
        file.write(string + '\n')
        strings_positions[(strings.index(string) + 1, position)] = string
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
