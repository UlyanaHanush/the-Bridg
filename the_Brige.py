import telebot
from telebot import types

token = '5408994306:AAHp9oVwb8NemrzFSPMixmEAlivwcbc0DNs'
bot = telebot.TeleBot(token)

# кнопки
but_1 = types.InlineKeyboardButton(text="Меню... заведения", callback_data="Меню... заведения")
but_2 = types.InlineKeyboardButton(text="Бронирование столика", callback_data="Бронирование столика")
but_3 = types.InlineKeyboardButton(text="Отзывы и контакты", callback_data="Отзывы и контакты")
but_4 = types.InlineKeyboardButton(text="Горячие напитки", callback_data="Горячие напитки")
but_5 = types.InlineKeyboardButton(text="Французская выпечка", callback_data="Французская выпечка")
but_6 = types.InlineKeyboardButton(text="Десерты", callback_data="Десерты")
but_today = types.InlineKeyboardButton(text="Сегодня", callback_data="Сегодня")
but_tomorrow = types.InlineKeyboardButton(text="Заврта", callback_data="Заврта")
but_day_after_tomorrow = types.InlineKeyboardButton(text="Послезавтра", callback_data="Послезавтра")
time_18 = types.InlineKeyboardButton(text="18:00", callback_data="18:00")
time_19 = types.InlineKeyboardButton(text="19:00", callback_data="19:00")
time_20 = types.InlineKeyboardButton(text="20:00", callback_data="20:00")
time_21 = types.InlineKeyboardButton(text="21:00", callback_data="21:00")
time_22 = types.InlineKeyboardButton(text="22:00", callback_data="22:00")
time_23 = types.InlineKeyboardButton(text="23:00", callback_data="23:00")
but_org = types.InlineKeyboardButton(text="Связаться с организатором", url="https://t.me/Ulyasha_Hanush")
but_back_main = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="Вернуться в главное меню")
but_review = types.InlineKeyboardButton(text="Ознакомиться с нашими отзывами",
                                        callback_data="Ознакомиться с нашими отзывами")
but_7 = types.InlineKeyboardButton(text="Круассаны", callback_data="Круассаны")
but_8 = types.InlineKeyboardButton(text="Макароны", callback_data="Макароны")
but_9 = types.InlineKeyboardButton(text="Эклеры", callback_data="Эклеры")
but_10 = types.InlineKeyboardButton(text="Мороженное", callback_data="Мороженное")
but_11 = types.InlineKeyboardButton(text="Блины", callback_data="Блины")

# массив кнопок
key_main_menu = types.InlineKeyboardMarkup(row_width=1)
key_menu = types.InlineKeyboardMarkup(row_width=1)
key_date = types.InlineKeyboardMarkup(row_width=3)
key_time = types.InlineKeyboardMarkup(row_width=6)
key_org = types.InlineKeyboardMarkup(row_width=1)
key_coffee_start = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
key_back_main = types.InlineKeyboardMarkup(row_width=1)
key_baking = types.InlineKeyboardMarkup(row_width=1)
key_desert = types.InlineKeyboardMarkup(row_width=1)

# добавление кнопок в массив
key_main_menu.add(but_1, but_2, but_3)
key_menu.add(but_4, but_5, but_6, but_back_main)
key_date.add(but_today, but_tomorrow, but_day_after_tomorrow, but_back_main)
key_time.add(time_18, time_19, time_20, time_21, time_22, time_23, but_back_main)
key_org.add(but_org, but_review)
key_coffee_start.row('Выбрать кофе', 'Помощь')
key_back_main.add(but_back_main)
key_baking.add(but_7, but_9, but_8, but_back_main)
key_desert.add(but_10, but_11), but_back_main

booking = []
coffee = []
review_user = []


# приветствие бота
@bot.message_handler(commands=["start"])
def inline(message):
    bot.send_message(message.chat.id, 'Добро пожаловать Под Бруклинский мост )))')
    bot.send_photo(message.chat.id, photo=open('img/Plesk.jpg', 'rb'), reply_markup=key_main_menu)


