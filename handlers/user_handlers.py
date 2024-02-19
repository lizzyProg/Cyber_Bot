import os
import sys
import asyncio
from aiogram.filters import Command, CommandStart, BaseFilter
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon_ru import LEXICON_RU
from aiogram import Bot, Router, F
from services.services import my_password_generate
from services.services import password_policy_checked
from config_data.config import Config, load_config
from keyboards.keyboards import *
from handlers.filter import MyCallback
import sqlite3


sys.path.append(os.getcwd())

configg: Config = load_config()

bot: Bot = Bot(token=configg.tg_bot.token, parse_mode='HTML')
router: Router = Router()

generated_password = None
passwords_dict = None


@router.message(CommandStart())
async def process_start_message(message: Message):
    conn = sqlite3.connect('bot.db')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER primary key AUTOINCREMENT, user_id text, password text, '
                'codeword text)')
    conn.commit()
    cur.close()
    conn.close()

    await message.answer(text=LEXICON_RU[message.text])
    await message.answer(text=LEXICON_RU['menu'], reply_markup=kb_start.as_markup(row_width=1))


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU[message.text])


@router.callback_query(MyCallback.filter(F.a == 'menu'))
async def process_button_menu(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['menu'], reply_markup=kb_start.as_markup(row_width=1))


@router.message(F.text.startswith('codeword '))
async def process_get_codeword(message: Message):
    users_id = str(message.from_user.id)
    users_codeword = str(message.text)[9:]
    conn = sqlite3.connect('bot.db')
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM users WHERE user_id = ? AND password IS NOT NULL', (users_id,))
    passwords = cur.fetchone()
    cur.execute('SELECT COUNT(*) FROM users WHERE user_id = ? AND codeword = ?', (users_id,
                                                                                  users_codeword,))
    info1 = cur.fetchone()
    if info1[0] >= 1 and passwords != 0:
        global passwords_dict
        cur.execute('SELECT * FROM users')
        passwords = cur.fetchall()

        passwords_dict = {}
        for el in passwords:
            if el[1] == users_id:
                passwords_dict[passwords.index(el) + 1] = el[2]
            else:
                continue

        passwords_st = ''
        for key, value in passwords_dict.items():
            passwords_st += f'{key}. {value}\n'

        passwords_screened = ''
        for i in passwords_st:
            if i in ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']:
                passwords_screened += f'\{i}'
            else:
                passwords_screened += i
        if passwords_screened != '':
            await message.answer(text=LEXICON_RU['all_saved_passwords'])
            await message.answer(text=f'||{passwords_screened}||',
                                 reply_markup=kb_saved_passwords.as_markup(row_width=1),
                                 parse_mode='markdownv2')
        else:
            await message.answer(text=LEXICON_RU['no_saved_passwords'],
                                 reply_markup=kb_start.as_markup(row_width=1))

    elif info1[0] == 0 and passwords[0] == 1:
        cur.execute('UPDATE users SET codeword = ? WHERE user_id = ?', (users_codeword, users_id))
        await message.answer(text=LEXICON_RU['codeword_saved'], reply_markup=kb_start.as_markup(row_width=1))
    else:
        await message.answer(text=LEXICON_RU['no_saved_passwords'],
                             reply_markup=kb_start.as_markup(row_width=1))
    conn.commit()
    cur.close()
    conn.close()

'''
def process_codeword_db(message: Message):
    users_id = str(message.from_user.id)
    conn = sqlite3.connect('bot.db')
    cur = conn.cursor()
    cur.execute('SELECT codeword FROM users WHERE user_id = ?', (users_id,))
    codeword = str(cur.fetchone())
    conn.commit()
    cur.close()
    conn.close()
    return codeword


class Filter2(BaseFilter):
    def __init__(self, codeword: str) -> None:
        self.codeword = codeword

    async def __call__(self, message: Message) -> bool:
        return self.codeword == message.text
'''
'''
@router.message(F.text, Filter2(codeword=message.text))
async def process_saved_passwords(message: Message):
    global passwords_dict
    users_id = str(message.from_user.id)
    conn = sqlite3.connect('bot.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    passwords = cur.fetchall()

    passwords_dict = {}
    for el in passwords:
        if el[1] == users_id:
            passwords_dict[passwords.index(el) + 1] = el[2]
        else:
            continue

    passwords_st = ''
    for key, value in passwords_dict.items():
        passwords_st += f'{key}. {value}\n'

    passwords_screened = ''
    for i in passwords_st:
        if i in ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']:
            passwords_screened += f'\{i}'
        else:
            passwords_screened += i
    if passwords_screened != '':
        await message.answer(text=LEXICON_RU['all_saved_passwords'])
        await message.answer(text=f'||{passwords_screened}||', reply_markup=kb_saved_passwords.as_markup(row_width=1),
                             parse_mode='markdownv2')
    else:
        await message.answer(text=LEXICON_RU['no_saved_passwords'],
                             reply_markup=kb_start.as_markup(row_width=1))

    cur.close()
    conn.close()
'''


