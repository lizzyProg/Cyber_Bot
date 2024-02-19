import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers


logger = logging.getLogger(__name__)


async def main():
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()
    dp.include_router(user_handlers.router)
    await dp.start_polling(bot)
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')


logger.info('Starting bot')

config: Config = load_config()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')
