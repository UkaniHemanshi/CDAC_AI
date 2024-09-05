choice = "Yes"
whole_phone_list = {}

while(True):
    if choice == "Yes":
        operation = int(input("Enter your choice for phonebook access\n 1. Add\n 2. Search\n 3. update\n 4. Delete\n "))
        match operation:
            case 1:
                ph_email_dict = {}

                contact_name = input("Enter your contact name: ")
                ph_no = int(input("Enter your phone number: "))
                email = input("Enter your email: ")

                # adding dictionary to dictionary where key is contact_name and value as dictionary of ph_no and email
                ph_email_dict['Phone_number'] = ph_no
                ph_email_dict['Email'] = email
                whole_phone_list[contact_name] = ph_email_dict

                print(f'Your whole contact list are: {whole_phone_list}')

            case 2:
                search_choice = input("Enter your contact_name which you want to search: ")
                if search_choice in whole_phone_list.keys():
                    print(whole_phone_list[search_choice])
                else:
                    print(f'Your contact name = "{search_choice} "does not exist')

                print(f'Your whole contact list are: {whole_phone_list}')

            case 3:
                update_choice = input("Enter your contact_name which you want to update: ")
                if update_choice in whole_phone_list.keys():
                    choice_up = input("Enter your choice for update either phone or email:  ")

                    if choice_up == "phone":
                        new_phone = int(input("Enter your new phone number: "))
                        whole_phone_list[update_choice]['Phone_number'] = new_phone
                        print(f'Your whole contact list are: {whole_phone_list}')

                    elif choice_up == "email":
                        new_email = input("Enter your new email: ")
                        whole_phone_list[update_choice]['Email'] = new_email
                        print(f'Your whole contact list are: {whole_phone_list}')
                    else:
                        print(f'Your whole contact list are: {whole_phone_list}')
                        break
            case 4:
                delete_choice = input("Enter your contact_name which you want to delete: ")
                if delete_choice in whole_phone_list.keys():
                    del whole_phone_list[delete_choice]
                print(f'Your whole contact list are: {whole_phone_list}')

    choice = input("Enter Yes or No for more phonebook access operation: ")
    if choice == "No":
        break