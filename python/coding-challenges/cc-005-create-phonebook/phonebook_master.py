def print_menu():
    print("Welcome to the phonebook application")
    print('1. Find phone number')
    print('2. Insert a phone number')
    print('3. Delete a person from the phonebook')
    print('4. Terminate')
    print()

numbers = {}
menu_choice = 0
print_menu()

while menu_choice != 4:
    menu_choice = int(input("Select operation on Phonebook App (1/2/3) :"))
    
    if menu_choice == 2:

        name = input("Insert name of the person: ")
        phone = input("Insert phone number of the person: ")

        if not phone.isdecimal:
            print ("Invalid input format, cancelling operation ...","\n")

        else:
            numbers[name] = phone
            print ("Phone number of", name, "is inserted into the phonebook","\n")

    elif menu_choice == 3:
        name = input("Whom to delete from phonebook :")
        if name in numbers:
            del numbers[name]
            print(name, "is deleted from the phonebook","\n")
        else:
            print(name, "was not found in the phonebook","\n")
    
    elif menu_choice == 1:
        
        name = input("Find the phone number of :")
        if name in numbers:
            print(numbers[name],"\n")
        else:
            print("Couldn't find phone number of", name,"\n")
    elif menu_choice != 4:
        print_menu()
        print()

if menu_choice == 4:
    print("Exiting Phonebook")