import re

ukrainian_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
latin_alphabet = 'abcdefghijklmnopqrstuvwxyz'


def custom_sort(word):
    cleaned = word.lower()

    if cleaned and cleaned[0] in ukrainian_alphabet:
        alphabet = ukrainian_alphabet
        priority = 0
    else:
        alphabet = latin_alphabet
        priority = 1

    indexes = []

    for char in cleaned:
        if char in alphabet:
            indexes.append(alphabet.index(char))
        else:
            indexes.append(999)

    return priority, indexes


with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print('Початковий текст:\n')
print(text)

words = re.findall(r"[\w’'-]+", text, re.UNICODE)

sorted_words = sorted(words, key=custom_sort)

print('\nВідсортований список слів:\n')
print(sorted_words)