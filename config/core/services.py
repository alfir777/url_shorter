import secrets
from string import ascii_letters, digits


def generate_slug(length: int) -> str:
    letters_and_digits = ascii_letters + digits
    return ''.join(secrets.choice(letters_and_digits) for i in range(length))
