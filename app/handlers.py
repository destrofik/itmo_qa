from telegram import Update, ForceReply
from telegram.ext import ContextTypes
from study_plans import get_plan
from recommendations import get_recommendations

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет, {user.mention_html()}! Я помогу выбрать магистерскую программу ITMO.\n"
        "Напиши название программы (ai или ai_product), чтобы узнать учебный план.\n"
        "Или задай вопросы по обучению."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Напиши 'ai' или 'ai_product' для описания программы.\n"
        "Также можешь спросить про рекомендации по выборным дисциплинам."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # Проверяем, есть ли упоминание программ
    if text in ("ai", "ai_product"):
        plan = get_plan(text)
        if plan:
            msg = f"Описание программы:\n{plan['description']}\n\nКурсы:\n" + "\n".join(f"- {c}" for c in plan["courses"])
            await update.message.reply_text(msg)
        else:
            await update.message.reply_text("Извините, информация по этой программе пока недоступна.")
        return

    # Обработка рекомендаций (примитивно)
    if "рекомендации" in text or "выборные" in text:
        # Можно расширить: парсить background из контекста или отдельной команды
        program_key = None
        # Ищем упоминание программы в сообщении
        for p in ("ai", "ai_product"):
            if p in text:
                program_key = p
                break

        rec = get_recommendations(program_key or "ai", background=None)
        await update.message.reply_text(f"Рекомендации:\n{rec}")
        return

    await update.message.reply_text("Извините, я пока могу помочь только с информацией о 'ai' и 'ai_product'.")
