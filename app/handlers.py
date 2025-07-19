from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from study_plans import get_plan
from recommendations import get_recommendations


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("AI", callback_data="program_ai")],
        [InlineKeyboardButton("AI Product", callback_data="program_ai_product")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Выбери магистерскую программу:",
        reply_markup=reply_markup
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("program_"):
        program_key = data.split("_")[1]
        plan = get_plan(program_key)
        if not plan:
            await query.edit_message_text("Информация по этой программе пока недоступна.")
            return

        text = f"Описание программы:\n{plan['description']}\n\nКурсы:\n" + "\n".join(f"- {course}" for course in plan["courses"])

        keyboard = [
            [InlineKeyboardButton("Рекомендации по выборным дисциплинам", callback_data=f"rec_{program_key}")],
            [InlineKeyboardButton("Вернуться к выбору программы", callback_data="back_to_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text=text, reply_markup=reply_markup)

    elif data.startswith("rec_"):
        program_key = data.split("_")[1]
        rec = get_recommendations(program_key)

        keyboard = [
            [InlineKeyboardButton("Вернуться к программе", callback_data=f"program_{program_key}")],
            [InlineKeyboardButton("Вернуться к выбору программы", callback_data="back_to_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text=f"Рекомендации по выборным дисциплинам:\n{rec}", reply_markup=reply_markup)

    elif data == "back_to_menu":
        keyboard = [
            [InlineKeyboardButton("AI", callback_data="program_ai")],
            [InlineKeyboardButton("AI Product", callback_data="program_ai_product")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Выбери магистерскую программу:", reply_markup=reply_markup)
