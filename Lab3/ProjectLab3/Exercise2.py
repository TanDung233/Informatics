import re

def findVT_ITMO(text):
    pattern = r"\bВТ\b(?:\s+\w+){0,4}\s+\bИТМО\b" 
    matches = re.findall(pattern,text)
    return matches

# Пример текста для проверки
text1 = "Я буду изучать ВТ в ИТМО"
text2 = "Многие специалисты в области ВТ окончили ИТМО"
text3 = "Вы знаете, что ВТ такое? ВТ _ Это кафедра ИТМО"
text4 = "Ты знаешь, что ВТ _ лучший факультет в ИТМО"
text5 = "Первый ВТ тест ИТМО, а вот ещё ВТ пример другой тест ИТМО"

def output(text,result):
    print("Ввод:",text)
    print("Вывод:",result)

# Вывод результата
output(text1,findVT_ITMO(text1))
output(text2,findVT_ITMO(text2))
output(text3,findVT_ITMO(text3))
output(text4,findVT_ITMO(text4))
output(text5,findVT_ITMO(text5))
