# Занятие 2.2. Работа с кодировками, русскими буквами
# https://github.com/vlk83/py-3_task_2.2

# Написать программу, которая будет выводить топ 10 самых часто
# встречающихся в новостях слов длиннее 6 символов для каждого файла.

# Не забываем про декомпозицию и организацию кода в функции.
# В решении домашнего задания вам могут помочь: split(), sort или sorted.

import json

def top_words_from_africa():
    
    with open('newsafr.json', 'r', encoding='utf8') as f1:
        newsafr = json.load(f1)

        # создаем список слов из всех description'ов
        all_descriptions_word_list = []
        for _ in newsafr["rss"]["channel"]["item"]:
            all_descriptions_word_list.extend( _ ["description"]["__cdata"].split())
        
        # создаем частотный словарь для всех слов длиннее 6 символов
        all_descriptions_word_dict = {}
        for word in all_descriptions_word_list:
            if len(word)>6:
                if word in all_descriptions_word_dict:
                    value = all_descriptions_word_dict[word]
                    all_descriptions_word_dict[word] = value + 1
                else:
                    all_descriptions_word_dict[word] = 1

        # выводим топ 10 слов и их частоту
        for value in sorted(set(all_descriptions_word_dict.values()), reverse=True)[:10]:
            for word in all_descriptions_word_dict.keys():
                if all_descriptions_word_dict[word] == value:
                    print (word, all_descriptions_word_dict[word])


