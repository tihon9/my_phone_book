import re


def sort_phone_book(file="Phone_book.txt"):
    # Функция для сортировки справочника
    with open(file, "r") as f:
        lst_sort = f.readlines()
    lst_sort.sort()
    with open(file, "w") as f:
        for i in lst_sort:
            f.write(i)


def add_contact(l_name, f_name, patronymic, company, work_phone, personal_phone, file="Phone_book.txt"):
    # Функция для добавления нового контакта
    with open(file, "a") as f:
        f.write(
            f"{l_name.title()} | {f_name.title()} | {patronymic.title()} | {company} | {work_phone} | {personal_phone}\n")
    sort_phone_book()


def view_contacts_by_letter(letter, file="Phone_book.txt"):
    # Функция для вывода контактов с фамилиями на определенную букву
    with open(file, "r") as f:
        contact = f.readline()
        count_contact = 0
        while True:
            if contact:
                if contact[0].lower() == letter.lower():
                    print(contact.replace("|", ""))
                    count_contact += 1
                    contact = f.readline()
                else:
                    contact = f.readline()
            else:
                if count_contact == 0:
                    print(f"Фамилий, начинающихся с буквы {letter.upper()} нет")
                break


def view_contacts(file="Phone_book.txt"):
    # Функция для постраничного вывода
    with open(file, "r") as f:
        lst_cont = f.readlines()
    lett = 0
    while lett < 33:
        print(f"'{lst_alph[lett].upper()}'")
        q = 0
        for i in lst_cont:
            if i[0].lower() == lst_alph[lett]:
                q += 1
                print(i.replace("|", ""))
        if q == 0:
            print(f"На букву {lst_alph[lett].upper()} записей нет\n")
        lett += 1
        if input("Для продолжения нажмите 'Enter', для выхода нажмите '1', 'Enter'\n") == "1":
            break


def search_for_contacts(lst_ch, last_n="", first_n="", patr="", comp="", work_ph="", personal_ph="",
                        file="Phone_book.txt"):
    # Функция для поиска контакта по нескольким параметрам
    with open(file, "r") as f:
        contact = f.readline()
        count = 0
        while contact:
            coin = 0
            new_contact = list(contact.split("|"))
            new_contact = [i.strip() for i in new_contact]
            if 1 in lst_ch and last_n == new_contact[0]:
                coin += 1
            if 2 in lst_ch and first_n == new_contact[1]:
                coin += 1
            if 3 in lst_ch and patr == new_contact[2]:
                coin += 1
            if 4 in lst_ch and comp == new_contact[3]:
                coin += 1
            if 5 in lst_ch and work_ph == new_contact[4]:
                coin += 1
            if 6 in lst_ch and personal_ph == new_contact[5]:
                coin += 1
            if coin == len(lst_ch):
                print(contact.replace("|", ""))
                count += 1
            contact = f.readline()
        if count == 0:
            print("Контакт не найден")


def changing_a_contact(contact_fio, file="Phone_book.txt"):
    with open(file, "r") as f:
        contact = f.readline()
        new_contact_lst = []
        count = 0
        while contact:
            new_contact = contact.split("|")
            new_contact = [i.strip() for i in new_contact]
            coin = 0
            for i in range(3):
                if new_contact[i].lower() == contact_fio[i].lower():
                    coin += 1
            if coin == 3:
                count += 1
                last_n_, first_n_, patr_, comp_, work_ph_, personal_ph_ = [i for i in new_contact]
                print(f"Найден контакт: {contact.replace('|', '')}\n")
                new_date = input(
                    "Если фамилию нужно заменить- введите новую и нажмите 'Enter', если оставить прежнюю- нажмите 'Enter'.\n-")
                if new_date:
                    last_n_ = new_date
                new_date = input(
                    "Если имя нужно заменить- введите новое и нажмите 'Enter', если оставить прежним- нажмите 'Enter'.\n-")
                if new_date:
                    first_n_ = new_date
                new_date = input(
                    "Если отчество нужно заменить- введите новое и нажмите 'Enter', если оставить прежним- нажмите 'Enter'.\n-")
                if new_date:
                    patr_ = new_date
                new_date = input(
                    "Если название компании нужно заменить- введите новое и нажмите 'Enter', если оставить прежним- нажмите 'Enter'.\n-")
                if new_date:
                    comp_ = new_date
                new_date = input(
                    "Если рабочий телефон нужно заменить- введите новый и нажмите 'Enter', если оставить прежним- нажмите 'Enter'.\n-")
                if new_date:
                    work_ph_ = new_date
                new_date = input(
                    "Если личный телефон нужно заменить- введите новый и нажмите 'Enter', если оставить прежним- нажмите 'Enter'.\n-")
                if new_date:
                    personal_ph_ = new_date
                new_contact_lst.append(f"{last_n_} | {first_n_} | {patr_} | {comp_} | {work_ph_} | {personal_ph_}\n")
                print(f"{last_n_}  {first_n_}  {patr_}  {comp_}  {work_ph_}  {personal_ph_}\n")
                contact = f.readline()
            else:
                new_contact_lst.append(contact)
                contact = f.readline()

    if count > 0:
        with open("Phone_book.txt", "w") as f:
            for i in new_contact_lst:
                f.write(i)
        sort_phone_book()
    else:
        print("Контакт не найден, проверьте корректность данных!")


