
character = input("Enter a character: ")


if character.isdigit():
    print("It is a number.")

elif character.isalpha():
    if character.isupper():
        print("It is an uppercase letter.")
    else:
        print("It is a lowercase letter.")

else:
    print("It is neither a letter nor a number.")
