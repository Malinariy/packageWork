import os, shutil
dst = *** #импортирование файлов из src
src = *** #экспорт файлов

for dirnames in os.listdir(src):
    abs_path = os.path.join(src, dirnames) #путь к папкам, которые находятся в одной папке
    for i in os.listdir(abs_path):
        shutil.move(os.path.join(abs_path, i), os.path.join(dst, i))
