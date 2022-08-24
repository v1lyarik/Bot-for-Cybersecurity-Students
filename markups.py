from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mainMenu = InlineKeyboardMarkup(row_width=1)
btnAsk = InlineKeyboardButton(text="АСК 🎷", callback_data="ACK")
btnBit = InlineKeyboardButton(text="БІТ 🩻", callback_data="BIT")
btnUi = InlineKeyboardButton(text="УІ ✨", callback_data="UI")
btnZi = InlineKeyboardButton(text="ЗІ ⚡️", callback_data="ZI")

btnBack = InlineKeyboardButton(text="Назад в меню ↩️", callback_data="BackMenu")
btnBackLZi = InlineKeyboardButton(text="Назад в перелік предметів ↩️", callback_data="BackZi")
btnBackLZi2 = InlineKeyboardButton(text="Назад в перелік предметів ↩️", callback_data="BackZi2")
btnBackLAck = InlineKeyboardButton(text="Назад в перелік предметів ↩️", callback_data="BackAck")
btnBackLAck2 = InlineKeyboardButton(text="Назад в перелік предметів ↩️", callback_data="BackAck2")
btnBackLUi = InlineKeyboardButton(text="Назад в перелік предметів ↩️", callback_data="BackUI")
btnBackLUi2 = InlineKeyboardButton(text="Назад в перелік предметів ↩️", callback_data="BackUi2")
btnBackLBit = InlineKeyboardButton(text="Назад в перелік предметів ↩️", callback_data="BackBIT")
btnBackLBit2 = InlineKeyboardButton(text="Назад в перелік предметів ↩️", callback_data="BackBit2")

buttonBM = InlineKeyboardMarkup(row_width=1)
buttonBLZi= InlineKeyboardMarkup(row_width=1)
buttonBLZi2 = InlineKeyboardMarkup(row_width=1)
buttonBLAck = InlineKeyboardMarkup(row_width=1)
buttonBLAck2 = InlineKeyboardMarkup(row_width=1)
buttonBLUi = InlineKeyboardMarkup(row_width=1)
buttonBLUi2 = InlineKeyboardMarkup(row_width=1)
buttonBLBit = InlineKeyboardMarkup(row_width=1)
buttonBLBit2 = InlineKeyboardMarkup(row_width=1)



buttonBLUi.insert(btnBackLUi)
buttonBLUi2.insert(btnBackLUi2)
buttonBLUi.insert(btnBackLUi)
buttonBM.insert(btnBack)
buttonBLZi.insert(btnBackLZi)
buttonBLZi2.insert(btnBackLZi2)
buttonBLAck.insert(btnBackLAck)
buttonBLAck2.insert(btnBackLAck2)
buttonBLBit.insert(btnBackLBit)
buttonBLBit2.insert(btnBackLBit2)


btnCourseUi = InlineKeyboardMarkup(row_width=1)
btn2courseu = InlineKeyboardButton(text="2 Курс", callback_data="2CourseUi")
btn3courseu = InlineKeyboardButton(text="3 Курс", callback_data="3CourseUi")
btnCourseUi.insert(btn2courseu)
btnCourseUi.insert(btn3courseu)


btnCourseAck = InlineKeyboardMarkup(row_width=1)
btn2coursea = InlineKeyboardButton(text="2 Курс", callback_data="2CourseAck")
btn3coursea = InlineKeyboardButton(text="3 Курс", callback_data="3CourseAck")
btnCourseAck.insert(btn2coursea)
btnCourseAck.insert(btn3coursea)


btnCourseBit = InlineKeyboardMarkup(row_width=1)
btn2courseb = InlineKeyboardButton(text="2 Курс", callback_data="2CourseBit")
btn3courseb = InlineKeyboardButton(text="3 Курс", callback_data="3CourseBit")
btnCourseBit.insert(btn2courseb)
btnCourseBit.insert(btn3courseb)


btnCourseZi = InlineKeyboardMarkup(row_width=1)
btn2coursez = InlineKeyboardButton(text="2 Курс", callback_data="2CourseZi")
btn3coursez = InlineKeyboardButton(text="3 Курс", callback_data="3CourseZi")
btnCourseZi.insert(btn2coursez)
btnCourseZi.insert(btn3coursez)


lessonsMenu2Zi = InlineKeyboardMarkup(row_width=1)
tikZi2 = InlineKeyboardButton(text="Теорія інформації і кодування", callback_data="tikZi2")
networkZi2 = InlineKeyboardButton(text="Комп'ютерні мережі", callback_data="networkZi2")
metrologyZi2 = InlineKeyboardButton(text="Метрологія та вимірювальна техніка", callback_data="metrologyZi2")
schemeZi2 = InlineKeyboardButton(text="Схемотехніка", callback_data="schemeZi2")

lessonsMenuZi = InlineKeyboardMarkup(row_width=1)
incidentResponse = InlineKeyboardButton(text="Технології розслідування інцидентів інформаційної безпеки", callback_data="zi_incedent")
methodsDefense = InlineKeyboardButton(text="Методи та засоби захисту інформації", callback_data="zi_methodsOfDefense")
workDef = InlineKeyboardButton(text="Основи охорони праці та безпека життєдіяльності", callback_data="zi_workDef")
zi_architecture = InlineKeyboardButton(text="Архітектура комп'ютерних систем", callback_data="zi_arch")
it_tech = InlineKeyboardButton(text="Основи інформаційно-телекомунікаційних технологій", callback_data="z_itTech")
zi_predictions = InlineKeyboardButton(text="Прогноз та моделювання в соціальній сфері та забезпечення неперервності ІБ бізнесу", callback_data="zi_predictions")

