def input_error(func):
    """
    Decorator to handle common input errors for functions.
    
    Args:
        func (function): The function to be decorated.
    
    Returns:
        function: The wrapped function with error handling.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please enter name and phone number"
        except KeyError:
            return "Key Error"
        except IndexError:
            return "Please enter name"
        except TypeError:
            return "Invalid input format"
    return inner

def parse_input(user_input):
    """
    Parse user input into a command and arguments.
    
    Args:
        user_input (str): The input string from the user.
    
    Returns:
        tuple: A tuple containing the command and a list of arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    """
    Add a new contact to the contacts dictionary.
    
    Args:
        args (list): A list containing the name and phone number.
        contacts (dict): The dictionary to store contacts.
    
    Returns:
        str: A message indicating the result of the operation.
    """
    if len(args) < 2:
        return "Please enter name and phone number"
    
    name, phone = args
    if not phone.isdigit():
        return "Incorrect phone number format"
    
    contacts[name] = phone
    return f"Contact {name} added."

@input_error
def change_contact(args, contacts):
    """
    Change the phone number of an existing contact.
    
    Args:
        args (list): A list containing the name and new phone number.
        contacts (dict): The dictionary to store contacts.
    
    Returns:
        str: A message indicating the result of the operation.
    """
    if len(args) < 2:
        return "Please enter name and new phone number"
    
    name, phone = args
    if not phone.isdigit():
        return "Incorrect phone number format"
    
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Name not found"

@input_error
def show_phone(args, contacts):
    """
    Show the phone number of a contact.
    
    Args:
        args (list): A list containing the name of the contact.
        contacts (dict): The dictionary to store contacts.
    
    Returns:
        str: The phone number of the contact or an error message.
    """
    if len(args) < 1:
        return "Please enter a name"

    name = args[0]
    return contacts.get(name, "Name not found")

def show_all(contacts):
    """
    Show all contacts in the contacts dictionary.
    
    Args:
        contacts (dict): The dictionary to store contacts.
    
    Returns:
        dict or str: The contacts dictionary or a message if no contacts are found.
    """
    if not contacts:
        return "No contacts found"
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])

@input_error
def main():
    """
    Main function to run the assistant bot.
    
    Continuously prompts the user for commands and performs actions based on the input.
    """
    contacts = {} 
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()