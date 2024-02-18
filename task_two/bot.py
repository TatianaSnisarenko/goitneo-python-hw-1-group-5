def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    valid_format_message = 'Invalid "add" format. Command "add" must have 3 arguments: <add Name phone_number>.'
    if len(args) < 2:
        return valid_format_message
    name, phone = args
    if contacts.get(name) == None:
        contacts[name] = phone
        return 'Contact added.'
    else:
        return 'Such name is already present, please, use "change" command instead.'

def change_contact(args, contacts):
    valid_format_message = 'Invalid "change" format. Command "change" must have 3 arguments: <change Name new_phone_number>.'
    if len(args) < 2:
        return valid_format_message
    name, phone = args
    if contacts.get(name) != None:
        contacts[name] = phone
        return 'Contact updated.'
    else:
        return 'Such name is not found, please, use "add" command instead.'

def show_phone(args, contacts):
    valid_format_message = 'Invalid "phone" format. Command "phone" must have 2 arguments: <phone Name>.'
    if len(args) < 1:
        return valid_format_message
    phone = contacts.get(args[0])
    return phone if phone != None else 'Such name is not found, please, try again.'

def show_all(contacts):
    if contacts:
        return ', '.join(': '.join(item) for item in contacts.items())
    else:
        return 'Contacts are empty. Please, use add command to add new contacts'

def main():
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print('Invalid command.')

if __name__ == '__main__':
    main()