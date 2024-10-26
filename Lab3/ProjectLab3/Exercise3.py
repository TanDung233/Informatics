def json_to_yaml(json_data, idlv=0):
    json_data=json_data.strip()
    yaml_str=""
    id='   ' *idlv # Создает отступы на основе текущего уровня вложенности
    pairs = []
    current_pair = ""
    bracket_count = 0 # Переменная для подсчета количества скобок

    if json_data.startswith('{') and json_data.endswith('}'):
        json_data=json_data[1:-1]
        for i in json_data:
            if i == '{':
                bracket_count += 1
            elif i == '}':
                bracket_count -= 1
            elif i == ',' and bracket_count == 0:
                pairs.append(current_pair.strip())
                current_pair = ""
                continue
            current_pair += i

        pairs.append(current_pair.strip())

        for pair in pairs:
            key_value = pair.split(':', 1)
            key = key_value[0].strip().strip('"')
            yaml_str +=f"{id}{key}: "
            value = key_value[1].strip().strip('"')
            if value.startswith('{') and value.endswith('}'):
                yaml_str += "\n" + json_to_yaml(value,idlv +1)
            else:
                yaml_str += f"{value}\n"
    return yaml_str

json_text ='''{
    "timetable": {
        "subject1" : 
            {
                "day" : "Среда",
                "time" : "13:30-15:00",
                "name" : "Основы дискретной математики",
                "teacher" : "Лисицына Любовь Сергеевна",
                "week" : "четная" ,
                "location" : "Кронверкский пр. д.49 лит.А",
                "room" : "ауд. 2435/7",
                "format" : "Очно - дистанционный"
            },
        "subject2" : 
            {
                "day" : "Среда",
                "time" : "15:20-16:50",
                "name" : "Основы профессиональной деятельности(Лаб)",
                "teacher" : "Ткешелашвили Нино Мерабиевна",
                "week" : "четная",
                "location" : "Кронверкский пр. д.49 лит.А",
                "room" : "ауд. 2308",
                "format" : "Очно"
            }
    }
}
'''

yaml_data = json_to_yaml(json_text)
print(yaml_data)
