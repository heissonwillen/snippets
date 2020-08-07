import os

for file in os.listdir():
    file_name, file_extension = os.path.splitext(file)

    if file_extension != '.py':
        new_name = f'{file_name.split(".")[3][-3:]}{file_extension}'

        # print(new_name)

        os.rename(file, new_name)
