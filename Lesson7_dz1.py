# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
#


def start_proj(file_path, proj_name='my_project', argv=['settings', 'mainapp', 'adminapp', 'authapp']):
    start_path, *args = argv
    ROOT = './'

    if not os.path.exists(proj_name):
        os.mkdir(os.path.join(ROOT, str(proj_name)))

    path_dirs = os.path.join(ROOT, proj_name)

    for dir1 in argv:
        print(dir1)
        print(path_dirs)
        print(not os.path.exists(path_dirs))

        if not os.path.exists(os.path.join(path_dirs, dir1)):
            os.mkdir(os.path.join(path_dirs, dir1))
            print('создана')
        else:
            to_do = (input(r'Папка уже еcть. Удалить? (y\n)'))
            if to_do == 'y':
                os.rmdir(os.path.join(path_dirs, dir1))
                print('удалена')
                continue
            elif to_do == 'n':
                continue
    print(*os.walk(path_dirs))


if __name__ == '__main__':
    import os
    import sys

    exit(start_proj(sys.argv))
