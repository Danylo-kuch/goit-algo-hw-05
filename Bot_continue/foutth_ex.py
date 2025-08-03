def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def load_contacts():
    contacts = {}
    path = "goit-algo-hw-04\\Bot\\contacts.txt"
    try:
        with open(path, "r") as f:
            for line in f:
                if ":" in line:
                    name, phone = line.strip().split(":", 1)
                    contacts[name.strip()] = phone.strip()
    except FileNotFoundError:
        return contacts
    return contacts

def input_error(func):
    def inner(*args, **kwargs):
        try:
            if not args or len(args[0]) == 0:
                return "Missing arguments" 
            
            elif func.__name__ == "add_contact" and len(args[0]) != 2:
                return "Usage: add <name> <phone>"
            
            elif func.__name__ == "change_contacts_phone" and len(args[0]) != 2:
                return "Usage: change <name> <new_phone>"
            
            elif func.__name__ == "show_contacts_phone" and len(args[0]) != 1:
                return "Usage: phone <name>"
            
            return func(*args, **kwargs)
        except KeyError:
            return f"The name {args[0][0]} wasn't found in your contacts"
        except (ValueError, IndexError):
            return "Give me name and phone number please!"
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} was successfully added!"

@input_error
def change_contacts_phone(args, contacts):
    name, new_phone = args
    contacts[name] = new_phone
    return f"Your phone number was successfully changed"

@input_error
def show_contacts_phone(args, contacts):
    name = args[0]
    return f"Here is the phone number for {name}: {contacts[name]}"

    
def show_all_contacts():
    with open("goit-algo-hw-04\\Bot\\contacts.txt", "r") as f:
        lines = f.readlines()
        if not lines:
            return "No contacts found."
        else:
            result = "All contacts:\n"
            result += "\n".join(line.strip() for line in lines)
            return result

def save_contacts(contacts):
    with open("goit-algo-hw-04\\Bot\\contacts.txt", "w") as f:
        for name, phone in contacts.items():
            f.write(f"{name}: {phone}\n")


def main():
    contacts = load_contacts()
    print("Welcome to the assistant BOT created by Danylo Kucherenko!")
    while True:
        user_input = input("Enter the command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Okay. Good bye!")
            break

        elif command == "hello":
            print("Hi! How can I help you?")

        elif command == "add":
            firstly = add_contact(args, contacts)
            save_contacts(contacts)
            print(firstly)

        elif command == "change":
            changed = change_contacts_phone(args, contacts)
            save_contacts(contacts)
            print(changed)

        elif command == "phone":
            phone = show_contacts_phone(args, contacts)
            print(phone)
        
        elif command == "all":
            result = show_all_contacts()
            print(result)


        else:
            print("Invalid command")

if __name__ == "__main__":
    main()