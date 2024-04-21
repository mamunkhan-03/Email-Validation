email=input("Please enter your email : ")
space=False
upper=False
specialChar=False
if len(email)>=6:
    if email[0].isalpha():
        if ('@' in email) and( email.count('@')==1):
            if (email[-4]=='.') ^ (email[-3]=='.'):
                for i in email:
                    if i==i.isspace():
                        space=True
                    elif i==i.isupper():
                        upper=True
                    elif i==i.isdigit():
                        continue
                    elif i=='_' or i=="." or i=="@":
                        continue
                    else:
                        specialChar=True

                if space or upper or specialChar:
                    print("Wrong email! space, uppercase letter and special character doesn't allow")


                else:
                    print("Your email is absolutely correct")
            else :
                print("Wrong email! The position of .(dot) isn't 3rd or 4th last position or it occurs in both position ")

        else:
            print("Wrong email! It does't contains any' @' or it occurs twice ")

    else:
        print("Wrong email! First character is not a alphabet in your email. ")
else:
    print("Wrong email! It is too sort")