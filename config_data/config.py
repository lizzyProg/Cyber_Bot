from dataclasses import dataclass


BOT_TOKEN = "6049386124:AAHDxDLPq2rxA1UgBgxulyzrpJNFX-fC0_4"


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    return Config(tg_bot=TgBot(token=BOT_TOKEN))
