from lexicon.lexicon_ru import LEXICON_RU
from passwordgenerator import pwgenerator
from password_strength import PasswordPolicy


policy = PasswordPolicy.from_names(
    length=15,
    uppercase=5,
    numbers=3,
    special=4,
    nonletters=7,
    strength=0.66
)


def password_policy_checked(user_password: str):
    if not policy.test(user_password):
        return LEXICON_RU['strong_password']
    else:
        return LEXICON_RU['weak_password']


def my_password_generate():
    password_generated = pwgenerator.generate()
    return password_generated





