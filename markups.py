from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mainMenu = InlineKeyboardMarkup(row_width=1)
btnAsk = InlineKeyboardButton(text="АСК 🎷", callback_data="ACK")
btnBit = InlineKeyboardButton(text="БІТ 🩻", callback_data="BIT")
btnUi = InlineKeyboardButton(text="УІ ✨", callback_data="UI")
btnZi = InlineKeyboardButton(text="ЗІ ⚡️", callback_data="ZI")

btnBack = InlineKeyboardButton(text="Назад в меню ↩️", callback_data="BackMenu")
btnBackLZi = InlineKeyboardButton(text="Назад в перелік предметів ↩️", callback_data="BackZi")
btnBackLAck = InlineKeyboardButton(text="Назад в перелік предметів ↩️", callback_data="BackAck")
btnBackLUi = InlineKeyboardButton(text="Назад в перелік предметів ↩️", callback_data="BackUI")
btnBackLBit = InlineKeyboardButton(text="Назад в перелік предметів ↩️", callback_data="BackBIT")

buttonBM = InlineKeyboardMarkup(row_width=1)
buttonBLZi= InlineKeyboardMarkup(row_width=1)
buttonBLAck= InlineKeyboardMarkup(row_width=1)
buttonBLUi = InlineKeyboardMarkup(row_width=1)
buttonBLBit = InlineKeyboardMarkup(row_width=1)

buttonBLUi.insert(btnBackLUi)
buttonBM.insert(btnBack)
buttonBLZi.insert(btnBackLZi)
buttonBLAck.insert(btnBackLAck)
buttonBLBit.insert(btnBackLBit)

lessonsMenuZi = InlineKeyboardMarkup(row_width=1)
incidentResponse = InlineKeyboardButton(text="Технології розслідування інцидентів інформаційної безпеки", callback_data="zi_incedent")
methodsDefense = InlineKeyboardButton(text="Методи та засоби захисту інформації", callback_data="zi_methodsOfDefense")
workDef = InlineKeyboardButton(text="Основи охорони праці та безпека життєдіяльності", callback_data="zi_workDef")
zi_architecture = InlineKeyboardButton(text="Архітектура комп'ютерних систем", callback_data="zi_arch")
it_tech = InlineKeyboardButton(text="Основи інформаційно-телекомунікаційних технологій", callback_data="z_itTech")
zi_predictions = InlineKeyboardButton(text="Прогноз та моделювання в соціальній сфері та забезпечення неперервності ІБ бізнесу", callback_data="zi_predictions")

lessonsMenuAck = InlineKeyboardMarkup(row_width=1)
incidentResponse_ack = InlineKeyboardButton(text="Технології розслідування інцидентів інформаційної безпеки", callback_data="ack_incident")
defTool = InlineKeyboardButton(text="Інструменти мережевої безпеки", callback_data="ack_defTool")
ack_workDef = InlineKeyboardButton(text="Основи охорони праці та безпека життєдіяльності", callback_data="ack_workDef")
ack_architecture = InlineKeyboardButton(text="Архітектура комп'ютерних систем", callback_data="ack_arch")
methodDef = InlineKeyboardButton(text="Методи та засоби захисту інформації", callback_data="ack_methodsOfDefense")

lessonsMenuUi = InlineKeyboardMarkup(row_width=1)
ui_defInfo = InlineKeyboardButton(text="Методи та засоби захисту інформації", callback_data="ui_defInfo")
ui_crypto = InlineKeyboardButton(text="Криптографічні системи та протоколи", callback_data="ui_crypto")
ui_arch = InlineKeyboardButton(text="Архітектура комп`ютерних систем", callback_data="ui_arch")
ui_tools = InlineKeyboardButton(text="Засоби приймання,передавання та обробки інформації в системах технічного захисту інформації", callback_data="ui_tools")
ui_safety = InlineKeyboardButton(text="Безпека інфраструктури комп`ютерних мереж", callback_data="ui_safety")

lessonsMenuBit = InlineKeyboardMarkup(row_width=1)
bit_incedents = InlineKeyboardButton(text="Технології розслідування інцидентів" , callback_data="bit_incedents")
bit_cryptology = InlineKeyboardButton(text="Алгоритмічні основи криптології", callback_data="bit_cryptology")
bit_workDef = InlineKeyboardButton(text="Основи охорони праці", callback_data="bit_workDef")
bit_methods = InlineKeyboardButton(text="Методи та засоби технічного захисту інформації", callback_data="bit_methods")
bit_arch = InlineKeyboardButton(text="Архітектура комп`ютерних систем", callback_data="bit_arch")

mainMenu.insert(btnZi)
mainMenu.insert(btnUi)
mainMenu.insert(btnAsk)
mainMenu.insert(btnBit)

lessonsMenuZi.insert(incidentResponse)
lessonsMenuZi.insert(methodsDefense)
lessonsMenuZi.insert(workDef)
lessonsMenuZi.insert(zi_architecture)
lessonsMenuZi.insert(it_tech)
lessonsMenuZi.insert(zi_predictions)
lessonsMenuZi.insert(btnBack)

lessonsMenuAck.insert(incidentResponse_ack)
lessonsMenuAck.insert(defTool)
lessonsMenuAck.insert(ack_workDef)
lessonsMenuAck.insert(ack_architecture)
lessonsMenuAck.insert(methodDef)
lessonsMenuAck.insert(btnBack)

lessonsMenuUi.insert(ui_arch)
lessonsMenuUi.insert(ui_safety)
lessonsMenuUi.insert(ui_tools)
lessonsMenuUi.insert(ui_defInfo)
lessonsMenuUi.insert(ui_crypto)
lessonsMenuUi.insert(btnBack)

lessonsMenuBit.insert(bit_incedents)
lessonsMenuBit.insert(bit_cryptology)
lessonsMenuBit.insert(bit_workDef)
lessonsMenuBit.insert(bit_methods)
lessonsMenuBit.insert(bit_arch)
lessonsMenuBit.insert(btnBack)