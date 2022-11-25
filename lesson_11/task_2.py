import sys
import os
import json

phonebook_name = None

try:
    phonebook_name = sys.argv[1]
except Exception as err:
    print('Please, enter the name of the phonebook.')
    exit()

try:
    with open('db.json', 'r+') as f:
        data = json.load(f)
except FileNotFoundError:
    print("The db file does not exist in the current folder")
    exit()
except json.decoder.JSONDecodeError:
    print("The db file has a bad format")
    exit()

try:
    phonebook_contacts = data[phonebook_name]
except KeyError:
    phonebook_contacts = []


def show_up_menu():
    print(f'{phonebook_name} Phonebook > Menu\n')
    print('[1]  Add new contacts')
    print('[2]  Search contacts')
    print('[3]  Delete a contact')
    print('[4]  Update a contact')
    print('[0]  Exit the program\n')


def menu():
    menu_item = None

    while menu_item is None or menu_item > 4:
        show_up_menu()

        input_value = input("Please enter your choice: ")

        if not input_value.isdigit():
            continue
        else:
            menu_item = int(input_value)

    return menu_item


def add_new_contacts():
    switcher = ''

    while switcher == '' or switcher == 'y':
        os.system('clear')
        print(f'{phonebook_name} Phonebook > Add a new Contact\n')

        contact = {'first_name': None, 'last_name': None, 'telephone_number': None, 'city': None, 'state': None}

        for field in contact:
            input_value = input(f'{field}: ')
            contact[field] = input_value

        phonebook_contacts.append(contact)

        switcher = input('\nAre you going to add more? (y/n)')


def seek_contacts():
    print(f'{phonebook_name} Phonebook > Search Contacts')
    term = input('Enter a search query: ')
    contact_values = lambda contact: list(contact.values()) + ['%s %s' % (contact['first_name'], contact['last_name'])]
    search = lambda contact: term in contact_values(contact)
    contacts = list(filter(search, phonebook_contacts))

    print("\n{:<10} {:<10} {:<10} {:<10} {:<10}".format('FName', 'LName', 'Phone', 'City', 'State'))
    print(50 * '-')

    for contact in contacts:
        print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(*list(contact.values())))

    print(50 * '-')
    input('\nPress any key to continue')


def delete_contact():
    print(f'{phonebook_name} Phonebook > Delete Contact')
    telephone_number = input('Enter a phone number: ')
    is_deleted = False

    for i in range(len(phonebook_contacts)):
        if phonebook_contacts[i]['telephone_number'] == telephone_number:
            del phonebook_contacts[i]
            is_deleted = True
            break
    if is_deleted:
        print(f'{telephone_number} has been successfully deleted.')
    else:
        print(f'{telephone_number} does not exist in the phonebook')

    input('\nPress any key to continue')


def update_contact():
    print(f'{phonebook_name} Phonebook > Update Contact')
    telephone_number = input('Enter a phone number: ')

    contact = next((item for item in phonebook_contacts if item['telephone_number'] == telephone_number), None)

    if not contact:
        print(f'The contact {telephone_number} does not exist.')
    else:
        for field in contact:
            input_value = input(f'{field} [{contact[field]}]: ')

            if input_value: contact[field] = input_value

        print(f'The contact {telephone_number} has been successfully updated.')

    input('\nPress any key to continue')


def persist_contacts():
    data[phonebook_name] = phonebook_contacts

    json_object = json.dumps(data, indent=4)

    with open("db.json", "w") as f:
        f.write(json_object)


def menu_dispatcher(action_number=-1):
    os.system('clear')

    if action_number == 1:
        add_new_contacts()
    elif action_number == 2:
        seek_contacts()
    elif action_number == 3:
        delete_contact()
    elif action_number == 4:
        update_contact()
    else:
        persist_contacts()
        print(f'The {phonebook_name} has been successfully saved to the file')
        print('Bye, bye!')
        exit()


while True:
    os.system('clear')
    choice = menu()

    menu_dispatcher(choice)
