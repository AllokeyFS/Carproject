import requests
from aiogram import Bot, Dispatcher
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, Contact
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage



bot = Bot(token='')
dp = Dispatcher(bot, storage=MemoryStorage())
req_ip = 'http://192.168.31.230:8000'
# req_ip = 'http://192.168.1.104:8000'

# keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
# keyboard.add('')

keyboard_sub = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_sub.add('Subscribe')
keyboard_sub.add('Mailing')
keyboard_sub.add('Off')
keyboard_sub.add('On')
keyboard_unsub = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_unsub.add('Unsubscribe')
keyboard_unsub.add('Mailing')
keyboard_unsub.add('Off')
keyboard_unsub.add('On')




class Registration:
    def __init__(self, message: Message):
        self.message = message


    async def registration_users(self, message: Message):
        class RegistrationState(StatesGroup):
            phone = State()


        await RegistrationState.phone.set()
        keyboard_num = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard_num.add(KeyboardButton('Отправить номер телефона', request_contact=True))
        await message.answer('Пожалуйста, отправьте номер телефона для регистрации', reply_markup=keyboard_num)


        @dp.message_handler(content_types=types.ContentType.CONTACT, state=RegistrationState.phone)
        async def phone_state(message: Message, state: FSMContext):
            async with state.proxy() as data:
                data['phone'] = message.contact.phone_number
                phone = data['phone']
                await message.answer(f'Вы успешно зарегистрированы\nВызовите меню старта\nВаш номер{phone}', reply_markup=keyboard_sub)
                user_id = message.from_user.id
                first_name = message.from_user.first_name
                data_user = {
                    "nickname": first_name,
                    "user_id": user_id,
                    "phone_number": phone
                    }
                req = requests.post(f'{req_ip}/telegram/telegramuser/', data=data_user)
                if req.status_code == 201:
                    await bot.send_message(message.from_user.id, 'Welcome!', reply_markup=keyboard_sub)
                else:
                    await message.answer('ERROR')
            await state.finish()



@dp.message_handler(commands='start')
async def start_command(message: Message):
    user_id = message.from_user.id
    check_user = requests.get(f'{req_ip}/telegram/telegramuser/?user_id={user_id}').json()
    check_sub = requests.get(f'{req_ip}/telegram/mailing/?user__user_id={user_id}').json()
    if check_sub:
        await message.answer('In data', reply_markup=keyboard_unsub)
    if check_user:
        await bot.send_message(message.from_user.id, 'In database', reply_markup=keyboard_sub)
    else:
        registration = Registration(message)
        await registration.registration_users(message)



@dp.message_handler(text='Subscribe')
async def subscription(message: Message):
    user_id = message.from_user.id
    data = {
    "user": user_id,
    "is_active": True
    }
    check_sub = requests.get(f'{req_ip}/telegram/mailing/?user__user_id={user_id}').json()
    check_user = requests.get(f'{req_ip}/telegram/telegramuser/?user_id={user_id}').json()
    check_falsesub = requests.get(f'{req_ip}/telegram/mailingfalse/?user__user_id={user_id}').json()
    if not check_user:
        return await message.answer('Not in database, press /start') 
    if check_sub or check_falsesub:
        return await bot.send_message(message.from_user.id ,'Subscribed', reply_markup=keyboard_unsub)
    # elif check_falsesub:
    #     return await bot.send_message(message.from_user.id ,'Subscribed', reply_markup=keyboard_unsub)
    register = requests.post(f'{req_ip}/telegram/mailing/', data=data)
    if register.status_code == 201:
        await bot.send_message(message.from_user.id ,'Subscribed', reply_markup=keyboard_unsub,)
    else:
        await message.answer('ERROR')



@dp.message_handler(text='Unsubscribe')
async def unsubscription(message: Message):
    user_id = message.from_user.id
    check_sub = requests.get(f'{req_ip}/telegram/mailing/?user__user_id={user_id}').json()
    # check_falsesub = requests.get(f'{req_ip}/telegram/mailingfalse/?user__user_id={user_id}').json()
    if not check_sub:
        return await message.answer('Not in database, please subscribe', reply_markup=keyboard_sub)
    sub_id = check_sub[0]['id']
    # false_sub_id = check_falsesub[0]['id']
    
    delete_sub = requests.delete(f'{req_ip}/telegram/mailing/{sub_id}/')
    # delete_false_sub = requests.delete(f'{req_ip}/telegram/mailing/{false_sub_id}/')
    if delete_sub.status_code == 204:
        await message.answer('Unsubscribed', reply_markup=keyboard_sub)
    else:
        await message.answer('Try again')



@dp.message_handler(text='Mailing')
async def mailing_list(message: Message):
    class Mailing(StatesGroup):
        mailing_text = State()


    
    if message.from_user.id == 573015206:
        await Mailing.mailing_text.set()
        await bot.send_message(message.from_user.id, 'Enter')

        @dp.message_handler(state=Mailing.mailing_text)
        async def mailing(message: Message, state: FSMContext):
            async with state.proxy() as data:
                success = 0
                fail = 0
                data['mailing_text'] = message.text
                mailing_text = data['mailing_text']
                check_sub = requests.get(f'{req_ip}/telegram/mailing/').json()
                await state.finish()
            for item in check_sub:
                
                try:
                    success +=1
                    await bot.send_message(item['user'], text=mailing_text)
                except Exception:
                    fail += 1
                    continue
            await bot.send_message(message.from_user.id, text=f'Данные о рассылки\n Текст: {mailing_text}\n✅Успешно: {success}\n❌Ошибки: {fail}\nРассылка завершенна🔔') 
    else:
        await bot.send_message(message.from_user.id, text='Рассылка недоступна')




    # check_sub = requests.get(f'{req_ip}/telegram/mailing/').json()
    # # print(check_sub)
    # if message.from_user.id == 573015206:
    #     for user_id in check_sub:
    #         try:
    #             await bot.send_message(user_id['user'], 'Text')
    #         except Exception:
    #             continue

@dp.message_handler(text='Off')
async def unmailing_list(message: Message):
    user_id = message.from_user.id
    check_sub = requests.get(f'{req_ip}/telegram/mailing/?user__user_id={user_id}').json()
    if not check_sub:
        return await message.answer('Not in database')
    id_sub = check_sub[0]['id']
    patch_sub = requests.patch(f'{req_ip}/telegram/mailing/{id_sub}/', data={'is_active': False})
    if patch_sub.status_code == 200:
        await message.answer('Success', reply_markup=keyboard_unsub)
    else:
        await message.answer('Try again')

@dp.message_handler(text='On')
async def unmailing_list(message: Message):
    user_id = message.from_user.id
    check_sub = requests.get(f'{req_ip}/telegram/mailingfalse/?user__user_id={user_id}').json()
    if not check_sub:
        return await message.answer('Not in database')
    id_sub = check_sub[0]['id']
    patch_sub = requests.patch(f'{req_ip}/telegram/mailingfalse/{id_sub}/', data={'is_active': True})
    if patch_sub.status_code == 200:
        await message.answer('Success', reply_markup=keyboard_unsub)
    else:
        await message.answer('Try again')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)