lessonsMenu2Ack = InlineKeyboardMarkup(row_width=1)
tikAck2 = InlineKeyboardButton(text="Теорія інформації і кодування", callback_data="tikAck2")
networkAck2 = InlineKeyboardButton(text="Комп'ютерні мережі", callback_data="networkAck2")
teamAck2 = InlineKeyboardButton(text="Командна робота", callback_data="teamAck2")
schemeAck2 = InlineKeyboardButton(text="Схемотехніка", callback_data="schemeAck2")
philosophyAck2 = InlineKeyboardButton(text="Філософія", callback_data="philosophyAck2")



lessonsMenuAck = InlineKeyboardMarkup(row_width=1)
incidentResponse_ack = InlineKeyboardButton(text="Технології розслідування інцидентів інформаційної безпеки", callback_data="ack_incident")
defTool = InlineKeyboardButton(text="Інструменти мережевої безпеки", callback_data="ack_defTool")
ack_workDef = InlineKeyboardButton(text="Основи охорони праці та безпека життєдіяльності", callback_data="ack_workDef")
ack_architecture = InlineKeyboardButton(text="Архітектура комп'ютерних систем", callback_data="ack_arch")
methodDef = InlineKeyboardButton(text="Методи та засоби захисту інформації", callback_data="ack_methodsOfDefense")



lessonsMenu2Ui = InlineKeyboardMarkup(row_width=1)
tikUi2 = InlineKeyboardButton(text="Теорія інформації і кодування", callback_data="tikUi2")
networkUi2 = InlineKeyboardButton(text="Комп'ютерні мережі", callback_data="networkUi2")
teamUi2 = InlineKeyboardButton(text="Командна робота", callback_data="teamUi2")
schemeUi2 = InlineKeyboardButton(text="Схемотехніка", callback_data="schemeUi2")

lessonsMenuUi = InlineKeyboardMarkup(row_width=1)
ui_defInfo = InlineKeyboardButton(text="Методи та засоби захисту інформації", callback_data="ui_defInfo")
ui_crypto = InlineKeyboardButton(text="Криптографічні системи та протоколи", callback_data="ui_crypto")
ui_arch = InlineKeyboardButton(text="Архітектура комп`ютерних систем", callback_data="ui_arch")
ui_tools = InlineKeyboardButton(text="Засоби приймання,передавання та обробки інформації в системах технічного захисту інформації", callback_data="ui_tools")
ui_safety = InlineKeyboardButton(text="Безпека інфраструктури комп`ютерних мереж", callback_data="ui_safety")

lessonsMenu2Bit = InlineKeyboardMarkup(row_width=1)
tikBit2 = InlineKeyboardButton(text="Теорія інформації і кодування", callback_data="tikBit2")
networkBit2 = InlineKeyboardButton(text="Комп'ютерні мережі", callback_data="networkBit2")
schemeBit2 = InlineKeyboardButton(text="Схемотехніка", callback_data="schemeBit2")
philosophyBit2 = InlineKeyboardButton(text="Філософія", callback_data="philosophyBit2")

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

lessonsMenu2Zi.insert(networkZi2)
lessonsMenu2Zi.insert(tikZi2)
lessonsMenu2Zi.insert(metrologyZi2)
lessonsMenu2Zi.insert(schemeZi2)
lessonsMenu2Zi.insert(btnBack)


lessonsMenuZi.insert(incidentResponse)
lessonsMenuZi.insert(methodsDefense)
lessonsMenuZi.insert(workDef)
lessonsMenuZi.insert(zi_architecture)
lessonsMenuZi.insert(it_tech)
lessonsMenuZi.insert(zi_predictions)
lessonsMenuZi.insert(btnBack)

lessonsMenu2Ack.insert(tikAck2)
lessonsMenu2Ack.insert(teamAck2)
lessonsMenu2Ack.insert(networkAck2)
lessonsMenu2Ack.insert(schemeAck2)
lessonsMenu2Ack.insert(philosophyAck2)
lessonsMenu2Ack.insert(btnBack)

lessonsMenuAck.insert(incidentResponse_ack)
lessonsMenuAck.insert(defTool)
lessonsMenuAck.insert(ack_workDef)
lessonsMenuAck.insert(ack_architecture)
lessonsMenuAck.insert(methodDef)
lessonsMenuAck.insert(btnBack)


lessonsMenu2Ui.insert(networkUi2)
lessonsMenu2Ui.insert(tikUi2)
lessonsMenu2Ui.insert(teamUi2)
lessonsMenu2Ui.insert(schemeUi2)
lessonsMenu2Ui.insert(btnBack)

lessonsMenuUi.insert(ui_arch)
lessonsMenuUi.insert(ui_safety)
lessonsMenuUi.insert(ui_tools)
lessonsMenuUi.insert(ui_defInfo)
lessonsMenuUi.insert(ui_crypto)
lessonsMenuUi.insert(btnBack)


lessonsMenu2Bit.insert(networkBit2)
lessonsMenu2Bit.insert(tikBit2)
lessonsMenu2Bit.insert(philosophyBit2)
lessonsMenu2Bit.insert(schemeBit2)
lessonsMenu2Bit.insert(btnBack)

lessonsMenuBit.insert(bit_incedents)
lessonsMenuBit.insert(bit_cryptology)
lessonsMenuBit.insert(bit_workDef)
lessonsMenuBit.insert(bit_methods)
lessonsMenuBit.insert(bit_arch)
lessonsMenuBit.insert(btnBack)
