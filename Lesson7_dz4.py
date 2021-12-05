# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках), размер которых не
# превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
#
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.


def size_stat(dir_p):
    dir_path = 'C:\Windows'
    size_dict = {100 * 10 ** i: 0 for i in range(7)}
    size_list = []

    print(dir_path)

    for iteam in os.scandir(str(dir_path)):
        if iteam.is_file():
            # print(iteam.name, iteam.stat().st_size, iteam.is_file())
            size_list.append(iteam.stat().st_size)
    size_list.sort()
    for el in size_list:
        if el < 100:
            size_dict[100] += 1


        elif 100 < el < 1000:
            size_dict[1000] += 1


        elif 1000 < el < 10000:
            size_dict[10000] += 1


        elif 10000 < el < 1000000:
            size_dict[100000] += 1


        elif 1000000 < el < 10000000:
            size_dict[10000000] += 1

    print(size_dict)


if __name__ == '__main__':
    import os
    import sys

    exit(size_stat(sys.argv))
