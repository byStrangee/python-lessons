from utils import write_data, get_data, sign_up, sign_in, add_new_user, login

from bot import bot, dp, executor, types

from json import loads
    
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
    
command = {
    'signup': {
        'email': False,
        'password': False,
        'success': None
    },
    'signin': {
        'email': False,
        'password': False,
        'success': None
    }
}    

data = {
    'email': '',
    'password': ''
}


@dp.message_handler(commands=['login'])
async def send(message: types.Message):

    data['email'] = ''
    
    data['password'] = ''
    
    await message.reply('Welcome back!\nEnter email')
    
    command['signin']['email'] = True
    
    command['signup']['email'] = False
    
    command['signup']['password'] = False


    @dp.message_handler(commands=['signup'])
async def send(message: types.Message):
    data['email'] = ''
    
    data['password'] = ''
    
    await message.reply('Enter email')
    
    command['signup']['email'] = True
    
    command['signin']['email'] = False
    
    command['signin']['password'] = False
    
@dp.message_handler()
async def send(message: types.Message):
    
    if command['signup']['email']:
        
        data['email'] = message.text
        
        command['signup']['password'] = True
        
        command['signup']['email'] = False
        
        await message.reply('Enter your password')
    
    elif command['signup']['password']:
        
        command['signup']['password'] = False
        
        data['password'] = message.text
        
        await message.reply('Wait registering new account')
    
        user_info = loads(str(message['from']))
    
        user_info['email'] = data['email']
        
        user_id = user_info['id']
        
        _auth = add_new_user(data['email'], data['password'], user_id, user_info)
        
        if _auth:
        
            await message.reply('Succesfully registered')
        
        else:
        
            await message.reply('Failure. Maybe you are trying to signup exciting account. Try again')

    
    if command['signin']['email']:
    
        data['email'] = message.text
        
        command['signin']['password'] = True
        
        await message.reply('Enter you password')
        
        command['signin']['email'] = False
    
    elif command['signin']['password']:
    
        command['signin']['password'] = False
        
        data['password'] = message.text
        
        await message.reply('Logging in please wait...')
        
        user_id = message['from']['id']
        
        _auth = login(data['email'], data['password'], user_id)
        
        if _auth:
        
            await message.reply('succesfully logged in')
            
            await message.reply('Your informations on my database')
            
            _message = ''
            
            for i, k in _auth.get().val().items():
            
                _message += (f"{i}: {k}\n")
            
            else:
            
                await message.reply(_message)
        
        print(_auth)
        
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)