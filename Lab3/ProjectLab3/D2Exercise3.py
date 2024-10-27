import re

def json_to_yaml(json_data):
    json_data= re.sub(r'"|{|}|,',r'',json_data) # Удаление ненужных символов: кавычек, фигурных скобок и запятых
    idlv = [] # Инициализация списка для уровней отступа
    non_empty_lines = [] # Инициализация списка для ненулевых строк
    adjusted_lines = [] # Инициализация списка для отрегулированных строк
    lines = json_data.split('\n')

    for line in lines:
        if line.strip():
            non_empty_lines.append(line)

    for line in non_empty_lines:
        indent_level = len(line) - len(line.lstrip())
        idlv.append(indent_level)
    idlv = sorted(set(idlv))

    for line in non_empty_lines:
        indent_level = len(line) - len(line.lstrip())
        for i in idlv:
            if indent_level == i:
                adjusted_line = '     ' * idlv.index(i) + line.lstrip()
                adjusted_lines.append(adjusted_line)
            else:
                continue
    return '\n'.join(adjusted_lines)

# Пример
json_text = '''{
    "timetable": {
        "subject1": 
            {
                "day": "Среда",
                "time": "13:30-15:00",
                "name": "Основы дискретной математики",
                "teacher": "Лисицына Любовь Сергеевна",
                "week": "четная",
                "location": "Кронверкский пр. д.49 лит.А",
                "room": "ауд. 2435/7",
                "format": "Очно - дистанционный"
            },
        "subject2": 
            {
                "day": "Среда",
                "time": "15:20-16:50",
                "name": "Основы профессиональной деятельности(Лаб)",
                "teacher": "Ткешелашвили Нино Мерабиевна",
                "week": "четная",
                "location": "Кронверкский пр. д.49 лит.А",
                "room": "ауд. 2308",
                "format": "Очно"
            }
    }
}
'''

yaml_data = json_to_yaml(json_text)
print(yaml_data)
