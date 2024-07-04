from environs import Env
from dataclasses import dataclass

@dataclass
class ClientSettings:
    client_id: str
    client_secret: int

@dataclass
class AppSettings:
    app: ClientSettings

def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return AppSettings(
        app=ClientSettings(
            client_id=env.str('CLIENT_ID'),
            client_secret=env.str('CLIENT_SECRET')
        )
    )