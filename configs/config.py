from configparser import ConfigParser
from os import path


def create_config() -> None:
    _config.add_section("Telegram")
    _config.set("Telegram", "api_id", "you api_id here")
    _config.set("Telegram", "api_hash", "you api_hash here")
    _config.set("Telegram", "username", "magicBot")
    _config.set("Telegram", "session_string", "None")

    with open(_path, "w") as config_file:
        _config.write(config_file)


def write_session_string_in_config(session_string: str) -> None:
    _config.set("Telegram", "session_string", session_string)
    with open(_path, "w") as config_file:
        _config.write(config_file)


_config: ConfigParser = ConfigParser()
_path: str = path.join(path.dirname(__file__), "config.ini")
if not path.exists(_path):
    create_config()
    print("Отсутствовал файл configs.ini файл, заполните api в нём")
    exit()

_config.read(_path)

API_ID = _config['Telegram']['api_id']
API_HASH = _config['Telegram']['api_hash']
USERNAME: str = _config['Telegram']['username']
SESSION_STRING = (None
                  if _config['Telegram']['session_string'] == "None" or
                     _config['Telegram']['session_string'] == ""
                  else _config['Telegram']['session_string'])
