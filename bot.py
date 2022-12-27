import telebot

bot = telebot.TeleBot("5863278624:AAFW5zXpffCSA9qSpAhVUMf0TG3Huq3o4iM")


@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет,<b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b> \n" \
           f"Я помощник по твоему обучению я.п. Python. И мой создатель развивает меня в этом направлении."
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["help"])
def help(message):
    mess = f"Привет,<b>{message.from_user.first_name}</b> " \
           f"На данный момент я знаю, что такое: " \
           f"\n if-elif-else\n While \n break \n continue \n Range\n For \n Вложенные циклы \n" \
           f"Словари\n Кортежи\n Списки\n Строки\n Множества\n Типы данных\n Работа с файлами\n Исключения\n" \
           f"def(функции)\n Рекурсия\n *args\n **kwargs\n enumerate() \n List comprehension\n lambda функции\n map " \
           f"\n Замыкания\n  Декораторы \n Модули и пакеты \n Виртуальные окружения \n Установка пакетов в python\n" \
           f"JSON данные \n CLI \n Переменные окружения \n Pathlib \n Работа с SQlite3 в Python \n pep8 \n Срезы \n " \
           f"<b>Я помогу тебе. Для этого введи одно из вышеперечисленных слов или словосочетаний. И я вспомогательный " \
           f"материал.</b> "
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["help2"])
def help2(message):
    mess = f"Привет,<b>{message.from_user.first_name}</b>\n" \
           f"У меня есть ещё пара команд: Методички, Задания, Методичка (её номер) "
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello" or message.text == "Привет":
        bot.send_message(message.chat.id, "И тебе привет!", parse_mode="html")
    elif message.text == "Отдохнуть бы!":
        bot.send_message(message.chat.id, f"Послушай и отдохни\n", parse_mode="html")
        bot.send_audio(message.chat.id, open(r"c:/Users/admin/downloads/Nirvana.mp3", "rb"))
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode="html")
    elif message.text == "Срезы":
        bot.send_message(message.chat.id,
                         "Изучай: https://habr.com/ru/post/587282/ \n "
                         "Ещё ссылка: https://proproprogs.ru/python_base/spiski-srezy-i-metody \n ", parse_mode="html")
    elif message.text == "pep8" or message.text == "Pep8":
        bot.send_message(message.chat.id,
                         "Изучай: https://python-scripts.com/pathlib \n Ссылка на видео: https://www.youtube.com/watch?v=pAJO25vJneQ \n "
                         "Ещё видео: https://www.youtube.com/watch?v=qBSYKHXVgf0 ", parse_mode="html")
    elif message.text == "Работа с SQlite3 в Python" or message.text == "SQlite3":
        bot.send_message(message.chat.id,
                         "Изучай: https://python-scripts.com/pathlib \n Ссылка на видео: https://www.youtube.com/watch?v=K1C5JAo7cMU \n "
                         "Часть 2: https://www.youtube.com/watch?v=gm0p517EG7o \n "
                         "Ещё видео: https://www.youtube.com/watch?v=fs7xrH2975U ", parse_mode="html")
    elif message.text == "Pathlib" or message.text == "pathlib":
        bot.send_message(message.chat.id,
                         "Изучай: https://python-scripts.com/pathlib \n Ссылка на видео: https://www.youtube.com/watch?v=wZvk8nyPQCY \n "
                         "Ещё видео: https://www.youtube.com/watch?v=DOgjN7RmHds", parse_mode="html")
    elif message.text == "Переменные окружения":
        bot.send_message(message.chat.id,
                         "Изучай: https://lumpics.ru/environment-variables-in-windows-10/ \n "
                         "Ссылка на видео: https://www.youtube.com/watch?v=L9-I4NibguY \n ", parse_mode="html")
    elif message.text == "CLI" or message.text == "Интерфейс командной строки":
        bot.send_message(message.chat.id,
                         "Изучай: https://tproger.ru/translations/python-command-line-tools-with-click/ \n "
                         "Ссылка на видео: https://www.youtube.com/watch?v=vm9tOamPkeQ \n ", parse_mode="html")
    elif message.text == "JSON данные" or message.text == "JSON":
        bot.send_message(message.chat.id,
                         "Изучай: https://dvmn.org/encyclopedia/modules/json/ \n Ссылка на видео: https://www.youtube.com/watch?v=rIhygmw9HZM \n "
                         "Ещё видео: https://www.youtube.com/watch?v=3xaN1tDdkF4", parse_mode="html")
    elif message.text == "Установка пакетов в Python" or message.text == "Виртуальные окружения":
        bot.send_message(message.chat.id,
                         "Изучай: https://habr.com/ru/post/491916/ \n Ссылка на видео: https://www.youtube.com/watch?v=xSsKtIiUaOY \n "
                         "Ещё видео: https://www.youtube.com/watch?v=rsG1Y5k-9jo", parse_mode="html")
    elif message.text == "Декораторы" or message.text == "Wraps":
        bot.send_message(message.chat.id,
                         "Изучай: https://dev-gang.ru/article/ljambdafunkcija-v-python-fe2p8vf789/ \n Ссылка на видео: https://www.youtube.com/watch?v=Va-ovLxHmus \n "
                         "Часть 2: https://www.youtube.com/watch?v=tj8EiBK8TeA", parse_mode="html")
    elif message.text == "Модули и пакеты" or message.text == " __init__":
        bot.send_message(message.chat.id,
                         "Изучай: https://devpractice.ru/python-lesson-13-modules-and-packages/ \n "
                         "Ссылка на видео: https://www.youtube.com/watch?v=VCRxOdCueqM ", parse_mode="html")
    elif message.text == "Замыкания" or message.text == "Closure":
        bot.send_message(message.chat.id,
                         "Изучай: https://advpyneng.readthedocs.io/ru/latest/book/07_closure/closure.html \n "
                         "Ссылка на видео: https://www.youtube.com/watch?v=lA979PBb0TY ", parse_mode="html")
    elif message.text == "Функция map" or message.text == "map":
        bot.send_message(message.chat.id,
                         "Изучай: https://egoroffartem.pythonanywhere.com/course/python/funktsiya-map-python \n "
                         "Ссылка на видео: https://www.youtube.com/watch?v=2ghKShXWuSs ", parse_mode="html")
    elif message.text == "lambda" or message.text == "lambda функции":
        bot.send_message(message.chat.id,
                         "Изучай: https://dev-gang.ru/article/ljambdafunkcija-v-python-fe2p8vf789/ \n "
                         "Ссылка на видео: https://www.youtube.com/watch?v=8fzrm1tX5lI ", parse_mode="html")
    elif message.text == "List comprehension" or message.text == "Списковые включения":
        bot.send_message(message.chat.id,
                         "Изучай: https://egoroffartem.pythonanywhere.com/course/python/generatori-spiskov-python-list-comprehension \n Ссылка на видео: https://www.youtube.com/watch?v=_zBTBr6XdZo \n"
                         "Часть 2: https://www.youtube.com/watch?v=_RA35zG-0gA \n "
                         "Часть 3: https://www.youtube.com/watch?v=vn6bV6BYm7w", parse_mode="html")
    elif message.text == "enumerate()" or message.text == "enumerate":
        bot.send_message(message.chat.id,
                         "Изучай: https://proproprogs.ru/python_base/funkciya-enumerate-primery-ispolzovaniya \n "
                         "Ссылка на видео: https://www.youtube.com/watch?v=Hz1lDs69cCs ", parse_mode="html")
    elif message.text == "*args" or message.text == "**kwargs":
        bot.send_message(message.chat.id,
                         "Изучай: https://pavel-karateev.gitbook.io/intermediate-python/sintaksis/args_and_kwargs \n "
                         "Ссылка на видео: https://www.youtube.com/watch?v=mcAB5dBXMp4 ", parse_mode="html")
    elif message.text == "Рекурсия" or message.text == "рекурсивные вызовы":
        bot.send_message(message.chat.id,
                         "Изучай: https://pythontutor.ru/lessons/functions/ \n "
                         "Ссылка на видео: https://www.youtube.com/watch?v=jvFULnNpNLg \n"
                         "Часть 2: https://www.youtube.com/watch?v=rzGCxtZdMuM ", parse_mode="html")
    elif message.text == "def(функции)" or message.text == "def" or message.text == "Функции":
        bot.send_message(message.chat.id,
                         "Изучай: https://pythonworld.ru/tipy-dannyx-v-python/vse-o-funkciyax-i-ix-argumentax.html \n "
                         "Ссылка на видео: https://www.youtube.com/watch?v=DJAlfolEv9A", parse_mode="html")
    elif message.text == "if-elif-else" or message.text == "проверка истинности" or message.text == "if/else":
        bot.send_message(message.chat.id,
                         "Изучай: https://pythonworld.ru/osnovy/instrukciya-if-elif-else-proverka-istinnosti-trexmestnoe-vyrazhenie-ifelse.html"
                         "\n Ссылка на видео: https://www.youtube.com/watch?v=EggJRTzid1M\n "
                         "Часть 2: https://www.youtube.com/watch?v=8YshxYHIeeI \n "
                         "Часть 3: https://www.youtube.com/watch?v=8F-EfhsKHCI", parse_mode="html")
    elif message.text == "While" or message.text == "break" or message.text == "continue":
        bot.send_message(message.chat.id,
                         "Изучай: https://www.youtube.com/watch?v=Ll3AN1FXXfE \n "
                         "Часть 2: https://www.youtube.com/watch?v=Myh7OdxoYsA", parse_mode="html")
    elif message.text == "Range" or message.text == "Функция range":
        bot.send_message(message.chat.id, "Ссылка на видео: https://www.youtube.com/watch?v=9J0fvF4k4F4",
                         parse_mode="html")
    elif message.text == "Вложенные циклы Python":
        bot.send_message(message.chat.id, "Ссылка на видео: https://www.youtube.com/watch?v=tsVgSwSdsa8",
                         parse_mode="html")
    elif message.text == "For" or message.text == "Цикл for":
        bot.send_message(message.chat.id, "Изучай: https://www.youtube.com/watch?v=iopPsTT7Pes", parse_mode="html")
    elif message.text == "Кортежи" or message.text == "кортежи" or message.text == "кортеж":
        bot.send_message(message.chat.id,
                         "Изучай: https://pythonworld.ru/tipy-dannyx-v-python/kortezhi-tuple.html" "Ссылка на видео:",
                         parse_mode="html")
    elif message.text == "Словари" or message.text == "Словарь" or message.text == "словарь":
        bot.send_message(message.chat.id,
                         "Изучай: https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html \n" 
                         "Ссылка на видео: https://www.youtube.com/watch?v=7_Zrh1--d5o", parse_mode="html")
    elif message.text == "Лист" or message.text == "Список" or message.text == "Списки":
        bot.send_message(message.chat.id,
                         "Изучай: https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html \n" 
                         "Ссылка на видео: https://www.youtube.com/watch?v=CEQZYZMPJSU", parse_mode="html")
    elif message.text == "Строки" or message.text == "Функции и методы строк":
        bot.send_message(message.chat.id,
                         "Изучай: https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html \n" 
                         "Ссылка на видео: https://www.youtube.com/watch?v=GmMD6gQYWe4", parse_mode="html")
    elif message.text == "Множества" or message.text == "set" or message.text == "frozenset":
        bot.send_message(message.chat.id,
                         "Изучай: https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html \n" 
                         "Ссылка на видео: https://www.youtube.com/watch?v=KMGRXDxUw18", parse_mode="html")
    elif message.text == "Типы данных" or message.text == "Тип данных питон":
        bot.send_message(message.chat.id,
                         "Изучай: https://pythonworld.ru/tipy-dannyx-v-python/chisla-int-float-complex.html \n" 
                         "Ссылка на видео: https://www.youtube.com/watch?v=DZvNZ9l9NT4", parse_mode="html")
    elif message.text == "Работа с файлами" or message.text == "файлы" or message.text == "Файлы":
        bot.send_message(message.chat.id,
                         "Изучай: https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html \n" 
                         "Ссылка на видео: https://www.youtube.com/watch?v=oRr_bEXJbV0", parse_mode="html")
    elif message.text == "Исключения" or message.text == "try" or message.text == "expect":
        bot.send_message(message.chat.id,
                         "Изучай: https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html \n" 
                         "Ссылка на видео: https://www.youtube.com/watch?v=qjqbek5tG3A", parse_mode="html")
    elif message.text == "Я Виталий Горшков" or message.text == "я Горшков" or message.text == "Я Горшков":
        bot.send_message(message.chat.id, "<b>ВИТАЛИК, ИДИ БЫСТРО УЧИСЬ И НЕ ЛЕНИСЬ!</b>", parse_mode="html")
    elif message.text == "Методичка 15" or message.text == "Задание 15" or message.text == "Методичка 2.20":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.20 (15).pdf", "rb"), )
    elif message.text == "Методичка 14" or message.text == "Задание 14" or message.text == "Методичка 2.19":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.19 (14).pdf", "rb"))
    elif message.text == "Методичка 13" or message.text == "Задание 13" or message.text == "Методичка 2.18":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.18 (13).pdf", "rb"))
    elif message.text == "Методичка 12" or message.text == "Задание 12" or message.text == "Методичка 2.17":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.17 (12).pdf", "rb"))
    elif message.text == "Методичка 11" or message.text == "Задание 11" or message.text == "Методичка 2.16":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.16 (11).pdf", "rb"))
    elif message.text == "Методичка 10" or message.text == "Задание 10" or message.text == "Методичка 2.15":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.15 (10).pdf", "rb"))
    elif message.text == "Методичка 9" or message.text == "Задание 9" or message.text == "Методичка 2.14":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.14 (9).pdf", "rb"))
    elif message.text == "Методичка 8" or message.text == "Задание 8" or message.text == "Методичка 2.13":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.13 (8).pdf", "rb"))
    elif message.text == "Методичка 7" or message.text == "Задание 7" or message.text == "Методичка 2.12":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.12 (7).pdf", "rb"))
    elif message.text == "Методичка 6" or message.text == "Задание 6" or message.text == "Методичка 2.11":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.11 (6).pdf", "rb"))
    elif message.text == "Методичка 5" or message.text == "Задание 5" or message.text == "Методичка 2.10":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.10 (5).pdf", "rb"))
    elif message.text == "Методичка 4" or message.text == "Задание 4" or message.text == "Методичка 2.9":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.9 (4).pdf", "rb"))
    elif message.text == "Методичка 3" or message.text == "Задание 3" or message.text == "Методичка 2.8":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.8 (3).pdf", "rb"))
    elif message.text == "Методичка 2" or message.text == "Задание 2" or message.text == "Методичка 2.7":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.7 (2).pdf", "rb"))
    elif message.text == "Методичка 1" or message.text == "Задание 1" or message.text == "Методичка 2.6":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.6 (1).pdf", "rb"))
    elif message.text == "Методички" or message.text == "Задания":
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.20 (15).pdf", "rb"))
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.19 (14).pdf", "rb"))
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.18 (13).pdf", "rb"))
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.17 (12).pdf", "rb"))
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.16 (11).pdf", "rb"))
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.15 (10).pdf", "rb"))
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.14 (9).pdf", "rb"))
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.13 (8).pdf", "rb"))
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.12 (7).pdf", "rb"))
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.11 (6).pdf", "rb"))
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.10 (5).pdf", "rb"))
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.9 (4).pdf", "rb"))
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.8 (3).pdf", "rb"))
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.7 (2).pdf", "rb"))
        bot.send_document(message.chat.id, document=open("c:/Users/admin/downloads/labs/2.6 (1).pdf", "rb"))

    else:
        bot.send_message(message.chat.id,
                         "Извини, я тебя не понимаю. Напиши, пожалуйста, /help или /help2, для отображения моего "
                         "функционала.",
                         parse_mode="html")


bot.polling(none_stop=True)
