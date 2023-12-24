from hashlib import md5


def password_check(password: str, hash_password: str) -> bool:
    return password_generate(password) == hash_password


def password_generate(text: str) -> str:
    return md5(text.encode()).hexdigest()