# проверка набора кнопок по запросу usera
@bot.callback_query_handler(func=lambda c: True)
def food(c):
    if c.data == "Меню... заведения":
        bot.send_photo(c.message.chat.id, photo=open('img/cafe.jpg', 'rb'), reply_markup=key_menu)
    elif c.data == "Горячие напитки":
        bot.send_message(c.message.chat.id, 'Смешав базовую Бразилию с насыщенной и яркой Колумбией Киндио,'
                                            'двумя самыми знаменитыми регионами Эфиопии — Иргачиф и Сидамо'
                                            'мы добились яркого с цветочным нотами аромата, богатого вкуса какао,'
                                            'орехов, с нотами сладкого цитруса и красных ягод.',
                         reply_markup=key_coffee_start)
    elif c.data == "Французская выпечка":
        bot.send_photo(c.message.chat.id, photo=open('img/Franc_cake.jpg', 'rb'))
        bot.send_message(c.message.chat.id, 'Мы печем для Вас каждое утро', reply_markup=key_baking)
    elif c.data == "Круассаны":
        bot.send_photo(c.message.chat.id, photo=open('img/Croissant.jpg', 'rb'))
        bot.send_message(c.message.chat.id, 'Свежий, сливочный и очень вкусный — круассан'
                                            'от пекарни Дражина именно такой!'
                                            'Особенность продукции нашей пекарни — оригинальные рецепты,'
                                            'тонкая ручная работа и полностью натуральный состав.'
                                            'Мы выпекаем круассаны в течение всего дня и продаём'
                                            'исключительно день в день', reply_markup=key_back_main)
    elif c.data == "Макароны":
        bot.send_photo(c.message.chat.id, photo=open('img/Makaronikowe.jpg', 'rb'))
        bot.send_message(c.message.chat.id, 'Макаронс - нежный и очень воздушных десерт, обожаемый во всём мире.'
                                            'Визуально эти пирожные похожи на маленькие гамбургеры.'
                                            'Два круглых бисквита, скреплённые кремом или джемом.'
                                            'Сам десерт может быть любого цвета. Каждый макаронс имеет свой особенный,'
                                            'неповторимый вкус, включая необычные сочетания, такие как:'
                                            'клубника с базиликом, карамель с морской солью, облепиха с розмарином.'
                                            'Бывают даже экстравагантные пирожные со вкусом голубого сыра'
                                            'или чая Эрл Грей.', reply_markup=key_back_main)
    elif c.data == "Эклеры":
        bot.send_photo(c.message.chat.id, photo=open('img/ecler.jpg', 'rb'))
        bot.send_message(c.message.chat.id, 'Ванильный эклер из заварного теста наполнен масляным кремом'
                                            'на основе сливочного масла с добавлением заварного крема,'
                                            'верхняя поверхность покрыта помадкой сахарной белой.',
                         reply_markup=key_back_main)
    elif c.data == "Десерты":
        bot.send_photo(c.message.chat.id, photo=open('img/desert.jpg', 'rb'))
        bot.send_message(c.message.chat.id, 'Частичка души в каждом рецепте', reply_markup=key_desert)
    elif c.data == "Мороженное":
        bot.send_photo(c.message.chat.id, photo=open('img/ice_cream.jpg', 'rb'))
        bot.send_message(c.message.chat.id, 'Перед вами настоящая палитра вкусов: йогурт с лесными ягодами,'
                                            'печеная слива, соленая карамель, тыква с корицей, джандуйя,'
                                            'клубника и розовый перец, мусковадо, глазированный каштан,'
                                            'шафран и ваниль…Выбирать между сочными или сливочными джелато,'
                                            'освежающими гранитами и нежными семифреддо совершенно невозможно.',
                         reply_markup=key_back_main)
    elif c.data == "Блины":
        bot.send_photo(c.message.chat.id, photo=open('img/pancakes.jpg', 'rb'))
        bot.send_message(c.message.chat.id, 'Блины на кефире и молоке, запеченные с миндальным кремом, —'
                                            'это уже не просто блюдо масленичного меню, а восхитительный десерт,'
                                            'который можно подать по любому поводу. Великолепные вкусовые впечатления'
                                            'гарантированы! Благодаря присутствию в тесте кисломолочного продукта,'
                                            'блины получаются очень нежными и прекрасно пропитываются кремом. А'
                                            'запекание идеально завершает дело,обеспечивая десерту хрустящую корочку.',
                         reply_markup=key_back_main)

    elif c.data == "Вернуться в главное меню":
        bot.send_photo(c.message.chat.id,
                       photo=open('img/Plesk.jpg', 'rb'),
                       reply_markup=key_main_menu)
    elif c.data == "Бронирование столика":
        bot.send_message(c.message.chat.id, 'Карта нашего заведения\n')
        bot.send_photo(c.message.chat.id, photo=open('img/plan_cafe.jpg', 'rb'))
        msg = bot.send_message(c.message.chat.id, 'Выберите подходящий столик и напишите нам какой: ')
        bot.register_next_step_handler(msg, table_bron)
    elif c.data in ["Сегодня", "Заврта", "Послезавтра"]:
        bot.send_photo(c.message.chat.id, photo=open('img/clock.jpg', 'rb'))
        bot.send_message(c.message.chat.id, 'Выберите время', reply_markup=key_time)
        booking.append(c.data)
    elif c.data in ["18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]:
        booking.append(c.data)
        bot.send_message(c.message.chat.id, f"Забронировали для Вас столик №{' '.join(booking)}")
        booking.clear()
    elif c.data == "Отзывы и контакты":
        bot.send_location(c.message.chat.id, latitude=53.85167483163817, longitude=27.439326399999995)
        bot.send_message(c.message.chat.id, 'Время работы:\nПн-Пт: 18:00 - 01:00\nСб-Вс: 19:00 - 02:00\n'
                                            'Адрес: ул. Громова, 44\n'
                                            'Телефон: +375-29-804-37-53', reply_markup=key_org)
        msge = bot.send_message(c.message.chat.id, 'Оставьте ваш отзыв')
        bot.register_next_step_handler(msge, review)
    elif c.data == "Ознакомиться с нашими отзывами":
        bot.send_message(c.message.chat.id, f"{' '.join(review_user)}", reply_markup=key_back_main)


def table_bron(message):
    bot.send_photo(message.chat.id, photo=open('img/calendar.jpg', 'rb'))
    bot.send_message(message.chat.id, 'Прекрасный выбор\n Выберите день', reply_markup=key_date)
    booking.append(message.text)


def review(message):
    bot.send_message(message.chat.id, "спасибо что оставили отзыв", reply_markup=key_back_main)
    review_user.append(message.text + '\n\n')


# набор кнопок для кофе
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Выбрать кофе":
        coffee_selection = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        coffee_selection.row('Латте', 'Капучино', 'Американо')
        bot.send_message(message.from_user.id, 'У нас лучшие сорта кофе ', reply_markup=coffee_selection)
    elif message.text == "Латте" or message.text == "Капучино" or message.text == "Американо":
        coffee_selection = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        coffee_selection.row('0,2', '0,3', '0,5')
        bot.send_message(message.from_user.id, 'Выберите объем', reply_markup=coffee_selection)
        coffee.append(message.text)
    elif message.text == "0,2" or message.text == "0,3" or message.text == "0,5":
        coffee_selection = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        coffee_selection.row('Да, оплатить заказ', 'Нет, хочу поменять заказ')
        coffee.append(message.text)
        bot.send_message(message.from_user.id, f"Ваш заказ: кофе ☕ {' '.join(coffee)} мл?",
                         reply_markup=coffee_selection)
    elif message.text == "Да, оплатить заказ":
        coffee_selection = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        coffee_selection.row('Вернуться к меню', 'Нет, хочу поменять заказ')
        bot.send_message(message.from_user.id,
                         'Отправьте деньги на этот ulyana-кошелек:' + '0x7861D09Eb3A1bBBd9Ff493dcF8d2ded089144c39',
                         reply_markup=coffee_selection)
    elif message.text == "Вернуться к меню":
        bot.send_message(message.from_user.id, 'Спасибо за оплату', reply_markup=key_main_menu)
    elif message.text == "Нет, хочу поменять заказ":
        coffee_selection = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        coffee.clear()
        coffee_selection.row('Выбрать кофе')
        bot.send_message(message.from_user.id, 'Вперед за новым выбором', reply_markup=coffee_selection)
    elif message.text == "Помощь":
        bot.send_message(message.from_user.id, 'Не волнуйся, здесь тебе подскажут. Это наш помощник. Вперед по ссылке ',
                         reply_markup=key_org)
        bot.send_message(message.from_user.id, 'Надеемся, что все вопросы решены',
                         reply_markup=key_back_main)
    else:
        print("Ваш запрос не распознан")


bot.polling(none_stop=True, interval=0)
