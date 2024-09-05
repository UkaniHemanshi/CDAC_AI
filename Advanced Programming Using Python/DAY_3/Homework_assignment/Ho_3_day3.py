choice = "Yes"
whole_book_list = {}

while (True):
    if choice == "Yes":
        operation = int(input("Enter your choice for book collection access\n 1. Add\n 2. Search\n 3. remove\n 4. Display\n "))
        match operation:
            case 1:
                auth_gen_yeardict = {}

                book_title = input("Enter the name of book: ")
                author = input("Enter the author name of book: ")
                genres = input("Enter the genres of book: ")
                year = int(input("Enter the year of book: "))

                # adding dictionary to dictionary where key is book_title and value as dictionary of author and genres,year
                auth_gen_yeardict['Author'] = author
                auth_gen_yeardict['Genre'] = genres
                auth_gen_yeardict['Year'] = year
                whole_book_list[book_title] = auth_gen_yeardict

                print(f'Your book collection are: {whole_book_list}')

            case 2:
                choice_up = input("Enter your choice for search by either author or genres : ")

                if choice_up == "author":
                    search_auth = input("Enter the name of author which you want to search: ")
                    for i in whole_book_list.values():
                        if search_auth == i['Author']:
                            for key, value in whole_book_list.items():
                                if value['Author'] == i['Author']:
                                    print(f"{key}: {value}")
                                    break
                        else:
                            print(f"Your book is not available in stock !!! ")

                elif choice_up == "genre":
                    search_gen = input("Enter the name of genre which you want to search: ")
                    for i in whole_book_list.values():
                        if i['Genre'] == search_gen:
                            for key, value in whole_book_list.items():
                                if value['Genre'] == i['Genre']:
                                    print(f"{key}: {value}")
                                    break
                        else:
                            print(f"Your book is not available in stock !!! ")
                else:
                    print(f"Your choice is invalid !!! ")
            case 3:
                delete_choice = input("Enter your book_title which you want to delete: ")
                if delete_choice in whole_book_list.keys():
                    del whole_book_list[delete_choice]
                print(f'Your book collection are: {whole_book_list}')

            case 4:
                print(f'Your book collection are: {whole_book_list}')

    choice = input("Enter Yes or No for more phonebook access operation: ")
    if choice == "No":
        break