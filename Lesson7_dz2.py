import json
import re
with open('config.json', 'r', encoding='utf-8') as f:
    #print(''.join(f.readlines()), end='')
    #print(f.readlines())
    dir_lvl1 =[]
    dir_lvl2 =[]
    dir_lvl3 =[]
    dir_lvl4 =[]
    dir_lvl5 =[]
    file_names = []
    for el in f.readlines():
        if el.count(' ') == 0 and el.count('.') ==0:
            print(type(el))
            dir_lvl1.append(el)
        elif el.count(' ') == 3 and el.count('.') ==0:
            dir_lvl2.append(el)
        elif el.count(' ') == 5 and el.count('.') ==0:
            dir_lvl3.append(el)
        elif el.count(' ') == 8 and el.count('.') ==0:
            dir_lvl4.append(el)
        elif el.count('.') != 0:
            file_names.append(el)

    print(dir_lvl1)
    print(dir_lvl2)
    print(dir_lvl3)
    print(dir_lvl4)
    print(dir_lvl5)