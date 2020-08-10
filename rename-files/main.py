import os

for file in os.listdir():
    name, extension = os.path.splitext(file)

    if extension != '.py':
        os.rename(file, f'{name.split(".")[3][-3:]}{extension}')
