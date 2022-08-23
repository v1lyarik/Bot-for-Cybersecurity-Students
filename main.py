import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentTypes
from aiogram.types.message import ContentType
from aiogram.types import CallbackQuery
import markups as nav

token = '5514598490:AAHGay8NjptSpb-oaMdH8QCe1qgQBRHDd9A'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start (message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, f'Привіт, я бот програми "Лабки за бабки"\nВибери свою спеціалізацію. \n \nЗа питаннями, пропозиціями, скаргами писати @v1lyarik 🫡', reply_markup=nav.mainMenu)
        

@dp.callback_query_handler(text="BackMenu")
async def back_Menu (message: types.Message):
    await bot.send_message(message.from_user.id, f'Вибери свій спеціалізацію.', reply_markup=nav.mainMenu)
    
@dp.callback_query_handler(text="BackZi")
async def back_Zi (message: types.Message):
    await bot.send_message(message.from_user.id, f'Вибери свій предмет.', reply_markup=nav.lessonsMenuZi)

@dp.callback_query_handler(text="BackAck")
async def back_Ack(message: types.Message):
    await bot.send_message(message.from_user.id, f'Вибери свій предмет.', reply_markup=nav.lessonsMenuAck)

@dp.callback_query_handler(text="BackUI")
async def back_Ui(message: types.Message):
    await bot.send_message(message.from_user.id, f'Вибери свій предмет.', reply_markup=nav.lessonsMenuUi)
    
@dp.callback_query_handler(text="BackBIT")
async def back_bit(message: types.Message):
    await bot.send_message(message.from_user.id, f'Вибери свій предмет.', reply_markup=nav.lessonsMenuBit)
    
    
#ZI        
@dp.callback_query_handler(text="ZI")
async def zi(message:types.message):
    await bot.send_message(message.from_user.id, "З якого предмету потрібна допомога?", reply_markup=nav.lessonsMenuZi)
    
@dp.callback_query_handler(text="zi_incedent")
async def zi_incident(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nБогдан Фіголь @Sir_fidelity", parse_mode='html', reply_markup=nav.buttonBLZi)

@dp.callback_query_handler(text="zi_methodsOfDefense")
async def zzi_methodsOfDefense(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nБогдан Фіголь @Sir_fidelity", parse_mode='html', reply_markup=nav.buttonBLZi)
    
@dp.callback_query_handler(text="zi_workDef")
async def zzi_workDef(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nБогдан Фіголь @Sir_fidelity", parse_mode='html', reply_markup=nav.buttonBLZi)
    
@dp.callback_query_handler(text="zi_arch")
async def zzi_arch(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nБогдан Фіголь @Sir_fidelity", parse_mode='html', reply_markup=nav.buttonBLZi)
    
@dp.callback_query_handler(text="z_itTech")
async def zz_itTech(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nБогдан Фіголь @Sir_fidelity", parse_mode='html', reply_markup=nav.buttonBLZi)
    
@dp.callback_query_handler(text="zi_predictions")
async def i_predictions(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nБогдан Фіголь @Sir_fidelity", parse_mode='html', reply_markup=nav.buttonBLZi)

#UI       
@dp.callback_query_handler(text="UI")
async def ui(message:types.message):
    await bot.send_message(message.from_user.id, "З якого предмету потрібна допомога?", reply_markup=nav.lessonsMenuUi) 
@dp.callback_query_handler(text="ui_arch")
async def ui_arch(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLUi)
@dp.callback_query_handler(text="ui_safety")
async def ui_safety(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLUi)    
@dp.callback_query_handler(text="ui_tools")
async def ui_tools(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLUi)    
@dp.callback_query_handler(text="ui_defInfo")
async def ui_defInfo(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLUi)    
@dp.callback_query_handler(text="ui_crypto")
async def ui_crypto(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLUi)   
    
#ACK       
@dp.callback_query_handler(text="ACK")
async def ack(message:types.message):
    await bot.send_message(message.from_user.id, "З якого предмету потрібна допомога?", reply_markup=nav.lessonsMenuAck) 
@dp.callback_query_handler(text="ack_incident")
async def ack_incident(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLAck)
@dp.callback_query_handler(text="ack_defTool")
async def ack_defTool(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLAck)    
@dp.callback_query_handler(text="ack_workDef")
async def ack_workDef(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLAck)    
@dp.callback_query_handler(text="ack_arch")
async def ack_arch(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLAck)    
@dp.callback_query_handler(text="ack_methodsOfDefense")
async def ack_methodsOfDefense(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLAck) 
    
#BIT       
@dp.callback_query_handler(text="BIT")
async def bit(message:types.message):
    await bot.send_message(message.from_user.id, "З якого предмету потрібна допомога?", reply_markup=nav.lessonsMenuBit) 
@dp.callback_query_handler(text="bit_incedents")
async def ack_incident(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nОлександр Волотовський @obitoihikki", parse_mode='html', reply_markup=nav.buttonBLBit)
@dp.callback_query_handler(text="bit_cryptology")
async def bit_cryptology(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLBit)    
@dp.callback_query_handler(text="bit_workDef")
async def bit_workDef(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLBit)    
@dp.callback_query_handler(text="bit_methods")
async def bit_methods(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLBit)    
@dp.callback_query_handler(text="bit_arch")
async def bit_arch(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLBit) 
    
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
