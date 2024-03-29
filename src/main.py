from objects.AddressBook import AddressBook
from objects.Notes import Notes
from servises.SaveService import SaveService
import bot_functions
from prompt_toolkit import prompt
from servises.CompleterService import MyCompleter



def main():
    """
    Main function to run the console bot assistant.

    This function initializes the necessary objects, such as the SaveService, AddressBook, and Notes.
    It also defines a dictionary of commands mapped to their corresponding functions.
    The user is prompted to enter a command, and the appropriate handler function is called based on the input.
    The loop continues until the user enters either 'exit' or 'close'.

    Returns:
        None
    """
    save_service = SaveService()
    book = AddressBook(save_service)
    notes = Notes(save_service)

    commands = {
        "add": lambda args: bot_functions.add_contact_command(args, book),
        "edit": lambda args: bot_functions.edit_contact_command(args, book),
        "remove": lambda args: bot_functions.remove_contact_command(args, book),       
        "birthdays": lambda args: bot_functions.birthdays_command(args, book),        
        "hello": lambda args: bot_functions.hello_command(args),
        "all": lambda args: bot_functions.show_all_contacts_command(args, book),
        "search": lambda args: bot_functions.search_contacts_command(args, book),
        "add-comment": lambda args: bot_functions.add_comment_command(args, book),
        "remove-comment": lambda args: bot_functions.remove_comment_command(args, book),
        "add-note": lambda args: bot_functions.add_notes_command(args, notes),
        "remove-note": lambda args: bot_functions.remove_notes_command(args, notes),
        "edit-note": lambda args: bot_functions.edit_notes_command(args, notes),
        "notes": lambda args: bot_functions.list_notes_command(args, notes),
        "find-notes": lambda args: bot_functions.find_notes_command(args, notes),
        "help": lambda args: bot_functions.help(commands),
        }
    
    autocommand = list(commands.keys()) + ["close", "exit"]
    
    while True:
        user_input = prompt("Enter a command: ", completer=MyCompleter(autocommand)).lower().split()
        command, args = user_input[0], user_input[1:]

        if command in ["exit", "close"]:
            print("Good bye!")
            break

        handler = commands.get(command)
        if not handler:
            print("Invalid command.")
            continue

        result = handler(args)
        if result:
            print(result)
        


if __name__ == "__main__":
    main()