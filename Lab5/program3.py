import json

students = {
    'Шевченко': ['Андрій', 'Петрович', 2003],
    'Коваленко': ['Марія', 'Іванівна', 2004],
    'Бондар': ['Олексій', 'Сергійович', 2002],
    'Ткаченко': ['Ірина', 'Володимирівна', 2005],
    'Мельник': ['Назар', 'Олегович', 2001],
    'Іваненко': ['Світлана', 'Михайлівна', 2000],
    'Петренко': ['Дмитро', 'Юрійович', 2003],
    'Савченко': ['Олена', 'Василівна', 2004],
    'Кравчук': ['Максим', 'Романович', 2002],
    'Візьонок': ['Дмитро', 'Олександрович', 2005]
}

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(students, file, ensure_ascii=False, indent=4)

print('Дані записані у файл data.json')

with open('data.json', 'r', encoding='utf-8') as file:
    loaded_students = json.load(file)

print('\nДані з JSON файлу:\n')

for surname, data in loaded_students.items():
    print(f'{surname}: {data[0]} {data[1]}, {data[2]} рік народження')