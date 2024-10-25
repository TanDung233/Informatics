import re

def countemojis(text):
    pattern = r'X<{O'
    matches = re.findall(pattern, text)
    return len(matches)

# текста для проверки
text1 = "Hello world X<{O1234X<{O>"
text2 = "X<{OabcdX<{Oef"
text3 = "Здравствуйте! Я X<{O>"
text4 = "X<{OПривет! X<{OX<{O"
text5 = "X<{OBы такая красиваяX<{OX<{OX<{O"

#Ожиданные ответы
answer=[2,2,1,3,4]

# функция для проверки
def tocheck(texts_to_check, answer):
    for i in range(len(texts_to_check)):
        if answer[i] != countemojis(texts_to_check[i]):
            print(f"ERROR at text {i + 1}")
            return
    print("Successful")

#Ответы
print(countemojis(text1))
print(countemojis(text2))
print(countemojis(text3))
print(countemojis(text4))
print(countemojis(text5))

tocheck([text1, text2, text3, text4, text5], answer)
