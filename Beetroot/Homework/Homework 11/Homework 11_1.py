# 1


with open("myfile.txt", "w") as file:  # створення файлу
    file.write("Hello file world!\n")


with open("myfile.txt", "r") as file:  # читання файлу
    print(file.read())
