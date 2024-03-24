# Python Core
# Модуль 5
# домашнє завдання 4
# Лопатін Євген

def input_error(func): # створюємо декоратор
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Введіть ім'я та телефон"
        except KeyError:
            return "Такого ім'я не існує в базі"
        except IndexError:
            return "Введіть аргумент для команди"
    return inner

@input_error
def parse_input(user_input): # створюємо функцію обробки вводу 
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts): # створюємо функцію додавання контактів
    name, phone = args
    count = 1
    while True: # уникаємо перезапис імен в словнинку +1
        if name in contacts:
            name = name.split("_")[0]
            name = f'{name}_{count}'
            count += 1
        else:
            break
    contacts[name] = phone
    return "Контакт добавлений."

@input_error
def change_contact(args, contacts): # створюємо функцію зміни контакту
    name, phone = args
    if not name in contacts:
        raise KeyError("Contact")
    contacts[name] = phone
    return "Контакт оновлений."

@input_error
def all_contact(contacts): # створюємо функцію виводу списку контактів словником
    return contacts

@input_error
def phone_contact(args, contacts): # створюємо функцію виводу телефону за іменем
    name = args[0]
    return contacts[name] 

 
def main():  # створюємо основну функцію бота
    contacts = {}
    print("Вас вітає штучний асистент!\n Вам доступні наступні команди:\n привітальна команда hello \n команда для додавання користувача: add --тут вводиться імя-- --тут вводиться телефон--\n команда для зміни телефону користувача: change --тут вводиться імя-- --тут вводиться новий телефон-- \n команда для виведення телефону за іменем: phone --тут вводиться імя-- \n команда для виводу всіх збережених контактів: all \n для завершення розмови використовуйте команди close або exit ")
    while True: # створюємо незкінченний цикл обробки команд по заданих функціях
        user_input = input("Введіть відповідну команду для продовження, або введіть exit для виходу: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]: # умова для ціх команд 
            print("До побачення!")
            break

        elif command == "hello": # умова для цієй команди
            print("Як я можу Вам допомогти?")
        
        elif command == "add": # умова для цієй команди
            print(add_contact(args, contacts))
            
        elif command == "change": # умова для цієй команди
            print(change_contact(args, contacts))
            
        elif command == "phone": # умова для цієй команди
            print(phone_contact(args, contacts))
            
        elif command == "all": # умова для цієй команди
            print(all_contact(contacts))
        
        else: # умова меседжу помилки
            print("Неправильна команда: введіть правильну команду для продовження, або введіть exit для виходу.")

if __name__ == "__main__":
    main()
