from dataclasses import dataclass

@dataclass
class Message:
    user: str
    content: str

@dataclass
class User:
    name: str
    status: str = 'online'