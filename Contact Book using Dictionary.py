
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print("Contact added!")

def search_contact(name):
    return contacts.get(name, "Not found")

def update_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        print("Contact updated!")
    else:
        print("Contact not found!")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted!")
    else:
        print("Contact not found!")

# Example usage
add_contact("Sneha", "9999988882")
print(search_contact("Sneha"))
update_contact("Sneha", "8888999999")
delete_contact("Sneha")
