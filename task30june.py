
import re

# task1

# names = ['Aygun Kazimova', 'fermer Həsən', 'Namiq Qaracuxurlu', 'Rehim Rehimli', 'roya Ayxan', 'Eynulla']
# for name in names:
#     match = re.findall('[A-Z].* [A-Z]', name)
#     if match:
#         print(name)

# task3

# info = """Dünyada bir çox saytlar mövcuddur. Bunların bir çoxu fərqli məqsədlərə xidmət edirlər. 
# Müsal üçün http://www.google.com saytı axtarış üçün istifadə olunur. 
# Digər yandan https://facebook.com və http://www.instagram.com saytları sosial şəbəkə kimi fəaliyyət göstərirlər"""

# match2 = re.split('\s', info)
# new_list = []
# for word in match2:
#     match3 = re.match('[http]', word)
#     if match3:
#         new_list.append(word)
# print(new_list)

# task5

# numbers = """051-235-64-12, 055-236-642-23, 077-623-234-26, 51-125-646-32, 50-125-542-12, 70-253-644-12, 050-135-346-64"""
# number_list = re.split(', ', numbers)
# azercell_numbers = []
# for number in number_list:
#     match5 = re.match('^(05|5)[^5]', number)
#     if match5:
#         azercell_numbers.append(number)
# print(azercell_numbers)