from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message
from aiogram.filters import BaseFilter
# from handlers.user_handlers import *


class MyCallback(CallbackData, prefix='pressed_button_'):
    a: str

# class Filter1(BaseFilter):
    # async def __call__(self, message: Message):
        # return int(message.text) in range(1, 100)


'''
class Filter2(BaseFilter):
    def __init__(self) -> None:
        global users_codeword1
        self.codeword = users_codeword1
        print(self.codeword)

    async def __call__(self, message: Message) -> bool:
        return self.codeword == message.text
'''