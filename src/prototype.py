import copy
from logger_config import setup_logging

logger = setup_logging()

class Monster:
    def __init__(self, name: str, skills: list[str]):
        self.name = name
        self.skills = skills

    def __str__(self):
        return f"Monster {self.name} with skills: {self.skills}"

    def clone(self, **kwargs):
        # Используем deepcopy, чтобы вложенные списки тоже скопировались
        obj = copy.deepcopy(self)
        # Позволяем изменить некоторые поля при клонировании
        obj.__dict__.update(kwargs)
        return obj

# 1. Создаем "Прототип" (эталон)
basic_orc = Monster("Orc Warrior", ["Strong", "Green"])

# 2. Клонируем его
elite_orc = basic_orc.clone(name="Elite Orc")
elite_orc.skills.append("Berserk")

logger.info(f"Original: {basic_orc}")
logger.info(f"Clone: {elite_orc}")