import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentTypes
from aiogram.types.message import ContentType
from aiogram.types import CallbackQuery
import markups as nav

token = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start (message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, f'Привіт, я бот програми "Лабки за бабки"\nВибери свою спеціалізацію. \n \nЗа питаннями, пропозиціями, скаргами писати @v1lyarik 🫡', reply_markup=nav.mainMenu)
        

'''_______________________________________________________________________________________________________''' 

@dp.callback_query_handler(text="BackMenu")
async def back_Menu (message: types.Message):
    await bot.send_message(message.from_user.id, f'Вибери свою спеціалізацію.', reply_markup=nav.mainMenu)
    
@dp.callback_query_handler(text="BackUi2")
async def back_Ui2(message: types.Message):
    await bot.send_message(message.from_user.id, f'Вибери свій предмет.', reply_markup=nav.lessonsMenu2Ui)

@dp.callback_query_handler(text="BackZi")
async def back_Zi(message: types.Message):
    await bot.send_message(message.from_user.id, f'Вибери свій предмет.', reply_markup=nav.lessonsMenuZi)

@dp.callback_query_handler(text="BackAck")
async def back_Ack(message: types.Message):
    await bot.send_message(message.from_user.id, f'Вибери свій предмет.', reply_markup=nav.lessonsMenuAck)

@dp.callback_query_handler(text="BackAck2")
async def back_Ack2(message: types.Message):
    await bot.send_message(message.from_user.id, f'Вибери свій предмет.', reply_markup=nav.lessonsMenu2Ack)
    
@dp.callback_query_handler(text="BackZi2")
async def back_Zi2(message: types.Message):
    await bot.send_message(message.from_user.id, f'Вибери свій предмет.', reply_markup=nav.lessonsMenu2Zi)

@dp.callback_query_handler(text="BackUI")
async def back_Ui(message: types.Message):
    await bot.send_message(message.from_user.id, f'Вибери свій предмет.', reply_markup=nav.lessonsMenuUi)
    
@dp.callback_query_handler(text="BackBIT")
async def back_bit(message: types.Message):
    await bot.send_message(message.from_user.id, f'Вибери свій предмет.', reply_markup=nav.lessonsMenuBit)
    
@dp.callback_query_handler(text="BackBit2")
async def back_bit2(message: types.Message):
    await bot.send_message(message.from_user.id, f'Вибери свій предмет.', reply_markup=nav.lessonsMenu2Bit)
    
'''_______________________________________________________________________________________________________''' 
#ZI        
@dp.callback_query_handler(text="ZI")
async def zzi(message:types.message):    
    await bot.send_message(message.from_user.id, "Який ти курс?", reply_markup=nav.btnCourseZi)

#ZI2
@dp.callback_query_handler(text="2CourseZi")
async def course2lessZI(message:types.message):
    await bot.send_message(message.from_user.id, "З якого предмета потрібна допомога?", reply_markup=nav.lessonsMenu2Zi)

@dp.callback_query_handler(text="networkZi2")
async def zi_network(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLZi2)

@dp.callback_query_handler(text="tikZi2")
async def tikZi2(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLZi2)    
    
@dp.callback_query_handler(text="metrologyZi2")
async def metrologyZi2(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLZi2)
#zi3
@dp.callback_query_handler(text="3CourseZi")
async def course3lessZI(message:types.message):
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
'''_______________________________________________________________________________________________________''' 

#UI       
       
@dp.callback_query_handler(text="UI")
async def ui(message:types.message):    
    await bot.send_message(message.from_user.id, "Який ти курс?", reply_markup=nav.btnCourseUi)

#UI2
@dp.callback_query_handler(text="2CourseUi")
async def course2lessUI(message:types.message):
    await bot.send_message(message.from_user.id, "З якого предмета потрібна допомога?", reply_markup=nav.lessonsMenu2Ui)

@dp.callback_query_handler(text="networkUi2")
async def networkUi2(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLUi2)

@dp.callback_query_handler(text="tikUi2")
async def tikUi2(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLUi2)    
    
@dp.callback_query_handler(text="teamUi2")
async def teamUi2(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLUi2)
    
@dp.callback_query_handler(text="3CourseUi")
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
'''_______________________________________________________________________________________________________''' 

#ACK       
@dp.callback_query_handler(text="ACK")
async def ack(message:types.message):    
    await bot.send_message(message.from_user.id, "Який ти курс?", reply_markup=nav.btnCourseAck)

#UI2
@dp.callback_query_handler(text="2CourseAck")
async def course2lessAck(message:types.message):
    await bot.send_message(message.from_user.id, "З якого предмета потрібна допомога?", reply_markup=nav.lessonsMenu2Ack)

@dp.callback_query_handler(text="networkAck2")
async def networkAck2(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLAck2)

@dp.callback_query_handler(text="tikAck2")
async def tikAck2(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLAck2)    
    
@dp.callback_query_handler(text="teamAck2")
async def teamAck2(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLAck2)
    
@dp.callback_query_handler(text="schemeAck2")
async def schemeAck2(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLAck2) 
    
@dp.callback_query_handler(text="philosophyAck2")
async def philosophyAck2(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLAck2)
    

    
@dp.callback_query_handler(text="3CourseAck")
async def ack3(message:types.message):
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
'''_______________________________________________________________________________________________________''' 

#BIT 
@dp.callback_query_handler(text="BIT")
async def zi(message:types.message):    
    await bot.send_message(message.from_user.id, "Який ти курс?", reply_markup=nav.btnCourseBit)

#BIT2
@dp.callback_query_handler(text="2CourseBit")
async def course2lessUI(message:types.message):
    await bot.send_message(message.from_user.id, "З якого предмета потрібна допомога?", reply_markup=nav.lessonsMenu2Bit)

@dp.callback_query_handler(text="networkBit2")
async def networkBit2(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLBit2)

@dp.callback_query_handler(text="tikBit2")
async def tikBit2(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLBit2)    
    
@dp.callback_query_handler(text="schemeBit2")
async def schemeBit2(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLBit2)
    
@dp.callback_query_handler(text="philosophyBit2")
async def philosophyBit2(message:types.message):
    await bot.send_message(message.from_user.id, f"<b>Список виконавців:</b> \nEmpty Field", parse_mode='html', reply_markup=nav.buttonBLBit2)
          
@dp.callback_query_handler(text="3CourseBit")
async def bit(message:types.message):
    await bot.send_message(message.from_user.id, "З якого предмету потрібна допомога?", reply_markup=nav.lessonsMenuBit ) 
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
