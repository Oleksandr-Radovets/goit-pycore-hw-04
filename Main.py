import os
import pathlib
from importlib.resources import files
import colorama
import regex
import sys

from colorama import Fore


def total_salary(path):
    suma = 0
    try:
        txt = pathlib.Path.open(path)
        str = txt.readlines()
        for strTxt in str:
            pattern = r"\D"
            strNumb = regex.sub(pattern, "", strTxt)
            suma = int(strNumb.strip()) + suma
    except:
        print("Invalid file reference")
    finally:
        txt.close()
    result = {f"Загальна сума заробітної плати: {suma}, Середня заробітна плата : {suma // len(str)}"}
    return result


print(total_salary("salary.txt"))

def get_cats_info(path):
    arrayList = list()
    try:
        txt = pathlib.Path.open(path)
        str = txt.readlines()
        for strTxt in str:
            parse = regex.sub(r"[\W\;,\-:!\.\_]", " ", strTxt)
            parse1 = regex.search(r"(\w+)(\s+)(\w+)(\s+)(\d)", parse)
            arrayList.append({f"id : {parse1.group(1)},"
                              f" name: {parse1.group(3)},"
                              f" age: {parse1.group(5)}"})
    except:
        print("Invalid file reference")
    finally:
        txt.close()
    return arrayList


# print(get_cats_info("animals.txt"))

if __name__ == "__main__":
    path = "D:/PythonProject/goit-pycore-hw-04/"


def pathColor(path):
    for root, dirs, file in os.walk(path.__str__()):
        print(root, dirs, file)
        print(F"{Fore.LIGHTBLUE_EX} Вложенные папки:")
        for dir_name in dirs:
            print(f'{Fore.LIGHTBLUE_EX}[FOLDER] {dir_name}')
        print(F"{Fore.LIGHTYELLOW_EX} Файлы:")
        for file_name in file:
            print(f'{Fore.LIGHTYELLOW_EX}[FILE] {file_name}')
        print()
    checkSlash = regex.findall(r"\\", path) or regex.findall(r"/", path)
    for path in path.__str__().split(checkSlash[0]):
        if os.path.isdir(path):
            print(f"{Fore.LIGHTMAGENTA_EX}[DISC]{path}")
        elif os.path.isfile(path):
            print(f"{Fore.LIGHTYELLOW_EX}[FILE]{path}")
        elif os.path.abspath(path):
            print(f"{Fore.LIGHTBLUE_EX}[FOLDER]{path}")

pathColor(path)




dictList = {}
def main():
    print(F"{Fore.LIGHTBLUE_EX}Hello my Friend")
    print("I am assistant bot!")
    while True:
        print("select a command", "--->__add_Name_and_Phone<---> add")
        print("select a command", "--->__change_Phone<---> change")
        print("select a command", "--->__add_Name_and_Phone<---> show")
        print("select a command", "--->__all_Name_and_Phone<---> all")
        command = input().__str__().lower().strip()
        if command == "add":
            print(F"{Fore.LIGHTYELLOW_EX}Your name and number Phone")
            name = input(F"{Fore.LIGHTYELLOW_EX}please your name:").strip().lower()
            phone = input(F"{Fore.LIGHTYELLOW_EX}please your phone :").strip().lower()
            user = add_contact(name.__str__(), phone.__str__())
            if user is not None:
                print("your number has been added")
        if command == "change":
            print("enter your name and the new number you want to replace")
            name1 = input("your name :").strip().lower()
            number1 = input("your new phone :").strip().lower()
            result = change_contact(name1.__str__(), number1.__str__())
            if result is not None:
                print(f"{name1} number phone is change {result}")
        if command == "show":
            namePhoneFind = input("your name: ").strip().lower()
            print(show_phone(namePhoneFind))
        if command == "all":
            input("click go to see all phone numbers : ")
            result = show_all()
            if result is None:
                print("the database is empty")
            else:
                print(result)
        if command in ["close", "exit"]:
            print("Good bye my Friend!")
            break


def add_contact(name, phone):
        pettern1 = r"\D"
        matches = regex.sub(pettern1, "", phone)
        checkNumber = bool(regex.search(r"^380\d{9}$", matches))
        checkNum = bool(regex.search(r"^0\d{9}$", matches))
        checkN = bool(regex.search(r"^+380\d{9}$", matches))
        if checkNumber:
            number = "+" + matches
            dictNamePhone = dictList[name] = number
            return dictNamePhone
        elif checkNum:
            number1 = "+38" + matches
            dictNamePhone1 = dictList[name] = number1
            return dictNamePhone1
        elif checkN:
            dictNamePhone2 = dictList[name] = matches
            return dictNamePhone2
        else:
            print("the number format is not correct")


def change_contact(nameCh, phoneCh):
    newPhone = 0
    pettern1 = r"\D"
    matches = regex.sub(pettern1, "", phoneCh)
    checkNumber = bool(regex.search(r"^380\d{9}$", matches))
    checkNum = bool(regex.search(r"^0\d{9}$", matches))
    checkN = bool(regex.search(r"^+380\d{9}$", matches))
    if checkNumber:
        newPhone = "+" + matches
        return updateDictByKey(dictList,nameCh,newPhone)
    elif checkNum:
        newPhone = "+38" + matches
        return updateDictByKey(dictList, nameCh, newPhone)
    elif checkN:
        newPhone = matches
        return updateDictByKey(dictList, nameCh, matches)
    else:
        print("the number format is not correct")

def show_phone(showName):
    for k, v in dictList.items():
        if k == str(showName):
            return v
        else:
            TypeError("Your name and phone is not dataBase")

def show_all():
    for k, v in dictList.items():
        return k,v

def updateDictByKey(dictList,name,value):
    for k, v in dictList.items():
        if k == name:
            dictList[k] = value
            return value
    print("Your name is not dataBase")

main()
