# HW №1
import re
from pathlib import Path
from my_pack.style import *

# Функції модуля
def total_salary(path)->tuple:
    try:
        with open(path, 'r', encoding = 'utf-8') as fh:
            lines = fh.readlines()
        # обробка даних, отриманих з файлу
        emploeer_count = len(lines)
        total = 0
        average = 0
        p=r'[,]'
        for line in lines:
            line = re.sub(r'\n','',line)    # Видалення символу переносу строки
            line = re.split(p, line)        # Розбиття на елементи за заданим розділювачем
            total += int(line[1])
        average = total / emploeer_count
    except Exception as error:
        print_error(f'Error: {error}')
    
    return (total, average)

# ----------------------------------------------------
# Головна програма
def main():
    print_tytle('Загальна та середня ЗП працівників')
    data_dir = Path('data')
    data_file = Path('salary_file.txt')
    data_path = data_dir / data_file
    section_name ='Робота з базою даних:\n'+ data_path.__str__()
    print_section(section_name)
    
    total, average = total_salary(data_path)
    print(f'\
Загальна сума заробітної плати: {total}\n\
Середня заробітна плата: {average}')
    print_end('Кінець')
    
# ----------------------------------------------------   
# Точка входу
# print_serv_msg(f'Check: __name__ = {__name__}') # Перевірка коректності входу, для головного скрипта - "__main__"
if __name__ == '__main__':
    main()
else:
    print_error('Помилка виконання скрипта!')