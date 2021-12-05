from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


menu = InlineKeyboardButton("📝Меню", callback_data='menu')
back_from_dockb = InlineKeyboardButton("◀️Назад", callback_data='menu')
empty_kb = ReplyKeyboardRemove()
back_button = InlineKeyboardButton("◀️Назад", callback_data='back1')

profile = KeyboardButton("🤟Профиль")
document = KeyboardButton("📃Документ")
topic = KeyboardButton("🔍Искать статью")
support = KeyboardButton("☺Поддержка")
start_kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(profile).insert(document).add(topic).insert(support)

bs_item = InlineKeyboardButton("Продать/Купить товар", callback_data='bs')
rent_item = InlineKeyboardButton("Сдать/Взять в аренду", callback_data='rent')
offers = InlineKeyboardButton("Выполнение работ", callback_data='off')
doc_kb = InlineKeyboardMarkup().add(bs_item).add(rent_item).add(offers).add(back_from_dockb).insert(menu)

service = InlineKeyboardButton("Возмездное оказание услуги", callback_data='serv')
control = InlineKeyboardButton("Доверительное управление", callback_data='ctrl')
credit = InlineKeyboardButton("Заем/Кредит", callback_data='credit')
assignment = InlineKeyboardButton("Поручение", callback_data='assign')
transfer = InlineKeyboardButton("Перевозка", callback_data='trans')
keep = InlineKeyboardButton("Хранение", callback_data='keep')
contract = InlineKeyboardButton("Подряд", callback_data='contract')
contract_kb = InlineKeyboardMarkup().add(service).add(control).add(credit).add(assignment).insert(transfer).add(keep).insert(contract).add(back_button).insert(menu)

doc_rent = InlineKeyboardButton("Договор Ренты", callback_data='doc_rent')
doc_arenda = InlineKeyboardButton("Договор Аренды", callback_data='doc_arenda')
doc_assign = InlineKeyboardButton("Договор поручения", callback_data='doc_assign')
choose_doc = InlineKeyboardMarkup().add(doc_rent).add(doc_arenda).add(doc_assign).add(back_button).insert(menu)
