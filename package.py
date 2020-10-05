import os, shutil, pathlib, fnmatch

dst = "G:/Fol/here" #импортирование файлов из src
src = "G:/резервныве копии с телефона/Huinya" #экспорт файлов

for dirnames in os.listdir(src):
    abs_path = os.path.join(src, dirnames) #путь к папкам, которые находятся в одной папке
    abs_path_listDir = os.listdir(abs_path)
    for i in abs_path_listDir:
        shutil.move(os.path.join(abs_path, i), os.path.join(dst, i))


