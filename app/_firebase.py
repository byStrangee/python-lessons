from config import auth, db

from utils import write_data, get_data, sign_up, sign_in, add_new_user

from bot import bot, dp, executor, types

    
@dp.message_handler(commands=['start'])
async def send(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    print(message["from"]['id'])
    await message.reply("Hi!\nYou can simply enter /login or /signup command")
    
@dp.message_handler(commands=['help'])
async def send(message: types.Message):
    await message.reply('/login - login an exciting account\n/signup - register a new account')
    
    
@dp.message_handler(commands=['signup'])
async def send(message: types.Message):
    await message.reply('Enter email')

    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)