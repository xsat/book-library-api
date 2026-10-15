from hashlib import md5
from random import choice
from string import printable


def access_token_generate() -> str:
    random_word: str = "".join(choice(printable) for _i in range(40))

    return password_generate(random_word)


def password_check(password: str, hash_password: str) -> bool:
    return password_generate(password) == hash_password


def password_generate(text: str) -> str:
    return md5(text.encode()).hexdigest()

