import os

path = os.path.normpath("C:/Windows/Web")

print(path)

folder_name = "test_folder"

if os.path.isdir(folder_name):
    os.rmdir(folder_name)
else:
    os.mkdir(folder_name)


# чи є шлях абсолютним
print(os.path.isabs(path))
# чи це файл
print(os.path.isfile(path))
# чи це папка
print(os.path.isdir(path))
# чи це ярлик
print(os.path.islink(path))
