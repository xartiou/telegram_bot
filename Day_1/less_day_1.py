# Простейший Чат-бот, поздоровайтесь
# {Вопрос на входе} => {Алгоритм ответа} => {Ответ на выходе}
#
# Простейший алгоритм — это поиск по базе известных вопросов и ответов.

import random
import re
import nltk

text = input()
if text in ["Привет", "Здарова", "Хеллоу"]:
    print(random.choice(["Здрасте", "Йоу", "Приветики"]))
elif text in ["Пока", "Увидимся", "Чао"]:
    print(random.choice(["Буду ждать нашей встречи", "Ок", "Бай-бай"]))
else:
    print("Не понял")


# input = ввод данных от пользователя
# random.choice = выбор случайного элемента из списка
# print = вывод на экран

# Алгоритм ответа
# Если вопрос это что-то типа "Привет" или "Здарова" ну или там "Хеллоу"
# То ответить случайной фразой вроде "Йоу", "Приветики" или "Здрасте"
# Сложность — в том, чтобы сравнить Текст Пользователя и текст в программе.

# Задание
# Дописать функцию так, чтобы все примеры ниже работали
# Shift+ENTER!!


# Функция очищения текста
# "Привет!!!" => "привет"

def filter(text):
    text = text.lower()
    expression = r'[^\w\s]'  # Регулярное выражение = "Все что не слово и не пробел"
    return re.sub(expression, "", text)  # Substitute - заменить "Все что не слово и не пробел" на ""


# Функция text_match должна сравнивать текст пользователя с примером и решать похожи ли они
def text_match(user_text, example):
    # Убираем все лишнее
    user_text = filter(user_text)
    example = filter(example)

    # Если фраза содержится в другой
    if user_text.find(example) != -1:  # Если example найден внутри user_text
        return True

    if example.find(user_text) != -1:  # Если user_text найден внутри example
        return True

    example_length = len(example)  # Длина фразы example

    # На сколько (%) отличаются фразы
    difference = nltk.edit_distance(user_text, example) / example_length
    return difference < 0.4  # Если разница меньше 40%


# filter("ПриВеТ!!!")
#
# # Тексты совпадают
# text_match("Привет", "Привет")
#
# # Лишние символы ( regular expressions)
# text_match("Привет!!!", "Привет")
#
# # Регулярные выражение (RegExp / Регэкспы)
# # Инструмент для обработки строки
# # "Удалить в строке все знаки препинания" - например
#
# # Лишние слова ( find)
# text_match("Привет, как дела", "Привет")
#
# # Опечатки ( levenstein)
# text_match("Превет", "Привет")
#
# length = 6
# nltk.edit_distance("Превет", "Привед") / length

# *************************
# Определение намерения (intent) пользователя

# `{Вопрос на входе}` => `{Алгоритм ответа}` => `{Ответ на выходе}`

# Примеры вопросов => Выбирался нужный вопрос с помощью функции text_match => Выдать вариант ответа
# Интент = намерение пользователя = зачем он это спросил?

INTENTS = {
    "hello": {
        "examples": ["Привет", "Хеллоу", "Хай"],
        "response": ["Здрасте", "Йоу"],
    },
    "how-are-you": {
        "examples": ["Как дела", "Чем занят", "Чо по чем"],
        "response": ["Вроде ничего", "На чиле, на расслабоне"],
    },
}

# Записывать сколько угодно новых фраз
# Поместить в файл или в БД


INTENTS.keys()


# Определить намерение по тексту
# "Чем занят" => "how-are-you"
def get_intent(text):
    # Проверить все существующие intent'ы
    for intent_name in INTENTS.keys():
        examples = INTENTS[intent_name]["examples"]
        # Какой-нибудь один будет иметь example похожий на text
        # Проверить все examples
        for example in examples:
            if text_match(text, example):
                return intent_name


# "hello" => "Йоу"
# Берет случайны response для данного intent'а
def get_response(intent):
    return random.choice(INTENTS[intent]["response"])


def bot(text):
    intent = get_intent(text)  # Найти намерение
    if not intent:  # Если намерение не найдено
        print("Ничего не понятно")
    else:  # Если намерение найдено
        print(get_response(intent))


text = ""
while text != "Выход":
    text = input()
    bot(text)