a = ord("а")
lst_alph = ''.join([chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)])

while True:
    action = input("""Введите команду:\n\n 
    -Для просмотра справочника постранично- 1, 'Enter'
    -Для просмотра контактов с фамилиями начинающимися на определенную букву- введите букву, 'Enter'
    -Для добавления новой записи- 2, 'Enter'
    -Для редактирования данных контакта- 3, 'Enter'
    -Для поиска по заданным параметрам- 4, 'Enter'
    -Для выхода нажмите- 5, 'Enter'\n\n
    """).lower()

    if action == "1":
        view_contacts()

    elif action == "2":
        print("Введите данные контакта на русском языке.")
        while True:
            l_name = input("Фамилия: ")
            if re.match("[а-я|А-Я]+", l_name):
                break
            else:
                print("Некорректный ввод, попробуйте снова")
        while True:
            f_name = input("Имя: ")
            if re.match("[а-я|А-Я]+", f_name):
                break
            else:
                print("Некорректный ввод, попробуйте снова")

        while True:
            patronymic = input("Отчество: ")
            if re.match("[а-я|А-Я]+", patronymic):
                break
            else:
                print("Некорректный ввод, попробуйте снова")
        while True:
            company = input("Название организации (в формате ООО'Хххх' или ЗАО'Хххх', или ОАО'Хххх', или ИП'Ххххххх': ")
            if re.match(r"""ИП'.+'|ИП".+"|ООО'.+'|ООО".+"|ЗАО'.+'|ЗАО".+"|ОАО'.+'|ОАО".+""", company):
                break
            else:
                print("Некорректный ввод, попробуйте снова")
        while True:
            work_phone = input("Рабочий телефон(в формате: 8(ххх)ххх-хх-хх): ")
            if re.match("\d\(\d{3}\)\d{3}-\d{2}-\d{2}", work_phone):
                break
            else:
                print("Некорректный ввод, попробуйте снова")
        while True:
            personal_phone = input("Личный телефон(в формате: 8(ххх)ххх-хх-хх) : ")
            if re.match("\d\(\d{3}\)\d{3}-\d{2}-\d{2}", personal_phone):
                break
            else:
                print("Некорректный ввод, попробуйте снова")
        add_contact(l_name, f_name, patronymic, company, work_phone, personal_phone)
        print("Контакт добавлен\n")

    elif action == "3":
        while True:
            contact_fio = input("Введите фамилию, имя и отчество контакта через пробел: ").split()
            if len(contact_fio) == 3:
                break
            else:
                print("Неверный ввод, попробуйте снова")
        changing_a_contact(contact_fio)

    elif action == "4":
        while True:
            lst_check = input("""Введите одну или несколько цифр через запятую, в зависимости от того по каким данным 
            нужно осуществить поиск:
            1- для фамилии
            2- для имени
            3- для отчества
            4- для названия организации
            5- для рабочего телефона
            6- для личного телефона\n\n""").split(",")
            if lst_check:
                break
            else:
                continue
        lst_ch = list(map(int, lst_check))
        if 1 in lst_ch:
            last_n = input("Фамилия: \n")
        else:
            last_n = ""
        if 2 in lst_ch:
            first_n = input("Имя: \n")
        else:
            first_n = ""
        if 3 in lst_ch:
            patr = input("Отчество: \n")
        else:
            patr = ""
        if 4 in lst_ch:
            comp = input("Название организации: \n")
        else:
            comp = ""
        if 5 in lst_ch:
            work_ph = input("Рабочий телефон(в формате: 8(ххх)ххх-хх-хх): \n")
        else:
            work_ph = ""
        if 6 in lst_ch:
            personal_ph = input("Личный телефон(в формате: 8(ххх)ххх-хх-хх): \n\n")
        else:
            personal_ph = ""
        search_for_contacts(lst_ch, last_n, first_n, patr, comp, work_ph, personal_ph)

    elif action.lower() in lst_alph:
        view_contacts_by_letter(action.lower())

    elif action == "5":
        break

    else:
        print("Неправильный ввод, попробуйте снова")
        continue
