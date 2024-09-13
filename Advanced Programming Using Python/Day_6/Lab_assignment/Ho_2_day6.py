
def extract_email_id():
        try:
            with open("email_list.txt", "r") as f:
                email_list = f.readlines()
        except FileNotFoundError:
            print("Your File does not found !!! ")
        else:
            print(email_list)

            # Challenge 2 Ensure that email addresses are unique and count the number of unique email addresses
            unique_email_list = set(email_list)
            print(f"Your unique email list is : {unique_email_list} and the length is : {len(unique_email_list)}")

            f.close()
        finally:
            print("Your program is completed.  ")


extract_email_id()