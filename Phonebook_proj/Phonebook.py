import os
import json
import sys

# ЗАВАНТАЖУЮ ФАЙЛ
def load_phonebook(filename='contacts.json'):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл '{filename}' не знайдено.")
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_phonebook(contacts, filename='contacts.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)

# ДОДАВАННЯ КОНТАКТУ
def add_contact(contacts):
    number = input('Номер телефону: ').strip()
    if not number:
        print("Порожній ввід")
        return

    if number in contacts:
        print('Такий номер уже існує!')
        return
    contacts[number] = {
        "first_name": input("Ім'я: ").strip(),
        "last_name": input("Прізвище: ").strip(),
        "city": input("Місто: ").strip(),
        "state": input("Область: ").strip()
    }
    print("Запис додано.")

# ВИДАЛЕННЯ КОНТАКТУ
def delete_contact(contacts):
    number = input(
        "Введи номер телефону для видалення (або натисни Enter, щоб шукати за ім’ям/прізвищем): "
    ).strip().lower()

    if number:
        if number in contacts:
            approve = input("Дійсно видалити цей контакт? (введи так або ні): ").strip().lower()
            if approve == "так":
                del contacts[number]
                print("Контакт видалено")
            else:
                print("Видалення контакту не відбулось")
        else:
            print("Контакт не знайдений")
        return

    first = input("Ім’я (можна лишити порожнім): ").strip().lower()
    second = input("Прізвище (можна лишити порожнім): ").strip().lower()

    found = []
    for num, data in contacts.items():
        if (not first or first in data['first_name'].lower()) and (not second or second in data['last_name'].lower()):
            found.append((num, data))

    if not found:
        print("Таких не знайдено")
        return

    for index_in_list, (number, data) in enumerate(found, start=1):
        print(f"\n{index_in_list}. {number} {data['first_name']} {data['last_name']}")

    choice = input("Введи номер контакту або індекс для видалення (або 'ні' для скасування): ").strip().lower()

    if choice == "ні":
        print("Видалення скасовано")
        return

    if choice.isdigit():
        index_in_list = int(choice) - 1
        if 0 <= index_in_list < len(found):
            number_to_delete = found[index_in_list][0]
            del contacts[number_to_delete]
            print("Обране видалене")
        else:
            print("Некоректний вибір")
    elif choice in contacts:
        del contacts[choice]
        print("Обране видалене")
    else:
        print("Недійсний ввід")


# ОНОВЛЕННЯ КОНТАКТУ
def update_contact(contacts):
    number = input("Введи номер контакту для оновлення (або натисни Enter, щоб шукати за прізвищем): ").strip().lower()

    if number:
        if number in contacts:
            контакт = contacts[number]
        else:
            print("Контакт не знайдений")
            return
    else:
        last_name = input("Введи прізвище: ").strip().lower()
        збіги = []
        for num, data in contacts.items():
            if last_name in data['last_name'].lower():
                збіги.append((num, data))

        if not збіги:
            print("Збігів не знайдено")
            return

        for i, (num, data) in enumerate(збіги, 1):
            print(f"{i}. {num} — {data['first_name']} {data['last_name']}")

        вибір = input("Введи індекс контакту для оновлення (або 'ні' для скасування): ").strip().lower()
        if вибір == "ні":
            print("Оновлення скасовано")
            return
        if not вибір.isdigit():
            print("Некоректний ввід")
            return

        індекс = int(вибір) - 1
        if індекс < 0 or індекс >= len(збіги):
            print("Недійсний індекс")
            return

        number = збіги[індекс][0]
        контакт = contacts[number]

    print("Залиш поле порожнім, якщо не хочеш змінювати.")
    for field in ['first_name', 'last_name', 'city', 'state']:
        нове = input(f"{field}: ").strip()
        if нове:
            контакт[field] = нове

    contacts[number] = контакт
    print("Контакт оновлено")


# ПОШУК ЗА ПОЛЕМ
def search_by_field(contacts, field, prompt):
    look = input(prompt).strip().lower()
    found = False
    for number, data in contacts.items():
        if look in data.get(field, '').lower():
            print("-" * 40)
            print(f"Номер:      {number}")
            print(f"Ім’я:       {data['first_name']}")
            print(f"Прізвище:   {data['last_name']}")
            print(f"Місто:      {data['city']}")
            print(f"Область:    {data['state']}")
            found = True
    if not found:
        print("🔍 Нічого не знайдено.")
    else:
        print("#" * 40)

# ПОШУК ЗА ПОВНИМ ІМ'ЯМ
def search_by_full_name(contacts):
    full_name = input("Додайте повне ім`я: ").strip().lower()
    for number, data in contacts.items():
        name = f"{data.get('first_name', '').strip()} {data.get('last_name', '').strip()}".lower()
        if full_name == name:
            print("-" * 40)
            print(f"Номер:      {number}")
            print(f"Ім'я:       {data['first_name']}")
            print(f"Прізвище:   {data['last_name']}")
            print(f"Місто:      {data['city']}")
            print(f"Область:    {data['state']}")
            found = True
        if not found:
            print("Нічого не знайдено")
        else:
            print("#" * 40)

# ПОШУК ЗА ТЕЛЕФОНОМ
def search_by_phone(contacts):
    number = input("Ввкдіть номер телефону: ").strip()
    if number in contacts:
        data = contacts[number]
        print("-" * 40)
        print(f"Номер:      {number}")
        print(f"Ім'я:       {data['first_name']}")
        print(f"Прізвище:   {data['last_name']}")
        print(f"Місто:      {data['city']}")
        print(f"Область:    {data['state']}")
        found = True
    if not found:
        print("Нічого не знайдено")
    else:
        print("#" * 40)

# ПОШУК ЗА МІСЦЕМ ПРОЖИВАННЯ
def search_by_city_state(contacts):
    home = input("Введіть місто чи область: ").strip()
    found = False
    for number, data in contacts.items():
        city = data.get('city', '').strip().lower()
        state = data.get('state', '').strip.lower()
        if home in state or home in city:
            print("-" * 40)
            print(f"Номер:      {number}")
            print(f"Ім'я:       {data['first_name']}")
            print(f"Прізвище:   {data['last_name']}")
            print(f"Місто:      {data['city']}")
            print(f"Область:    {data['state']}")
            found = True
        if not found:
            print("Нічого не знайдено")

# МЕНЮ
def main():
    if len(sys.argv) < 2:
        print("Запуск: python phonebook.py contacts.json")
        return

    filename = sys.argv[1]
    contacts = load_phonebook(filename)

    while True:
        print("\nМеню:")
        print("[1] Додати запис")
        print("[2] Пошук за ім’ям")
        print("[3] Пошук за прізвищем")
        print("[4] Пошук за повним ім’ям")
        print("[5] Пошук за номером телефону")
        print("[6] Пошук за місцем проживання")
        print("[7] Оновити запис")
        print("[8] Видалити запис")
        print("[9] Вийти та зберегти")

        choice = input(">>> ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_by_field(contacts, 'first_name', 'Введіть ім’я: ')
        elif choice == '3':
            search_by_field(contacts, 'last_name', 'Введіть прізвище: ')
        elif choice == '4':
            search_by_full_name(contacts)
        elif choice == '5':
            search_by_phone(contacts)
        elif choice == '6':
            search_by_city_state(contacts)
        elif choice == '7':
            update_contact(contacts)
        elif choice == '8':
            delete_contact(contacts)
        elif choice == '9':
            save_phonebook(contacts, filename)
            print("Збережено. До зустрічі!")
            break
        else:
            print("Невідома команда.")


if __name__ == "__main__":
    main()


