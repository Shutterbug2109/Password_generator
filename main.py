from src.password_gen import password_gen

if __name__ == '__main__':
    min_length = int(input("Enter the minimum length of the password: "))
    number = input("Do you want numbers in your password? (y/n): ").lower() == 'y'
    special_char = input("Do you want special characters in your password? (y/n): ").lower() == 'y'
    
    mypass = password_gen(min_length = min_length, number = number, special_char = special_char)
    print(mypass)