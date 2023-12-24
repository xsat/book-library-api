from dataclasses import dataclass, field


@dataclass
class User:
    user_id: int
    username: str
    password_hash: str
