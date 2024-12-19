import re


def split_email(email):
    email_p = r'^(?P<username>[a-zA-Z0-9][a-zA-Z0-9._%+-]*[a-zA-Z0-9])@(?P<domain>[a-zA-Z0-9-]+\.[a-zA-Z]{2,})$'

    match = re.match(email_p, email)
    if match:
        x = match.group('username')
        y = match.group('domain')
        print(f"username: {x}")
        print(f"domain: {y}")
    else:
        print("Некорректный email адрес.")


def main():
    email = input("Введите email: ")

    split_email(email)


main()
