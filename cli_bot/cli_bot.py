from re import sub

EXIT_COMMANDS = ["good bye", "close", "exit", "quit"]

EXIT_MESSAGE = "Good bye!"

HELLO_COMMAND = "hello"

MAX_LEN_NAME = 15

FOR_FORMAT = "|{:^5}|{:^" + str(MAX_LEN_NAME + 2) + "}|{:^19}|"

contacts_book = {"Mary": "380501112222",
                 "Bill": "380501233234"}


def exit_handler() -> str:
    return EXIT_MESSAGE


def hello_handler() -> str:
    return "How can I help you?"


def comfortable_view(phone: str) -> str:
    return f"+{phone[:2]}({phone[2:5]}){phone[5:8]}-{phone[8:10]}-{phone[10:]}"


def show_all_handler() -> str:
    if len(contacts_book) == 0:
        result = "The contacts book is empty."
    else:
        result = f"{FOR_FORMAT}\n\n".format('N', 'Name', 'Phone')
        number = 0
        for contact in contacts_book:
            number += 1
            new_string = FOR_FORMAT.format(str(number),
                        contact, comfortable_view(contacts_book[contact]))
            result = f"{result}{new_string}\n"
    return result


def sanitize_phone(phone: str) -> str:
    return sub(r'\D', '', phone)


def correct_phone(phone: str) -> str:
    phone = sanitize_phone(phone)
    if len(phone) == 10:
        return f"38{phone}"
    elif len(phone) != 12:
        return ""
    else:
        return phone
    

def without_first_word(string: str) -> str:
    return string[string.find(" ")+1:]


def add_handler(name_phone: str) -> str:
    new_name = name_phone.split()[0][:MAX_LEN_NAME]
    if new_name in contacts_book:
        raise ValueError
    new_phone = without_first_word(name_phone)
    new_phone = correct_phone(new_phone)
    if new_phone:
        contacts_book[new_name] = new_phone
        return "A new contact has been added to the contact book."
    else:
        raise IndexError


def change_handler(name_phone: str) -> str:
    name = name_phone.split()[0][:MAX_LEN_NAME]
    if name in contacts_book:
        new_phone = without_first_word(name_phone)
        new_phone = correct_phone(new_phone)
        if new_phone:
            contacts_book[name] = new_phone
            return "The contact's phone number has been changed."
        else:
            raise IndexError
    else:
        raise KeyError


def phone_handler(name: str) -> str:
    return contacts_book[name]


def input_error(func):
    def inner(command: str) -> str:
        try:
            result = func(command)
            if not result:
                result = "Unknown command."
            return f"\n{result}\n"
        except KeyError:
            return "Contact with this name does not exist."
        except ValueError:
            return "A contact with this name already exists, use command 'change' to correct the phone."
        except IndexError:
            return 'The phone number is incorrect.'
    return inner


@input_error
def parser(command: str) -> str:
    command_lower = command.lower()
    first_word_of_command = command_lower.split()[0]
    result = ""
    if command_lower in EXIT_COMMANDS:
        result = exit_handler()
    elif command_lower == HELLO_COMMAND:
        result = hello_handler()
    elif command_lower == "show all":
        result = show_all_handler()
    elif first_word_of_command == "add":
        result = add_handler(without_first_word(command))
    elif first_word_of_command == "change":
        result = change_handler(without_first_word(command))
    elif first_word_of_command == "phone":
        result = phone_handler(without_first_word(command))
    return result


def main() -> None:
    result = ""
    while result.strip() != EXIT_MESSAGE:
        command = input("\nEnter the command   ")
        result = parser(command)
        print(result)


if __name__ == "__main__":
    main()