@router.callback_query(MyCallback.filter(F.a == 'generate_password'))
async def process_generate_button(callback: CallbackQuery):
    global generated_password
    generated_password = my_password_generate()
    await callback.message.answer(text=LEXICON_RU['made_password'] + f'<code>{generated_password}</code>',
                                  reply_markup=kb_generate.as_markup(row_width=1), parse_mode='HTML')


@router.callback_query(MyCallback.filter(F.a == 'another_password'))
async def process_more_password(callback: CallbackQuery):
    global generated_password
    generated_password = my_password_generate()
    await callback.message.answer(text=LEXICON_RU['made_password'] + f'<code>{generated_password}</code>',
                                  reply_markup=kb_generate.as_markup(row_width=1), parse_mode='HTML')


@router.callback_query(MyCallback.filter(F.a == 'check_password'))
async def process_check_password(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['send_password'],
                                     reply_markup=kb_check_password.as_markup(row_width=1))


@router.message(F.text.startswith('password '))
async def process_got_password(message: Message):
    await message.answer(password_policy_checked(message.text[9:]),
                         reply_markup=kb_checked_password.as_markup(row_width=1))


@router.callback_query(MyCallback.filter(F.a == 'give_advices'))
async def process_give_advices(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['advices_message1'],
                                  reply_markup=kb_give_advices.as_markup(row_width=1))


@router.callback_query(MyCallback.filter(F.a == 'next_advice1'))
async def process_next_advice1(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['advices_message2'], reply_markup=kb_give_advice2.as_markup())


@router.callback_query(MyCallback.filter(F.a == 'next_advice2'))
async def process_next_advice2(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['advices_message3'], reply_markup=kb_give_advice3.as_markup())


@router.callback_query(MyCallback.filter(F.a == 'next_advice3'))
async def process_next_advice3(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['advices_message4'], reply_markup=kb_give_advice4.as_markup())


@router.callback_query(MyCallback.filter(F.a == 'next_advice4'))
async def process_next_advice4(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['advices_message5'], reply_markup=kb_give_advice5.as_markup())


@router.callback_query(MyCallback.filter(F.a == 'next_advice5'))
async def process_bonus_advice(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['advices_message6'], reply_markup=kb_before_comic.as_markup())


@router.callback_query(MyCallback.filter(F.a == 'bonus_message'))
async def process_comic(callback: CallbackQuery):
    comic = "https://linux-faq.ru/thumb.php?src=e_MEDIA_IMAGE/2016-02/password_strength.jpg&w=400"
    await callback.message.answer_photo(photo=comic)
    await callback.message.answer(text=LEXICON_RU['advices_message7'],
                                  reply_markup=kb_advices_end.as_markup(row_width=1))


@router.callback_query(MyCallback.filter(F.a == 'save_password'))
async def process_save_password(callback: CallbackQuery):
    users_id = str(callback.from_user.id)
    global generated_password
    conn = sqlite3.connect('bot.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO users(user_id, password) VALUES (?, ?)', (users_id, generated_password,))
    cur.execute('SELECT COUNT(*) FROM users WHERE user_id = ?', (users_id,))
    num_passwords = cur.fetchone()
    await callback.message.answer(text=LEXICON_RU['password_was_saved'],
                                  reply_markup=kb_start.as_markup(row_width=1))

    conn.commit()
    cur.close()
    conn.close()
    if num_passwords[0] == 1:
        await callback.message.answer(text=LEXICON_RU['create_codeword'])


@router.callback_query(MyCallback.filter(F.a == 'remove_password'))
async def process_removing_password(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['remove_password_num'],
                                  reply_markup=kb_removing_password.as_markup(row_width=1))


@router.callback_query(MyCallback.filter(F.a == 'saved_passwords'))
async def process_check_codeword(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['check_codeword'])


class MyFilter:
    def __init__(self, range1):
        self.range = range1

    async def __call__(self, message: Message):
        return int(message.text) in self.range


@router.message(MyFilter(range(1, 20)))
async def process_got_password_num(message: Message):
    key = int(str(message.text))
    global passwords_dict
    users_id = str(message.from_user.id)
    conn = sqlite3.connect('bot.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    passwords = cur.fetchall()

    passwords_dict = {}
    for el in passwords:
        if el[1] == users_id:
            passwords_dict[passwords.index(el) + 1] = el[2]
        else:
            continue
    await message.answer(text=LEXICON_RU['password_was_removed'],
                         reply_markup=kb_saved_passwords.as_markup(row_width=1))
    cur.execute('DELETE FROM users WHERE user_id = ? AND password = ?', (users_id,
                                                                         passwords_dict.get(key)))
    conn.commit()
    cur.close()
    conn.close()

# @router.message()
# async def other_message(message: Message):
#    await message.answer(text=LEXICON_RU['other_answer'])
