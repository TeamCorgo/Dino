from datetime import datetime


class User:
    def __init__(self, username: str, token: str):
        self.username = username
        self.token = token
        self.created = datetime.now().strftime("%Y.%m.%d %H:%M")
        self.x = 0
        self.y = 0
        self.z = 0


class Cell:
    def __init__(self, color: str):
        self.color = color
        self.created = datetime.now().strftime("%Y.%m.%d %H:%M")


class AppState:
    def __init__(self):
        self.users = {}
        self.worlds = {}
        self.themes = {}
        self.seed = "49db74f7-3662-46ab-a33a-9d355439fe0b"


state = AppState()
