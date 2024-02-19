from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from handlers.filter import MyCallback
from lexicon.lexicon_ru import LEXICON_RU

kb_start: InlineKeyboardBuilder = InlineKeyboardBuilder()

saved_passwords: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_saved_passwords'],
                                                             callback_data=MyCallback(a='saved_passwords').pack())

generate_password: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_generate_password'],
                                                               callback_data=MyCallback(a='generate_password').pack())

check_password: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_check_password'],
                                                            callback_data=MyCallback(a='check_password').pack())

give_advices: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_give_advices'],
                                                          callback_data=MyCallback(a='give_advices').pack())
buttons_start: list = [generate_password, check_password, give_advices, saved_passwords]
kb_start.row(*buttons_start, width=1)

kb_generate: InlineKeyboardBuilder = InlineKeyboardBuilder()

save_password: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['save_password'],
                                                           callback_data=MyCallback(a='save_password').pack())

another_password: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_another_password'],
                                                              callback_data=MyCallback(a='another_password').pack())

menu: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_menu'],
                                                  callback_data=MyCallback(a='menu').pack())
buttons_generate: list = [save_password, another_password, menu]
kb_generate.row(*buttons_generate, width=1)

kb_check_password: InlineKeyboardBuilder = InlineKeyboardBuilder()
kb_check_password.button(text=LEXICON_RU['button_menu'],
                         callback_data=MyCallback(a='menu').pack())

kb_give_advices: InlineKeyboardBuilder = InlineKeyboardBuilder()
menu: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_menu'],
                                                  callback_data=MyCallback(a='menu').pack())

next_advice1: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_next'],
                                                          callback_data=MyCallback(a='next_advice1').pack())
buttons_give_advice1: list = [next_advice1, menu]
kb_give_advices.row(*buttons_give_advice1, width=1)

kb_give_advice2: InlineKeyboardBuilder = InlineKeyboardBuilder()
menu: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_menu'],
                                                  callback_data=MyCallback(a='menu').pack())

next_advice2: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_next'],
                                                          callback_data=MyCallback(a='next_advice2').pack())
buttons_give_advice2: list = [next_advice2, menu]
kb_give_advice2.row(*buttons_give_advice2, width=1)

kb_give_advice3: InlineKeyboardBuilder = InlineKeyboardBuilder()
menu: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_menu'],
                                                  callback_data=MyCallback(a='menu').pack())

next_advice3: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_next'],
                                                          callback_data=MyCallback(a='next_advice3').pack())
buttons_give_advice3: list = [next_advice3, menu]
kb_give_advice3.row(*buttons_give_advice3, width=1)

kb_give_advice4: InlineKeyboardBuilder = InlineKeyboardBuilder()
menu: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_menu'],
                                                  callback_data=MyCallback(a='menu').pack())

next_advice4: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_next'],
                                                          callback_data=MyCallback(a='next_advice4').pack())
buttons_give_advice4: list = [next_advice4, menu]
kb_give_advice4.row(*buttons_give_advice4, width=1)

kb_give_advice5: InlineKeyboardBuilder = InlineKeyboardBuilder()
menu: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_menu'],
                                                  callback_data=MyCallback(a='menu').pack())

next_advice5: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_next'],
                                                          callback_data=MyCallback(a='next_advice5').pack())
buttons_give_advice5: list = [next_advice5, menu]
kb_give_advice5.row(*buttons_give_advice5, width=1)

kb_before_comic: InlineKeyboardBuilder = InlineKeyboardBuilder()
menu: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_menu'],
                                                  callback_data=MyCallback(a='menu').pack())
bonus_message: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_bonus_message'],
                                                           callback_data=MyCallback(a='bonus_message').pack())
buttons_before_comic: list = [bonus_message, menu]
kb_before_comic.row(*buttons_before_comic, width=1)

kb_advices_end: InlineKeyboardBuilder = InlineKeyboardBuilder()
kb_advices_end.button(text=LEXICON_RU['button_menu'],
                      callback_data=MyCallback(a='menu').pack())

kb_checked_password: InlineKeyboardBuilder = InlineKeyboardBuilder()
check_password: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_check_password'],
                                                            callback_data=MyCallback(a='check_password').pack())

menu: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_menu'],
                                                  callback_data=MyCallback(a='menu').pack())
buttons_checked_password: list = [check_password, menu]
kb_checked_password.row(*buttons_checked_password, width=1)

kb_saved_passwords: InlineKeyboardBuilder = InlineKeyboardBuilder()
remove_password: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['remove_password'],
                                                             callback_data=MyCallback(a='remove_password').pack())
menu: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_menu'],
                                                  callback_data=MyCallback(a='menu').pack())
buttons_saved_passwords: list = [remove_password, menu]
kb_saved_passwords.row(*buttons_saved_passwords, width=1)

kb_removing_password: InlineKeyboardBuilder = InlineKeyboardBuilder()
menu: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_menu'],
                                                  callback_data=MyCallback(a='menu').pack())
buttons_removing_password: list = [menu]
kb_removing_password.row(*buttons_removing_password, width=1)
