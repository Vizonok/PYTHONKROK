from urllib.parse import unquote
import pyperclip

url = input('Вставте закодоване посилання:\n')

decoded_url = unquote(url)

print('\nРозкодоване посилання:')
print(decoded_url)

pyperclip.copy(decoded_url)

print('\nПосилання скопійовано в буфер обміну.')