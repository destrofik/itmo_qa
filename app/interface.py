from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


async def main_keyboard():

    kb_list = [
        [KeyboardButton(text="О нас"), KeyboardButton(text="Профиль")],
        [KeyboardButton(text="Программы"), KeyboardButton(text="Контакты")]
    ]

    kb = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Воспользуйтесь меню:"
    )

    return kb



async def profile_keyboard():

    profile_list = [
        [KeyboardButton(text='Посмотреть профиль'), KeyboardButton(text="Редактировать профиль")],
        [KeyboardButton(text="В главное меню")]
    ]

    profile_kb = ReplyKeyboardMarkup(  # Corrected indentation here
        keyboard=profile_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Профиль:"
    )

    return profile_kb

async def edit_keyboard():

    edit_list = [
        [KeyboardButton(text='ФИО'), KeyboardButton(text="Программа обучения")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="В главное меню")]
    ]

    edit_kb = ReplyKeyboardMarkup(  # Corrected indentation here
        keyboard=edit_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Редактировать"
    )

    return edit_kb


async def call_manager_support():
    buttons_list = [
        [InlineKeyboardButton(text="Поддержка", url='https://t.me/destrofikk')],
        [InlineKeyboardButton(text="ИТМО", web_app=WebAppInfo(url='https://abit.itmo.ru/program/master/ai'))]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons_list, row_width=1)

    return keyboard

def get_pagination_keyboard(page: int, total_pages: int):
    buttons_list = [
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="prev_page"),
         InlineKeyboardButton(text=f"Стр {page}/{total_pages}", callback_data="current_page"),
         InlineKeyboardButton(text="➡️ Вперёд", callback_data="next_page")]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons_list, row_width=1)
    return keyboard
