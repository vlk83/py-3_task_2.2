# Занятие 2.2. Работа с кодировками, русскими буквами

import json

def top_words_from_africa():
    
    with open('newsafr.json', 'r', encoding='utf8') as f:
        news = json.load(f)

        # создаем список слов из всех description'ов
        all_descriptions_word_list = []
        for _ in news["rss"]["channel"]["item"]:
            all_descriptions_word_list.extend( _ ["description"]["__cdata"].split())
        
        # создаем частотный словарь для всех слов длиннее 6 символов
        all_descriptions_word_dict = {}
        for word in all_descriptions_word_list:
            if len(word)>6 and word.isalpha():
                if word in all_descriptions_word_dict:
                    value = all_descriptions_word_dict[word]
                    all_descriptions_word_dict[word] = value + 1
                else:
                    all_descriptions_word_dict[word] = 1

        print('------------------------------------------------')
        print('топ 10 слов в файле newsafr.json и их частота:\n')
        
        # выводим топ 10 слов и их частоту
        for value in sorted(set(all_descriptions_word_dict.values()), reverse=True)[:10]:
            for word in all_descriptions_word_dict.keys():
                if all_descriptions_word_dict[word] == value:
                    print (word, all_descriptions_word_dict[word])



def top_words_from_cyprus():
    
    with open('newscy.json', 'r', encoding='koi8-r') as f:
        news = json.load(f)

        # создаем список слов из всех description'ов
        all_descriptions_word_list = []
        for _ in news["rss"]["channel"]["item"]:
            all_descriptions_word_list.extend( _ ["description"]["__cdata"].split())
        
        # создаем частотный словарь для всех слов длиннее 6 символов
        all_descriptions_word_dict = {}
        for word in all_descriptions_word_list:
            if len(word)>6 and word.isalpha():
                if word in all_descriptions_word_dict:
                    value = all_descriptions_word_dict[word]
                    all_descriptions_word_dict[word] = value + 1
                else:
                    all_descriptions_word_dict[word] = 1

        print('-----------------------------------------------')
        print('топ 10 слов в файле newscy.json и их частота:\n')

        # выводим топ 10 слов и их частоту
        for value in sorted(set(all_descriptions_word_dict.values()), reverse=True)[:10]:
            for word in all_descriptions_word_dict.keys():
                if all_descriptions_word_dict[word] == value:
                    print (word, all_descriptions_word_dict[word])

def top_words_from_italy():
    
    with open('newsit.json', 'r', encoding='cp1251') as f:
        news = json.load(f)

        # создаем список слов из всех description'ов
        all_descriptions_word_list = []
        for _ in news["rss"]["channel"]["item"]:
            all_descriptions_word_list.extend( _ ["description"].split())
        
        # создаем частотный словарь для всех слов длиннее 6 символов
        all_descriptions_word_dict = {}
        for word in all_descriptions_word_list:
            if len(word)>6 and word.isalpha():
                if word in all_descriptions_word_dict:
                    value = all_descriptions_word_dict[word]
                    all_descriptions_word_dict[word] = value + 1
                else:
                    all_descriptions_word_dict[word] = 1

        print('-----------------------------------------------')
        print('топ 10 слов в файле newsit.json и их частота:\n')

        # выводим топ 10 слов и их частоту
        for value in sorted(set(all_descriptions_word_dict.values()), reverse=True)[:10]:
            for word in all_descriptions_word_dict.keys():
                if all_descriptions_word_dict[word] == value:
                    print (word, all_descriptions_word_dict[word])


top_words_from_africa()
top_words_from_cyprus()
top_words_from_italy()
