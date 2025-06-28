with open("scratch_1.py" "r", encoding="utf-8") as file:
    for рядок in file:
        слово = рядок.strip()
        if слово.lower() == "стоп":
            print("Стоп — вихід із циклу.")
            break
        print("Слово з файлу:", слово)