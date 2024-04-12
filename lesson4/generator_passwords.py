import random
import string

def generate_password(length, use_digits=False, use_symbols=False, use_uppercase=False):
    characters = string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Укажите желаемую длину пароля: "))
    use_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
    use_symbols = input("Использовать символы? (y/n): ").lower() == 'y'
    use_uppercase = input("Использовать заглавные буквы? (y/n): ").lower() == 'y'

    passwords = set()
    while len(passwords) < 5:
        password = generate_password(length, use_digits, use_symbols, use_uppercase)
        passwords.add(password)

    for index, password in enumerate(passwords, 1):
        print(f"{index}. {password}")


main()
