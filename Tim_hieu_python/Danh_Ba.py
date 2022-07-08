class Contact:
    def __init__(self, name, add, phone, email):
        self.name = name
        self.add = add
        self.phone = phone
        self.email = email

def read_contact():
    name = input("Enter contact name: ")
    add = input("Enter contact address: ")
    phone = input("Enter contact number phone: ")
    email = input("Enter contact email: ")
    contact = Contact(name, add, phone, email)
    return contact

def read_contacts():
    contacts = []
    total = int(input("Enter how many contact: "))
    for i in range(total):
        print("Contact " + str(i+1) + ": ")
        con = read_contact()
        contacts.append(con)
    return contacts

def print_contact(contact):
    print("Name: ", contact.name, end="")
    print("Address: ", contact.add, end="")
    print("Number phone: ", contact.phone, end="")
    print("Email: ", contact.email, end="")

def print_contacts(contacts):
    for i in range(len(contacts)):
        print("Contact ", str(i+1), ": ")
        print_contact(contacts[i])

def write_contact_to_txt(contact, file):
    file.write(contact.name + "\n")
    file.write(contact.add + "\n")
    file.write(contact.phone + "\n")
    file.write(contact.email + "\n")

def write_contacts_to_txt(contacts):
    total = len(contacts)
    with open("contact.txt", "w", encoding='utf-8') as file:
        file.write(str(total) + "\n")
        for i in range(total):
            write_contact_to_txt(contacts[i], file)

def read_contact_from_txt(file):
    name = file.readline()
    add = file.readline()
    phone = file.readline()
    email = file.readline()
    contact = Contact(name, add, phone, email)
    return contact

def read_contacts_from_txt():
    contacts = []
    with open("contact.txt", "r", encoding='utf-8') as file:
        total = file.readline()
        for i in range(int(total)):
            con = read_contact_from_txt(file)
            contacts.append(con)
    return contacts



def main():
    print("======================================================")
    contacts = read_contacts()
    write_contacts_to_txt(contacts)
    contacts = read_contacts_from_txt()
    print_contacts(contacts)

main()