import csv
import random as rd

with open('students.csv', 'w', encoding='windows-1251') as csv_file:
    fieldnames = ['student', 'variant']
    writer = csv.DictWriter(csv_file, fieldnames, delimiter=",",
                            lineterminator="\r")
    writer.writeheader()
    [writer.writerow(i) for i in (
        {'student': 'Шишкин Михаил Петрович', 'variant': rd.randint(1, 2)},
        {'student': 'Коновалов Никита Сергеевич', 'variant': rd.randint(1, 2)},
        {'student': 'Кузнецов Александр Александрович', 'variant': rd.randint(1, 2)},
        {'student': 'Васильев Александр Александрович', 'variant': rd.randint(1, 2)},
        {'student': 'Кузнецов Анастасий Соболевич', 'variant': rd.randint(1, 2)},
    )]
