def countemojis(text):
    pattern ='X<{O'
    if (pattern in text):
        print(text.count(pattern))

# текста для проверки
text1 = "Hello world X<{O1234X<{O>"
text2 = "X<{OabcdX<{Oef"
text3 = "Здравствуйте! Я X<{O>"
text4 = "X<{OПривет! X<{OX<{O"
text5 = "X<{OBы такая красиваяX<{OX<{OX<{O"

#Ответы
countemojis(text1)
countemojis(text2)
countemojis(text3)
countemojis(text4)
countemojis(text5)
