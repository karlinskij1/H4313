import os

print(os.sep)

path = "C:\Windows\Web"

for path, dirnames, filenames in os.walk(path):
    print(f'path - {path}')
    print(f'dirnames - {dirnames}')
    print(f"filenames - {filenames}\n")