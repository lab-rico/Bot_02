from aiogram.utils import executor
from bot_app.create_bot import dp
from bot_app import commands, other

#


commands.register_handlers_client(dp)
#other.on_startup(dp)
#other.register_handlers_client(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
